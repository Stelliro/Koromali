# Koromali/core_debug_tools/debug_framework/debug_window.py
from typing import Type
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget
from PyQt6.QtCore import QSize


class DebugWindow(QMainWindow):
    """A floating window that hosts various debugging tool widgets in tabs."""

    def __init__(self, koromali_api, parent=None):
        super().__init__(parent)
        self.koromali_api = koromali_api
        self.setWindowTitle("Koromali - Debugger")
        self.setMinimumSize(QSize(800, 600))

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setDocumentMode(True)

        self.setCentralWidget(self.tab_widget)
        self.tools = {}

    def add_tool_tab(self, tool_name: str, widget_class: Type[QWidget]):
        """Creates an instance of the widget class and adds it as a tab."""
        if tool_name in self.tools:
            return  # Avoid duplicate tabs

        # Pass the main Koromali API to the tool if it needs it
        tool_instance = widget_class(self.koromali_api)
        self.tab_widget.addTab(tool_instance, tool_name)
        self.tools[tool_name] = tool_instance