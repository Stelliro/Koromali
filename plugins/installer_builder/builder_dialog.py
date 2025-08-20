import os
import webbrowser
from pathlib import Path
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QWidget, QFormLayout, QLineEdit,
                             QPushButton, QTextEdit, QMessageBox, QDialogButtonBox,
                             QHBoxLayout, QFileDialog, QGroupBox, QLabel, QCheckBox)
from PyQt6.QtCore import pyqtSlot, QRunnable, QObject, pyqtSignal, QThreadPool
from PyQt6.QtGui import QFont, QCursor
import qtawesome as qta
from .build_logic import BuildLogic
from utils.helpers import get_base_path
from app_core.config import APP_NAME, ORG_NAME

class WorkerSignals(QObject):
    log_message = pyqtSignal(str, str)
    finished = pyqtSignal(bool, str)

class BuildWorker(QRunnable):
    def __init__(self, config: dict):
        super().__init__()
        self.config = config
        self.signals = WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        self.logic = BuildLogic(self.signals.log_message.emit)
        success, message = self.logic.run_full_build(self.config)
        self.signals.finished.emit(success, message)

class BuilderDialog(QDialog):
    """The UI for the Installer Builder plugin."""
    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.api = api
        self.settings = api.get_manager("settings")
        self.threadpool = QThreadPool()
        
        self.setWindowTitle("Application Installer Builder")
        self.setMinimumSize(800, 700)
        self.main_layout = QVBoxLayout(self)

        self._setup_ui()
        self._load_settings()

    def _setup_ui(self):
        main_group = QGroupBox("1. Application Details")
        form = QFormLayout(main_group)
        self.app_name_edit = QLineEdit()
        self.version_edit = QLineEdit()
        self.author_edit = QLineEdit()
        self.project_root_dir_edit = QLineEdit()
        self.main_exe_edit = QLineEdit("Koromali.exe")
        
        form.addRow("<b>Application Name:</b>", self.app_name_edit)
        form.addRow("<b>Version:</b>", self.version_edit)
        form.addRow("<b>Author/Company:</b>", self.author_edit)
        form.addRow("<b>Project Root Directory:</b>", self._create_browse_field(self.project_root_dir_edit, "Select Project Root Folder", is_file=False))
        form.addRow("<b>Main Executable Name:</b>", self.main_exe_edit)
        self.main_layout.addWidget(main_group)

        options_group = QGroupBox("2. Installer Options")
        opt_form = QFormLayout(options_group)
        self.desktop_sc_check = QCheckBox("Create Desktop Shortcut"); self.desktop_sc_check.setChecked(True)
        self.startmenu_sc_check = QCheckBox("Create Start Menu Shortcuts"); self.startmenu_sc_check.setChecked(True)
        self.install_tray_app_check = QCheckBox("Include System Tray Application"); self.install_tray_app_check.setChecked(True)
        self.install_extra_themes_check = QCheckBox("Include Extra Community Themes"); self.install_extra_themes_check.setChecked(True)
        self.license_path_edit = QLineEdit()
        self.installer_icon_edit = QLineEdit()
        
        opt_form.addRow("Shortcuts:", self._create_hbox_layout([self.desktop_sc_check, self.startmenu_sc_check]))
        opt_form.addRow("Components:", self._create_hbox_layout([self.install_tray_app_check, self.install_extra_themes_check]))
        opt_form.addRow("License File:", self._create_browse_field(self.license_path_edit, "Select License File (*.txt *.md)"))
        opt_form.addRow("Installer Icon (.ico):", self._create_browse_field(self.installer_icon_edit, "Select Icon File (*.ico)"))
        self.main_layout.addWidget(options_group)

        paths_group = QGroupBox("3. Build Paths")
        path_form = QFormLayout(paths_group)
        self.output_dir_edit = QLineEdit()
        self.nsis_path_edit = QLineEdit()
        self.nsi_template_edit = QLineEdit()
        path_form.addRow("<b>Installer Output Directory:</b>", self._create_browse_field(self.output_dir_edit, "Select Output Directory", is_file=False))
        path_form.addRow("<b>NSIS Path (makensis.exe):</b>", self._create_browse_field(self.nsis_path_edit, "Select NSIS Executable"))
        path_form.addRow("<b>NSIS Template (.nsi):</b>", self._create_browse_field(self.nsi_template_edit, "Select NSIS Template (*.nsi)"))
        self.main_layout.addWidget(paths_group)

        log_group = QGroupBox("4. Build Log"); log_layout = QVBoxLayout(log_group)
        self.log_output = QTextEdit(); self.log_output.setReadOnly(True)
        log_layout.addWidget(self.log_output)
        self.main_layout.addWidget(log_group, 1)

        buttons = QDialogButtonBox()
        self.start_button = buttons.addButton("Start Build", QDialogButtonBox.ButtonRole.ActionRole)
        self.close_button = buttons.addButton(QDialogButtonBox.StandardButton.Close)
        self.start_button.clicked.connect(self._start_build)
        self.close_button.clicked.connect(self.reject)
        self.main_layout.addWidget(buttons)

    def _create_browse_field(self, line_edit, title, is_file=True):
        widget, layout = QWidget(), QHBoxLayout(); layout.setContentsMargins(0,0,0,0)
        layout.addWidget(line_edit); btn = QPushButton("..."); btn.setFixedWidth(40)
        btn.clicked.connect(lambda: self._browse(line_edit, title, is_file))
        layout.addWidget(btn)
        widget.setLayout(layout)
        return widget
    
    def _create_hbox_layout(self, widgets: list) -> QWidget:
        widget, layout = QWidget(), QHBoxLayout(); layout.setContentsMargins(0,0,0,0)
        for w in widgets: layout.addWidget(w)
        layout.addStretch()
        return widget

    def _browse(self, line_edit, title, is_file):
        start_dir = self.project_root_dir_edit.text() or str(Path.home())
        if is_file: path, _ = QFileDialog.getOpenFileName(self, title, start_dir)
        else: path = QFileDialog.getExistingDirectory(self, title, start_dir)
        if path: line_edit.setText(os.path.normpath(path))
        
    def _collect_and_validate_config(self):
        config = {
            "metadata": {
                "app_name": self.app_name_edit.text().strip(), 
                "version": self.version_edit.text().strip(), 
                "author": self.author_edit.text().strip(), 
                "main_exe": self.main_exe_edit.text().strip()
            },
            "build": {
                "project_root_dir": self.project_root_dir_edit.text().strip(),
                "output_dir": self.output_dir_edit.text().strip(), 
                "nsis_path": self.nsis_path_edit.text().strip(), 
                "nsi_template_path": self.nsi_template_edit.text().strip(),
                "license_path": self.license_path_edit.text().strip(), 
                "installer_icon_path": self.installer_icon_edit.text().strip(),
                "desktop_shortcut": self.desktop_sc_check.isChecked(), 
                "start_menu_shortcut": self.startmenu_sc_check.isChecked(),
                "install_tray_app": self.install_tray_app_check.isChecked(),
                "install_extra_themes": self.install_extra_themes_check.isChecked()
            }
        }
        
        required_fields = {
            ("metadata", "app_name"): "Application Name",
            ("metadata", "version"): "Version",
            ("build", "project_root_dir"): "Project Root Directory",
            ("build", "output_dir"): "Installer Output Directory",
            ("build", "nsis_path"): "NSIS Path",
            ("build", "nsi_template_path"): "NSIS Template"
        }

        for (section, key), name in required_fields.items():
            if not config[section].get(key):
                QMessageBox.warning(self, "Missing Information", f"The field '{name}' is required.")
                return None
        return config

    def _start_build(self):
        config = self._collect_and_validate_config()
        if not config: return
        self._save_settings(config)
        self.log_output.clear()

        worker = BuildWorker(config)
        worker.signals.log_message.connect(self.add_log_message)
        worker.signals.finished.connect(self.on_build_finished)
        self.threadpool.start(worker)

    def on_build_finished(self, success, message):
        if success: QMessageBox.information(self, "Build Complete", message)
        else: QMessageBox.critical(self, "Build Failed", message)

    def add_log_message(self, message, color_hex):
        safe_message = message.replace('<', '&lt;').replace('>', '&gt;')
        self.log_output.append(f"<span style='color:{color_hex}; font-family: Consolas;'>{safe_message}</span>")
    
    def _load_settings(self):
        base_path = get_base_path()
        self.app_name_edit.setText(APP_NAME)
        self.author_edit.setText(ORG_NAME)
        self.version_edit.setText(self.api.get_main_window()._get_current_version_string())
        
        self.project_root_dir_edit.setText(self.settings.get("builder_project_root", base_path))
        self.output_dir_edit.setText(self.settings.get("builder_last_out_dir", os.path.join(base_path, "dist")))
        self.nsis_path_edit.setText(self.settings.get("builder_nsis_path", ""))
        self.nsi_template_edit.setText(self.settings.get("builder_nsi_template", os.path.join(base_path, "assets", "template.nsi")))
        self.license_path_edit.setText(self.settings.get("builder_license_path", os.path.join(base_path, "LICENSE.md")))
        self.installer_icon_edit.setText(self.settings.get("builder_installer_icon", os.path.join(base_path, "assets", "koromali.ico")))

    def _save_settings(self, config):
        self.settings.set("builder_nsis_path", config['build']['nsis_path'])
        self.settings.set("builder_nsi_template", config['build']['nsi_template_path'])
        self.settings.set("builder_last_out_dir", config['build']['output_dir'])
        self.settings.set("builder_project_root", config['build']['project_root_dir'])
        self.settings.set("builder_license_path", config['build']['license_path'])
        self.settings.set("builder_installer_icon", config['build']['installer_icon_path'])