# /plugins/live_share_studio/join_session_dialog.py
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox, QPushButton, QHBoxLayout)
from .crypto_utils import CryptoUtils

class JoinSessionDialog(QDialog):
    """A dialog for a guest to enter connection details."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Join Live Share Session")
        self.crypto = CryptoUtils()
        
        self.layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.session_url_input = QLineEdit()
        self.session_url_input.setPlaceholderText("ws://<host-ip-address>:<port>")
        form_layout.addRow("Session URL:", self.session_url_input)

        self.encryption_key_input = QLineEdit()
        self.encryption_key_input.setPlaceholderText("Enter the secret key from the host")
        form_layout.addRow("Encryption Key:", self.encryption_key_input)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Your display name")
        form_layout.addRow("Your Username:", self.username_input)

        user_id_layout = QHBoxLayout()
        self.user_id_input = QLineEdit()
        self.user_id_input.setPlaceholderText("A unique ID to identify you")
        self.user_id_input.setText(self.crypto.generate_user_id())
        generate_id_button = QPushButton("Generate")
        generate_id_button.clicked.connect(self._generate_user_id)
        user_id_layout.addWidget(self.user_id_input)
        user_id_layout.addWidget(generate_id_button)
        form_layout.addRow("Your Unique ID:", user_id_layout)
        
        self.layout.addLayout(form_layout)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        
        self.layout.addWidget(button_box)

    def _generate_user_id(self):
        self.user_id_input.setText(self.crypto.generate_user_id())
        
    def get_session_url(self) -> str:
        return self.session_url_input.text().strip()

    def get_encryption_key(self) -> str:
        return self.encryption_key_input.text().strip()

    def get_username(self) -> str:
        return self.username_input.text().strip()

    def get_user_id(self) -> str:
        return self.user_id_input.text().strip()