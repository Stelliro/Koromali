# Koromali/ui/explorer/list_view_widget.py
import os
import sys
from typing import List, Optional, TYPE_CHECKING

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QInputDialog, QMessageBox,
    QProxyStyle, QStyle, QApplication, QAbstractItemView, QToolButton,
    QHBoxLayout, QTreeWidgetItemIterator, QHeaderView, QFrame, QLabel, QMenu, QDialog,
    QFormLayout, QDialogButtonBox, QFileDialog, QColorDialog, QPushButton, QStyleOptionViewItem,
    QButtonGroup, QListWidget, QListWidgetItem, QSplitter, QStackedWidget, QPlainTextEdit, QScrollArea
)
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QDrag, QKeyEvent, QIcon, QPaintEvent, QDragEnterEvent, QDropEvent,
    QDragMoveEvent, QMouseEvent, QAction, QPixmap, QFont, QRegion
)
from PyQt6.QtCore import (
    Qt, QFileInfo, QMimeData, QRect, QFileSystemWatcher, QTimer, QPoint, QPointF,
    QUrl, QItemSelection, QItemSelectionModel, pyqtSignal, QPropertyAnimation, QRectF, QSize
)
from functools import partial
import qtawesome as qta

from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log
from utils.helpers import LARGE_FILE_SIZE_BYTES
from .icon_provider import CustomFileIconProvider
from .context_menu import populate_project_context_menu
from .helpers import get_git_statuses_for_root
from app_core.project_icon_manager import ProjectIconManager
from app_core.theme_manager import ThemeManager

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager


TREE_ITEM_MIME_TYPE = "application/x-Koromali-tree-item"
PROJECT_MIME_TYPE = "application/x-Koromali-project-item"

# --- Preview behavior caps ---
MAX_TEXT_PREVIEW_BYTES = 512 * 1024  # 512 KB cap for text preview
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg', '.webp'}
BINARY_EXTS = {
    '.exe', '.dll', '.so', '.o', '.a', '.lib', '.dylib', '.app', '.msi',
    '.zip', '.rar', '.7z', '.gz', '.tar', '.bz2', '.iso', '.db', '.sqlite3',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.gguf', '.bin',
    '.pth', '.safetensors', '.onnx'
}


