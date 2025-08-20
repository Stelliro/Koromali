# Koromali/app_core/highlighters/rust_syntax_highlighter.py
from typing import Dict, List, Tuple, TYPE_CHECKING
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager


class RustSyntaxHighlighter(QSyntaxHighlighter):
    """A syntax highlighter for Rust code."""

    def __init__(self, parent_document, theme_manager: "ThemeManager"):
        super().__init__(parent_document)
        self.theme_manager = theme_manager
        self.highlighting_rules: List[Tuple[QRegularExpression, QTextCharFormat]] = []
        self.multiline_comment_format = QTextCharFormat()
        self.initialize_formats_and_rules()
        log.info("RustSyntaxHighlighter initialized.")

    def initialize_formats_and_rules(self):
        """Initializes all text formats and regular expression rules based on the theme."""
        self.formats: Dict[str, QTextCharFormat] = {}
        colors = self.theme_manager.current_theme_data.get("colors", {})

        def get_color(key: str, fallback: str) -> QColor:
            return QColor(colors.get(f"syntax.{key}", fallback))

        self.formats["keyword"] = QTextCharFormat()
        self.formats["keyword"].setForeground(get_color("keyword", "#e67e80"))
        self.formats["keyword"].setFontWeight(QFont.Weight.Bold)

        self.formats["special"] = QTextCharFormat()
        self.formats["special"].setForeground(get_color("self", "#e67e80"))
        self.formats["special"].setFontItalic(True)

        self.formats["attribute"] = QTextCharFormat()
        self.formats["attribute"].setForeground(get_color("decorator", "#dbbc7f"))

        self.formats["macro"] = QTextCharFormat()
        self.formats["macro"].setForeground(get_color("decorator", "#dbbc7f"))

        self.formats["type"] = QTextCharFormat()
        self.formats["type"].setForeground(get_color("className", "#dbbc7f"))

        self.formats["functionName"] = QTextCharFormat()
        self.formats["functionName"].setForeground(get_color("functionName", "#83c092"))

        self.formats["comment"] = QTextCharFormat()
        self.formats["comment"].setForeground(get_color("comment", "#5f6c6d"))
        self.formats["comment"].setFontItalic(True)
        self.multiline_comment_format = self.formats["comment"]

        self.formats["string"] = QTextCharFormat()
        self.formats["string"].setForeground(get_color("string", "#a7c080"))

        self.formats["number"] = QTextCharFormat()
        self.formats["number"].setForeground(get_color("number", "#d699b6"))

        self.highlighting_rules = []
        keywords = [
            r'\b(as|break|const|continue|crate|else|enum|extern|false|fn|for|if|impl|in|let|loop|match|mod|move|mut|pub|ref|return|static|struct|super|trait|true|type|unsafe|use|where|while|async|await|dyn)\b'
        ]
        self.highlighting_rules += [(QRegularExpression(p), self.formats["keyword"]) for p in keywords]
        special_keywords = [r'\b(self|Self)\b']
        self.highlighting_rules += [(QRegularExpression(p), self.formats["special"]) for p in special_keywords]
        self.highlighting_rules.extend([
            (QRegularExpression(r"#\!\[[^\]]+\]|#\[[^\]]+\]"), self.formats["attribute"]),
            (QRegularExpression(r"\b([a-zA-Z0-9_]+)!\b"), self.formats["macro"]),
            (QRegularExpression(r'\b[A-Z][a-zA-Z0-9_]*\b'), self.formats["type"]),
            (QRegularExpression(r'\b(fn)\s+([a-zA-Z_][a-zA-Z0-9_]*)'), self._format_function_definition),
            (QRegularExpression(r"'\w+"), self.formats["special"]),
            (QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"'), self.formats["string"]),
            (QRegularExpression(r'\b[0-9]+(_[0-9]+)*\.?[0-9]*\b'), self.formats["number"]),
            (QRegularExpression(r'//.*'), self.formats["comment"]),
        ])
        self.comment_start_expression = QRegularExpression(r"/\*")
        self.comment_end_expression = QRegularExpression(r"\*/")

    def _format_function_definition(self, match):
        """Custom formatter to style `fn` as keyword and name as functionName."""
        self.setFormat(match.capturedStart(1), match.capturedLength(1), self.formats["keyword"])
        self.setFormat(match.capturedStart(2), match.capturedLength(2), self.formats["functionName"])

    def highlightBlock(self, text: str):
        for pattern, fmt in self.highlighting_rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                if callable(fmt):
                    fmt(match)
                else:
                    self.setFormat(match.capturedStart(), match.capturedLength(), fmt)

        self.setCurrentBlockState(0)
        search_index = 0

        # Elegantly handle continuation from a previous block
        if self.previousBlockState() == 1:
            end_match = self.comment_end_expression.match(text, 0)
            if not end_match.hasMatch():
                # The entire block is a comment, our work is simple and swift.
                self.setCurrentBlockState(1)
                self.setFormat(0, len(text), self.multiline_comment_format)
                return

            # The comment concludes, we find our new starting point.
            length = end_match.capturedEnd()
            self.setFormat(0, length, self.multiline_comment_format)
            search_index = length

        # Now, we seek new comments with a more expressive loop.
        while (start_match := self.comment_start_expression.match(text, search_index)).hasMatch():
            start_pos = start_match.capturedStart()
            end_match = self.comment_end_expression.match(text, start_pos + start_match.capturedLength())

            if not end_match.hasMatch():
                # An unclosed comment, a cliffhanger for the next block.
                self.setCurrentBlockState(1)
                self.setFormat(start_pos, len(text) - start_pos, self.multiline_comment_format)
                return  # Our tale for this block is told.

            # A complete, self-contained comment.
            length = end_match.capturedEnd() - start_pos
            self.setFormat(start_pos, length, self.multiline_comment_format)
            search_index = end_match.capturedEnd()

    def rehighlight(self):
        self.initialize_formats_and_rules()
        super().rehighlight()