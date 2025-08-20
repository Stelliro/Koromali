# Koromali/plugins/plugin_publisher/plugin_main.py
from app_core.koromali_api import KoromaliPluginAPI
from .publish_dialog import PublishDialog
from utils.logger import log

class PluginPublisherPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.publish_dialog = None
        self.publish_action = self.api.add_menu_action(
            menu_name="tools",
            text="Publish Plugin...",
            callback=self.show_publish_dialog,
            icon_name="fa5s.cloud-upload-alt"
        )
        self.update_action_state()
        github_manager = self.api.get_manager("github")
        if github_manager:
            github_manager.auth_successful.connect(self._on_auth_state_changed)
            # You should connect to a unified signal if possible, or connect to both
            # If the manager does not have an explicit logout signal, auth_failed can work
            # as a stand-in for state change that indicates a logged-out status.
            # self.github_manager.logged_out.connect(self._on_auth_state_changed) # Ideal
            self.api.get_main_window().destroyed.connect(self.shutdown)


    def shutdown(self):
        # Disconnect signals to prevent calls to a deleted object on app close
        log.info("Plugin Publisher is shutting down.")
        github_manager = self.api.get_manager("github")
        if github_manager:
            try:
                github_manager.auth_successful.disconnect(self._on_auth_state_changed)
            except (TypeError, RuntimeError):
                pass
        
        # Action is managed by API, so no need to manually remove,
        # just nullify references
        self.publish_action = None
        if self.publish_dialog:
             self.publish_dialog.deleteLater()
             self.publish_dialog = None

    def _on_auth_state_changed(self, *args, **kwargs):
        """
        Slot to handle authentication state changes. This will call the UI
        update method.
        """
        self.update_action_state()

    def show_publish_dialog(self):
        github_manager = self.api.get_manager("github")
        if not (github_manager and github_manager.get_authenticated_user()):
            self.api.show_message("warning", "Login Required", "You must be logged into GitHub to publish a plugin.")
            return

        if self.publish_dialog is None or not self.publish_dialog.isVisible():
            self.publish_dialog = PublishDialog(self.api, self.api.get_main_window())
        self.publish_dialog.show()
        self.publish_dialog.raise_()
        self.publish_dialog.activateWindow()

    def update_action_state(self):
        # Add a guard to ensure the action exists before modification.
        if not self.publish_action:
            return
            
        github_manager = self.api.get_manager("github")
        is_logged_in = bool(github_manager and github_manager.get_authenticated_user())
        self.publish_action.setEnabled(is_logged_in)
        self.publish_action.setToolTip("Upload a plugin." if is_logged_in else "Log in to GitHub to use.")

def initialize(koromali_api: KoromaliPluginAPI):
    return PluginPublisherPlugin(koromali_api)