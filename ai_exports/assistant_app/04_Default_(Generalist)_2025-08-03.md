---SYSTEM-PROMPT---

You are an expert software developer. Your task is to modify the user's project based on their instructions.
## Golden Rules
- Your response MUST ONLY contain the complete, updated content for each file that needs to change.
- Enclose each file's content in the standard `### File: /path/to/file.ext` and code block format.
- Do not add any extra commentary, explanations, or summaries outside of the code blocks.
- Each provided file must be complete and correct, including all necessary imports and boilerplate.
- If a file is not being changed, do not include it in the response.
- Ensure file paths are relative to the project root and use forward slashes (e.g., `app_core/main.py`).
- Maintain existing code style, indexntation, and conventions for all unchanged parts of a file.

---USER-PROMPT---

# Project Task...

## Project File Tree:
```
assistant_app
├── assistant_app
│   ├── ui
│   │   └── screens
│   │       ├── conversation_screen.py
│   │       └── models_screen.py
│   ├── logging_config.py
│   └── main.py
├── audio
│   ├── __init__.py
│   └── stt.py
├── cleaner
│   ├── clean.bat
│   └── clean.sh
├── installer
│   ├── __init__.py
│   ├── installer.css
│   └── installer_tui.py
├── llm
│   ├── __init__.py
│   └── gguf_client.py
├── models
│   ├── downloader.py
│   ├── hf_utils.py
│   ├── llm_manager.py
│   └── tts_manager.py
├── plugins
│   ├── __init__.py
│   ├── base.py
│   ├── exit_command.py
│   ├── registry.py
│   └── time_command.py
├── screens
│   └── models_screen.py
├── tts
│   ├── __init__.py
│   └── tts_engine.py
├── ui
│   ├── screens
│   │   ├── __init__.py
│   │   ├── conversation_screen.py
│   │   └── models_screen.py
│   ├── __init__.py
│   ├── tui.css
│   └── tui.py
├── .env.example
├── .gitignore
├── __init__.py
├── app_settings.py
├── assistant.py
├── config.py
├── installer_tui.py
├── logging_config.py
├── main.py
├── README.md
├── requirements.txt
├── run.py
├── start.bat
├── start.sh
└── tui.css
```

## Project Files

### File: `/.env.example`
```example
# Assistant App Configuration
# This file is used as a template to create your .env file on first run.

# The host URL for the Ollama service
OLLAMA_HOST="http://localhost:11434"

# The wake word required to activate the assistant
WAKE_WORD="computer"

# The level of detail for logs. Can be DEBUG, INFO, WARNING, ERROR, CRITICAL.
LOG_LEVEL="INFO"
```

### File: `/.gitignore`
```text
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.env
*.venv
env/
venv/

# IDE specific files
.idea/
.vscode/

# Build artifacts
build/
dist/
*.egg-info/
```

### File: `/README.md`
```md
# CogniCore

CogniCore is a focus and productivity overlay tool designed for a neurodiverse audience. This tool is built to be simple and effective, with a plugin system to extend its functionality.

## Features (Planned)

- **Overlay Mode:** Keeps the application and its plugins always on top of other windows.
- **Plugin System:** Easily install new tools like timers, to-do lists, and more.
- **Simple UI:** A clean and straightforward user interface.

## Getting Started

To get started with CogniCore, clone the repository and run the main application file.
```

### File: `/__init__.py`
```py
# This file makes the 'assistant_app' directory a Python package.
```

### File: `/app_settings.py`
```py
# assistant_app/app_settings.py
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class AppSettings:
    """Manages persistent application settings like active models."""

    def __init__(self, file_path: str = "settings.json"):
        self.file_path = Path(file_path)
        self.defaults = {
            "active_llm_model": None, # Will be a file path to a .gguf file
            "active_tts_model": "tts_models/en/ljspeech/vits" # A default model from Coqui
        }
        self.settings = self._load()

    def _load(self) -> dict:
        """Loads settings from the JSON file, or returns defaults if it doesn't exist."""
        if self.file_path.exists():
            logger.info(f"Loading settings from {self.file_path}")
            with self.file_path.open('r', encoding='utf-8') as f:
                try:
                    loaded_settings = json.load(f)
                    for key, value in self.defaults.items():
                        loaded_settings.setdefault(key, value)
                    return loaded_settings
                except json.JSONDecodeError:
                    logger.error(f"Failed to decode {self.file_path}, using default settings.")
                    return self.defaults.copy()
        else:
            logger.info("Settings file not found, creating with default settings.")
            self.settings = self.defaults.copy()
            self._save()
            return self.settings

    def _save(self):
        """Saves the current settings to the JSON file."""
        try:
            with self.file_path.open('w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4)
            logger.info(f"Settings successfully saved to {self.file_path}")
        except Exception as e:
            logger.error(f"Failed to save settings to {self.file_path}: {e}", exc_info=True)

    def get(self, key: str):
        """Gets a setting value by key."""
        return self.settings.get(key)

    def set(self, key: str, value):
        """Sets a setting value and saves the changes."""
        self.settings[key] = value
        self._save()

settings_manager = AppSettings()
```

### File: `/assistant.py`
```py
# assistant_app/assistant.py
import logging
from pathlib import Path

from .app_settings import settings_manager
from .llm.gguf_client import GGUFClient
from .plugins.registry import CommandRegistry

logger = logging.getLogger(__name__)

class Assistant:
    """
    The brain of the AI assistant. It orchestrates the LLM, command registry,
    and state management.
    """
    def __init__(self):
        self.is_running = True
        self.llm_client = None
        self.command_registry = None
        self.reload()

    def reload(self):
        """Reloads the assistant's components, like the LLM client."""
        logger.info("Reloading assistant components...")
        self.command_registry = CommandRegistry()
        
        active_model_path = settings_manager.get("active_llm_model")
        if active_model_path and Path(active_model_path).exists():
            try:
                self.llm_client = GGUFClient(model_path=active_model_path)
                self.is_running = True
                logger.info("Assistant components reloaded successfully.")
            except Exception as e:
                logger.critical(f"Failed to load GGUF model '{active_model_path}': {e}", exc_info=True)
                self.llm_client = None
                self.is_running = False
        else:
            logger.warning("No active LLM model set or model file not found.")
            self.llm_client = None
            self.is_running = True

    def process_prompt(self, prompt: str) -> str:
        """
        Processes a user prompt and returns the appropriate text response.
        """
        if not self.is_running or self.command_registry is None:
            return "Assistant is not properly initialized. Please restart the application."

        if self.llm_client is None:
             return "No active LLM model. Please set one in the Model Manager (Ctrl+M)."

        logger.info(f"Processing user prompt: '{prompt}'")
        
        if command := self.command_registry.find_command(prompt):
            logger.info(f"User prompt triggered command: {type(command).__name__}")
            return command.execute(self)

        logger.debug("Prompt did not match a command. Sending to LLM.")
        llm_response = self.llm_client.get_completion(prompt)
        logger.info(f"LLM generated response: '{llm_response[:100]}...'")
        
        if command := self.command_registry.find_command(llm_response):
            logger.info(f"LLM response triggered command: {type(command).__name__}")
            return command.execute(self)

        return llm_response
```

### File: `/assistant_app/logging_config.py`
```py
# assistant_app/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
from assistant_app import config

def setup_logging(log_filename="assistant_app.log"):
    """Configures the root logger for the application."""
    
    log_formatter = logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(name)-25.25s] [%(levelname)-8.8s]  %(message)s"
    )
    
    log_file_handler = RotatingFileHandler(
        log_filename, 
        maxBytes=5*1024*1024,
        backupCount=3,
        encoding='utf-8'
    )
    log_file_handler.setFormatter(log_formatter)
    
    root_logger = logging.getLogger()
    
    # Set level on the root logger
    log_level = getattr(config, "LOG_LEVEL", "INFO")
    root_logger.setLevel(log_level)
    
    # Clear existing handlers to prevent duplicate logs
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
        
    root_logger.addHandler(log_file_handler)
    logging.captureWarnings(True)

    logging.info("="*60)
    logging.info(f"Logging configured for '{log_filename}'.")
    logging.info(f"Log Level set to {logging.getLevelName(root_logger.level)}")
    logging.info("="*60)
```

### File: `/assistant_app/main.py`
```py
# assistant_app/main.py
import sys
import logging
import traceback
from datetime import datetime
from pathlib import Path
from rich.console import Console

# Fallback console for pre-TUI errors
_console = Console()

# --- Pre-flight Checks & Setup ---
try:
    # Create essential model directories before any other imports
    Path("tts_models").mkdir(exist_ok=True)
    Path("llm_models").mkdir(exist_ok=True)

    # Set up logging as the very first operation
    # Note: main app logs to "assistant.log", installer logs to "installer.log"
    from assistant_app.logging_config import setup_logging
    setup_logging(log_filename="assistant_app.log")

except Exception:
    # If logging itself fails, we must use the fallback and generate a crash log
    _console.print("[bold red]FATAL: Failed to configure application logging.[/bold red]")
    crash_log_path = Path("crash.log")
    with crash_log_path.open("w", encoding="utf-8") as f:
        f.write(f"--- Assistant App Crash Report (Logging Failure) ---\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("-" * 30 + "\n\n")
        traceback.print_exc(file=f)
    _console.print(f"[bold red]A '{crash_log_path}' has been created. Exiting.[/bold red]")
    sys.exit(1)

logger = logging.getLogger(__name__)

def main():
    """Application entry point. Initializes and runs the Textual UI."""
    try:
        logger.info("Main application starting up.")
        
        # Check if setup is complete
        if not Path("venv/deps_installed.marker").exists():
            logger.error("Dependencies are not installed. Please run the start script.")
            _console.print("[bold red]FATAL: Dependencies not installed. Please run 'start.bat' or './start.sh' again.[/bold red]")
            sys.exit(1)
        
        from assistant_app.ui.tui import AssistantTUI
        
        app = AssistantTUI()
        app.run()
    except Exception:
        logger.critical("A critical unhandled error occurred in the main application.", exc_info=True)
        crash_log_path = Path("crash.log")
        with crash_log_path.open("w", encoding="utf-8") as f:
            f.write(f"--- Assistant App Crash Report ---\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write("-" * 30 + "\n\n")
            traceback.print_exc(file=f)

        _console.print(f"\n[bold red on white] AN UNRECOVERABLE ERROR OCCURRED [/]")
        _console.print(f"[bold red]A '{crash_log_path}' file has been created with the full error details.[/bold red]")
        sys.exit(1)
    finally:
        logger.info("Application shutdown sequence finished.\n\n")

if __name__ == "__main__":
    main()
```

