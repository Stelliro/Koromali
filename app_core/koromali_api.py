# app_core/koromali_api.py
from typing import Callable, Optional, Any, TYPE_CHECKING
from PyQt6.QtWidgets import (QDockWidget, QTabWidget, QWidget, QMenu, QMessageBox)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, pyqtSignal, QObject
import qtawesome as qta
from utils.logger import log

if TYPE_CHECKING:
    from ui.main_window import MainWindow
    from ui.editor_widget import HighlightManager

class KoromaliPluginAPI(QObject):
    project_lock_requested = pyqtSignal(str, bool)

    def __init__(self, main_window: 'MainWindow'):
        super().__init__()
        self._main_window = main_window
        self.theme_editor_launcher: Optional[Callable] = None
        self.highlighter_map: dict[str, Any] = {}
        self.highlight_manager: Optional['HighlightManager'] = None
        self.registered_panels: dict[str, dict] = {}
        log.info("KoromaliPluginAPI initialized.")

    def get_main_window(self) -> 'MainWindow':
        return self._main_window

    def get_main_tab_widget(self) -> Optional[QTabWidget]:
        if hasattr(self._main_window, 'tab_widget'):
            return self._main_window.tab_widget
        log.error("API request for tab_widget failed: MainWindow has no tab_widget.")
        return None

    def get_manager(self, manager_name: str) -> Optional[Any]:
        name_map = {
            "project": self._main_window.project_manager, "file_handler": self._main_window.file_handler,
            "settings": self._main_window.settings, "theme": self._main_window.theme_manager,
            "completion": self._main_window.completion_manager, "github": self._main_window.github_manager,
            "git": self._main_window.git_manager, "linter": self._main_window.linter_manager,
            "update": self._main_window.update_manager, "plugin": self._main_window.plugin_manager,
        }
        if not (manager := name_map.get(manager_name.lower())):
            log.warning(f"Plugin requested an unknown manager: '{manager_name}'")
        return manager

    def add_dock_panel(self, widget: QWidget, title: str, area_str: str, icon_name: Optional[str] = None) -> Optional[QDockWidget]:
        panel_id = f"panel_{title.lower().replace(' ', '_')}"
        if panel_id not in self.registered_panels:
            self.registered_panels[panel_id] = {
                'widget_class': type(widget),
                'title': title,
                'default_area': area_str,
                'icon_name': icon_name
            }
            log.info(f"Panel '{title}' registered implicitly via add_dock_panel.")

        return self._main_window.add_dock_panel(widget, title, area_str, icon_name)

    def get_registered_panels(self) -> dict:
        """Returns the dictionary of all registered panels."""
        return self.registered_panels

    def get_plugin_instance(self, plugin_id: str) -> Optional[Any]:
        if plugin_manager := self.get_manager("plugin"):
            if plugin := plugin_manager.plugins.get(plugin_id):
                if plugin.is_loaded: return plugin.instance
        log.warning(f"Could not find a loaded plugin instance for ID: '{plugin_id}'")
        return None

    def register_theme_editor_launcher(self, launcher_callback: Callable):
        self.theme_editor_launcher = launcher_callback
        log.info("A theme editor launcher has been registered.")
        if hasattr(mw := self.get_main_window(), 'preferences_dialog') and mw.preferences_dialog:
            mw.preferences_dialog.connect_theme_editor_button()

    def get_menu(self, menu_name: str) -> Optional[QMenu]:
        return getattr(self._main_window, f"{menu_name.lower()}_menu", None)

    def register_highlighter(self, extension: str, highlighter_class):
        if not extension.startswith('.'): extension = f".{extension}"
        self.highlighter_map[extension.lower()] = highlighter_class
        log.info(f"Registered highlighter '{highlighter_class.__name__}' for '{extension}' files.")

    def add_menu_action(self, menu_name, text, callback, shortcut=None, icon_name=None, insert_before=None):
        menu = getattr(self._main_window, f"{menu_name.lower()}_menu", None)
        if not menu:
            menu = self._main_window.menuBar().addMenu(f"&{menu_name.capitalize()}")
            setattr(self._main_window, f"{menu_name.lower()}_menu", menu)
        icon = qta.icon(icon_name) if icon_name else None
        action = QAction(icon, text, self._main_window)
        if shortcut: action.setShortcut(shortcut)
        action.triggered.connect(callback)
        
        # New logic to insert before a specific action
        if isinstance(insert_before, QAction):
            menu.insertAction(insert_before, action)
        else:
            menu.addAction(action)
        return action

    def add_toolbar_action(self, action: QAction):
        if hasattr(self._main_window, 'main_toolbar'):
            self._main_window.main_toolbar.addAction(action)
            log.info(f"Added action '{action.text()}' to main toolbar.")
        else:
            log.error("Cannot add toolbar action: Main toolbar not found.")

    def register_file_opener(self, extension: str, handler_callable: Callable):
        if not extension.startswith('.'): extension = f".{extension}"
        self._main_window.file_open_handlers[extension.lower()] = handler_callable

    def show_message(self, level, title, text):
        icon_map = {'info': QMessageBox.Icon.Information, 'warning': QMessageBox.Icon.Warning,
                    'critical': QMessageBox.Icon.Critical}
        icon = icon_map.get(level.lower(), QMessageBox.Icon.NoIcon)
        msg_box = QMessageBox(icon, title, text, parent=self._main_window)
        msg_box.exec()

    def show_status_message(self, message: str, timeout: int = 4000):
        self._main_window.statusBar().showMessage(message, timeout)

    def register_progress_bar(self, task_id: str, description: str):
        """Creates and shows a progress bar in the status bar for a long-running task."""
        self._main_window.register_progress_bar(task_id, description)

    def update_progress_bar(self, task_id: str, value: int, max_value: int):
        """Updates the value of a registered progress bar."""
        self._main_window.update_progress_bar(task_id, value, max_value)

    def hide_progress_bar(self, task_id: str):
        """Hides and removes a progress bar from the status bar."""
        self._main_window.hide_progress_bar(task_id)

    def log_info(self, msg): log.info(f"[Plugin] {msg}")
    def log_warning(self, msg): log.warning(f"[Plugin] {msg}")
    def log_error(self, msg): log.error(f"[Plugin] {msg}")