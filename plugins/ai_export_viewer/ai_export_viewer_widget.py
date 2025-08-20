# Koromali/plugins/ai_export_viewer/ai_export_viewer_widget.py
import os
import re
from functools import partial
from typing import TYPE_CHECKING, List, Dict, Any
from datetime import datetime
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QTextEdit, QPushButton, QMessageBox, QSplitter, QFrame, QTreeView,
    QApplication, QGroupBox, QToolButton, QMenu, QScrollBar
)
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem, QTextCursor, QTextDocument, QIcon, QAction
from PyQt6.QtCore import Qt, QPoint, QTimer, QModelIndex
from markdown import markdown
import qtawesome as qta
from utils.helpers import get_base_path
from utils.logger import log

if TYPE_CHECKING:
    from app_core.koromali_api import KoromaliPluginAPI
    from app_core.theme_manager import ThemeManager
    from app_core.settings_manager import SettingsManager

class AIExportViewerWidget(QWidget):
    """
    A widget that displays a list of past AI exports and their content,
    with a navigable minimap and copyable code blocks.
    """
    def __init__(self, api: "KoromaliPluginAPI", parent=None):
        super().__init__(parent)
        self.api = api
        self.theme_manager = api.get_manager("theme")
        self.settings_manager = api.get_manager("settings")
        self.export_dir = os.path.join(get_base_path(), "ai_exports")
        self.document_structure: List[Dict[str, Any]] = []
        self.copy_buttons: List[QPushButton] = []
        self._ensure_export_dir_exists()
        self.setObjectName("AIExportViewerWidget")

        self.reposition_timer = QTimer(self)
        self.reposition_timer.setSingleShot(True)
        self.reposition_timer.setInterval(50)
        self.reposition_timer.timeout.connect(self._update_copy_button_positions)

        self._setup_ui()
        self._connect_signals()
        self.update_theme()
        self.refresh_list()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        toolbar = QFrame()
        toolbar.setObjectName("ExportViewerToolbar")
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(5, 5, 5, 5)
        self.refresh_button = QPushButton(qta.icon('fa5s.sync-alt'), "Refresh")
        self.delete_button = QPushButton(qta.icon('fa5s.trash-alt'), "Delete")
        toolbar_layout.addWidget(self.refresh_button)
        toolbar_layout.addWidget(self.delete_button)
        toolbar_layout.addStretch()
        main_layout.addWidget(toolbar)

        top_splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(top_splitter, 1)

        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        self.export_list_widget = QListWidget()
        self.export_list_widget.setAlternatingRowColors(True)
        left_layout.addWidget(self.export_list_widget)
        top_splitter.addWidget(left_widget)

        right_pane = QWidget()
        right_layout = QVBoxLayout(right_pane)
        right_layout.setContentsMargins(0, 0, 0, 0)
        content_splitter = QSplitter(Qt.Orientation.Horizontal)
        right_layout.addWidget(content_splitter)
        right_pane.setLayout(right_layout)
        top_splitter.addWidget(right_pane)

        guide_pane = QGroupBox("Project Export Viewer")
        guide_layout = QVBoxLayout(guide_pane)
        guide_toolbar_layout = QHBoxLayout()
        guide_toolbar_layout.addStretch()
        self.expand_all_btn = QToolButton()
        self.expand_all_btn.setIcon(qta.icon('fa5s.angle-double-down', color='grey'))
        self.expand_all_btn.setToolTip("Expand All")
        self.expand_all_btn.setAutoRaise(True)
        self.collapse_all_btn = QToolButton()
        self.collapse_all_btn.setIcon(qta.icon('fa5s.angle-double-up', color='grey'))
        self.collapse_all_btn.setToolTip("Collapse All")
        self.collapse_all_btn.setAutoRaise(True)
        guide_toolbar_layout.addWidget(self.expand_all_btn)
        guide_toolbar_layout.addWidget(self.collapse_all_btn)
        guide_layout.addLayout(guide_toolbar_layout)
        self.minimap_tree = QTreeView()
        self.minimap_tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.minimap_tree.setHeaderHidden(True)
        self.minimap_model = QStandardItemModel()
        self.minimap_tree.setModel(self.minimap_model)
        guide_layout.addWidget(self.minimap_tree)
        content_splitter.addWidget(guide_pane)

        # Content view area with manual scrollbar
        content_area_widget = QWidget()
        content_area_layout = QHBoxLayout(content_area_widget)
        content_area_layout.setContentsMargins(0,0,0,0)
        content_area_layout.setSpacing(0)
        
        self.content_view = QTextEdit()
        self.content_view.setReadOnly(True)
        self.content_view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # Turn off internal scrollbar
        self.content_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.v_scrollbar = QScrollBar(Qt.Orientation.Vertical)
        
        content_area_layout.addWidget(self.content_view)
        content_area_layout.addWidget(self.v_scrollbar)
        content_splitter.addWidget(content_area_widget)
        
        content_splitter.setSizes([220, 580])
        top_splitter.setSizes([250, 800])

    def _connect_signals(self):
        self.export_list_widget.currentItemChanged.connect(self._on_export_selected)
        self.refresh_button.clicked.connect(self.refresh_list)
        self.delete_button.clicked.connect(self._delete_selected_export)
        self.minimap_tree.customContextMenuRequested.connect(self._show_minimap_context_menu)
        self.minimap_tree.clicked.connect(self._on_minimap_item_clicked)
        self.minimap_tree.doubleClicked.connect(self._on_minimap_item_double_clicked)
        self.expand_all_btn.clicked.connect(self.minimap_tree.expandAll)
        self.collapse_all_btn.clicked.connect(self.minimap_tree.collapseAll)
        
        # Connect our custom scrollbar
        self.v_scrollbar.valueChanged.connect(self.content_view.verticalScrollBar().setValue)
        self.content_view.verticalScrollBar().rangeChanged.connect(self.v_scrollbar.setRange)
        self.content_view.verticalScrollBar().valueChanged.connect(self.v_scrollbar.setValue)
        self.content_view.verticalScrollBar().valueChanged.connect(self.reposition_timer.start)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.reposition_timer.start()

    def _ensure_export_dir_exists(self):
        try:
            os.makedirs(self.export_dir, exist_ok=True)
        except OSError as e:
            log.error(f"Could not create export directory: {e}", exc_info=True)

    def refresh_list(self):
        self.export_list_widget.clear()
        self.content_view.clear()
        self.delete_button.setEnabled(False)
        self.minimap_model.clear()
        all_files = []
        try:
            if os.path.isdir(self.export_dir):
                for root, _, files in os.walk(self.export_dir):
                    for filename in files:
                        if filename.endswith('.md'):
                            path = os.path.join(root, filename)
                            display_name = os.path.relpath(path, self.export_dir).replace(os.sep, '/')
                            all_files.append((path, display_name))
            all_files.sort(key=lambda x: os.path.getmtime(x[0]), reverse=True)
            if not all_files:
                self.export_list_widget.addItem("No exports found.")
                self.export_list_widget.setEnabled(False)
                return
            self.export_list_widget.setEnabled(True)
            for path, display_name in all_files:
                item = QListWidgetItem(display_name)
                item.setData(Qt.ItemDataRole.UserRole, path)
                self.export_list_widget.addItem(item)
            if self.export_list_widget.count() > 0:
                self.export_list_widget.setCurrentRow(0)
        except OSError as e:
            log.error(f"Error reading export directory {self.export_dir}: {e}")
            self.export_list_widget.addItem("Error reading directory.")
            self.export_list_widget.setEnabled(False)

    def _clear_copy_buttons(self):
        for button in self.copy_buttons:
            button.deleteLater()
        self.copy_buttons.clear()

    def _reformat_timestamp_in_content(self, content: str) -> str:
        match = re.search(r"^(.*Timestamp: )(.+?)$", content, re.MULTILINE)
        if not match: return content
        original_line, prefix, iso_timestamp_str = match.group(0), match.group(1), match.group(2).strip()
        iso_timestamp_str = iso_timestamp_str.strip('}", ')
        try:
            dt_object = datetime.fromisoformat(iso_timestamp_str)
            formatted_timestamp = dt_object.strftime("%I:%M:%S %p on %A, %B %d, %Y")
            new_line = f"{prefix}{formatted_timestamp}"
            return content.replace(original_line, new_line)
        except (ValueError, TypeError) as e:
            log.warning(f"Could not parse timestamp '{iso_timestamp_str}': {e}")
            return content

    def _on_export_selected(self, current: QListWidgetItem, _):
        self.minimap_model.clear()
        self.document_structure.clear()
        self._clear_copy_buttons()
        if not current or not current.data(Qt.ItemDataRole.UserRole):
            self.content_view.clear()
            self.delete_button.setEnabled(False)
            return
        self.delete_button.setEnabled(True)
        filepath = current.data(Qt.ItemDataRole.UserRole)
        try:
            with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
            content = self._reformat_timestamp_in_content(content)
            self._parse_and_populate_structure(content)
            html = markdown(content, extensions=['fenced_code', 'tables', 'extra', 'sane_lists'])
            self.content_view.setHtml(html)
            QTimer.singleShot(100, self._map_structure_to_document)
        except Exception as e:
            error_message = f"Error reading file:\n{filepath}\n\n{str(e)}"
            self.content_view.setText(error_message)
            log.error(f"Failed to read export file {filepath}: {e}", exc_info=True)

    def _parse_and_populate_structure(self, content: str):
        self.minimap_model.clear()
        self.document_structure.clear()
        file_pattern = re.compile(r"(### File: `.*?`.*?)(?=### File: `|\Z)", re.DOTALL)
        code_pattern = re.compile(r"```(?:\w*\n)?(.*?)```", re.DOTALL)
        user_prompt_match = re.search(r"---USER-PROMPT---(.*)", content, re.DOTALL)
        if not user_prompt_match: return
        user_prompt_content = user_prompt_match.group(1)
        root_item = self.minimap_model.invisibleRootItem()
        path_map = {"/": root_item}
        for match in file_pattern.finditer(user_prompt_content):
            file_section = match.group(1)
            header_match = re.search(r"### File: `(/.*?)`", file_section)
            if header_match:
                full_path = header_match.group(1)
                if "relative_path" in full_path:
                    log.warning(f"Skipping malformed path in export file: {full_path}")
                    continue
                all_code_blocks = code_pattern.finditer(file_section)
                full_script_content = "\n\n".join(block.group(1).strip() for block in all_code_blocks)
                if not full_script_content: continue
                struct_item_index = len(self.document_structure)
                self.document_structure.append({"header": full_path, "type": "file", "content": full_script_content, "cursor": None})
                parts = full_path.strip('/').split('/')
                current_path_key = ""
                parent_item = root_item
                for part in parts[:-1]:
                    current_path_key += "/" + part
                    if current_path_key not in path_map:
                        dir_item = QStandardItem(part)
                        dir_item.setEditable(False)
                        dir_item.setIcon(qta.icon('fa5.folder', color='grey'))
                        parent_item.appendRow(dir_item)
                        path_map[current_path_key] = dir_item
                        parent_item = dir_item
                    else:
                        parent_item = path_map[current_path_key]
                file_item = QStandardItem(parts[-1])
                file_item.setEditable(False)
                file_item.setIcon(qta.icon('fa5.file-alt', color='grey'))
                file_item.setData(struct_item_index, Qt.ItemDataRole.UserRole)
                parent_item.appendRow(file_item)
        self.minimap_tree.collapseAll()
        if root_item.rowCount() > 0:
            self.minimap_tree.expand(self.minimap_model.index(0, 0))

    def _map_structure_to_document(self):
        doc = self.content_view.document()
        search_cursor = QTextCursor(doc)
        search_cursor.movePosition(QTextCursor.MoveOperation.Start)
        for item in self.document_structure:
            search_text = f"File: {item['header']}"
            cursor = doc.find(search_text, search_cursor)
            if not cursor.isNull():
                item['cursor'] = cursor
                search_cursor = cursor
            else:
                log.warning(f"Could not map document location for header: {item['header']}")
        self._update_copy_button_positions()

    def _update_copy_button_positions(self):
        self._clear_copy_buttons()
        for item in self.document_structure:
            if item.get('type') == 'file' and item.get('cursor') and item.get('content'):
                cursor = item['cursor']
                code_block_start_cursor = self.content_view.document().find("```", cursor)
                if not code_block_start_cursor.isNull():
                    rect = self.content_view.cursorRect(code_block_start_cursor)
                    btn = QPushButton(qta.icon('fa5s.copy'), "Copy", self.content_view)
                    btn.setCursor(Qt.CursorShape.PointingHandCursor)
                    btn.setStyleSheet("QPushButton { background-color: #555; border: 1px solid #777; border-radius: 3px; padding: 2px 5px; color: white; } QPushButton:hover { background-color: #666; }")
                    x_pos = self.content_view.viewport().width() - btn.sizeHint().width() - 15
                    y_pos = rect.top() + 5
                    btn.move(x_pos, y_pos)
                    btn.clicked.connect(partial(self._on_copy_button_clicked, item['content']))
                    btn.show()
                    self.copy_buttons.append(btn)

    def _on_minimap_item_clicked(self, index: QModelIndex):
        if self.minimap_model.hasChildren(index):
            self.minimap_tree.setExpanded(index, not self.minimap_tree.isExpanded(index))

    def _on_minimap_item_double_clicked(self, index: QModelIndex):
        if self.minimap_model.hasChildren(index): return
        model_item = self.minimap_model.itemFromIndex(index)
        if not model_item: return
        struct_index = model_item.data(Qt.ItemDataRole.UserRole)
        if struct_index is not None:
            struct_item = self.document_structure[struct_index]
            if struct_item.get('cursor'):
                self.content_view.setTextCursor(struct_item['cursor'])
                self.content_view.ensureCursorVisible()

    def _show_minimap_context_menu(self, point: QPoint):
        index = self.minimap_tree.indexAt(point)
        if not index.isValid(): return
        model_item = self.minimap_model.itemFromIndex(index)
        if not model_item or self.minimap_model.hasChildren(index): return
        struct_index = model_item.data(Qt.ItemDataRole.UserRole)
        if struct_index is None: return
        script_content = self.document_structure[struct_index]['content']
        menu = QMenu(self.minimap_tree)
        copy_action = QAction(qta.icon('fa5s.copy'), "Copy Script", menu)
        copy_action.triggered.connect(lambda: self._copy_script_to_clipboard(script_content))
        menu.addAction(copy_action)
        menu.exec(self.minimap_tree.viewport().mapToGlobal(point))

    def _copy_script_to_clipboard(self, script_content: str):
        QApplication.clipboard().setText(script_content)
        log.info(f"Copied script to clipboard ({len(script_content)} characters).")

    def _on_copy_button_clicked(self, code_to_copy):
        self._copy_script_to_clipboard(code_to_copy)
        sender = self.sender()
        if isinstance(sender, QPushButton):
            original_text = sender.text()
            sender.setText("Copied!")
            QTimer.singleShot(1500, lambda: sender.setText(original_text))

    def _delete_selected_export(self):
        current_item = self.export_list_widget.currentItem()
        if not current_item: return
        filepath = current_item.data(Qt.ItemDataRole.UserRole)
        if not filepath: return
        filename = os.path.basename(filepath)
        reply = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to permanently delete this export?\n\n{filename}", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            try:
                os.remove(filepath)
                log.info(f"Deleted AI export file: {filepath}")
                self.refresh_list()
            except OSError as e:
                log.error(f"Failed to delete file {filepath}: {e}")
                QMessageBox.critical(self, "Deletion Failed", f"Could not delete file:\n{e}")

    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        font_family = self.settings_manager.get("font_family", "Consolas")
        font_size = self.settings_manager.get("font_size", 11)
        bg_color, fg_color = colors.get('editor.background', '#2b2b2b'), colors.get('editor.foreground', '#a9b7c6')
        accent, line_bg = colors.get('accent', '#88c0d0'), colors.get('editor.lineHighlightBackground', '#323232')
        comment, string = colors.get('syntax.comment', '#808080'), colors.get('syntax.string', '#6A8759')
        toolbar_bg, border = colors.get('sidebar.background', '#3c3f41'), colors.get('input.border', '#555')
        self.setStyleSheet(f"""QWidget {{ color: {fg_color}; }} AIExportViewerWidget {{ background-color: {bg_color}; }} #ExportViewerToolbar {{ background-color: {toolbar_bg}; border-bottom: 1px solid {border}; }} QListWidget, QTreeView {{ background-color: {bg_color}; border: none; }} QGroupBox {{ border: 1px solid {border}; margin-top: 10px; }} QGroupBox::title {{ subcontrol-origin: margin; subcontrol-position: top center; padding: 0 5px; }} QToolButton {{ margin: 1px; }}""")
        md_style = f"""h1,h2,h3,h4,h5,h6 {{ color:{accent}; border-bottom:1px solid {line_bg}; padding-bottom:4px; margin-top:15px; }} a {{ color:{string}; text-decoration:none; }} a:hover {{ text-decoration:underline; }} p,li {{ font-size:{font_size}pt; }} pre,code {{ display: block; background-color:{line_bg}; border:1px solid {border}; border-radius:4px; padding:10px; font-family:"{font_family}"; white-space: pre-wrap; }} code {{ padding:2px 4px; border:none; }} blockquote {{ color:{comment}; border-left:3px solid {accent}; padding-left:10px; margin-left:5px; }} table{{border-collapse:collapse;}} th,td{{border:1px solid {border}; padding:6px;}} th{{background-color:{line_bg};}}"""
        self.content_view.document().setDefaultStyleSheet(md_style)
        font = QFont(self.settings_manager.get("font_family", "Arial"), font_size)
        self.content_view.document().setDefaultFont(font)
        self.content_view.setStyleSheet(f"background-color: {bg_color}; border:none; padding:10px;")
        if item := self.export_list_widget.currentItem():
            self._on_export_selected(item, None)