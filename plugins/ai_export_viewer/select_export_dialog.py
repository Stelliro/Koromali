# /plugins/ai_export_viewer/select_export_dialog.py
import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QListWidgetItem, QDialogButtonBox, QPushButton
from PyQt6.QtCore import Qt
from utils.helpers import get_base_path


class SelectExportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select AI Export for Restore")
        self.setMinimumSize(400, 500)
        self.selected_export_path = None

        layout = QVBoxLayout(self)
        self.export_list = QListWidget()
        layout.addWidget(self.export_list)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        self.ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        self.ok_button.setEnabled(False)
        self.export_list.currentItemChanged.connect(lambda: self.ok_button.setEnabled(True))
        self.export_list.itemDoubleClicked.connect(self.accept)

        self._populate_list()
    
    def _populate_list(self):
        export_dir = os.path.join(get_base_path(), "ai_exports")
        if not os.path.isdir(export_dir):
            return

        all_files = []
        for root, _, files in os.walk(export_dir):
            # Exclude backups subdirectories from the restore list by default
            if "backups" in root.split(os.sep):
                continue
            for filename in files:
                if filename.endswith('.md'):
                    path = os.path.join(root, filename)
                    display_name = os.path.relpath(path, export_dir).replace(os.sep, '/')
                    all_files.append((path, display_name))
        
        # Sort by most recent first
        all_files.sort(key=lambda x: os.path.getmtime(x[0]), reverse=True)

        for path, display_name in all_files:
            item = QListWidgetItem(display_name)
            item.setData(Qt.ItemDataRole.UserRole, path)
            self.export_list.addItem(item)
            
    def accept(self):
        if item := self.export_list.currentItem():
            self.selected_export_path = item.data(Qt.ItemDataRole.UserRole)
        super().accept()