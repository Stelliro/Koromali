# Koromali/app_core/completion_manager.py
import os
import sys
import shutil
import html
from typing import Any, Optional, TYPE_CHECKING
from PyQt6.QtCore import QObject, QThread, pyqtSignal
import jedi
from .settings_manager import SettingsManager
from utils.logger import log

if TYPE_CHECKING:
    from .theme_manager import ThemeManager


def find_python_interpreter_for_jedi(settings: SettingsManager) -> str:
    """
    Intelligently finds the best Python executable for Jedi to use.
    This now accepts a settings_manager instance.
    """
    user_path = settings.get("python_interpreter_path")
    if (user_path and
            os.path.exists(user_path) and
            "Koromali.exe" not in user_path):
        log.info(f"Jedi: Using user-defined interpreter: {user_path}")
        return user_path

    if getattr(sys, 'frozen', False):
        frozen_dir = os.path.dirname(sys.executable)
        local_python_path = os.path.join(frozen_dir, "python.exe")
        if os.path.exists(local_python_path):
            log.info(
                "Jedi: Found local python.exe in frozen app dir: "
                f"{local_python_path}"
            )
            return local_python_path

    if not getattr(sys, 'frozen', False):
        if "Koromali.exe" not in sys.executable:
            log.info(
                "Jedi: Running from source, using sys.executable: "
                f"{sys.executable}"
            )
            return sys.executable

    system_python = shutil.which("python")
    if system_python and "Koromali.exe" not in system_python:
        log.warning(
            "Jedi: Falling back to system python on PATH: "
            f"{system_python}"
        )
        return system_python

    log.error("Jedi: Could not find a suitable Python interpreter.")
    return ""


class JediWorker(QObject):
    completions_ready = pyqtSignal(list)
    definition_ready = pyqtSignal(str, int, int)
    signature_ready = pyqtSignal(object)

    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.settings = settings_manager
        self.project: Optional[jedi.Project] = None

    def set_project(self, project_path: str):
        try:
            python_executable = find_python_interpreter_for_jedi(self.settings)
            if not python_executable:
                log.error(
                    "JediWorker could not be initialized: No valid "
                    "Python interpreter found."
                )
                self.project = None
                return

            if project_path and os.path.isdir(project_path):
                self.project = jedi.Project(
                    path=project_path,
                    environment_path=python_executable
                )
                log.info(
                    f"Jedi context set to project: {project_path} with "
                    f"interpreter: {python_executable}"
                )
            else:
                env = jedi.create_environment(python_executable, safe=False)
                self.project = jedi.Project(
                    os.path.expanduser("~"), environment=env
                )
                log.info(
                    "Jedi context set to default environment with "
                    f"interpreter: {python_executable}"
                )
        except Exception as e:
            log.error(f"Failed to initialize Jedi project: {e}", exc_info=True)
            self.project = None

    def get_completions(self, source: str, line: int, col: int, filepath: str):
        if not self.project:
            self.completions_ready.emit([])
            return
        try:
            script = jedi.Script(code=source, path=filepath, project=self.project)
            completions = script.complete(line=line, column=col)
            completion_data = [{
                'name': c.name, 'type': c.type,
                'description': c.description, 'docstring': c.docstring(raw=True)
            } for c in completions]
            self.completions_ready.emit(completion_data)
        except Exception as e:
            log.error(f"Error getting Jedi completions: {e}", exc_info=False)
            self.completions_ready.emit([])

    def get_definition(self, source: str, line: int, col: int, filepath: str):
        if not self.project:
            self.definition_ready.emit(None, -1, -1)
            return
        try:
            script = jedi.Script(code=source, path=filepath, project=self.project)
            definitions = script.goto(line=line, column=col)
            if definitions:
                d = definitions[0]
                self.definition_ready.emit(str(d.module_path), d.line, d.column)
            else:
                self.definition_ready.emit(None, -1, -1)
        except Exception as e:
            log.error(f"Error getting Jedi definition: {e}", exc_info=False)
            self.definition_ready.emit(None, -1, -1)

    def get_signature(self, source: str, line: int, col: int, filepath: str):
        if not self.project:
            self.signature_ready.emit(None)
            return
        try:
            script = jedi.Script(code=source, path=filepath, project=self.project)
            signatures = script.get_signatures(line=line, column=col)
            self.signature_ready.emit(signatures[0] if signatures else None)
        except Exception as e:
            log.error(f"Error getting Jedi signature: {e}", exc_info=False)
            self.signature_ready.emit(None)