### File: `/assistant_app/ui/screens/conversation_screen.py`
```py
# assistant_app/ui/screens/conversation_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, ListView
# CORRECTED IMPORT: The @work decorator IS IN textual.worker for this version.
from textual.worker import work

from assistant_app import config
from assistant_app.assistant import Assistant
from assistant_app.audio.stt import listen_for_audio
from assistant_app.tts.tts_engine import speak_text
from assistant_app.ui.tui import AssistantResponse, StatusUpdate, ConversationListItem

logger = logging.getLogger(__name__)

class ConversationScreen(Screen):
    """The main conversation screen for the assistant."""
    BINDINGS = [
        ("tab", "toggle_input_mode", "Toggle Input"),
    ]
    
    def __init__(self, assistant: Assistant, **kwargs):
        super().__init__(**kwargs)
        self.assistant = assistant
        self.input_mode = "voice"

    def compose(self) -> ComposeResult:
        yield Header()
        yield ScrollableContainer(ListView(id="conversation"), id="conversation-container")
        yield Input(placeholder="Type your message...", id="text-input", disabled=True)
        yield Footer()

    def on_mount(self) -> None:
        """Called when the screen is first mounted."""
        if self.assistant.is_running:
            self.action_listen_for_wake_word()
        else:
            list_view = self.query_one(ListView)
            list_view.append(
                ConversationListItem(
                    "Assistant failed to initialize. Check active models in Model Manager (Ctrl+M) and logs.",
                    "assistant"
                )
            )

    @work(exclusive=True, group="audio_input")
    def action_listen_for_wake_word(self) -> None:
        """Continuously listens for the wake word."""
        self.app.post_message(StatusUpdate("LISTENING..."))
        logger.debug("Starting wake word listener.")
        while self.input_mode == "voice" and self.assistant.is_running:
            text = listen_for_audio()
            if text is None: continue

            if config.WAKE_WORD in text:
                prompt = text.replace(config.WAKE_WORD, "", 1).strip()
                if prompt:
                    self.app.post_message(StatusUpdate("PROCESSING..."))
                    self.action_process_prompt(prompt)
                else:
                    self.app.post_message(StatusUpdate("Yes?"))
                    self.speak_and_reset_status("Yes?")
                return

    @work(exclusive=True, group="processing")
    def action_process_prompt(self, prompt: str) -> None:
        """Processes the prompt and posts the response."""
        response = self.assistant.process_prompt(prompt)
        self.post_message(AssistantResponse(response, prompt))
        if not self.assistant.is_running: # Exit command might have been triggered
            self.app.exit()
        else:
            self.speak_and_reset_status(response)

    @work(exclusive=True, group="audio_output")
    def speak_and_reset_status(self, text: str) -> None:
        """Speaks text and then restarts the wake word listener if in voice mode."""
        speak_text(text)
        if self.input_mode == "voice":
            self.action_listen_for_wake_word()
        else:
            self.post_message(StatusUpdate("TYPING..."))
    
    def action_toggle_input_mode(self) -> None:
        """Switches between voice and text input modes."""
        text_input = self.query_one("#text-input", Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.disabled = False
            text_input.focus()
            self.post_message(StatusUpdate("TYPING..."))
        else:
            self.input_mode = "voice"
            text_input.disabled = True
            text_input.value = ""
            self.action_listen_for_wake_word()
            
    async def on_input_submitted(self, message: Input.Submitted) -> None:
        """Handles submission from the text input field."""
        prompt = message.value
        if prompt:
            message.input.value = ""
            self.post_message(StatusUpdate("PROCESSING..."))
            self.action_process_prompt(prompt)
        self.set_focus(None)

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        """Receives a response from a worker and adds it to the conversation."""
        list_view = self.query_one(ListView)
        list_view.append(ConversationListItem(message.user_prompt, "user"))
        list_view.append(ConversationListItem(message.text, "assistant"))
        list_view.scroll_end()

    async def on_status_update(self, message: StatusUpdate) -> None:
        """Updates the footer status from a worker."""
        self.query_one(Footer).border_title = message.text
```

### File: `/assistant_app/ui/screens/models_screen.py`
```py
# assistant_app/ui/screens/models_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Input, Button, Static, ProgressBar
# CORRECTED IMPORT: The @work decorator IS IN textual.worker for this version.
from textual.worker import work

from assistant_app.app_settings import settings_manager
from assistant_app.models import llm_manager, tts_manager, hf_utils

logger = logging.getLogger(__name__)

class ModelsScreen(Screen):
    BINDINGS = [
        ("d", "download_selected", "Download"),
        ("s", "set_active", "Set Active"),
        ("delete", "delete_selected", "Delete Selected"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with ScrollableContainer():
            yield Static("LLM Models - Remote", classes="title")
            with Horizontal(classes="input_bar"):
                yield Input(placeholder="HuggingFace Repo (e.g., TheBloke/Llama-2-7B-GGUF)", id="hf-repo-input")
                yield Button("Fetch Files", id="hf-fetch-button")
            yield DataTable(id="hf-files-table", cursor_type="row", classes="model_table")
            
            yield Static("LLM Models - Local", classes="title")
            yield DataTable(id="llm-table", cursor_type="row", classes="model_table")

            yield Static("TTS Models - Local", classes="title")
            yield DataTable(id="tts-local-table", cursor_type="row", classes="model_table")

            yield Static("TTS Models - Remote (Coqui)", classes="title")
            yield DataTable(id="tts-remote-table", cursor_type="row", classes="model_table")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#hf-files-table").add_columns("GGUF File", "URL")
        self.query_one("#llm-table").add_columns("Filename", "Path", "Status")
        self.query_one("#tts-local-table").add_columns("Local TTS Model", "Status")
        self.query_one("#tts-remote-table").add_columns("Available TTS Model")
        
        self.update_llm_table()
        self.update_tts_tables()
        self.fetch_remote_tts_models()
    
    def update_llm_table(self):
        table = self.query_one("#llm-table", DataTable)
        table.clear()
        local_models = llm_manager.get_local_models()
        active_model = settings_manager.get("active_llm_model")
        for model_path in sorted(local_models):
            status = "[bold green](Active)[/]" if str(model_path) == active_model else ""
            table.add_row(model_path.name, str(model_path), status, key=str(model_path))

    def update_tts_tables(self):
        table = self.query_one("#tts-local-table", DataTable)
        table.clear()
        local_models = tts_manager.get_local_models_list()
        active_model = settings_manager.get("active_tts_model")
        for model_name in sorted(local_models):
            status = "[bold green](Active)[/]" if model_name == active_model else ""
            table.add_row(model_name, status, key=model_name)

    @work(exclusive=True, thread=True)
    def fetch_hf_files(self, repo_id: str):
        table = self.query_one("#hf-files-table")
        self.call_from_thread(table.clear)
        self.call_from_thread(setattr, table, 'loading', True)
        files = hf_utils.list_gguf_files_from_repo(repo_id)
        self.call_from_thread(setattr, table, 'loading', False)
        if files:
            for f in files:
                self.call_from_thread(table.add_row, f['filename'], f['url'], key=f['url'])
        else:
            self.call_from_thread(table.add_row, "[red]No GGUF files found or repo is invalid.[/red]", "")
            
    @work(exclusive=True, thread=True)
    def fetch_remote_tts_models(self):
        table = self.query_one("#tts-remote-table")
        self.call_from_thread(setattr, table, 'loading', True)
        models = tts_manager.get_remote_models_list()
        self.call_from_thread(setattr, table, 'loading', False)
        if models:
            for model_name in models:
                self.call_from_thread(table.add_row, model_name, key=model_name)
        else:
            self.call_from_thread(table.add_row, "[red]Could not retrieve remote TTS models.[/red]")

    async def on_button_pressed(self, message: Button.Pressed):
        if message.button.id == "hf-fetch-button":
            repo_id = self.query_one("#hf-repo-input", Input).value
            if repo_id:
                self.fetch_hf_files(repo_id)

    def action_download_selected(self) -> None:
        hf_table = self.query_one("#hf-files-table")
        tts_table = self.query_one("#tts-remote-table")

        try:
            if hf_table.has_focus:
                row_key = hf_table.get_row_key(hf_table.cursor_row)
                filename = hf_table.get_cell(row_key, "GGUF File")
                if row_key and filename:
                    self.app.push_screen(DownloadScreen(url=row_key, filename=filename))
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name:
                    self.app.push_screen(TTSDownloadScreen(model_name=model_name))
        except KeyError:
            logger.warning("Download triggered with no row selected.")

    def action_delete_selected(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")

        try:
            if llm_table.has_focus:
                filepath = llm_table.get_row_key(llm_table.cursor_row)
                if filepath and llm_manager.delete_model(filepath):
                    if settings_manager.get("active_llm_model") == filepath:
                        settings_manager.set("active_llm_model", None)
                    self.update_llm_table()
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name and tts_manager.delete_model(model_name):
                    if settings_manager.get("active_tts_model") == model_name:
                        settings_manager.set("active_tts_model", "tts_models/en/ljspeech/vits")
                    self.update_tts_tables()
        except KeyError:
            logger.warning("Delete triggered with no row selected.")

    def action_set_active(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus:
                row_key = llm_table.get_row_key(llm_table.cursor_row)
                if row_key:
                    settings_manager.set("active_llm_model", row_key)
                    self.update_llm_table()
            elif tts_table.has_focus:
                row_key = tts_table.get_row_key(tts_table.cursor_row)
                if row_key:
                    settings_manager.set("active_tts_model", row_key)
                    self.update_tts_tables()
        except KeyError:
            logger.warning(f"Set Active triggered with no row selected.")

class DownloadScreen(Screen):
    """A modal screen for showing GGUF download progress."""
    
    def __init__(self, url: str, filename: str):
        super().__init__()
        self.url = url
        self.filename = filename

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading: {self.filename}", id="progress-label"),
            Horizontal(
                Static("Starting...", id="progress-stats"),
                classes="stats_bar",
            ),
            ProgressBar(total=100, id="download-progress"),
            id="progress-dialog",
        )
    
    def on_mount(self) -> None:
        self.download_model_file()
    
    def on_download_progress(self, event: str, total_size: int = 0, downloaded: int = 0, message: str = ""):
        def update_ui():
            progress_bar = self.query_one(ProgressBar)
            stats_label = self.query_one("#progress-stats")

            if event == "start":
                progress_bar.total = total_size or 100
                stats_label.update("Connecting...")
            
            elif event == "update":
                progress_bar.update(progress=downloaded)
                total_mb = (progress_bar.total or 0) / (1024 * 1024)
                downloaded_mb = downloaded / (1024 * 1024)
                percent = (downloaded / progress_bar.total * 100) if progress_bar.total else 0
                stats_label.update(f"{downloaded_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)")
            
            elif event == "finish":
                if (models_screen := self.app.get_screen("models")):
                    models_screen.update_llm_table()
                self.app.pop_screen()
            
            elif event == "error":
                self.app.pop_screen()
        
        self.call_from_thread(update_ui)

    @work(exclusive=True, thread=True)
    def download_model_file(self) -> None:
        llm_manager.download_model(self.url, self.filename, self.on_download_progress)

class TTSDownloadScreen(Screen):
    """A modal screen showing a simple busy spinner for TTS downloads."""

    def __init__(self, model_name: str):
        super().__init__()
        self.model_name = model_name

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading TTS Model: {self.model_name}", id="progress-label"),
            Static("This may take a few minutes. Please wait...", id="progress-stats"),
            id="progress-dialog",
        )

    def on_mount(self) -> None:
        self.download_tts_model()

    def on_download_finished(self, event: str, message: str = "") -> None:
        def update_ui():
            if (models_screen := self.app.get_screen("models")):
                models_screen.update_tts_tables()
            self.app.pop_screen()
        
        self.call_from_thread(update_ui)
    
    @work(exclusive=True, thread=True)
    def download_tts_model(self) -> None:
        tts_manager.download_model(self.model_name, self.on_download_finished)
```

