# Koromali/app_core/highlighters/csharp_syntax_highlighter.py
from typing import List, Tuple, TYPE_CHECKING
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager


class CSharpSyntaxHighlighter(QSyntaxHighlighter):
    """A syntax highlighter for C# code."""

    def __init__(self, parent_document, theme_manager: "ThemeManager"):
        super().__init__(parent_document)
        self.theme_manager = theme_manager
        self.highlighting_rules: List[Tuple[QRegularExpression, QTextCharFormat]] = []
        self.multiline_comment_format = QTextCharFormat()
        self.initialize_formats_and_rules()
        log.info("CSharpSyntaxHighlighter initialized.")

    def initialize_formats_and_rules(self):
        formats = {}
        colors = self.theme_manager.current_theme_data.get("colors", {})

        def get_color(key: str, fallback: str) -> QColor:
            return QColor(colors.get(f"syntax.{key}", fallback))

        formats["keyword"] = QTextCharFormat()
        formats["keyword"].setForeground(get_color("keyword", "#e67e80"))
        formats["keyword"].setFontWeight(QFont.Weight.Bold)

        formats["preprocessor"] = QTextCharFormat()
        formats["preprocessor"].setForeground(get_color("decorator", "#dbbc7f"))

        formats["string"] = QTextCharFormat()
        formats["string"].setForeground(get_color("string", "#a7c080"))

        formats["comment"] = QTextCharFormat()
        formats["comment"].setForeground(get_color("comment", "#5f6c6d"))
        formats["comment"].setFontItalic(True)
        self.multiline_comment_format = formats["comment"]

        formats["number"] = QTextCharFormat()
        formats["number"].setForeground(get_color("number", "#d699b6"))

        formats["className"] = QTextCharFormat()
        formats["className"].setForeground(get_color("className", "#dbbc7f"))

        formats["functionName"] = QTextCharFormat()
        formats["functionName"].setForeground(get_color("functionName", "#83c092"))

        # Rule construction
        self.highlighting_rules = []

        keywords = [
            r'\babstract\b', r'\bas\b', r'\bbase\b', r'\bbool\b', r'\bbreak\b',
            r'\bbyte\b', r'\bcase\b', r'\bcatch\b', r'\bchar\b', r'\bchecked\b',
            r'\bclass\b', r'\bconst\b', r'\bcontinue\b', r'\bdecimal\b',
            r'\bdefault\b', r'\bdelegate\b', r'\bdo\b', r'\bdouble\b', r'\belse\b',
            r'\benum\b', r'\bevent\b', r'\bexplicit\b', r'\bextern\b', r'\bfalse\b',
            r'\bfinally\b', r'\bfixed\b', r'\bfloat\b', r'\bfor\b', r'\bforeach\b',
            r'\bgoto\b', r'\bif\b', r'\bimplicit\b', r'\bin\b', r'\bint\b',
            r'\binterface\b', r'\binternal\b', r'\bis\b', r'\block\b', r'\blong\b',
            r'\bnamespace\b', r'\bnew\b', r'\bnull\b', r'\bobject\b',
            r'\boperator\b', r'\bout\b', r'\boverride\b', r'\bparams\b',
            r'\bprivate\b', r'\bprotected\b', r'\bpublic\b', r'\breadonly\b',
            r'\bref\b', r'\breturn\b', r'\bsbyte\b', r'\bsealed\b', r'\bshort\b',
            r'\bsizeof\b', r'\bstackalloc\b', r'\bstatic\b', r'\bstring\b',
            r'\bstruct\b', r'\bswitch\b', r'\bthis\b', r'\bthrow\b', r'\btrue\b',
            r'\btry\b', r'\btypeof\b', r'\buint\b', r'\bulong\b', r'\bunchecked\b',
            r'\bunsafe\b', r'\bushort\b', r'\busing\b', r'\bvirtual\b',
            r'\bvoid\b', r'\bvolatile\b', r'\bwhile\b', r'\byield\b', r'\bvar\b'
        ]

        self.highlighting_rules += [(QRegularExpression(p), formats["keyword"]) for p in keywords]

        self.highlighting_rules.extend([
            (QRegularExpression(r'^\s*#[a-zA-Z_]+'), formats["preprocessor"]),
            (QRegularExpression(r'\b[A-Z][A-Za-z0-9_]*'), formats["className"]),
            (QRegularExpression(r'\b[A-Z][a-zA-Z0-9_]*(?=\s*\()'), formats["functionName"]),
            (QRegularExpression(r'"(?:[^"\\]|\\.)*"'), formats["string"]),
            (QRegularExpression(r"'\\?.'"), formats["string"]),
            (QRegularExpression(r'//.*'), formats["comment"]),
        ])

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