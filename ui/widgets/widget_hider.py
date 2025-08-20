# /ui/widgets/widget_hider.py

from collections import defaultdict
from typing import TYPE_CHECKING, Dict, Tuple
from PyQt6.QtWidgets import QToolButton, QWidget, QDockWidget, QToolBar, QApplication
from PyQt6.QtCore import Qt, pyqtSignal, QPoint, QMimeData, QByteArray, QSize, QPropertyAnimation, QEasingCurve, QPointF, pyqtProperty, QRectF
from PyQt6.QtGui import QMouseEvent, QDrag, QPixmap, QPainter, QPolygonF, QColor, QPen

if TYPE_CHECKING:
    from ui.main_window import MainWindow

# Define a custom MIME type to identify drags originating from our hider buttons.
# This allows the MainWindow to distinguish them from other drag events like file drops.
HIDER_WIDGET_MIME_TYPE = "application/x-koromali-hider-widget"

class HiderButton(QToolButton):
    """A button on the edge of the window representing a hidden widget, now with custom arrow drawing and animation."""
    drag_started = pyqtSignal(QWidget)

    def __init__(self, widget_to_control: QWidget, edge: str, theme_manager, parent: QWidget = None):
        super().__init__(parent)
        self.widget = widget_to_control
        self.edge = edge
        self.theme_manager = theme_manager
        self.drag_start_position = QPoint()
        self.animation: QPropertyAnimation = None

        self.setCheckable(True)
        self.setAutoRaise(True)
        self.setToolTip(f"Show '{self.widget.windowTitle()}'")
        
    def paintEvent(self, event):
        """Custom painting to draw an arrow indicating the widget's location."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        colors = self.theme_manager.current_theme_data.get('colors', {})
        arrow_color = QColor(colors.get('editor.foreground', '#cccccc'))
        bg_color = QColor(colors.get('sidebar.background', '#333333'))
        
        # Make the background slightly transparent to blend with the edge
        bg_color.setAlpha(220)
        painter.fillRect(self.rect(), bg_color)
        
        pen = QPen(arrow_color, 2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        
        rect = self.rect()
        w, h = rect.width(), rect.height()
        
        arrow_size = 5 # Size of the arrow head lines
        
        if self.edge == 'left': # Arrow should point right >
            p1 = QPointF(w * 0.4, h / 2 - arrow_size)
            p2 = QPointF(w * 0.6, h / 2)
            p3 = QPointF(w * 0.4, h / 2 + arrow_size)
            painter.drawPolyline(QPolygonF([p1, p2, p3]))
        elif self.edge == 'right': # Arrow should point left <
            p1 = QPointF(w * 0.6, h / 2 - arrow_size)
            p2 = QPointF(w * 0.4, h / 2)
            p3 = QPointF(w * 0.6, h / 2 + arrow_size)
            painter.drawPolyline(QPolygonF([p1, p2, p3]))
        elif self.edge == 'top': # Arrow should point down v
            p1 = QPointF(w / 2 - arrow_size, h * 0.4)
            p2 = QPointF(w / 2, h * 0.6)
            p3 = QPointF(w / 2 + arrow_size, h * 0.4)
            painter.drawPolyline(QPolygonF([p1, p2, p3]))
        elif self.edge == 'bottom': # Arrow should point up ^
            p1 = QPointF(w / 2 - arrow_size, h * 0.6)
            p2 = QPointF(w / 2, h * 0.4)
            p3 = QPointF(w / 2 + arrow_size, h * 0.6)
            painter.drawPolyline(QPolygonF([p1, p2, p3]))


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
            
        self.drag_started.emit(self.widget)
        self.setDown(False)


class WidgetHiderManager:
    """
    Manages the creation, positioning, and state of hider buttons for
    registered toolbars and dock widgets, ensuring they never overlap.
    """
    def __init__(self, main_window: 'MainWindow'):
        self.main_window = main_window
        # Structure: {widget: {'button': HiderButton, 'last_area': Qt.DockWidgetArea | Qt.ToolBarArea, 'animation': QPropertyAnimation}}
        self.managed_widgets: Dict[QWidget, Dict] = {}

    def register_widget(self, widget: QWidget, default_area):
        """Registers a QDockWidget or QToolBar to be managed."""
        if widget in self.managed_widgets:
            return
        
        button = HiderButton(widget, 'none', self.main_window.theme_manager, self.main_window)
        button.hide()
        
        animation = QPropertyAnimation(button, b"pos")
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        button.animation = animation # Give the button a reference to its animation
        
        self.managed_widgets[widget] = {
            'button': button, 
            'last_area': default_area,
            'animation': animation
        }

        button.clicked.connect(self._on_button_clicked)
        button.drag_started.connect(self._on_widget_drag_started)
        widget.visibilityChanged.connect(self.update_hider_positions)

        if isinstance(widget, QDockWidget):
            widget.dockLocationChanged.connect(
                lambda area: self._update_widget_area(widget, area)
            )

    def _on_button_clicked(self):
        """Shows the corresponding widget when its hider button is clicked."""
        button = self.main_window.sender()
        if not isinstance(button, HiderButton): return

        widget = button.widget
        if widget in self.managed_widgets:
            last_area = self.managed_widgets[widget]['last_area']
            if isinstance(widget, QDockWidget):
                self.main_window.addDockWidget(last_area, widget)
                widget.setFloating(False)
            elif isinstance(widget, QToolBar):
                self.main_window.addToolBar(last_area, widget)
            widget.show()
            widget.raise_()

    def _on_widget_drag_started(self, widget_to_drag: QWidget):
        """Initiates a QDrag operation when a hider button is dragged."""
        drag = QDrag(widget_to_drag)
        mime_data = QMimeData()
        
        widget_id = str(id(widget_to_drag))
        mime_data.setData(HIDER_WIDGET_MIME_TYPE, QByteArray(widget_id.encode()))
        
        drag.setMimeData(mime_data)

        pixmap = widget_to_drag.grab()
        drag.setPixmap(pixmap.scaledToWidth(150, Qt.TransformationMode.SmoothTransformation))
        drag.setHotSpot(QPoint(10, 10))

        widget_to_drag.hide()
        drag.exec(Qt.DropAction.MoveAction)

    def _update_widget_area(self, widget: QWidget, new_area):
        """Stores the last known docking/toolbar area of a widget."""
        if widget in self.managed_widgets:
            if new_area != Qt.DockWidgetArea.NoDockWidgetArea and new_area != Qt.ToolBarArea.NoToolBarArea:
                self.managed_widgets[widget]['last_area'] = new_area
        self.update_hider_positions()
        
    def animate_edge(self, edge: str, show: bool):
        """Animates all hider buttons for a specific edge in or out."""
        for data in self.managed_widgets.values():
            if data['button'].edge == edge:
                animation = data['animation']
                animation.setDirection(QPropertyAnimation.Direction.Forward if show else QPropertyAnimation.Direction.Backward)
                if animation.state() != QPropertyAnimation.State.Running:
                    animation.start()

    def update_hider_positions(self):
        """The core layout logic that arranges hider buttons along window edges."""
        # This function now calculates start/end positions for animations
        # It doesn't show/hide them directly anymore.
        
        hidden_widgets_by_area = defaultdict(list)
        for widget, data in self.managed_widgets.items():
            if not widget.isVisible():
                area = data['last_area']
                hidden_widgets_by_area[area].append(data)

        margin = 2
        main_geo = self.main_window.geometry()
        
        self._calculate_button_positions('left', hidden_widgets_by_area[Qt.DockWidgetArea.LeftDockWidgetArea], margin, main_geo)
        self._calculate_button_positions('right', hidden_widgets_by_area[Qt.DockWidgetArea.RightDockWidgetArea], margin, main_geo)
        self._calculate_button_positions('top', hidden_widgets_by_area[Qt.ToolBarArea.TopToolBarArea] + hidden_widgets_by_area[Qt.DockWidgetArea.TopDockWidgetArea], margin, main_geo)
        self._calculate_button_positions('bottom', hidden_widgets_by_area[Qt.ToolBarArea.BottomToolBarArea] + hidden_widgets_by_area[Qt.DockWidgetArea.BottomDockWidgetArea], margin, main_geo)
        
        # Hide any buttons that are no longer part of a group (e.g., widget became visible)
        all_hidden_buttons = {b['button'] for bl in hidden_widgets_by_area.values() for b in bl}
        for data in self.managed_widgets.values():
            if data['button'] not in all_hidden_buttons:
                data['button'].hide()

    def _calculate_button_positions(self, edge, button_data_list, margin, window_geo):
        if not button_data_list: return

        is_vertical = edge in ['left', 'right']
        button_width = 30 if is_vertical else 100
        button_height = 100 if is_vertical else 30
        
        status_bar_height = self.main_window.statusBar().height() if self.main_window.statusBar() and self.main_window.statusBar().isVisible() else 0
        menu_bar_height = self.main_window.menuBar().height() if self.main_window.menuBar() and self.main_window.menuBar().isVisible() else 0

        total_size = sum((button_height if is_vertical else button_width) + margin for _ in button_data_list)
        offset = ( (window_geo.height() if is_vertical else window_geo.width()) - total_size) / 2

        for data in button_data_list:
            button, animation = data['button'], data['animation']
            button.edge = edge
            button.setFixedSize(button_width, button_height)
            
            if is_vertical:
                end_x = margin
                start_x = -button_width
                if edge == 'right':
                    end_x = window_geo.width() - button_width - margin
                    start_x = window_geo.width()
                
                end_y = start_y = offset
                
                animation.setStartValue(QPoint(int(start_x), int(start_y)))
                animation.setEndValue(QPoint(int(end_x), int(end_y)))
                offset += button_height + margin
            else: # Horizontal
                end_y = margin + menu_bar_height
                start_y = -button_height
                if edge == 'bottom':
                    end_y = window_geo.height() - button_height - margin - status_bar_height
                    start_y = window_geo.height()
                
                end_x = start_x = offset
                
                animation.setStartValue(QPoint(int(start_x), int(start_y)))
                animation.setEndValue(QPoint(int(end_x), int(end_y)))
                offset += button_width + margin
            
            # Place button at its start position initially
            if animation.state() != QPropertyAnimation.State.Running:
                button.move(animation.startValue())
            
            button.show()