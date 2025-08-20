# /plugins/markdown_viewer/markdown_editor_widget.py
import qtawesome as qta
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextBrowser,
    QSplitter, QMenu, QToolButton, QFrame, QPlainTextEdit
)
from PyQt6.QtGui import QFont, QTextCursor, QAction
from PyQt6.QtCore import QTimer, pyqtSignal, Qt
from markdown import markdown

from app_core.koromali_api import KoromaliPluginAPI
from .markdown_syntax_highlighter import MarkdownSyntaxHighlighter
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager
    from app_core.settings_manager import SettingsManager

class MarkdownFormattingToolbar(QWidget):
    format_bold_requested = pyqtSignal()
    format_italic_requested = pyqtSignal()
    format_strikethrough_requested = pyqtSignal()
    format_inline_code_requested = pyqtSignal()
    heading_level_requested = pyqtSignal(int)
    code_block_requested = pyqtSignal()
    def __init__(self, theme_manager: "ThemeManager", parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.setWindowFlags(Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.frame = QFrame(self)
        self.frame.setObjectName("FormattingToolbarFrame")
        layout = QHBoxLayout(self.frame)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)
        self._add_tool_button("fa5s.bold", "Bold (Ctrl+B)", self.format_bold_requested)
        self._add_tool_button("fa5s.italic", "Italic (Ctrl+I)", self.format_italic_requested)
        self._add_tool_button("fa5s.strikethrough", "Strikethrough", self.format_strikethrough_requested)
        self._add_tool_button("fa5s.code", "Inline Code", self.format_inline_code_requested)
        layout.addWidget(self._create_separator())
        self._create_heading_menu()
        layout.addWidget(self._create_separator())
        self._add_tool_button("fa5s.file-code", "Insert Code Block", self.code_block_requested)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.frame)
        self.update_theme()
    def _add_tool_button(self, icon_name, tooltip, signal_to_emit):
        button = QToolButton()
        button.setIcon(qta.icon(icon_name, color='white'))
        button.setToolTip(tooltip)
        button.clicked.connect(signal_to_emit.emit)
        self.frame.layout().addWidget(button)
    def _create_separator(self):
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        return separator
    def _create_heading_menu(self):
        button = QToolButton()
        button.setIcon(qta.icon("fa5s.heading", color='white'))
        button.setToolTip("Apply Heading")
        button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        menu = QMenu(self)
        for i in range(1, 7):
            action = QAction(f"Heading {i}", self)
            action.triggered.connect(lambda _, level=i: self.heading_level_requested.emit(level))
            menu.addAction(action)
        button.setMenu(menu)
        self.frame.layout().addWidget(button)
    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        bg, border, accent = colors.get('menu.background', '#3a4145'), colors.get('input.border', '#555555'), colors.get('accent', '#88c0d0')
        self.setStyleSheet(f"""#FormattingToolbarFrame {{ background-color: {bg}; border: 1px solid {border}; border-radius: 6px; }} QToolButton {{ background: transparent; border: none; padding: 5px; border-radius: 4px; }} QToolButton:hover {{ background-color: {accent}; }} QFrame[frameShape="5"] {{ color: {border}; }}""")
    def show_at(self, global_pos):
        self.move(global_pos)
        self.show()
        self.activateWindow()
    def focusOutEvent(self, event):
        self.hide()
        super().focusOutEvent(event)


