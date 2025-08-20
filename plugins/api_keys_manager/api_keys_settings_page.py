# Koromali/plugins/api_keys_manager/api_keys_settings_page.py
from PyQt6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QLabel,
    QDialogButtonBox, QVBoxLayout
)
import qtawesome as qta


class ApiKeysDialog(QDialog):
    """A dialog for managing API keys."""
    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager

        self.setWindowTitle("Manage API Keys")
        self.setMinimumWidth(500)

        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        info_label = QLabel(
            "Enter your API keys below. They are stored locally and securely."
        )
        form_layout.addRow(info_label)

        # Add providers here. We'll start with OpenAI.
        self.openai_key_input, openai_layout = self._create_key_input()
        form_layout.addRow("OpenAI API Key:", openai_layout)

        main_layout.addLayout(form_layout)

        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        main_layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        self.load_settings()

    def _create_key_input(self) -> tuple[QLineEdit, QHBoxLayout]:
        """Creates a password-style QLineEdit with a show/hide button."""
        layout = QHBoxLayout()
        line_edit = QLineEdit()
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        show_hide_button = QPushButton(qta.icon('fa5s.eye'), "")
        show_hide_button.setCheckable(True)
        show_hide_button.setToolTip("Show/Hide Key")
        show_hide_button.setFixedWidth(30)
        show_hide_button.toggled.connect(
            lambda c: line_edit.setEchoMode(
                QLineEdit.EchoMode.Normal if c
                else QLineEdit.EchoMode.Password)
        )

        layout.addWidget(line_edit)
        layout.addWidget(show_hide_button)
        return line_edit, layout

    def load_settings(self):
        """Loads saved API keys into the input fields."""
        keys = self.settings_manager.get("api_keys", {})
        self.openai_key_input.setText(keys.get("OpenAI", ""))

    def save_settings(self):
        """Saves the API keys from the input fields."""
        keys = self.settings_manager.get("api_keys", {})
        keys["OpenAI"] = self.openai_key_input.text()
        self.settings_manager.set("api_keys", keys)
        self.settings_manager.save()

    def accept(self):
        """Saves settings and closes the dialog."""
        self.save_settings()
        super().accept()