class SystemIconPickerDialog(QDialog):
    """A dialog to select a standard system icon or a default application icon."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Project Icon")
        self.setMinimumSize(450, 550)
        self.selected_icon_data = None  # Will be ('type', identifier)

        layout = QVBoxLayout(self)
        self.icon_list = QListWidget()
        self.icon_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.icon_list.setIconSize(QSize(24, 24))
        self.icon_list.setSpacing(10)
        self.icon_list.setMovement(QListWidget.Movement.Static)
        self.icon_list.itemDoubleClicked.connect(self.accept)
        layout.addWidget(self.icon_list)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self._populate_icons()

    def _add_category_header(self, title: str):
        """Adds a non-selectable header item to the list."""
        header = QListWidgetItem(title.upper())
        header.setFlags(Qt.ItemFlag.NoItemFlags)
        font = header.font(); font.setBold(True); header.setFont(font)
        header.setForeground(QColor("#888"))
        self.icon_list.addItem(header)

    def _populate_icons(self):
        style = QApplication.style()

        system_icons = {
            "Folders & Drives": ['SP_DirIcon', 'SP_FileIcon', 'SP_DriveFDIcon', 'SP_DriveHDIcon', 'SP_ComputerIcon'],
            "Actions": ['SP_DialogOkButton', 'SP_DialogCancelButton', 'SP_DialogHelpButton', 'SP_TrashIcon', 'SP_ArrowUp', 'SP_ArrowDown', 'SP_ArrowLeft', 'SP_ArrowRight'],
            "Information": ['SP_MessageBoxInformation', 'SP_MessageBoxWarning', 'SP_MessageBoxCritical', 'SP_MessageBoxQuestion']
        }

        app_icons = {
            "Application Icons": ['mdi.folder-cog-outline', 'mdi.git', 'mdi.folder-zip-outline', 'mdi.folder-key-outline', 'mdi.folder-pound-outline', 'mdi.python']
        }

        self._add_category_header("Application Icons")
        for category, icon_names in app_icons.items():
            for name in icon_names:
                icon = qta.icon(name, color="#83c092")
                display_name = name.replace("mdi.", "").replace("-", " ").title()
                item = QListWidgetItem(icon, display_name)
                item.setData(Qt.ItemDataRole.UserRole, ('qta', name))
                self.icon_list.addItem(item)

        for category, icon_keys in system_icons.items():
            self._add_category_header(category)
            for key in icon_keys:
                if hasattr(QStyle.StandardPixmap, key):
                    enum_value = getattr(QStyle.StandardPixmap, key)
                    icon = style.standardIcon(enum_value)
                    if not icon.isNull():
                        display_name = key.replace("SP_", "").replace("Icon", "")
                        item = QListWidgetItem(icon, display_name)
                        item.setData(Qt.ItemDataRole.UserRole, ('system', enum_value.value))
                        self.icon_list.addItem(item)

    def accept(self):
        if self.icon_list.currentItem():
            self.selected_icon_data = self.icon_list.currentItem().data(Qt.ItemDataRole.UserRole)
        super().accept()


class ProjectSettingsDialog(QDialog):
    """A dialog for managing project-specific settings like a custom icon."""

    def __init__(self, project_path: str, icon_manager: ProjectIconManager, settings_manager: "SettingsManager", parent=None):
        super().__init__(parent)
        self.project_path = project_path
        self.icon_manager = icon_manager
        self.settings_manager = settings_manager

        customizations = self.settings_manager.get('project_customizations', {})
        project_config = customizations.get(self.project_path, {})
        self.new_icon_path = project_config.get('icon_path')
        self.new_icon_color = project_config.get('icon_color')
        self.new_system_icon_enum = project_config.get('system_icon_enum')
        self.new_qta_icon_name = project_config.get('qta_icon_name')

        project_name = os.path.basename(project_path)
        self.setWindowTitle(f"Project Settings - {project_name}")
        self.setMinimumWidth(450)

        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        icon_layout = QHBoxLayout()
        self.icon_preview = QLabel()
        self.icon_preview.setFixedSize(QSize(32, 32))
        icon_layout.addWidget(self.icon_preview)

        browse_button = QPushButton("Browse...")
        browse_button.clicked.connect(self._browse_for_icon)
        icon_layout.addWidget(browse_button)

        color_button = QPushButton("Set Color...")
        color_button.clicked.connect(self._set_icon_color)
        icon_layout.addWidget(color_button)

        system_icon_button = QPushButton("System Icon...")
        system_icon_button.clicked.connect(self._select_system_icon)
        icon_layout.addWidget(system_icon_button)

        icon_layout.addStretch()

        form_layout.addRow("Custom Icon:", icon_layout)
        main_layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        reset_button = QPushButton("Reset to Default")
        reset_button.clicked.connect(self._reset_to_default)
        button_layout.addWidget(reset_button)
        button_layout.addStretch()

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_layout.addWidget(self.button_box)
        main_layout.addLayout(button_layout)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self._load_current_settings()

    def _load_current_settings(self):
        current_icon = self.icon_manager.get_icon(self.project_path)
        self.icon_preview.setPixmap(current_icon.pixmap(QSize(32, 32)))

    def _browse_for_icon(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Icon File", self.project_path,
                                              "Image Files (*.png *.ico *.jpg *.svg)")
        if path:
            self.new_icon_path = path
            self.new_icon_color = None
            self.new_system_icon_enum = None
            self.new_qta_icon_name = None
            pixmap = QPixmap(path)
            self.icon_preview.setPixmap(
                pixmap.scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def _set_icon_color(self):
        initial_color = QColor(self.new_icon_color) if self.new_icon_color else Qt.GlobalColor.white
        color = QColorDialog.getColor(initial_color, self, "Select Icon Color")
        if color.isValid():
            self.new_icon_color = color.name()
            self.new_icon_path = None
            self.new_system_icon_enum = None
            if not self.new_qta_icon_name:
                self.new_qta_icon_name = 'mdi.folder-outline'
            colored_icon = qta.icon(self.new_qta_icon_name, color=color)
            self.icon_preview.setPixmap(colored_icon.pixmap(QSize(32, 32)))

    def _select_system_icon(self):
        dialog = SystemIconPickerDialog(self)
        if dialog.exec():
            icon_type, identifier = dialog.selected_icon_data
            if icon_type == 'system':
                self.new_system_icon_enum = identifier
                self.new_qta_icon_name = None
                icon = QApplication.style().standardIcon(QStyle.StandardPixmap(self.new_system_icon_enum))
            elif icon_type == 'qta':
                self.new_qta_icon_name = identifier
                self.new_system_icon_enum = None
                color = self.new_icon_color or self.icon_manager.theme_manager.current_theme_data.get('colors', {}).get('accent', '#83c092')
                icon = qta.icon(self.new_qta_icon_name, color=color)

            self.new_icon_path = None
            self.icon_preview.setPixmap(icon.pixmap(QSize(32, 32)))

    def _reset_to_default(self):
        self.new_icon_path = None
        self.new_icon_color = None
        self.new_system_icon_enum = None
        self.new_qta_icon_name = None
        self.icon_manager.clear_customization(self.project_path)
        default_icon = self.icon_manager.get_icon(self.project_path)
        self.icon_preview.setPixmap(default_icon.pixmap(QSize(32, 32)))

    def accept(self):
        if self.new_icon_path is None and self.new_icon_color is None and self.new_system_icon_enum is None and self.new_qta_icon_name is None:
            self.icon_manager.clear_customization(self.project_path)
        else:
            self.icon_manager.set_customization(
                self.project_path,
                self.new_icon_path,
                self.new_icon_color,
                self.new_system_icon_enum,
                self.new_qta_icon_name
            )
        super().accept()


class NoDrawProxyStyle(QProxyStyle):
    """A proxy style to prevent drawing the default expand/collapse arrows."""
    def drawPrimitive(self, element: QStyle.PrimitiveElement, option, painter, widget=None):
        if element == QStyle.PrimitiveElement.PE_IndicatorBranch:
            return
        super().drawPrimitive(element, option, painter, widget)


class StyledTreeView(QTreeWidget):
    """A QTreeWidget with custom branch painting and enhanced drag-and-drop feedback."""
    def __init__(self, koromali_api: KoromaliPluginAPI, parent_view: 'FileSystemListView', parent: QWidget = None):
        super().__init__(parent)
        self.koromali_api = koromali_api
        self.parent_view = parent_view
        self.theme_manager = koromali_api.get_manager("theme")
        self.file_handler = koromali_api.get_manager("file_handler")

        self.setStyle(NoDrawProxyStyle(self.style()))
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(False)
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setExpandsOnDoubleClick(False)

        self._internal_drop_pending = False
        self._drop_target_indicator_rect = QRectF()

    def startDrag(self, supportedActions: Qt.DropAction):
        items = self.selectedItems()
        if not items:
            return

        item = items[0]
        data = self.mimeData(items)
        if not data:
            return

        drag = QDrag(self)
        drag.setMimeData(data)

        pixmap_widget = QWidget()
        pixmap_layout = QHBoxLayout(pixmap_widget)
        pixmap_widget.setLayout(pixmap_layout)
        pixmap_layout.setContentsMargins(5, 5, 5, 5)

        icon_label = QLabel()
        icon_label.setPixmap(item.icon(0).pixmap(16, 16))
        pixmap_layout.addWidget(icon_label)

        text_label = QLabel(item.text(0))
        text_label.setFont(self.font())
        pixmap_layout.addWidget(text_label)

        theme_colors = self.theme_manager.current_theme_data.get('colors', {})
        bg_color = theme_colors.get('list.activeSelectionBackground', '#2d334f')
        fg_color = theme_colors.get('list.activeSelectionForeground', '#d3c6aa')
        pixmap_widget.setStyleSheet(f"background-color: {bg_color}; color: {fg_color}; border-radius: 4px;")

        pixmap_widget.adjustSize()

        pixmap = QPixmap(pixmap_widget.size())
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        pixmap_widget.render(painter)
        painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(10, 10))

        self._internal_drop_pending = False
        result = drag.exec(supportedActions, Qt.DropAction.MoveAction)

        if result == Qt.DropAction.MoveAction and not self._internal_drop_pending:
            log.info("External move detected. Refreshing parent view.")
            self.parent_view.refresh()

    def supportedDropActions(self) -> Qt.DropAction:
        return Qt.DropAction.CopyAction | Qt.DropAction.MoveAction

    def mimeData(self, items: List[QTreeWidgetItem]) -> Optional[QMimeData]:
        if not items:
            return None

        mime = QMimeData()
        first_item_data = items[0].data(0, Qt.ItemDataRole.UserRole)
        first_item_path = first_item_data.get('path') if first_item_data else None

        if not first_item_path or first_item_data.get('is_root'):
            return None

        mime.setData(TREE_ITEM_MIME_TYPE, first_item_path.encode('utf-8'))

        urls = []
        for item in items:
            data = item.data(0, Qt.ItemDataRole.UserRole)
            path = data.get('path') if data else None
            if path:
                urls.append(QUrl.fromLocalFile(path))
        mime.setUrls(urls)

        return mime

    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.topLevelItemCount() > 0:
            colors = self.theme_manager.current_theme_data.get('colors', {})
            pen = QPen(QColor(colors.get('accent', '#83c092')), 1)
            painter.setPen(pen)
            painter.drawLine(8, 0, 8, self.viewport().height())

        if not self._drop_target_indicator_rect.isNull():
            colors = self.theme_manager.current_theme_data.get('colors', {})
            drop_color = QColor(colors.get('accent', '#83c092'))
            drop_color.setAlpha(80)
            painter.fillRect(self._drop_target_indicator_rect, drop_color)

    def drawBranches(self, painter: QPainter, rect: QRect, index: 'QModelIndex'):
        # DO NOT CHANGE: keep diagonal style exactly as it is
        item = self.itemFromIndex(index)
        if not item or not item.parent() or item.parent() == self.invisibleRootItem():
            return
        colors = self.theme_manager.current_theme_data.get('colors', {})
        accent_color = QColor(colors.get('accent', '#83c092'))
        indent = self.indentation()
        half_indent = indent / 2.0
        ROOT_ITEM_OFFSET = 14

        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        depth = -1
        temp_item = item
        while temp_item.parent() and temp_item.parent() != self.invisibleRootItem():
            depth += 1
            temp_item = temp_item.parent()

        if depth < 0:
            painter.restore()
            return

        painter.setPen(QPen(accent_color, 1))
        for i in range(depth):
            ancestor = item
            for _ in range(depth - i):
                ancestor = ancestor.parent()
            if ancestor.parent() and ancestor.parent().indexOfChild(ancestor) < ancestor.parent().childCount() - 1:
                line_x = ROOT_ITEM_OFFSET + (i * indent) + half_indent
                painter.drawLine(QPointF(line_x, rect.top()), QPointF(line_x, rect.bottom()))

        item_is_folder = item.childCount() > 0 or (item.childCount() == 1 and not item.child(0).text(0))
        item_is_last_child = item.parent().indexOfChild(item) == item.parent().childCount() - 1
        expander_x = ROOT_ITEM_OFFSET + (depth * indent) + (indent * 0.25)
        parent_guide_x = (ROOT_ITEM_OFFSET + ((depth - 1) * indent) + half_indent) if depth > 0 else ROOT_ITEM_OFFSET
        center_y = rect.center().y()
        diagonal_start_y = rect.center().y() - 4.0

        if depth > 0:
            end_y = diagonal_start_y if item_is_last_child else rect.bottom()
            painter.drawLine(QPointF(parent_guide_x, rect.top()), QPointF(parent_guide_x, end_y))

        painter.setPen(QPen(accent_color, 2.0 if item_is_folder else 1.0))
        painter.drawLine(QPointF(parent_guide_x, diagonal_start_y), QPointF(expander_x, center_y))

        if item_is_folder:
            painter.setPen(QPen(accent_color, 1.2))
            self._draw_expander_at(painter, QPointF(expander_x, center_y), item.isExpanded())
        painter.restore()

    def _draw_expander_at(self, painter: QPainter, pos: QPointF, is_open: bool):
        arrow_size = 3.5
        p1 = pos + QPointF(-arrow_size / 2, -arrow_size)
        p2 = pos + QPointF(arrow_size / 2, 0)
        p3 = pos + QPointF(-arrow_size / 2, arrow_size)
        painter.save()
        painter.translate(pos)
        painter.rotate(90 if is_open else 0)
        painter.translate(-pos)
        painter.drawLine(p1, p2)
        painter.drawLine(p2, p3)
        painter.restore()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasFormat(TREE_ITEM_MIME_TYPE):
            event.accept()
        else:
            self._drop_target_indicator_rect = QRectF()
            self.viewport().update()
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event: QDragMoveEvent):
        if not event.mimeData().hasFormat(TREE_ITEM_MIME_TYPE):
            event.ignore()
            return

        source_path_bytes = event.mimeData().data(TREE_ITEM_MIME_TYPE)
        source_path = source_path_bytes.data().decode('utf-8')
        target_item = self.itemAt(event.position().toPoint())

        valid_drop_target = False
        if target_item:
            target_data = target_item.data(0, Qt.ItemDataRole.UserRole)
            target_path = target_data.get('path') if target_data else None

            if target_path and os.path.normpath(source_path) != os.path.normpath(target_path):
                dest_dir_item = target_item if target_data.get('is_dir') else target_item.parent()
                if dest_dir_item:
                    dest_data = dest_dir_item.data(0, Qt.ItemDataRole.UserRole)
                    dest_dir = dest_data.get('path')

                    if not (os.path.isdir(source_path) and os.path.normpath(dest_dir).startswith(
                            os.path.normpath(source_path) + os.sep)):
                        valid_drop_target = True
                        visual_target_rect = self.visualItemRect(dest_dir_item)
                        self._drop_target_indicator_rect = QRectF(0, visual_target_rect.y(),
                                                                  self.viewport().width(),
                                                                  visual_target_rect.height())

        if valid_drop_target:
            event.acceptProposedAction()
        else:
            event.ignore()
            self._drop_target_indicator_rect = QRectF()

        self.viewport().update()

    def dragLeaveEvent(self, event):
        self._drop_target_indicator_rect = QRectF()
        self.viewport().update()
        super().dragLeaveEvent(event)

    def dropEvent(self, event: QDropEvent):
        self._drop_target_indicator_rect = QRectF()
        self.viewport().update()

        if not event.mimeData().hasFormat(TREE_ITEM_MIME_TYPE):
            event.ignore()
            return

        self._internal_drop_pending = True
        source_path = event.mimeData().data(TREE_ITEM_MIME_TYPE).data().decode('utf-8')
        target_item = self.itemAt(event.position().toPoint())
        if not target_item:
            event.ignore()
            return

        target_data = target_item.data(0, Qt.ItemDataRole.UserRole)
        target_path = target_data.get('path')
        if not target_path:
            event.ignore()
            return

        dest_dir_item = target_item if target_data.get('is_dir') else target_item.parent()
        if not dest_dir_item:
            event.ignore()
            return

        dest_dir = dest_dir_item.data(0, Qt.ItemDataRole.UserRole)['path']

        is_copy = (QApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier) == Qt.KeyboardModifier.ControlModifier

        operation = self.file_handler.copy_item_to_dest if is_copy else self.file_handler.move_item
        success, new_path = self.parent_view._perform_file_operation(operation, source_path, dest_dir,
                                                                      return_result=True)

        if success:
            log.info("Internal drag-drop successful. View will be refreshed by file handler signal.")

        event.acceptProposedAction()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Delete:
            selected_items = self.selectedItems()
            paths = [item.data(0, Qt.ItemDataRole.UserRole)['path'] for item in selected_items if
                     item.data(0, Qt.ItemDataRole.UserRole)]
            if paths:
                self.parent_view._action_delete(paths)
                event.accept()
                return
        super().keyPressEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        super().mousePressEvent(event)

        if event.button() == Qt.MouseButton.LeftButton:
            item = self.itemAt(event.pos())
            if not item:
                self.clearSelection()
                return
            if (data := item.data(0, Qt.ItemDataRole.UserRole)) and data.get('is_dir'):
                self.parent_view.blockSignals(True)
                self.parent_view._lock_scroll()
                item.setExpanded(not item.isExpanded())
                self.parent_view.blockSignals(False)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        super().mouseDoubleClickEvent(event)


class ProjectButton(QToolButton):
    """A draggable button for the Project Dock with a context menu."""
    project_activated = pyqtSignal(str)

    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.path = path
        self.setCheckable(True)
        self.setAutoRaise(True)
        self.drag_start_pos = QPoint()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.clicked.connect(self._on_clicked)

    def _on_clicked(self):
        self.project_activated.emit(self.path)

    def show_context_menu(self, pos: QPoint):
        """Creates and shows the context menu."""
        if isinstance(dock := self.parent(), ProjectDock):
            dock.show_project_button_context_menu(self.mapToGlobal(pos), self.path)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return
        if (event.pos() - self.drag_start_pos).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mime = QMimeData()
        mime.setData(PROJECT_MIME_TYPE, self.path.encode('utf-8'))
        drag.setMimeData(mime)

        pixmap = self.icon().pixmap(32, 32)
        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(16, 16))
        drag.exec(Qt.DropAction.MoveAction)


class ProjectDock(QWidget):
    """A vertical dock for managing and reordering project folders."""
    orderChanged = pyqtSignal(list)

    def __init__(self, api: KoromaliPluginAPI, parent=None):
        super().__init__(parent)
        self.api = api
        self.project_manager = self.api.get_manager("project")
        self.file_handler = self.api.get_manager("file_handler")
        self.theme_manager: ThemeManager = self.api.get_manager("theme")

        self.setAcceptDrops(True)
        self.setFixedWidth(50)
        self.setObjectName("ProjectDock")

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(5)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        self._drag_indicator = QWidget(self)
        self._drag_indicator.setFixedSize(self.width() - 10, 4)
        self._drag_indicator.hide()

        self._setup_ui()
        self.update_theme()

    def _setup_ui(self):
        add_project_button = QToolButton()
        add_project_button.setIcon(qta.icon('mdi.folder-plus-outline'))
        add_project_button.setToolTip("Create New Project...")
        add_project_button.setAutoRaise(True)
        add_project_button.clicked.connect(self.api.get_main_window().action_create_new_project)
        self.layout.addWidget(add_project_button)
        self.layout.addStretch()

    def update_theme(self):
        """Applies a theme-aware stylesheet for active project highlighting."""
        colors = self.theme_manager.current_theme_data.get('colors', {})
        bg_color = colors.get('tab.activeBackground', '#424d53')
        accent_color = colors.get('accent', '#83c092')
        hover_bg_color = QColor(accent_color)
        hover_bg_color.setAlphaF(0.15)

        rgba_hover_str = f"rgba({hover_bg_color.red()}, {hover_bg_color.green()}, {hover_bg_color.blue()}, {hover_bg_color.alphaF()})"

        self.setStyleSheet(f"""
            QToolButton {{
                border-left: 3px solid transparent;
                border-radius: 4px;
            }}
            QToolButton:checked {{
                background-color: {bg_color};
                border-left: 3px solid {accent_color};
            }}
            QToolButton:hover:!checked {{
                background-color: {rgba_hover_str};
            }}
        """)
        indicator_color = QColor(accent_color)
        indicator_color.setAlpha(180)
        self._drag_indicator.setStyleSheet(f"background-color: {indicator_color.name()}; border-radius: 2px;")

    def add_project(self, path, name, icon):
        button = ProjectButton(path, self)
        button.setFixedSize(QSize(40, 40))
        button.setIcon(icon)
        button.setIconSize(QSize(24, 24))
        button.setToolTip(f"{name}\n{path}")
        button.project_activated.connect(self.project_manager.set_active_project)
        self.button_group.addButton(button)
        self.layout.insertWidget(self.layout.count() - 1, button)

    def clear_projects(self):
        while self.layout.count() > 2:
            item = self.layout.takeAt(1)
            if widget := item.widget():
                self.button_group.removeButton(widget)
                widget.deleteLater()

    def project_paths(self):
        paths = []
        for i in range(self.layout.count()):
            if isinstance(widget := self.layout.itemAt(i).widget(), ProjectButton):
                paths.append(widget.path)
        return paths

    def show_project_button_context_menu(self, position: QPoint, path: str):
        """Creates and shows a context menu for a project button."""
        menu = QMenu(self)
        menu.addAction(
            qta.icon('mdi.folder-cog-outline'),
            "Project Settings...",
            lambda: self.parent()._show_project_settings_dialog(path)
        )
        menu.addSeparator()
        menu.addAction(
            qta.icon('mdi.folder-remove-outline'),
            "Close Project",
            lambda: self.project_manager.close_project(path)
        )
        menu.addSeparator()
        menu.addAction(
            "Reveal in Explorer",
            lambda: self.file_handler.reveal_in_explorer(path)
        )
        menu.exec(position)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasFormat(PROJECT_MIME_TYPE):
            event.accept()
            source = event.source()
            if isinstance(source, ProjectButton):
                source.hide()

    def dragLeaveEvent(self, event):
        self._drag_indicator.hide()
        for i in range(self.layout.count()):
            if isinstance(widget := self.layout.itemAt(i).widget(), ProjectButton):
                widget.show()

    def dragMoveEvent(self, event: QDragMoveEvent):
        pos_y = event.position().y()
        index_at_pos = -1

        for i in range(self.layout.count() - 1):
            if isinstance(widget := self.layout.itemAt(i).widget(), ProjectButton):
                if pos_y < widget.y() + widget.height() / 2:
                    index_at_pos = i
                    break

        if index_at_pos == -1 and self.layout.count() > 2:
            index_at_pos = self.layout.count() - 1

        if index_at_pos > 0:
            target_widget = self.layout.itemAt(index_at_pos).widget() if index_at_pos < self.layout.count() - 1 else None

            last_button_item = self.layout.itemAt(self.layout.count() - 2)
            last_button_widget = last_button_item.widget() if last_button_item else None

            y_pos = target_widget.y() - self.layout.spacing() // 2 if target_widget else \
                (last_button_widget.y() + last_button_widget.height() + self.layout.spacing() // 2 if last_button_widget else 0)

            self._drag_indicator.move(QPoint(5, int(y_pos)))
            self._drag_indicator.show()

    def dropEvent(self, event: QDropEvent):
        """Handles dropping a project button to reorder it."""
        self._drag_indicator.hide()
        source_path = event.mimeData().data(PROJECT_MIME_TYPE).data().decode('utf-8')

        current_order = self.project_paths()
        if source_path not in current_order:
            event.ignore()
            return

        current_order.remove(source_path)

        # Determine the target drop index relative to the project buttons
        pos_y = event.position().y()
        target_project_index = 0

        project_buttons = [self.layout.itemAt(i).widget() for i in range(self.layout.count())
                           if isinstance(self.layout.itemAt(i).widget(), ProjectButton)]

        for i, button in enumerate(project_buttons):
            if button.path != source_path:
                if pos_y < button.y() + button.height() / 2:
                    target_project_index = i
                    break
                else:
                    target_project_index = i + 1

        current_order.insert(target_project_index, source_path)

        self.orderChanged.emit(current_order)
        event.acceptProposedAction()

        # Ensure the dragged button is visible again
        source_widget = event.source()
        if isinstance(source_widget, ProjectButton):
            source_widget.show()


class FileSystemListView(QWidget):
    DEFAULT_IGNORED_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'node_modules', '.vscode', '.idea'}

    def __init__(self, koromali_api: KoromaliPluginAPI, parent: QWidget = None):
        super().__init__(parent)
        self.api = koromali_api
        self.project_manager = self.api.get_manager("project")
        self.file_handler = self.api.get_manager("file_handler")
        self.theme_manager = self.api.get_manager("theme")
        self.settings_manager = self.api.get_manager("settings")
        self.icon_provider = CustomFileIconProvider(self.api)
        self.project_icon_manager = ProjectIconManager(self.theme_manager, self.settings_manager)
        self.git_statuses = {}
        self.fs_watcher = QFileSystemWatcher(self)
        self.watched_paths = set()
        self._refresh_timer = QTimer(self)
        self._refresh_timer.setSingleShot(True)
        self._refresh_timer.setInterval(300)
        self._is_programmatic_change = False

        self.scroll_lock_timer = QTimer(self)
        self.scroll_lock_timer.setSingleShot(True)
        self.scroll_lock_timer.setInterval(5000)
        self._is_scroll_locked = False

        # Preview state
        self._preview_update_timer = QTimer(self)
        self._preview_update_timer.setSingleShot(True)
        self._preview_update_timer.setInterval(120)  # debounce selection
        self._preview_visible = self.settings_manager.get("explorer_preview_visible", True)

        self._setup_ui()
        self._connect_signals()
        self.api.get_main_window().theme_changed_signal.connect(self.project_dock.update_theme)

    # ---------------- UI ----------------

    def _setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.project_dock = ProjectDock(self.api, self)
        main_layout.addWidget(self.project_dock)

        # Left: tree container (unchanged)
        self.tree_container = QWidget()
        layout = QVBoxLayout(self.tree_container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar_frame = QFrame()
        toolbar_frame.setObjectName("ExplorerToolbar")
        toolbar_layout = QHBoxLayout(toolbar_frame)
        toolbar_layout.setContentsMargins(5, 2, 5, 2)
        toolbar_layout.setSpacing(5)
        self.expand_button = QToolButton(icon=qta.icon('mdi.arrow-expand-all', color='gray'), toolTip="Expand All",
                                         autoRaise=True)
        self.collapse_button = QToolButton(icon=qta.icon('mdi.arrow-collapse-all', color='gray'),
                                           toolTip="Collapse All", autoRaise=True)
        self.refresh_button = QToolButton(icon=qta.icon('mdi.refresh', color='gray'), toolTip="Refresh", autoRaise=True)

        self.toggle_hidden_button = QToolButton(autoRaise=True, checkable=True)

        # Preview toggle
        self.toggle_preview_button = QToolButton(autoRaise=True, checkable=True)
        self.toggle_preview_button.setChecked(self._preview_visible)
        self.toggle_preview_button.setToolTip("Hide Preview" if self._preview_visible else "Show Preview")
        self.toggle_preview_button.setIcon(qta.icon('mdi.dock-right' if self._preview_visible else 'mdi.dock-window', color='gray'))

        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.toggle_hidden_button)
        toolbar_layout.addWidget(self.toggle_preview_button)
        toolbar_layout.addWidget(self.expand_button)
        toolbar_layout.addWidget(self.collapse_button)
        toolbar_layout.addWidget(self.refresh_button)
        layout.addWidget(toolbar_frame)

        self.tree_widget = StyledTreeView(self.api, self)
        self.tree_widget.setHeaderHidden(True)
        self.tree_widget.setAlternatingRowColors(True)
        self.tree_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tree_widget.setIndentation(14)
        layout.addWidget(self.tree_widget)

        # Right: preview container
        self.preview_container = self._build_preview_ui()

        # Splitter to hold tree + preview (project dock stays separate)
        self.splitter = QSplitter(Qt.Orientation.Horizontal, self)
        self.splitter.addWidget(self.tree_container)
        self.splitter.addWidget(self.preview_container)
        self.splitter.setStretchFactor(0, 5)
        self.splitter.setStretchFactor(1, 4)
        if not self._preview_visible:
            self.preview_container.hide()

        main_layout.addWidget(self.splitter)

        # Restore splitter sizes if present
        sizes = self.settings_manager.get("explorer_splitter_sizes", None)
        if isinstance(sizes, list) and len(sizes) == 2:
            self.splitter.setSizes([int(sizes[0]), int(sizes[1])])

    def _build_preview_ui(self) -> QWidget:
        wrap = QWidget()
        lay = QVBoxLayout(wrap)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        # Header (path + size)
        self.preview_header = QFrame()
        header_layout = QHBoxLayout(self.preview_header)
        header_layout.setContentsMargins(8, 4, 8, 4)
        header_layout.setSpacing(6)

        self.preview_icon = QLabel()
        self.preview_icon.setFixedSize(16, 16)
        self.preview_path_label = QLabel("No file selected")
        self.preview_path_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        header_layout.addWidget(self.preview_icon)
        header_layout.addWidget(self.preview_path_label, 1)

        self.preview_info_label = QLabel("")
        header_layout.addWidget(self.preview_info_label)

        lay.addWidget(self.preview_header)

        # Body
        self.preview_stack = QStackedWidget()
        # 0: empty
        self.preview_empty = QLabel("Select a file to preview")
        self.preview_empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_stack.addWidget(self.preview_empty)

        # 1: text
        self.preview_text = QPlainTextEdit()
        self.preview_text.setReadOnly(True)
        mono = QFont("Consolas"); mono.setStyleHint(QFont.StyleHint.Monospace)
        self.preview_text.setFont(mono)
        self.preview_stack.addWidget(self.preview_text)

        # 2: image
        self.preview_image_scroll = QScrollArea()
        self.preview_image_scroll.setWidgetResizable(True)
        self.preview_image_label = QLabel()
        self.preview_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_image_scroll.setWidget(self.preview_image_label)
        self.preview_stack.addWidget(self.preview_image_scroll)

        lay.addWidget(self.preview_stack, 1)
        self._apply_theme_to_preview()
        return wrap

    def _apply_theme_to_preview(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        bg = colors.get('panel.background', '#2b2f3a')
        fg = colors.get('panel.foreground', '#cbd3e1')
        border = colors.get('panel.border', '#3b414d')
        self.preview_header.setStyleSheet(
            f"QFrame {{ background: {bg}; border-left: 1px solid {border}; }}"
            f"QLabel {{ color: {fg}; }}"
        )

    # ---------------- Signals ----------------

    def _connect_signals(self):
        self.expand_button.clicked.connect(self.expand_all)
        self.collapse_button.clicked.connect(self.collapse_all)
        self.refresh_button.clicked.connect(self.refresh)
        self.toggle_hidden_button.toggled.connect(self._on_toggle_hidden)
        self.tree_widget.itemExpanded.connect(self.on_item_expanded)
        self.tree_widget.itemCollapsed.connect(self.on_item_collapsed)
        self.tree_widget.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.tree_widget.customContextMenuRequested.connect(self.show_context_menu)
        self.fs_watcher.directoryChanged.connect(self._schedule_refresh)
        self.fs_watcher.fileChanged.connect(self._schedule_refresh)
        self._refresh_timer.timeout.connect(self.refresh)
        self.project_dock.orderChanged.connect(self._on_project_reordered)
        self.project_manager.projects_changed.connect(self.refresh)

        if (git_manager := self.api.get_manager("git")):
            git_manager.git_success.connect(self.refresh)
        self.file_handler.item_created.connect(self._on_item_created)
        self.file_handler.item_renamed.connect(self._on_item_renamed)
        self.file_handler.item_deleted.connect(self._on_item_deleted)

        self.scroll_lock_timer.timeout.connect(self._unlock_scroll)
        v_scrollbar = self.tree_widget.verticalScrollBar()
        v_scrollbar.sliderPressed.connect(self._lock_scroll)
        v_scrollbar.actionTriggered.connect(self._lock_scroll)

        # Preview / selection wiring
        self.tree_widget.itemSelectionChanged.connect(self._on_selection_changed)
        self._preview_update_timer.timeout.connect(self._update_preview_from_selection)
        self.toggle_preview_button.toggled.connect(self._on_toggle_preview)

    # ---------------- Preview ----------------

    def _on_toggle_preview(self, checked: bool):
        self._preview_visible = checked
        self.settings_manager.set("explorer_preview_visible", checked)
        self.toggle_preview_button.setToolTip("Hide Preview" if checked else "Show Preview")
        self.toggle_preview_button.setIcon(qta.icon('mdi.dock-right' if checked else 'mdi.dock-window', color='gray'))
        if checked:
            self.preview_container.show()
        else:
            self.preview_container.hide()

        # Remember splitter sizes
        self.settings_manager.set("explorer_splitter_sizes", self.splitter.sizes())

    def _on_selection_changed(self):
        self._preview_update_timer.start()

    def _update_preview_from_selection(self):
        if not self._preview_visible:
            return
        items = self.tree_widget.selectedItems()
        if not items:
            self._set_preview_empty("No file selected")
            return
        if len(items) > 1:
            self._set_preview_empty("Multiple items selected")
            return

        data = items[0].data(0, Qt.ItemDataRole.UserRole) or {}
        path = data.get('path'); is_dir = data.get('is_dir', False)
        if not path or is_dir or not os.path.exists(path):
            self._set_preview_empty("Folder selected")
            return

        self._render_preview_for_path(path)

    def _set_preview_empty(self, msg: str):
        self.preview_path_label.setText(msg)
        self.preview_info_label.setText("")
        self.preview_icon.setPixmap(QPixmap())
        self.preview_stack.setCurrentIndex(0)

    def _render_preview_for_path(self, path: str):
        file_info = QFileInfo(path)
        self.preview_path_label.setText(os.path.basename(path))
        self.preview_icon.setPixmap(self.icon_provider.icon(file_info).pixmap(16, 16))

        try:
            size = os.path.getsize(path)
        except OSError:
            size = 0
        self.preview_info_label.setText(f"{size:,} bytes")

        _, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext in IMAGE_EXTS:
            pix = QPixmap(path)
            if pix.isNull():
                self._set_preview_empty("Unable to render image")
                return
            self.preview_image_label.setPixmap(pix)
            self.preview_stack.setCurrentIndex(2)
            return

        if ext in BINARY_EXTS:
            self._set_preview_empty("Binary file")
            return

        # Try reading text safely
        try:
            with open(path, "rb") as f:
                data = f.read(MAX_TEXT_PREVIEW_BYTES + 1)
            if b'\x00' in data:
                self._set_preview_empty("Binary file")
                return
            truncated = len(data) > MAX_TEXT_PREVIEW_BYTES
            text = data[:MAX_TEXT_PREVIEW_BYTES].decode("utf-8", errors="ignore")
            if truncated:
                text += "\n\n… (preview truncated)"
            self.preview_text.setPlainText(text)
            self.preview_stack.setCurrentIndex(1)
        except Exception as e:
            log.warning(f"Preview read failed for '{path}': {e}")
            self._set_preview_empty("Unable to preview file")

    # ---------------- Existing behavior (kept) ----------------

    def _connect_theme(self):
        self._apply_theme_to_preview()

    def _lock_scroll(self):
        self._is_scroll_locked = True
        self.scroll_lock_timer.start()

    def _unlock_scroll(self):
        self._is_scroll_locked = False

    def _update_toggle_hidden_button_state(self):
        show_hidden = self.settings_manager.get("explorer_show_hidden_files", False)
        self.toggle_hidden_button.setChecked(show_hidden)
        self.toggle_hidden_button.setToolTip("Hide hidden files/folders" if show_hidden else "Show hidden files/folders")
        icon_name = 'mdi.eye-outline' if show_hidden else 'mdi.eye-off-outline'
        self.toggle_hidden_button.setIcon(qta.icon(icon_name, color='gray'))

    def _on_toggle_hidden(self, checked):
        self.settings_manager.set("explorer_show_hidden_files", checked)
        self.refresh()

    def set_project_enabled(self, project_path: str, is_enabled: bool):
        """
        Enables or disables interaction for all items belonging to a specific project root.
        """
        norm_path = os.path.normpath(project_path)
        root_item = self._find_item_by_path(norm_path)

        if not root_item:
            log.warning(f"Could not find project root item to lock/unlock: {project_path}")
            return

        font = root_item.font(0)
        font.setItalic(not is_enabled)  # visually indicate locked state (italic when disabled)
        root_item.setFont(0, font)

        self._recursive_set_enabled(root_item, is_enabled)

    def _recursive_set_enabled(self, item: QTreeWidgetItem, is_enabled: bool):
        """Helper to recursively set the enabled state of tree items."""
        current_flags = item.flags()
        if is_enabled:
            item.setFlags(current_flags | Qt.ItemFlag.ItemIsEnabled)
        else:
            item.setFlags(current_flags & ~Qt.ItemFlag.ItemIsEnabled)

        for i in range(item.childCount()):
            if child := item.child(i):
                self._recursive_set_enabled(child, is_enabled)

    def _find_item_by_path(self, path_to_find: str) -> Optional[QTreeWidgetItem]:
        """Finds a QTreeWidgetItem in the tree by its stored file path."""
        norm_path = os.path.normpath(path_to_find)
        iterator = QTreeWidgetItemIterator(self.tree_widget)
        while iterator.value():
            item = iterator.value()
            if data := item.data(0, Qt.ItemDataRole.UserRole):
                if os.path.normpath(data.get('path', '')) == norm_path:
                    return item
            iterator += 1
        return None

    def _action_new_file(self, target_dir: str):
        file_name, ok = QInputDialog.getText(self, "New File", "Enter file name:")
        if ok and file_name:
            self._perform_file_operation(self.file_handler.create_file, os.path.join(target_dir, file_name))

    def _action_new_folder(self, target_dir: str):
        folder_name, ok = QInputDialog.getText(self, "New Folder", "Enter folder name:")
        if ok and folder_name:
            self._perform_file_operation(self.file_handler.create_folder, os.path.join(target_dir, folder_name))

    def _action_rename(self, path: str):
        old_name = os.path.basename(path)
        new_name, ok = QInputDialog.getText(self, f"Rename '{old_name}'", "Enter new name:", text=old_name)
        if ok and new_name and new_name != old_name:
            self._perform_file_operation(self.file_handler.rename_item, path, new_name)

    def _action_delete(self, paths: List[str]):
        if not paths:
            return

        names = ", ".join([f"'{os.path.basename(p)}'" for p in paths[:5]])
        if len(paths) > 5:
            names += ", ..."

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to permanently delete {len(paths)} item(s)?\n({names})",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            for path in paths:
                self._perform_file_operation(self.file_handler.delete_item, path)

    def _action_duplicate(self, path: str):
        self._perform_file_operation(self.file_handler.duplicate_item, path)

    def _action_cut(self, path: str):
        self.file_handler.cut_item(path)

    def _action_copy(self, paths: List[str]):
        if paths:
            self.file_handler.copy_item(paths[0])

    def _action_paste(self, target_dir: str):
        self._perform_file_operation(self.file_handler.paste_item, target_dir)

    def _action_remove_boms(self, path: str):
        if hasattr(self.file_handler, "remove_boms_in_path"):
            self.file_handler.remove_boms_in_path(path)
        else:
            QMessageBox.warning(self, "Feature Not Available",
                                "The 'remove_boms_in_path' feature is not available in the File Handler.")

    def _action_export_for_backup(self, project_path: str):
        """Scans all files in a project and prepares them for an AI export backup."""
        ai_suite = self.api.get_plugin_instance("ai_suite")
        if not ai_suite or not hasattr(ai_suite, 'perform_backup_export'):
            self.api.show_message("critical", "Missing Plugin", "AI Suite plugin is not available or out of date.")
            return

        all_files, large_files = [], []
        ignored_dirs = {'.git', '__pycache__', 'venv', '.venv', 'dist', 'build', 'node_modules', 'ai_exports', 'backups'}
        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if d not in ignored_dirs]
            for filename in files:
                filepath = os.path.join(root, filename)
                try:
                    if os.path.getsize(filepath) > LARGE_FILE_SIZE_BYTES:
                        large_files.append(filepath)
                    all_files.append(filepath)
                except OSError:
                    continue

        final_file_list = all_files
        if large_files:
            file_names_str = "\n".join([f"- {os.path.basename(f)}" for f in large_files[:5]])
            if len(large_files) > 5:
                file_names_str += "\n- ..."

            reply = QMessageBox.question(self, "Large Files Detected",
                                         f"The following large files were found:\n{file_names_str}\n\n"
                                         "Including them may result in a very large export file.\n"
                                         "Do you want to include them in the backup?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.No:
                final_file_list = [f for f in all_files if f not in large_files]

        ai_suite.perform_backup_export(project_path, final_file_list)

    def _show_project_settings_dialog(self, project_path: str):
        dialog = ProjectSettingsDialog(project_path, self.project_icon_manager, self.settings_manager, self)
        if dialog.exec():
            log.info("Project settings changed. Refreshing view.")
            self.refresh()

    def _perform_file_operation(self, operation_func, *args, return_result=False):
        try:
            self._is_programmatic_change = True
            success, message_or_data = operation_func(*args)
            if not success:
                QMessageBox.warning(self, "Operation Failed", str(message_or_data))
            if return_result:
                return success, message_or_data
        except Exception as e:
            log.critical(f"An unexpected error occurred during file operation '{operation_func.__name__}': {e}",
                         exc_info=True)
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")
            if return_result:
                return False, None
        finally:
            self._is_programmatic_change = False

    def expand_all(self):
        self.tree_widget.expandAll()
        self._save_expanded_state_to_settings()

    def collapse_all(self):
        self.tree_widget.collapseAll()
        self._save_expanded_state_to_settings()

    def get_expanded_paths(self):
        expanded = set()
        iterator = QTreeWidgetItemIterator(self.tree_widget)
        while iterator.value():
            item = iterator.value()
            if item.isExpanded() and (data := item.data(0, Qt.ItemDataRole.UserRole)) and (path := data.get('path')):
                expanded.add(os.path.normpath(path))
            iterator += 1
        return list(expanded)

    def _save_expanded_state_to_settings(self):
        if self._is_programmatic_change:
            return
        # Also remember splitter sizes to persist preview width
        self.settings_manager.set("explorer_splitter_sizes", self.splitter.sizes())
        self.settings_manager.set("explorer_expanded_paths", self.get_expanded_paths())

    def _on_item_created(self, item_type: str, path: str):
        log.debug(f"'{item_type}' created: {path}. Refreshing and selecting.")
        self.refresh()
        QTimer.singleShot(150, lambda: self._select_and_scroll_to_path(path))
        if item_type == "file":
            self.api.get_main_window()._action_open_file(path)

    def _on_item_renamed(self, item_type: str, old: str, new: str):
        log.debug(f"'{item_type}' renamed from {old} to {new}. Refreshing.")
        self.api.get_main_window()._on_file_renamed(old, new)
        self.refresh()
        QTimer.singleShot(100, lambda: self._select_and_scroll_to_path(new))

    def _on_item_deleted(self, item_type: str, path: str):
        log.debug(f"'{item_type}' deleted: {path}. Refreshing.")
        self.refresh()
        QTimer.singleShot(150, lambda: self._select_and_scroll_to_path(os.path.dirname(path)))

    def _on_project_reordered(self, new_order: list):
        self.project_manager.reorder_projects(new_order)
        self.refresh()

    def on_item_double_clicked(self, item: QTreeWidgetItem, col: int):
        if (data := item.data(0, Qt.ItemDataRole.UserRole)) and not data.get('is_dir') and (path := data.get('path')) and os.path.isfile(path):
            self.api.get_main_window()._action_open_file(path)

    def _schedule_refresh(self, path: str):
        if not self._is_programmatic_change and path in self.watched_paths:
            log.debug(f"FS change at '{path}'. Scheduling refresh.")
            self._refresh_timer.start()

    def refresh(self):
        log.info("Refreshing file explorer view.")
        self._is_programmatic_change = True
        self._update_toggle_hidden_button_state()

        expanded_paths = set(os.path.normpath(p) for p in self.get_expanded_paths())
        selected_paths = {os.path.normpath(item.data(0, Qt.ItemDataRole.UserRole)['path']) for item in
                          self.tree_widget.selectedItems() if item.data(0, Qt.ItemDataRole.UserRole)}

        self.tree_widget.blockSignals(True)

        current_watched = list(self.watched_paths)
        if current_watched:
            self.fs_watcher.removePaths(current_watched)
        self.watched_paths.clear()

        self.tree_widget.clear()
        self.project_dock.clear_projects()

        open_projects = self.project_manager.get_open_projects()
        get_git_statuses_for_root.cache_clear()
        # Clear cached git statuses if helper is memoized
        if hasattr(get_git_statuses_for_root, "cache_clear"):
            get_git_statuses_for_root.cache_clear()

        self.git_statuses = {p: get_git_statuses_for_root(p) for p in open_projects}
        self.flat_git_status = {k: v for d in self.git_statuses.values() for k, v in d.items()}

        show_hidden = self.settings_manager.get("explorer_show_hidden_files", False)

        def populate_children(parent_item, path):
            try:
                self._add_to_watcher(path)
                for entry in sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower())):
                    if not show_hidden and (entry.name.startswith('.') or entry.name in self.DEFAULT_IGNORED_DIRS):
                        continue

                    norm_path = os.path.normpath(entry.path)
                    child_item = QTreeWidgetItem(parent_item, [entry.name])
                    child_item.setIcon(0, self.icon_provider.icon(QFileInfo(entry.path)))
                    child_item.setData(0, Qt.ItemDataRole.UserRole, {'path': norm_path, 'is_dir': entry.is_dir()})

                    if status := self.flat_git_status.get(norm_path):
                        self._apply_git_coloring(child_item, status)

                    if entry.is_dir():
                        if norm_path in expanded_paths:
                            child_item.setExpanded(True)
                            populate_children(child_item, norm_path)
                        else:
                            child_item.addChild(QTreeWidgetItem([""]))
            except OSError as e:
                log.warning(f"OS error scanning directory '{path}': {e}")

        for proj_path in open_projects:
            norm_proj = os.path.normpath(proj_path)
            item = QTreeWidgetItem(self.tree_widget, [os.path.basename(norm_proj)])
            item.setToolTip(0, norm_proj)

            icon = self.project_icon_manager.get_icon(norm_proj)
            item.setIcon(0, icon)
            item.setData(0, Qt.ItemDataRole.UserRole, {'path': norm_proj, 'is_dir': True, 'is_root': True})

            self.project_dock.add_project(norm_proj, os.path.basename(norm_proj), icon)

            if norm_proj in expanded_paths:
                item.setExpanded(True)

            populate_children(item, proj_path)

        active_project_path = self.project_manager.get_active_project_path()
        for button in self.project_dock.button_group.buttons():
            if isinstance(button, ProjectButton) and button.path == active_project_path:
                button.setChecked(True)
                break

        if selected_paths:
            self._select_paths(selected_paths)

        self.tree_widget.blockSignals(False)
        self._is_programmatic_change = False

        # After refresh, update preview for current selection
        self._update_preview_from_selection()

    def _apply_git_coloring(self, item: QTreeWidgetItem, status: str):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        color_map = {'??': 'git.untracked', 'M': 'git.modified', 'A': 'git.added', 'D': 'git.deleted',
                     'R': 'git.renamed', '!!': 'git.ignored'}
        for code, color_key in color_map.items():
            if code in status:
                if color_val := colors.get(color_key):
                    item.setForeground(0, QColor(color_val))
                    break

    def _add_to_watcher(self, path):
        if path and os.path.isdir(path) and path not in self.watched_paths:
            self.fs_watcher.addPath(path)
            self.watched_paths.add(path)

    def _select_paths(self, paths_to_select: set):
        self.tree_widget.clearSelection()
        selection_model = self.tree_widget.selectionModel()
        selection = QItemSelection()

        iterator = QTreeWidgetItemIterator(self.tree_widget)
        first_item = None
        while iterator.value():
            item = iterator.value()
            if (data := item.data(0, Qt.ItemDataRole.UserRole)) and (path := data.get('path')):
                if os.path.normpath(path) in paths_to_select:
                    if not first_item:
                        first_item = item
                    selection.select(self.tree_widget.indexFromItem(item), self.tree_widget.indexFromItem(item))
            iterator += 1

        if not selection.isEmpty():
            selection_model.select(selection, QItemSelectionModel.SelectionFlag.Select | QItemSelectionModel.SelectionFlag.Rows)
            if first_item:
                self.tree_widget.scrollToItem(first_item, QAbstractItemView.ScrollHint.PositionAtCenter)

    def _select_and_scroll_to_path(self, path: str):
        if not path or self._is_scroll_locked:
            return
        try:
            item = self._find_item_by_path(path)
            if item:
                parent = item.parent()
                while parent:
                    parent.setExpanded(True)
                    parent = parent.parent()

                self.tree_widget.scrollToItem(item, QAbstractItemView.ScrollHint.PositionAtCenter)
                self.tree_widget.setCurrentItem(item)
                item.setSelected(True)

        except RuntimeError as e:
            log.warning(f"Scroll failed (ignored): {e}")

    def on_item_expanded(self, item: QTreeWidgetItem):
        if self._is_programmatic_change:
            return

        if (data := item.data(0, Qt.ItemDataRole.UserRole)) and data.get('is_dir'):
            if item.childCount() == 1 and not item.child(0).text(0):
                item.takeChildren()
                self._populate_node(item)
        self._lock_scroll()
        self._save_expanded_state_to_settings()

    def on_item_collapsed(self, item: QTreeWidgetItem):
        if not self._is_programmatic_change:
            self._lock_scroll()
            self._save_expanded_state_to_settings()

    def _populate_node(self, parent_item: QTreeWidgetItem):
        path = (data := parent_item.data(0, Qt.ItemDataRole.UserRole)) and data.get('path')
        if not path or not os.path.isdir(path):
            return

        self._is_programmatic_change = True
        try:
            self._add_to_watcher(path)
            show_hidden = self.settings_manager.get("explorer_show_hidden_files", False)
            for entry in sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower())):
                if not show_hidden and (entry.name.startswith('.') or entry.name in self.DEFAULT_IGNORED_DIRS):
                    continue

                norm_path = os.path.normpath(entry.path)
                child = QTreeWidgetItem(parent_item, [entry.name])
                child.setIcon(0, self.icon_provider.icon(QFileInfo(entry.path)))
                child.setData(0, Qt.ItemDataRole.UserRole, {'path': norm_path, 'is_dir': entry.is_dir()})

                if status := self.flat_git_status.get(norm_path):
                    self._apply_git_coloring(child, status)

                if entry.is_dir():
                    child.addChild(QTreeWidgetItem([""]))
        except OSError as e:
            log.warning(f"Lazy-load OS error scanning '{path}': {e}")
        finally:
            self._is_programmatic_change = False

    def show_context_menu(self, position: QPoint):
        global_pos = self.tree_widget.viewport().mapToGlobal(position)
        menu = QMenu(self.tree_widget)

        selected_items = self.tree_widget.selectedItems()

        paths = [item.data(0, Qt.ItemDataRole.UserRole)['path'] for item in selected_items if item.data(0, Qt.ItemDataRole.UserRole)]

        if not paths:
            item_at_pos = self.tree_widget.itemAt(position)
            if item_at_pos:
                root = item_at_pos
                while root.parent():
                    root = root.parent()
                if (data := root.data(0, Qt.ItemDataRole.UserRole)) and (project_path := data.get('path')):
                    paths = [project_path]
                else:
                    if project_path := self.project_manager.get_active_project_path():
                        paths = [project_path]
                    else:
                        return
            else:
                if project_path := self.project_manager.get_active_project_path():
                    paths = [project_path]
                else:
                    return

        is_multi = len(paths) > 1
        first_path_for_check = paths[0] if not is_multi else None
        is_dir = os.path.isdir(first_path_for_check) if first_path_for_check else False

        if is_multi:
            target_dir_for_paste = os.path.dirname(paths[0])
        else:
            target_dir_for_paste = paths[0] if is_dir else os.path.dirname(paths[0])

        populate_project_context_menu(
            self, menu, paths=paths, is_dir=is_dir,
            project_manager=self.project_manager,
            target_dir_for_paste=target_dir_for_paste
        )

        if menu.actions():
            menu.exec(global_pos)
