# /plugins/corvus_integration/plugin_main.py
from app_core.koromali_api import KoromaliPluginAPI
from .corvus_chat_widget import CorvusChatWidget, CORVUS_AVAILABLE
from utils.logger import log

class CorvusIntegrationPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.chat_widget_instance = None

        if not CORVUS_AVAILABLE:
            log.error("Corvus Integration plugin disabled: Corvus application components could not be imported.")
            return

        self.api.add_menu_action(
            menu_name="tools",
            text="Corvus Chat...",
            callback=self.show_chat_panel,
            icon_name="fa5s.crow"
        )
        log.info("Corvus Integration plugin initialized.")

    def show_chat_panel(self):
        if self.chat_widget_instance and self.chat_widget_instance.parent():
            dock = self.chat_widget_instance.parent()
            while dock and not isinstance(dock, self.api.get_main_window().ClosableDockWidget):
                dock = dock.parent()
            
            if dock:
                dock.show()
                dock.raise_()
            return

        self.chat_widget_instance = CorvusChatWidget(self.api)

        self.api.add_dock_panel(
            widget=self.chat_widget_instance,
            title="Corvus Chat",
            area_str="bottom",
            icon_name="fa5s.robot"
        )

def initialize(koromali_api: KoromaliPluginAPI):
    if not CORVUS_AVAILABLE:
        return None
    return CorvusIntegrationPlugin(koromali_api)