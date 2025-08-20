# /plugins/corvus_integration/corvus_chat_widget.py
import os
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QHBoxLayout,
                             QPushButton, QFrame)
from PyQt6.QtGui import QFont, QTextCursor, QColor
from PyQt6.QtCore import QRunnable, QObject, pyqtSignal, QThreadPool
import qtawesome as qta
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log

# Attempt to import the Corvus assistant. Handle gracefully if it fails.
try:
    from corvus_app.assistant import Assistant
    CORVUS_AVAILABLE = True
except ImportError as e:
    log.error(f"Corvus Integration: Could not import Corvus assistant: {e}")
    Assistant = None
    CORVUS_AVAILABLE = False


class CorvusWorker(QRunnable):
    """A worker to run Assistant.process_prompt in the background."""
    class Signals(QObject):
        finished = pyqtSignal(str)
        error = pyqtSignal(str)

    def __init__(self, assistant_instance, prompt):
        super().__init__()
        self.assistant = assistant_instance
        self.prompt = prompt
        self.signals = self.Signals()

    def run(self):
        try:
            response = self.assistant.process_prompt(self.prompt)
            self.signals.finished.emit(response)
        except Exception as e:
            log.error(f"Error in CorvusWorker: {e}", exc_info=True)
            self.signals.error.emit(f"An error occurred while processing your request: {e}")


class CorvusChatWidget(QWidget):
    def __init__(self, api: KoromaliPluginAPI):
        super().__init__()
        self.api = api
        self.theme_manager = api.get_manager("theme")
        self.project_manager = api.get_manager("project")
        self.settings = api.get_manager("settings")
        self.threadpool = QThreadPool()
        self.assistant = Assistant() if CORVUS_AVAILABLE else None

        self._setup_ui()
        self._connect_signals()
        self.update_theme()

        if not CORVUS_AVAILABLE:
            self._set_error_state("Corvus application components could not be found.")

    def _setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setHtml("<i>Corvus Assistant Initialized. Ready for your prompt.</i>")
        
        input_frame = QFrame()
        input_layout = QVBoxLayout(input_frame)
        input_layout.setContentsMargins(0,0,0,0)
        
        self.input_box = QTextEdit()
        self.input_box.setFixedHeight(100)
        self.input_box.setPlaceholderText("Enter your prompt for Corvus...")

        button_bar_layout = QHBoxLayout()
        self.context_button = QPushButton(qta.icon('fa5s.file-import'), "Provide File Context")
        self.send_button = QPushButton(qta.icon('fa5s.paper-plane'), "Send")
        button_bar_layout.addWidget(self.context_button)
        button_bar_layout.addStretch()
        button_bar_layout.addWidget(self.send_button)

        input_layout.addWidget(self.input_box)
        input_layout.addLayout(button_bar_layout)
        
        self.main_layout.addWidget(self.chat_history, 1)
        self.main_layout.addWidget(input_frame)

    def _connect_signals(self):
        self.context_button.clicked.connect(self._provide_context)
        self.send_button.clicked.connect(self._send_chat)

    def _provide_context(self):
        editor = self.api.get_main_window()._get_current_editor()
        if not editor or not editor.filepath:
            self.api.show_message("info", "No File", "Please open a file in the editor to provide its context.")
            return
        file_content = editor.get_text()
        file_name = os.path.basename(editor.filepath)
        lang = os.path.splitext(file_name)[1].lstrip('.')
        context_prompt = (f"Please analyze the following file: `{file_name}`\n\n```{lang}\n{file_content}\n```\n\nMy question is: ")
        self.input_box.setPlainText(context_prompt)
        self.input_box.setFocus()
        cursor = self.input_box.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.input_box.setTextCursor(cursor)

    def _set_error_state(self, message: str):
        self.chat_history.setHtml(f"<b style='color:red;'>Initialization Failed:</b><br>{message}")
        self.input_box.setEnabled(False)
        self.send_button.setEnabled(False)
        self.context_button.setEnabled(False)

    def _send_chat(self):
        if not self.assistant: return
        prompt = self.input_box.toPlainText().strip()
        if not prompt: return
        
        self.input_box.clear()
        self.send_button.setEnabled(False)
        
        formatted_prompt = prompt.replace('\n', '<br>')
        self._append_to_history_html(f"<hr><b>You:</b><br>{formatted_prompt}")
        
        worker = CorvusWorker(self.assistant, prompt)
        worker.signals.finished.connect(self._on_chat_finished)
        worker.signals.error.connect(self._on_chat_error)
        self.threadpool.start(worker)

    def _on_chat_finished(self, response: str):
        formatted_response = response.replace('\n', '<br>')
        self._append_to_history_html(f"<hr><b>Corvus:</b><br>{formatted_response}")
        self.send_button.setEnabled(True)
        self.input_box.setFocus()

    def _on_chat_error(self, error_message: str):
        self._append_to_history_html(f"<b style='color:red;'>Error:</b> {error_message}")
        self.send_button.setEnabled(True)

    def _append_to_history_html(self, html: str):
        cursor = self.chat_history.textCursor(); cursor.movePosition(QTextCursor.MoveOperation.End)
        self.chat_history.setTextCursor(cursor); cursor.insertHtml(html); self.chat_history.ensureCursorVisible()

    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        font = QFont(self.settings.get("font_family"), 10)
        bg, fg, input_bg, border = (colors.get(k, d) for k, d in [
            ('sidebar.background', '#2a3338'), ('editor.foreground', '#d3c6aa'),
            ('editor.background', '#272e33'), ('input.border', '#5f6c6d')])
        
        self.setStyleSheet(f"background-color: {bg};")
        for widget in [self.chat_history, self.input_box]:
            widget.setStyleSheet(f"background-color: {input_bg}; color: {fg}; border: 1px solid {border};")
            widget.setFont(font)