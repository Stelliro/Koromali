# /plugins/ai_suite/ai_studio_dialog.py
from __future__ import annotations

import os
from typing import Dict, List, Optional, Set

from PyQt6.QtCore import (
    Qt,
    QSortFilterProxyModel,
    QModelIndex,
    pyqtSignal,
)
from PyQt6.QtGui import (
    QFileSystemModel,
    QFont,
    QBrush,
    QColor,
)
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QSplitter, QWidget, QGroupBox,
    QTreeView, QTextEdit, QPushButton, QMessageBox,
    QComboBox, QLabel, QFileDialog, QStatusBar, QTabWidget, 
    QFormLayout, QCheckBox, QApplication, QTreeWidget, QTreeWidgetItem, QHeaderView
)

try:
    import qtawesome as qta
except ImportError:
    qta = None

from app_core.koromali_api import KoromaliPluginAPI
from app_core import golden_rules
from utils.helpers import get_base_path

# --- CONSTANTS ---

EXCLUDE_DIRS = {
    '.git', '__pycache__', 'venv', '.venv', 'ai_exports', 'node_modules', 'dist', 'build', '.idea', '.vscode'
}

BINARY_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.tif', '.tiff', '.svg', '.webp',
    '.mp3', '.wav', '.flac', '.ogg', '.mp4', '.mov', '.avi', '.mkv',
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
    '.exe', '.dll', '.so', '.o', '.a', '.lib', '.dylib', '.app', '.msi', '.bin',
    '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.pyc'
}

TRISTATE = getattr(Qt.ItemFlag, "ItemIsTristate", getattr(Qt.ItemFlag, "ItemIsAutoTristate", None))
_BOLD_FONT = QFont()
_BOLD_FONT.setBold(True)
CHECK_BG = {
    Qt.CheckState.Checked: QBrush(QColor(76, 175, 80, 45)),
    Qt.CheckState.PartiallyChecked: QBrush(QColor(255, 193, 7, 45)),
}

# --- LOCAL SMART EXPORT LOGIC ---

def _is_path_checked(
    path: str,
    root_path: str,
    check_states: Dict[str, Qt.CheckState],
) -> bool:
    """Resolve check state with parent inheritance (handles lazy-loaded trees)."""
    norm_root = os.path.normpath(root_path)
    path = os.path.normpath(path)
    if path in check_states:
        return check_states[path] == Qt.CheckState.Checked
    parent = os.path.dirname(path)
    while len(parent) >= len(norm_root):
        if parent in check_states:
            state = check_states[parent]
            if state == Qt.CheckState.Checked:
                return True
            if state == Qt.CheckState.Unchecked:
                return False
            # PartiallyChecked: keep walking up; only explicit children count.
        if parent == norm_root:
            break
        next_parent = os.path.dirname(parent)
        if next_parent == parent:
            break
        parent = next_parent
    return False


def _build_export_preamble(project_name: str) -> str:
    """Instructions so a browser LLM returns machine-parsable patches/writes."""
    rules = golden_rules.get_rules_markdown()
    return "\n".join([
        f"# AI Export for Project: `{project_name}`",
        "",
        "You are assisting with this codebase. Read the project files below, then respond "
        "with **only** the file operations needed — no prose outside of the required blocks.",
        "",
        rules,
        "",
        "---",
        "",
        "## Project Files",
        "",
    ])


