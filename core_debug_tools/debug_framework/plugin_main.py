# Koromali/core_debug_tools/debug_framework/plugin_main.py
from utils.logger import log
from .api import KoromaliDebugAPI
from .debug_window import DebugWindow
from app_core.koromali_api import KoromaliPluginAPI


class DebugFrameworkPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.koromali_api = koromali_api
        self.main_window = self.koromali_api.get_main_window()
        self.debug_window = None

        log.info("Initializing Debug Tools Framework...")

        self.koromali_api.add_menu_action(
            menu_name="debug",
            text="Show Debugger",
            callback=self.show_debugger_window,
            icon_name="fa5s.bug"
        )

        if not hasattr(self.main_window, 'debug_api'):
            self.main_window.debug_api = KoromaliDebugAPI(self)

        log.info("Debug Framework initialized and attached to MainWindow.")

    def show_debugger_window(self):
        if not self.debug_window or not self.debug_window.isVisible():
            self.debug_window = DebugWindow(self.koromali_api, self.main_window)
            # Re-register tools
            if hasattr(self.main_window, 'debug_api'):
                for name, widget_class in self.main_window.debug_api.registered_tools.items():
                    self.debug_window.add_tool_tab(name, widget_class)

        self.debug_window.show()
        self.debug_window.raise_()
        self.debug_window.activateWindow()

    def add_tool_tab(self, tool_name: str, widget_class: type):
        if self.debug_window:
            self.debug_window.add_tool_tab(tool_name, widget_class)


def initialize(koromali_api: KoromaliPluginAPI):
    return DebugFrameworkPlugin(koromali_api)