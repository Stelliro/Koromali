# Koromali/plugins/script_runner/plugin_main.py
import os
import sys
import shutil
import platform
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QObject, QProcess, QTimer
from app_core.koromali_api import KoromaliPluginAPI
from .output_panel import OutputPanel
from utils.logger import log


class ScriptRunnerPlugin(QObject):
    """
    A plugin that adds the capability to compile and run scripts for various
    languages directly from the editor.
    """

    def __init__(self, koromali_api: KoromaliPluginAPI):
        super().__init__()
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.output_panel = OutputPanel(
            theme_manager=self.api.get_manager("theme"),
            settings_manager=self.api.get_manager("settings"),
            parent=self.main_window
        )
        self.process = None
        self._current_task_info = {}

        self.RUN_CONFIG = {
            '.py': {'handler': self._run_python_script, 'menu_text': 'Run Python Script', 'shortcut': 'F5',
                    'icon': 'mdi.language-python'},
            '.js': {'handler': self._run_node_script, 'menu_text': 'Run JS File', 'shortcut': 'Ctrl+F5',
                    'icon': 'mdi.language-javascript'},
            '.cpp': {'handler': self._compile_run_cpp, 'menu_text': 'Compile & Run C++', 'shortcut': 'F6',
                     'icon': 'mdi.language-cpp'},
            '.c': {'handler': self._compile_run_cpp, 'menu_text': 'Compile & Run C', 'shortcut': 'F6',
                   'icon': 'mdi.language-cpp'},
            '.cs': {'handler': self._compile_run_csharp, 'menu_text': 'Compile & Run C#', 'shortcut': 'F7',
                    'icon': 'mdi.language-csharp'},
        }
        self.run_actions = {}
        self._setup_ui()
        self._connect_signals()
        log.info("Script Runner plugin initialized and signals connected.")

    def _setup_ui(self):
        """Creates the 'Output' panel and adds run actions to the menu and toolbar."""
        self.api.add_dock_panel(
            widget=self.output_panel,
            title="Output",
            area_str="bottom",
            icon_name='mdi.console-line'
        )
        for config in self.RUN_CONFIG.values():
            action = self.api.add_menu_action("run", config['menu_text'], config['handler'], config['shortcut'],
                                              config['icon'])
            action.setEnabled(False)
            self.run_actions[config['menu_text']] = action

        self.stop_action = self.api.add_menu_action("run", "Stop Script", self.stop_script, "Ctrl+F2",
                                                    'mdi.stop-circle-outline')
        self.stop_action.setEnabled(False)

        py_action = self.run_actions.get('Run Python Script')
        if py_action:
            self.api.add_toolbar_action(py_action)
        self.api.add_toolbar_action(self.stop_action)

    def _connect_signals(self):
        """Connects signals to handle UI events."""
        self.main_window.tab_widget.currentChanged.connect(self._on_tab_changed)
        QTimer.singleShot(100, lambda: self._on_tab_changed(self.main_window.tab_widget.currentIndex()))
        self.main_window.theme_changed_signal.connect(self.output_panel.update_theme)

    def _on_tab_changed(self, indexx: int):
        """Updates the enabled state of run actions based on the current file type."""
        log.debug(f"ScriptRunner: Tab changed to indexx {indexx}.")
        active_ext = None

        widget = self.main_window.tab_widget.widget(indexx)
        if widget and hasattr(widget, 'filepath') and widget.filepath:
            _, active_ext = os.path.splitext(widget.filepath)
            log.debug(f"ScriptRunner: Filepath found with extension '{active_ext}'.")
        else:
            log.debug(f"ScriptRunner: Current tab widget at indexx {indexx} has no 'filepath' attribute or is None.")

        for ext, config in self.RUN_CONFIG.items():
            action = self.run_actions.get(config['menu_text'])
            if action:
                is_enabled = (active_ext is not None and ext == active_ext)
                action.setEnabled(is_enabled)

    def stop_script(self):
        """Terminates the currently running script process."""
        if self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            self.output_panel.append_output("[Runner] Terminating process...\n", is_error=True)
            self.process.terminate()
            if not self.process.waitForFinished(1000):
                self.process.kill()
                self.output_panel.append_output("[Runner] Process killed.\n", is_error=True)
        else:
            self._on_run_finished(-1)

    def _get_current_filepath(self) -> str | None:
        """
        Gets the filepath of the currently active editor tab, saving it first
        if it has been modified.
        """
        widget = self.main_window.tab_widget.currentWidget()
        if not widget or not hasattr(widget, 'filepath') or not widget.filepath:
            log.warning("ScriptRunner: Cannot run script, current tab has no valid filepath.")
            self.api.show_message("info", "Save File", "Please save the file before running.")
            return None

        if hasattr(widget, 'original_hash') and self.main_window._is_editor_modified(widget):
            log.info(f"ScriptRunner: Saving modified file '{widget.filepath}' before running.")
            self.main_window._action_save_file(editor_widget=widget)

        return widget.filepath

    def run_specific_script(self, filepath: str):
        """Runs a script from a given path, typically triggered by a context menu."""
        ext = os.path.splitext(filepath)[1].lower()
        if handler := next((c['handler'] for c_ext, c in self.RUN_CONFIG.items() if c_ext == ext), None):
            handler(filepath=filepath)
        else:
            self.api.show_message("warning", "Unsupported File Type", f"No run configuration for '{ext}' files.")

    def _find_python_interpreter(self) -> str:
        """Intelligently finds the best Python executable for running scripts."""
        settings_manager = self.api.get_manager("settings")
        user_path = settings_manager.get("python_interpreter_path", "").strip()
        if user_path and os.path.exists(user_path) and "Koromali.exe" not in user_path:
            log.info(f"ScriptRunner: Using user-defined interpreter: {user_path}")
            return user_path

        if getattr(sys, 'frozen', False):
            local_python_path = os.path.join(os.path.dirname(sys.executable), "python.exe")
            if os.path.exists(local_python_path):
                log.info(f"ScriptRunner: Found local python.exe in frozen app dir: {local_python_path}")
                return local_python_path

        if not getattr(sys, 'frozen', False):
            if "Koromali.exe" not in sys.executable:
                log.info(f"ScriptRunner: Running from source, using sys.executable: {sys.executable}")
                return sys.executable

        system_python = shutil.which("python")
        if system_python and "Koromali.exe" not in system_python:
            log.info(f"ScriptRunner: Found system python on PATH: {system_python}")
            return system_python

        log.error("ScriptRunner: Could not find a suitable Python interpreter.")
        return ""

    def _run_python_script(self, filepath: str = None):
        """Handles the logic for executing a Python script."""
        filepath = filepath or self._get_current_filepath()
        if not filepath:
            return
        interpreter_path = self._find_python_interpreter()
        if not interpreter_path:
            self.api.show_message("critical", "Python Not Found",
                                  "Could not find a Python interpreter. Please set one in Preferences.")
            return

        self._current_task_info = {'name': 'Python Script', 'source_path': filepath}
        self._start_process(interpreter_path, [filepath])

    def _run_node_script(self, filepath: str = None):
        """Handles the logic for executing a JavaScript file with Node.js."""
        filepath = filepath or self._get_current_filepath()
        if not filepath:
            return
        node_path = shutil.which("node")
        if not node_path:
            self.api.show_message("critical", "Node.js Not Found", "Could not find 'node' on your system PATH.")
            return

        self._current_task_info = {'name': 'Node.js Script', 'source_path': filepath}
        self._start_process(node_path, [filepath])

    def _compile_run_cpp(self, filepath: str = None):
        """Compiles and then runs a C++ or C source file."""
        source_path = filepath or self._get_current_filepath()
        if not source_path:
            return
        compiler_path = shutil.which("g++") or shutil.which("cl")
        if not compiler_path:
            self.api.show_message("critical", "Compiler Not Found", "No C++ compiler (g++ or cl.exe) found on PATH.")
            return

        source_dir = os.path.dirname(source_path)
        base_name = os.path.splitext(os.path.basename(source_path))[0]
        exe_path = os.path.join(source_dir, f"{base_name}.exe" if platform.system() == "Windows" else base_name)

        if "g++" in os.path.basename(compiler_path):
            args = [source_path, "-o", exe_path, "-std=c++17", "-Wall"]
        else:  # cl.exe
            args = [source_path, f"/Fe:{exe_path}", "/EHsc"]

        self._current_task_info = {'name': 'C++ Compilation', 'type': 'compile', 'runner_path': exe_path,
                                   'source_path': source_path}
        self._start_process(compiler_path, args)

    def _compile_run_csharp(self, filepath: str = None):
        """Compiles and then runs a C# source file."""
        source_path = filepath or self._get_current_filepath()
        if not source_path:
            return
        compiler_path = shutil.which("csc")
        if not compiler_path:
            self.api.show_message("critical", "C# Compiler Not Found", "C# compiler (csc.exe) not found on PATH.")
            return

        base_name = os.path.splitext(os.path.basename(source_path))[0]
        exe_path = os.path.join(os.path.dirname(source_path), f"{base_name}.exe")

        args = [f"/out:{exe_path}", source_path]
        self._current_task_info = {'name': 'C# Compilation', 'type': 'compile', 'runner_path': exe_path,
                                   'source_path': source_path}
        self._start_process(compiler_path, args)

    def _start_process(self, program: str, args: list):
        """Generic method to start a process and display its output."""
        if self.process and self.process.state() != QProcess.ProcessState.NotRunning:
            self.output_panel.append_output("[Runner] A process is already running.", is_error=True)
            return

        self.output_panel.clear_output()
        self.output_panel.append_output(f"[{self._current_task_info.get('name', 'Process')}] Starting...\n")
        self.output_panel.append_output(f"> {os.path.basename(program)} {' '.join(args)}\n\n")

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self._handle_stdout)
        self.process.readyReadStandardError.connect(self._handle_stderr)
        self.process.finished.connect(self._handle_finished)

        script_path = self._current_task_info.get('source_path', args[0])
        self.process.setWorkingDirectory(os.path.dirname(script_path))

        self.stop_action.setEnabled(True)
        self.process.start(program, args)

    def _handle_stdout(self):
        """Handles standard output from the running process."""
        if self.process:
            self.output_panel.append_output(
                self.process.readAllStandardOutput().data().decode(errors='replace'))

    def _handle_stderr(self):
        """Handles standard error from the running process."""
        if self.process:
            self.output_panel.append_output(
                self.process.readAllStandardError().data().decode(errors='replace'), is_error=True)

    def _handle_finished(self, exit_code, exit_status):
        """Handles the completion of a process, including compile-then-run logic."""
        task_name = self._current_task_info.get('name', 'Process')
        task_type = self._current_task_info.get('type')

        if task_type == 'compile':
            runner_path = self._current_task_info.get('runner_path')
            if exit_code == 0:
                self.output_panel.append_output(f"\n[{task_name}] Compilation successful.\n")
                execution_name = os.path.basename(runner_path)
                self._current_task_info = {'name': f"{execution_name} Execution", 'type': 'run',
                                           'runner_path': runner_path, 'source_path': runner_path}
                self._start_process(runner_path, [])
            else:
                self.output_panel.append_output(f"\n[{task_name}] Compilation failed.\n", is_error=True)
                self._on_run_finished(exit_code)
        else:
            self.output_panel.append_output(f"\n[{task_name}] Finished with exit code {exit_code}.\n")
            runner_path = self._current_task_info.get('runner_path')
            if runner_path and os.path.exists(runner_path) and not runner_path.endswith(('.py', '.js')):
                try:
                    os.remove(runner_path)
                    log.info(f"Removed temporary executable: {runner_path}")
                except OSError as e:
                    self.output_panel.append_output(f"Could not remove temporary file: {e}\n", is_error=True)
            self._on_run_finished(exit_code)

    def _on_run_finished(self, exit_code):
        """Final cleanup after a process run is fully complete."""
        self.stop_action.setEnabled(False)
        self.process = None
        self._current_task_info = {}
        self._on_tab_changed(self.main_window.tab_widget.currentIndex())


def initialize(koromali_api: KoromaliPluginAPI):
    return ScriptRunnerPlugin(koromali_api)