def _scan_and_generate_export(
    root_path: str,
    check_states: Dict[str, Qt.CheckState],
    include_logs: bool,
    *,
    include_instructions: bool = True,
) -> str:
    """
    Scans the disk directly to find files based on directory check states.
    This bypasses UI lazy-loading issues.
    """
    if not root_path or not os.path.isdir(root_path):
        return ""

    project_name = os.path.basename(os.path.normpath(root_path)) or "project"
    markdown_parts: List[str] = []
    if include_instructions:
        markdown_parts.append(_build_export_preamble(project_name))

    file_count = 0
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in sorted(files):
            abs_path = os.path.join(root, file)
            norm_path = os.path.normpath(abs_path)

            if not _is_path_checked(norm_path, root_path, check_states):
                continue

            rel_path = os.path.relpath(norm_path, root_path).replace(os.sep, '/')
            _, ext = os.path.splitext(rel_path)
            ext = ext.lower()

            if ext == '.log' and not include_logs:
                continue

            file_count += 1
            markdown_parts.append(f"### File: `/{rel_path}`")

            if ext in BINARY_EXTENSIONS:
                markdown_parts.append(f"> [Binary/Asset File] - Content omitted for {ext} file.\n")
                continue

            try:
                with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                lang = ext.lstrip('.') or 'text'
                # Prefer ~~~ when content contains triple backticks (e.g. markdown).
                fence = "~~~" if "```" in content else "```"
                markdown_parts.append(f"{fence}{lang}")
                markdown_parts.append(content.rstrip("\n"))
                markdown_parts.append(fence)
                markdown_parts.append("")
            except Exception as e:
                markdown_parts.append(f"> [Error reading file]: {e}\n")

    if file_count == 0 and not any(
        v == Qt.CheckState.Checked for v in check_states.values()
    ):
        markdown_parts.append(
            "_No files selected. Check files or folders in the Context Selection tree._\n"
        )

    return "\n".join(markdown_parts)


def _fmt_size(size_bytes: int) -> str:
    if not size_bytes: return "0 B"
    units = ("B", "KB", "MB", "GB", "TB")
    i, p = 0, float(size_bytes)
    while p >= 1024 and i < len(units) - 1:
        p /= 1024
        i += 1
    return f"{p:.2f} {units[i]}"

# --- ROBUST FILE MODEL ---

