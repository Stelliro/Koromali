# Koromali/app_core/highlighters/html_syntax_highlighter.py
from typing import TYPE_CHECKING
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager


class HtmlSyntaxHighlighter(QSyntaxHighlighter):
    """A syntax highlighter for HTML code."""

    def __init__(self, parent_document, theme_manager: "ThemeManager"):
        super().__init__(parent_document)
        self.theme_manager = theme_manager
        self.rules = []
        self.multiline_comment_format = QTextCharFormat()
        self.initialize_formats_and_rules()
        log.info("HtmlSyntaxHighlighter initialized.")

    def initialize_formats_and_rules(self):
        formats = {}
        colors = self.theme_manager.current_theme_data.get("colors", {})

        def get_color(key, fallback):
            return QColor(colors.get(f"syntax.{key}", fallback))

        # Format for tags like <p>, <div>
        tag_format = QTextCharFormat()
        tag_format.setForeground(get_color("keyword", "#e67e80"))

        # Format for attributes like href, class
        attribute_format = QTextCharFormat()
        attribute_format.setForeground(get_color("className", "#dbbc7f"))
        attribute_format.setFontItalic(True)

        # Format for attribute values like "styles.css"
        value_format = QTextCharFormat()
        value_format.setForeground(get_color("string", "#a7c080"))

        # Format for HTML comments <!-- ... -->
        comment_format = QTextCharFormat()
        comment_format.setForeground(get_color("comment", "#5f6c6d"))
        comment_format.setFontItalic(True)
        self.multiline_comment_format = comment_format

        # Format for DOCTYPE
        doctype_format = QTextCharFormat()
        doctype_format.setForeground(get_color("decorator", "#dbbc7f"))

        self.rules = [
            # Tags: <tag>, </tag>, <tag/>
            (QRegularExpression(r"</?([a-zA-Z0-9_-]+)"), tag_format),
            # Attributes: href=, class=
            (QRegularExpression(r'\b([a-zA-Z_-]+)(?=\s*=)'), attribute_format),
            # Attribute values in quotes
            (QRegularExpression(r'"[^"]*"'), value_format),
            (QRegularExpression(r"'[^']*'"), value_format),
            # DOCTYPE
            (QRegularExpression(r'<!DOCTYPE[^>]*>'), doctype_format),
        ]

        self.comment_start_expression = QRegularExpression(r"<!--")
        self.comment_end_expression = QRegularExpression(r"-->")

    def highlightBlock(self, text: str):
        # Apply single-line rules first
        for pattern, fmt in self.rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
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