### File: `/audio/__init__.py`
```py
# This file makes the 'audio' directory a Python sub-package.
```

### File: `/audio/stt.py`
```py
# assistant_app/audio/stt.py
import speech_recognition as sr

def listen_for_audio() -> str | None:
    """
    Captures audio from the microphone and transcribes it to text.
    Returns the transcribed text in lowercase, or None on error/timeout.
    """
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0
    
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return None # Not an error, just silence or unintelligible noise

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.RequestError:
        # API is unreachable or unresponsive, treat as a failed listen
        return None
    except Exception:
        return None
```

### File: `/cleaner/clean.bat`
```bat
@echo off
setlocal

echo.
echo ============================================================================
echo ==           ASSISTANT APP - FULL PROJECT RESET SCRIPT                    ==
echo ============================================================================
echo.
echo [WARNING] This script will PERMANENTLY DELETE:
echo           - All installed Python dependencies (the 'venv' folder)
echo           - All downloaded LLM and TTS models
echo           - All logs and local configuration files (.env, settings.json)
echo.

REM Get the directory of this script (the 'cleaner' folder)
set "SCRIPT_DIR=%~dp0"
REM Change the working directory to the parent folder (the project root)
cd /d "%SCRIPT_DIR%..\"

:confirm
set /p "choice=This action cannot be undone. Are you sure you want to proceed? (y/n): "
if /i not "%choice%"=="y" goto :end

echo.
echo [INFO] Starting full project cleanup in directory: '%cd%'
echo.

echo [Step 1/9] Uninstalling all dependencies by deleting the Python virtual environment...
if exist "venv" (
    rmdir /s /q venv
    echo [SUCCESS] 'venv' folder and all dependencies have been deleted.
) else (
    echo [INFO] 'venv' folder not found, skipping.
)

echo [Step 2/9] Deleting dependency marker...
if exist "venv\deps_installed.marker" (
    del "venv\deps_installed.marker" >nul 2>nul
)
if exist "deps_installed.marker" (
    del "deps_installed.marker" >nul 2>nul
)

echo [Step 3/9] Deleting downloaded LLM models...
if exist "llm_models" (
    rmdir /s /q llm_models
    echo [SUCCESS] 'llm_models' folder deleted.
) else (
    echo [INFO] 'llm_models' folder not found, skipping.
)

echo [Step 4/9] Deleting downloaded TTS models...
if exist "tts_models" (
    rmdir /s /q tts_models
    echo [SUCCESS] 'tts_models' folder deleted.
) else (
    echo [INFO] 'tts_models' folder not found, skipping.
)

echo [Step 5/9] Deleting local configuration...
if exist ".env" (
    del .env
    echo [SUCCESS] '.env' file deleted.
)
if exist "settings.json" (
    del settings.json
    echo [SUCCESS] 'settings.json' file deleted.
)

echo [Step 6/9] Deleting logs...
if exist "assistant.log" ( del assistant.log )
if exist "assistant_app.log" ( del assistant_app.log )
if exist "installer.log" ( del installer.log )
if exist "crash.log" ( del crash.log )
echo [SUCCESS] Log files deleted.

echo [Step 7/9] Deleting temporary files...
if exist "output.wav" ( del output.wav )
if exist "pip_install.log" ( del pip_install.log )

echo [Step 8/9] Deleting __pycache__ folders...
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" rmdir /s /q "%%d"
)

echo [Step 9/9] Deleting obsolete root files...
if exist "assistant_app.py" ( del assistant_app.py )


echo.
echo ============================================================================
echo.
echo [SUCCESS] Full project cleanup is complete.
echo You can now run 'start.bat' for a completely fresh installation.
echo.

:end
pause
endlocal
```

### File: `/cleaner/clean.sh`
```sh
#!/bin/bash

echo ""
echo "============================================================================"
echo "==            ASSISTANT APP - FULL PROJECT RESET SCRIPT                   =="
echo "============================================================================"
echo ""
echo "[WARNING] This script will PERMANENTLY DELETE:"
echo "          - All installed Python dependencies (the 'venv' folder)"
echo "          - All downloaded LLM and TTS models"
echo "          - All logs and local configuration files (.env, settings.json)"
echo ""

# Get the directory of this script (the 'cleaner' folder)
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
# Change the working directory to the parent folder (the project root)
cd "$SCRIPT_DIR/.."

read -p "This action cannot be undone. Are you sure? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi

echo ""
echo "[INFO] Starting full project cleanup in directory: $(pwd)"
echo ""

echo "[Step 1/9] Uninstalling all dependencies by deleting the Python virtual environment..."
if [ -d "venv" ]; then
    rm -rf venv
    echo "[SUCCESS] 'venv' folder and all dependencies have been deleted."
else
    echo "[INFO] 'venv' folder not found, skipping."
fi

echo "[Step 2/9] Deleting dependency marker..."
rm -f venv/deps_installed.marker
rm -f deps_installed.marker

echo "[Step 3/9] Deleting downloaded LLM models..."
if [ -d "llm_models" ]; then
    rm -rf llm_models
    echo "[SUCCESS] 'llm_models' folder deleted."
else
    echo "[INFO] 'llm_models' folder not found, skipping."
fi

echo "[Step 4/9] Deleting downloaded TTS models..."
if [ -d "tts_models" ]; then
    rm -rf tts_models
    echo "[SUCCESS] 'tts_models' folder deleted."
else
    echo "[INFO] 'tts_models' folder not found, skipping."
fi

echo "[Step 5/9] Deleting local configuration..."
rm -f .env
rm -f settings.json
echo "[SUCCESS] Local configuration deleted."

echo "[Step 6/9] Deleting logs..."
rm -f *.log
echo "[SUCCESS] Log files deleted."

echo "[Step 7/9] Deleting temporary files..."
rm -f output.wav
rm -f pip_install.log

echo "[Step 8/9] Deleting __pycache__ folders..."
find . -type d -name "__pycache__" -exec rm -rf {} +
echo "[SUCCESS] __pycache__ folders deleted."

echo "[Step 9/9] Deleting obsolete root files..."
rm -f assistant_app.py

echo ""
echo "============================================================================"
echo ""
echo "[SUCCESS] Full project cleanup is complete."
echo "You can now run './start.sh' for a completely fresh installation."
echo ""
```

### File: `/config.py`
```py
# assistant_app/config.py
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# The wake word to activate the assistant.
WAKE_WORD = os.getenv("WAKE_WORD", "computer")

# The level of detail for logs.
_log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, _log_level_str, logging.INFO)
```

### File: /logging_config.py```python
# assistant_app/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
from assistant_app import config

def setup_logging():
    """Configures the root logger for the application."""
    
    log_formatter = logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(name)-25.25s] [%(levelname)-8.8s]  %(message)s"
    )
    
    log_file_handler = RotatingFileHandler(
        "assistant.log", 
        maxBytes=5*1024*1024,
        backupCount=3,
        encoding='utf-8'
    )
    log_file_handler.setFormatter(log_formatter)
    
    root_logger = logging.getLogger()
    root_logger.setLevel(config.LOG_LEVEL)
    
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
        
    root_logger.addHandler(log_file_handler)
    logging.captureWarnings(True)
    
    logging.info("="*60)
    logging.info("Logging configured. Starting new application session.")
    logging.info(f"Log Level set to {logging.getLevelName(config.LOG_LEVEL)}")
    logging.info("="*60)
```

### File: `/installer/__init__.py`
```py
# This file makes the 'installer' directory a Python package.
```

### File: `/installer/installer.css`
```css
/* installer/installer.css */

Screen {
    align: center middle;
    background: $surface;
}

#installer-container {
    width: 80%;
    max-width: 100;
    height: 80%;
    max-height: 30;
    border: heavy $primary;
    background: $panel;
}

#installer-header {
    dock: top;
    height: 3;
    content-align: center middle;
    text-style: bold;
    background: $primary-darken-2;
}

#installer-footer {
    dock: bottom;
    height: 1;
    background: $primary-darken-2;
    color: $text-muted;
}

#status-line {
    padding: 0 1;
    text-style: bold;
    color: $warning;
}

#installer-log {
    height: 1fr;
    border: round $primary-lighten-2;
    margin: 1;
    background: $background;
    padding: 1;
}

#progress-bar {
    margin: 1;
    display: none;
    color: $success;
}

#progress-bar.visible {
    display: block;
}
```

### File: `/installer/installer_tui.py`
```py
# installer/installer_tui.py
import logging
import os
import shutil
import subprocess
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Footer, Header, ProgressBar, RichLog, Static
# CORRECTED IMPORT: The @work decorator IS IN textual.worker for v0.58.0.
from textual.worker import work

# --- Basic Setup ---
PROJECT_ROOT = Path(__file__).parent.parent
VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"

# Determine Python executable
if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
    PYTHON_CMD = "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"
    PYTHON_CMD = "python3"


