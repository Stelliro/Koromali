# Koromali/app_core/highlighters/css_syntax_highlighter.py
from typing import Dict, List, Tuple, TYPE_CHECKING
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager


class CssSyntaxHighlighter(QSyntaxHighlighter):
    """A syntax highlighter for CSS stylesheets."""

    def __init__(self, parent_document, theme_manager: "ThemeManager"):
        super().__init__(parent_document)
        self.theme_manager = theme_manager
        self.highlighting_rules: List[Tuple[QRegularExpression, QTextCharFormat]] = []
        self.multiline_comment_format = QTextCharFormat()

        self.initialize_formats_and_rules()
        log.info("CssSyntaxHighlighter initialized.")

    def initialize_formats_and_rules(self):
        """Initializes all text formats based on the current theme and sets up regex rules."""
        formats: Dict[str, QTextCharFormat] = {}
        colors = self.theme_manager.current_theme_data.get("colors", {})

        def get_color(key: str, fallback: str) -> QColor:
            # Re-use existing theme colors for consistency
            return QColor(colors.get(f"syntax.{key}", fallback))

        # Tag selectors, keywords like 'bold'
        formats["keyword"] = QTextCharFormat()
        formats["keyword"].setForeground(get_color("keyword", "#e67e80"))

        # Properties like 'color', 'font-size'
        formats["property"] = QTextCharFormat()
        formats["property"].setForeground(get_color("functionName", "#83c092"))

        # Class selectors like '.my-class'
        formats["class_selector"] = QTextCharFormat()
        formats["class_selector"].setForeground(get_color("className", "#dbbc7f"))
        
        # ID selectors like '#my-id', and at-rules like '@media'
        formats["at_rule_and_id"] = QTextCharFormat()
        formats["at_rule_and_id"].setForeground(get_color("decorator", "#dbbc7f"))

        # Values: numbers, units, colors
        formats["value_number"] = QTextCharFormat()
        formats["value_number"].setForeground(get_color("number", "#d699b6"))

        # Values: strings
        formats["value_string"] = QTextCharFormat()
        formats["value_string"].setForeground(get_color("string", "#a7c080"))

        # Braces, colons, etc.
        formats["operator"] = QTextCharFormat()
        formats["operator"].setForeground(get_color("operator", "#d3c6aa"))
        
        # Comments '/* ... */'
        formats["comment"] = QTextCharFormat()
        formats["comment"].setForeground(get_color("comment", "#5f6c6d"))
        formats["comment"].setFontItalic(True)
        self.multiline_comment_format = formats["comment"]
        
        # Build Rule List
        self.highlighting_rules = []

        # At-rules, e.g., @media, @keyframes
        self.highlighting_rules.append(
            (QRegularExpression(r"@[a-zA-Z_-]+"), formats["at_rule_and_id"])
        )

        # ID selector, e.g., #header
        self.highlighting_rules.append(
            (QRegularExpression(r"#[a-zA-Z0-9_-]+"), formats["at_rule_and_id"])
        )

        # Class selector, e.g., .container
        self.highlighting_rules.append(
            (QRegularExpression(r"\.[a-zA-Z0-9_-]+"), formats["class_selector"])
        )
        
        # Tag selectors (div, p, h1) and pseudo-classes (:hover)
        self.highlighting_rules.append(
            (QRegularExpression(r"\b([a-zA-Z_-]+)(?=\s*\{|::?[a-zA-Z-]+)"), formats["keyword"])
        )
        
        # Properties, e.g., color:, font-weight:
        self.highlighting_rules.append(
            (QRegularExpression(r"([a-zA-Z-]+)(?=\s*:)"), formats["property"])
        )
        
        # String values
        self.highlighting_rules.append(
            (QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"'), formats["value_string"])
        )
        self.highlighting_rules.append(
            (QRegularExpression(r"'[^'\\]*(\\.[^'\\]*)*'"), formats["value_string"])
        )
        
        # Number values (pixels, percentages, colors), e.g. 12px, 80%, #fff, rgb(...)
        self.highlighting_rules.append(
            (QRegularExpression(r"(-?\d+(\.\d+)?(px|em|rem|%|pt|vh|vw)?|#[0-9a-fA-F]{3,6})"), formats["value_number"])
        )

        # Keyword values, e.g. bold, block, sans-serif
        keywords = [
            'auto', 'bold', 'italic', 'normal', 'none', 'solid', 'dotted', 'dashed', 'double',
            'inherit', 'initial', 'unset', 'block', 'inline', 'flex', 'grid', 'absolute', 'relative',
            'static', 'fixed', 'sticky', 'center', 'left', 'right', 'justify'
        ]
        self.highlighting_rules += [
            (QRegularExpression(f"\\b{word}\\b"), formats["keyword"]) for word in keywords
        ]
        
        # Braces and operators
        self.highlighting_rules.append(
             (QRegularExpression(r"\{|\}|:|;"), formats["operator"])
        )
        
        # For multiline comments /* ... */
        self.comment_start_expression = QRegularExpression(r"/\*")
        self.comment_end_expression = QRegularExpression(r"\*/")

    def highlightBlock(self, text: str):
        # Apply single-line rules first
        for pattern, fmt in self.highlighting_rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)

        self.setCurrentBlockState(0)
        search_index = 0

        # Handle multiline comments
        if self.previousBlockState() == 1:
            end_match = self.comment_end_expression.match(text, 0)
            if not end_match.hasMatch():
                self.setCurrentBlockState(1)
                self.setFormat(0, len(text), self.multiline_comment_format)
                return

            length = end_match.capturedEnd()
            self.setFormat(0, length, self.multiline_comment_format)
            search_index = length

        while (start_match := self.comment_start_expression.match(text, search_index)).hasMatch():
            start_pos = start_match.capturedStart()
            end_match = self.comment_end_expression.match(text, start_pos + start_match.capturedLength())

            if not end_match.hasMatch():
                self.setCurrentBlockState(1)
                self.setFormat(start_pos, len(text) - start_pos, self.multiline_comment_format)
                return

            length = end_match.capturedEnd() - start_pos
            self.setFormat(start_pos, length, self.multiline_comment_format)
            search_index = end_match.capturedEnd()

    def rehighlight(self):
        """Forces a re-highlight of the entire document, usually on theme change."""
        self.initialize_formats_and_rules()
        super().rehighlight()