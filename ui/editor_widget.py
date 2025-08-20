# /ui/editor_widget.py
"""
Koromali - Editor Widget (Final, Fully-Featured Stable Version)
"""
from __future__ import annotations
from typing import Optional, Set, Dict, List, Tuple, TYPE_CHECKING
import re
import os
from math import cos, sin

from PyQt6.QtWidgets import (QWidget, QPlainTextEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QFrame, QSplitter,
                             QApplication, QStackedWidget, QToolButton, QScrollBar)
from PyQt6.QtGui import (QPainter, QColor, QFont, QPaintEvent, QTextFormat,
                         QTextBlockFormat, QPen, QTextCursor, QMouseEvent, QFontMetrics,
                         QKeyEvent, QTextDocument, QKeySequence, QWheelEvent, QPolygonF, QSyntaxHighlighter,
                         QTextOption, QResizeEvent)
from PyQt6.QtCore import (Qt, QSize, QRect, QRectF, QPointF, QEvent, pyqtSignal,
                          QObject, QTimer, QPoint, QPropertyAnimation, QEasingCurve)
import qtawesome as qta
from .widgets.find_panel import FindPanel
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager
    from app_core.koromali_api import KoromaliPluginAPI
    from .main_window import MainWindow
    from app_core.settings_manager import SettingsManager


class CustomTextArea(QPlainTextEdit):
    """
    A custom QPlainTextEdit that adds support for drawing indentation guides.
    """
    def __init__(self, editor_widget: 'EditorWidget'):
        super().__init__()
        self.editor_widget = editor_widget
        self.show_guides = True

    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)

        if self.show_guides:
            painter = QPainter(self.viewport())
            colors = self.editor_widget.theme_manager.current_theme_data.get('colors', {})
            guide_color = QColor(colors.get('editorIndentGuide.foreground', '#44475a'))
            pen = QPen(guide_color); pen.setStyle(Qt.PenStyle.DotLine); painter.setPen(pen)

            indent_size = self.fontMetrics().horizontalAdvance(' ' * self.editor_widget.settings.get("indent_width"))
            if indent_size <= 0: return

            block, offset = self.firstVisibleBlock(), self.contentOffset()
            while block.isValid():
                if not block.isVisible(): block = block.next(); continue
                block_rect = self.blockBoundingGeometry(block).translated(offset)
                text = block.text()
                if text:
                    line_indent = len(text) - len(text.lstrip())
                    effective_indent_levels, char_count = 0, 0
                    for char in text[:line_indent]:
                        if char == '\t':
                            effective_indent_levels += 1; char_count = 0
                        else:
                            char_count += 1
                            if char_count == self.editor_widget.settings.get("indent_width"):
                                effective_indent_levels += 1; char_count = 0
                    for i in range(1, effective_indent_levels + 1):
                        x = self.document().documentLayout().blockBoundingRect(block).left() + (i * indent_size)
                        painter.drawLine(QPointF(x, block_rect.top()), QPointF(x, block_rect.bottom()))
                if block_rect.top() > event.rect().bottom(): break
                block = block.next()


class HighlightManager(QObject):
    highlights_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._highlights: Dict[str, Dict[int, QColor]] = {}

    def add_highlight(self, source_id: str, line_number: int, color: QColor):
        if source_id not in self._highlights: self._highlights[source_id] = {}
        self._highlights[source_id][line_number] = color
        self.highlights_changed.emit()

    def toggle_highlight(self, source_id: str, line_number: int, color: QColor):
        if source_id in self._highlights and line_number in self._highlights[source_id]:
            del self._highlights[source_id][line_number]
        else:
            if source_id not in self._highlights: self._highlights[source_id] = {}
            self._highlights[source_id][line_number] = color
        self.highlights_changed.emit()

    def clear_highlights(self, source_id: str):
        if source_id in self._highlights:
            self._highlights.pop(source_id, None); self.highlights_changed.emit()

    def get_all_highlights(self) -> Dict[int, QColor]:
        return {k: v for source in self._highlights.values() for k, v in source.items()}


