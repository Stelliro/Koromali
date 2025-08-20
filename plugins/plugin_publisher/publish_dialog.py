# Koromali/plugins/plugin_publisher/publish_dialog.py
import os
import shutil
import tempfile
import json
import copy
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QComboBox,
                             QTextEdit, QPushButton, QDialogButtonBox, QLabel,
                             QMessageBox, QHBoxLayout, QListWidget,
                             QListWidgetItem, QRadioButton, QGroupBox,
                             QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# --- Content for auto-initializing a distro repo ---
README_CONTENT = """# Koromali Plugin Distribution Repository
This repository is structured to serve plugins for the Koromali.
- `index.json`: A manifest file listing all available plugins and their download URLs.
- `zips/`: This directory contains the packaged `.zip` files for each plugin.
To publish a new version of a plugin, use the "Publish Plugin" tool inside
Koromali.
"""
GITIGNORE_CONTENT = """# Ignore common temp files
*.tmp, *.bak, *~
# Ignore local environment
venv/, .venv/
"""


def _bump_version(version_str, level='patch'):
    """Bumps a semantic version string."""
    try:
        parts = version_str.split('.')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            return version_str
        major, minor, patch = [int(p) for p in parts]
        if level == 'patch':
            patch += 1
        elif level == 'minor':
            minor, patch = minor + 1, 0
        elif level == 'major':
            major, minor, patch = major + 1, 0, 0
        return f"{major}.{minor}.{patch}"
    except Exception:
        return version_str