class CheckableFileSystemModel(QFileSystemModel):
    checkStateChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.include_logs = False
        self._project_root: Optional[str] = None
        self._check_states: Dict[str, Qt.CheckState] = {}
        self._metadata: Dict[str, Dict[str, object]] = {}
        self.directoryLoaded.connect(self._on_directory_loaded)

    def set_include_logs(self, include: bool):
        self.include_logs = include
        self.layoutChanged.emit()

    def set_project_root(self, project_root: Optional[str]) -> None:
        """Remember the active project root for metadata lookups."""
        self._project_root = os.path.normpath(project_root) if project_root else None
        self._metadata.clear()

    def apply_metadata(self, metadata: Dict[str, Dict[str, object]]) -> None:
        """Merge size/token metadata keyed by absolute path."""
        for path, payload in (metadata or {}).items():
            if not path or not isinstance(payload, dict):
                continue
            self._metadata[os.path.normpath(path)] = dict(payload)
        self.layoutChanged.emit()

    def _format_tokens_display(self, path: str) -> Optional[str]:
        meta = self._metadata.get(os.path.normpath(path))
        if not meta:
            return None
        tokens = meta.get("tokens")
        if tokens is None:
            return None
        try:
            count = int(tokens)
        except (TypeError, ValueError):
            return None
        if meta.get("tokens_overflow"):
            return f"Above {count // 1000}k"
        if count >= 1000:
            return f"{count / 1000:.1f}k"
        return str(count)

    def is_index_checkable(self, index: QModelIndex) -> bool:
        return index.isValid()

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        flags = super().flags(index)
        if self.is_index_checkable(index):
            flags |= Qt.ItemFlag.ItemIsUserCheckable
            if self.isDir(index) and TRISTATE: 
                flags |= TRISTATE
        return flags

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            path = os.path.normpath(self.filePath(index))
            return self._check_states.get(path, Qt.CheckState.Unchecked)

        if index.column() == 0:
            path = os.path.normpath(self.filePath(index))
            state = self._check_states.get(path, Qt.CheckState.Unchecked)
            if role == Qt.ItemDataRole.FontRole and state == Qt.CheckState.Checked:
                return _BOLD_FONT
            if role == Qt.ItemDataRole.BackgroundRole and state in CHECK_BG:
                return CHECK_BG[state]
            if role == Qt.ItemDataRole.ForegroundRole:
                _, ext = os.path.splitext(path)
                if ext.lower() in BINARY_EXTENSIONS:
                    return QBrush(QColor("gray"))
            if role == Qt.ItemDataRole.ToolTipRole:
                meta = self._metadata.get(path)
                if meta and meta.get("tokens_overflow"):
                    return "Token estimate is a lower bound (file exceeded analysis size cap)."
                tokens_disp = self._format_tokens_display(path)
                if tokens_disp:
                    size = meta.get("size") if meta else None
                    size_part = f", {_fmt_size(int(size))}" if size is not None else ""
                    return f"~{tokens_disp} tokens{size_part}"
        return super().data(index, role)

    def setData(self, index: QModelIndex, value, role: int = Qt.ItemDataRole.EditRole) -> bool:
        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:
            if self._update_item(index, Qt.CheckState(value)):
                self.checkStateChanged.emit()
            return True
        return super().setData(index, value, role)

    def set_path_state(self, path: str, state: Qt.CheckState):
        idx = self.index(os.path.normpath(path))
        if idx.isValid():
            if self._update_item(idx, state):
                self.checkStateChanged.emit()

    def _update_item(self, index: QModelIndex, state: Qt.CheckState) -> bool:
        changed = self._set_recursive(index, state)
        if self._update_parents(index.parent()): changed = True
        return changed

    def _set_recursive(self, index: QModelIndex, state: Qt.CheckState) -> bool:
        path = os.path.normpath(self.filePath(index))
        changed = self._check_states.get(path) != state
        self._check_states[path] = state

        if self.isDir(index):
            # Recurse only if loaded, logic holds via _on_directory_loaded
            for row in range(self.rowCount(index)):
                self._set_recursive(self.index(row, 0, index), state)
            
        if changed: self.dataChanged.emit(index, index)
        return changed

    def _update_parents(self, parent_idx: QModelIndex) -> bool:
        changed = False
        while parent_idx.isValid():
            path = os.path.normpath(self.filePath(parent_idx))
            checked, checkable = 0, 0
            
            count = self.rowCount(parent_idx)
            for row in range(count):
                child = self.index(row, 0, parent_idx)
                checkable += 1
                c_path = os.path.normpath(self.filePath(child))
                c_state = self._check_states.get(c_path, Qt.CheckState.Unchecked)
                if c_state == Qt.CheckState.Checked: checked += 1
                elif c_state == Qt.CheckState.PartiallyChecked: checked += 0.5

            new_state = Qt.CheckState.Unchecked
            if checkable > 0:
                if checked == checkable: new_state = Qt.CheckState.Checked
                elif checked > 0: new_state = Qt.CheckState.PartiallyChecked
            
            if self._check_states.get(path) != new_state:
                self._check_states[path] = new_state
                self.dataChanged.emit(parent_idx, parent_idx)
                changed = True
            
            parent_idx = parent_idx.parent()
        return changed

    def _on_directory_loaded(self, path: str):
        idx = self.index(path)
        if not idx.isValid(): return
        p_state = self._check_states.get(os.path.normpath(path), Qt.CheckState.Unchecked)
        if p_state == Qt.CheckState.Checked:
            self._set_recursive(idx, p_state)

class SafeProxyModel(QSortFilterProxyModel):
    def filterAcceptsRow(self, row: int, parent: QModelIndex) -> bool:
        idx = self.sourceModel().index(row, 0, parent)
        if not idx.isValid(): return True
        name = self.sourceModel().fileName(idx)
        if name in EXCLUDE_DIRS: return False
        return super().filterAcceptsRow(row, parent)

# --- MAIN DIALOG ---