class LineNumberGutter(QWidget):
    HIGHLIGHTER_SOURCE_ID = "gutter_line_selection"

    def __init__(self, editor: 'EditorWidget'):
        super().__init__(editor)
        self.editor_widget = editor
        self.text_area = editor.text_area
        self.theme_manager = editor.theme_manager
        self.highlight_manager = editor.highlight_manager
        self.setMouseTracking(True); self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.hovered_line = -1

    def sizeHint(self) -> QSize:
        return QSize(self.fontMetrics().horizontalAdvance(str(self.text_area.blockCount())) + 15, 0)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self); colors = self.theme_manager.current_theme_data.get('colors', {})
        painter.fillRect(event.rect(), QColor(colors.get('editorGutter.background', '#2f383e')))
        block, top = self.text_area.firstVisibleBlock(), self.text_area.blockBoundingGeometry(self.text_area.firstVisibleBlock()).translated(self.text_area.contentOffset()).top()
        current_cursor_line = self.text_area.textCursor().blockNumber()
        all_highlights = self.highlight_manager.get_all_highlights()
        active_color, inactive_color, hover_bg = QColor(colors.get('gutter.activeLineNumberForeground', '#d3c6aa')), QColor(colors.get('editorLineNumber.foreground', '#5f6c6d')), QColor(colors.get('editorGutter.hoverBackground', '#83c0921a'))

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and (top + self.text_area.blockBoundingRect(block).height()) >= event.rect().top():
                line_num = block.blockNumber()
                if self.hovered_line == line_num: painter.fillRect(QRect(0, int(top), self.width(), self.fontMetrics().height()), hover_bg)
                final_color = active_color if line_num == current_cursor_line or (line_num + 1) in all_highlights else inactive_color
                painter.setPen(final_color); painter.setFont(self.text_area.font())
                painter.drawText(0, int(top), self.width() - 5, self.fontMetrics().height(), Qt.AlignmentFlag.AlignRight, str(line_num + 1))
            top += self.text_area.blockBoundingRect(block).height(); block = block.next()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self.hovered_line >= 0:
            self.highlight_manager.toggle_highlight(self.HIGHLIGHTER_SOURCE_ID, self.hovered_line + 1,
                                                    QColor(self.theme_manager.current_theme_data.get('colors', {}).get('editor.lineHighlightBackground', '#3a4145')))
            self.editor_widget.text_area.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        pos = event.position().y(); new_hover = -1
        block, top = self.text_area.firstVisibleBlock(), self.text_area.blockBoundingGeometry(self.text_area.firstVisibleBlock()).translated(self.text_area.contentOffset()).top()
        while block.isValid():
            bottom = top + self.text_area.blockBoundingRect(block).height()
            if top <= pos < bottom: new_hover = block.blockNumber(); break
            top = bottom; block = block.next()
        if self.hovered_line != new_hover: self.hovered_line = new_hover; self.update()

    def leaveEvent(self, event: QEvent):
        if self.hovered_line != -1: self.hovered_line = -1; self.update()