# --- Advanced Installer Logging ---
def setup_installer_logging():
    log_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8.8s]  %(message)s"
    )
    # Ensure logs are written relative to the project root
    log_file_path = PROJECT_ROOT / "installer.log"
    log_file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=2 * 1024 * 1024,
        backupCount=1,
        encoding="utf-8",
    )
    log_file_handler.setFormatter(log_formatter)
    
    logger = logging.getLogger("installer")
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.addHandler(log_file_handler)
    return logger

logger = setup_installer_logging()


class TuiLogHandler(logging.Handler):
    """A logging handler that sends records to a Textual RichLog widget."""
    def __init__(self, app_instance: App):
        super().__init__()
        self.app = app_instance
        self._rich_log = None
        self.setFormatter(logging.Formatter("[green]%(message)s[/]"))

    def get_widget(self) -> RichLog:
        if not self._rich_log:
            self._rich_log = self.app.query_one(RichLog)
        return self._rich_log

    def emit(self, record):
        try:
            widget = self.get_widget()
            self.app.call_from_thread(widget.write, self.format(record))
        except Exception:
            pass


class InstallerApp(App):
    """A Textual UI for installing and launching the assistant."""
    CSS_PATH = PROJECT_ROOT / "installer" / "installer.css"

    def compose(self) -> ComposeResult:
        with Container(id="installer-container"):
            yield Header("Assistant App Installer")
            yield Vertical(
                RichLog(id="installer-log", wrap=True, highlight=True),
                ProgressBar(id="progress-bar"),
            )
            with Footer():
                yield Static("Status: Initializing...", id="status-line")

    def on_mount(self) -> None:
        tui_handler = TuiLogHandler(self)
        logger.addHandler(tui_handler)
        self.run_installation()

    def update_status(self, message: str) -> None:
        self.call_from_thread(self.query_one("#status-line", Static).update, f"Status: {message}")
        logger.info(message)

    @work(exclusive=True)
    def run_installation(self):
        logger.info("=" * 60)
        logger.info(f"Installer UI Mounted. Started at {datetime.now()}")
        logger.info(f"Project Root: {PROJECT_ROOT}")
        logger.info("=" * 60)

        try:
            if MARKER_FILE.exists():
                self.update_status("Dependencies are already installed.")
                self.launch_main_app()
                return

            if not VENV_DIR.exists():
                self.create_venv()
            else:
                self.update_status("Virtual environment found.")
                self.install_dependencies()

        except Exception as e:
            self.update_status(f"[bold red]An unexpected error occurred![/]")
            logger.error(f"FATAL ERROR in installation orchestrator: {e}", exc_info=True)

    @work(exclusive=True)
    def create_venv(self):
        self.update_status("Creating virtual environment...")
        
        sys_python = shutil.which(PYTHON_CMD.replace(".exe", ""))
        if not sys_python:
            self.update_status("[bold red]FATAL: Could not find system Python.[/]")
            logger.error("System python could not be found via shutil.which().")
            return

        process = subprocess.Popen([sys_python, "-m", "venv", str(VENV_DIR)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        process.wait()

        if process.returncode == 0:
            self.update_status("Virtual environment created successfully.")
            self.install_dependencies()
        else:
            self.update_status("[bold red]Failed to create virtual environment![/]")
            logger.error(f"Venv creation failed. Stderr:\n{process.stderr.read()}")

    @work(exclusive=True)
    def install_dependencies(self):
        self.update_status("Installing dependencies... This may take several minutes.")
        progress_bar = self.query_one(ProgressBar)
        self.call_from_thread(progress_bar.add_class, "visible")
        self.call_from_thread(progress_bar.update, total=100)

        command = [str(VENV_PYTHON), "-m", "pip", "install", "-r", str(PROJECT_ROOT / "requirements.txt")]
        logger.info(f"Running command: {' '.join(command)}")

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', bufsize=1)
        for line in iter(process.stdout.readline, ""):
            if line.strip(): logger.info(line.strip())
        process.wait()

        if process.returncode == 0:
            self.call_from_thread(progress_bar.update, progress=100)
            self.update_status("Dependencies installed successfully!")
            MARKER_FILE.touch()
            self.create_env_file()
        else:
            self.update_status("[bold red]Dependency installation FAILED.[/]")
            logger.error(f"Pip install failed with return code {process.returncode}.")
            self.call_from_thread(lambda: setattr(self.query_one(Footer).styles, 'background', 'red'))

    @work(exclusive=True)
    def create_env_file(self):
        self.update_status("Setting up configuration...")
        try:
            if not (PROJECT_ROOT / ".env").exists():
                shutil.copy(PROJECT_ROOT / ".env.example", PROJECT_ROOT / ".env")
                logger.info("'.env' file created from example.")
        except FileNotFoundError:
             logger.warning("'.env.example' not found. Skipping .env creation.")
        except Exception as e:
            logger.error(f"Failed to create .env file: {e}")
        self.launch_main_app()
    
    @work(exclusive=True)
    def launch_main_app(self):
        self.update_status("All checks passed. Launching application...")
        self.app.sleep(2)
        main_app_module = "assistant_app.main"
        kwargs = {'start_new_session': True} if sys.platform != "win32" else {'creationflags': subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP}
        subprocess.Popen([str(VENV_PYTHON), "-m", main_app_module], **kwargs)
        self.app.exit()
```

### File: `/installer_tui.py`
```py
# installer/installer_tui.py
import logging
import os
import shutil
import subprocess
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Footer, Header, ProgressBar, RichLog, Static
from textual.worker import Worker
from textual.work import work # Correct import for Textual v0.58.0

# --- Basic Setup ---
PROJECT_ROOT = Path(__file__).parent.parent
VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"

# Determine Python executable
if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
    PYTHON_CMD = "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"
    PYTHON_CMD = "python3"


# --- Advanced Installer Logging ---
def setup_installer_logging():
    log_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8.8s]  %(message)s"
    )
    # Ensure logs are written relative to the project root
    log_file_path = PROJECT_ROOT / "installer.log"
    log_file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=2 * 1024 * 1024,
        backupCount=1,
        encoding="utf-8",
    )
    log_file_handler.setFormatter(log_formatter)
    
    logger = logging.getLogger("installer")
    logger.setLevel(logging.INFO)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.addHandler(log_file_handler)
    return logger

logger = setup_installer_logging()


class TuiLogHandler(logging.Handler):
    """A logging handler that sends records to a Textual RichLog widget."""
    def __init__(self, app_instance: App):
        super().__init__()
        self.app = app_instance
        # Don't try to get the widget yet, as it might not be composed.
        self._rich_log = None
        self.setFormatter(logging.Formatter("[green]%(message)s[/]"))

    def get_widget(self) -> RichLog:
        if not self._rich_log:
            self._rich_log = self.app.query_one(RichLog)
        return self._rich_log

    def emit(self, record):
        # The TUI might not be fully mounted when logging starts, so we have to be safe.
        try:
            widget = self.get_widget()
            self.app.call_from_thread(widget.write, self.format(record))
        except Exception:
            # If the TUI isn't ready, the log will just go to the file.
            pass


class InstallerApp(App):
    """A Textual UI for installing and launching the assistant."""
    CSS_PATH = PROJECT_ROOT / "installer" / "installer.css"

    def compose(self) -> ComposeResult:
        with Container(id="installer-container"):
            yield Header("Assistant App Installer")
            yield Vertical(
                RichLog(id="installer-log", wrap=True, highlight=True),
                ProgressBar(id="progress-bar"),
            )
            with Footer():
                yield Static("Status: Initializing...", id="status-line")

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        tui_handler = TuiLogHandler(self)
        logger.addHandler(tui_handler)
        self.run_installation()

    def update_status(self, message: str) -> None:
        self.call_from_thread(self.query_one("#status-line", Static).update, f"Status: {message}")
        logger.info(message)

    @work(exclusive=True)
    def run_installation(self):
        """Starts the installation process in a background worker."""
        logger.info("=" * 60)
        logger.info(f"Installer UI Mounted. Started at {datetime.now()}")
        logger.info(f"Project Root: {PROJECT_ROOT}")
        logger.info("=" * 60)

        try:
            if MARKER_FILE.exists():
                self.update_status("Dependencies are already installed.")
                self.launch_main_app()
                return

            if not VENV_DIR.exists():
                self.create_venv()
            else:
                self.update_status("Virtual environment found.")
                self.install_dependencies()

        except Exception as e:
            self.update_status(f"[bold red]An unexpected error occurred![/]")
            logger.error(f"FATAL ERROR in installation orchestrator: {e}", exc_info=True)

    @work(exclusive=True)
    def create_venv(self):
        self.update_status("Creating virtual environment...")
        
        sys_python = shutil.which(PYTHON_CMD.replace(".exe", ""))
        if not sys_python:
            self.update_status("[bold red]FATAL: Could not find system Python.[/]")
            logger.error("System python could not be found via shutil.which().")
            return

        process = subprocess.Popen(
            [sys_python, "-m", "venv", str(VENV_DIR)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        process.wait()

        if process.returncode == 0:
            self.update_status("Virtual environment created successfully.")
            self.install_dependencies()
        else:
            self.update_status("[bold red]Failed to create virtual environment![/]")
            err = process.stderr.read()
            logger.error(f"Venv creation failed. Stderr:\n{err}")

    @work(exclusive=True)
    def install_dependencies(self) -> Worker:
        self.update_status("Installing dependencies... This may take several minutes.")
        progress_bar = self.query_one(ProgressBar)
        self.call_from_thread(progress_bar.add_class, "visible")
        self.call_from_thread(progress_bar.update, total=100)

        command = [
            str(VENV_PYTHON), "-m", "pip", "install", "-r", str(PROJECT_ROOT / "requirements.txt"),
        ]
        
        logger.info(f"Running command: {' '.join(command)}")

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', bufsize=1)
        
        for line in iter(process.stdout.readline, ""):
            if line.strip(): logger.info(line.strip())

        process.wait()

        if process.returncode == 0:
            self.call_from_thread(progress_bar.update, progress=100)
            self.update_status("Dependencies installed successfully!")
            MARKER_FILE.touch()
            self.create_env_file()
        else:
            self.update_status("[bold red]Dependency installation FAILED.[/]")
            logger.error(f"Pip install failed with return code {process.returncode}.")
            self.call_from_thread(lambda: setattr(self.query_one(Footer).styles, 'background', 'red'))

    @work(exclusive=True)
    def create_env_file(self):
        self.update_status("Setting up configuration...")
        try:
            shutil.copy(PROJECT_ROOT / ".env.example", PROJECT_ROOT / ".env")
            logger.info("'.env' file created from example.")
        except FileNotFoundError:
             logger.warning("'.env.example' not found. Skipping .env creation.")
        except Exception as e:
            logger.error(f"Failed to create .env file: {e}")
        self.launch_main_app()
    
    @work(exclusive=True)
    def launch_main_app(self):
        self.update_status("All checks passed. Launching application...")
        self.app.sleep(2)
        
        main_app_module = "assistant_app.main"
        
        kwargs = {'start_new_session': True} if sys.platform != "win32" else {'creationflags': subprocess.DETACHED_PROCESS}
        subprocess.Popen([str(VENV_PYTHON), "-m", main_app_module], **kwargs)
        self.app.exit()
```

### File: `/llm/__init__.py`
```py
# This file makes the 'llm' directory a Python sub-package.
```

### File: `/llm/gguf_client.py`
```py
# assistant_app/llm/gguf_client.py
import logging
from llama_cpp import Llama

logger = logging.getLogger(__name__)

class GGUFClient:
    """
    Manages loading and interacting with a local GGUF model using llama-cpp-python.
    """
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.conversation_history = []
        logger.info(f"Initializing GGUFClient with model at '{model_path}'")
        # For n_gpu_layers, -1 means offload all possible layers to GPU
        self.llm = Llama(model_path=self.model_path, n_ctx=2048, n_gpu_layers=-1, verbose=False)
        logger.info("GGUF model loaded successfully.")

    def _add_to_history(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})
        logger.debug(f"Added to conversation history: role={role}, content='{content[:70]}...'")

    def get_completion(self, prompt: str) -> str:
        """
        Gets a completion from the loaded GGUF model.
        """
        logger.debug(f"Getting GGUF completion for prompt: '{prompt}'")

        system_message = {"role": "system", "content": "You are a helpful AI assistant."}
        user_message = {"role": "user", "content": prompt}
        
        # Construct the message list for the current turn
        messages = [system_message] + self.conversation_history + [user_message]
        
        try:
            response = self.llm.create_chat_completion(messages=messages, max_tokens=1024)
            llm_response = response['choices'][0]['message']['content'].strip()
            
            # Add both user prompt and assistant response to history for next turn
            self._add_to_history("user", prompt)
            self._add_to_history("assistant", llm_response)

            logger.debug(f"GGUF completion received successfully.")
            return llm_response
        except Exception as e:
            logger.error(f"GGUF model inference error: {e}", exc_info=True)
            return "I apologize, but I encountered an error during model processing."
```

### File: `/logging_config.py`
```py
# assistant_app/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
from assistant_app import config

def setup_logging():
    """Configures the root logger for the application."""
    
    # Define the log format
    log_formatter = logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(name)-20.20s] [%(levelname)-5.5s]  %(message)s"
    )
    
    # Set up a file handler that rotates logs
    log_file_handler = RotatingFileHandler(
        "assistant.log", 
        maxBytes=5*1024*1024,  # 5 MB
        backupCount=3,         # Keep 3 backup log files
        encoding='utf-8'
    )
    log_file_handler.setFormatter(log_formatter)
    
    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(config.LOG_LEVEL)
    
    # Remove any existing handlers to avoid duplicates
    if root_logger.handlers:
        root_logger.handlers = []
        
    root_logger.addHandler(log_file_handler)
    
    # Redirect warnings from the 'warnings' module to the logging system
    logging.captureWarnings(True)
    
    logging.info("="*60)
    logging.info("Logging configured. Starting new application session.")
    logging.info(f"Log Level set to {logging.getLevelName(config.LOG_LEVEL)}")
    logging.info("="*60)
