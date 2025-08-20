# /plugins/project_search/plugin_main.py
from PyQt6.QtWidgets import QProgressDialog
from PyQt6.QtCore import Qt, QThreadPool
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log
from .search_results_widget import SearchResultsWidget
from .search_worker import ProjectSearchWorker

class ProjectSearchPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.project_manager = self.api.get_manager("project")
        self.theme_manager = self.api.get_manager("theme")
        self.settings_manager = self.api.get_manager("settings")
        self.threadpool = QThreadPool()
        self.progress_dialog = None
        self.worker = None

        self.results_widget = SearchResultsWidget(self.theme_manager, self.settings_manager, self.main_window)
        self.results_widget.result_selected.connect(self.main_window._goto_definition_result)

        self.dock = self.api.add_dock_panel(
            widget=self.results_widget,
            title="Project Search Results",
            area_str="bottom",
            icon_name="mdi.folder-search-outline"
        )
        self.dock.hide()

        # Connect the central handler in MainWindow to this plugin's entry point
        self.main_window.project_find_requested.connect(self.start_search)
        self.main_window.theme_changed_signal.connect(self.results_widget.update_theme)

    def start_search(self, query: str, find_flags: object):
        project_path = self.project_manager.get_active_project_path()
        if not project_path: return

        self.dock.show()
        self.dock.raise_()
        
        self.worker = ProjectSearchWorker(project_path, query, find_flags)
        
        # Connect signals for this run
        self.worker.signals.finished.connect(lambda r: self._on_search_finished(query, r))
        self.worker.signals.error.connect(lambda e: self.api.show_message("critical", "Search Error", e))
        
        self.results_widget.clear_results()
        self.results_widget.set_search_summary(query, 0, 0, is_searching=True)
        self.threadpool.start(self.worker)

    def _on_search_finished(self, query, results):
        file_count = len(results)
        match_count = sum(len(matches) for matches in results.values())
        
        self.results_widget.set_search_summary(query, file_count, match_count, is_searching=False)
        self.results_widget.populate_results(results, self.project_manager.get_active_project_path())
        
        # Disconnect signals to prevent old workers from affecting new searches
        try:
            self.worker.signals.finished.disconnect()
            self.worker.signals.error.disconnect()
        except TypeError: # This happens if they were already disconnected
            pass
            
def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for the Project Search plugin."""
    return ProjectSearchPlugin(koromali_api)