class MiniMapWidget(QWidget):
    def __init__(self, editor: QPlainTextEdit, theme_manager: "ThemeManager"):
        super().__init__()
        self.editor = editor; self.theme_manager = theme_manager
        self.setCursor(Qt.CursorShape.PointingHandCursor); self.setMinimumWidth(80); self.setMaximumWidth(200)
        self.editor.verticalScrollBar().valueChanged.connect(self.update)
        self.editor.document().blockCountChanged.connect(self.update)

    def paintEvent(self, event: QPaintEvent):
        p, c, doc, vs = QPainter(self), self.theme_manager.current_theme_data.get('colors', {}), self.editor.document(), self.editor.verticalScrollBar()
        p.fillRect(self.rect(), QColor(c.get('editorGutter.background', '#16161e')))
        if doc.blockCount() == 0: return
        lh, th = 2.0, doc.blockCount() * 2.0; s = min(1.0, self.height() / th if th > 0 else 1.0)
        so = -(th - self.height()) * (vs.value() / (vs.maximum() or 1)) if th > self.height() else 0
        p.setPen(QColor(c.get('editor.foreground', '#c0caf5')))
        for i in range(doc.blockCount()):
            if (y := so + (i * lh * s)) > self.height(): break
            if text := doc.findBlockByNumber(i).text().lstrip():
                p.drawRect(QRectF((len(doc.findBlockByNumber(i).text()) - len(text)) * 1.5, y, len(text) * 0.8, max(1.0, lh * s)))
        fv, vb = self.editor.firstVisibleBlock().blockNumber(), (self.editor.viewport().height() // self.editor.fontMetrics().height()) if self.editor.fontMetrics().height() > 0 else 0
        vy, vh = so + (fv * lh * s), max(1.0, vb * lh * s)
        p.fillRect(QRectF(0, vy, self.width() - 1, vh), QColor(c.get('editorGutter.ruler.color', '#41a6b530')))
        p.setPen(QPen(QColor(c.get('editorGutter.ruler.color', '#41a6b5')), 1)); p.drawRect(QRectF(0, vy, self.width() - 1, vh))

    def mousePressEvent(self, e: QMouseEvent): self._scroll_from_mouse(e.position())
    def mouseMoveEvent(self, e: QMouseEvent):
        if e.buttons() & Qt.MouseButton.LeftButton: self._scroll_from_mouse(e.position())

    def _scroll_from_mouse(self, pos: QPointF):
        self.editor.verticalScrollBar().setValue(int((pos.y() / self.height()) * self.editor.verticalScrollBar().maximum()) if self.height() > 0 else 0)


class EditorWidget(QWidget):
    content_possibly_changed = pyqtSignal()
    cursor_position_display_updated = pyqtSignal(int, int)
    status_message_requested = pyqtSignal(str, int)
    find_in_project_requested, replace_in_project_requested = pyqtSignal(str, object), pyqtSignal(str, str, object)
    gutter_width_changed = pyqtSignal()

    CODE_EXTENSIONS = {'.py', '.js', '.ts', '.cs', '.java', '.go', '.rs', '.c', '.cpp', '.h', '.hpp', '.css', '.html', '.json', '.xml'}

    def __init__(self, koromali_api: 'KoromaliPluginAPI'):
        super().__init__()
        self.koromali_api = koromali_api
        self.theme_manager: 'ThemeManager' = koromali_api.get_manager("theme")
        self.settings: "SettingsManager" = koromali_api.get_manager("settings")
        self.highlight_manager: HighlightManager = koromali_api.highlight_manager

        self.filepath: Optional[str] = None; self.highlighter: Optional[QSyntaxHighlighter] = None
        self.main_layout = QVBoxLayout(self); self.main_layout.setContentsMargins(0, 0, 0, 0); self.main_layout.setSpacing(0)
        self.find_panel = FindPanel(self.theme_manager, self.settings, self); self.main_layout.addWidget(self.find_panel); self.find_panel.hide()

        editor_area = QWidget(); editor_layout = QHBoxLayout(editor_area); editor_layout.setContentsMargins(0, 0, 0, 0); editor_layout.setSpacing(0)
        self.splitter = QSplitter(Qt.Orientation.Horizontal); self.splitter.setHandleWidth(1); editor_layout.addWidget(self.splitter)
        editor_container = QWidget(); inner_layout = QHBoxLayout(editor_container); inner_layout.setContentsMargins(0, 0, 0, 0); inner_layout.setSpacing(0)
        
        self.text_area = CustomTextArea(self); self.text_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gutter = LineNumberGutter(self)

        inner_layout.addWidget(self.gutter); inner_layout.addWidget(self.text_area)
        self.splitter.addWidget(editor_container)
        self.v_scrollbar = QScrollBar(Qt.Orientation.Vertical); self.v_scrollbar.setFixedWidth(14); editor_layout.addWidget(self.v_scrollbar)
        self.main_layout.addWidget(editor_area)

        self._last_side_panel_width = 150; self._side_panel: Optional[QWidget] = None
        self._connect_signals()

    def install_side_panel_widget(self, widget: QWidget):
        if self.splitter.count() > 1 and self._side_panel: self._side_panel.setParent(None); self._side_panel.deleteLater()
        self._side_panel = widget; self.splitter.addWidget(self._side_panel)
        self.splitter.setSizes([self.width() - self._last_side_panel_width, self._last_side_panel_width])

    def toggle_side_panel_visibility(self):
        if self.splitter.count() < 2: return
        sizes = self.splitter.sizes()
        if sizes[1] > 5:
            self._last_side_panel_width = sizes[1]; self.splitter.setSizes([sum(sizes), 0])
        else:
            self.splitter.setSizes([sum(sizes) - self._last_side_panel_width, self._last_side_panel_width])

    def _connect_signals(self):
        self.text_area.blockCountChanged.connect(self.gutter.update)
        self.text_area.blockCountChanged.connect(self.update_gutter_width)
        self.text_area.updateRequest.connect(self.gutter.update)
        self.text_area.cursorPositionChanged.connect(self.gutter.update)
        self.text_area.cursorPositionChanged.connect(self._on_cursor_position_changed)
        self.content_possibly_changed.connect(self.text_area.document().setModified)
        self.text_area.textChanged.connect(self.content_possibly_changed)
        internal_scrollbar = self.text_area.verticalScrollBar()
        self.v_scrollbar.valueChanged.connect(internal_scrollbar.setValue)
        internal_scrollbar.valueChanged.connect(self.v_scrollbar.setValue)
        internal_scrollbar.rangeChanged.connect(self.v_scrollbar.setRange)
        self.find_panel.close_requested.connect(self.hide_find_panel)
        self.find_panel.status_message_requested.connect(self.status_message_requested)
        self.find_panel.find_in_project_requested.connect(self.find_in_project_requested)
        self.find_panel.replace_in_project_requested.connect(self.replace_in_project_requested)
        if self.highlight_manager:
            self.highlight_manager.highlights_changed.connect(self.gutter.update)
            self.highlight_manager.highlights_changed.connect(self.update_line_highlights)

    def update_line_highlights(self):
        selections, highlights = [], self.highlight_manager.get_all_highlights()
        for line, color in highlights.items():
            sel = QTextEdit.ExtraSelection(); sel.format.setBackground(color); sel.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
            sel.cursor = QTextCursor(self.document().findBlockByNumber(line - 1)); selections.append(sel)
        self.text_area.setExtraSelections(selections)

    def update_gutter_width(self, newBlockCount=None):
        self.gutter.setFixedWidth(self.gutter.sizeHint().width()); self.gutter_width_changed.emit()

    def _on_cursor_position_changed(self): self.cursor_position_display_updated.emit(*self.get_cursor_position())

    def apply_styles_and_settings(self):
        font = QFont(self.settings.get("font_family"), self.settings.get("font_size"))
        self.text_area.setFont(font); fm = self.text_area.fontMetrics()
        self.text_area.setTabStopDistance(self.settings.get("indent_width", 4) * fm.horizontalAdvance(' '))
        self.text_area.setWordWrapMode(QTextOption.WrapMode.WordWrap if self.settings.get("word_wrap") else QTextOption.WrapMode.NoWrap)
        self.text_area.show_guides = self.settings.get("show_indentation_guides")
        self.update_theme(); self.update_gutter_width(); self.update_line_highlights()

    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get("colors", {}); self.text_area.setStyleSheet(f"QPlainTextEdit {{ background-color: {colors.get('editor.background', '#272e33')}; color: {colors.get('editor.foreground', '#d3c6aa')}; border: none; selection-background-color: {colors.get('editor.selectionBackground', '#264f78')}; }}")
        scrollbar_bg, handle_bg = colors.get('editor.background', '#272e33'), colors.get('scrollbarSlider.background', '#4a4a4a80')
        self.v_scrollbar.setStyleSheet(f"QScrollBar:vertical {{ border: none; background: {scrollbar_bg}; width: 14px; margin: 0; }} QScrollBar::handle:vertical {{ background: {handle_bg}; min-height: 20px; border-radius: 7px; }} QScrollBar::handle:vertical:hover {{ background: {colors.get('scrollbarSlider.hoverBackground', '#5a5a5a90')}; }} QScrollBar::handle:vertical:pressed {{ background: {colors.get('scrollbarSlider.activeBackground', '#6a6a6aa0')}; }} QScrollBar::add-line, QScrollBar::sub-line {{ border: none; background: none; height: 0px; }} QScrollBar::add-page, QScrollBar::sub-page {{ background: none; }}")
        if self.highlighter: self.highlighter.rehighlight()
        self.gutter.update(); self.text_area.viewport().update()
        if self.splitter: self.splitter.setStyleSheet(f"QSplitter::handle {{ background-color: {colors.get('sidebar.background', '#2a3338')}; }} QSplitter::handle:hover {{ background-color: {colors.get('accent')}; }}")

    def set_filepath(self, fp: Optional[str]): self.filepath = fp
    def set_text(self, text: str): self.text_area.setPlainText(text)
    def get_text(self) -> str: return self.text_area.toPlainText()
    def document(self): return self.text_area.document()
    def get_cursor_position(self) -> tuple[int, int]: c = self.text_area.textCursor(); return c.blockNumber() + 1, c.columnNumber()
    def goto_line_and_column(self, line: int, col: int): c = QTextCursor(self.document().findBlockByNumber(line - 1)); c.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.MoveAnchor, col); self.text_area.setTextCursor(c); self.text_area.setFocus()
    def set_highlighter(self, h_class):
        if self.highlighter: self.highlighter.setDocument(None)
        if h_class: self.highlighter = h_class(self.document(), self.theme_manager)

    def toggle_find_panel(self):
        if self.find_panel.isVisible(): self.hide_find_panel()
        else: self.show_find_panel()

    def show_find_panel(self):
        self.find_panel.show(); self.find_panel.connect_editor(self); self.find_panel.focus_find_input()

    def hide_find_panel(self): self.find_panel.hide(); self.text_area.setFocus()
    def find_next(self, q, f): return self.text_area.find(q, f)

    def replace_current(self, query, replace, flags):
        c = self.text_area.textCursor()
        if c.hasSelection() and c.selectedText().lower() == query.lower():
            c.insertText(replace); return True
        if self.text_area.find(query, flags): self.text_area.textCursor().insertText(replace); return True
        return False

    def replace_all(self, query, replace, flags):
        count = 0; c = self.text_area.textCursor(); c.beginEditBlock()
        c.movePosition(QTextCursor.MoveOperation.Start); self.text_area.setTextCursor(c)
        while self.text_area.find(query, flags): self.text_area.textCursor().insertText(replace); count += 1
        c.endEditBlock(); return count

    def get_indent_string(self) -> str:
        return "\t" if self.settings.get("use_tabs_for_indent") else " " * self.settings.get("indent_width", 4)

    def increase_indent(self): self._modify_indent(self.get_indent_string())
    def decrease_indent(self): self._modify_indent(self.get_indent_string(), remove=True)
    def _modify_indent(self, indent_str, remove=False):
        c = self.text_area.textCursor()
        if not c.hasSelection(): c.insertText(indent_str) if not remove else self._unindent_line(c, indent_str); return
        c.beginEditBlock(); start_block = self.document().findBlock(c.selectionStart()); end_block = self.document().findBlock(c.selectionEnd())
        if c.selectionEnd() == end_block.position() and start_block != end_block: end_block = end_block.previous()
        block = start_block
        while True:
            cur = QTextCursor(block)
            if remove: self._unindent_line(cur, indent_str)
            else: cur.setPosition(block.position()); cur.insertText(indent_str)
            if block.blockNumber() == end_block.blockNumber(): break
            block = block.next()
        c.endEditBlock()

    def _unindent_line(self, cursor: QTextCursor, indent_str: str):
        text = cursor.block().text()
        if text.startswith(indent_str): cursor.setPosition(cursor.block().position()); [cursor.deleteChar() for _ in range(len(indent_str))]
        elif text.startswith(" "):
            spaces = len(text) - len(text.lstrip(' ')); cursor.setPosition(cursor.block().position()); [cursor.deleteChar() for _ in range(min(spaces, len(indent_str)))]

    def toggle_comment(self):
        if not self.filepath: return self.status_message_requested.emit("File type unknown.", 3000)
        comment_char = self.koromali_api.main_window.COMMENT_MAP.get(os.path.splitext(self.filepath)[1].lower())
        if not comment_char: return self.status_message_requested.emit(f"No comment style for '{os.path.splitext(self.filepath)[1]}'.", 3000)
        c = self.text_area.textCursor(); c.beginEditBlock()
        start, end = c.selectionStart(), c.selectionEnd(); start_block = self.document().findBlock(start)
        end_block = self.document().findBlock(end);
        if end == end_block.position() and c.columnNumber() == 0 and start_block != end_block: end_block = end_block.previous()
        is_commenting = not start_block.text().lstrip().startswith(comment_char)
        block = start_block
        while True:
            text = block.text(); cur = QTextCursor(block)
            if is_commenting:
                cur.setPosition(block.position() + (len(text) - len(text.lstrip()))); cur.insertText(comment_char + ' ')
            else:
                stripped = text.lstrip()
                if stripped.startswith(comment_char):
                    pos = text.find(comment_char); cur.setPosition(block.position() + pos); cur.deleteChar()
                    next_char = QTextCursor(cur); next_char.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, 1)
                    if next_char.selectedText() == ' ': cur.deleteChar()
            if block.blockNumber() == end_block.blockNumber(): break
            block = block.next()
        c.endEditBlock()