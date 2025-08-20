# Koromali/core_debug_tools/debug_framework/api.py
from typing import Dict, Type
from PyQt6.QtWidgets import QWidget
from utils.logger import log


class KoromaliDebugAPI:
    """A specialized API for debug-related plugins."""

    def __init__(self, debug_window_instance):
        self._debug_window = debug_window_instance
        self.registered_tools: Dict[str, Type[QWidget]] = {}
        log.info("KoromaliDebugAPI initialized.")

    def register_tool(self, tool_name: str, widget_class: Type[QWidget]):
        """
        Registers a widget to be shown in a tab in the main Debugger window.

        Args:
            tool_name: The name to be displayed on the tab.
            widget_class: The QWidget class (not an instance) to be
                          instantiated. The class constructor should accept
                          the main KoromaliAPI instance.
        """
        if tool_name in self.registered_tools:
            log.warning(
                f"Debug tool '{tool_name}' is already registered. Overwriting.")
        self.registered_tools[tool_name] = widget_class
        log.info(f"Registered new debug tool: {tool_name}")
        self._debug_window.add_tool_tab(tool_name, widget_class)