class MarkdownEditorWidget(QWidget):
    content_changed = pyqtSignal()
    
    def __init__(self, koromali_api: KoromaliPluginAPI, parent=None):
        super().__init__(parent)
        self.api = koromali_api
        self.theme_manager = self.api.get_manager("theme")
        self.settings_manager = self.api.get_manager("settings")
        self.filepath = None
        self.original_hash = 0
        self.is_syncing_scroll = False
        self.formatting_toolbar = MarkdownFormattingToolbar(self.theme_manager, self)
        
        self.editor = QPlainTextEdit(self)
        self.editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.highlighter = MarkdownSyntaxHighlighter(self.editor.document(), self.theme_manager)

        self._setup_ui()
        self._connect_signals()
        self.update_theme()
        
    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.viewer = QTextBrowser()
        self.viewer.setOpenExternalLinks(True)
        splitter = QSplitter(self)
        splitter.addWidget(self.editor) 
        splitter.addWidget(self.viewer)
        splitter.setSizes([self.width() // 2, self.width() // 2])
        layout.addWidget(splitter)

    def _connect_signals(self):
        self.update_timer = QTimer(self)
        self.update_timer.setSingleShot(True)
        self.update_timer.setInterval(250)
        self.update_timer.timeout.connect(self._render_preview)
        self.editor.textChanged.connect(self.update_timer.start)
        self.editor.textChanged.connect(self.content_changed.emit)
        
        self.formatting_toolbar.format_bold_requested.connect(lambda: self._wrap_selection("**"))
        self.formatting_toolbar.format_italic_requested.connect(lambda: self._wrap_selection("*"))
        self.formatting_toolbar.format_strikethrough_requested.connect(lambda: self._wrap_selection("~~"))
        self.formatting_toolbar.format_inline_code_requested.connect(lambda: self._wrap_selection("`"))
        self.formatting_toolbar.heading_level_requested.connect(self._format_heading)
        self.formatting_toolbar.code_block_requested.connect(self._insert_code_block)
        
        editor_scroll = self.editor.verticalScrollBar()
        viewer_scroll = self.viewer.verticalScrollBar()
        editor_scroll.valueChanged.connect(self._sync_scroll_from_editor)
        viewer_scroll.valueChanged.connect(self._sync_scroll_from_viewer)

    def contextMenuEvent(self, event):
        if self.editor.rect().contains(event.pos()):
            self.formatting_toolbar.show_at(event.globalPos())
        super().contextMenuEvent(event)

    def _wrap_selection(self, prefix, suffix=None):
        suffix = suffix or prefix
        cursor = self.editor.textCursor()
        if not cursor.hasSelection():
            cursor.insertText(f"{prefix}text{suffix}")
            cursor.movePosition(QTextCursor.MoveOperation.Left, n=len(suffix))
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.KeepAnchor, n=4)
        else:
            selected_text = cursor.selectedText()
            cursor.insertText(f"{prefix}{selected_text}{suffix}")
        self.editor.setTextCursor(cursor)

    def _format_heading(self, level):
        cursor = self.editor.textCursor()
        cursor.beginEditBlock()
        cursor.movePosition(QTextCursor.MoveOperation.StartOfBlock)
        cursor.insertText(f'{"#" * level} ')
        cursor.endEditBlock()

    def _insert_code_block(self):
        cursor = self.editor.textCursor()
        cursor.beginEditBlock()
        cursor.insertText("\n```python\n\n```\n")
        cursor.movePosition(QTextCursor.MoveOperation.Up, n=2)
        cursor.endEditBlock()
        self.editor.setTextCursor(cursor)

    def _sync_scroll_factory(self, source_bar, target_bar):
        def sync_scroll(value):
            if self.is_syncing_scroll: return
            self.is_syncing_scroll = True
            source_max = source_bar.maximum() or 1
            ratio = value / source_max
            target_bar.setValue(int(target_bar.maximum() * ratio))
            self.is_syncing_scroll = False
        return sync_scroll
        
    @property
    def _sync_scroll_from_editor(self):
        return self._sync_scroll_factory(self.editor.verticalScrollBar(), self.viewer.verticalScrollBar())
        
    @property
    def _sync_scroll_from_viewer(self):
        return self._sync_scroll_factory(self.viewer.verticalScrollBar(), self.editor.verticalScrollBar())

    def set_initial_content(self, filepath: str, content: str):
        """Sets the file path and initial content for the editor, avoiding redundant file reads."""
        self.filepath = filepath
        self.editor.setPlainText(content)
        self.original_hash = hash(content)
        self._render_preview() # Render the initial content immediately
        log.info(f"Markdown Editor: Successfully loaded content for '{filepath}'.")

    def get_text(self) -> str:
        return self.editor.toPlainText()

    def _render_preview(self):
        viewer_scroll = self.viewer.verticalScrollBar()
        scroll_max = viewer_scroll.maximum() or 1
        old_pos_ratio = viewer_scroll.value() / scroll_max
        md_text = self.get_text()
        html = markdown(md_text, extensions=['fenced_code', 'tables', 'extra', 'sane_lists'])
        self.viewer.setHtml(html)
        QTimer.singleShot(0, lambda: viewer_scroll.setValue(int(viewer_scroll.maximum() * old_pos_ratio)))
    
    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        font = QFont(self.settings_manager.get("font_family", "Consolas"), self.settings_manager.get("font_size", 11))
        self.editor.setFont(font)

        editor_bg = colors.get('editor.background', '#272e33')
        editor_fg = colors.get('editor.foreground', '#d3c6aa')
        selection_bg = colors.get('editor.selectionBackground', '#264f78')
        self.editor.setStyleSheet(f"""
            QPlainTextEdit {{
                background-color: {editor_bg};
                color: {editor_fg};
                border: none;
                selection-background-color: {selection_bg};
            }}
        """)
        
        viewer_bg = colors.get('editor.background', '#2b2b2b')
        string_color = colors.get('syntax.string', '#6A8759')
        accent_color = colors.get('accent', '#88c0d0')
        line_highlight_bg = colors.get('editor.lineHighlightBackground', '#323232')
        border_color = colors.get('input.border', '#555')
        comment_color = colors.get('syntax.comment', '#808080')
        
        style_sheet = f"""
            h1, h2, h3, h4, h5, h6 {{ color: {accent_color}; border-bottom: 1px solid {line_highlight_bg}; padding-bottom: 4px; margin-top: 15px; }}
            a {{ color: {string_color}; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            p, li {{ font-size: {font.pointSize()}pt; }}
            pre {{ background-color: {line_highlight_bg}; border: 1px solid {border_color}; border-radius: 4px; padding: 10px; font-family: "{font.family()}"; }}
            code {{ background-color: {line_highlight_bg}; font-family: "{font.family()}"; border-radius: 3px; padding: 2px 4px; }}
            blockquote {{ color: {comment_color}; border-left: 3px solid {accent_color}; padding-left: 15px; margin-left: 5px; font-style: italic; }}
            table {{ border-collapse: collapse; margin: 1em 0; }}
            th, td {{ border: 1px solid {border_color}; padding: 8px; }}
            th {{ background-color: {line_highlight_bg}; font-weight: bold; }}
        """
        doc = self.viewer.document()
        doc.setDefaultStyleSheet(style_sheet)
        doc.setDefaultFont(font)
        self.viewer.setStyleSheet(f"background-color: {viewer_bg}; border: none; padding: 10px;")
        
        if self.highlighter:
            self.highlighter.rehighlight()

        self.formatting_toolbar.update_theme()
        self._render_preview()