# Koromali/plugins/script_runner/output_panel.py
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QDockWidget, QTextEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtGui import QFont, QColor, QTextCursor
from PyQt6.QtCore import Qt

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager
    from app_core.settings_manager import SettingsManager


class OutputPanel(QDockWidget):
    def __init__(self, theme_manager: "ThemeManager", settings_manager: "SettingsManager", parent=None):
        super().__init__("Output", parent)
        self.theme_manager = theme_manager
        self.settings_manager = settings_manager
        self.setObjectName("OutputPanelDock")
        self.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea |
                             Qt.DockWidgetArea.RightDockWidgetArea)

        self.container_widget = QWidget()
        self.layout = QVBoxLayout(self.container_widget)
        self.layout.setContentsMargins(2, 2, 2, 2)

        self.control_bar_layout = QHBoxLayout()
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_output)
        self.control_bar_layout.addWidget(self.clear_button)
        self.control_bar_layout.addStretch(1)
        self.layout.addLayout(self.control_bar_layout)

        self.output_text_edit = QTextEdit()
        self.output_text_edit.setReadOnly(True)
        self.layout.addWidget(self.output_text_edit)

        self.container_widget.setLayout(self.layout)
        self.setWidget(self.container_widget)

        self.update_theme()

    def append_output(self, text: str, is_error: bool = False):
        """
        Appends text to the output panel, handling color for errors.

        This method uses a QTextCursor to ensure text is appended without
        introducing extra newlines, preserving the raw output from the process.
        """
        cursor = self.output_text_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.output_text_edit.setTextCursor(cursor)

        original_format = cursor.charFormat()

        if is_error:
            colors = self.theme_manager.current_theme_data.get("colors", {})
            error_color_hex = colors.get("syntax.comment", "#FF4444")
            error_color = QColor(error_color_hex if error_color_hex else "#FF0000")

            error_format = cursor.charFormat()
            error_format.setForeground(error_color)
            cursor.setCharFormat(error_format)

        # Insert text without adding an automatic newline
        cursor.insertText(text)

        # Restore the original format for subsequent text
        if is_error:
            cursor.setCharFormat(original_format)

        # Keep scrolled to the bottom
        scrollbar = self.output_text_edit.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def clear_output(self):
        self.output_text_edit.clear()

    def update_theme(self):
        font_family = self.settings_manager.get("font_family", "Consolas")
        font_size = self.settings_manager.get("font_size", 10)
        font = QFont(font_family, font_size)
        self.output_text_edit.setFont(font)

        colors = self.theme_manager.current_theme_data.get("colors", {})
        bg_color = colors.get("editor.background", "#1e1e1e")
        fg_color = colors.get("editor.foreground", "#d4d4d4")
        self.output_text_edit.setStyleSheet(f"background-color: {bg_color}; "
                                              f"color: {fg_color}; border: none;")