class VersionConflictDialog(QDialog):
    """Dialog to resolve a version conflict by overwriting or creating a new version."""
    def __init__(self, plugin_name, local_version, remote_version, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Version Conflict")
        self.result = (None, None)  # (action, version)
        self.local_version = local_version

        layout = QVBoxLayout(self)
        msg = f"A version conflict was detected for <b>{plugin_name}</b>."
        layout.addWidget(QLabel(msg))

        info_layout = QFormLayout()
        info_layout.addRow("Your local version:", QLabel(f"<b>{local_version}</b>"))
        info_layout.addRow("Version in repository:",
                           QLabel(f"<b>{remote_version}</b>"))
        layout.addLayout(info_layout)

        group = QGroupBox("Choose an action:")
        group_layout = QVBoxLayout(group)

        self.overwrite_radio = QRadioButton(
            f"Overwrite with version {local_version}")
        self.new_version_radio = QRadioButton("Create a new version:")
        self.new_version_edit = QLineEdit(_bump_version(remote_version, 'patch'))

        new_version_layout = QHBoxLayout()
        new_version_layout.addWidget(self.new_version_radio)
        new_version_layout.addWidget(self.new_version_edit)

        group_layout.addWidget(self.overwrite_radio)
        group_layout.addLayout(new_version_layout)
        self.new_version_radio.setChecked(True)
        self.overwrite_radio.toggled.connect(self.toggle_line_edit)
        layout.addWidget(group)

        buttons = (QDialogButtonBox.StandardButton.Ok |
                   QDialogButtonBox.StandardButton.Cancel)
        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        self.toggle_line_edit(True)

    def toggle_line_edit(self, checked):
        self.new_version_edit.setEnabled(self.new_version_radio.isChecked())

    def accept(self):
        if self.overwrite_radio.isChecked():
            self.result = ('overwrite', self.local_version)
        elif self.new_version_radio.isChecked():
            new_version = self.new_version_edit.text().strip()
            if not new_version:
                QMessageBox.warning(self, "Invalid Version",
                                    "New version cannot be empty.")
                return
            self.result = ('new', new_version)
        super().accept()


class BumpVersionDialog(QDialog):
    """Dialog to ask the user how to bump the version of a new plugin."""
    def __init__(self, current_version, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Initial Version")
        self.current_version = current_version
        self.new_version = current_version

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Publishing a new plugin with initial version:"))

        group = QGroupBox("Choose version:")
        group_layout = QVBoxLayout(group)

        self.radios = {
            'none': QRadioButton(f"Keep current version ({current_version})"),
            'patch': QRadioButton(
                f"Patch -> {_bump_version(current_version, 'patch')}"),
            'minor': QRadioButton(
                f"Minor -> {_bump_version(current_version, 'minor')}"),
            'major': QRadioButton(
                f"Major -> {_bump_version(current_version, 'major')}")
        }

        self.radios['none'].setChecked(True)
        for radio in self.radios.values():
            group_layout.addWidget(radio)

        layout.addWidget(group)

        buttons = (QDialogButtonBox.StandardButton.Ok |
                   QDialogButtonBox.StandardButton.Cancel)
        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def accept(self):
        for level, radio in self.radios.items():
            if radio.isChecked():
                if level == 'none':
                    self.new_version = self.current_version
                else:
                    self.new_version = _bump_version(self.current_version, level)
                break
        super().accept()


class MultiPublishSelectionDialog(QDialog):
    """A dialog to select which plugins to include in a batch publish."""
    def __init__(self, plugins, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Plugins to Publish")
        self.setMinimumSize(400, 300)
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Select plugins to include in this batch:"))
        self.list_widget = QListWidget()
        for plugin_data in plugins:
            display = (f"{plugin_data.get('name', 'Unknown')} "
                       f"v{plugin_data.get('version', '0.0.0')}")
            item = QListWidgetItem(display)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Checked)
            item.setData(Qt.ItemDataRole.UserRole, plugin_data)
            self.list_widget.addItem(item)
        layout.addWidget(self.list_widget)

        buttons = (QDialogButtonBox.StandardButton.Ok |
                   QDialogButtonBox.StandardButton.Cancel)
        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_selected_plugins(self):
        selected = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                selected.append(item.data(Qt.ItemDataRole.UserRole))
        return selected


class PublishDialog(QDialog):
    """A dialog to manage the process of publishing a plugin."""

    def __init__(self, api, parent):
        super().__init__(parent)
        self.api = api
        self.git_manager = api.get_manager("git")
        self.github_manager = api.get_manager("github")
        self.plugin_manager = api.get_manager("plugin")
        self.settings = api.get_manager("settings")
        self.publish_queue = []
        self._temp_dir = None
        self._current_step = None
        self.cloned_repo_path = None
        self.auto_increment_choice = False

        self.setWindowTitle("Publish a Plugin")
        self.setMinimumSize(600, 450)
        self._setup_ui()
        self._connect_ui_signals()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.plugin_selector = QComboBox()
        form_layout.addRow("Plugin to Publish:", self.plugin_selector)

        repo_layout = QHBoxLayout()
        repo_layout.setContentsMargins(0, 0, 0, 0)
        self.repo_combo = QComboBox()
        self.manage_repos_button = QPushButton("Manage...")
        repo_layout.addWidget(self.repo_combo, 1)
        repo_layout.addWidget(self.manage_repos_button)
        form_layout.addRow("Target Repository:", repo_layout)

        self.commit_message = QTextEdit()
        self.commit_message.setFixedHeight(80)
        form_layout.addRow("Commit Message:", self.commit_message)
        layout.addLayout(form_layout)

        layout.addWidget(QLabel("Log:"))
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setFont(QFont("Consolas", 9))
        self.log_output.setStyleSheet(
            "background-color: #1E1E1E; color: #D4D4D4;")
        layout.addWidget(self.log_output, 1)

        self.button_box = QDialogButtonBox()
        self.publish_button = self.button_box.addButton(
            "Publish Selected", QDialogButtonBox.ButtonRole.AcceptRole)
        self.auto_publish_button = self.button_box.addButton(
            "Publish Multiple...", QDialogButtonBox.ButtonRole.ActionRole)
        self.close_button = self.button_box.addButton(
            "Close", QDialogButtonBox.ButtonRole.RejectRole)
        layout.addWidget(self.button_box)

    def _connect_ui_signals(self):
        self.publish_button.clicked.connect(self._start_single_publish_flow)
        self.auto_publish_button.clicked.connect(self._start_auto_publish_flow)
        self.close_button.clicked.connect(self.reject)
        self.manage_repos_button.clicked.connect(self._open_preferences)
        self.plugin_selector.currentIndexChanged.connect(
            self._on_plugin_selected)

    def _open_preferences(self):
        self.api.get_main_window()._action_open_preferences()

    def _set_ui_locked(self, locked: bool):
        self.publish_button.setEnabled(not locked)
        self.auto_publish_button.setEnabled(not locked)
        self.plugin_selector.setEnabled(not locked)
        self.repo_combo.setEnabled(not locked)
        self.commit_message.setEnabled(not locked)
        self.manage_repos_button.setEnabled(not locked)
        self.close_button.setText("Cancel" if locked else "Close")

    def _add_log(self, message, is_error=False, is_warning=False):
        color = ("#FF5555" if is_error else
                 "#FFC66D" if is_warning else "#A9B7C6")
        self.log_output.append(
            f"<span style='color: {color};'>{message}</span>")
        self.api.log_info(f"[Plugin Publisher] {message}")

    def showEvent(self, event):
        super().showEvent(event)
        self._populate_plugins()
        self._populate_repos()
        can_publish = bool(self.repo_combo.count() and
                           self.plugin_selector.count())
        self.publish_button.setEnabled(can_publish)
        self.auto_publish_button.setEnabled(can_publish)
        tooltip = ""
        if not can_publish:
            tooltip = "Configure a distribution repo and select a plugin."
        self.publish_button.setToolTip(tooltip)
        self.auto_publish_button.setToolTip(tooltip)
        self.log_output.clear()

    def _populate_plugins(self):
        self.plugin_selector.clear()
        for plugin in self._get_publishable_plugins():
            display = (f"{plugin.get('name', 'Unknown')} "
                       f"(v{plugin.get('version', '0.0.0')})")
            self.plugin_selector.addItem(display, plugin)
        self._on_plugin_selected()

    def _get_publishable_plugins(self):
        """Gets a list of publishable plugin metadata from the plugin manager."""
        return self.plugin_manager.get_installed_plugins()

    def _populate_repos(self):
        self.repo_combo.clear()
        all_repos = self.settings.get("source_control_repos", [])
        primary_repo_id = self.settings.get("active_update_repo_id")
        primary_idx = -1
        for i, repo_config in enumerate(all_repos):
            repo_path = f"{repo_config.get('owner')}/{repo_config.get('repo')}"
            self.repo_combo.addItem(repo_path, repo_config)
            if repo_config.get('id') == primary_repo_id:
                primary_idx = i
        if primary_idx != -1:
            self.repo_combo.setCurrentIndex(primary_idx)

    def _on_plugin_selected(self, indexx=0):
        plugin_data = self.plugin_selector.currentData()
        if not plugin_data:
            self.commit_message.clear()
            return

        name = plugin_data.get('name', 'Unknown Plugin')
        version = plugin_data.get('version', '0.0.0')
        commit_msg = f"feat(plugin): Publish {name} v{version}"
        self.commit_message.setText(commit_msg)

    def _cleanup(self, success=True):
        self._set_ui_locked(False)
        self.git_manager.git_success.disconnect(self._on_git_step_success)
        self.git_manager.git_error.disconnect(self._on_publish_failed)
        if self._temp_dir and os.path.exists(self._temp_dir):
            shutil.rmtree(self._temp_dir, ignore_errors=True)
            self._add_log("Cleaned up temporary directory.")
        self._temp_dir = None
        self.cloned_repo_path = None
        self._current_step = None
        self.publish_queue = []

    def _on_publish_failed(self, error_message):
        self._add_log(f"FAILED on step '{self._current_step}': {error_message}",
                      is_error=True)
        self._cleanup(success=False)

    def _start_single_publish_flow(self):
        plugin_data = self.plugin_selector.currentData()
        if not plugin_data:
            QMessageBox.warning(self, "No Plugin Selected",
                                "Please select a plugin.")
            return

        publish_item = {
            "original_data": plugin_data,
            "run_data": copy.deepcopy(plugin_data)
        }
        self.auto_increment_choice = False
        self._start_publish_flow([publish_item])

    def _start_auto_publish_flow(self):
        all_plugins = self._get_publishable_plugins()
        if not all_plugins:
            QMessageBox.information(self, "No Plugins",
                                    "No publishable plugins found.")
            return

        dialog = MultiPublishSelectionDialog(all_plugins, self)
        if not dialog.exec():
            return

        plugins_to_publish = dialog.get_selected_plugins()
        if not plugins_to_publish:
            QMessageBox.information(self, "No Selection",
                                    "No plugins were selected.")
            return

        reply = QMessageBox.question(
            self, "Auto-increment Versions?",
            "Do you want to automatically increment the patch version for "
            "plugins that are not newer than the repository version?",
            (QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No |
             QMessageBox.StandardButton.Cancel),
            QMessageBox.StandardButton.Yes)

        if reply == QMessageBox.StandardButton.Cancel:
            return

        self.auto_increment_choice = (reply == QMessageBox.StandardButton.Yes)
        publish_list = [{"original_data": p, "run_data": copy.deepcopy(p)}
                        for p in plugins_to_publish]
        self._start_publish_flow(publish_list)

    def _start_publish_flow(self, publish_list):
        repo_data = self.repo_combo.currentData()
        if not repo_data:
            QMessageBox.warning(self, "Missing Repository",
                                "Please select a distribution repository.")
            return

        commit_text = self.commit_message.toPlainText().strip()
        if len(publish_list) == 1 and not commit_text:
            QMessageBox.warning(self, "Missing Commit Message",
                                "Please provide a commit message.")
            return

        self.publish_queue = publish_list
        owner = repo_data.get('owner')
        repo = repo_data.get('repo')
        self.distro_repo_path = f"{owner}/{repo}"

        self._set_ui_locked(True)
        self.log_output.clear()
        self._add_log("Starting plugin publication process...")
        self._temp_dir = tempfile.mkdtemp(prefix="Koromali-plugin-publish-")
        self.git_manager.git_success.connect(self._on_git_step_success)
        self.git_manager.git_error.connect(self._on_publish_failed)
        self._current_step = "CLONE"
        self._add_log(f"Cloning '{self.distro_repo_path}'...")
        repo_url = f"https://github.com/{self.distro_repo_path}.git"
        self.git_manager.clone_repo(repo_url, self._temp_dir)

    def _on_git_step_success(self, message: str, data: dict):
        if self._current_step == "CLONE":
            self.cloned_repo_path = data.get("path")
            self._add_log("Successfully cloned repository.")
            index_json_path = os.path.join(self.cloned_repo_path, "index.json")

            if not os.path.exists(index_json_path):
                self._current_step = "INITIALIZE_COMMIT"
                self._add_log("Empty repo detected. Initializing structure...")
                self._initialize_distro_repo()
                commit_msg = "ci: Initialize plugin distribution repository"
                self.git_manager.commit_files(self.cloned_repo_path, commit_msg)
            else:
                self._process_publish_queue()

        elif self._current_step == "INITIALIZE_COMMIT":
            self._add_log("Initial commit successful.")
            self._process_publish_queue()

        elif self._current_step == "PUBLISH_COMMIT":
            self._add_log(f"Commit successful. {message}")
            self._current_step = "PUSH"
            self._add_log(f"Pushing changes to '{self.distro_repo_path}'...")
            self.git_manager.push(self.cloned_repo_path)

        elif self._current_step == "PUSH":
            self._add_log("Push successful!")
            for item in self.publish_queue:
                original_version = item["original_data"].get("version")
                new_version = item["run_data"].get("version")
                if new_version != original_version:
                    self._update_local_plugin_json(item["original_data"],
                                                   new_version)

            self._add_log("\n--- PUBLICATION COMPLETE ---")
            self._cleanup(success=True)
            self._populate_plugins()

    def _process_publish_queue(self):
        self._current_step = "PROCESS_PLUGINS"
        is_batch = len(self.publish_queue) > 1
        index_path = os.path.join(self.cloned_repo_path, 'index.json')
        index_data = []
        try:
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    index_data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            self._on_publish_failed(f"Failed to load or parse index.json: {e}")
            return

        processed_items = []
        for item in self.publish_queue:
            plugin_data = item["run_data"]
            plugin_name = plugin_data.get('name', 'Unknown')
            self._add_log(f"--- Processing {plugin_name} ---")
            try:
                should_publish, final_version = self._check_version(
                    item, index_data, batch_mode=is_batch)

                if should_publish:
                    item['run_data']['version'] = final_version
                    self._package_plugin(item['run_data'])
                    self._update_index_data(item['run_data'], index_data)
                    processed_items.append(item)
                else:
                    self._add_log(f"Skipping '{plugin_name}'.", is_warning=True)
            except FileNotFoundError as e:
                self._add_log(f"ERROR for '{plugin_name}': {e}. Skipping.",
                              is_error=True)
            except Exception as e:
                msg = f"UNEXPECTED ERROR for '{plugin_name}': {e}. Skipping."
                self._add_log(msg, is_error=True)

        self.publish_queue = processed_items
        if not self.publish_queue:
            msg = "No plugins processed for publication. Nothing to commit."
            self._add_log(msg, is_warning=True)
            self._cleanup()
            return

        try:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=4)
        except IOError as e:
            self._on_publish_failed(f"Failed to write updated index.json: {e}")
            return

        commit_msg = self.commit_message.toPlainText()
        if is_batch:
            count = len(self.publish_queue)
            plural = 's' if count > 1 else ''
            commit_msg = f"feat(plugins): Update {count} plugin{plural}"
        elif len(self.publish_queue) == 1:
            p_data = self.publish_queue['run_data']
            p_name = p_data.get('name', 'Unknown')
            p_ver = p_data.get('version', '0.0.0')
            commit_msg = f"feat(plugin): Publish {p_name} v{p_ver}"
        self.commit_message.setText(commit_msg)

        count = len(self.publish_queue)
        self._add_log(f"Committing updates for {count} plugin(s)...")
        self._current_step = "PUBLISH_COMMIT"
        self.git_manager.commit_files(self.cloned_repo_path, commit_msg)

    def _check_version(self, publish_item, index_data, batch_mode=False):
        local_data = publish_item['original_data']
        local_version = local_data.get('version', '0.0.0')
        plugin_id = local_data.get('id')
        plugin_name = local_data.get('name', 'Unknown')

        old_entry = next((p for p in index_data if p.get('id') == plugin_id), None)

        if not old_entry:
            self._add_log(f"New plugin '{plugin_id}'.")
            if not batch_mode:
                dialog = BumpVersionDialog(local_version, self)
                if dialog.exec():
                    self._add_log(f"User selected initial version "
                                  f"{dialog.new_version}.")
                    return True, dialog.new_version
                return False, None
            return True, local_version

        remote_version = old_entry.get('version')
        if not remote_version:
            return True, local_version

        if local_version > remote_version:
            self._add_log(f"Newer version found: {remote_version} -> "
                          f"{local_version}.")
            return True, local_version

        if batch_mode:
            if self.auto_increment_choice:
                new_version = _bump_version(remote_version, 'patch')
                self._add_log(f"Auto-incrementing version: {remote_version} -> "
                              f"{new_version}.")
                return True, new_version
            else:
                return False, None

        dialog = VersionConflictDialog(
            plugin_name, local_version, remote_version, self)
        if dialog.exec():
            action, version = dialog.result
            if action:
                self._add_log(f"User chose to '{action}' with version {version}.")
                return True, version

        return False, None

    def _package_plugin(self, plugin_data):
        plugin_id = plugin_data.get('id')
        plugin_source_path = plugin_data.get('path')

        if not plugin_source_path or not os.path.isdir(plugin_source_path):
            raise FileNotFoundError(
                f"Source directory for '{plugin_id}' not found in metadata")

        zips_dir = os.path.join(self.cloned_repo_path, 'zips')
        os.makedirs(zips_dir, exist_ok=True)
        final_zip_path = os.path.join(zips_dir, f"{plugin_id}.zip")

        self._add_log(f"Packaging '{plugin_id}' to zip from "
                      f"'{plugin_source_path}'...")
        shutil.make_archive(os.path.splitext(final_zip_path), 'zip',
                            plugin_source_path)

    def _update_index_data(self, plugin_data, index_data):
        plugin_id = plugin_data.get('id')
        rel_zip_path = os.path.join('zips', f"{plugin_id}.zip").replace("\\", "/")
        download_url = (f"https://raw.githubusercontent.com/"
                        f"{self.distro_repo_path}/main/{rel_zip_path}")

        new_entry = {k: plugin_data.get(k) for k in
                     ('id', 'name', 'author', 'version', 'description')}
        new_entry['download_url'] = download_url

        index_data[:] = [entry for entry in index_data
                         if entry.get('id') != plugin_id]
        index_data.append(new_entry)
        self._add_log(f"Updated index for '{plugin_id}'.")

    def _update_local_plugin_json(self, plugin_data, new_version):
        plugin_id = plugin_data.get('id')
        self._add_log(f"Updating local plugin.json for '{plugin_id}' to "
                      f"v{new_version}")
        try:
            plugin_source_path = plugin_data.get('path')
            if not plugin_source_path:
                raise FileNotFoundError(
                    f"Source path for {plugin_id} not found in metadata.")

            json_file_path = os.path.join(plugin_source_path, 'plugin.json')

            with open(json_file_path, 'r+', encoding='utf-8') as f:
                plugin_json = json.load(f)
                plugin_json['version'] = new_version
                f.seek(0)
                json.dump(plugin_json, f, indent=4)
                f.truncate()
            self._add_log(f"Successfully updated local version for {plugin_id}.")
        except Exception as e:
            self._add_log(f"Could not update local plugin.json for "
                          f"{plugin_id}: {e}", is_error=True)

    def _initialize_distro_repo(self):
        try:
            with open(os.path.join(self.cloned_repo_path, 'index.json'), 'w') as f:
                json.dump([], f, indent=4)
            with open(os.path.join(self.cloned_repo_path, 'README.md'), 'w') as f:
                f.write(README_CONTENT)
            with open(os.path.join(self.cloned_repo_path, '.gitignore'), 'w') as f:
                f.write(GITIGNORE_CONTENT)
            zips_dir = os.path.join(self.cloned_repo_path, 'zips')
            os.makedirs(zips_dir, exist_ok=True)
            with open(os.path.join(zips_dir, '.gitkeep'), 'w') as f:
                pass
        except Exception as e:
            self._on_publish_failed(f"Error initializing distro repo files: {e}")
            raise