class AIStudioDialog(QDialog):
    def __init__(self, api: KoromaliPluginAPI, parent=None):
        super().__init__(parent)
        self.api = api
        self.main_window = getattr(api, 'get_main_window', lambda: None)()
        self.project_root: Optional[str] = None
        
        self._ensure_all_files_saved()

        try:
            self._setup_ui()
            self._init_projects()
        except Exception as e:
            QMessageBox.critical(self, "Initialization Error", f"Failed to open AI Studio:\n{e}")

    def _ensure_all_files_saved(self):
        try:
            if hasattr(self.main_window, 'file_handler') and hasattr(self.main_window.file_handler, 'save_all_files'):
                self.main_window.file_handler.save_all_files()
            elif hasattr(self.main_window, 'save_all_action'):
                self.main_window.save_all_action.trigger()
        except Exception:
            pass

    def _setup_ui(self):
        self.setWindowTitle("AI Studio")
        self.resize(1000, 700)
        layout = QVBoxLayout(self)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter, 1)

        # Left
        left = QWidget()
        l_layout = QVBoxLayout(left)
        p_grp = QGroupBox("1. Project")
        p_form = QFormLayout(p_grp)
        self.cbo_proj = QComboBox()
        self.cbo_proj.currentIndexChanged.connect(self._on_project_changed)
        p_form.addRow(self.cbo_proj)
        l_layout.addWidget(p_grp)

        f_grp = QGroupBox("2. Context Selection")
        f_layout = QVBoxLayout(f_grp)
        btn_bar = QHBoxLayout()
        btn_all = QPushButton("All")
        btn_none = QPushButton("None")
        self.chk_log = QCheckBox("Include Logs")
        btn_all.clicked.connect(lambda: self._set_root(Qt.CheckState.Checked))
        btn_none.clicked.connect(lambda: self._set_root(Qt.CheckState.Unchecked))
        self.chk_log.toggled.connect(self._on_logs_toggled)
        btn_bar.addWidget(btn_all)
        btn_bar.addWidget(btn_none)
        btn_bar.addWidget(self.chk_log)
        f_layout.addLayout(btn_bar)

        self.tree = QTreeView()
        self.model = CheckableFileSystemModel()
        self.model.checkStateChanged.connect(self._update_stats)
        self.proxy = SafeProxyModel()
        self.proxy.setSourceModel(self.model)
        self.tree.setModel(self.proxy)
        self.tree.setHeaderHidden(True)
        self.tree.setAlternatingRowColors(True)
        
        # --- FIXED: Column Resizing & Scrollbar ---
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        header = self.tree.header()
        header.setStretchLastSection(False) 
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        
        f_layout.addWidget(self.tree)
        self.lbl_stats = QLabel("Selected: 0 files (0 B)")
        f_layout.addWidget(self.lbl_stats)
        l_layout.addWidget(f_grp)
        splitter.addWidget(left)

        # Right
        tabs = QTabWidget()
        t_exp = QWidget()
        e_lay = QVBoxLayout(t_exp)
        
        act_bar = QHBoxLayout()
        self.btn_copy = QPushButton("Copy to Clipboard")
        self.btn_save = QPushButton("Save to File...")
        if qta:
            self.btn_copy.setIcon(qta.icon('fa5s.copy'))
            self.btn_save.setIcon(qta.icon('mdi.database-export-outline'))
        
        self.btn_copy.clicked.connect(self._copy_export)
        self.btn_save.clicked.connect(self._save_export)
        act_bar.addWidget(self.btn_copy)
        act_bar.addWidget(self.btn_save)
        e_lay.addLayout(act_bar)
        
        self.txt_preview = QTextEdit()
        self.txt_preview.setReadOnly(True)
        self.txt_preview.setPlaceholderText("Select files to preview...")
        e_lay.addWidget(self.txt_preview)
        tabs.addTab(t_exp, "Export")
        
        # Patcher Tab
        t_patch = QWidget()
        patch_layout = QVBoxLayout(t_patch)
        patch_layout.addWidget(QLabel("1. Paste AI Response (Markdown):"))
        self.patch_input = QTextEdit()
        self.patch_input.setPlaceholderText("Paste the response here...")
        patch_layout.addWidget(self.patch_input, 1)
        
        self.btn_analyze = QPushButton("Analyze Response")
        if qta: self.btn_analyze.setIcon(qta.icon('fa5s.microchip'))
        self.btn_analyze.clicked.connect(self._analyze_response)
        patch_layout.addWidget(self.btn_analyze)
        
        patch_layout.addWidget(QLabel("2. Review & Select Changes:"))
        self.changes_tree = QTreeWidget()
        self.changes_tree.setHeaderLabels(["File", "Operation", "Status"])
        self.changes_tree.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        patch_layout.addWidget(self.changes_tree, 2)
        
        self.btn_apply = QPushButton("Apply Selected Changes")
        if qta: self.btn_apply.setIcon(qta.icon('fa5s.check-circle'))
        self.btn_apply.clicked.connect(self._apply_changes)
        self.btn_apply.setEnabled(False)
        patch_layout.addWidget(self.btn_apply)
        
        tabs.addTab(t_patch, "AI Patcher")
        splitter.addWidget(tabs)
        splitter.setSizes([400, 600])

        self.status = QStatusBar()
        layout.addWidget(self.status)

    def _init_projects(self):
        self.cbo_proj.clear()
        projects = []
        if self.main_window and hasattr(self.main_window, 'project_manager'):
            projects = self.main_window.project_manager.get_open_projects()
        if not projects and hasattr(self.api, 'get_project_root'):
            root = self.api.get_project_root()
            if root:
                projects.append(root)
        for p in projects:
            self.cbo_proj.addItem(os.path.basename(p), p)
        if not projects:
            self.status.showMessage("No open projects found. Open a project first.")
            self.project_root = None
            # Never root the tree at "" — that exposes every drive (C:/, D:/, …).
            self.model.set_project_root(None)
            self.model.setRootPath("")
            self.tree.setRootIndex(self.proxy.mapFromSource(self.model.index("")))
            self.tree.setEnabled(False)
            self.btn_copy.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.txt_preview.setPlainText(
                "No open project.\n\n"
                "Open a folder/project in the main window, then reopen AI Studio "
                "to select files for export."
            )
        else:
            self.tree.setEnabled(True)
            self._on_project_changed(self.cbo_proj.currentIndex())

    def _on_project_changed(self, idx):
        path = self.cbo_proj.itemData(idx)
        if path and os.path.isdir(path):
            self.project_root = path
            self.tree.setEnabled(True)
            self.model.set_project_root(path)
            self.model.setRootPath(path)
            src = self.model.index(path)
            self.tree.setRootIndex(self.proxy.mapFromSource(src))
            self.model._check_states.clear()
            self._update_stats()
        else:
            self.project_root = None
            self.tree.setEnabled(False)
            self.btn_copy.setEnabled(False)
            self.btn_save.setEnabled(False)


    def _set_root(self, state):
        if self.project_root:
            self.model.set_path_state(self.project_root, state)

    def _on_logs_toggled(self, checked: bool):
        self.model.set_include_logs(checked)
        self._update_stats()

    def _update_stats(self):
        # Stats are an approximation; full scan happens on copy/save.
        if not self.project_root:
            self.lbl_stats.setText("Selected: 0 items")
            self.txt_preview.setPlainText("")
            self.btn_copy.setEnabled(False)
            self.btn_save.setEnabled(False)
            return

        count = len([k for k, v in self.model._check_states.items() if v == Qt.CheckState.Checked])
        self.lbl_stats.setText(f"Selected: ~{count} items (Review preview for details)")
        self.btn_copy.setEnabled(True)
        self.btn_save.setEnabled(True)

        content = _scan_and_generate_export(
            self.project_root, self.model._check_states, self.chk_log.isChecked()
        )
        if len(content) > 5000:
            self.txt_preview.setPlainText(content[:5000] + "\n\n... (preview truncated) ...")
        else:
            self.txt_preview.setPlainText(content)

    def _copy_export(self):
        if not self.project_root:
            QMessageBox.warning(self, "No Project", "Please select a project first.")
            return
        try:
            content = _scan_and_generate_export(
                self.project_root, self.model._check_states, self.chk_log.isChecked()
            )
            if not content.strip():
                QMessageBox.warning(self, "Empty Export", "No exportable content. Select files first.")
                return
            QApplication.clipboard().setText(content)
            self.status.showMessage("Copied full export (with Golden Rules) to clipboard.", 4000)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def _save_export(self):
        if not self.project_root:
            QMessageBox.warning(self, "No Project", "Please select a project first.")
            return
        try:
            content = _scan_and_generate_export(
                self.project_root, self.model._check_states, self.chk_log.isChecked()
            )
            if not content.strip():
                QMessageBox.warning(self, "Empty Export", "No exportable content. Select files first.")
                return
            export_dir = os.path.join(get_base_path(), "ai_exports")
            os.makedirs(export_dir, exist_ok=True)
            fname = f"{os.path.basename(self.project_root or 'export')}.md"
            path, _ = QFileDialog.getSaveFileName(
                self, "Save Export", os.path.join(export_dir, fname), "Markdown (*.md)"
            )
            if path:
                with open(path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(content)
                self.status.showMessage(f"Saved to {path}", 5000)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    # --- PATCHER LOGIC ---
    def _op_display(self, op_type: str) -> str:
        return {
            "CREATE_OR_REPLACE": "Write / Overwrite",
            "APPLY_PATCH": "Patch / Diff",
            "DELETE": "Delete",
            "MOVE": "Move / Rename",
        }.get(op_type, op_type or "Unknown")

    def _change_path_label(self, change: dict) -> str:
        if change.get("type") == "MOVE":
            return f"{change.get('src_path', '?')} → {change.get('dst_path', '?')}"
        return str(change.get("file_path", "Unknown"))

    def _analyze_response(self):
        text = self.patch_input.toPlainText()
        if not text.strip():
            return
        if not self.project_root:
            QMessageBox.warning(self, "No Project", "Please select a project first.")
            return

        self.changes_tree.clear()
        try:
            from . import response_parser
            changes = response_parser.parse_llm_response(text, self.project_root)
            if not changes:
                QMessageBox.information(
                    self,
                    "No Changes Found",
                    "No valid file operations found in the response.\n\n"
                    "Expected formats:\n"
                    "• ### File: `/path` + code fence (full file write)\n"
                    "• ```patch with unified diff\n"
                    "• ### File: `/path` + ---DELETED--- / ---MOVED-TO:---",
                )
                self.btn_apply.setEnabled(False)
                return

            for change in changes:
                item = QTreeWidgetItem(self.changes_tree)
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                item.setCheckState(0, Qt.CheckState.Checked)
                op_type = str(change.get("type", "Unknown"))
                item.setText(0, self._change_path_label(change))
                item.setText(1, self._op_display(op_type))
                item.setText(2, "Pending")
                if qta:
                    icons = {
                        "CREATE_OR_REPLACE": "fa5s.file-medical",
                        "APPLY_PATCH": "fa5s.file-contract",
                        "DELETE": "fa5s.trash",
                        "MOVE": "fa5s.file-export",
                    }
                    item.setIcon(0, qta.icon(icons.get(op_type, "fa5s.file")))
                item.setData(0, Qt.ItemDataRole.UserRole, change)
            self.btn_apply.setEnabled(True)
            self.status.showMessage(f"Found {len(changes)} changes.", 5000)
        except Exception as e:
            QMessageBox.critical(self, "Analysis Failed", f"Error parsing response:\n{e}")

    def _apply_changes(self):
        if not self.project_root:
            QMessageBox.warning(self, "No Project", "Please select a project first.")
            return

        root = self.changes_tree.invisibleRootItem()
        selected: List[dict] = []
        items = []
        for i in range(root.childCount()):
            item = root.child(i)
            if item.checkState(0) != Qt.CheckState.Checked:
                continue
            change = item.data(0, Qt.ItemDataRole.UserRole)
            if not change:
                continue
            selected.append(change)
            items.append(item)

        if not selected:
            QMessageBox.information(self, "Nothing Selected", "Check at least one change to apply.")
            return

        try:
            from . import response_parser
        except ImportError:
            QMessageBox.critical(self, "Error", "response_parser module is missing.")
            return

        ok, message = response_parser.apply_changes_to_project(self.project_root, selected)
        if ok:
            for item in items:
                item.setText(2, "Success")
                item.setForeground(2, QBrush(QColor("green")))
            QMessageBox.information(self, "Success", message)
            self.btn_apply.setEnabled(False)
            self.status.showMessage(message, 5000)
        else:
            for item in items:
                item.setText(2, "Error")
                item.setForeground(2, QBrush(QColor("red")))
            QMessageBox.warning(self, "Apply Failed", message)
            self.status.showMessage("Apply failed — see dialog for details.", 5000)