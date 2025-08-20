# Koromali/ui/preferences_dialog.py
import uuid
import sys
import os
import tempfile
import requests
from typing import Optional, Any, TYPE_CHECKING
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTabWidget,
                             QWidget, QLabel, QComboBox, QSpinBox, QCheckBox,
                             QPushButton, QLineEdit, QDialogButtonBox,
                             QFontComboBox, QSplitter, QFormLayout,
                             QListWidget, QListWidgetItem, QMessageBox,
                             QGroupBox, QFileDialog, QInputDialog,
                             QStackedWidget)
from PyQt6.QtGui import QFont, QDesktopServices, QColor
from PyQt6.QtCore import Qt, QSize, pyqtSignal, QUrl

from app_core.config import APP_NAME
from utils.logger import log

if sys.platform == "win32":
    try:
        import winshell
    except ImportError:
        winshell = None
        log.warning("The 'winshell' package is not installed. Startup shortcut features will be disabled.")

import qtawesome as qta
from utils.helpers import get_startup_shortcut_path
from app_core.plugin_manager import Plugin

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager
    from app_core.github_manager import GitHubManager
    from app_core.source_control_manager import SourceControlManager
    from app_core.plugin_manager import PluginManager
    from app_core.koromali_api import KoromaliPluginAPI
    from app_core.settings_manager import SettingsManager