```

### File: `/main.py`
```py
import tkinter as tk

class CogniCore(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CogniCore")
        self.geometry("300x200")
        self.label = tk.Label(self, text="Hello, CogniCore!")
        self.label.pack(pady=20)

if __name__ == "__main__":
    app = CogniCore()
    app.mainloop()
```

### File: `/models/downloader.py`
```py
# assistant_app/models/downloader.py
import requests
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def download_file(url: str, dest_folder: str | Path, dest_filename: str, progress_callback: callable):
    """Downloads a file with progress reporting."""
    dest_path = Path(dest_folder) / dest_filename
    logger.info(f"Starting download from {url} to {dest_path}")
    try:
        with requests.get(url, stream=True, timeout=30) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            progress_callback("start", total_size=total_size)
            
            downloaded = 0
            with open(dest_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress_callback("update", downloaded=downloaded)
            
            logger.info(f"Download completed successfully: {dest_path}")
            progress_callback("finish")
            return dest_path
    except requests.RequestException as e:
        logger.error(f"Failed to download file from {url}: {e}", exc_info=True)
        progress_callback("error", message=str(e))
        return None
```

### File: `/models/hf_utils.py`
```py
# assistant_app/models/hf_utils.py
import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin

logger = logging.getLogger(__name__)

def list_gguf_files_from_repo(repo_id: str):
    """
    Scrapes a Hugging Face model repository page to find all GGUF files.
    
    Args:
        repo_id (str): The ID of the repository (e.g., "TheBloke/Llama-2-7B-Chat-GGUF").

    Returns:
        list[dict]: A list of dictionaries, each containing 'filename' and 'url'.
    """
    files = []
    base_url = f"https://huggingface.co/{repo_id}/tree/main"
    logger.info(f"Fetching GGUF file list from {base_url}")

    try:
        response = requests.get(base_url, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links that contain '.gguf' in their href
        for link in soup.find_all('a', href=lambda href: href and '.gguf' in href):
            filename = link.text.strip()
            # Construct the direct download URL
            relative_path = link['href']
            # The download URL requires "?download=true"
            download_url = urljoin(f"https://huggingface.co", f"{relative_path}?download=true")
            files.append({"filename": filename, "url": download_url})
            
        logger.info(f"Found {len(files)} GGUF files in repo {repo_id}.")
        return files

    except requests.RequestException as e:
        logger.error(f"Failed to fetch Hugging Face repo page for {repo_id}: {e}", exc_info=True)
        return []
```

### File: `/models/llm_manager.py`
```py
# assistant_app/models/llm_manager.py
import os
import logging
from pathlib import Path

from .downloader import download_file as download_gguf_file

logger = logging.getLogger(__name__)

LLM_MODELS_PATH = Path("llm_models")
LLM_MODELS_PATH.mkdir(exist_ok=True)

def get_local_models():
    """Returns a list of locally installed GGUF models."""
    if not LLM_MODELS_PATH.exists():
        return []
    return [f for f in LLM_MODELS_PATH.glob("*.gguf")]

def download_model(url: str, filename: str, progress_callback: callable):
    """Downloads a GGUF model file."""
    return download_gguf_file(url, LLM_MODELS_PATH, filename, progress_callback)

def delete_model(filepath: Path | str):
    """Deletes a local GGUF model file."""
    try:
        model_path = Path(filepath)
        if model_path.exists():
            logger.info(f"Attempting to delete GGUF model: {model_path}")
            model_path.unlink()
            logger.info(f"Successfully deleted model: {model_path}")
            return True
        else:
            logger.warning(f"Attempted to delete a non-existent model: {filepath}")
            return False
    except Exception as e:
        logger.error(f"Failed to delete model {filepath}: {e}", exc_info=True)
        return False
```

### File: `/models/tts_manager.py`
```py
# assistant_app/models/tts_manager.py
import logging
from TTS.utils.manage import ModelManager
from pathlib import Path
import shutil

logger = logging.getLogger(__name__)

# The directory where TTS models will be stored
TTS_MODELS_PATH = Path("tts_models")
TTS_MODELS_PATH.mkdir(exist_ok=True)

_model_manager = None

def get_model_manager():
    global _model_manager
    if _model_manager is None:
        # NOTE: ModelManager creates a local DB file in ~/.local/share/tts/tts_models.json
        _model_manager = ModelManager(TTS_MODELS_PATH)
    return _model_manager

def get_remote_models_list():
    """Gets the list of available TTS models from Coqui."""
    try:
        manager = get_model_manager()
        # The `list_models` returns a huge list, we need to filter for tts_models
        all_models = manager.list_models()
        tts_models = [m for m in all_models if "/tts/" in m and "gan" not in m] # Filter out GAN vocoders
        return sorted(tts_models)
    except Exception as e:
        logger.error(f"Could not fetch remote TTS model list: {e}", exc_info=True)
        return []

def get_local_models_list():
    """Finds installed TTS models by checking for model directories."""
    if not TTS_MODELS_PATH.exists():
        return []
        
    local_models = set()
    for lang_dir in TTS_MODELS_PATH.iterdir():
        if lang_dir.is_dir():
            for author_dir in lang_dir.iterdir():
                if author_dir.is_dir():
                    for model_dir in author_dir.iterdir():
                        if model_dir.is_dir() and (model_dir / "model_file.pth").exists():
                             model_name = f"{lang_dir.name}/{author_dir.name}/{model_dir.name}"
                             local_models.add(model_name)
    return sorted(list(local_models))

def download_model(model_name: str, progress_callback: callable):
    """Downloads a Coqui TTS model without showing a progress bar in the console."""
    logger.info(f"Starting download for TTS model: {model_name}")
    try:
        manager = get_model_manager()
        # progress_bar=False is critical to prevent it from corrupting the Textual UI
        manager.download_model(model_name, progress_bar=False)
        logger.info(f"Successfully downloaded TTS model: {model_name}")
        progress_callback("finish")
    except Exception as e:
        logger.error(f"Failed to download TTS model {model_name}: {e}", exc_info=True)
        progress_callback("error", message=str(e))

def delete_model(model_name: str):
    """Deletes a local TTS model directory."""
    try:
        model_path_parts = model_name.split("/")
        if len(model_path_parts) != 3:
             logger.error(f"Invalid TTS model name format for deletion: {model_name}")
             return False
        
        target_path = TTS_MODELS_PATH.joinpath(*model_path_parts)
        
        if target_path.exists() and target_path.is_dir():
            logger.info(f"Attempting to delete TTS model directory: {target_path}")
            shutil.rmtree(target_path)
            logger.info(f"Successfully deleted model: {model_name}")
            return True
        else:
            logger.warning(f"Attempted to delete a non-existent TTS model: {model_name} at {target_path}")
            return False
    except Exception as e:
        logger.error(f"Failed to delete model {model_name}: {e}", exc_info=True)
        return False
```

### File: `/plugins/__init__.py`
```py
# This file makes the 'plugins' directory a Python sub-package.
```

### File: `/plugins/base.py`
```py
# assistant_app/plugins/base.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# To prevent circular imports
if TYPE_CHECKING:
    from assistant_app.assistant import Assistant

class Command(ABC):
    """Abstract base class for all command plugins."""

    @property
    @abstractmethod
    def keywords(self) -> list[str]:
        """Lowercase keywords that trigger this command."""
        pass

    def matches(self, text: str) -> bool:
        """Checks if the text triggers this command."""
        return any(keyword in text.lower() for keyword in self.keywords)

    @abstractmethod
    def execute(self, assistant: "Assistant") -> str:
        """
        Executes the command.

        Args:
            assistant: The main Assistant instance to allow commands
                       to modify its state (e.g., is_running).

        Returns:
            The text response to be spoken by the assistant.
        """
        pass
```

### File: `/plugins/exit_command.py`
```py
# assistant_app/plugins/exit_command.py
from assistant_app.plugins.base import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from assistant_app.assistant import Assistant

class ExitCommand(Command):
    """Command to gracefully shut down the assistant."""

    @property
    def keywords(self) -> list[str]:
        return ["exit", "shutdown", "stop", "goodbye"]

    def execute(self, assistant: "Assistant") -> str:
        """Sets the assistant's running state to False."""
        assistant.is_running = False 
        # The TUI observes this change and initiates a clean shutdown.
        return "Shutting down now. Goodbye!"
```

### File: `/plugins/registry.py`
```py
# assistant_app/plugins/registry.py
import os
import importlib
import logging
from assistant_app.plugins.base import Command

logger = logging.getLogger(__name__)

class CommandRegistry:
    """Discovers, loads, and manages command plugins."""

    def __init__(self, plugins_dir="assistant_app/plugins"):
        logger.info(f"Initializing CommandRegistry, scanning '{plugins_dir}' for plugins.")
        self.commands: list[Command] = self._discover_plugins(plugins_dir)
        logger.info(f"Discovered and loaded {len(self.commands)} command(s).")

    def _discover_plugins(self, plugins_dir: str) -> list[Command]:
        loaded_commands = []
        for filename in os.listdir(plugins_dir):
            if filename.endswith("_command.py") and not filename.startswith("__"):
                module_name = f"{plugins_dir.replace('/', '.')}.{filename[:-3]}"
                try:
                    module = importlib.import_module(module_name)
                    for attr in dir(module):
                        attribute = getattr(module, attr)
                        if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                            loaded_commands.append(attribute())
                            logger.debug(f"Successfully loaded command: {attribute.__name__}")
                except Exception as e:
                     logger.error(f"Failed to load plugin from {module_name}: {e}", exc_info=True)
        return loaded_commands

    def find_command(self, text: str) -> Command | None:
        """Finds the first command that matches the given text."""
        for command in self.commands:
            if command.matches(text):
                logger.debug(f"Text '{text[:30]}...' matched command: {type(command).__name__}")
                return command
        return None
```

### File: `/plugins/time_command.py`
```py
# assistant_app/plugins/time_command.py
from datetime import datetime
from assistant_app.plugins.base import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from assistant_app.assistant import Assistant

class TimeCommand(Command):
    """A command to get the current time."""

    @property
    def keywords(self) -> list[str]:
        return ["time", "date"]

    def execute(self, assistant: "Assistant") -> str:
        """Returns the current time in a readable format."""
        now = datetime.now()
        # Example: "The current time is 10:30 PM."
        current_time = now.strftime("%I:%M %p").strip("0")
        return f"The current time is {current_time}."
```

### File: `/requirements.txt`
```txt
# No external libraries are required yet.
```

### File: `/run.py`
```py
# run.py
import sys
import subprocess
from importlib import metadata
from importlib.metadata import version, PackageNotFoundError

# The single source of truth for the required version of Textual
TEXTUAL_VERSION = "0.58.0"
REQUIRED_PKG = f"textual=={TEXTUAL_VERSION}"
PKG_NAME = "textual"

def check_and_install_textual():
    """
    Checks if the correct version of Textual is installed using importlib.metadata.
    If not, it attempts to install or update it.
    """
    try:
        # Check if the package is installed and if the version is correct
        installed_version = version(PKG_NAME)
        if installed_version == TEXTUAL_VERSION:
            print(f"[INFO] Found correct Textual version ({installed_version}).")
            return True
        else:
            print(f"[BOOTSTRAP] Found Textual {installed_version}, but require {TEXTUAL_VERSION}. Upgrading...")
            # Fall through to the installation block
    except PackageNotFoundError:
        print(f"[BOOTSTRAP] Textual not found. Attempting to install {REQUIRED_PKG}...")
    
    # --- Installation block ---
    try:
        # Using check_call will raise an exception on failure
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", REQUIRED_PKG])
        print("[BOOTSTRAP] Textual prepared successfully.")
        return True
    except subprocess.CalledProcessError:
        print(f"[FATAL] Failed to install {REQUIRED_PKG}. Please check your network and run again.")
        return False

def main():
    """
    Entry point for the application. Ensures Textual is ready,
    then launches the installer UI.
    """
    print("Initializing...")
    
    if not check_and_install_textual():
        input("Press Enter to exit.")
        sys.exit(1)

    print("Launching Installer UI...")
    # This dynamic import is safe because we know the dependency is correct now.
    from installer.installer_tui import InstallerApp
    app = InstallerApp()
    app.run()

if __name__ == "__main__":
    main()
```

### File: `/screens/models_screen.py`
```py
# assistant_app/ui/screens/models_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Input, Button, Static, ProgressBar
from textual.worker import work

from assistant_app.app_settings import settings_manager
from assistant_app.models import llm_manager, tts_manager, hf_utils

logger = logging.getLogger(__name__)

class ModelsScreen(Screen):
    BINDINGS = [
        ("delete", "delete_selected_llm", "Delete LLM"),
        ("d", "download_selected", "Download"),
        ("s", "set_active", "Set Active"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Static("LLM Models", classes="title")
            with Horizontal(classes="input_bar"):
                yield Input(placeholder="HuggingFace Repo (e.g., TheBloke/Llama-2-7B-GGUF)", id="hf-repo-input")
                yield Button("Fetch Files", id="hf-fetch-button")
            yield DataTable(id="hf-files-table", cursor_type="row", classes="model_table")
            yield Static("Local LLM Models", classes="title")
            yield DataTable(id="llm-table", cursor_type="row", classes="model_table")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#hf-files-table").add_columns("GGUF File", "URL")
        self.query_one("#llm-table").add_columns("Filename", "Path", "Status")
        self.update_llm_table()
    
    def update_llm_table(self):
        table = self.query_one("#llm-table")
        table.clear()
        local_models = llm_manager.get_local_models()
        active_model = settings_manager.get("active_llm_model")
        for model_path in sorted(local_models):
            status = "[bold green](Active)[/]" if str(model_path) == active_model else ""
            table.add_row(model_path.name, str(model_path), status, key=str(model_path))

    async def on_button_pressed(self, message: Button.Pressed):
        if message.button.id == "hf-fetch-button":
            repo_id = self.query_one("#hf-repo-input", Input).value
            if repo_id:
                self.fetch_hf_files(repo_id)
    
    @work(exclusive=True)
    def fetch_hf_files(self, repo_id: str):
        table = self.query_one("#hf-files-table")
        table.clear()
        table.loading = True
        files = hf_utils.list_gguf_files_from_repo(repo_id)
        table.loading = False
        if files:
            for f in files:
                table.add_row(f['filename'], f['url'], key=f['url'])
        else:
            table.add_row("[red]No GGUF files found or failed to fetch repo.[/red]", "")

    def action_download_selected(self) -> None:
        try:
            table = self.query_one("#hf-files-table")
            download_url = table.get_row_key(table.cursor_row)
            filename = table.get_row(download_url)[0]
            if download_url and filename:
                self.app.push_screen(DownloadScreen(url=download_url, filename=filename))
        except KeyError:
            logger.warning("Tried to download with no row selected.")

    def action_delete_selected_llm(self) -> None:
        try:
            table = self.query_one("#llm-table")
            filepath = table.get_row_key(table.cursor_row)
            if filepath:
                llm_manager.delete_model(filepath)
                self.update_llm_table()
        except KeyError:
            logger.warning("Tried to delete LLM with no row selected.")

    def action_set_active(self) -> None:
        try:
            table = self.query_one("#llm-table")
            row_key = table.get_row_key(table.cursor_row)
            if row_key:
                settings_manager.set("active_llm_model", row_key)
                self.update_llm_table()
        except KeyError:
            logger.warning(f"Tried to set active LLM with no row selected.")

class DownloadScreen(Screen):
    """A modal screen for showing download progress with a moving spinner."""
    
    def __init__(self, url: str, filename: str):
        super().__init__()
        self.url = url
        self.filename = filename
        self.spinner_chars = "|/-\\"
        self.spinner_index = 0

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading: {self.filename}", id="progress-label"),
            Horizontal(
                Static(self.spinner_chars[0], id="spinner"),
                Static("Starting...", id="progress-stats"),
                classes="stats_bar",
            ),
            ProgressBar(total=100, id="download-progress"),
            id="progress-dialog",
        )
    
    def on_mount(self) -> None:
        self.download_model_file()
    
    @work(exclusive=True, thread=True)
    def download_model_file(self) -> None:
        """Calls the download manager in a background thread."""
        llm_manager.download_model(self.url, self.filename, self.on_download_progress)

    def on_download_progress(self, event: str, total_size: int = 0, downloaded: int = 0, message: str = "") -> None:
        """Callback to update the UI from the download worker."""
        progress_bar = self.query_one(ProgressBar)
        stats_label = self.query_one("#progress-stats")
        spinner = self.query_one("#spinner")

        if event == "start":
            progress_bar.total = total_size or 100
            stats_label.update("Connecting...")
        
        elif event == "update":
            progress_bar.update(progress=downloaded)
            
            # Update the moving spinner
            self.spinner_index = (self.spinner_index + 1) % len(self.spinner_chars)
            spinner.update(self.spinner_chars[self.spinner_index])
            
            # Update the detailed progress stats
            total_mb = (progress_bar.total or 0) / (1024 * 1024)
            downloaded_mb = downloaded / (1024 * 1024)
            percent = (downloaded / progress_bar.total * 100) if progress_bar.total else 0
            stats_label.update(f"{downloaded_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)")
        
        elif event == "finish":
            # Update the underlying models screen before closing
            if (models_screen := self.app.get_screen("models")):
                models_screen.update_llm_table()
            self.app.pop_screen()
        
        elif event == "error":
            # In case of an error, just close the dialog
            self.app.pop_screen()
```

### File: `/start.bat`
```bat
@echo off
setlocal

title Assistant App Launcher

REM ============================================================================
REM == This script's only job is to run the main Python entrypoint.           ==
REM == All logic is now handled inside run.py for better reliability.         ==
REM ============================================================================

set "PYTHON_CMD=python"
set "ENTRYPOINT_SCRIPT=run.py"

cls

REM --- Find Python ---
where %PYTHON_CMD% >nul 2>nul
if %errorlevel% neq 0 (
    echo [FATAL ERROR] Python is not installed or not in the system PATH.
    echo Please install Python 3.9+ and ensure it's added to your PATH.
    echo Website: https://www.python.org/
    pause
    goto :eof
)

REM --- Execute the main Python entrypoint ---
%PYTHON_CMD% %ENTRYPOINT_SCRIPT%

echo.
echo The application has closed. Press any key to exit.
pause > nul
```

### File: `/start.sh`
```sh
#!/bin/bash
set -e

# ============================================================================
# == This script's only job is to run the main Python entrypoint.           ==
# == All logic is now handled inside run.py for better reliability.         ==
# ============================================================================

PYTHON_CMD="python3"
ENTRYPOINT_SCRIPT="run.py"

clear

# --- Find Python ---
if ! command -v "$PYTHON_CMD" &> /dev/null; then
    echo "[FATAL ERROR] Python 3 is not installed or not in your PATH."
    echo "Please install Python 3.9+ to continue."
    exit 1
fi

# --- Execute the main Python entrypoint ---
"$PYTHON_CMD" "$ENTRYPOINT_SCRIPT"

echo ""
echo "The application has closed."
```

### File: `/tts/__init__.py`
```py
# Make tts a package
```

### File: `/tts/tts_engine.py`
```py
# assistant_app/tts/tts_engine.py
import logging
import sys
import subprocess
from TTS.api import TTS as CoquiTTS
from assistant_app.app_settings import settings_manager

logger = logging.getLogger(__name__)

class TTSEngine:
    """Manages TTS model loading and speech synthesis."""
    _instance = None
    _current_model_name: str | None = None
    _tts: CoquiTTS | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TTSEngine, cls).__new__(cls)
            cls._instance.reload_model()
        return cls._instance

    def reload_model(self):
        """Loads the TTS model specified in settings, or reloads if it has changed."""
        model_name = settings_manager.get("active_tts_model")
        
        if self._tts and self._current_model_name == model_name:
            logger.debug(f"TTS model '{model_name}' is already loaded.")
            return

        logger.info(f"Attempting to load TTS model: '{model_name}'")
        try:
            self._tts = CoquiTTS(model_name, progress_bar=False, gpu=False)
            self._current_model_name = model_name
            logger.info(f"TTS model '{model_name}' loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load TTS model '{model_name}': {e}", exc_info=True)
            self._tts = None
            self._current_model_name = None

    def _play_audio(self, file_path: str):
        """Plays an audio file using an appropriate OS command."""
        logger.debug(f"Playing audio file: {file_path}")
        try:
            if sys.platform == "win32":
                subprocess.run(["start", "/B", file_path], shell=True, check=True)
            elif sys.platform == "darwin":
                subprocess.run(["afplay", file_path], check=True, capture_output=True)
            else:
                subprocess.run(["aplay", file_path], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            logger.error(f"Failed to play audio. Ensure `aplay` (Linux) or `afplay` (macOS) is installed. Error: {e}")

    def speak(self, text: str):
        """Synthesizes text to speech."""
        if not text:
            return

        if self._tts is None:
            logger.warning("TTS is not available. Cannot speak.")
            return
        
        try:
            logger.debug(f"Synthesizing speech for text: '{text[:50]}...'")
            output_path = "output.wav"
            self._tts.tts_to_file(text=text, file_path=output_path)
            self._play_audio(output_path)
        except Exception as e:
            logger.error(f"Failed to synthesize or play speech: {e}", exc_info=True)

def speak_text(text: str):
    """Global convenience function to access the TTSEngine."""
    engine = TTSEngine()
    engine.speak(text)
```

### File: `/tui.css`
```css
/* assistant_app/tui.css */

Screen {
    layout: vertical;
}

Header {
    dock: top;
    height: 1;
    background: $accent-darken-2;
    color: $text;
}

Footer {
    dock: bottom;
    height: 1;
    border-top: tall $accent;
    border-title-style: bold;
    border-title-align: center;
}

/* Conversation Screen */
#conversation-container {
    padding: 1;
    height: 1fr;
}

#text-input {
    dock: bottom;
    height: 3;
    display: none;
}

#text-input:not([disabled]) {
    display: block;
}

/* Models Screen */
.title {
    background: $primary-background-darken-2;
    padding: 1;
    text-align: center;
    text-style: bold;
}

.input_bar {
    height: 3;
    padding-top: 1;
    align: center middle;
}

#hf-repo-input {
    width: 1fr;
}

