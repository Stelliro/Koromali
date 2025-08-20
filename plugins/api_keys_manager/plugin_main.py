# Koromali/plugins/api_keys_manager/plugin_main.py
from .api_keys_settings_page import ApiKeysDialog
from app_core.koromali_api import KoromaliPluginAPI

class ApiKeysManagerPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.api.add_menu_action(
            menu_name="tools",
            text="Manage API Keys...",
            callback=self.show_api_keys_dialog,
            icon_name="fa5s.key"
        )

    def show_api_keys_dialog(self):
        settings_manager = self.api.get_manager("settings")
        dialog = ApiKeysDialog(settings_manager, self.api.get_main_window())
        dialog.exec()

def initialize(koromali_api: KoromaliPluginAPI):
    return ApiKeysManagerPlugin(koromali_api)