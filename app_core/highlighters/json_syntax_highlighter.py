# Koromali/app_core/highlighters/json_syntax_highlighter.py
from typing import TYPE_CHECKING
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager

class JsonSyntaxHighlighter(QSyntaxHighlighter):
    """A syntax highlighter for JSON files."""

    def __init__(self, parent_document, theme_manager: "ThemeManager"):
        super().__init__(parent_document)
        self.theme_manager = theme_manager
        self.highlighting_rules = []
        self.initialize_formats_and_rules()
        log.info("JsonSyntaxHighlighter initialized.")

    def initialize_formats_and_rules(self):
        """Initializes formats and rules based on the current theme."""
        colors = self.theme_manager.current_theme_data.get("colors", {})

        def get_color(key: str, fallback: str) -> QColor:
            return QColor(colors.get(f"syntax.{key}", fallback))

        key_format = QTextCharFormat()
        key_format.setForeground(get_color("className", "#dbbc7f"))

        string_format = QTextCharFormat()
        string_format.setForeground(get_color("string", "#a7c080"))

        number_format = QTextCharFormat()
        number_format.setForeground(get_color("number", "#d699b6"))

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(get_color("keyword", "#e67e80"))
        keyword_format.setFontWeight(QFont.Weight.Bold)

        brace_format = QTextCharFormat()
        brace_format.setForeground(get_color("brace", "#d3c6aa"))

        self.highlighting_rules = [
            (QRegularExpression(r'[\{\}\[\]]'), brace_format),
            (QRegularExpression(r'\b(true|false|null)\b'), keyword_format),
            (QRegularExpression(r'\b-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?\b'), number_format),

            # The more specific rule (key) now comes BEFORE the generic rule (string).
            # This correctly identifies strings followed by a colon as keys.
            (QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"(?=\s*:)'), key_format),
            (QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"'), string_format),
        ]

    def highlightBlock(self, text: str):
        """Highlights a single block of text."""
        for pattern, fmt in self.highlighting_rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)

    def rehighlight(self):
        """Re-initializes formats and rules, called when the theme changes."""
        self.initialize_formats_and_rules()
        super().rehighlight()