#hf-fetch-button {
    width: auto;
    height: 1;
    margin-left: 1;
}

.model_table {
    height: 12;
    margin-bottom: 1;
    border: tall $primary-darken-2;
}

/* Download Screen Dialog */
#progress-dialog {
    align: center middle;
    background: $primary-background-lighten-2;
    width: 80%;
    height: auto;
    min-height: 5;
    max-height: 7;
    padding: 1;
    border: heavy $accent;
}

#progress-label {
    width: 100%;
    text-align: center;
    margin-bottom: 1;
}

.stats_bar {
    height: 1;
    width: 100%;
    align: center middle;
}

#progress-stats {
    width: 1fr;
}
```

### File: `/ui/__init__.py`
```py
# Makes 'ui' a Python package
```

### File: `/ui/screens/__init__.py`
```py
# Makes 'screens' a Python package
```

### File: `/ui/screens/conversation_screen.py`
```py
# assistant_app/ui/screens/conversation_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, ListView
from textual.worker import work

from assistant_app import config
from assistant_app.assistant import Assistant
from assistant_app.audio.stt import listen_for_audio
from assistant_app.tts.tts_engine import speak_text
from assistant_app.ui.tui import AssistantResponse, StatusUpdate, ConversationListItem

logger = logging.getLogger(__name__)

