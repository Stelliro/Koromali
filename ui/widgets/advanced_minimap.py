# /ui/widgets/advanced_minimap.py
import re
from typing import List, Dict, Tuple, Optional
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QPainter, QColor, QFont, QMouseEvent, QPen, QFontMetrics, QResizeEvent
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF, QEvent, QSize
import qtawesome as qta

from app_core.theme_manager import ThemeManager
from utils.logger import log

class CodeParser:
    """Base class for language-specific code parsers."""
    def parse(self, text: str) -> List[Dict]:
        """Parses text and returns a list of symbol dictionaries."""
        return []

class PythonParser(CodeParser):
    """Parses Python code to find classes and functions."""
    SYMBOL_REGEX = re.compile(r"^\s*(?:class|def)\s+([A-Za-z_][A-Za-z0-9_]*)")

    def parse(self, text: str) -> List[Dict]:
        symbols = []
        for line_num, line in enumerate(text.splitlines(), 1):
            match = self.SYMBOL_REGEX.match(line)
            if match:
                symbol_type = 'class' if 'class' in line else 'function'
                symbol_name = match.group(1)
                symbols.append({
                    "name": symbol_name,
                    "type": symbol_type,
                    "line": line_num
                })
        return symbols

class JavaScriptParser(CodeParser):
    """Parses JavaScript/TypeScript code to find classes, functions, and methods."""
    SYMBOL_REGEX = re.compile(
        r"^\s*(?:(?:export\s+)?(?:async\s+)?(?:class|function\**)\s+([A-Za-z_][A-Za-z0-9_]*)|(?:const|let|var)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:async)?\s*(?:\([^)]*\)|[A-Za-z_][A-Za-z0-9_]*)\s*=>|function)"
    )

    def parse(self, text: str) -> List[Dict]:
        symbols = []
        for line_num, line in enumerate(text.splitlines(), 1):
            match = self.SYMBOL_REGEX.match(line)
            if match:
                symbol_name = match.group(1) or match.group(2)
                if symbol_name:
                    symbol_type = 'class' if 'class' in line else 'function'
                    symbols.append({
                        "name": symbol_name,
                        "type": symbol_type,
                        "line": line_num
                    })
        return symbols

class CppParser(CodeParser):
    """Parses C/C++ code to find namespaces, classes, structs, and functions."""
    SYMBOL_REGEX = re.compile(
        r"^\s*(?:(namespace|class|struct|enum(?:\s+class)?)\s+([A-Za-z_][A-Za-z0-9_]*)|"
        r"((?:[\w:]+<[^>]+>\s*)?[\w:]+\s+&\s*|[\w:<>*\s&]+)\s+([A-Za-z_][A-Za-z0-9_:]+)\s*\([^)]*\)\s*(?:const)?\s*(?:{|;))"
    )

    def parse(self, text: str) -> List[Dict]:
        symbols = []
        excluded_keywords = {'if', 'for', 'while', 'switch', 'return', 'catch'}
        for line_num, line in enumerate(text.splitlines(), 1):
            if 'main(' in line:
                 symbols.append({"name": "main", "type": "function", "line": line_num})
                 continue
            match = self.SYMBOL_REGEX.match(line.strip())
            if match:
                type_keyword, type_name, _, func_name = match.groups()
                if type_keyword:
                    symbols.append({
                        "name": type_name,
                        "type": 'class' if type_keyword in ['class', 'struct'] else 'namespace',
                        "line": line_num
                    })
                elif func_name and func_name not in excluded_keywords and 'operator' not in func_name:
                    symbols.append({
                        "name": func_name,
                        "type": "function",
                        "line": line_num
                    })
        return symbols

class CSharpParser(CodeParser):
    """Parses C# code to find namespaces, classes, structs, enums, interfaces, and methods."""
    SYMBOL_REGEX = re.compile(
        r"^\s*(?:public|private|protected|internal|static|virtual|abstract|override|sealed|async|unsafe|partial)*\s*"
        r"(?:(namespace|class|struct|enum|interface)\s+([A-Za-z_][A-Za-z0-9_]*)|"
        r"([\w<>,?\[\]]+\s+)([A-Za-z_][A-Za-z0-9_]+)\s*\(.*\))"
    )
    def parse(self, text: str) -> List[Dict]:
        symbols = []
        excluded_keywords = {'if', 'for', 'while', 'switch', 'return', 'catch', 'foreach'}
        for line_num, line in enumerate(text.splitlines(), 1):
            match = self.SYMBOL_REGEX.match(line.strip())
            if match:
                type_keyword, type_name, _, method_name = match.groups()
                if type_keyword and type_name:
                    symbols.append({
                        "name": type_name,
                        "type": 'class' if type_keyword != 'namespace' else 'namespace',
                        "line": line_num
                    })
                elif method_name and method_name not in excluded_keywords and not line.strip().endswith(';'):
                    symbols.append({
                        "name": method_name,
                        "type": "function",
                        "line": line_num
                    })
        return symbols

