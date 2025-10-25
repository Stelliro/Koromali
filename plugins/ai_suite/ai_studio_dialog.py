# /plugins/ai_suite/ai_studio_dialog.py
from __future__ import annotations

import os
import json
import difflib
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Iterator, TYPE_CHECKING

from PyQt6.QtCore import (
    Qt,
    QSortFilterProxyModel,
    QModelIndex,
    QThreadPool,
    QItemSelectionModel,
    pyqtSignal,
)
from PyQt6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QFileSystemModel,
    QFont,
    QBrush,
    QColor,
)
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QSplitter, QWidget, QGroupBox,
    QTreeView, QTextEdit, QPushButton, QDialogButtonBox, QMessageBox,
    QComboBox, QLabel, QFileDialog,
    QStatusBar, QTabWidget, QFormLayout, QHeaderView, QApplication,
    QAbstractItemView
)

if TYPE_CHECKING:
    from app_core.koromali_api import KoromaliPluginAPI

import qtawesome as qta


try:
    from utils.logger import log
    from utils.helpers import human_readable_size
except Exception:  # pragma: no cover
    class _L:
        def info(self, *a, **k): print("[INFO]", *a)
        def warning(self, *a, **k): print("[WARN]", *a)
        def error(self, *a, **k): print("[ERROR]", *a)
    log = _L()
    def human_readable_size(n: int) -> str: return f"{n} B"


from .api_client import ApiClient
from .style_preset_manager import StylePresetManager
from .persona_manager import PersonaManager
from .token_cache import TokenCache
from .workers import TokenCountWorker
from .persona_logic import get_files_for_persona
from .response_parser import parse_llm_response
from .diff_preview_dialog import DiffPreviewDialog


EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'ai_exports', 'node_modules', 'dist', 'build'}

TRISTATE_FLAG = getattr(
    Qt.ItemFlag,
    "ItemIsTristate",
    getattr(Qt.ItemFlag, "ItemIsAutoTristate", None),
)


CHECK_STATE_TOOLTIPS = {
    Qt.CheckState.Unchecked: "Not included in the current request.",
    Qt.CheckState.Checked: "Included in the current request.",
    Qt.CheckState.PartiallyChecked: (
        "Partially included – some child items are selected."
    ),
}

_BOLD_FONT = QFont()
_BOLD_FONT.setBold(True)

CHECK_STATE_BACKGROUNDS = {
    Qt.CheckState.Checked: QBrush(QColor(76, 175, 80, 45)),
    Qt.CheckState.PartiallyChecked: QBrush(QColor(255, 193, 7, 45)),
}