class AuthDialog(QDialog):
    def __init__(self, user_code: str, verification_uri: str,
                 parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setWindowTitle("GitHub Device Authorization")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Please authorize Koromali in your browser."))
        url_label = QLabel(f"1. Open: <a href='{verification_uri}'>{verification_uri}</a>")
        url_label.setOpenExternalLinks(True)
        layout.addWidget(url_label)
        layout.addWidget(QLabel("2. Enter this one-time code:"))
        code_label = QLineEdit(user_code)
        code_label.setReadOnly(True)
        code_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        code_label.setFont(QFont("Consolas", 14, QFont.Weight.Bold))
        layout.addWidget(code_label)
        QDesktopServices.openUrl(QUrl(verification_uri))
        self.setFixedSize(self.sizeHint())


class PreferencesDialog(QDialog):
    settings_changed_for_editor_refresh = pyqtSignal()
    theme_changed_signal = pyqtSignal(str)

    def __init__(self, theme_manager: 'ThemeManager', git_manager: 'SourceControlManager',
                 github_manager: 'GitHubManager', plugin_manager: 'PluginManager',
                 koromali_api: 'KoromaliPluginAPI', settings_manager: 'SettingsManager',
                 parent: Optional[QWidget] = None):
        super().__init__(parent)
        log.info("PreferencesDialog initializing...")
        self.setWindowTitle("Preferences")
        self.setMinimumSize(QSize(850, 700))
        self.theme_manager = theme_manager
        self.git_manager = git_manager
        self.github_manager = github_manager
        self.plugin_manager = plugin_manager
        self.koromali_api = koromali_api
        self.settings = settings_manager # Use passed-in instance

        self.original_settings: dict[str, Any] = {}
        self.original_git_config: dict[str, str] = {}
        self.staged_repos: list[dict] = []
        self.staged_active_repo_id: Optional[str] = None
        self.current_repo_id_in_form: Optional[str] = None
        self.auth_dialog: Optional[AuthDialog] = None
        self.restart_needed = False
        self.is_loading = False
        self.main_layout = QVBoxLayout(self)
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        self._create_tabs()
        self._create_button_box()
        self._connect_global_signals()
        self._connect_ui_changed_signals()
        log.info("PreferencesDialog initialized.")

    def _create_tabs(self):
        self._create_appearance_tab()
        self._create_editor_tab()
        self._create_run_tab()
        self._create_system_tab()
        self._create_source_control_tab()
        self._create_plugins_tab()

    def _create_button_box(self):
        buttons = (
                QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Apply)
        self.button_box = QDialogButtonBox(buttons)
        self.main_layout.addWidget(self.button_box)

    def _connect_global_signals(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.button_box.button(QDialogButtonBox.StandardButton.Apply).clicked.connect(self.apply_settings)
        self.git_manager.git_config_ready.connect(self._populate_git_config_fields)
        self.github_manager.device_code_ready.connect(self._on_device_code_ready)
        self.github_manager.auth_successful.connect(self._on_auth_successful)
        self.github_manager.auth_failed.connect(self._on_auth_failed)
        self.github_manager.auth_polling_lapsed.connect(self._on_auth_polling_lapsed)
        self.github_manager.operation_success.connect(self._handle_github_op_success)
        self.github_manager.plugin_index_ready.connect(self._on_plugin_index_ready)
        self.git_manager.git_success.connect(self._handle_git_success)

    def _handle_github_op_success(self, message, data):
        if "Repository" in message and "created" in message:
            new_repo_id = str(uuid.uuid4())
            owner, repo_name = self.git_manager.parse_git_url(data.get("clone_url"))
            new_repo = {"id": new_repo_id, "name": data.get("name"), "owner": owner, "repo": repo_name}
            self.staged_repos.append(new_repo)
            QMessageBox.information(self, "Success", f"Repository '{repo_name}' created on GitHub.")
            self._populate_repo_list(select_repo_id=new_repo_id)
            self._on_ui_setting_changed()

    def showEvent(self, event):
        self.is_loading = True
        self._load_settings_into_dialog()
        self.git_manager.get_git_config()
        self._update_auth_status()
        self._populate_all_plugin_lists()
        self.button_box.button(QDialogButtonBox.StandardButton.Apply).setEnabled(False)
        self.restart_needed = False
        super().showEvent(event)
        self.is_loading = False

    def _load_settings_into_dialog(self):
        self.original_settings = self.settings.settings.copy()
        self._repopulate_theme_combo()
        self.font_family_combo.setCurrentFont(QFont(self.settings.get("font_family")))
        self.font_size_spinbox.setValue(self.settings.get("font_size"))
        self.show_line_numbers_checkbox.setChecked(self.settings.get("show_line_numbers"))
        self.word_wrap_checkbox.setChecked(self.settings.get("word_wrap"))
        self.show_indent_guides_checkbox.setChecked(self.settings.get("show_indentation_guides"))
        self.indent_style_combo.setCurrentText(self.settings.get("indent_style").capitalize())
        self.indent_width_spinbox.setValue(self.settings.get("indent_width"))
        self.auto_save_checkbox.setChecked(self.settings.get("auto_save_enabled"))
        self.auto_save_delay_spinbox.setValue(self.settings.get("auto_save_delay_seconds"))
        self.max_recent_files_spinbox.setValue(self.settings.get("max_recent_files"))
        self.python_path_edit.setText(self.settings.get("python_interpreter_path", ""))
        if sys.platform == "win32":
            self.nsis_path_edit.setText(self.settings.get("nsis_path", ""))
            self.cleanup_build_checkbox.setChecked(self.settings.get("cleanup_after_build", True))
            if winshell and hasattr(self, 'run_in_background_checkbox'): self.run_in_background_checkbox.setChecked(
                self.settings.get("run_in_background", False))

        self.staged_repos = [r.copy() for r in self.settings.get("source_control_repos", [])]
        self.staged_active_repo_id = self.settings.get("active_update_repo_id")
        self._populate_repo_list()
        self.plugins_repo_edit.setText(self.settings.get("plugins_distro_repo", "Stelliro/Koromali-plugins"))

    def _connect_ui_changed_signals(self):
        for w in self.findChildren((QComboBox, QSpinBox, QCheckBox, QFontComboBox, QLineEdit)):
            if isinstance(w, QComboBox):
                w.currentIndexChanged.connect(self._on_ui_setting_changed)
            elif isinstance(w, QFontComboBox):
                w.currentFontChanged.connect(self._on_ui_setting_changed)
            elif isinstance(w, QSpinBox):
                w.valueChanged.connect(self._on_ui_setting_changed)
            elif isinstance(w, QCheckBox):
                w.stateChanged.connect(self._on_ui_setting_changed)
            elif isinstance(w, QLineEdit):
                w.textChanged.connect(self._on_ui_setting_changed)

    def _on_ui_setting_changed(self, *args):
        if not self.is_loading and self.isVisible(): self.button_box.button(
            QDialogButtonBox.StandardButton.Apply).setEnabled(True)

    def apply_settings(self):
        ab = self.button_box.button(QDialogButtonBox.StandardButton.Apply)
        if not ab.isEnabled(): return

        ss = {
            "last_theme_id": self.theme_combo.currentData(),
            "font_family": self.font_family_combo.currentFont().family(),
            "font_size": self.font_size_spinbox.value(),
            "show_line_numbers": self.show_line_numbers_checkbox.isChecked(),
            "word_wrap": self.word_wrap_checkbox.isChecked(),
            "show_indentation_guides": self.show_indent_guides_checkbox.isChecked(),
            "indent_style": self.indent_style_combo.currentText().lower(),
            "indent_width": self.indent_width_spinbox.value(),
            "auto_save_enabled": self.auto_save_checkbox.isChecked(),
            "auto_save_delay_seconds": self.auto_save_delay_spinbox.value(),
            "max_recent_files": self.max_recent_files_spinbox.value(),
            "python_interpreter_path": self.python_path_edit.text().strip(),
            "source_control_repos": self.staged_repos,
            "active_update_repo_id": self.staged_active_repo_id,
            "plugins_distro_repo": self.plugins_repo_edit.text().strip(),
        }

        if sys.platform == "win32":
            ss["nsis_path"] = self.nsis_path_edit.text().strip()
            ss["cleanup_after_build"] = self.cleanup_build_checkbox.isChecked()
            if winshell and hasattr(self, 'run_in_background_checkbox'):
                ss["run_in_background"] = self.run_in_background_checkbox.isChecked()
                if ss["run_in_background"] != self.original_settings.get("run_in_background", False):
                    self._manage_startup_shortcut(ss["run_in_background"])

        nn, ne = self.git_user_name_edit.text().strip(), self.git_user_email_edit.text().strip()
        if nn != self.original_git_config.get('name') or ne != self.original_git_config.get('email'):
            self.git_manager.set_git_config(nn, ne)
            self.original_git_config = {'name': nn, 'email': ne}

        self._save_repo_form_to_staged()

        for k, v in ss.items(): self.settings.set(k, v, False)
        self.settings.save()
        self.theme_changed_signal.emit(self.theme_combo.currentData())
        self.settings_changed_for_editor_refresh.emit()
        self.original_settings = self.settings.settings.copy()
        ab.setEnabled(False)
        if self.restart_needed: QMessageBox.information(self, "Restart Required", "Some changes require a restart.")
        self.restart_needed = False
        log.info("Applied settings.")

    def accept(self):
        if self.button_box.button(QDialogButtonBox.StandardButton.Apply).isEnabled(): self.apply_settings()
        super().accept()

    def reject(self):
        if self.auth_dialog and self.auth_dialog.isVisible(): self.auth_dialog.reject()
        if self.button_box.button(QDialogButtonBox.StandardButton.Apply).isEnabled():
            if QMessageBox.question(self, "Unsaved Changes", "Discard?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) == QMessageBox.StandardButton.No: return
        if self.theme_combo.currentData() != self.original_settings.get("last_theme_id"):
            self.theme_changed_signal.emit(self.original_settings.get("last_theme_id"))
        super().reject()

    def _create_layout_in_groupbox(self, t, pl):
        g = QGroupBox(t)
        pl.addWidget(g)
        l = QFormLayout(g)
        return l

    def _create_appearance_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(15)
        theme_group = self._create_layout_in_groupbox("Theming", layout)
        self.theme_combo = QComboBox()
        self.edit_themes_button = QPushButton("Customize Themes...")
        self.connect_theme_editor_button()
        theme_group.addRow("Theme:", self.theme_combo)
        theme_group.addRow("", self.edit_themes_button)
        font_group = self._create_layout_in_groupbox("Editor Font", layout)
        self.font_family_combo = QFontComboBox()
        self.font_size_spinbox = QSpinBox()
        self.font_size_spinbox.setRange(6, 72)
        font_group.addRow("Font Family:", self.font_family_combo)
        font_group.addRow("Font Size:", self.font_size_spinbox)
        layout.addStretch()
        self.tab_widget.addTab(tab, qta.icon('fa5s.palette'), "Appearance")

    def _repopulate_theme_combo(self):
        current_id = self.original_settings.get("last_theme_id", "Koromali_dark")
        self.theme_combo.blockSignals(True)
        self.theme_combo.clear()
        for theme_id, name in self.theme_manager.get_available_themes_for_ui().items():
            self.theme_combo.addItem(name, theme_id)
        if (index := self.theme_combo.findData(current_id)) != -1: self.theme_combo.setCurrentIndex(index)
        self.theme_combo.blockSignals(False)

    def connect_theme_editor_button(self):
        if self.koromali_api.theme_editor_launcher:
            try:
                self.edit_themes_button.clicked.disconnect()
            except TypeError:
                pass
            self.edit_themes_button.clicked.connect(self.koromali_api.theme_editor_launcher)
            if theme_editor_instance := self.koromali_api.get_plugin_instance('theme_editor'):
                if dialog := getattr(theme_editor_instance, 'dialog_instance', None):
                    if hasattr(dialog, 'custom_themes_changed'):
                        dialog.custom_themes_changed.connect(self._repopulate_theme_combo)
            self.edit_themes_button.show()
        else:
            self.edit_themes_button.hide()

    def _create_editor_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(15)
        display_layout = self._create_layout_in_groupbox("Display", layout)
        display_layout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        self.show_line_numbers_checkbox = QCheckBox("Show line numbers")
        self.word_wrap_checkbox = QCheckBox("Enable word wrap")
        self.show_indent_guides_checkbox = QCheckBox("Show indentation guides")
        display_layout.addRow(self.show_line_numbers_checkbox)
        display_layout.addRow(self.word_wrap_checkbox)
        display_layout.addRow(self.show_indent_guides_checkbox)
        indent_layout = self._create_layout_in_groupbox("Indentation", layout)
        self.indent_style_combo = QComboBox()
        self.indent_style_combo.addItems(["Spaces", "Tabs"])
        self.indent_width_spinbox = QSpinBox()
        self.indent_width_spinbox.setRange(1, 16)
        indent_layout.addRow("Indent Using:", self.indent_style_combo)
        indent_layout.addRow("Indent/Tab Width:", self.indent_width_spinbox)
        file_layout = self._create_layout_in_groupbox("File Handling", layout)
        self.auto_save_checkbox = QCheckBox("Enable auto-save")
        self.auto_save_delay_spinbox = QSpinBox()
        self.auto_save_delay_spinbox.setRange(1, 60)
        self.auto_save_delay_spinbox.setSuffix(" seconds")
        self.max_recent_files_spinbox = QSpinBox()
        self.max_recent_files_spinbox.setRange(1, 50)
        file_layout.addRow(self.auto_save_checkbox)
        file_layout.addRow("Auto-Save Delay:", self.auto_save_delay_spinbox)
        file_layout.addRow("Max Recent Files:", self.max_recent_files_spinbox)
        layout.addStretch()
        self.tab_widget.addTab(tab, qta.icon('fa5s.edit'), "Editor")

    def _create_run_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(15)
        py_group = self._create_layout_in_groupbox("Python Interpreter", layout)
        py_path_layout = QHBoxLayout()
        self.python_path_edit = QLineEdit()
        self.python_path_edit.setPlaceholderText("Leave empty to use system default")
        browse_py_button = QPushButton("Browse...")
        browse_py_button.clicked.connect(self._browse_for_python)
        py_path_layout.addWidget(self.python_path_edit)
        py_path_layout.addWidget(browse_py_button)
        py_group.addRow("Python Executable Path:", py_path_layout)
        build_group = self._create_layout_in_groupbox("Build & Installation (Windows Only)", layout)
        if sys.platform == "win32":
            nsis_path_layout = QHBoxLayout()
            self.nsis_path_edit = QLineEdit()
            self.nsis_path_edit.setPlaceholderText("e.g., C:\\Program Files (x86)\\NSIS\\makensis.exe")
            browse_nsis_button = QPushButton("Browse...")
            browse_nsis_button.clicked.connect(self._browse_for_nsis)
            nsis_path_layout.addWidget(self.nsis_path_edit)
            nsis_path_layout.addWidget(browse_nsis_button)
            self.cleanup_build_checkbox = QCheckBox("Delete temporary build files after install")
            build_group.addRow("NSIS Path (for Installer):", nsis_path_layout)
            build_group.addRow("", self.cleanup_build_checkbox)
        else:
            build_group.addRow(QLabel("Build options are only available on Windows."))
        layout.addStretch()
        self.tab_widget.addTab(tab, qta.icon('fa5s.play-circle'), "Execution")

    def _browse_for_nsis(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select NSIS Executable", "", "NSIS (makensis.exe);;All Files (*)")
        if path: self.nsis_path_edit.setText(path)

    def _browse_for_python(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Python Executable", "",
                                              "Python Executable (python.exe; python);;All Files (*)")
        if path: self.python_path_edit.setText(path)

    def _create_system_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(15)
        startup_group = self._create_layout_in_groupbox("System Startup", layout)
        if sys.platform == "win32" and winshell:
            self.run_in_background_checkbox = QCheckBox(
                f"Launch {APP_NAME} on system startup (runs in system tray)")
            self.run_in_background_checkbox.setToolTip(
                "Creates a shortcut in the Windows Startup folder.")
            startup_group.addRow(
                self.run_in_background_checkbox)
        else:
            startup_group.addRow(QLabel("Startup options are only available on Windows."))
        layout.addStretch()
        self.tab_widget.addTab(tab, qta.icon('fa5s.desktop'), "System")

    def _manage_startup_shortcut(self, create: bool):
        if not winshell: return
        shortcut_path = get_startup_shortcut_path()
        if not shortcut_path: return
        try:
            if create and not os.path.exists(shortcut_path):
                tray_exe_name = f"{APP_NAME}Tray.exe"
                tray_exe_path = os.path.join(os.path.dirname(sys.executable), tray_exe_name)
                if not os.path.exists(tray_exe_path):
                    dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', tray_exe_name))
                    if os.path.exists(dev_path):
                        tray_exe_path = dev_path
                    else:
                        raise FileNotFoundError(f"{tray_exe_name} not found.")
                
                winshell.CreateShortcut(Path=shortcut_path, Target=tray_exe_path)
                log.info(f"Created startup shortcut for '{tray_exe_path}'.")
            elif not create and os.path.exists(shortcut_path):
                os.remove(shortcut_path)
                log.info("Removed startup shortcut.")
        except Exception as e:
            QMessageBox.critical(self, "Shortcut Error", f"Could not manage startup shortcut:\n{e}")

    def _create_source_control_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(15)
        git_user_group = self._create_layout_in_groupbox("Git Identity", layout)
        self.git_user_name_edit = QLineEdit()
        self.git_user_email_edit = QLineEdit()

        sync_button = QPushButton("Sync with GitHub")
        sync_button.setObjectName("syncWithGitHubButton")
        sync_button.clicked.connect(self._sync_git_with_github)

        git_user_group.addRow("Username:", self.git_user_name_edit)
        git_user_group.addRow("Email:", self.git_user_email_edit)
        git_user_group.addRow(sync_button)

        gh_auth_group = self._create_layout_in_groupbox("GitHub Integration", layout)
        self.auth_status_label = QLabel("<i>Checking status...</i>")
        self.auth_button = QPushButton("Log in to GitHub")
        self.auth_button.clicked.connect(self.github_manager.start_device_flow)
        self.logout_button = QPushButton("Log out")
        self.logout_button.clicked.connect(self._logout_github)
        gh_auth_group.addRow(self.auth_status_label)
        gh_auth_group.addRow(self.auth_button)
        gh_auth_group.addRow(self.logout_button)

        repo_group = self._create_layout_in_groupbox("Update Repository Management", layout)
        repo_splitter, _ = self._create_repo_management_widgets()
        repo_group.layout().addWidget(repo_splitter)
        layout.addStretch()
        self.tab_widget.addTab(tab, qta.icon('fa5b.git-alt'), "Source Control")

    def _create_repo_management_widgets(self):
        splitter = QSplitter()
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.addWidget(QLabel("Repositories:"))
        self.repo_list = QListWidget()
        self.repo_list.currentItemChanged.connect(self._on_repo_selection_changed)
        left_layout.addWidget(self.repo_list)
        repo_buttons = QHBoxLayout()
        add_repo_btn = QPushButton()
        add_repo_btn.setIcon(qta.icon('fa5s.plus'))
        remove_repo_btn = QPushButton()
        remove_repo_btn.setIcon(qta.icon('fa5s.minus'))
        add_repo_btn.clicked.connect(self._action_add_repo)
        remove_repo_btn.clicked.connect(self._action_remove_repo)
        repo_buttons.addStretch()
        repo_buttons.addWidget(add_repo_btn)
        repo_buttons.addWidget(remove_repo_btn)
        left_layout.addLayout(repo_buttons)
        splitter.addWidget(left_widget)
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        self.repo_name_edit = QLineEdit()
        self.repo_owner_edit = QLineEdit()
        self.repo_repo_edit = QLineEdit()
        self.repo_is_active_checkbox = QCheckBox("Set as active repo for app updates")
        self.repo_is_active_checkbox.toggled.connect(self._on_active_checkbox_toggled)
        self.create_on_gh_button = QPushButton("Create on GitHub & Link")
        self.create_on_gh_button.clicked.connect(self._action_create_repo)
        form_layout.addRow("Name:", self.repo_name_edit)
        form_layout.addRow("Owner (user or org):", self.repo_owner_edit)
        form_layout.addRow("Repository Name:", self.repo_repo_edit)
        form_layout.addRow(self.repo_is_active_checkbox)
        form_layout.addRow(self.create_on_gh_button)
        splitter.addWidget(form_widget)
        return splitter, form_widget

    def _create_plugins_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        plugins_tabs = QTabWidget()
        plugins_tabs.addTab(self._create_plugins_manage_tab(), qta.icon('fa5s.tasks'), "Manage")
        plugins_tabs.addTab(self._create_plugins_install_tab(), qta.icon('fa5s.download'), "Install")
        layout.addWidget(plugins_tabs)
        self.tab_widget.addTab(tab, qta.icon('fa5s.plug'), "Plugins")

    def _create_plugins_manage_tab(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.addWidget(QLabel("Installed Plugins:"))
        self.manage_plugins_list = QListWidget()
        self.manage_plugins_list.itemSelectionChanged.connect(self._on_installed_plugin_selected)
        left_layout.addWidget(self.manage_plugins_list)
        batch_buttons_layout = QHBoxLayout()
        self.enable_all_button = QPushButton("Enable All")
        self.disable_all_button = QPushButton("Disable Non-Essential")
        self.enable_all_button.clicked.connect(self._enable_all_plugins)
        self.disable_all_button.clicked.connect(self._disable_all_non_core_plugins)
        batch_buttons_layout.addWidget(self.enable_all_button)
        batch_buttons_layout.addWidget(self.disable_all_button)
        left_layout.addLayout(batch_buttons_layout)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        self.plugin_details_stack = QStackedWidget()
        placeholder = QLabel("Select a plugin to see details.")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plugin_details_stack.addWidget(placeholder)
        details_widget = QWidget()
        details_layout = QFormLayout(details_widget)
        self.plugin_name_label = QLabel()
        self.plugin_version_label = QLabel()
        self.plugin_author_label = QLabel()
        self.plugin_desc_label = QLabel()
        self.plugin_desc_label.setWordWrap(True)
        self.plugin_status_label = QLabel()
        details_layout.addRow("<b>Name:</b>", self.plugin_name_label)
        details_layout.addRow("<b>Version:</b>", self.plugin_version_label)
        details_layout.addRow("<b>Author:</b>", self.plugin_author_label)
        details_layout.addRow("<b>Description:</b>", self.plugin_desc_label)
        details_layout.addRow("<b>Status:</b>", self.plugin_status_label)
        self.plugin_details_stack.addWidget(details_widget)
        actions_layout = QHBoxLayout()
        self.enable_plugin_checkbox = QCheckBox("Enabled")
        self.enable_plugin_checkbox.toggled.connect(self._on_plugin_enabled_changed)
        self.reload_plugin_button = QPushButton("Reload")
        self.reload_plugin_button.clicked.connect(self._reload_selected_plugin)
        self.uninstall_button = QPushButton("Uninstall")
        self.uninstall_button.clicked.connect(self._uninstall_selected_plugin)
        actions_layout.addWidget(self.enable_plugin_checkbox)
        actions_layout.addStretch()
        actions_layout.addWidget(self.reload_plugin_button)
        actions_layout.addWidget(self.uninstall_button)
        right_layout.addWidget(self.plugin_details_stack, 1)
        right_layout.addLayout(actions_layout)
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([300, 550])
        layout.addWidget(splitter)
        return tab

    def _create_plugins_install_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(10)
        repo_group = QGroupBox("Install from Repository")
        repo_layout = QVBoxLayout(repo_group)
        repo_input_widget = QWidget()
        repo_input_layout = QHBoxLayout(repo_input_widget)
        repo_input_layout.setContentsMargins(0, 0, 0, 0)
        repo_input_layout.addWidget(QLabel("GitHub Repo (user/repo):"))
        self.plugins_repo_edit = QLineEdit()
        self.fetch_plugins_button = QPushButton("Fetch")
        self.fetch_plugins_button.clicked.connect(self._fetch_remote_plugins)
        repo_input_layout.addWidget(self.plugins_repo_edit, 1)
        repo_input_layout.addWidget(self.fetch_plugins_button)
        repo_layout.addWidget(repo_input_widget)
        self.remote_plugins_list = QListWidget()
        self.remote_plugins_list.itemSelectionChanged.connect(self._on_remote_plugin_selected)
        repo_layout.addWidget(self.remote_plugins_list)
        self.install_remote_button = QPushButton("Install Selected Plugin")
        self.install_remote_button.setEnabled(False)
        self.install_remote_button.clicked.connect(self._install_selected_remote_plugin)
        repo_layout.addWidget(self.install_remote_button, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(repo_group)
        local_group = QGroupBox("Install from File/URL")
        local_layout = QHBoxLayout(local_group)
        self.install_from_url_button = QPushButton("From URL...")
        self.install_from_file_button = QPushButton("From File...")
        self.install_from_url_button.clicked.connect(lambda: self._install_plugin_from_url(""))
        self.install_from_file_button.clicked.connect(self._install_plugin_from_file)
        local_layout.addWidget(self.install_from_url_button)
        local_layout.addWidget(self.install_from_file_button)
        local_layout.addStretch()
        layout.addWidget(local_group)
        layout.addStretch()
        return tab

    def _action_create_repo(self):
        owner, repo = self.repo_owner_edit.text(), self.repo_repo_edit.text()
        if owner and repo: self.github_manager.create_repo(repo, "", False)

    def _populate_git_config_fields(self, name, email):
        self.git_user_name_edit.setText(name)
        self.git_user_email_edit.setText(email)
        self.original_git_config = {'name': name, 'email': email}

    def _handle_git_success(self, msg, data):
        if "config updated" in msg: self._on_ui_setting_changed()

    def _sync_git_with_github(self):
        user_info = self.github_manager.get_user_info()
        if not user_info:
            QMessageBox.warning(self, "Not Logged In", "Please log in to GitHub first.")
            return
        user_name = user_info.get('login', '')
        user_email = user_info.get('email', '')
        if not user_email: user_email = f"{user_info.get('id')}+{user_name}@users.noreply.github.com"
        self.git_user_name_edit.setText(user_name)
        self.git_user_email_edit.setText(user_email)
        self._on_ui_setting_changed()

    def _logout_github(self):
        self.github_manager.logout()
        self._update_auth_status()

    def _update_auth_status(self):
        user = self.github_manager.get_authenticated_user()
        is_logged_in = bool(user)
        self.auth_status_label.setText(f"Logged in as: <b>{user}</b>" if is_logged_in else "<i>Not logged in.</i>")
        self.auth_button.setVisible(not is_logged_in)
        self.logout_button.setVisible(is_logged_in)
        sync_button = self.findChild(QPushButton, "syncWithGitHubButton")
        if sync_button:
            sync_button.setEnabled(is_logged_in)

    def _on_device_code_ready(self, data):
        self.auth_dialog = AuthDialog(data.get('user_code'), data.get('verification_uri'),
                                      self)
        self.auth_dialog.show()
        self.github_manager.poll_for_token(
            data['device_code'], data['interval'], data['expires_in'])

    def _on_auth_successful(self, username):
        if self.auth_dialog: self.auth_dialog.accept()
        self.auth_dialog = None
        self._update_auth_status()
        self._on_ui_setting_changed()

    def _on_auth_failed(self, error):
        if self.auth_dialog: self.auth_dialog.reject()
        self.auth_dialog = None
        QMessageBox.critical(self, "GitHub Authentication Failed", error)
        self._update_auth_status()

    def _on_auth_polling_lapsed(self):
        if self.auth_dialog: self.auth_dialog.reject()
        self.auth_dialog = None
        QMessageBox.warning(self, "Authentication Timed Out", "Device authorization timed out.")

    def _on_repo_selection_changed(self, current, previous):
        if previous: self._save_repo_form_to_staged()
        self._load_staged_to_repo_form(current)

    def _on_active_checkbox_toggled(self, checked):
        if checked and self.current_repo_id_in_form: self.staged_active_repo_id = self.current_repo_id_in_form
        self._on_ui_setting_changed()

    def _save_repo_form_to_staged(self):
        if not self.current_repo_id_in_form: return
        repo = next((r for r in self.staged_repos if r['id'] == self.current_repo_id_in_form), None)
        if repo:
            repo['name'] = self.repo_name_edit.text()
            repo['owner'] = self.repo_owner_edit.text()
            repo['repo'] = self.repo_repo_edit.text()

    def _load_staged_to_repo_form(self, item):
        self.is_loading = True
        self.current_repo_id_in_form = item.data(Qt.ItemDataRole.UserRole) if item else None
        if self.current_repo_id_in_form:
            repo = next((r for r in self.staged_repos if r['id'] == self.current_repo_id_in_form), {})
            self.repo_name_edit.setText(repo.get('name', ''))
            self.repo_owner_edit.setText(repo.get('owner', ''))
            self.repo_repo_edit.setText(repo.get('repo', ''))
            self.repo_is_active_checkbox.setChecked(self.current_repo_id_in_form == self.staged_active_repo_id)
        else:
            self._clear_repo_form()
        self.is_loading = False

    def _action_add_repo(self):
        new_repo = {"id": str(uuid.uuid4()), "name": "New Repository", "owner": "", "repo": ""}
        self.staged_repos.append(new_repo)
        self._populate_repo_list(select_repo_id=new_repo['id'])
        self._on_ui_setting_changed()

    def _action_remove_repo(self):
        if item := self.repo_list.currentItem():
            repo_id = item.data(Qt.ItemDataRole.UserRole)
            self.staged_repos = [r for r in self.staged_repos if r['id'] != repo_id]
            if self.staged_active_repo_id == repo_id: self.staged_active_repo_id = None
            self._populate_repo_list()
            self._on_ui_setting_changed()

    def _populate_repo_list(self, select_repo_id=None):
        self.repo_list.clear()
        self._clear_repo_form()
        for repo in self.staged_repos:
            item = QListWidgetItem(repo['name'])
            item.setData(Qt.ItemDataRole.UserRole, repo['id'])
            self.repo_list.addItem(item)
        if select_repo_id:
            for i in range(self.repo_list.count()):
                if self.repo_list.item(i).data(Qt.ItemDataRole.UserRole) == select_repo_id:
                    self.repo_list.setCurrentRow(i)
                    break

    def _clear_repo_form(self):
        self.repo_name_edit.clear()
        self.repo_owner_edit.clear()
        self.repo_repo_edit.clear()
        self.repo_is_active_checkbox.setChecked(False)

    def _populate_all_plugin_lists(self):
        self._populate_manage_plugins_list()

    def _populate_manage_plugins_list(self):
        self.manage_plugins_list.clear()
        plugins = sorted(self.plugin_manager.get_all_plugins(), key=lambda p: p.name.lower())
        for p in plugins:
            item = QListWidgetItem(p.name)
            item.setData(Qt.ItemDataRole.UserRole, p.id)
            self.manage_plugins_list.addItem(item)

    def _on_installed_plugin_selected(self):
        items = self.manage_plugins_list.selectedItems()
        if not items:
            self.plugin_details_stack.setCurrentIndex(0)
            return
        plugin = self.plugin_manager.plugins.get(items[0].data(Qt.ItemDataRole.UserRole))
        if plugin:
            self.plugin_details_stack.setCurrentIndex(1)
            self.is_loading = True
            self.plugin_name_label.setText(plugin.name)
            self.plugin_version_label.setText(plugin.version)
            self.plugin_author_label.setText(plugin.manifest.get('author', 'N/A'))
            self.plugin_desc_label.setText(plugin.manifest.get('description', 'No description.'))
            self.plugin_status_label.setText(plugin.status_reason)
            self.enable_plugin_checkbox.setChecked(plugin.enabled)
            self.enable_plugin_checkbox.setEnabled(not plugin.is_core)
            self.reload_plugin_button.setEnabled(plugin.is_loaded)
            self.uninstall_button.setEnabled(plugin.source_type == 'user')
            self.is_loading = False

    def _on_plugin_enabled_changed(self, checked):
        if self.is_loading: return
        items = self.manage_plugins_list.selectedItems()
        if items and (plugin := self.plugin_manager.plugins.get(items[0].data(Qt.ItemDataRole.UserRole))):
            (self.plugin_manager.enable_plugin if checked else self.plugin_manager.disable_plugin)(plugin.id)
            self.restart_needed = True

    def _reload_selected_plugin(self):
        items = self.manage_plugins_list.selectedItems()
        self.restart_needed = True
        if items:
            self.plugin_manager.reload_plugin(items[0].data(Qt.ItemDataRole.UserRole))
            self._on_installed_plugin_selected()

    def _reload_all_plugins(self):
        self.plugin_manager.discover_and_load_plugins()
        self.restart_needed = True
        self._populate_manage_plugins_list()

    def _enable_all_plugins(self):
        if QMessageBox.question(self, "Enable All Plugins",
                                "This will enable all plugins and reload them. A restart might be required for all changes to take full effect.\n\nContinue?",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
            log.info("User requested to enable all plugins.")
            self.plugin_manager.enable_all()
            self.restart_needed = True
            self._populate_manage_plugins_list()
            self._on_ui_setting_changed()

    def _disable_all_non_core_plugins(self):
        if QMessageBox.question(self, "Disable Non-Essential Plugins",
                                "This will disable and unload all non-essential plugins (e.g., language support, AI tools, debug tools).\nCore functionality like the file explorer and search will not be affected.\n\nContinue?",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
            log.info("User requested to disable all non-essential plugins.")
            self.plugin_manager.disable_all_non_core()
            self.restart_needed = True
            self._populate_manage_plugins_list()
            self._on_ui_setting_changed()

    def _on_remote_plugin_selected(self):
        self.install_remote_button.setEnabled(bool(self.remote_plugins_list.selectedItems()))

    def _fetch_remote_plugins(self):
        self.github_manager.fetch_plugin_index(self.plugins_repo_edit.text().strip())

    def _on_plugin_index_ready(self, plugin_list):
        self.remote_plugins_list.clear()
        for p in plugin_list:
            item = QListWidgetItem(f"{p['name']} v{p['version']}")
            item.setData(Qt.ItemDataRole.UserRole, p)
            self.remote_plugins_list.addItem(item)

    def _install_selected_remote_plugin(self):
        if item := self.remote_plugins_list.currentItem():
            self._install_plugin_from_url(item.data(Qt.ItemDataRole.UserRole).get('download_url'))

    def _install_plugin_from_url(self, url):
        url, ok = QInputDialog.getText(self, "Install from URL", "Plugin ZIP URL:", text=url)

        if not (url and ok):
            return

        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                r = requests.get(url)
                r.raise_for_status()

                zip_path = os.path.join(temp_dir, "plugin.zip")
                with open(zip_path, 'wb') as f:
                    f.write(r.content)

                ok, msg = self.plugin_manager.install_plugin_from_zip(zip_path)

                (QMessageBox.information if ok else QMessageBox.warning)(self, "Plugin Install", msg)

                if ok:
                    self.restart_needed = True
                    self._populate_all_plugin_lists()

            except Exception as e:
                QMessageBox.critical(self, "Download Error", f"Failed to download or install plugin: {e}")

    def _install_plugin_from_file(self):
        f, _ = QFileDialog.getOpenFileName(self, "Select Plugin Zip", "", "ZIP Archives (*.zip)")
        if f:
            ok, msg = self.plugin_manager.install_plugin_from_zip(f)
            (QMessageBox.information if ok else QMessageBox.warning)(self, "Install Failed", msg)
            if ok:
                self.restart_needed = True
                self._populate_manage_plugins_list()

    def _uninstall_selected_plugin(self):
        if items := self.manage_plugins_list.selectedItems():
            pid = items[0].data(Qt.ItemDataRole.UserRole)
            plugin = self.plugin_manager.plugins.get(pid)
            if QMessageBox.question(self, "Confirm Uninstall",
                                    f"Are you sure you want to uninstall '{plugin.name}'?") == QMessageBox.StandardButton.Yes:
                ok, msg = self.plugin_manager.uninstall_plugin(pid)
                (QMessageBox.information if ok else QMessageBox.warning)(self, "Uninstall Status", msg)
                if ok:
                    self.restart_needed = True
                    self._populate_all_plugin_lists()