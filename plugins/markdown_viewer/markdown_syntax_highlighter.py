# /plugins/markdown_viewer/markdown_syntax_highlighter.py
from typing import TYPE_CHECKING
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression, Qt

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager


class MarkdownSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent_document, theme_manager: "ThemeManager"):
        super().__init__(parent_document)
        self.theme_manager = theme_manager
        self.formats = {}
        self.rules = []
        # Fallback to a default color if something goes wrong
        default_fg_color = self.theme_manager.current_theme_data.get("colors", {}).get("editor.foreground", "#ffffff")
        self.default_fg = QColor(default_fg_color)
        self.initialize_formats_and_rules()

    def _get_high_contrast_color(self, fg_color: QColor, bg_color: QColor) -> QColor:
        CONTRAST_THRESHOLD = 80
        fg_lightness = fg_color.lightness()
        bg_lightness = bg_color.lightness()

        if abs(fg_lightness - bg_lightness) < CONTRAST_THRESHOLD:
            return QColor(Qt.GlobalColor.white) if bg_lightness < 128 else QColor(Qt.GlobalColor.black)
        return fg_color

    def initialize_formats_and_rules(self):
        colors = self.theme_manager.current_theme_data.get("colors", {})
        editor_bg = QColor(colors.get('editor.background', '#2b2b2b'))
        accent = QColor(colors.get('accent', '#88c0d0'))
        comment_color = QColor(colors.get('syntax.comment', '#808080'))

        self.formats['marker'] = QTextCharFormat()
        self.formats['marker'].setForeground(editor_bg.lighter(150))
        self.formats['marker'].setFontWeight(QFont.Weight.Bold)
        self.formats['blockquote'] = QTextCharFormat()
        self.formats['blockquote'].setForeground(comment_color)
        self.formats['blockquote'].setFontItalic(True)
        self.formats['hr'] = QTextCharFormat()
        self.formats['hr'].setForeground(editor_bg.lighter(130))
        self.formats['hr'].setFontWeight(QFont.Weight.Bold)

        base_heading_format = QTextCharFormat()
        base_heading_format.setFontWeight(QFont.Weight.Bold)
        base_heading_format.setForeground(accent)
        for i in range(1, 7):
            self.formats[f'h{i}'] = QTextCharFormat(base_heading_format)
            self.formats[f'h{i}'].setFontPointSize(22 - (i - 1) * 2)

        self.formats['bold'] = QTextCharFormat()
        self.formats['bold'].setFontWeight(QFont.Weight.Bold)
        self.formats['italic'] = QTextCharFormat()
        self.formats['italic'].setFontItalic(True)
        self.formats['strikethrough'] = QTextCharFormat()
        self.formats['strikethrough'].setFontStrikeOut(True)

        code_block_bg_color = QColor(colors.get('editor.lineHighlightBackground', '#323232'))
        self.formats['code_block'] = QTextCharFormat()
        self.formats['code_block'].setBackground(code_block_bg_color)
        self.formats['code_block'].setFontFamily("Consolas")

        self.formats['inline_code'] = QTextCharFormat()
        original_inline_code_fg = QColor(colors.get('syntax.string', '#a7c080'))
        final_inline_code_fg = self._get_high_contrast_color(original_inline_code_fg, code_block_bg_color)
        self.formats['inline_code'].setBackground(code_block_bg_color)
        self.formats['inline_code'].setForeground(final_inline_code_fg)
        self.formats['inline_code'].setFontFamily("Consolas")

        self.rules = [
            (QRegularExpression(r"^(#{1,6})\s"), self._format_heading),
            (QRegularExpression(r"^>+\s?"), self._format_simple('blockquote')),
            (QRegularExpression(r"^[-_*]{3,}\s*$"), self._format_simple('hr')),
            (QRegularExpression(r"^(\s*[\*\-\+]\s)"), self._format_marker_only()),
            (QRegularExpression(r"^(\s*[0-9]+\.\s)"), self._format_marker_only()),
            (QRegularExpression(r"(\*\*)(\S.*?\S)(\*\*)"), self._format_inline('bold')),
            (QRegularExpression(r"(\*)(\S.*?\S)(\*)"), self._format_inline('italic')),
            (QRegularExpression(r"(__)(\S.*?\S)(__)"), self._format_inline('bold')),
            (QRegularExpression(r"(_)(\S.*?\S)(_)"), self._format_inline('italic')),
            (QRegularExpression(r"(~~)([^~]+)(~~)"), self._format_inline('strikethrough')),
            (QRegularExpression(r"(`)([^`]+)(`)"), self._format_inline('inline_code')),
        ]
        self.code_block_delimiter = QRegularExpression(r"^```")

    def _format_simple(self, fmt_name):
        return lambda match: self.setFormat(match.capturedStart(0), match.capturedLength(0), self.formats[fmt_name])

    def _format_marker_only(self):
        return lambda match: self.setFormat(match.capturedStart(1), match.capturedLength(1), self.formats['marker'])

    def _format_heading(self, match):
        level = len(match.captured(1))
        self.setFormat(match.capturedStart(1), level, self.formats['marker'])
        self.setFormat(match.capturedEnd(1), self.currentBlock().length() - match.capturedEnd(1),
                       self.formats[f'h{level}'])

    def _format_inline(self, fmt_name):
        def formatter(match):
            self.setFormat(match.capturedStart(2), len(match.captured(2)), self.formats[fmt_name])
            marker_format = self.formats['inline_code'] if fmt_name == 'inline_code' else self.formats['marker']
            self.setFormat(match.capturedStart(1), len(match.captured(1)), marker_format)
            self.setFormat(match.capturedStart(3), len(match.captured(3)), marker_format)

        return formatter

    def highlightBlock(self, text: str):
        # State 0: Normal text, State 1: Inside a code block
        is_in_code_block = self.previousBlockState() == 1
        delimiter_match = self.code_block_delimiter.match(text)

        if is_in_code_block:
            if delimiter_match.hasMatch():
                # We are at the end of a code block, so mark this line
                # as a delimiter and switch state back to normal.
                self.setCurrentBlockState(0)
                self.setFormat(0, len(text), self.formats['marker'])
            else:
                # We are still inside a code block. Apply the block format.
                self.setCurrentBlockState(1)
                code_bg = self.formats['code_block'].background().color()
                corrected_fg = self._get_high_contrast_color(self.default_fg, code_bg)
                block_format = QTextCharFormat(self.formats['code_block'])
                block_format.setForeground(corrected_fg)
                self.setFormat(0, len(text), block_format)
        else:  # Normal text block
            if delimiter_match.hasMatch():
                # This is the start of a new code block. Mark the delimiter
                # line and switch the state for the next block.
                self.setCurrentBlockState(1)
                self.setFormat(0, len(text), self.formats['marker'])
            else:
                # This is a normal text line. Reset state and apply inline rules.
                self.setCurrentBlockState(0)
                for pattern, formatter in self.rules:
                    iterator = pattern.globalMatch(text)
                    while iterator.hasNext():
                        match = iterator.next()
                        formatter(match)

    def rehighlight(self):
        default_fg_color = self.theme_manager.current_theme_data.get("colors", {}).get("editor.foreground", "#ffffff")
        self.default_fg = QColor(default_fg_color)
        self.initialize_formats_and_rules()
        super().rehighlight()