class CheckableFileSystemModel(QFileSystemModel):
    """A file system model that keeps track of per-path check states."""

    checkStateChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._check_states: Dict[str, Qt.CheckState] = {}
        self._checked_files: set[str] = set()
        self.directoryLoaded.connect(self._on_directory_loaded)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        flags = super().flags(index) | Qt.ItemFlag.ItemIsUserCheckable
        if self.isDir(index) and TRISTATE_FLAG is not None:
            flags |= TRISTATE_FLAG
        return flags

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return super().data(index, role)

        path = self.filePath(index)
        state = self._check_states.get(path, Qt.CheckState.Unchecked)

        if role == Qt.ItemDataRole.CheckStateRole:
            return state

        if role == Qt.ItemDataRole.FontRole and state == Qt.CheckState.Checked:
            return _BOLD_FONT

        if role == Qt.ItemDataRole.BackgroundRole and state in CHECK_STATE_BACKGROUNDS:
            return CHECK_STATE_BACKGROUNDS[state]

        if role == Qt.ItemDataRole.ToolTipRole:
            return CHECK_STATE_TOOLTIPS.get(state)

        return super().data(index, role)

    def setData(self, index: QModelIndex, value, role: int = Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.CheckStateRole:
            state = Qt.CheckState(value)
            if self._update_index_state(index, state):
                self.checkStateChanged.emit()
            return True
        return super().setData(index, value, role)

    def clear_checks(self):
        if not self._check_states and not self._checked_files:
            return
        self._check_states.clear()
        self._checked_files.clear()
        root_index = self.index(self.rootPath())
        if root_index.isValid():
            self.dataChanged.emit(root_index, root_index)
        self.checkStateChanged.emit()

    def get_checked_files(self) -> List[str]:
        return sorted(self._checked_files)

    def get_check_state(self, index: QModelIndex) -> Qt.CheckState:
        return self._check_states.get(self.filePath(index), Qt.CheckState.Unchecked)

    def set_path_state(
        self, path: str, state: Qt.CheckState, emit_signal: bool = True
    ) -> bool:
        index = self.index(path)
        if not index.isValid():
            return False
        changed = self._update_index_state(index, state)
        if changed and emit_signal:
            self.checkStateChanged.emit()
        return changed

    def set_all_under_path(self, path: str, state: Qt.CheckState):
        index = self.index(path)
        if not index.isValid():
            return
        if self._update_index_state(index, state):
            self.checkStateChanged.emit()

    def toggle_path(self, path: str):
        index = self.index(path)
        if not index.isValid():
            return
        current = self.get_check_state(index)
        new_state = (
            Qt.CheckState.Unchecked
            if current == Qt.CheckState.Checked
            else Qt.CheckState.Checked
        )
        if self._update_index_state(index, new_state):
            self.checkStateChanged.emit()

    def _update_index_state(self, index: QModelIndex, state: Qt.CheckState) -> bool:
        if not index.isValid():
            return False

        changed = self._apply_state(index, state)
        parent_changed = self._update_parent_state(index.parent())
        return changed or parent_changed

    def _apply_state(self, index: QModelIndex, state: Qt.CheckState) -> bool:
        path = self.filePath(index)
        previous = self._check_states.get(path, Qt.CheckState.Unchecked)
        changed = previous != state
        self._check_states[path] = state

        if self.isDir(index):
            self._checked_files.discard(path)
            self.dataChanged.emit(index, index)
            for row in range(self.rowCount(index)):
                child = self.index(row, 0, index)
                changed = self._apply_state(child, state) or changed
        else:
            if state == Qt.CheckState.Checked:
                if path not in self._checked_files:
                    changed = True
                self._checked_files.add(path)
            else:
                if path in self._checked_files:
                    changed = True
                self._checked_files.discard(path)
            self.dataChanged.emit(index, index)

        return changed

    def _update_parent_state(self, parent_index: QModelIndex) -> bool:
        changed = False
        while parent_index.isValid():
            path = self.filePath(parent_index)
            child_states = []
            for row in range(self.rowCount(parent_index)):
                child = self.index(row, 0, parent_index)
                child_state = self._check_states.get(
                    self.filePath(child), Qt.CheckState.Unchecked
                )
                child_states.append(child_state)

            if child_states:
                if all(state == Qt.CheckState.Checked for state in child_states):
                    new_state = Qt.CheckState.Checked
                elif all(state == Qt.CheckState.Unchecked for state in child_states):
                    new_state = Qt.CheckState.Unchecked
                else:
                    new_state = Qt.CheckState.PartiallyChecked
            else:
                new_state = self._check_states.get(path, Qt.CheckState.Unchecked)

            previous = self._check_states.get(path, Qt.CheckState.Unchecked)
            if previous != new_state:
                self._check_states[path] = new_state
                changed = True
                self.dataChanged.emit(parent_index, parent_index)

            parent_index = parent_index.parent()

        return changed

    def _on_directory_loaded(self, path: str):
        index = self.index(path)
        if not index.isValid():
            return

        parent_state = self._check_states.get(path, Qt.CheckState.Unchecked)
        if parent_state == Qt.CheckState.PartiallyChecked:
            return

        changed = False
        for row in range(self.rowCount(index)):
            child = self.index(row, 0, index)
            child_path = self.filePath(child)
            child_state = self._check_states.get(child_path, Qt.CheckState.Unchecked)
            if child_state != parent_state:
                changed = self._apply_state(child, parent_state) or changed

        if changed:
            self.checkStateChanged.emit()


class DirectoryFilterProxyModel(QSortFilterProxyModel):
    """A proxy model to filter out specific directories from a QFileSystemModel."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.exclude_dirs = EXCLUDE_DIRS

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        source_index = self.sourceModel().index(source_row, 0, source_parent)
        if not source_index.isValid():
            return True

        file_name = self.sourceModel().fileName(source_index)
        if file_name in self.exclude_dirs:
            return False
            
        return super().filterAcceptsRow(source_row, source_parent)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        """Ensure that every item passing the filter is selectable and enabled."""
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        # Get the flags from the original source model
        source_index = self.mapToSource(index)
        source_flags = self.sourceModel().flags(source_index)

        # Ensure the item is always enabled and selectable
        return source_flags | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable


class AIStudioDialog(QDialog):
    """A comprehensive dialog for interacting with AI models."""

    def __init__(self, api: "KoromaliPluginAPI", parent=None):
        super().__init__(parent)
        self.api = api
        self.main_window = api.get_main_window()
        self.project_root: Optional[str] = None
        self.response_changes: List[Dict] = []
        self.token_cache: Optional[TokenCache] = None
        self.thread_pool = QThreadPool()
        
        self.persona_manager = PersonaManager()
        self.style_manager = StylePresetManager()

        self.setWindowTitle("AI Studio")
        self.setMinimumSize(1200, 800)

        main_layout = QVBoxLayout(self)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter, 1)

        splitter.addWidget(self._create_left_panel())
        splitter.addWidget(self._create_right_panel())

        self.status_bar = QStatusBar()
        main_layout.addWidget(self.status_bar)

        splitter.setSizes([400, 800])
        self._populate_personas()
        self._populate_styles()
        self._populate_projects()
        self._update_ui_state()

    def _create_left_panel(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        project_group = QGroupBox("1. Select Project")
        project_layout = QFormLayout(project_group)
        self.project_selector = QComboBox()
        project_layout.addRow("Active Project:", self.project_selector)
        layout.addWidget(project_group)

        context_group = QGroupBox("2. Select Context Files")
        context_layout = QVBoxLayout(context_group)
        
        # --- Selection & View Buttons ---
        view_bar = QHBoxLayout()
        expand_all_btn = QPushButton("Expand All")
        collapse_all_btn = QPushButton("Collapse All")
        view_bar.addWidget(expand_all_btn)
        view_bar.addWidget(collapse_all_btn)
        view_bar.addStretch()
        context_layout.addLayout(view_bar)
        
        selection_bar = QHBoxLayout()
        select_all_btn = QPushButton("Select All")
        select_none_btn = QPushButton("Select None")
        invert_selection_btn = QPushButton("Invert Selection")
        selection_bar.addWidget(select_all_btn)
        selection_bar.addWidget(select_none_btn)
        selection_bar.addWidget(invert_selection_btn)
        context_layout.addLayout(selection_bar)
        
        # --- File Tree ---
        self.file_tree = QTreeView()
        self.file_tree.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.file_model = CheckableFileSystemModel()
        self.file_model.setRootPath("")
        self.proxy_model = DirectoryFilterProxyModel()
        self.proxy_model.setSourceModel(self.file_model)
        self.file_tree.setModel(self.proxy_model)
        self.file_tree.setHeaderHidden(True)
        for i in range(1, self.file_model.columnCount()):
            self.file_tree.hideColumn(i)
        context_layout.addWidget(self.file_tree)

        # --- Selection Info Label ---
        self.selection_info_label = QLabel("Selected: 0 files (0 tokens)")
        context_layout.addWidget(self.selection_info_label)
        
        layout.addWidget(context_group, 1)

        # --- Connections ---
        self.project_selector.currentIndexChanged.connect(self._on_project_changed)
        select_all_btn.clicked.connect(self._select_all)
        select_none_btn.clicked.connect(self._deselect_all)
        invert_selection_btn.clicked.connect(self._invert_selection)
        expand_all_btn.clicked.connect(self._expand_all)
        collapse_all_btn.clicked.connect(self._collapse_all)
        self.file_model.checkStateChanged.connect(self._update_selection_info)

        return widget

    def _create_right_panel(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.tabs = QTabWidget()
        self.tabs.addTab(self._create_prompt_tab(), "1. Prompt")
        self.tabs.addTab(self._create_response_tab(), "2. Response")
        layout.addWidget(self.tabs)
        return widget

    def _create_prompt_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        config_group = QGroupBox("3. Define Task")
        config_layout = QVBoxLayout(config_group)
        
        persona_layout = QHBoxLayout()
        self.persona_selector = QComboBox()
        self.recommend_files_btn = QPushButton(qta.icon('fa5s.lightbulb'), "Recommend Files")
        persona_layout.addWidget(QLabel("Persona:"))
        persona_layout.addWidget(self.persona_selector, 1)
        persona_layout.addWidget(self.recommend_files_btn)
        
        style_layout = QHBoxLayout()
        self.style_selector = QComboBox()
        style_layout.addWidget(QLabel("Style:"))
        style_layout.addWidget(self.style_selector, 1)

        config_layout.addLayout(persona_layout)
        config_layout.addLayout(style_layout)

        self.prompt_edit = QTextEdit()
        self.prompt_edit.setPlaceholderText("Enter your instructions for the AI...")
        config_layout.addWidget(self.prompt_edit, 1)

        self.send_button = QPushButton(qta.icon('fa5s.paper-plane'), "Send to AI")
        config_layout.addWidget(self.send_button)
        layout.addWidget(config_group)

        self.send_button.clicked.connect(self._send_to_ai)
        self.recommend_files_btn.clicked.connect(self._apply_persona_selection)
        return widget

    def _create_response_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        splitter = QSplitter(Qt.Orientation.Vertical)
        layout.addWidget(splitter)
        
        response_input_group = QGroupBox("4. Paste AI Response")
        response_input_layout = QVBoxLayout(response_input_group)
        self.response_text_edit = QTextEdit()
        self.response_text_edit.setPlaceholderText("Paste the full response from your AI model here...")
        response_input_layout.addWidget(self.response_text_edit)
        parse_button = QPushButton(qta.icon('fa5s.cogs'), "Parse Response")
        parse_button.clicked.connect(self._parse_manual_response)
        response_input_layout.addWidget(parse_button)
        splitter.addWidget(response_input_group)
        
        changes_group = QGroupBox("5. Review & Apply Changes")
        changes_layout = QVBoxLayout(changes_group)
        self.response_tree = QTreeView()
        self.response_model = QStandardItemModel()
        self.response_model.setHorizontalHeaderLabels(['File', 'Change', 'Status'])
        self.response_tree.setModel(self.response_model)
        self.response_tree.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.response_tree.header().setStretchLastSection(True)
        changes_layout.addWidget(self.response_tree)
        self.apply_button = QPushButton(qta.icon('fa5s.check'), "Preview & Apply Patch...")
        changes_layout.addWidget(self.apply_button)
        self.apply_button.clicked.connect(self._preview_and_apply_change)
        self.response_tree.selectionModel().selectionChanged.connect(self._update_ui_state)
        splitter.addWidget(changes_group)
        splitter.setSizes([200, 400])
        return widget

    def _populate_personas(self):
        self.persona_selector.clear()
        personas = self.persona_manager.get_personas()
        if not personas:
            self.persona_selector.addItem("No Personas Found", userData=None)
            self.persona_selector.setEnabled(False)
        else:
            for persona in personas:
                self.persona_selector.addItem(f"{persona['name']}", userData=persona['id'])
            self.persona_selector.setEnabled(True)

    def _populate_styles(self):
        self.style_selector.clear()
        styles = self.style_manager.list_presets()
        for style_name in styles:
            self.style_selector.addItem(style_name)

    def _populate_projects(self):
        self.project_selector.clear()
        try:
            projects = self.main_window.project_manager.get_open_projects()
        except AttributeError:
            log.error("Could not access project_manager on the main window.")
            projects = []
        for path in projects:
            self.project_selector.addItem(os.path.basename(path), userData=path)
        if not projects:
            self.status_bar.showMessage("No open projects found.")
        self._on_project_changed(0)
        self._update_ui_state()

    def _on_project_changed(self, index: int):
        path = self.project_selector.itemData(index)
        if path and os.path.isdir(path):
            self.project_root = path
            self.token_cache = TokenCache(path)
            source_index = self.file_model.setRootPath(path)
            self.file_model.clear_checks()
            proxy_index = self.proxy_model.mapFromSource(source_index)
            self.file_tree.setRootIndex(proxy_index)
        else:
            self.project_root = None
            self.token_cache = None
            self.file_model.setRootPath("")
            self.file_model.clear_checks()
            self.status_bar.showMessage("Please select a valid project.")
        self._update_ui_state()

    def _get_selected_file_paths(self) -> List[str]:
        if not self.project_root:
            return []
        return self.file_model.get_checked_files()

    def _update_selection_info(self):
        selected_files = self._get_selected_file_paths()
        count = len(selected_files)
        if count == 0:
            self.selection_info_label.setText("Selected: 0 files (0 tokens)")
            return
        
        self.selection_info_label.setText(f"Selected: {count} files (Calculating tokens...)")
        if self.project_root and self.token_cache:
            worker = TokenCountWorker(self.project_root, selected_files, self.token_cache)
            worker.signals.finished.connect(self._on_token_count_finished)
            self.thread_pool.start(worker)

    def _on_token_count_finished(self, success: bool, counts: Dict[str, int]):
        if success:
            total_tokens = sum(counts.values())
            file_count = len(self._get_selected_file_paths())
            self.selection_info_label.setText(f"Selected: {file_count} files ({total_tokens:,} tokens)")

    def _expand_all(self):
        self.file_tree.expandAll()

    def _collapse_all(self):
        self.file_tree.collapseAll()

    def _select_all(self):
        if not self.project_root:
            return
        self.file_tree.expandAll()
        self.file_model.set_all_under_path(self.project_root, Qt.CheckState.Checked)
        self.file_tree.selectAll()

    def _deselect_all(self):
        if not self.project_root:
            return
        self.file_model.set_all_under_path(self.project_root, Qt.CheckState.Unchecked)
        self.file_tree.clearSelection()

    def _invert_selection(self):
        if not self.project_root:
            return

        self.file_tree.expandAll()

        to_toggle: List[str] = []

        def recurse(parent_index: QModelIndex):
            for row in range(self.proxy_model.rowCount(parent_index)):
                proxy_index = self.proxy_model.index(row, 0, parent_index)
                source_index = self.proxy_model.mapToSource(proxy_index)
                if not source_index.isValid():
                    continue
                if self.file_model.isDir(source_index):
                    recurse(proxy_index)
                else:
                    to_toggle.append(self.file_model.filePath(source_index))

        recurse(self.file_tree.rootIndex())

        if not to_toggle:
            return

        changed = False
        for path in to_toggle:
            current_index = self.file_model.index(path)
            current_state = self.file_model.get_check_state(current_index)
            new_state = (
                Qt.CheckState.Unchecked
                if current_state == Qt.CheckState.Checked
                else Qt.CheckState.Checked
            )
            changed = (
                self.file_model.set_path_state(path, new_state, emit_signal=False)
                or changed
            )

        if changed:
            self.file_model.checkStateChanged.emit()

    def _apply_persona_selection(self):
        persona_id = self.persona_selector.currentData()
        if not persona_id or not self.project_root:
            return
            
        recommended_files = get_files_for_persona(persona_id, self.project_root)
        if recommended_files is None:
            QMessageBox.information(self, "Persona Suggestion", "This persona has no specific file recommendations. Consider selecting all files.")
            return

        self.file_tree.expandAll()
        self.file_model.set_all_under_path(self.project_root, Qt.CheckState.Unchecked)
        QApplication.processEvents() # Allow UI to update

        selection_model = self.file_tree.selectionModel()
        selection_model.clearSelection()

        first_index = None
        changed = False
        for file_path in recommended_files:
            changed = (
                self.file_model.set_path_state(
                    file_path, Qt.CheckState.Checked, emit_signal=False
                )
                or changed
            )
            source_index = self.file_model.index(file_path)
            if source_index.isValid():
                proxy_index = self.proxy_model.mapFromSource(source_index)
                if proxy_index.isValid():
                    if first_index is None:
                        first_index = proxy_index
                    selection_model.select(
                        proxy_index,
                        QItemSelectionModel.SelectionFlag.Select
                        | QItemSelectionModel.SelectionFlag.Rows,
                    )

        if changed:
            self.file_model.checkStateChanged.emit()

        if first_index:
            self.file_tree.scrollTo(first_index, QAbstractItemView.ScrollHint.PositionAtTop)


        log.info(f"Applied file selection for persona '{persona_id}'.")


    def _send_to_ai(self):
        self.status_bar.showMessage("Sending request to AI...")
        QApplication.processEvents()
        response_text = self._get_mock_response()
        self.response_text_edit.setPlainText(response_text)
        self._parse_manual_response()
        self.tabs.setCurrentIndex(1)

    def _parse_manual_response(self):
        response_text = self.response_text_edit.toPlainText()
        if not response_text:
            QMessageBox.warning(self, "Empty Response", "There is no response text to parse.")
            return

        self.response_model.clear()
        self.response_model.setHorizontalHeaderLabels(['File', 'Change', 'Status'])
        if not self.project_root: 
            QMessageBox.critical(self, "No Project", "A project must be selected before parsing a response.")
            return
        
        try:
            self.response_changes = parse_llm_response(response_text, self.project_root)
        except Exception as e:
            QMessageBox.critical(self, "Parsing Error", f"Failed to parse AI response:\n{e}")
            self.response_changes = []
            return

        for change in self.response_changes:
            path_item = QStandardItem(change.get('file_path', 'N/A'))
            path_item.setData(change, Qt.ItemDataRole.UserRole)
            type_item = QStandardItem(change.get('type', 'N/A'))
            status_item = QStandardItem("Pending")
            self.response_model.appendRow([path_item, type_item, status_item])
        
        self.status_bar.showMessage(f"Parsed {len(self.response_changes)} proposed changes.")
        self._update_ui_state()


    def _preview_and_apply_change(self):
        indexes = self.response_tree.selectionModel().selectedIndexes()
        if not indexes: return

        item = self.response_model.itemFromIndex(indexes[0])
        change = item.data(Qt.ItemDataRole.UserRole)
        
        if change.get("type") == "APPLY_PATCH":
            self._show_diff_preview(change)
        else:
            QMessageBox.information(self, "Not Implemented", f"Preview for '{change.get('type')}' is not implemented.")

    def _show_diff_preview(self, change: Dict):
        if not self.project_root: return
        
        file_path = os.path.join(self.project_root, change['file_path'])
        patch_content = change['content']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except FileNotFoundError:
            original_content = ""

        dialog = DiffPreviewDialog(file_path, original_content, patch_content, self)
        if dialog.exec():
            self.status_bar.showMessage(f"Successfully applied patch to {change['file_path']}.")
            for row in range(self.response_model.rowCount()):
                item = self.response_model.item(row, 0)
                if item and item.data(Qt.ItemDataRole.UserRole) == change:
                    self.response_model.item(row, 2).setText("Applied")
                    break
        else:
            self.status_bar.showMessage(f"Patch for {change['file_path']} was cancelled.")

    def _update_ui_state(self):
        has_project = self.project_root is not None
        self.send_button.setEnabled(has_project)
        self.recommend_files_btn.setEnabled(has_project and self.persona_selector.count() > 0)
        has_selection = bool(self.response_tree.selectionModel().selectedIndexes())
        self.apply_button.setEnabled(has_selection)

    def _get_mock_response(self) -> str:
        if not self.project_root:
            return ""
        target_file = "plugins/ai_suite/plugin.json"
        full_path = os.path.join(self.project_root, target_file)
        if not os.path.exists(full_path):
            return "Mock response needs plugins/ai_suite/plugin.json to exist."

        lines = [
            "I have reviewed the project and suggest an update to the version number.",
            "", "```patch", f"--- a/{target_file}", f"+++ b/{target_file}",
            "@@ -3,7 +3,7 @@", '     "id": "ai_suite",', '     "name": "AI Suite",',
            '     "author": "Koromali Team",', '-    "version": "2.3.0",',
            '+    "version": "2.4.0-updated",',
            '     "description": "A unified suite for AI-assisted development, including context export, response parsing, and interactive patching.",',
            '     "entry_point": "plugin_main.py"', ' }', "```",
            "This version bump reflects the recent architectural changes."
        ]
        return "\n".join(lines)