class ConversationScreen(Screen):
    """The main conversation screen for the assistant."""
    BINDINGS = [
        ("tab", "toggle_input_mode", "Toggle Input"),
    ]
    
    def __init__(self, assistant: Assistant, **kwargs):
        super().__init__(**kwargs)
        self.assistant = assistant
        self.input_mode = "voice"

    def compose(self) -> ComposeResult:
        yield Header()
        yield ScrollableContainer(ListView(id="conversation"), id="conversation-container")
        yield Input(placeholder="Type your message...", id="text-input", disabled=True)
        yield Footer()

    def on_mount(self) -> None:
        """Called when the screen is first mounted."""
        if self.assistant.is_running:
            self.action_listen_for_wake_word()
        else:
            list_view = self.query_one(ListView)
            list_view.append(
                ConversationListItem(
                    "Assistant failed to initialize. Check active models in Model Manager (Ctrl+M) and logs.",
                    "assistant"
                )
            )

    @work(exclusive=True, group="audio_input")
    def action_listen_for_wake_word(self) -> None:
        """Continuously listens for the wake word."""
        self.app.post_message(StatusUpdate("LISTENING..."))
        logger.debug("Starting wake word listener.")
        while self.input_mode == "voice" and self.assistant.is_running:
            text = listen_for_audio()
            if text is None: continue

            if config.WAKE_WORD in text:
                prompt = text.replace(config.WAKE_WORD, "", 1).strip()
                if prompt:
                    self.app.post_message(StatusUpdate("PROCESSING..."))
                    self.action_process_prompt(prompt)
                else:
                    self.app.post_message(StatusUpdate("Yes?"))
                    self.speak_and_reset_status("Yes?")
                return

    @work(exclusive=True, group="processing")
    def action_process_prompt(self, prompt: str) -> None:
        """Processes the prompt and posts the response."""
        response = self.assistant.process_prompt(prompt)
        self.post_message(AssistantResponse(response, prompt))
        if not self.assistant.is_running: # Exit command might have been triggered
            self.app.exit()
        else:
            self.speak_and_reset_status(response)

    @work(exclusive=True, group="audio_output")
    def speak_and_reset_status(self, text: str) -> None:
        """Speaks text and then restarts the wake word listener if in voice mode."""
        speak_text(text)
        if self.input_mode == "voice":
            self.action_listen_for_wake_word()
        else:
            self.post_message(StatusUpdate("TYPING..."))
    
    def action_toggle_input_mode(self) -> None:
        """Switches between voice and text input modes."""
        text_input = self.query_one("#text-input", Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.disabled = False
            text_input.focus()
            self.post_message(StatusUpdate("TYPING..."))
        else:
            self.input_mode = "voice"
            text_input.disabled = True
            text_input.value = ""
            self.action_listen_for_wake_word()
            
    async def on_input_submitted(self, message: Input.Submitted) -> None:
        """Handles submission from the text input field."""
        prompt = message.value
        if prompt:
            message.input.value = ""
            self.post_message(StatusUpdate("PROCESSING..."))
            self.action_process_prompt(prompt)
        self.set_focus(None)

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        """Receives a response from a worker and adds it to the conversation."""
        list_view = self.query_one(ListView)
        list_view.append(ConversationListItem(message.user_prompt, "user"))
        list_view.append(ConversationListItem(message.text, "assistant"))
        list_view.scroll_end()

    async def on_status_update(self, message: StatusUpdate) -> None:
        """Updates the footer status from a worker."""
        self.query_one(Footer).border_title = message.text
```

### File: `/ui/screens/models_screen.py`
```py
# assistant_app/ui/screens/models_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Input, Button, Static, ProgressBar
from textual.worker import work

from assistant_app.app_settings import settings_manager
from assistant_app.models import llm_manager, tts_manager, hf_utils

logger = logging.getLogger(__name__)

class ModelsScreen(Screen):
    BINDINGS = [
        ("d", "download_selected", "Download"),
        ("s", "set_active", "Set Active"),
        ("delete", "delete_selected", "Delete Selected"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with ScrollableContainer():
            yield Static("LLM Models - Remote", classes="title")
            with Horizontal(classes="input_bar"):
                yield Input(placeholder="HuggingFace Repo (e.g., TheBloke/Llama-2-7B-GGUF)", id="hf-repo-input")
                yield Button("Fetch Files", id="hf-fetch-button")
            yield DataTable(id="hf-files-table", cursor_type="row", classes="model_table")
            
            yield Static("LLM Models - Local", classes="title")
            yield DataTable(id="llm-table", cursor_type="row", classes="model_table")

            yield Static("TTS Models - Local", classes="title")
            yield DataTable(id="tts-local-table", cursor_type="row", classes="model_table")

            yield Static("TTS Models - Remote (Coqui)", classes="title")
            yield DataTable(id="tts-remote-table", cursor_type="row", classes="model_table")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#hf-files-table").add_columns("GGUF File", "URL")
        self.query_one("#llm-table").add_columns("Filename", "Path", "Status")
        self.query_one("#tts-local-table").add_columns("Local TTS Model", "Status")
        self.query_one("#tts-remote-table").add_columns("Available TTS Model")
        
        self.update_llm_table()
        self.update_tts_tables()
        self.fetch_remote_tts_models()
    
    def update_llm_table(self):
        table = self.query_one("#llm-table", DataTable)
        table.clear()
        local_models = llm_manager.get_local_models()
        active_model = settings_manager.get("active_llm_model")
        for model_path in sorted(local_models):
            status = "[bold green](Active)[/]" if str(model_path) == active_model else ""
            table.add_row(model_path.name, str(model_path), status, key=str(model_path))

    def update_tts_tables(self):
        table = self.query_one("#tts-local-table", DataTable)
        table.clear()
        local_models = tts_manager.get_local_models_list()
        active_model = settings_manager.get("active_tts_model")
        for model_name in sorted(local_models):
            status = "[bold green](Active)[/]" if model_name == active_model else ""
            table.add_row(model_name, status, key=model_name)

    @work(exclusive=True, thread=True)
    def fetch_hf_files(self, repo_id: str):
        table = self.query_one("#hf-files-table")
        self.call_from_thread(table.clear)
        self.call_from_thread(setattr, table, 'loading', True)
        files = hf_utils.list_gguf_files_from_repo(repo_id)
        self.call_from_thread(setattr, table, 'loading', False)
        if files:
            for f in files:
                self.call_from_thread(table.add_row, f['filename'], f['url'], key=f['url'])
        else:
            self.call_from_thread(table.add_row, "[red]No GGUF files found or repo is invalid.[/red]", "")
            
    @work(exclusive=True, thread=True)
    def fetch_remote_tts_models(self):
        table = self.query_one("#tts-remote-table")
        self.call_from_thread(setattr, table, 'loading', True)
        models = tts_manager.get_remote_models_list()
        self.call_from_thread(setattr, table, 'loading', False)
        if models:
            for model_name in models:
                self.call_from_thread(table.add_row, model_name, key=model_name)
        else:
            self.call_from_thread(table.add_row, "[red]Could not retrieve remote TTS models.[/red]")

    async def on_button_pressed(self, message: Button.Pressed):
        if message.button.id == "hf-fetch-button":
            repo_id = self.query_one("#hf-repo-input", Input).value
            if repo_id:
                self.fetch_hf_files(repo_id)

    def action_download_selected(self) -> None:
        hf_table = self.query_one("#hf-files-table")
        tts_table = self.query_one("#tts-remote-table")

        try:
            if hf_table.has_focus:
                row_key = hf_table.get_row_key(hf_table.cursor_row)
                filename = hf_table.get_cell(row_key, "GGUF File")
                if row_key and filename:
                    self.app.push_screen(DownloadScreen(url=row_key, filename=filename))
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name:
                    self.app.push_screen(TTSDownloadScreen(model_name=model_name))
        except KeyError:
            logger.warning("Download triggered with no row selected.")

    def action_delete_selected(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")

        try:
            if llm_table.has_focus:
                filepath = llm_table.get_row_key(llm_table.cursor_row)
                if filepath and llm_manager.delete_model(filepath):
                    if settings_manager.get("active_llm_model") == filepath:
                        settings_manager.set("active_llm_model", None)
                    self.update_llm_table()
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name and tts_manager.delete_model(model_name):
                    if settings_manager.get("active_tts_model") == model_name:
                        settings_manager.set("active_tts_model", "tts_models/en/ljspeech/vits")
                    self.update_tts_tables()
        except KeyError:
            logger.warning("Delete triggered with no row selected.")

    def action_set_active(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus:
                row_key = llm_table.get_row_key(llm_table.cursor_row)
                if row_key:
                    settings_manager.set("active_llm_model", row_key)
                    self.update_llm_table()
            elif tts_table.has_focus:
                row_key = tts_table.get_row_key(tts_table.cursor_row)
                if row_key:
                    settings_manager.set("active_tts_model", row_key)
                    self.update_tts_tables()
        except KeyError:
            logger.warning(f"Set Active triggered with no row selected.")

class DownloadScreen(Screen):
    """A modal screen for showing GGUF download progress."""
    
    def __init__(self, url: str, filename: str):
        super().__init__()
        self.url = url
        self.filename = filename

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading: {self.filename}", id="progress-label"),
            Horizontal(
                Static("Starting...", id="progress-stats"),
                classes="stats_bar",
            ),
            ProgressBar(total=100, id="download-progress"),
            id="progress-dialog",
        )
    
    def on_mount(self) -> None:
        self.download_model_file()
    
    def on_download_progress(self, event: str, total_size: int = 0, downloaded: int = 0, message: str = ""):
        def update_ui():
            progress_bar = self.query_one(ProgressBar)
            stats_label = self.query_one("#progress-stats")

            if event == "start":
                progress_bar.total = total_size or 100
                stats_label.update("Connecting...")
            
            elif event == "update":
                progress_bar.update(progress=downloaded)
                total_mb = (progress_bar.total or 0) / (1024 * 1024)
                downloaded_mb = downloaded / (1024 * 1024)
                percent = (downloaded / progress_bar.total * 100) if progress_bar.total else 0
                stats_label.update(f"{downloaded_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)")
            
            elif event == "finish":
                if (models_screen := self.app.get_screen("models")):
                    models_screen.update_llm_table()
                self.app.pop_screen()
            
            elif event == "error":
                self.app.pop_screen()
        
        self.call_from_thread(update_ui)

    @work(exclusive=True, thread=True)
    def download_model_file(self) -> None:
        llm_manager.download_model(self.url, self.filename, self.on_download_progress)

class TTSDownloadScreen(Screen):
    """A modal screen showing a simple busy spinner for TTS downloads."""

    def __init__(self, model_name: str):
        super().__init__()
        self.model_name = model_name

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading TTS Model: {self.model_name}", id="progress-label"),
            Static("This may take a few minutes. Please wait...", id="progress-stats"),
            id="progress-dialog",
        )

    def on_mount(self) -> None:
        self.download_tts_model()

    def on_download_finished(self, event: str, message: str = "") -> None:
        def update_ui():
            if (models_screen := self.app.get_screen("models")):
                models_screen.update_tts_tables()
            self.app.pop_screen()
        
        self.call_from_thread(update_ui)
    
    @work(exclusive=True, thread=True)
    def download_tts_model(self) -> None:
        tts_manager.download_model(self.model_name, self.on_download_finished)
```

### File: `/ui/tui.css`
```css
/* assistant_app/ui/tui.css */

Screen {
    layout: vertical;
}

Header {
    dock: top;
    height: 1;
    background: $accent-darken-2;
    color: $text;
}

Footer {
    dock: bottom;
    height: 1;
    border-top: tall $accent;
    border-title-style: bold;
    border-title-align: center;
}

/* Conversation Screen */
#conversation-container {
    padding: 1;
    height: 1fr;
}

#text-input {
    dock: bottom;
    height: 3;
    display: none;
}

#text-input:not([disabled]) {
    display: block;
}

