# /ui/main_window.py
import os
import sys
import re
from functools import partial
from typing import Optional, List, cast, Dict
from PyQt6.QtCore import (Qt, pyqtSignal, QTimer, QSize, QUrl, QObject, QRunnable, QThreadPool, QEvent, QPoint,
                          QPropertyAnimation, QEasingCurve, QRect, QByteArray)
from PyQt6.QtGui import (QKeySequence, QAction, QCloseEvent, QDesktopServices, QIcon, QActionGroup, QDragEnterEvent,
                         QDropEvent, QTextDocument, QResizeEvent, QMouseEvent)
from PyQt6.QtWidgets import (QMessageBox, QMenu, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow, QStatusBar,
                             QTabWidget, QLabel, QToolButton, QToolBar, QSizePolicy, QApplication, QFileDialog,
                             QDockWidget, QComboBox,
                             QProgressDialog, QPushButton, QInputDialog, QProgressBar)

import qtawesome as qta

# Import managers by class, not instance
from app_core.config import GITHUB_REPO_URL
from app_core.settings_manager import SettingsManager
from app_core.theme_manager import ThemeManager
from app_core.file_handler import FileHandler
from app_core.completion_manager import CompletionManager
from app_core.github_manager import GitHubManager
from app_core.koromali_api import KoromaliPluginAPI
from app_core.linter_manager import LinterManager
from app_core.plugin_manager import PluginManager
from app_core.project_manager import ProjectManager
from app_core.source_control_manager import SourceControlManager
from app_core.update_manager import UpdateManager
from app_core.syntax_highlighters import *
from ui.editor_widget import EditorWidget, HighlightManager, MiniMapWidget
from ui.widgets.advanced_minimap import AdvancedMinimap
from ui.explorer.list_view_widget import FileSystemListView
from ui.preferences_dialog import PreferencesDialog
from ui.widgets.draggable_tab_widget import DraggableTabWidget
from ui.widgets.problems_panel import ProblemsPanel
from ui.widgets.source_control_panel import ProjectSourceControlPanel
from ui.widgets.splash_screen import SplashScreen
from ui.widgets.add_panel_popup import AddPanelPopup
from ui.widgets.widget_hider import WidgetHiderManager, HIDER_WIDGET_MIME_TYPE
from ui.widgets.large_file_viewer_widget import LargeFileViewerWidget
from utils import versioning, helpers
from utils.logger import log


class ClosableDockWidget(QDockWidget):
    """A QDockWidget that intercepts its close event to hide instead."""
    def __init__(self, title, main_window_ref):
        super().__init__(title, main_window_ref)
        self.main_window_ref = main_window_ref

    def closeEvent(self, event: QCloseEvent):
        """Overrides the close event to just hide the widget."""
        self.setVisible(False)
        event.ignore()


