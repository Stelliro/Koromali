# /ui/dialogs/run_config_dialog.py
"""Dialog for choosing a project entry-point script."""

from __future__ import annotations

import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QLineEdit,
    QListWidgetItem,
    QDialogButtonBox,
)


class RunConfigDialog(QDialog):
    def __init__(self, project_path: str, parent=None):
        super().__init__(parent)
        self.project_path = project_path
        self.selected_script = None
        self.setWindowTitle("Configure Launch Script")
        self.resize(500, 400)
        self._init_ui()
        self._load_files()

    def _init_ui(self):
        layout = QVBoxLayout(self)

        lbl = QLabel(
            f"Select the main entry point for:\n{os.path.basename(self.project_path)}"
        )
        lbl.setStyleSheet("font-weight: bold; margin-bottom: 5px;")
        layout.addWidget(lbl)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search files...")
        self.search_input.textChanged.connect(self._filter_list)
        layout.addWidget(self.search_input)

        self.file_list = QListWidget()
        self.file_list.itemDoubleClicked.connect(self.accept)
        layout.addWidget(self.file_list)

        btns = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        layout.addWidget(btns)

    def _load_files(self):
        self.files = []
        if not self.project_path or not os.path.isdir(self.project_path):
            return

        skip_dirs = {
            "venv",
            ".venv",
            "__pycache__",
            ".git",
            "node_modules",
            "dist",
            "build",
            "ai_exports",
        }
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            for f in files:
                if f.endswith(".py"):
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, self.project_path)
                    self.files.append((rel_path.replace("\\", "/"), full_path))

        self.files.sort()
        self._filter_list("")

    def _filter_list(self, text: str):
        self.file_list.clear()
        needle = (text or "").lower()
        for rel_path, full_path in self.files:
            if needle in rel_path.lower():
                item = QListWidgetItem(rel_path)
                item.setData(Qt.ItemDataRole.UserRole, full_path)
                self.file_list.addItem(item)

    def accept(self):
        if self.file_list.currentItem():
            self.selected_script = self.file_list.currentItem().data(
                Qt.ItemDataRole.UserRole
            )
            super().accept()
