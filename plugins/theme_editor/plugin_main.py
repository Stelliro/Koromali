# Koromali/plugins/theme_editor/plugin_main.py
from .theme_editor_dialog import ThemeEditorDialog
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log


class ThemeEditorPlugin:
    """Initializes the Theme Editor and connects it to the UI."""

    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        # Correctly get the theme_manager via the API
        self.theme_manager = self.api.get_manager("theme")
        self.dialog_instance = None

        # This action will be added to the "Tools" menu.
        self.action = self.api.add_menu_action(
            menu_name="tools",
            text="Theme Editor...",
            callback=self.show_theme_editor_dialog,
            icon_name="fa5s.palette"
        )

        # Let the core application know how to launch this plugin's main feature.
        # This is used by the Preferences dialog.
        self.api.register_theme_editor_launcher(self.show_theme_editor_dialog)
        log.info("Theme Editor registered its launcher with the core API.")

    def show_theme_editor_dialog(self):
        """Creates and shows the theme editor dialog."""
        # Lazily create the dialog instance to save resources on startup
        if self.dialog_instance is None or not self.dialog_instance.parent():
            self.dialog_instance = ThemeEditorDialog(self.theme_manager, self.main_window)
            # When a theme is saved/deleted in the dialog, tell the main window to update its menus
            self.dialog_instance.custom_themes_changed.connect(
                self.main_window._rebuild_theme_menu
            )
        self.dialog_instance.exec()

    def shutdown(self):
        """
        A cleanup method called by the plugin manager before unloading.
        This is crucial for preventing errors on plugin reloads.
        """
        log.info("Theme Editor plugin is shutting down.")
        if self.action:
            # Safely remove the menu action from the UI
            if menu := self.api.get_menu("tools"):
                menu.removeAction(self.action)
            self.action.deleteLater()
        if self.dialog_instance:
            self.dialog_instance.deleteLater()


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for the Theme Editor plugin."""
    return ThemeEditorPlugin(koromali_api)