class RustParser(CodeParser):
    """Parses Rust code to find functions, structs, enums, impls, and traits."""
    SYMBOL_REGEX = re.compile(r"^\s*(?:pub(?:\([^)]+\))?\s+)?(?:unsafe\s+)?(?:async\s+)?(?:const\s+)?(fn|struct|enum|impl|trait)\s+([A-Za-z_][A-Za-z0-9_]*)")

    def parse(self, text: str) -> List[Dict]:
        symbols = []
        for line_num, line in enumerate(text.splitlines(), 1):
            match = self.SYMBOL_REGEX.match(line)
            if match:
                symbol_type, symbol_name = match.groups()
                symbols.append({
                    "name": symbol_name,
                    "type": 'function' if symbol_type == 'fn' else 'class',
                    "line": line_num
                })
        return symbols

class HtmlParser(CodeParser):
    """Parses HTML code to find tags with 'id' attributes."""
    SYMBOL_REGEX = re.compile(r"""<([a-zA-Z0-9]+)
                                  [^>]*?
                                  id\s*=\s*
                                  (?:"([^"]*)"|'([^']*)')
                                  """, re.VERBOSE | re.IGNORECASE)
    def parse(self, text: str) -> List[Dict]:
        symbols = []
        for line_num, line in enumerate(text.splitlines(), 1):
            for match in self.SYMBOL_REGEX.finditer(line):
                symbol_name = match.group(2) or match.group(3)
                if symbol_name:
                    symbols.append({
                        "name": f"#{symbol_name}",
                        "type": "class",
                        "line": line_num
                    })
        return symbols


