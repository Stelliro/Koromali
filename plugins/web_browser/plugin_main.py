# /plugins/web_browser/plugin_main.py
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log

try:
    from .browser_widget import BrowserWidget, WEB_ENGINE_AVAILABLE
except ImportError as e:
    log.error(f"Web Browser plugin failed to import dependencies: {e}")
    WEB_ENGINE_AVAILABLE = False


class WebBrowserPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.browser_widget_instance = None
        
        self.api.add_menu_action(
            menu_name="tools",
            text="Private Browser",
            callback=self.open_browser_panel,
            icon_name="mdi.web"
        )

    def open_browser_panel(self):
        """Opens the private browser in a dockable panel."""
        if self.browser_widget_instance and self.browser_widget_instance.parent():
            dock = self.browser_widget_instance.parent()
            dock.show()
            dock.raise_()
            return

        self.browser_widget_instance = BrowserWidget(self.api)
        
        self.api.add_dock_panel(
            widget=self.browser_widget_instance,
            title="Private Browser",
            area_str="right",
            icon_name="mdi.web"
        )
        
        if not WEB_ENGINE_AVAILABLE:
            self.api.show_message(
                "critical",
                "Dependency Missing",
                "The Web Browser plugin requires PyQt6-WebEngine. Please install it by running:\npip install PyQt6-WebEngine"
            )


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for the Web Browser plugin."""
    if not WEB_ENGINE_AVAILABLE:
        log.error("Cannot initialize Web Browser plugin: PyQt6-WebEngine is not installed.")
        return None
        
    log.info("Web Browser plugin initialized.")
    return WebBrowserPlugin(koromali_api)