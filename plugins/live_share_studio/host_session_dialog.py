# /plugins/live_share_studio/host_session_dialog.py
import os
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit,
                             QDialogButtonBox, QListWidget, QListWidgetItem,
                             QPushButton, QHBoxLayout, QSpinBox, QLabel)
from PyQt6.QtCore import Qt
from .crypto_utils import CryptoUtils

class HostSessionDialog(QDialog):
    """Dialog for the host to select projects and set session parameters."""

    def __init__(self, open_projects: list, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Host New Live Share Session")
        self.setMinimumWidth(400)
        self.crypto = CryptoUtils()

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.project_list = QListWidget()
        self.project_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        for project_path in open_projects:
            item = QListWidgetItem(os.path.basename(project_path))
            item.setData(Qt.ItemDataRole.UserRole, project_path)
            self.project_list.addItem(item)
            item.setSelected(True)
        form.addRow("Projects to Share:", self.project_list)
        
        self.port_spinbox = QSpinBox()
        self.port_spinbox.setRange(1024, 65535)
        self.port_spinbox.setValue(8765)
        form.addRow("Port:", self.port_spinbox)
        
        key_layout = QHBoxLayout()
        self.encryption_key_input = QLineEdit()
        self.encryption_key_input.setPlaceholderText("Leave blank to auto-generate")
        generate_key_button = QPushButton("Generate")
        generate_key_button.clicked.connect(self._generate_key)
        key_layout.addWidget(self.encryption_key_input)
        key_layout.addWidget(generate_key_button)
        form.addRow("Encryption Key:", key_layout)
        
        layout.addLayout(form)
        layout.addWidget(QLabel("<small>Share the URL and Key with guests securely.</small>"))

        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
    def _generate_key(self):
        self.encryption_key_input.setText(self.crypto.generate_key())

    def get_selected_projects(self) -> list:
        return [item.data(Qt.ItemDataRole.UserRole) for item in self.project_list.selectedItems()]
        
    def get_port(self) -> int:
        return self.port_spinbox.value()
        
    def get_encryption_key(self) -> str:
        key = self.encryption_key_input.text().strip()
        if not key:
            key = self.crypto.generate_key()
            self.encryption_key_input.setText(key)
        return key