class CompletionManager(QObject):
    completions_available = pyqtSignal(list)
    definition_found = pyqtSignal(str, int, int)
    hover_tip_ready = pyqtSignal(str)

    _completions_requested = pyqtSignal(str, int, int, str)
    _definition_requested = pyqtSignal(str, int, int, str)
    _signature_requested = pyqtSignal(str, int, int, str)
    _project_path_changed = pyqtSignal(str)

    def __init__(self, settings_manager: SettingsManager, theme_manager: 'ThemeManager', parent: Optional[QObject] = None):
        super().__init__(parent)
        self.settings = settings_manager
        self.theme_manager = theme_manager
        self.thread = QThread()
        self.worker = JediWorker(self.settings)
        self.worker.moveToThread(self.thread)

        self._completions_requested.connect(self.worker.get_completions)
        self._definition_requested.connect(self.worker.get_definition)
        self._signature_requested.connect(self.worker.get_signature)
        self._project_path_changed.connect(self.worker.set_project)

        self.worker.completions_ready.connect(self.completions_available)
        self.worker.definition_ready.connect(self.definition_found)
        self.worker.signature_ready.connect(self._format_signature_for_tooltip)

        self.thread.start()
        log.info("CompletionManager background thread started.")

    def update_project_path(self, project_path: str):
        self._project_path_changed.emit(project_path)

    def request_completions(self, source: str, line: int, col: int, filepath: str):
        self._completions_requested.emit(source, line, col, filepath)

    def request_definition(self, source: str, line: int, col: int, filepath: str):
        self._definition_requested.emit(source, line, col, filepath)

    def request_signature(self, source: str, line: int, col: int, filepath: str):
        self._signature_requested.emit(source, line, col, filepath)

    def _format_signature_for_tooltip(self, signature: Optional[Any]):
        if not signature:
            self.hover_tip_ready.emit("")
            return

        try:
            colors = self.theme_manager.current_theme_data.get('colors', {})
            bg = colors.get('menu.background', '#2b2b2b')
            fg = colors.get('editor.foreground', '#a9b7c6')
            accent = colors.get('syntax.functionName', '#88c0d0')
            doc_fg = colors.get('syntax.comment', '#88929b')
            border = colors.get('input.border', '#555555')

            params_str = ', '.join(p.description for p in signature.params)
            header = f"def {signature.name}({params_str})"
            docstring = signature.docstring(raw=True).strip()

            doc_html = html.escape(docstring)
            doc_html = f"<pre style='white-space: pre-wrap; margin: 0; padding: 0; font-family: inherit;'>{doc_html}</pre>"

            tooltip_html = f"""
                <div style='background-color: {bg}; color: {fg};
                            font-family: Consolas, "Courier New", monospace;
                            font-size: 10pt; padding: 8px; border-radius: 4px;
                            border: 1px solid {border};'>
                    <b style='color: {accent};'>{header}</b>
            """
            if docstring:
                tooltip_html += (f"<hr style='border-color: {border}; border-style: solid; margin: 6px 0;' />"
                                 f"<div style='color: {doc_fg};'>{doc_html}</div>")
            tooltip_html += "</div>"
            self.hover_tip_ready.emit(tooltip_html.strip())
        except Exception as e:
            log.error(f"Error formatting signature tooltip: {e}", exc_info=False)
            self.hover_tip_ready.emit("")

    def shutdown(self):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            if not self.thread.wait(3000):
                self.thread.terminate()