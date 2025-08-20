# /plugins/live_share_studio/remote_cursor_widget.py
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRect

class RemoteCursorWidget(QWidget):
    """An overlay for drawing remote collaborators' cursors and selections."""
    def __init__(self, editor_widget, parent=None):
        super().__init__(parent)
        self.editor_widget = editor_widget
        self.remote_cursors = {} # { "user_id": {"pos": int, "selection_end": int, "color": str} }

        self.setParent(self.editor_widget.text_area.viewport())
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.resize(self.parent().size())

    def update_cursors(self, cursors_data: dict):
        self.remote_cursors = cursors_data
        self.update() # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        text_area = self.editor_widget.text_area
        
        for user_id, data in self.remote_cursors.items():
            color = QColor(data.get("color", "#FF5555"))
            cursor_pos = data.get("pos")
            selection_end = data.get("selection_end")

            # Draw selection highlight
            if cursor_pos is not None and selection_end is not None and cursor_pos != selection_end:
                selection_color = QColor(color)
                selection_color.setAlpha(80) # Semi-transparent
                
                # TODO: Convert start/end text positions to a series of QRects
                # for multi-line selections and fill them.
                # painter.fillRect(rect, selection_color)
                pass

            # Draw cursor
            if cursor_pos is not None:
                cursor = text_area.textCursor()
                cursor.setPosition(cursor_pos)
                cursor_rect = text_area.cursorRect(cursor)
                
                painter.setPen(QPen(color, 2))
                painter.drawLine(cursor_rect.topLeft(), cursor_rect.bottomLeft())