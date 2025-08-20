# /plugins/refactor_tool/plugin_main.py
import os
from pathlib import Path
from PyQt6.QtWidgets import QMessageBox, QProgressDialog
from PyQt6.QtCore import QThreadPool, Qt
from app_core.koromali_api import KoromaliPluginAPI
from .name_refactorer import ProjectReplaceWorker
from utils.logger import log

class RefactorPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.project_manager = self.api.get_manager("project")
        self.threadpool = QThreadPool()
        self.progress_dialog = None
        self.worker = None # To hold the currently running worker
        
        # Connect to main window signals
        if hasattr(self.main_window, 'project_replace_requested'):
             self.main_window.project_replace_requested.connect(self.start_project_replace)

        log.info("Refactor Tool plugin initialized.")

    def trigger_rename_refactor(self, old_path_str: str, new_path_str: str):
        """This method is called by the MainWindow when a file is renamed."""
        old_path = Path(old_path_str)
        new_path = Path(new_path_str)

        old_name = old_path.stem
        new_name = new_path.stem

        if not old_name or not new_name or old_name == new_name:
            return

        project_path = self._get_project_for_path(old_path_str)
        if not project_path:
            log.warning(f"Could not determine project for renamed file: {old_path_str}")
            return

        reply = QMessageBox.question(
            self.main_window,
            "Refactor Project?",
            f"You renamed '{old_path.name}' to '{new_path.name}'.\n\n"
            f"Would you like to search the entire project '{os.path.basename(project_path)}' "
            f"and replace all occurrences of the name '{old_name}' with '{new_name}'?\n\n"
            "This action cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            return

        # Use dummy flags for simple name replacement
        class DummyFlags:
            def __and__(self, other): return False

        self.worker = ProjectReplaceWorker(project_path, old_name, new_name, DummyFlags())
        self._start_worker("Refactoring on rename...")

    def start_project_replace(self, query: str, replace_text: str, find_flags):
        project_path = self.project_manager.get_active_project_path()
        if not project_path:
            self.api.show_message("warning", "No Active Project", "Please select a project to run project-wide replace.")
            return

        reply = QMessageBox.question(
            self.main_window,
            "Confirm Replace in Project",
            f"Are you sure you want to replace all occurrences of:\n'{query}'\nwith:\n'{replace_text}'\n\nin all text files in the project '{os.path.basename(project_path)}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Cancel:
            return

        self.worker = ProjectReplaceWorker(project_path, query, replace_text, find_flags)
        self._start_worker(f"Replacing '{query}' in project...")

    def _start_worker(self, progress_title: str):
        self.worker.signals.finished.connect(self.on_refactor_finished)
        self.worker.signals.progress.connect(self.on_refactor_progress)
        
        self.progress_dialog = QProgressDialog(
            progress_title, "Cancel", 0, 0, self.main_window
        )
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.canceled.connect(self.worker.cancel)
        self.progress_dialog.show()

        self.threadpool.start(self.worker)

    def _get_project_for_path(self, file_path: str) -> str | None:
        """Finds which open project a given file path belongs to."""
        for p_path in self.project_manager.get_open_projects():
            norm_p = os.path.normpath(p_path)
            norm_f = os.path.normpath(file_path)
            if os.path.commonpath([norm_f, norm_p]) == norm_p:
                return p_path
        return None

    def on_refactor_progress(self, current_file: str):
        if self.progress_dialog:
            self.progress_dialog.setLabelText(f"Scanning: {current_file}")
            
    def on_refactor_finished(self, modified_files: list, errors: list):
        if self.progress_dialog:
            self.progress_dialog.close()
        
        modified_count = len(modified_files)
        error_count = len(errors)

        if self.worker and self.worker.is_cancelled:
            QMessageBox.warning(self.main_window, "Refactoring Cancelled", "The refactoring process was cancelled.")
            return

        summary_message = f"Refactoring complete.\n\n- {modified_count} file(s) were modified."
        if error_count > 0:
            summary_message += f"\n- {error_count} error(s) occurred:\n" + "\n".join(errors[:5])
        
        QMessageBox.information(self.main_window, "Refactor Complete", summary_message)
        
        if modified_count > 0:
            if hasattr(self.main_window, '_reload_open_tabs'):
                self.main_window._reload_open_tabs(modified_files)
            if hasattr(self.main_window, 'source_control_panel'):
                self.main_window.source_control_panel.refresh_all_projects()


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for the Refactor Plugin."""
    return RefactorPlugin(koromali_api)