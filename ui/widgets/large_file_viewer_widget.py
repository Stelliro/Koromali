# /ui/widgets/large_file_viewer_widget.py
import os
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QFrame, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, pyqtSignal
import qtawesome as qta
from app_core.theme_manager import ThemeManager

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager

class LargeFileViewerWidget(QWidget):
    """A performance-optimized widget for viewing very large files."""
    content_possibly_changed = pyqtSignal()
    
    def __init__(self, theme_manager: ThemeManager, settings_manager: "SettingsManager"):
        super().__init__()
        self.theme_manager = theme_manager
        self.settings_manager = settings_manager
        self.filepath: str = ""
        self.original_hash = 0

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Warning banner
        self.warning_banner = QFrame()
        self.warning_banner.setObjectName("LargeFileWarningBanner")
        banner_layout = QHBoxLayout(self.warning_banner)
        icon_label = QLabel()
        icon_label.setPixmap(qta.icon('mdi.alert-outline', color='black').pixmap(16, 16))
        self.warning_label = QLabel("Large File Mode (Read-Only): Performance features like syntax highlighting are disabled.")
        self.edit_button = QPushButton("Edit Anyway")
        banner_layout.addWidget(icon_label)
        banner_layout.addWidget(self.warning_label, 1)
        banner_layout.addWidget(self.edit_button)
        main_layout.addWidget(self.warning_banner)

        # Text area
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        main_layout.addWidget(self.text_area)

    def _connect_signals(self):
        self.edit_button.clicked.connect(self._enable_editing)
        self.text_area.textChanged.connect(self.content_possibly_changed)

    def _enable_editing(self):
        self.text_area.setReadOnly(False)
        self.warning_label.setText("Editing enabled. Performance may be degraded.")
        self.edit_button.hide()

    def set_content(self, filepath: str, content: str):
        self.filepath = filepath
        self.original_hash = hash(content)
        self.text_area.setPlainText(content)
        self.update_theme()

    def get_text(self) -> str:
        return self.text_area.toPlainText()

    def goto_line_and_column(self, line, col):
        """Minimal implementation for go-to-line."""
        # QPlainTextEdit would be better, but QTextEdit is needed for banner
        cursor = self.text_area.textCursor()
        cursor.movePosition(cursor.MoveOperation.Start)
        cursor.movePosition(cursor.MoveOperation.Down, n=line-1)
        cursor.movePosition(cursor.MoveOperation.Right, n=col)
        self.text_area.setTextCursor(cursor)
        self.text_area.ensureCursorVisible()

    def update_theme(self):
        font = QFont(self.settings_manager.get("font_family"), self.settings_manager.get("font_size"))
        self.text_area.setFont(font)

        colors = self.theme_manager.current_theme_data.get("colors", {})
        editor_bg = colors.get('editor.background', '#272e33')
        editor_fg = colors.get('editor.foreground', '#d3c6aa')
        selection_bg = colors.get('editor.selectionBackground', '#264f78')
        warning_bg = colors.get('syntax.className', '#dbbc7f')

        self.setStyleSheet(f"""
            #LargeFileWarningBanner {{
                background-color: {warning_bg};
                border-bottom: 1px solid black;
                padding: 4px;
            }}
            #LargeFileWarningBanner QLabel, #LargeFileWarningBanner QPushButton {{
                color: black;
                background: transparent;
                border: none;
            }}
            #LargeFileWarningBanner QPushButton {{
                text-decoration: underline;
            }}
        """)
        self.text_area.setStyleSheet(f"""
            QTextEdit {{
                background-color: {editor_bg};
                color: {editor_fg};
                border: none;
                selection-background-color: {selection_bg};
            }}
        """)