/* Models Screen */
.title {
    background: $primary-background-darken-2;
    padding: 1;
    text-align: center;
    text-style: bold;
}

.input_bar {
    height: 3;
    padding-top: 1;
    align: center middle;
}

#hf-repo-input {
    width: 1fr;
}

#hf-fetch-button {
    width: auto;
    height: 1;
    margin-left: 1;
}

.model_table {
    height: 12;
    border: tall $primary-darken-2;
}

#progress-dialog {
    align: center middle;
    background: $primary-background-lighten-2;
    width: 80%;
    height: 5;
    padding: 1;
    border: heavy $accent;
}

#progress-label {
    width: 100%;
    text-align: center;
}

#progress-percent {
     width: 100%;
     text-align: center;
}
```

### File: `/ui/tui.py`
```py
# assistant_app/ui/tui.py
import logging
from textual.app import App, ComposeResult
from textual.widgets import ListItem, Label
from assistant_app.assistant import Assistant
from assistant_app.ui.screens.conversation_screen import ConversationScreen
from assistant_app.ui.screens.models_screen import ModelsScreen

logger = logging.getLogger(__name__)

# --- Message Classes for cross-screen communication ---
class AssistantResponse:
    """Posted when the assistant generates a response."""
    def __init__(self, text: str, user_prompt: str):
        self.text = text
        self.user_prompt = user_prompt

class StatusUpdate:
    """Posted to update the UI status footer."""
    def __init__(self, text: str):
        self.text = text

# -- UI Widgets (shared) --
class ConversationListItem(ListItem):
    """A list item widget to display a single conversation entry."""
    def __init__(self, content: str, role: str, **kwargs):
        super().__init__(**kwargs)
        self.content = content
        self.role = role
    
    def compose(self) -> ComposeResult:
        style = "bold cyan" if self.role == "user" else "bold green"
        yield Label(f"[{style}]{self.role.capitalize()}:[/] {self.content}")

class AssistantTUI(App):
    """The main Textual application for the AI Assistant."""
    CSS_PATH = "tui.css"
    SCREENS = {"models": ModelsScreen}
    BINDINGS = [
        ("ctrl+c", "request_quit", "Quit"),
        ("ctrl+m", "toggle_models_screen", "Models"),
    ]

    def __init__(self):
        super().__init__()
        self.assistant = Assistant()

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        self.push_screen(ConversationScreen(assistant=self.assistant))

    def action_toggle_models_screen(self) -> None:
        """Toggle the model management screen."""
        if isinstance(self.screen, ModelsScreen):
            logger.info("Closing models screen, reloading assistant components.")
            self.pop_screen()
            self.assistant.reload()
            from assistant_app.tts.tts_engine import TTSEngine
            TTSEngine().reload_model()
        else:
            self.push_screen("models")
    
    # --- Global Message Handlers ---
    async def on_assistant_response(self, message: AssistantResponse) -> None:
        # We assume only the conversation screen can meaningfully handle this
        if isinstance(self.screen, ConversationScreen):
            await self.screen.on_assistant_response(message)
    
    async def on_status_update(self, message: StatusUpdate) -> None:
        # Status updates are also mainly for the conversation screen
        if isinstance(self.screen, ConversationScreen):
            await self.screen.on_status_update(message)
```