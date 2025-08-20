# Koromali/plugins/terminal/terminal_widget.py
import os
import sys
import platform
import subprocess
import shutil
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QMenu, QFileDialog, QApplication,
                             QHBoxLayout, QPushButton, QFrame, QMessageBox, QLabel)
from PyQt6.QtGui import QColor, QFont, QTextCursor, QKeySequence
from PyQt6.QtCore import QProcess, Qt
import qtawesome as qta
from utils.logger import log


class TerminalWidget(QWidget):
    """An interactive terminal widget that runs a native shell process."""

    def __init__(self, koromali_api):
        super().__init__()
        self.api = koromali_api
        self.project_manager = self.api.get_manager("project")
        self.settings = self.api.get_manager("settings")
        self.theme_manager = self.api.get_manager("theme")
        self.main_window = self.api.get_main_window()
        
        self.process = QProcess(self)
        self.input_start_position = 0

        self._setup_ui()
        self._connect_signals()
        self.update_theme()
        self.start_shell()
        self._on_project_changed() # Set initial state

    def _setup_ui(self):
        """Initializes the UI components."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Toolbar for buttons
        toolbar = QFrame()
        toolbar.setObjectName("TerminalToolbar")
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(5, 2, 5, 2)
        toolbar_layout.setSpacing(5)

        self.cwd_label = QLabel()
        self.cwd_label.setObjectName("TerminalCwdLabel")
        toolbar_layout.addWidget(self.cwd_label)
        toolbar_layout.addStretch(1)

        self.create_venv_button = QPushButton(qta.icon('mdi.language-python'), "Create Venv")
        self.activate_venv_button = QPushButton("Activate Venv")
        self.install_reqs_button = QPushButton(qta.icon('mdi.format-list-numbered'), "Install requirements.txt")
        self.remove_venv_button = QPushButton("Remove Venv")
        
        self.stop_button = QPushButton(qta.icon('fa5s.stop-circle'), "Stop Process")
        self.clear_button = QPushButton(qta.icon('fa5s.broom'), "Clear")

        toolbar_layout.addWidget(self.create_venv_button)
        toolbar_layout.addWidget(self.activate_venv_button)
        toolbar_layout.addWidget(self.install_reqs_button)
        toolbar_layout.addWidget(self.remove_venv_button)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        toolbar_layout.addWidget(separator)
        
        toolbar_layout.addWidget(self.stop_button)
        toolbar_layout.addWidget(self.clear_button)
        
        main_layout.addWidget(toolbar)

        # Main terminal text area
        self.output_area = QTextEdit()
        self.output_area.setAcceptRichText(False)
        self.output_area.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        main_layout.addWidget(self.output_area)

    def _connect_signals(self):
        """Connects signals for the process and UI."""
        self.process.readyReadStandardOutput.connect(self._handle_stdout)
        self.process.readyReadStandardError.connect(self._handle_stderr)
        self.process.finished.connect(self._on_process_finished)

        self.project_manager.projects_changed.connect(self._on_project_changed)

        self.clear_button.clicked.connect(self.clear_terminal)
        self.stop_button.clicked.connect(self.stop_process)
        self.create_venv_button.clicked.connect(self._create_venv)
        self.activate_venv_button.clicked.connect(self._activate_venv)
        self.install_reqs_button.clicked.connect(self._install_requirements)
        self.remove_venv_button.clicked.connect(self._remove_venv)
        self.output_area.customContextMenuRequested.connect(self._show_context_menu)
        self.output_area.keyPressEvent = self.keyPressEvent

    def _get_project_venv_paths(self):
        """Returns paths related to the virtual environment for the active project."""
        proj_path = self.project_manager.get_active_project_path()
        if not proj_path: return None, None, None, None

        venv_path = os.path.join(proj_path, "venv")
        is_windows = platform.system() == "Windows"
        scripts_dir = "Scripts" if is_windows else "bin"
        python_exe = "python.exe" if is_windows else "python"
        
        venv_python = os.path.join(venv_path, scripts_dir, python_exe)
        reqs_path = os.path.join(proj_path, "requirements.txt")

        return venv_path, venv_python, reqs_path, proj_path
        
    def _on_project_changed(self):
        """Updates UI and functionality based on the current project."""
        venv_path, _, reqs_path, proj_path = self._get_project_venv_paths()

        venv_exists = bool(venv_path and os.path.isdir(venv_path))
        reqs_exist = bool(reqs_path and os.path.isfile(reqs_path))
        
        self.create_venv_button.setEnabled(proj_path and not venv_exists)
        self.activate_venv_button.setEnabled(venv_exists)
        self.install_reqs_button.setEnabled(venv_exists and reqs_exist)
        self.remove_venv_button.setEnabled(venv_exists)

        dock = self.parent()
        while dock and not isinstance(dock, QWidget if not hasattr(self.main_window, "ClosableDockWidget") else self.main_window.ClosableDockWidget):
            dock = dock.parent()
            
        if dock and proj_path:
            dock.setWindowTitle(f"Terminal - {os.path.basename(proj_path)}")
        elif dock:
            dock.setWindowTitle("Terminal - (No Project)")

        # Restart shell to switch to new project directory
        if self.process.state() == QProcess.ProcessState.Running:
             self.stop_process()
             self.start_shell()
        
    def _run_command(self, cmd_list: list[str]):
        """Writes a command to the running shell process."""
        command = " ".join(f'"{arg}"' if " " in arg else arg for arg in cmd_list) + "\n"
        self._append_text(f"\n> {command}\n")
        self.process.write(command.encode())
        
    def _create_venv(self):
        # Use the same logic as the ScriptRunner plugin to find a suitable Python interpreter
        script_runner_plugin = self.api.get_plugin_instance("script_runner")
        if script_runner_plugin and hasattr(script_runner_plugin, "_find_python_interpreter"):
            python_exe = script_runner_plugin._find_python_interpreter()
        else:
            python_exe = self.settings.get("python_interpreter_path") or shutil.which("python")

        if not python_exe:
             QMessageBox.critical(self, "Python Not Found", "Cannot create virtual environment. No Python interpreter found.")
             return
        self._run_command([python_exe, "-m", "venv", "venv"])

    def _activate_venv(self):
        _, _, _, proj_path = self._get_project_venv_paths()
        is_windows = platform.system() == "Windows"
        activate_script = os.path.join("venv", "Scripts", "activate.bat") if is_windows else os.path.join("venv", "bin", "activate")
        
        self.output_area.setFocus()
        self.output_area.moveCursor(QTextCursor.MoveOperation.End)
        self.output_area.insertPlainText(f"source {activate_script}" if not is_windows else activate_script)
        self._append_text("\n Activation command typed for you. Press Enter to run.", QColor("#33FF33"))
        
    def _install_requirements(self):
        _, venv_python, reqs_path, _ = self._get_project_venv_paths()
        if venv_python and reqs_path and os.path.exists(venv_python) and os.path.exists(reqs_path):
             self._run_command([venv_python, "-m", "pip", "install", "-r", "requirements.txt"])

    def _remove_venv(self):
        venv_path, _, _, _ = self._get_project_venv_paths()
        if not venv_path or not os.path.isdir(venv_path): return

        reply = QMessageBox.question(self, "Confirm Removal", "Are you sure you want to delete the 'venv' directory?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.setDisabled(True)
            self._append_text(f"\nRemoving '{venv_path}'...")
            try:
                shutil.rmtree(venv_path)
                self._append_text("\nVirtual environment removed successfully.\n")
            except Exception as e:
                self._append_text(f"\nError: {e}\n", QColor("red"))
            finally:
                self.setDisabled(False)
                self._on_project_changed()

    def update_theme(self):
        """Applies colors and fonts from the current theme."""
        font = QFont(self.settings.get("font_family"), self.settings.get("font_size"))
        self.output_area.setFont(font)

        colors = self.theme_manager.current_theme_data.get('colors', {})
        bg = colors.get('editor.background', '#1E1E1E')
        fg = colors.get('editor.foreground', '#D4D4D4')
        toolbar_bg = colors.get('sidebar.background', '#252526')
        border = colors.get('input.border', '#3c3c3c')
        comment_color = colors.get('syntax.comment', '#808080')

        self.setStyleSheet(f"""
            TerminalWidget {{ background-color: {bg}; }}
            #TerminalToolbar {{ 
                background-color: {toolbar_bg}; 
                border-bottom: 1px solid {border}; 
            }}
            #TerminalCwdLabel {{
                color: {comment_color};
                padding: 0 5px;
                font-style: italic;
            }}
            QTextEdit {{
                background-color: {bg};
                color: {fg};
                border: none;
                padding: 5px;
            }}
            #TerminalToolbar QFrame {{
                color: {border};
            }}
        """)

    def start_shell(self):
        """Starts the appropriate native shell for the OS."""
        if self.process.state() == QProcess.ProcessState.Running:
            return

        project_path = self.project_manager.get_active_project_path()
        start_dir = project_path if project_path and os.path.isdir(project_path) else os.path.expanduser("~")

        self.cwd_label.setText(f"CWD: {start_dir}")
        self.cwd_label.setToolTip(start_dir)
        self._append_text(f"Starting terminal in: {start_dir}\n")

        shell_cmd, args = "", []
        if platform.system() == "Windows":
            shell_cmd = "cmd.exe"
            args = ["/K", "prompt $P$G"]
        else:
            shell_cmd = os.environ.get("SHELL", "/bin/bash")

        self.process.setWorkingDirectory(start_dir)
        self.process.start(shell_cmd, args)
        log.info(f"Terminal started in '{start_dir}' with shell '{shell_cmd}'.")
        self.output_area.setFocus()

    def keyPressEvent(self, event):
        """Handles user input, sending it to the shell process."""
        cursor = self.output_area.textCursor()

        if cursor.position() < self.input_start_position:
            cursor.setPosition(self.input_start_position)
            self.output_area.setTextCursor(cursor)

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            command = self.output_area.toPlainText()[self.input_start_position:]
            QTextEdit.keyPressEvent(self.output_area, event)
            self.process.write((command + "\n").encode())
            return

        if event.key() == Qt.Key.Key_Backspace:
            if cursor.position() > self.input_start_position:
                QTextEdit.keyPressEvent(self.output_area, event)
            return

        if event.key() == Qt.Key.Key_C and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            self.process.write(b'\x03')
            return

        QTextEdit.keyPressEvent(self.output_area, event)

    def _append_text(self, text, color=None):
        """Appends text to the output, scrolling to the end."""
        cursor = self.output_area.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.output_area.setTextCursor(cursor)

        if color: self.output_area.setTextColor(color)
        self.output_area.insertPlainText(text)
        if color: 
             colors = self.theme_manager.current_theme_data.get('colors', {})
             default_fg = QColor(colors.get('editor.foreground', '#d4d4d4'))
             self.output_area.setTextColor(default_fg)

        self.output_area.verticalScrollBar().setValue(self.output_area.verticalScrollBar().maximum())
        self.input_start_position = self.output_area.textCursor().position()

    def _handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode(errors='ignore')
        self._append_text(data)

    def _handle_stderr(self):
        data = self.process.readAllStandardError().data().decode(errors='ignore')
        colors = self.theme_manager.current_theme_data.get('colors', {})
        error_color = QColor(colors.get('syntax.comment', '#cd5c5c'))
        self._append_text(data, color=error_color)

    def _on_process_finished(self):
        self._append_text("\n[Process finished. Relaunching shell...]\n")
        self.start_shell()

    def _show_context_menu(self, pos):
        """Displays a custom context menu."""
        menu = QMenu()
        menu.addAction(qta.icon('fa5.copy'), "Copy", self.output_area.copy)
        menu.addAction("Paste", self.output_area.paste)
        menu.addSeparator()
        menu.addAction("Copy All", self.copy_all)
        menu.addSeparator()
        menu.addAction(qta.icon('fa5s.file-export'), "Export Session...", self.export_to_file)
        menu.exec(self.output_area.mapToGlobal(pos))

    def copy_all(self):
        QApplication.clipboard().setText(self.output_area.toPlainText())

    def export_to_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export Terminal Session", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(self.output_area.toPlainText())
                log.info(f"Terminal session exported to {path}")
            except Exception as e:
                log.error(f"Failed to export terminal session: {e}")

    def clear_terminal(self):
        self.output_area.clear()
        if platform.system() == "Windows":
            self.process.write(b'cls\n')
        else:
            self.stop_process()
            self.start_shell()

    def stop_process(self):
        if self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            log.info("Stopping terminal process...")
            try:
                self.process.readyReadStandardOutput.disconnect()
                self.process.readyReadStandardError.disconnect()
                self.process.finished.disconnect()
                if hasattr(self.process, 'errorOccurred'):
                    self.process.errorOccurred.disconnect()
            except TypeError:
                pass 
            self.process.kill()
            if not self.process.waitForFinished(2000):
                log.warning("Terminal process did not terminate within 2 seconds of being killed.")

    def closeEvent(self, event):
        """Ensure the shell process is terminated when the widget closes."""
        self.stop_process()
        super().closeEvent(event)