class MainWindow(QMainWindow):
    untitled_file_counter, _is_app_closing = 0, False
    theme_changed_signal = pyqtSignal(str)
    project_find_requested = pyqtSignal(str, object)
    project_replace_requested = pyqtSignal(str, str, object)
    COMMENT_MAP = {'.py': '#', '.js': '//', '.ts': '//', '.cs': '//', '.java': '//', '.go': '//', '.rs': '//',
                   '.c': '//', '.cpp': '//', '.h': '//', '.hpp': '//', '.css': '/*', '.html': '<!--'}
    END_COMMENT_MAP = {'/*': '*/', '<!--': '-->'}

    def __init__(self, file_handler: FileHandler, theme_manager: ThemeManager, 
                 settings_manager: SettingsManager, debug_mode=False, parent=None):
        super().__init__(parent)
        log.info("MainWindow __init__ started.")

        self.file_handler = file_handler
        self.theme_manager = theme_manager
        self.settings = settings_manager
        self.debug_mode = debug_mode
        self.file_handler.parent_window = self
        self.preferences_dialog, self.threadpool = None, QThreadPool()
        self.last_active_project_path = None
        self.progress_bars: Dict[str, QProgressBar] = {}
        
        self.setMouseTracking(True)
        self._last_hover_edge = None
        self.shared_paths = set()

        self._initialize_managers()
        self.koromali_api = KoromaliPluginAPI(self)
        self.koromali_api.highlight_manager = self.highlight_manager
        self.koromali_api.project_lock_requested.connect(self._handle_project_lock)
        log.info("MainWindow connected to project lock signals from API.")
        
        self.encoding_map = {"UTF-8": "utf-8", "UTF-8-SIG": "utf-8-sig", "UTF-16 LE": "utf-16le",
                             "UTF-16 BE": "utf-16be", "Latin-1": "latin-1", "Windows-1252": "cp1252"}
        self.reverse_encoding_map = {v: k for k, v in self.encoding_map.items()}
        self._register_built_in_highlighters()
        self.plugin_manager = PluginManager(self)
        self.setWindowTitle(f"koromali - v{versioning.APP_VERSION}")
        self._load_window_geometry()
        self._create_core_widgets()
        
        self.hider_manager = WidgetHiderManager(self)
        
        self._create_core_actions()
        self._create_core_menu()
        self._create_toolbar()
        self._create_tools_dock_widget()
        self._create_layout()
        self._create_statusbar()
        self._integrate_file_explorer()
        self._integrate_linter_ui()
        self._integrate_source_control_ui()
        self._integrate_global_drag_drop()
        self._connect_signals()
        
        self.installEventFilter(self)

        log.info("MainWindow __init__ has completed. Waiting for finalization signal.")
        
    def set_shared_paths(self, paths: list):
        """Updates the set of paths being shared in a collaboration session."""
        self.shared_paths = {os.path.normpath(p) for p in paths}
        log.info(f"Shared paths updated: {self.shared_paths}")
        if hasattr(self, 'explorer_panel') and self.explorer_panel:
            self.explorer_panel.refresh()

    def get_shared_paths(self) -> set:
        """Gets the set of currently shared paths."""
        return self.shared_paths
        
    def _handle_project_lock(self, project_path: str, should_lock: bool):
        """Slot to handle requests from plugins to lock/unlock a project in the explorer."""
        if hasattr(self, 'explorer_panel') and self.explorer_panel:
            self.explorer_panel.set_project_enabled(project_path, not should_lock)
            log.info(f"Project '{os.path.basename(project_path)}' in explorer set to enabled: {not should_lock}")

    def leaveEvent(self, event: QEvent):
        """Hides any visible hider buttons when the mouse leaves the window."""
        if hasattr(self, 'hider_manager') and self._last_hover_edge:
            self.hider_manager.animate_edge(self._last_hover_edge, show=False)
            self._last_hover_edge = None
        super().leaveEvent(event)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj is self:
            if event.type() in [QEvent.Type.Resize, QEvent.Type.Move]:
                if hasattr(self, 'hider_manager'):
                    QTimer.singleShot(10, self.hider_manager.update_hider_positions)
            
            elif event.type() == QEvent.Type.MouseMove:
                if hasattr(self, 'hider_manager'):
                    pos = event.pos()
                    margin = 8  # Increased margin for easier activation
                    
                    hot_edge = None
                    # Get heights of bars, defaulting to 0 if they don't exist or are hidden
                    menu_bar_h = self.menuBar().height() if self.menuBar() and self.menuBar().isVisible() else 0
                    status_bar_h = self.statusBar().height() if self.statusBar() and self.statusBar().isVisible() else 0
                    
                    if 0 <= pos.x() < margin:
                        hot_edge = 'left'
                    elif self.width() - margin < pos.x() <= self.width():
                        hot_edge = 'right'
                    elif menu_bar_h <= pos.y() < menu_bar_h + margin:
                        hot_edge = 'top'
                    elif self.height() - status_bar_h - margin < pos.y() <= self.height() - status_bar_h:
                        hot_edge = 'bottom'

                    if self._last_hover_edge != hot_edge:
                        if self._last_hover_edge:
                            self.hider_manager.animate_edge(self._last_hover_edge, show=False)
                        if hot_edge:
                            self.hider_manager.animate_edge(hot_edge, show=True)
                        self._last_hover_edge = hot_edge
        
        return super().eventFilter(obj, event)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasFormat(HIDER_WIDGET_MIME_TYPE) or event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            for url in mime_data.urls():
                if url.isLocalFile():
                    self._action_open_file(url.toLocalFile())
            event.acceptProposedAction()
        elif mime_data.hasFormat(HIDER_WIDGET_MIME_TYPE):
            widget_id_bytes = mime_data.data(HIDER_WIDGET_MIME_TYPE)
            widget_id = int(widget_id_bytes.data().decode())
            
            widget_to_show = None
            for widget in self.hider_manager.managed_widgets:
                if id(widget) == widget_id:
                    widget_to_show = widget
                    break
            
            if widget_to_show:
                widget_to_show.setFloating(True)
                widget_to_show.move(event.position().toPoint())
                widget_to_show.show()
                widget_to_show.raise_()
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()

    def add_dock_panel(self, panel: QWidget, title: str, area_str: str, icon_name: Optional[str] = None) -> QDockWidget:
        area = getattr(Qt.DockWidgetArea, area_str.capitalize() + "DockWidgetArea",
                       Qt.DockWidgetArea.BottomDockWidgetArea)

        if area == Qt.DockWidgetArea.BottomDockWidgetArea:
            if not hasattr(self, '_bottom_dock_widget'):
                self._bottom_dock_widget = ClosableDockWidget("Info Panels", self)
                self._bottom_dock_widget.setFeatures(
                    QDockWidget.DockWidgetFeature.DockWidgetMovable | QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetClosable)
                self._bottom_tab_widget = DraggableTabWidget(self, detachable=False)
                self._bottom_tab_widget.setDocumentMode(True)

                add_button = QToolButton()
                add_button.setIcon(qta.icon('mdi.plus'))
                add_button.setAutoRaise(True)
                add_button.clicked.connect(self._show_add_panel_popup)
                self._bottom_tab_widget.setCornerWidget(add_button, Qt.Corner.TopRightCorner)
                
                self._bottom_tab_widget.setTabsClosable(True)
                self._bottom_tab_widget.tabCloseRequested.connect(self._close_info_panel_tab)
                self._bottom_tab_widget.close_tab_requested.connect(self._close_info_panel_tab)

                self._bottom_dock_widget.setWidget(self._bottom_tab_widget)
                self.addDockWidget(area, self._bottom_dock_widget)
                
                self.hider_manager.register_widget(self._bottom_dock_widget, area)
                self.docks_menu.addAction(self._bottom_dock_widget.toggleViewAction())

            for i in range(self._bottom_tab_widget.count()):
                if self._bottom_tab_widget.widget(i) == panel:
                    return self._bottom_dock_widget

            icon = qta.icon(icon_name) if icon_name else QIcon()
            self._bottom_tab_widget.addTab(panel, icon, title)
            return self._bottom_dock_widget

        dock = ClosableDockWidget(title, self)
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable | QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetClosable)
        dock.setWidget(panel)
        self.addDockWidget(area, dock)

        self.hider_manager.register_widget(dock, area)
        self.docks_menu.addAction(dock.toggleViewAction())
        return dock
    
    def register_toolbar(self, toolbar: QToolBar, area=Qt.ToolBarArea.TopToolBarArea):
        log.info(f"Registering toolbar from plugin: {toolbar.windowTitle()}")
        self.addToolBar(area, toolbar)
        if hasattr(self, 'hider_manager'):
            self.hider_manager.register_widget(toolbar, area)

        if hasattr(self, 'toolbars_menu'):
            self.toolbars_menu.addAction(toolbar.toggleViewAction())
        else:
            log.warning("Could not add toolbar toggle action because 'toolbars_menu' does not exist.")
            self.view_menu.addAction(toolbar.toggleViewAction())

    def register_progress_bar(self, task_id: str, description: str):
        if task_id in self.progress_bars: self.hide_progress_bar(task_id)
        progress_bar = QProgressBar(); progress_bar.setToolTip(description)
        progress_bar.setTextVisible(False); progress_bar.setMaximumHeight(16)
        self.statusBar().addPermanentWidget(progress_bar, 1)
        self.progress_bars[task_id] = progress_bar; progress_bar.show()

    def update_progress_bar(self, task_id: str, value: int, max_value: int):
        if progress_bar := self.progress_bars.get(task_id):
            if progress_bar.maximum() != max_value: progress_bar.setRange(0, max_value)
            progress_bar.setValue(value)

    def hide_progress_bar(self, task_id: str):
        if progress_bar := self.progress_bars.pop(task_id, None):
            self.statusBar().removeWidget(progress_bar); progress_bar.deleteLater()

    def finalize_and_show(self, splash: Optional[QWidget] = None):
        log.info("Finalizing startup and showing MainWindow.")
        self.show()
        if splash:
            log.debug("Splash screen is present. Starting fade-out.")
            splash.finish()
            QTimer.singleShot(500, lambda: self.set_quit_on_last_window_closed(True))
        else:
            self.set_quit_on_last_window_closed(True)
        QTimer.singleShot(100, self._deferred_initialization)
        log.info("MainWindow is now visible and deferred initialization is scheduled.")

    def set_quit_on_last_window_closed(self, enabled: bool):
        QApplication.instance().setQuitOnLastWindowClosed(enabled)
        log.info(f"Application 'QuitOnLastWindowClosed' set to {enabled}.")

    def _deferred_initialization(self):
        log.info("Starting deferred initialization...")
        self._apply_theme_and_icons(self.settings.get("last_theme_id"))
        plugins_to_ignore = ['enhanced_exceptions'] if self.debug_mode else []
        if self.debug_mode:
            try:
                from core_debug_tools.enhanced_exceptions.plugin_main import initialize as init_eh
                self.eh_instance = init_eh(self.koromali_api, sys.excepthook)
            except Exception as e:
                log.error(f"Failed to load core exception handler: {e}", exc_info=True)
        self.plugin_manager.discover_and_load_plugins(ignore_list=plugins_to_ignore)

        self.last_active_project_path = self.project_manager.get_active_project_path()
        self._load_project_session(self.last_active_project_path)

        self._post_init_setup()
        log.info("Deferred initialization complete.")

    def _post_init_setup(self):
        self._update_recent_files_menu()
        self._update_window_title()
        if not self.tab_widget.count():
            self._add_new_tab(is_placeholder=True)

    def _register_built_in_highlighters(self):
        log.info("Registering syntax highlighters.")
        [self.koromali_api.register_highlighter(ext, hc) for ext, hc in
         {'.py': PythonSyntaxHighlighter, '.pyw': PythonSyntaxHighlighter, '.json': JsonSyntaxHighlighter,
          '.html': HtmlSyntaxHighlighter, '.css': CssSyntaxHighlighter, '.js': JavaScriptSyntaxHighlighter,
          '.rs': RustSyntaxHighlighter, '.c': CppSyntaxHighlighter, '.cpp': CppSyntaxHighlighter, '.h': CppSyntaxHighlighter,
          '.hpp': CppSyntaxHighlighter, '.cs': CSharpSyntaxHighlighter}.items()]

    def _initialize_managers(self):
        # Now these managers are created with dependencies injected
        self.project_manager = ProjectManager(self.settings)
        self.highlight_manager = HighlightManager()
        self.completion_manager = CompletionManager(self.settings, self.theme_manager, self)
        self.github_manager = GitHubManager(self.settings, self)
        self.git_manager = SourceControlManager(self)
        self.linter_manager = LinterManager(self)
        self.update_manager = UpdateManager(self.settings, self)
        
        self.actions, self.editor_tabs_data, self.file_open_handlers = {}, {}, {}
        self.lint_timer = QTimer(self)
        self.lint_timer.setSingleShot(True)
        self.lint_timer.setInterval(1500)
        self.auto_save_timer = QTimer(self)
        self.auto_save_timer.setSingleShot(True)
        self.draft_save_timer = QTimer(self)
        self.draft_save_timer.setSingleShot(True)
        self.draft_save_timer.setInterval(2000)

    def _add_new_tab(self, filepath=None, content="", encoding='utf-8', is_placeholder=False):
        if is_placeholder:
            if self.tab_widget.count() > 0:
                return
            self.tab_widget.addTab(QLabel("Open a file or project...", alignment=Qt.AlignmentFlag.AlignCenter),
                                   "Welcome")
            self.tab_widget.setTabsClosable(False)
            return
        if self.tab_widget.count() == 1 and isinstance(self.tab_widget.widget(0), QLabel):
            self.tab_widget.removeTab(0)

        new_widget = self._create_standard_editor(filepath, content, encoding)
        if new_widget:
            name = os.path.basename(filepath or f"Untitled-{self.untitled_file_counter + 1}")
            self.untitled_file_counter += 1 if not filepath else 0
            idx = self.tab_widget.addTab(new_widget, name)
            self.tab_widget.setTabToolTip(idx, filepath or f"Unsaved {name}")
            self.tab_widget.setCurrentWidget(new_widget)
            new_widget.text_area.setFocus()
        else:
            log.critical("Failed to create standard editor from _add_new_tab.")

    def _load_window_geometry(self):
        self.resize(QSize(*self.settings.get("window_size", [1600, 1000])))
        pos = self.settings.get("window_position")
        if pos:
            self.move(*pos)

    def _create_core_actions(self):
        am = {"new_file": ("&New File", lambda: self._add_new_tab(is_placeholder=False), "Ctrl+N", 'mdi.file-outline'),
              "open_file": ("&Open File...", self._action_open_file_dialog, "Ctrl+O", 'mdi.folder-open-outline'),
              "open_folder": ("Open &Folder...", self._action_open_folder, "Ctrl+Shift+O", 'mdi.folder-outline'),
              "create_project": ("New Project...", self.action_create_new_project, "Ctrl+Shift+N", 'mdi.folder-plus-outline'),
              "close_project": ("&Close Project", self._action_close_project, None, None),
              "export_project": ("Export Project as Zip...", self._action_export_project, None, 'mdi.folder-zip-outline'),
              "save": ("&Save", self._action_save_file, "Ctrl+S", 'mdi.content-save-outline'),
              "save_as": ("Save &As...", self._action_save_as, "Ctrl+Shift+S", None),
              "save_all": ("Save A&ll", self._action_save_all, "Ctrl+Alt+S", None),
              "find_replace": ("&Find/Replace...", self.toggle_find_panel, "Ctrl+F", "mdi.magnify"),
              "preferences": ("&Preferences...", self._action_open_preferences, "Ctrl+,", 'mdi.cog-outline'),
              "exit": ("E&xit", self.close, "Ctrl+Q", None),
              "force_quit": ("&Force Quit", self._action_force_quit, "Ctrl+Shift+Q", 'mdi.alert-outline')}
        for k, p in am.items():
            a = QAction(p[0], self)
            a.triggered.connect(p[1])
            a.setData(p[3])
            if p[2]: a.setShortcut(QKeySequence(p[2]))
            self.actions[k] = a
        self.actions["find_replace"].setEnabled(False)

        edit_am = {
            "toggle_comment": ("Toggle Comment", self._action_toggle_comment, "Ctrl+/", 'fa5s.comment-slash'),
            "increase_indent": ("Increase Indent", self._action_increase_indent, "Ctrl+]", 'fa5s.indent'),
            "decrease_indent": ("Decrease Indent", self._action_decrease_indent, "Ctrl+[", 'fa5s.outdent'),
        }
        for k, p in edit_am.items():
            a = QAction(p[0], self)
            if p[1]:
                a.triggered.connect(p[1])
            if p[2]:
                a.setShortcut(QKeySequence(p[2]))
            if p[3]:
                a.setData(p[3])
            self.actions[k] = a

        a = QAction("Toggle Side Panel", self)
        a.triggered.connect(self._action_toggle_editor_side_panel)
        a.setShortcut(QKeySequence("Ctrl+B"))
        a.setData('mdi.view-split-vertical')
        self.actions["toggle_side_panel"] = a

        self.actions["run"] = QAction("Run", self)
        self.actions["run"].setData('fa5s.play')
        self.actions["run"].setToolTip("Run (F5)")
        self.actions["stop"] = QAction("Stop", self)
        self.actions["stop"].setData('fa5s.stop')
        self.actions["stop"].setToolTip("Stop Script (Ctrl+F2)")
        self.actions["stop"].setEnabled(False)

    def _get_current_editor(self) -> Optional[EditorWidget]:
        widget = self.tab_widget.currentWidget()
        return widget if isinstance(widget, EditorWidget) else None

    def _action_toggle_comment(self):
        if editor := self._get_current_editor():
            editor.toggle_comment()

    def _action_increase_indent(self):
        if editor := self._get_current_editor():
            editor.increase_indent()

    def _action_decrease_indent(self):
        if editor := self._get_current_editor():
            editor.decrease_indent()

    def _action_toggle_editor_side_panel(self):
        if editor := self._get_current_editor():
            editor.toggle_side_panel_visibility()

    def _integrate_file_explorer(self):
        d = ClosableDockWidget("Explorer", self)
        d.setWidget(FileSystemListView(self.koromali_api))
        self.explorer_panel = d.widget()
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, d)
        
        self.hider_manager.register_widget(d, Qt.DockWidgetArea.LeftDockWidgetArea)

        self.docks_menu.addAction(d.toggleViewAction())
        self.project_manager.projects_changed.connect(self._on_project_list_or_active_changed)
        QTimer.singleShot(100, self.explorer_panel.refresh)

    def _integrate_linter_ui(self):
        self.problems_panel = ProblemsPanel(self)
        self.add_dock_panel(self.problems_panel, "Problems", "bottom", "mdi.bug-outline")
        self.linter_manager.lint_results_ready.connect(self._update_problems_panel)
        self.linter_manager.error_occurred.connect(lambda err: self.problems_panel.show_info_message(f"Linter Error: {err}"))
        self.problems_panel.problem_selected.connect(self._goto_definition_result)

    def _integrate_source_control_ui(self):
        self.source_control_panel = ProjectSourceControlPanel(self.project_manager, self.git_manager,
                                                              self.github_manager, self.koromali_api, self)
        self.add_dock_panel(self.source_control_panel, "Source Control", "bottom", "mdi.git")

    def _integrate_global_drag_drop(self):
        self.setAcceptDrops(True)

    def _update_problems_panel(self, problems):
        if isinstance(editor := self.tab_widget.currentWidget(), EditorWidget) and (
        fp := self.editor_tabs_data.get(editor, {}).get('filepath')):
            self.problems_panel.update_problems({fp: problems})

    def _create_core_widgets(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setMouseTracking(True)
        self.tab_widget = DraggableTabWidget(self)
        self.tab_widget.setMouseTracking(True)
        self.tab_widget.close_all_tabs_requested.connect(self._action_close_all_tabs)
        self.tab_widget.setObjectName("MainTabWidget")

        b = QToolButton()
        b.setIcon(qta.icon('mdi.plus'))
        b.setAutoRaise(True)
        b.clicked.connect(lambda: self._add_new_tab(is_placeholder=False))
        self.tab_widget.setCornerWidget(b, Qt.Corner.TopRightCorner)

        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)

    def _create_core_menu(self):
        mb = self.menuBar()
        setattr(self, "file_menu", mb.addMenu("&File"))
        setattr(self, "edit_menu", mb.addMenu("&Edit"))
        setattr(self, "view_menu", mb.addMenu("&View"))
        setattr(self, "run_menu", mb.addMenu("&Run"))
        setattr(self, "tools_menu", mb.addMenu("&Tools"))
        setattr(self, "help_menu", mb.addMenu("&Help"))
        self.file_menu.addActions([self.actions[k] for k in ["new_file", "open_file"]])
        self.recent_files_menu = self.file_menu.addMenu("Open &Recent")
        self.file_menu.addSeparator()
        self.file_menu.addActions([self.actions[k] for k in ["create_project", "open_folder", "close_project"]])
        self.file_menu.addAction(self.actions["export_project"])
        self.file_menu.addSeparator()
        self.file_menu.addActions([self.actions[k] for k in ["save", "save_as", "save_all"]])
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.actions["preferences"])
        self.file_menu.addSeparator()
        self.file_menu.addActions([self.actions["exit"], self.actions["force_quit"]])
        self.edit_menu.addAction(self.actions["find_replace"])
        self.edit_menu.addSeparator()
        self.edit_menu.addActions([self.actions[k] for k in ["toggle_comment", "increase_indent", "decrease_indent"]])
        self.theme_menu = self.view_menu.addMenu("&Themes")
        self.toolbars_menu = self.view_menu.addMenu("Toolbars")
        self.docks_menu = self.view_menu.addMenu("Docks")
        self.view_menu.addSeparator()
        self.view_menu.addAction(self.actions["toggle_side_panel"])
        self.run_menu.addAction(self.actions["run"])
        self.run_menu.addAction(self.actions["stop"])
        self.help_menu.addAction("About Koromali", self._show_about_dialog)
        self.help_menu.addAction("View on GitHub", self._open_github_link)

    def _create_menu_button(self, primary_action, sub_actions) -> QToolButton:
        button = QToolButton(self)
        button.setDefaultAction(primary_action)
        button.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        menu = QMenu(button)
        menu.addActions(sub_actions)
        button.setMenu(menu)
        return button

    def _create_toolbar(self):
        tb = QToolBar("Main Toolbar")
        tb.setObjectName("MainToolbar")
        tb.setIconSize(QSize(18, 18))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tb)
        self.main_toolbar = tb
        self.toolbars_menu.addAction(tb.toggleViewAction())
        
        self.hider_manager.register_widget(tb, Qt.ToolBarArea.TopToolBarArea)

        tb.addAction(self.actions["new_file"])
        tb.addAction(self.actions["open_file"])
        tb.addAction(self.actions["open_folder"])
        save_button = self._create_menu_button(self.actions["save"], [self.actions["save"], self.actions["save_as"], self.actions["save_all"]])
        tb.addWidget(save_button)

    def _create_tools_dock_widget(self):
        tools_toolbar = QToolBar("Tools Toolbar")
        tools_toolbar.setIconSize(QSize(18, 18))
        
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tools_toolbar)
        self.toolbars_menu.addAction(tools_toolbar.toggleViewAction())
        self.hider_manager.register_widget(tools_toolbar, Qt.ToolBarArea.TopToolBarArea)

        tools_toolbar.addAction(self.actions["run"])
        tools_toolbar.addAction(self.actions["stop"])
        tools_toolbar.addSeparator()
        tools_toolbar.addAction(self.actions["toggle_comment"])
        tools_toolbar.addAction(self.actions["increase_indent"])
        tools_toolbar.addAction(self.actions["decrease_indent"])
        tools_toolbar.addAction(self.actions["toggle_side_panel"])
        tools_toolbar.addSeparator()
        tools_toolbar.addAction(self.actions["find_replace"])
        tools_toolbar.addSeparator()

        self.encoding_toolbar_label = QLabel(" Encoding: ")
        self.encoding_combo = QComboBox()
        self.encoding_combo.setToolTip("File Encoding")
        self.encoding_combo.setFixedWidth(150)
        [self.encoding_combo.addItem(dn, an) for dn, an in self.encoding_map.items()]
        tools_toolbar.addWidget(self.encoding_toolbar_label)
        tools_toolbar.addWidget(self.encoding_combo)
        tools_toolbar.addSeparator()
        tools_toolbar.addAction(self.actions["preferences"])

    def _create_layout(self):
        lay = QHBoxLayout(self.central_widget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.tab_widget)

    def _create_statusbar(self):
        self.setStatusBar(QStatusBar(self))
        self.char_count_label = QLabel(" Chars: 0 ")
        self.encoding_label = QLabel(" UTF-8 ")
        self.cursor_label = QLabel(" Ln 1, Col 1 ")
        self.statusBar().addPermanentWidget(self.char_count_label)
        self.statusBar().addPermanentWidget(self.encoding_label)
        self.statusBar().addPermanentWidget(self.cursor_label)

    def _connect_signals(self):
        self.tab_widget.currentChanged.connect(self._on_tab_changed)
        self.tab_widget.tabCloseRequested.connect(self._action_close_tab_by_index)
        self.lint_timer.timeout.connect(self._trigger_file_linter)
        self.completion_manager.definition_found.connect(self._goto_definition_result)
        self.auto_save_timer.timeout.connect(self._auto_save_current_tab)
        self.file_handler.recent_files_changed.connect(self._update_recent_files_menu)
        self.encoding_combo.activated.connect(self._on_encoding_changed_from_dropdown)
        self.draft_save_timer.timeout.connect(self._save_current_draft)

    def _apply_theme_and_icons(self, theme_id):
        self.theme_manager.set_theme(theme_id, QApplication.instance())
        self.theme_changed_signal.emit(theme_id)
        [act.setIcon(qta.icon(ico)) for act in self.actions.values() if (ico := act.data())]
        self._rebuild_theme_menu()
        [w.update_theme() for i in range(self.tab_widget.count()) if hasattr(w := self.tab_widget.widget(i), 'update_theme')]
        if hasattr(self, 'explorer_panel'):
            self.explorer_panel.refresh()
        if hasattr(self, 'hider_manager'):
            self.hider_manager.update_hider_positions()

    def _rebuild_theme_menu(self):
        self.theme_menu.clear()
        g = QActionGroup(self)
        g.setExclusive(True)
        for t, n in self.theme_manager.get_available_themes_for_ui().items():
            a = QAction(n, self, checkable=True, triggered=lambda _, tid=t: self._on_theme_selected(tid))
            a.setData(t)
            a.setChecked(t == self.theme_manager.current_theme_id)
            g.addAction(a)
            self.theme_menu.addAction(a)

    def _show_add_panel_popup(self):
        add_button = self.sender()
        if not add_button:
            return
        popup = AddPanelPopup(self.koromali_api, self)
        popup.panel_selected.connect(self._add_selected_panel)
        button_pos = self.mapToGlobal(add_button.pos())
        popup_pos = QPoint(button_pos.x() - popup.width() + add_button.width(), button_pos.y() + add_button.height())
        popup.move(popup_pos)
        popup.show()

    def _add_selected_panel(self, panel_id: str):
        panel_info = self.koromali_api.get_registered_panels().get(panel_id)
        if not panel_info:
            log.error(f"Attempted to add unregistered panel with ID: {panel_id}")
            return
        for i in range(self._bottom_tab_widget.count()):
            widget = self._bottom_tab_widget.widget(i)
            if isinstance(widget, panel_info['widget_class']):
                self._bottom_tab_widget.setCurrentWidget(widget)
                return
        new_panel_instance = panel_info['widget_class'](self.koromali_api)
        self.add_dock_panel(new_panel_instance, panel_info['title'], panel_info['default_area'], panel_info['icon_name'])
        self._bottom_tab_widget.setCurrentWidget(new_panel_instance)

    def _close_info_panel_tab(self, index: int):
        if hasattr(self, '_bottom_tab_widget') and 0 <= index < self._bottom_tab_widget.count():
            widget = self._bottom_tab_widget.widget(index)
            self._bottom_tab_widget.removeTab(index)
            widget.deleteLater()
            log.info(f"Closed info panel tab: {widget.windowTitle()}")

    def action_create_new_project(self):
        project_name, ok = QInputDialog.getText(self, "New Project", "Enter project name:")
        if not (ok and project_name):
            return

        projects_dir = helpers.get_projects_path()
        new_project_path = os.path.join(projects_dir, project_name)
        if os.path.exists(new_project_path):
            QMessageBox.warning(self, "Project Exists", f"A project named '{project_name}' already exists in the local workspace.")
            return

        try:
            os.makedirs(new_project_path)
            log.info(f"Created new project directory in workspace: {new_project_path}")
            self.project_manager.open_project(new_project_path)
        except OSError as e:
            QMessageBox.critical(self, "Creation Failed", f"Could not create project directory:\n{e}")
            
    def _action_open_file(self, fp: Optional[str] = None):
        if not (isinstance(fp, str) and fp): return
        np = os.path.normpath(fp)
        
        for i in range(self.tab_widget.count()):
            widget = self.tab_widget.widget(i)
            if (isinstance(widget, (EditorWidget, LargeFileViewerWidget))) and self.editor_tabs_data.get(widget, {}).get('filepath') == np:
                self.tab_widget.setCurrentWidget(widget)
                return

        try:
            if helpers.is_binary_file(np):
                QMessageBox.information(self, "Unsupported File", f"The file '{os.path.basename(np)}' is a binary or unsupported file type and cannot be opened in the editor.")
                return
            
            is_large = os.path.getsize(np) > helpers.LARGE_FILE_SIZE_BYTES
            if is_large:
                size_mb = os.path.getsize(np) / (1024 * 1024)
                reply = QMessageBox.warning(
                    self, "Large File Warning",
                    f"The file '{os.path.basename(np)}' is very large ({size_mb:.2f} MB).\n\n"
                    "Opening it may cause the application to become unresponsive. It will be opened in a performance-safe read-only mode.\n\n"
                    "Are you sure you want to continue?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.No:
                    self.statusBar().showMessage("File opening cancelled by user.", 3000)
                    return
        except (IOError, OSError) as e:
            QMessageBox.critical(self, "Error", f"Could not access file properties:\n{e}")
            return

        try:
            original_content, detected_encoding = self.file_handler._read_with_encoding_detection(np)
            if original_content is None:
                raise IOError("Could not decode the file with any of the supported encodings.")

            content = helpers.clean_git_conflict_markers(original_content)
            if content != original_content:
                log.info(f"Cleaned git conflict markers from {np} on load.")
                reply = QMessageBox.question(self, "Conflict Markers Removed",
                                             f"Git conflict markers were found and removed from '{os.path.basename(np)}'.\n\nDo you want to save these changes immediately?",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    with open(np, 'w', encoding=detected_encoding) as f:
                        f.write(content)
                    log.info(f"Saved automatically cleaned file: {np}")

        except (IOError, OSError) as e:
            msg = f"Error opening file '{os.path.basename(np)}'.\n\nReason: {e}"
            log.error(msg, exc_info=True)
            QMessageBox.critical(self, "Error", msg)
            return
            
        if is_large:
            new_widget = self._create_large_file_viewer(np, original_content)
        elif handler := self.file_open_handlers.get(os.path.splitext(np)[1].lower()):
            new_widget = handler(np, content)
        else:
            new_widget = self._create_standard_editor(np, content, detected_encoding)

        if new_widget:
            if self.tab_widget.count() == 1 and isinstance(self.tab_widget.widget(0), QLabel):
                self.tab_widget.removeTab(0)
            if self.tab_widget.indexOf(new_widget) == -1:
                icon_name = 'mdi.alert-outline' if is_large else None
                icon = qta.icon(icon_name, color='orange') if icon_name else QIcon()
                idx = self.tab_widget.addTab(new_widget, icon, os.path.basename(np))
                self.tab_widget.setTabToolTip(idx, np)
                self.tab_widget.setTabsClosable(True)
            
            self.tab_widget.setCurrentWidget(new_widget)
            if hasattr(new_widget, 'setFocus'): QTimer.singleShot(0, new_widget.setFocus)
            self.file_handler._add_to_recent_files(np)

    def _create_standard_editor(self, filepath: str, content: str, encoding: str) -> Optional[EditorWidget]:
        try:
            editor = EditorWidget(self.koromali_api)
            editor.apply_styles_and_settings()
            if highlighter_class := self.koromali_api.highlighter_map.get(os.path.splitext(filepath or "")[1].lower()):
                editor.set_highlighter(highlighter_class)
            editor.set_filepath(filepath)
            editor.set_text(content)
            file_extension = os.path.splitext(filepath)[1].lower() if filepath else ""
            minimap = AdvancedMinimap(editor, self.theme_manager, file_extension) if file_extension in AdvancedMinimap.PARSERS else MiniMapWidget(editor.text_area, self.theme_manager)
            editor.install_side_panel_widget(minimap)
            self.editor_tabs_data[editor] = {
                'filepath': filepath, 
                'original_hash': hash(content), 
                'encoding': encoding,
                'original_content_for_diff': content # For live share
            }
            editor.cursor_position_display_updated.connect(lambda l, c: self.cursor_label.setText(f" Ln {l}, Col {c} "))
            editor.content_possibly_changed.connect(partial(self._on_content_changed, editor))
            editor.status_message_requested.connect(self.statusBar().showMessage)
            editor.find_in_project_requested.connect(self.project_find_requested)
            editor.replace_in_project_requested.connect(self.project_replace_requested)
            return editor
        except Exception as e:
            log.critical(f"Failed to create standard editor tab: {e}", exc_info=True)
            QMessageBox.critical(self, "Fatal Error", f"Could not create the editor widget for the file:\n{os.path.basename(filepath)}\n\nError: {e}"); return None
            
    def _create_large_file_viewer(self, filepath: str, content: str) -> Optional[LargeFileViewerWidget]:
        try:
            viewer = LargeFileViewerWidget(self.theme_manager, self.settings)
            viewer.set_content(filepath, content)
            self.editor_tabs_data[viewer] = {'filepath': filepath, 'original_hash': hash(content), 'encoding': 'utf-8'}
            viewer.content_possibly_changed.connect(partial(self._on_content_changed, viewer))
            return viewer
        except Exception as e:
            log.critical(f"Failed to create large file viewer: {e}", exc_info=True)
            return None

    def _action_open_file_dialog(self):
        filepath = self.file_handler.open_file_dialog()
        if filepath:
            self._action_open_file(filepath)

    def _action_open_folder(self, path=None):
        path = path if path and isinstance(path, str) else QFileDialog.getExistingDirectory(self, "Open Folder", self.project_manager.get_active_project_path() or helpers.get_projects_path())
        if path: self.project_manager.open_project(path)

    def _action_close_project(self, path=None):
        self._save_current_project_session(); p = path if isinstance(path, str) else self.project_manager.get_active_project_path()
        if p: self.project_manager.close_project(p)
        else: self.statusBar().showMessage("No active project.", 2000)
        
    def _action_export_project(self):
        if not self.project_manager.is_project_open():
            self.api.show_message("info", "No Project", "Please select a project to export.")
            return

        active_path = self.project_manager.get_active_project_path()
        project_name = os.path.basename(active_path)
        
        save_path, _ = QFileDialog.getSaveFileName(self, "Export Project as Zip", f"{project_name}.zip", "Zip Archives (*.zip)")
        
        if save_path:
            success = self.project_manager.create_project_zip(save_path)
            if success:
                self.api.show_message("info", "Export Successful", f"Project '{project_name}' was successfully exported to:\n{save_path}")
            else:
                self.api.show_message("critical", "Export Failed", "Could not create the project zip archive. Check the logs for details.")

    def _on_theme_selected(self, tid):
        self.settings.set("last_theme_id", tid); self._apply_theme_and_icons(tid)

    def _on_tab_changed(self, index):
        self._update_window_title()
        w = self.tab_widget.widget(index) if index != -1 else None
        is_ed = False
        self.encoding_combo.blockSignals(True)
        if isinstance(w, (EditorWidget, LargeFileViewerWidget)):
            is_ed, d = True, self.editor_tabs_data.get(w, {})
            l, c = (1, 1) if isinstance(w, LargeFileViewerWidget) else w.get_cursor_position()
            char_count = len(w.get_text())
            self.cursor_label.setText(f" Ln {l}, Col {c} "); self.char_count_label.setText(f" Chars: {char_count} ")
            enc = d.get('encoding', 'utf-8'); edn = self.reverse_encoding_map.get(enc, "UTF-8"); self.encoding_label.setText(f" {edn} ")
            idx = self.encoding_combo.findData(enc)
            if idx != -1: self.encoding_combo.setCurrentIndex(idx)
            self.encoding_combo.setEnabled(bool(d.get('filepath')) and not isinstance(w, LargeFileViewerWidget))
        else:
            self.cursor_label.setText(""); self.encoding_label.setText(" N/A "); self.char_count_label.setText(""); self.encoding_combo.setEnabled(False)
        self.encoding_combo.blockSignals(False)
        self.actions["find_replace"].setEnabled(is_ed)

    def _is_editor_modified(self, ed):
        return hasattr(ed, 'get_text') and hash(ed.get_text()) != self.editor_tabs_data.get(ed, {}).get('original_hash', hash(None))

    def _on_content_changed(self, editor):
        if not self.tab_widget.isAncestorOf(editor): return
        mod, idx = self._is_editor_modified(editor), self.tab_widget.indexOf(editor)
        if idx != -1:
            txt = self.tab_widget.tabText(idx)
            self.tab_widget.setTabText(idx, f'{txt} *' if mod and not txt.endswith(' *') else txt[:-2] if not mod and txt.endswith(' *') else txt)
        self._update_window_title(); self.char_count_label.setText(f" Chars: {len(editor.get_text())} ")
        if self.settings.get("auto_save_enabled"): self.auto_save_timer.start(self.settings.get("auto_save_delay_seconds", 3) * 1000)
        if mod: self.draft_save_timer.start()

    def _on_file_renamed(self, old_path: str, new_path: str):
        log.info(f"File renamed from '{old_path}' to '{new_path}'.")
        for i in range(self.tab_widget.count()):
            widget = self.tab_widget.widget(i)
            if hasattr(widget, 'filepath') and os.path.normpath(widget.filepath) == os.path.normpath(old_path):
                widget.filepath = new_path
                if widget in self.editor_tabs_data: self.editor_tabs_data[widget]['filepath'] = new_path
                self.tab_widget.setTabText(i, os.path.basename(new_path)); self.tab_widget.setTabToolTip(i, new_path)
                self._update_window_title(); break
        if refactor_plugin := self.plugin_manager.get_plugin_instance_by_id("refactor_tool"):
            if hasattr(refactor_plugin, 'trigger_rename_refactor'): refactor_plugin.trigger_rename_refactor(old_path, new_path)

    def _update_window_title(self):
        proj = os.path.basename(self.project_manager.get_active_project_path() or ""); c = ""
        if (w := self.tab_widget.currentWidget()) and hasattr(w, 'filepath') and w.filepath:
            c = os.path.basename(w.filepath); c += " *" if self._is_editor_modified(w) else ""
        elif w: c = self.tab_widget.tabText(self.tab_widget.currentIndex())
        self.setWindowTitle(" - ".join(filter(None, [c, proj, "Koromali"])))

    def _action_save_file(self, editor_widget=None, save_as=False):
        editor = editor_widget or self.tab_widget.currentWidget()
        if not hasattr(editor, 'get_text'): return None
        fp, content = getattr(editor, 'filepath', None), editor.get_text()
        encoding = self.editor_tabs_data.get(editor, {}).get('encoding', 'utf-8')
        new_fp, new_encoding = self.file_handler.save_file_content(fp, content, save_as, encoding)
        if new_fp:
            if os.path.exists(d_path := helpers.get_draft_path(new_fp)): os.remove(d_path); log.info(f"Draft for {new_fp} removed.")
            self.file_handler._add_to_recent_files(new_fp); setattr(editor, 'filepath', new_fp)
            if editor not in self.editor_tabs_data: self.editor_tabs_data[editor] = {}
            self.editor_tabs_data[editor].update({'filepath': new_fp, 'original_hash': hash(content), 'encoding': new_encoding, 'original_content_for_diff': content})
            if (idx := self.tab_widget.indexOf(editor)) != -1: self.tab_widget.setTabText(idx, os.path.basename(new_fp)); self.tab_widget.setTabToolTip(idx, new_fp)
            self.statusBar().showMessage(f"File saved: {os.path.basename(new_fp)}", 3000)
            self._on_content_changed(editor); self._on_tab_changed(self.tab_widget.currentIndex())
            return new_fp
        self.statusBar().showMessage("Save cancelled.", 2000); return None

    def _action_save_as(self):
        self._action_save_file(save_as=True)

    def _action_save_all(self):
        saved = sum(1 for i in range(self.tab_widget.count()) if hasattr(ed := self.tab_widget.widget(i), 'get_text') and self._is_editor_modified(ed) and self._action_save_file(ed))
        if saved > 0: self.statusBar().showMessage(f"Saved {saved} files.", 3000)

    def _action_close_all_tabs(self):
        log.info("Closing all tabs requested by user.")
        for i in range(self.tab_widget.count() - 1, -1, -1): self._action_close_tab_by_index(i)

    def _action_close_tab_by_index(self, index):
        if not (w := self.tab_widget.widget(index)): return
        if self._is_editor_modified(w): self._save_draft(w)
        e = QCloseEvent(); self._close_widget_safely(w, e)
        if e.isAccepted():
            if self.tab_widget.indexOf(w) != -1: self.tab_widget.removeTab(self.tab_widget.indexOf(w))
            w.deleteLater(); log.info(f"Tab {index} closed.")
            if self.tab_widget.count() == 0: self._add_new_tab(is_placeholder=True)

    def _close_widget_safely(self, widget, event):
        if widget in self.editor_tabs_data: del self.editor_tabs_data[widget]
        event.accept()

    def _update_recent_files_menu(self):
        self.recent_files_menu.clear(); [self.recent_files_menu.addAction((a := QAction(f"&{i + 1} {os.path.basename(fp)}", self), a.setData(fp), a.setToolTip(fp), a.triggered.connect(self._action_open_recent_file))[0]) for i, fp in enumerate(self.settings.get("recent_files", [])[:10])]; self.recent_files_menu.setEnabled(bool(self.recent_files_menu.actions()))

    def _action_open_recent_file(self):
        if act := self.sender(): self._action_open_file(act.data())

    def _trigger_file_linter(self):
        if (ed := self.tab_widget.currentWidget()) and isinstance(ed, EditorWidget) and (fp := self.editor_tabs_data.get(ed, {}).get('filepath')): self.linter_manager.lint_file(fp)

    def _show_about_dialog(self): QMessageBox.about(self, "About", f"Koromali v{versioning.APP_VERSION}")
    def _open_github_link(self):
        if not GITHUB_REPO_URL:
            log.warning("GitHub repository URL is not configured; link unavailable.")
            return
        QDesktopServices.openUrl(QUrl(GITHUB_REPO_URL))

    def _auto_save_current_tab(self):
        if hasattr(ed := self.tab_widget.currentWidget(), 'get_text') and self._is_editor_modified(ed): self._action_save_file(editor_widget=ed)

    def _on_editor_settings_changed(self):
        [w.apply_styles_and_settings() for i in range(self.tab_widget.count()) if isinstance(w := self.tab_widget.widget(i), EditorWidget)]

    def _action_open_preferences(self):
        if not self.preferences_dialog or not self.preferences_dialog.isVisible():
            self.preferences_dialog = PreferencesDialog(self.theme_manager, self.git_manager, self.github_manager, self.plugin_manager, self.koromali_api, self.settings, self)
            self.preferences_dialog.settings_changed_for_editor_refresh.connect(self._on_editor_settings_changed)
            self.preferences_dialog.theme_changed_signal.connect(self._on_theme_selected)
        self.preferences_dialog.show(); self.preferences_dialog.raise_(); self.preferences_dialog.activateWindow()

    def _action_force_quit(self): log.warning("Force quit."); QApplication.instance().quit()
    
    def _reload_open_tabs(self, paths_to_reload: List[str]):
        """Finds open tabs matching the given paths, closes, and re-opens them."""
        norm_paths = {os.path.normpath(p) for p in paths_to_reload}
        tabs_to_reopen = []
        
        for i in range(self.tab_widget.count() - 1, -1, -1):
            widget = self.tab_widget.widget(i)
            if hasattr(widget, 'filepath') and widget.filepath:
                widget_path = os.path.normpath(widget.filepath)
                # Check if the widget's path is in the set, or is a child of a folder in the set
                if any(widget_path == p or widget_path.startswith(p + os.sep) for p in norm_paths):
                    tabs_to_reopen.append(widget.filepath)
                    self.tab_widget.removeTab(i)
                    widget.deleteLater()
        
        if self.tab_widget.count() == 0:
            self._add_new_tab(is_placeholder=True)
        
        for fp in reversed(tabs_to_reopen):
            self._action_open_file(fp)

    def _goto_definition_result(self, fp, line, col):
        if not fp: self.statusBar().showMessage("Def not found", 3000); return
        np = os.path.normpath(fp)
        for i in range(self.tab_widget.count()):
            if isinstance(ed := self.tab_widget.widget(i), (EditorWidget, LargeFileViewerWidget)) and self.editor_tabs_data.get(ed, {}).get('filepath') == np:
                self.tab_widget.setCurrentIndex(i)
                if hasattr(ed, 'goto_line_and_column'): ed.goto_line_and_column(line, col)
                return
        self._action_open_file(np)
        if isinstance(cur := self.tab_widget.currentWidget(), (EditorWidget, LargeFileViewerWidget)) and hasattr(cur, 'goto_line_and_column'):
            cur.goto_line_and_column(line, col)
        else:
            log.warning(f"Failed jump to def for {np}")

    def _shutdown_plugins(self):
        log.info("Shutting down plugins"); [p.instance.shutdown() for p in self.plugin_manager.get_loaded_plugins() if hasattr(p.instance, 'shutdown')]

    def _shutdown_managers(self):
        log.info("Shutting down managers"); [m.shutdown() for m in [self.completion_manager, self.github_manager, self.git_manager, self.linter_manager] if hasattr(m, 'shutdown')]

    def _save_current_project_session(self):
        active_project = self.project_manager.get_active_project_path()
        if not active_project: return
        open_files = [data['filepath'] for widget, data in self.editor_tabs_data.items() if data.get('filepath') and self.tab_widget.isAncestorOf(widget)]
        project_sessions = self.settings.get("project_sessions", {}); project_sessions[active_project] = open_files
        self.settings.set("project_sessions", project_sessions, save_immediately=False)
        log.info(f"Saved tab session for project '{os.path.basename(active_project)}'.")

    def _load_project_session(self, project_path: str):
        if not project_path: return
        project_sessions = self.settings.get("project_sessions", {}); files_to_open = project_sessions.get(project_path, [])
        log.info(f"Loading tab session for project '{os.path.basename(project_path)}' with {len(files_to_open)} files.")
        for fp in files_to_open:
            if os.path.exists(fp): self._action_open_file(fp)
            else: log.warning(f"Could not restore session file, path not found: {fp}")

    def _close_all_tabs_for_project_switch(self):
        self.tab_widget.blockSignals(True)
        # Collect widgets to delete first
        widgets_to_delete = [self.tab_widget.widget(i) for i in range(self.tab_widget.count())]
        # Clear the tab widget UI, which detaches the widgets
        self.tab_widget.clear()
        # Safely delete the detached widgets and clear our tracking data
        for widget in widgets_to_delete:
            if widget:
                widget.deleteLater()
        self.editor_tabs_data.clear()
        self.tab_widget.blockSignals(False)
        # Add the placeholder tab back
        self._add_new_tab(is_placeholder=True)

    def _on_project_list_or_active_changed(self):
        new_active_project = self.project_manager.get_active_project_path()
        if self.last_active_project_path != new_active_project:
            log.info(f"Active project changed from '{self.last_active_project_path}' to '{new_active_project}'")
            self._save_current_project_session()
            self._close_all_tabs_for_project_switch()
            self._load_project_session(new_active_project)
            self.last_active_project_path = new_active_project
        # Also refresh the explorer to update its active state visuals
        if hasattr(self, 'explorer_panel'):
            self.explorer_panel.refresh()

    def closeEvent(self, e: QCloseEvent):
        if self._is_app_closing: e.accept(); return
        self._is_app_closing = True; log.info("Starting shutdown.")
        self._save_current_project_session(); [self._save_draft(w) for i in range(self.tab_widget.count()) if self._is_editor_modified(w := self.tab_widget.widget(i))]
        if hasattr(self, 'explorer_panel'): self.settings.set("explorer_expanded_paths", self.explorer_panel.get_expanded_paths(), False)
        self.project_manager.save_session(); self.settings.save(); self._shutdown_plugins(); self._shutdown_managers()
        log.info("Shutdown complete."); e.accept()

    def toggle_find_panel(self):
        if isinstance(ed := self.tab_widget.currentWidget(), EditorWidget): ed.toggle_find_panel()
        else: log.warning("Find on non-editor.")

    def _on_active_project_changed(self, cur, _):
        if not cur: return
        root = cur;
        while p := root.parent(): root = p
        if (d := root.data(0, Qt.ItemDataRole.UserRole)) and (p := d.get('path')):
            self.project_manager.set_active_project(p); self.completion_manager.update_project_path(p)

    def _on_item_created(self, itype, path):
        if itype == 'file': self._add_header_to_new_file(path)

    def _generate_header_line(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        s = self.COMMENT_MAP.get(ext)
        if not s: return None
        
        root = self.project_manager.get_active_project_path()
        if not root or not file_path.startswith(root): return None

        # Correctly handle path joining and separator replacement
        rel_path_with_root = os.path.join(os.path.basename(root), os.path.relpath(file_path, root))
        formatted_path = rel_path_with_root.replace(os.sep, '/')
        
        end_comment = self.END_COMMENT_MAP.get(s, '')
        return f"{s} Koromali/{formatted_path} {end_comment}\n"

    def _add_header_to_new_file(self, file_path):
        if h := self._generate_header_line(file_path):
            try:
                with open(file_path, 'w', encoding='utf-8') as f: f.write(h); log.info(f"Header for {file_path}")
            except IOError as e: log.error(f"Header write failed:{e}")

    def _on_encoding_changed_from_dropdown(self, index: int):
        editor = self.tab_widget.currentWidget()
        if not isinstance(editor, (EditorWidget, LargeFileViewerWidget)): return
        new_enc, data = self.encoding_combo.itemData(index), self.editor_tabs_data.get(editor)
        if not data or new_enc == data.get('encoding'): return
        if QMessageBox.question(self, "Change Encoding", f"Save file with {self.encoding_combo.currentText()}?", QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel) == QMessageBox.StandardButton.Save: self._resave_with_new_encoding(editor, new_enc)
        else: self._on_tab_changed(self.tab_widget.currentIndex())

    def _resave_with_new_encoding(self, editor: QWidget, new_encoding: str):
        if not (data := self.editor_tabs_data.get(editor)) or not data.get('filepath'): return
        saved, final_enc = self.file_handler.save_file_content(data['filepath'], editor.get_text(), False, encoding=new_encoding)
        if saved:
            data.update({'encoding': final_enc, 'original_hash': hash(editor.get_text())}); self._on_content_changed(editor)
            self.statusBar().showMessage("File re-saved.", 4000)
        else:
            self.statusBar().showMessage("Re-save failed.", 4000); self._on_tab_changed(self.tab_widget.currentIndex())

    def _save_draft(self, editor: QWidget):
        if not (hasattr(editor, 'filepath') and editor.filepath): return
        enc = 'utf-8' if not isinstance(editor, (EditorWidget, LargeFileViewerWidget)) else self.editor_tabs_data.get(editor, {}).get('encoding', 'utf-8')
        try:
            with open(helpers.get_draft_path(editor.filepath), 'w', encoding=enc) as f:
                f.write(editor.get_text()); log.info(f"Saved draft for {os.path.basename(editor.filepath)}")
        except (IOError, OSError) as e: log.error(f"Draft save failed:{e}")

    def _save_current_draft(self):
        if (ed := self.tab_widget.currentWidget()) and self._is_editor_modified(ed):
            self._save_draft(ed)