class MinimapDisplay(QWidget):
    """The widget responsible for painting and interacting with the symbol list."""

    def __init__(self, editor, theme_manager: ThemeManager, parent_minimap):
        super().__init__(parent_minimap)
        self.editor = editor
        self.theme_manager = theme_manager
        self.parent_minimap = parent_minimap
        self.hovered_symbol_line = -1
        self.active_symbol_line = -1
        self.scroll_y = 0

        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        colors = self.theme_manager.current_theme_data.get('colors', {})
        bg_color = QColor(colors.get('editorGutter.background', '#1f2335'))
        painter.fillRect(self.rect(), bg_color)

        symbols = self.parent_minimap.filtered_symbols
        font = QFont("Segoe UI", 8)
        painter.setFont(font)
        fm = QFontMetrics(font)
        symbol_line_height = fm.height() + 4

        # Draw Viewport Highlight
        doc = self.editor.document()
        total_editor_lines = doc.blockCount()
        if total_editor_lines > 0 and symbols:
            total_content_height = len(symbols) * symbol_line_height
            
            first_visible_line = self.editor.firstVisibleBlock().blockNumber()
            visible_lines_editor = self.editor.viewport().height() // self.editor.fontMetrics().height() if self.editor.fontMetrics().height() > 0 else 0
            
            viewport_y_in_content = (first_visible_line / total_editor_lines) * total_content_height
            viewport_h_in_content = (visible_lines_editor / total_editor_lines) * total_content_height
            
            final_viewport_y = viewport_y_in_content + self.scroll_y

            viewport_color = QColor(colors.get('editorGutter.ruler.color', '#41a6b5'))
            viewport_color.setAlpha(30)
            painter.fillRect(QRectF(0, final_viewport_y, self.width(), viewport_h_in_content), viewport_color)


        if not symbols:
            return

        painter.setClipRect(self.rect())

        icon_color_class = QColor(colors.get('syntax.className', '#dbbc7f'))
        icon_color_func = QColor(colors.get('syntax.functionName', '#83c092'))
        text_color = QColor(colors.get('editor.foreground', '#d3c6aa'))
        hover_bg_color = QColor(colors.get('list.hoverBackground', '#ffffff1a'))
        
        active_color = QColor(colors.get('list.activeSelectionBackground', '#83c092'))
        active_color.setAlpha(60)
        active_border_color = QColor(colors.get('list.activeSelectionBackground', '#83c092'))

        icon_class = qta.icon('mdi.puzzle-outline', color=icon_color_class)
        icon_func = qta.icon('mdi.function-variant', color=icon_color_func)
        
        for i, symbol in enumerate(symbols):
            y_pos = i * symbol_line_height + self.scroll_y
            
            if y_pos > self.height() or (y_pos + symbol_line_height) < 0:
                continue

            # Draw active symbol highlight
            if self.active_symbol_line == symbol['line']:
                painter.fillRect(QRectF(0, y_pos, self.width(), symbol_line_height), active_color)
                painter.fillRect(QRectF(0, y_pos, 3, symbol_line_height), active_border_color)

            # Draw hover highlight (if not the active symbol)
            if self.hovered_symbol_line == symbol['line'] and self.active_symbol_line != symbol['line']:
                painter.fillRect(QRectF(0, y_pos, self.width(), symbol_line_height), hover_bg_color)

            icon = icon_class if symbol['type'] == 'class' else icon_func
            pixmap = icon.pixmap(12, 12)
            painter.drawPixmap(8, int(y_pos + (symbol_line_height - pixmap.height()) / 2), pixmap)

            display_name = symbol['name'].replace('_', ' ').title()
            
            search_query = self.parent_minimap.search_input.text()
            if search_query:
                self._draw_highlighted_text(painter, 28, y_pos, symbol_line_height, display_name, search_query, text_color, active_border_color)
            else:
                painter.setPen(text_color)
                painter.drawText(28, int(y_pos + (symbol_line_height + fm.ascent() - fm.descent()) / 2), display_name)
                
    def _draw_highlighted_text(self, painter, x, y, line_height, text, query, base_color, highlight_color):
        fm = painter.fontMetrics()
        start_index = text.lower().find(query.lower())
        if start_index == -1:
            painter.setPen(base_color)
            painter.drawText(x, int(y + (line_height + fm.ascent() - fm.descent()) / 2), text)
            return

        end_index = start_index + len(query)
        
        pre_text = text[:start_index]
        pre_width = fm.horizontalAdvance(pre_text)
        painter.setPen(base_color)
        painter.drawText(x, int(y + (line_height + fm.ascent() - fm.descent()) / 2), pre_text)

        match_text = text[start_index:end_index]
        match_width = fm.horizontalAdvance(match_text)
        painter.setPen(highlight_color)
        painter.drawText(x + pre_width, int(y + (line_height + fm.ascent() - fm.descent()) / 2), match_text)
        
        post_text = text[end_index:]
        painter.setPen(base_color)
        painter.drawText(x + pre_width + match_width, int(y + (line_height + fm.ascent() - fm.descent()) / 2), post_text)
        
    def wheelEvent(self, event):
        fm = QFontMetrics(QFont("Segoe UI", 8))
        symbol_line_height = fm.height() + 4
        total_content_height = len(self.parent_minimap.filtered_symbols) * symbol_line_height
        
        if total_content_height > self.height():
            delta = -event.angleDelta().y() / 4
            new_scroll_y = self.scroll_y + delta
            
            max_scroll = 0
            min_scroll = -(total_content_height - self.height())
            self.scroll_y = max(min_scroll, min(max_scroll, new_scroll_y))
            
            self.update()

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.MouseButton.LeftButton:
            if self.hovered_symbol_line != -1:
                self._jump_to_line(self.hovered_symbol_line)

    def mouseMoveEvent(self, e: QMouseEvent):
        fm = QFontMetrics(QFont("Segoe UI", 8))
        symbol_line_height = fm.height() + 4
        content_y = e.position().y() - self.scroll_y
        new_hovered_line = -1
        
        symbols = self.parent_minimap.filtered_symbols
        if symbols:
            index = int(content_y // symbol_line_height)
            if 0 <= index < len(symbols):
                new_hovered_line = symbols[index]['line']

        if self.hovered_symbol_line != new_hovered_line:
            self.hovered_symbol_line = new_hovered_line
            self.update()

    def leaveEvent(self, event: QEvent):
        if self.hovered_symbol_line != -1:
            self.hovered_symbol_line = -1
            self.update()

    def _jump_to_line(self, line_number: int):
        cursor = self.editor.textCursor()
        block = self.editor.document().findBlockByNumber(line_number - 1)
        if block.isValid():
            cursor.setPosition(block.position())
            self.editor.setTextCursor(cursor)
            self.editor.centerCursor()
        self.editor.setFocus()


class AdvancedMinimap(QWidget):
    """Container widget for the advanced minimap and its search bar."""
    PARSERS = {
        '.py': PythonParser,
        '.js': JavaScriptParser, '.ts': JavaScriptParser,
        '.c': CppParser, '.cpp': CppParser, '.h': CppParser, '.hpp': CppParser,
        '.cs': CSharpParser,
        '.rs': RustParser,
        '.html': HtmlParser, '.htm': HtmlParser,
    }

    def __init__(self, editor, theme_manager: ThemeManager, file_extension: str):
        super().__init__()
        self.editor = editor
        self.theme_manager = theme_manager
        
        self.symbols: List[Dict] = []
        self.filtered_symbols: List[Dict] = []
        self.parser: Optional[CodeParser] = self.PARSERS.get(file_extension, CodeParser)()
        
        self.update_highlight_timer = QTimer()
        self.update_highlight_timer.setSingleShot(True)
        self.update_highlight_timer.setInterval(100)
        self.update_highlight_timer.timeout.connect(self._update_active_symbol)

        self._setup_ui()
        self._connect_signals()
        
        self.update_symbols()
        self.update_highlight_timer.start()

    def _setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.main_layout.setSpacing(2)

        search_container = QWidget()
        search_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0,0,0,0)
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Filter symbols...")
        self.search_input.setFixedHeight(26)
        search_layout.addWidget(self.search_input)

        self.clear_button = qta.IconWidget('mdi.close', color='gray')
        self.clear_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clear_button.mouseReleaseEvent = lambda e: self.search_input.clear()
        self.clear_button.hide()
        search_layout.addWidget(self.clear_button)
        
        search_container.setLayout(search_layout)
        self.main_layout.addWidget(search_container)
        
        self.display_widget = MinimapDisplay(self.editor.text_area, self.theme_manager, self)
        self.main_layout.addWidget(self.display_widget)
        self.update_theme()

    def _connect_signals(self):
        self.editor.text_area.document().contentsChanged.connect(self.update_symbols)
        self.editor.text_area.cursorPositionChanged.connect(self.update_highlight_timer.start)
        self.editor.text_area.verticalScrollBar().valueChanged.connect(self.display_widget.update)
        self.search_input.textChanged.connect(self._update_filter)

    def _update_filter(self, text: str):
        self.clear_button.setVisible(bool(text))
        if not text:
            self.filtered_symbols = self.symbols
        else:
            self.filtered_symbols = [
                s for s in self.symbols if text.lower() in s['name'].lower()
            ]
        self.display_widget.scroll_y = 0
        self.display_widget.update()
        
    def update_symbols(self):
        if self.parser:
            text = self.editor.get_text()
            self.symbols = self.parser.parse(text)
            self._update_filter(self.search_input.text())
            self._update_active_symbol()

    def _update_active_symbol(self):
        """Finds which symbol is active based on editor cursor and scrolls it into view."""
        cursor_line = self.editor.get_cursor_position()[0]
        
        active_symbol = None
        active_symbol_index = -1

        for i, symbol in enumerate(self.symbols):
            if symbol['line'] <= cursor_line:
                active_symbol = symbol
                active_symbol_index = i
            else:
                break
        
        new_active_line = active_symbol['line'] if active_symbol else -1
        
        if self.display_widget.active_symbol_line != new_active_line:
            self.display_widget.active_symbol_line = new_active_line
            
            # --- Auto-scroll logic ---
            if active_symbol_index != -1:
                fm = QFontMetrics(QFont("Segoe UI", 8))
                symbol_line_height = fm.height() + 4
                
                try:
                    filtered_index = self.filtered_symbols.index(active_symbol)
                except ValueError:
                    filtered_index = -1

                if filtered_index != -1:
                    symbol_y_pos = filtered_index * symbol_line_height
                    viewport_top = -self.display_widget.scroll_y
                    viewport_bottom = viewport_top + self.display_widget.height()

                    if symbol_y_pos < viewport_top:
                        self.display_widget.scroll_y = -symbol_y_pos
                    elif (symbol_y_pos + symbol_line_height) > viewport_bottom:
                        self.display_widget.scroll_y = -(symbol_y_pos + symbol_line_height - self.display_widget.height())
            
            self.display_widget.update()

    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        style = f"""
            QLineEdit {{
                background-color: {colors.get('input.background', '#3a4145')};
                border: 1px solid {colors.get('input.border', '#5f6c6d')};
                border-radius: 4px; padding: 4px 6px;
                color: {colors.get('input.foreground', '#d3c6aa')};
            }}
        """
        self.search_input.setStyleSheet(style)
        self.display_widget.update()