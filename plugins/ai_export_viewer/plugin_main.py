# /plugins/ai_export_viewer/plugin_main.py
import os
from typing import List

from PyQt6.QtWidgets import QMessageBox, QMenu
from PyQt6.QtCore import QTimer
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
        self._pending_restore_paths: List[str] = []

        self.api.add_menu_action(
            menu_name="tools",
            text="View AI Exports",
            callback=self.open_viewer_tab,
            icon_name="fa5s.robot",
        )

        # Defer until explorer exists
        QTimer.singleShot(100, self._deferred_setup)
        log.info("AI Export Viewer plugin initialized and menu action added.")

    def _deferred_setup(self):
        """Connect to the explorer panel after the UI is fully initialized."""
        explorer = getattr(self.main_window, "explorer_panel", None)
        if explorer is None:
            log.warning(
                "Could not find 'explorer_panel' to integrate AI Export Viewer context menu."
            )
            return

        # Preferred: stable signal that fires before menu.exec
        if hasattr(explorer, "context_menu_about_to_show"):
            explorer.context_menu_about_to_show.connect(self._on_context_menu_about_to_show)
            log.info("AI Export Viewer hooked explorer context_menu_about_to_show.")
            return

        # Fallback for older explorer implementations
        tree = getattr(explorer, "tree_widget", None)
        if tree is not None:
            tree.customContextMenuRequested.connect(self._legacy_context_menu_hook)
            log.info("AI Export Viewer using legacy explorer context menu hook.")
        else:
            log.warning("Explorer panel has no tree_widget; restore-from-export menu unavailable.")

    def _on_context_menu_about_to_show(self, menu: QMenu, paths: list):
        if not paths or menu is None:
            return
        self._pending_restore_paths = list(paths)
        menu.addSeparator()
        action = menu.addAction(qta.icon("mdi.backup-restore"), "Restore from Export...")
        action.triggered.connect(self._trigger_restore_workflow)

    def _legacy_context_menu_hook(self, _position):
        """Best-effort append when only customContextMenuRequested is available."""
        from PyQt6.QtCore import Qt

        explorer = getattr(self.main_window, "explorer_panel", None)
        if not explorer:
            return
        tree = explorer.tree_widget
        selected = tree.selectedItems()
        if not selected:
            return

        paths = []
        for item in selected:
            data = item.data(0, Qt.ItemDataRole.UserRole)
            if data and data.get("path"):
                paths.append(data["path"])
        if not paths:
            return

        self._pending_restore_paths = paths
        menu = tree.findChild(QMenu)
        if not menu:
            return
        menu.addSeparator()
        action = menu.addAction(qta.icon("mdi.backup-restore"), "Restore from Export...")
        action.triggered.connect(self._trigger_restore_workflow)

    def _trigger_restore_workflow(self):
        """Handles the entire process of selecting an export and restoring files."""
        target_paths = list(self._pending_restore_paths)
        if not target_paths:
            # Fallback: re-read current selection
            explorer = getattr(self.main_window, "explorer_panel", None)
            if explorer:
                from PyQt6.QtCore import Qt
                for item in explorer.tree_widget.selectedItems():
                    data = item.data(0, Qt.ItemDataRole.UserRole)
                    if data and data.get("path"):
                        target_paths.append(data["path"])

        if not target_paths:
            self.api.show_message(
                "warning", "Nothing Selected", "No valid items selected for restore."
            )
            return

        dialog = SelectExportDialog(self.main_window)
        if not dialog.exec():
            return

        export_path = dialog.selected_export_path
        if not export_path:
            return

        project_manager = self.api.get_manager("project")
        project_root = project_manager.get_active_project_path() if project_manager else None
        if not project_root:
            self.api.show_message(
                "critical",
                "No Project Active",
                "Cannot restore files without an active project context.",
            )
            return

        success, message = perform_restore(
            export_path, target_paths, project_root, self.main_window
        )

        if success:
            QMessageBox.information(self.main_window, "Restore Complete", message)
            if hasattr(self.main_window, "_reload_open_tabs"):
                self.main_window._reload_open_tabs(target_paths)
            if hasattr(self.main_window, "explorer_panel"):
                self.main_window.explorer_panel.refresh()
        else:
            QMessageBox.warning(self.main_window, "Restore Failed", message)

    def open_viewer_tab(self):
        """Opens a new tab containing the AI Export Viewer widget."""
        for i in range(self.main_window.tab_widget.count()):
            if isinstance(self.main_window.tab_widget.widget(i), AIExportViewerWidget):
                self.main_window.tab_widget.setCurrentIndex(i)
                return

        self.viewer_widget = AIExportViewerWidget(self.api, parent=self.main_window)
        index = self.main_window.tab_widget.addTab(
            self.viewer_widget, qta.icon("fa5s.robot"), "AI Exports"
        )
        self.main_window.tab_widget.setCurrentIndex(index)
        self.main_window.tab_widget.setTabsClosable(True)


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for Koromali to load the plugin."""
    try:
        return AIExportViewerPlugin(koromali_api)
    except Exception as e:
        log.error(f"Failed to initialize AI Export Viewer: {e}", exc_info=True)
        return None
