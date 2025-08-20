# /plugins/ai_export_viewer/plugin_main.py
import os
from functools import partial
from typing import List
from PyQt6.QtWidgets import QMenu, QMessageBox
from PyQt6.QtCore import QTimer, Qt
import qtawesome as qta
from app_core.koromali_api import KoromaliPluginAPI
from .ai_export_viewer_widget import AIExportViewerWidget
from .select_export_dialog import SelectExportDialog
from .restore_logic import perform_restore
from utils.logger import log


class AIExportViewerPlugin:
    """Plugin to view AI-generated export files and restore from them."""

    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.viewer_widget = None

        self.api.add_menu_action(
            menu_name="tools",
            text="View AI Exports",
            callback=self.open_viewer_tab,
            icon_name="fa5s.robot"
        )
        
        # Use a timer to ensure the explorer panel is initialized before connecting
        QTimer.singleShot(100, self._deferred_setup)
        log.info("AI Export Viewer plugin initialized and menu action added.")

    def _deferred_setup(self):
        """Connect to the explorer panel after the UI is fully initialized."""
        if hasattr(self.main_window, 'explorer_panel'):
            explorer_tree = self.main_window.explorer_panel.tree_widget
            explorer_tree.customContextMenuRequested.connect(self._on_explorer_context_menu)
            log.info("AI Export Viewer successfully integrated with explorer context menu.")
        else:
            log.warning("Could not find 'explorer_panel' to integrate AI Export Viewer context menu.")

    def _on_explorer_context_menu(self, position):
        """Adds the 'Restore from Export' action to the explorer's context menu."""
        explorer_tree = self.main_window.explorer_panel.tree_widget
        selected_items = explorer_tree.selectedItems()
        if not selected_items:
            return

        # Get the explorer's own context menu to append to it
        menu = explorer_tree.findChild(QMenu)
        if not menu:
            return

        menu.addSeparator()
        restore_action = menu.addAction(qta.icon('mdi.backup-restore'), "Restore from Export...")
        restore_action.triggered.connect(self._trigger_restore_workflow)

    def _trigger_restore_workflow(self):
        """Handles the entire process of selecting an export and restoring files."""
        explorer_tree = self.main_window.explorer_panel.tree_widget
        selected_items = explorer_tree.selectedItems()
        target_paths = [item.data(0, Qt.ItemDataRole.UserRole)['path'] for item in selected_items if item.data(0, Qt.ItemDataRole.UserRole)]

        if not target_paths:
            self.api.show_message("warning", "Nothing Selected", "No valid items selected for restore.")
            return

        # Step 1: User selects the export file
        dialog = SelectExportDialog(self.main_window)
        if not dialog.exec():
            return
        
        export_path = dialog.selected_export_path
        if not export_path:
            return

        project_root = self.api.get_manager("project").get_active_project_path()
        if not project_root:
            self.api.show_message("critical", "No Project Active", "Cannot restore files without an active project context.")
            return

        # Step 2: Perform the restore logic (which includes backup prompt)
        success, message = perform_restore(export_path, target_paths, project_root, self.main_window)

        # Step 3: Show result and reload tabs
        if success:
            QMessageBox.information(self.main_window, "Restore Complete", message)
            self._reload_open_tabs(target_paths)
            if hasattr(self.main_window, 'explorer_panel'):
                self.main_window.explorer_panel.refresh()
        else:
            QMessageBox.warning(self.main_window, "Restore Failed", message)

    def _reload_open_tabs(self, restored_paths: List[str]):
        """Finds open tabs matching the restored paths, closes, and re-opens them."""
        tab_widget = self.api.get_main_tab_widget()
        if not tab_widget: return

        norm_paths = {os.path.normpath(p) for p in restored_paths}
        tabs_to_reopen = []
        
        for i in range(tab_widget.count() - 1, -1, -1):
            widget = tab_widget.widget(i)
            widget_data = self.main_window.editor_tabs_data.get(widget, {})
            widget_path = widget_data.get('filepath')
            
            if widget_path:
                norm_widget_path = os.path.normpath(widget_path)
                if any(norm_widget_path == p or norm_widget_path.startswith(p + os.sep) for p in norm_paths):
                    tabs_to_reopen.append(widget_path)
                    tab_widget.removeTab(i)
                    widget.deleteLater()
        
        if not tabs_to_reopen and tab_widget.count() == 0:
            self.main_window._add_new_tab(is_placeholder=True)
        
        for fp in reversed(tabs_to_reopen):
            self.main_window._action_open_file(fp)

    def open_viewer_tab(self):
        """Opens a new tab containing the AI Export Viewer widget."""
        self.viewer_widget = AIExportViewerWidget(
            self.api,
            parent=self.main_window
        )

        for i in range(self.main_window.tab_widget.count()):
            if isinstance(self.main_window.tab_widget.widget(i), AIExportViewerWidget):
                self.main_window.tab_widget.setCurrentIndex(i)
                return

        indexx = self.main_window.tab_widget.addTab(self.viewer_widget, "AI Exports")
        self.main_window.tab_widget.setCurrentIndex(indexx)
        self.main_window.tab_widget.setTabsClosable(True)


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for Koromali to load the plugin."""
    try:
        return AIExportViewerPlugin(koromali_api)
    except Exception as e:
        log.error(f"Failed to initialize AI Export Viewer: {e}", exc_info=True)
        return None