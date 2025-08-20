# Koromali/plugins/terminal/plugin_main.py
from PyQt6.QtCore import Qt
from utils.logger import log
from .terminal_widget import TerminalWidget
from app_core.koromali_api import KoromaliPluginAPI
import qtawesome as qta


class TerminalPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.terminal_widget = None

        self._setup_ui()
        log.info("Integrated Terminal plugin initialized.")

    def _setup_ui(self):
        """Creates and registers the terminal panel and menu action."""
        self.terminal_widget = TerminalWidget(self.api)

        # Use the simplified API to add the widget as a dockable panel.
        # This automatically handles registration with the hider manager and view menu.
        dock = self.api.add_dock_panel(
            widget=self.terminal_widget,
            title="Terminal",
            area_str="bottom",
            icon_name='mdi.console'
        )

        if dock and dock.toggleViewAction():
            # The API's add_dock_panel already adds the action to the "View > Docks" menu.
            # This logic ensures that if we want a direct "View -> Terminal" action, it exists.
            terminal_toggle_action = dock.toggleViewAction()
            terminal_toggle_action.setText("Terminal") # Ensure it has a good name in the menu
            terminal_toggle_action.setIcon(qta.icon('mdi.console'))
            # To avoid duplicates, we can check if an action with this text already exists.
            view_menu = self.api.get_menu("view")
            if view_menu and not any(a.text() == "Terminal" for a in view_menu.actions()):
                 view_menu.addAction(terminal_toggle_action)


    def shutdown(self):
        """
        Called by the plugin manager or main window to ensure the terminal's
        underlying shell process is terminated correctly.
        """
        if self.terminal_widget:
            self.terminal_widget.stop_process()
            log.info("Terminal process stopped on shutdown request.")


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for Koromali to load the plugin."""
    try:
        return TerminalPlugin(koromali_api)
    except Exception as e:
        log.error(f"Failed to initialize Terminal Plugin: {e}", exc_info=True)
        return None