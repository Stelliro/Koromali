# Koromali/plugins/ai_quick_actions/plugin_main.py
from functools import partial
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal
from app_core.koromali_api import KoromaliPluginAPI
from plugins.ai_suite.api_client import ApiClient
from plugins.ai_suite.ai_response_dialog import AIResponseDialog

class AIWorker(QRunnable):
    class Signals(QObject):
        finished = pyqtSignal(bool, str)

    def __init__(self, api_client, provider, model, system_prompt, user_prompt):
        super().__init__()
        self.api_client, self.provider, self.model = api_client, provider, model
        self.system_prompt, self.user_prompt = system_prompt, user_prompt
        self.signals = self.Signals()

    def run(self):
        success, response = self.api_client.send_request(
            self.provider, self.model, self.system_prompt, self.user_prompt)
        self.signals.finished.emit(success, response)

class AIQuickActionsPlugin:
    ACTIONS = [{"name": "Explain this code", "icon": "fa5s.question-circle", "system": "You are an expert developer. Explain the following code snippet clearly and concisely. Describe its purpose, inputs, and outputs.", "user": "Please explain this code:\n\n```python\n{selected_code}\n```"}, {"name": "Suggest a refactoring", "icon": "fa5s.magic", "system": "You are a senior developer focused on writing clean, efficient, and maintainable Python code. Refactor the following code snippet, explaining the key improvements you made.", "user": "Please refactor this code:\n\n```python\n{selected_code}\n```"}, {"name": "Find potential bugs", "icon": "fa5s.bug", "system": "You are a quality assurance expert. Analyze the following code for potential bugs, logical errors, or edge cases that might not be handled correctly.", "user": "Please find potential bugs in this code:\n\n```python\n{selected_code}\n```"}]

    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        settings = self.api.get_manager("settings")
        self.api_client = ApiClient(settings)
        self.thread_pool = QThreadPool()

        # Create a dedicated "AI" menu if it doesn't exist
        ai_menu = self.api.get_menu("ai")
        if not ai_menu:
            ai_menu = self.main_window.menuBar().addMenu("AI")
            setattr(self.main_window, "ai_menu", ai_menu)

        for config in self.ACTIONS:
            self.api.add_menu_action(
                "ai", config["name"], partial(self._run_action, config), icon_name=config["icon"])

    def _run_action(self, config):
        editor = self.main_window.tab_widget.currentWidget()
        if not hasattr(editor, 'text_area'):
            self.api.show_message("info", "No Editor", "Please open a file in an editor tab to use AI actions.")
            return

        text = editor.text_area.textCursor().selectedText()
        if not text:
            self.api.show_message("info", "No Text Selected", "Please select some code to use this AI action.")
            return

        provider = "OpenAI"
        if not self.api_client.get_api_key(provider):
            QMessageBox.warning(self.main_window, "API Key Missing",
                                f"API Key for {provider} not found. Please add it via Tools -> Manage API Keys...")
            return

        models = self.api_client.PROVIDER_CONFIG.get(provider, {}).get("models", [])
        if not models:
            QMessageBox.warning(
                self.main_window,
                "No Models Configured",
                f"No models are listed for provider {provider}.",
            )
            return
        # Prefer a user override when present; otherwise first configured model.
        settings = self.api.get_manager("settings")
        preferred = (settings.get("ai_default_model", "") or "").strip() if settings else ""
        model = preferred if preferred in models else models[0]

        self.api.show_status_message(f"Sending selection to {model}...")
        worker = AIWorker(
            self.api_client,
            provider,
            model,
            config["system"],
            config["user"].format(selected_code=text),
        )
        worker.signals.finished.connect(self._on_action_finished)
        self.thread_pool.start(worker)

    def _on_action_finished(self, success, response):
        self.api.show_status_message("AI response received.", 2000)
        if success:
            dialog = AIResponseDialog(response, self.main_window)
            dialog.exec()
        else:
            QMessageBox.critical(self.main_window, "API Error", response)

def initialize(koromali_api: KoromaliPluginAPI):
    return AIQuickActionsPlugin(koromali_api)