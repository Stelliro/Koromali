# /plugins/live_share_studio/session_manager_panel.py
import os
import json
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QStackedWidget, QMessageBox, QPushButton,
                             QFormLayout, QLineEdit, QListWidget, QLabel, QGroupBox, QApplication, QFileDialog)
from PyQt6.QtGui import QClipboard

from app_core.koromali_api import KoromaliPluginAPI
from .collaboration_server import CollaborationServer
from .collaboration_client import CollaborationClient
from .editor_integration import EditorIntegration
from .host_session_dialog import HostSessionDialog
from .join_session_dialog import JoinSessionDialog

class SessionManagerPanel(QWidget):
    """The main UI dock widget for managing a Live Share session."""

    def __init__(self, api: KoromaliPluginAPI, server: CollaborationServer,
                 client: CollaborationClient, editor_integration: EditorIntegration, 
                 parent=None):
        super().__init__(parent)
        self.api = api
        self.server = server
        self.client = client
        self.editor_integration = editor_integration
        self.project_manager = self.api.get_manager("project")

        self._setup_ui()
        self._connect_signals()
        
    def _setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.stack = QStackedWidget()
        self.default_view = self._create_default_view()
        self.hosting_view = self._create_hosting_view()
        self.guest_view = self._create_guest_view()
        self.stack.addWidget(self.default_view)
        self.stack.addWidget(self.hosting_view)
        self.stack.addWidget(self.guest_view)
        self.main_layout.addWidget(self.stack)

    def _create_default_view(self) -> QWidget:
        view = QWidget()
        layout = QVBoxLayout(view)
        self.start_host_button = QPushButton("Start Hosting Session...")
        self.join_session_button = QPushButton("Join Session...")
        layout.addWidget(self.start_host_button)
        layout.addWidget(self.join_session_button)
        layout.addStretch()
        return view

    def _create_hosting_view(self) -> QWidget:
        view = QWidget()
        layout = QVBoxLayout(view)
        info_group = QGroupBox("Session Details (Host)")
        form = QFormLayout(info_group)
        self.session_url_label = QLineEdit(readOnly=True)
        self.encryption_key_label = QLineEdit(readOnly=True)
        self.copy_details_button = QPushButton("Copy Details")
        form.addRow("Session URL:", self.session_url_label)
        form.addRow("Encryption Key:", self.encryption_key_label)
        form.addRow(self.copy_details_button)
        layout.addWidget(info_group)
        
        users_group = QGroupBox("Connected Users")
        users_layout = QVBoxLayout(users_group)
        self.host_user_list = QListWidget()
        users_layout.addWidget(self.host_user_list)
        layout.addWidget(users_group, 1)

        self.export_log_button = QPushButton("Export Edit Log")
        self.stop_host_button = QPushButton("Stop Hosting")
        layout.addWidget(self.export_log_button)
        layout.addWidget(self.stop_host_button)
        return view

    def _create_guest_view(self) -> QWidget:
        view = QWidget()
        layout = QVBoxLayout(view)
        users_group = QGroupBox("Connected Users")
        users_layout = QVBoxLayout(users_group)
        self.guest_user_list = QListWidget()
        users_layout.addWidget(self.guest_user_list)
        layout.addWidget(users_group, 1)
        self.leave_session_button = QPushButton("Leave Session")
        layout.addWidget(self.leave_session_button)
        return view

    def _connect_signals(self):
        # Default View
        self.start_host_button.clicked.connect(self._start_hosting)
        self.join_session_button.clicked.connect(self._join_session)
        # Hosting View
        self.stop_host_button.clicked.connect(self._stop_hosting)
        self.copy_details_button.clicked.connect(self._copy_session_details)
        self.export_log_button.clicked.connect(self._export_edit_log)
        # Guest View
        self.leave_session_button.clicked.connect(self._leave_session)
        # Server/Client signals
        self.server.server_started.connect(self._on_server_started)
        self.client.connection_successful.connect(lambda: self.stack.setCurrentIndex(2))
        self.client.connection_failed.connect(lambda msg: QMessageBox.critical(self, "Connection Failed", msg))
        self.client.user_list_updated.connect(self._update_user_list)
        self.client.permission_denied.connect(lambda reason: self.api.show_status_message(f"Permission Denied: {reason}", 5000))
        self.client.edit_log_received.connect(self._save_edit_log)

    def _start_hosting(self):
        if not self.project_manager.get_open_projects():
            QMessageBox.warning(self, "No Projects Open", "Please open at least one project before starting a session.")
            return

        dialog = HostSessionDialog(self.project_manager.get_open_projects(), self)
        if dialog.exec():
            selected_projects = dialog.get_selected_projects()
            port = dialog.get_port()
            key = dialog.get_encryption_key()

            if not selected_projects or not key:
                QMessageBox.warning(self, "Incomplete Setup", "You must select projects and provide an encryption key.")
                return

            self.api.show_status_message("Starting Live Share server...", 5000)
            self.server.set_session_data(key, selected_projects)
            self.server.start_server(port=port)

    def _on_server_started(self, ip, port, session_id):
        url = f"ws://{ip}:{port}"
        self.session_url_label.setText(url)
        self.encryption_key_label.setText(self.server.encryption_key)
        self.stack.setCurrentIndex(1)
        self.api.get_main_window().set_shared_paths(self.server.shared_projects)
        # The host also connects as a client
        host_username = "Host"
        host_id = self.client.crypto.generate_user_id() # Host gets a unique ID too
        self.client.connect_to_server(url, host_username, host_id, self.server.encryption_key)
        
    def _copy_session_details(self):
        url = self.session_url_label.text()
        key = self.encryption_key_label.text()
        details = f"Koromali Live Share Session:\nURL: {url}\nKey: {key}"
        QApplication.clipboard().setText(details)
        self.api.show_status_message("Session details copied to clipboard.", 3000)

    def _stop_hosting(self):
        self.server.stop()
        if self.client.is_connected():
            self.client.disconnect()
        self.api.get_main_window().set_shared_paths([])
        self.stack.setCurrentIndex(0)

    def _join_session(self):
        dialog = JoinSessionDialog(self)
        if dialog.exec():
            url = dialog.get_session_url()
            key = dialog.get_encryption_key()
            username = dialog.get_username() or f"Guest_{os.getlogin()}"
            user_id = dialog.get_user_id()

            if url and key and user_id and username:
                self.client.connect_to_server(url, username, user_id, key)
            else:
                QMessageBox.warning(self, "Incomplete Details", "Please fill in all session details.")

    def _leave_session(self):
        if self.client.is_connected():
            self.client.disconnect()
        # The disconnect signal handler in client now clears shared paths
        self.stack.setCurrentIndex(0)

    def _export_edit_log(self):
        self.client.send_message("get_edit_log", {})
    
    def _save_edit_log(self, log_data: dict):
        if not log_data:
            self.api.show_status_message("No edit history to export.", 3000)
            return
        
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Edit Log", "", "JSON Files (*.json)")
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    json.dump(log_data, f, indent=4)
                self.api.show_status_message(f"Edit log saved to {file_path}", 4000)
            except Exception as e:
                QMessageBox.critical(self, "Save Failed", f"Could not save the edit log: {e}")

    def _update_user_list(self, users: dict):
        current_list = self.host_user_list if self.server.is_running() else self.guest_user_list
        current_list.clear()
        for user_id, user_info in users.items():
            roles_str = ", ".join(user_info.get('roles', []))
            current_list.addItem(f"{user_info.get('name')} [{roles_str}]")