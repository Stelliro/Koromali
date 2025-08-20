# /plugins/live_share_studio/plugin_main.py
from PyQt6.QtWidgets import QWidget
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log
from .session_manager_panel import SessionManagerPanel
from .collaboration_server import CollaborationServer
from .collaboration_client import CollaborationClient
from .editor_integration import EditorIntegration
from .crypto_utils import CryptoUtils

class LiveSharePlugin:
    """Main class for the Live Share Studio plugin."""

    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()

        # Initialize core components with dependencies
        self.crypto_utils = CryptoUtils()
        self.server = CollaborationServer(self.crypto_utils)
        self.client = CollaborationClient(self.crypto_utils, self.api)
        self.editor_integration = EditorIntegration(self.api, self.client)
        
        self.session_panel = SessionManagerPanel(
            self.api, self.server, self.client, self.editor_integration
        )

        # Register the panel with the UI
        self.api.add_dock_panel(
            widget=self.session_panel,
            title="Live Share",
            area_str="right",
            icon_name="fa5s.users"
        )
        
        # Add a menu action to easily open the panel
        self.api.add_menu_action(
            menu_name="tools",
            text="Live Share Studio",
            callback=self.show_panel,
            icon_name="fa5s.users"
        )
        log.info("Live Share Studio plugin initialized.")

    def show_panel(self):
        """Shows and raises the Live Share session panel."""
        # A dock widget is usually wrapped in a parent QDockWidget
        if self.session_panel.parent() and isinstance(self.session_panel.parent(), QWidget):
            self.session_panel.parent().show()
            self.session_panel.parent().raise_()

    def shutdown(self):
        """Cleans up resources when the plugin is unloaded."""
        log.info("Shutting down Live Share Studio...")
        if self.server.is_running():
            self.server.stop()
        if self.client.is_connected():
            self.client.disconnect()
        self.editor_integration.shutdown()
        log.info("Live Share Studio shutdown complete.")


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for the plugin."""
    return LiveSharePlugin(koromali_api)