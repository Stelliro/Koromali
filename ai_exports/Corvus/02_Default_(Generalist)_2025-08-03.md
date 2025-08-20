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
Corvus
├── cleaner
│   ├── clean.bat
│   └── clean.sh
├── corvus_app
│   ├── audio
│   │   ├── __init__.py
│   │   └── stt.py
│   ├── llm
│   │   ├── __init__.py
│   │   └── llm_client.py
│   ├── screens
│   │   ├── __init__.py
│   │   ├── conversation_screen.py
│   │   └── models_screen.py
│   ├── tts
│   │   ├── __init__.py
│   │   └── tts_engine.py
│   ├── ui
│   │   ├── screens
│   │   │   ├── __init__.py
│   │   │   ├── conversation_screen.py
│   │   │   └── models_screen.py
│   │   ├── __init__.py
│   │   ├── tui.css
│   │   └── tui.py
│   ├── __init__.py
│   ├── app_settings.py
│   ├── assistant.py
│   ├── config.py
│   ├── logging_config.py
│   └── main.py
├── installer
│   ├── __init__.py
│   ├── installer.css
│   └── installer_tui.py
├── models
│   ├── __init__.py
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
├── .env.example
├── .gitignore
├── __init__.py
├── installer.log
├── README.md
├── requirements.txt
├── run.py
├── start.bat
└── start.sh
```

## Project Files

### File: `/.env.example`
```example
# Assistant App Configuration
# This file is used as a template to create your .env file on first run.

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
# Corvus

Corvus is a minimalist, voice-first AI assistant designed to run completely offline on your local machine. It leverages local GGUF language models and a real-time text-to-speech engine to provide a private, responsive, and customizable assistant experience directly in your terminal.

---
> *In mythology, the raven (`Corvus` in Latin) is a symbol of intellect and memory. Odin, the Allfather, was accompanied by two ravens, Huginn (Thought) and Muninn (Memory), who flew across the world to bring him knowledge. This name was chosen to reflect the app's intention to serve as an intelligent and helpful companion.*
---

## Key Features

- **100% Offline & Private:** Your conversations never leave your machine. The core LLM and TTS functionalities are fully offline.
- **Voice Activated:** Use a wake word ("computer") to interact without touching the keyboard. **Note:** The default speech-to-text engine (`speech_recognition`) uses a Google API and requires an internet connection.
- **Local LLM Powered:** Runs powerful GGUF language models of your choice via `llama-cpp-python`.
- **Customizable Voice:** Integrates with Coqui TTS for a wide range of text-to-speech voices.
- **Plugin System:** Extend Corvus's capabilities with simple, custom Python commands.
- **Simple TUI:** A clean and straightforward terminal user interface.

## Quickstart

First-time setup is handled by an interactive installer. Simply run the start script for your OS.

**On Windows:**
```

### File: `/__init__.py`
```py
# This file makes 'corvus_app' a Python package.
```

### File: `/cleaner/clean.bat`
```bat
@echo off
setlocal

REM Set the working directory to the project root immediately to ensure all paths are correct.
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%..\"
if errorlevel 1 (
    echo [FATAL] Could not change to project root directory. Exiting.
    pause
    exit /b 1
)

echo.
echo ============================================================================
echo ==              CORVUS - AGGRESSIVE PROJECT RESET SCRIPT                  ==
echo ============================================================================
echo.
echo [WARNING] This script will PERMANENTLY DELETE:
echo           - All installed Python dependencies (the 'venv' folder)
echo           - All downloaded LLM and TTS models
echo           - All logs, settings, and temporary files
echo           - Any old, obsolete files from previous project structures
echo.
echo [INFO] Your source code ('corvus_app', 'installer', etc.) WILL NOT be deleted.
echo.

:confirm
set "CHOICE="
set /p "CHOICE=This action will perform a full factory reset of generated files. Are you sure? (y/n): "
if /i "%CHOICE%"=="y" goto :proceed
if /i "%CHOICE%"=="yes" goto :proceed
if /i "%CHOICE%"=="n" goto :cancel
if /i "%CHOICE%"=="no" goto :cancel
echo.
echo [ERROR] Invalid input. Please enter 'y' or 'n'.
echo.
goto :confirm

:cancel
echo.
echo Cleanup cancelled by user.
goto :end

:proceed
echo.
echo [INFO] Starting aggressive project cleanup in directory: '%cd%'
echo.

echo [Step 1/7] Deleting Python virtual environment ('venv')...
if exist "venv" (
    rmdir /s /q venv
    if exist "venv" (
        echo [ERROR] Failed to delete the 'venv' directory. It may be in use by another program (e.g., your IDE or terminal). Please close it and try again.
    ) else (
        echo [INFO] 'venv' directory successfully deleted.
    )
) else (
    echo [INFO] 'venv' directory not found, skipping.
)

echo [Step 2/7] Deleting all downloaded AI models...
if exist "llm_models" ( rmdir /s /q llm_models )
if exist "tts_models" ( rmdir /s /q tts_models )

echo [Step 3/7] Deleting all logs, settings, and temporary files...
del /q /f .env settings.json *.log crash.log pip_install.log output.wav >nul 2>nul

echo [Step 4/7] Deleting __pycache__ folders...
for /d /r . %%d in (__pycache__) do ( if exist "%%d" rmdir /s /q "%%d" )

echo [Step 5/7] Deleting old/obsolete root files from previous structures...
del /q /f assistant.py config.py logging_config.py main.py tui.css installer_tui.py app_settings.py >nul 2>nul

echo [Step 6/7] Deleting old 'assistant_app' source folder if it exists...
if exist "assistant_app" ( rmdir /s /q assistant_app )

echo [Step 7/7] Deleting old top-level UI/TTS folders if they exist...
if exist "ui" ( rmdir /s /q ui )
if exist "tts" ( rmdir /s /q tts )

echo.
echo ============================================================================
echo [SUCCESS] Aggressive cleanup is complete.
echo Your source code is intact. You can now run 'start.bat' for a fresh installation.
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
echo "==              CORVUS - AGGRESSIVE PROJECT RESET SCRIPT                  =="
echo "============================================================================"
echo ""
echo "[WARNING] This script will PERMANENTLY DELETE:"
echo "          - All installed Python dependencies (the 'venv' folder)"
echo "          - All downloaded LLM and TTS models"
echo "          - All logs, settings, and temporary files"
echo "          - Any old, obsolete files from previous project structures"
echo ""
echo "[INFO] Your source code ('corvus_app', 'installer', etc.) WILL NOT be deleted."
echo ""

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR/.."

while true; do
    read -p "This action will perform a full factory reset of generated files. Are you sure? (y/n) " -n 1 -r REPLY
    echo
    case $REPLY in
        [Yy])
            break
            ;;
        [Nn])
            echo "Cleanup cancelled by user."
            exit 0
            ;;
        *)
            echo "[ERROR] Invalid input. Please answer y or n."
            ;;
    esac
done


echo ""
echo "[INFO] Starting aggressive project cleanup in directory: $(pwd)"
echo ""

echo "[1/7] Deleting Python virtual environment ('venv')..."
rm -rf venv

echo "[2/7] Deleting all downloaded AI models..."
rm -rf llm_models tts_models

echo "[3/7] Deleting all logs, settings, and temporary files..."
rm -f .env settings.json *.log crash.log pip_install.log output.wav

echo "[4/7] Deleting __pycache__ folders..."
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "[5/7] Deleting old/obsolete root files from previous structures..."
rm -f assistant.py config.py logging_config.py main.py tui.css installer_tui.py app_settings.py

echo "[6/7] Deleting old 'assistant_app' source folder if it exists..."
rm -rf assistant_app

echo "[7/7] Deleting old top-level UI/TTS folders if they exist..."
rm -rf ui tts


echo ""
echo "============================================================================"
echo "[SUCCESS] Aggressive cleanup is complete."
echo "Your source code is intact. You can now run './start.sh' for a fresh installation."
echo ""
```

### File: `/corvus_app/__init__.py`
```py

```

### File: `/corvus_app/app_settings.py`
```py
# corvus_app/app_settings.py
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class AppSettings:
    """Manages persistent application settings like active models."""
    def __init__(self, file_path: str = "settings.json"):
        self.file_path = Path(file_path)
        self.defaults = {
            "active_llm_model": None,
            "active_tts_model": "tts_models/en/ljspeech/vits"
        }
        self.settings = self._load()

    def _load(self) -> dict:
        if self.file_path.exists():
            with self.file_path.open('r', encoding='utf-8') as f:
                try:
                    loaded_settings = json.load(f)
                    for key, value in self.defaults.items():
                        loaded_settings.setdefault(key, value)
                    return loaded_settings
                except json.JSONDecodeError:
                    return self.defaults.copy()
        else:
            self.settings = self.defaults.copy()
            self._save()
            return self.settings

    def _save(self):
        with self.file_path.open('w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key: str):
        return self.settings.get(key)

    def set(self, key: str, value):
        self.settings[key] = value
        self._save()

settings_manager = AppSettings()
```

### File: `/corvus_app/assistant.py`
```py
# corvus_app/assistant.py
import logging

from corvus_app.llm.llm_client import LLMClient
from plugins.registry import CommandRegistry

logger = logging.getLogger(__name__)

class Assistant:
    def __init__(self):
        logger.info("Initializing Assistant...")
        self.is_running = True
        self.registry = CommandRegistry()
        self.llm_client = LLMClient()
        
    def reload(self):
        """Reloads components like the LLM model."""
        logger.info("Reloading Assistant components...")
        self.llm_client.reload_model()

    def process_prompt(self, prompt: str) -> str:
        """
        Processes a user prompt by checking for commands first,
        then falling back to the LLM.
        """
        logger.info(f"Processing prompt: '{prompt}'")

        # Check for a matching command plugin first
        command = self.registry.find_command(prompt)
        if command:
            logger.info(f"Executing command: {command.__class__.__name__}")
            return command.execute(self)

        # If no command, use the LLM
        logger.info("No command found, deferring to LLM.")
        return self.llm_client.get_response(prompt)
```

### File: `/corvus_app/audio/__init__.py`
```py
# This file makes the 'audio' directory a Python sub-package.
```

### File: `/corvus_app/audio/stt.py`
```py
# corvus_app/audio/stt.py
import logging
import speech_recognition as sr

logger = logging.getLogger(__name__)

def listen_for_audio() -> str:
    """
    Listens for audio from the default microphone and returns the recognized text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # We use a shorter, more responsive duration for ambient noise adjustment
        r.adjust_for_ambient_noise(source, duration=0.5)
        logger.info("Listening for wake word or command...")
        try:
            # Increased timeout to give users more time to speak.
            audio = r.listen(source, timeout=7, phrase_time_limit=15)
            logger.info("Recognizing speech...")
            # Using recognize_google for its accuracy and ease of use.
            text = r.recognize_google(audio)
            logger.info(f"Recognized text: '{text}'")
            return text.lower()
        except sr.WaitTimeoutError:
            logger.debug("Listening timed out, no audio detected.")
            return ""
        except sr.UnknownValueError:
            logger.debug("Speech was unintelligible.")
            return ""
        except sr.RequestError as e:
            logger.error(f"Could not request results from recognizer; {e}")
            return ""
        except Exception as e:
            logger.error(f"An unexpected error occurred during audio processing: {e}", exc_info=True)
            return ""
```

### File: `/corvus_app/config.py`
```py
# corvus_app/config.py
import os
import logging
from dotenv import load_dotenv

load_dotenv()

WAKE_WORD = os.getenv("WAKE_WORD", "corvus")

_log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, _log_level_str, logging.INFO)
```

### File: `/corvus_app/llm/__init__.py`
```py
# This file makes the 'llm' directory a Python sub-package.
```

### File: `/corvus_app/llm/llm_client.py`
```py
# corvus_app/llm/llm_client.py
import logging
from llama_cpp import Llama
from corvus_app.app_settings import settings_manager

logger = logging.getLogger(__name__)

class LLMClient:
    """
    A singleton client to manage the lifecycle of the Llama CPP model.
    It handles loading, reloading, and generating text responses.
    """
    _instance = None
    _current_model_path: str | None = None
    _llm: Llama | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMClient, cls).__new__(cls)
            # Initial model load is triggered on first instantiation
            cls._instance.reload_model()
        return cls._instance

    def reload_model(self):
        """
        Loads or reloads the GGUF model specified in the application settings.
        If the model path hasn't changed, it does nothing.
        """
        model_path = settings_manager.get("active_llm_model")
        if not model_path:
            logger.warning("No active LLM model selected. LLM client not loaded.")
            self._llm = None
            self._current_model_path = None
            return

        if self._llm and self._current_model_path == model_path:
            logger.debug("LLM model is already up-to-date.")
            return

        logger.info(f"Attempting to load LLM model: '{model_path}'")
        try:
            # Parameters for a responsive chat model
            self._llm = Llama(model_path=model_path, n_ctx=2048, n_gpu_layers=-1, verbose=False)
            self._current_model_path = model_path
            logger.info(f"LLM model '{model_path}' loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load LLM model '{model_path}': {e}", exc_info=True)
            self._llm = None
            self._current_model_path = None

    def get_response(self, prompt: str) -> str:
        """
        Generates a text response from the loaded LLM for a given prompt.
        """
        if not self._llm:
            logger.error("LLM not loaded, cannot get response.")
            return "I can't respond right now as my language model is not loaded. Please select a model in the settings."

        logger.debug(f"Generating LLM response for prompt: '{prompt}'")
        
        # A simple but effective chat instruction format
        system_prompt = "You are a helpful assistant."
        full_prompt = f"System: {system_prompt}\nUser: {prompt}\nAssistant:"
        
        try:
            output = self._llm(
                full_prompt,
                max_tokens=256,
                stop=["User:", "\n"],
                echo=False,
                temperature=0.7
            )
            response_text = output['choices'][0]['text'].strip()
            logger.info(f"LLM generated response: '{response_text}'")
            return response_text
        except Exception as e:
            logger.error(f"Error during LLM inference: {e}", exc_info=True)
            return "I'm sorry, I encountered an error while thinking of a response."
```

### File: `/corvus_app/logging_config.py`
```py
# corvus_app/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
from . import config

def setup_logging(log_filename="corvus_app.log"):
    """Configures the root logger for the application."""
    log_formatter = logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(name)-25.25s] [%(levelname)-8.8s]  %(message)s"
    )
    log_file_handler = RotatingFileHandler(
        log_filename, maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
    )
    log_file_handler.setFormatter(log_formatter)
    root_logger = logging.getLogger()
    root_logger.setLevel(config.LOG_LEVEL)
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
    root_logger.addHandler(log_file_handler)
    logging.captureWarnings(True)
    logging.info("="*60)
    logging.info(f"Logging configured for '{log_filename}'. Log Level: {logging.getLevelName(root_logger.level)}")
    logging.info("="*60)
```

### File: `/corvus_app/main.py`
```py
# corvus_app/main.py
import sys
import logging
import traceback
from datetime import datetime
from pathlib import Path
from rich.console import Console

_console = Console()

def bootstrap():
    """Initial setup for directories and logging."""
    try:
        Path("tts_models").mkdir(exist_ok=True)
        Path("llm_models").mkdir(exist_ok=True)
        from corvus_app.logging_config import setup_logging
        setup_logging(log_filename="corvus_app.log")
    except Exception as e:
        _console.print("[bold red]FATAL: Failed to configure application logging.[/bold red]")
        with open("crash.log", "w", encoding="utf-8") as f:
            f.write(f"--- Corvus Crash Report (Bootstrap Failure) ---\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\nError: {e}\n")
            f.write("-" * 30 + "\n\n")
            traceback.print_exc(file=f)
        _console.print("[bold red]A 'crash.log' has been created. Exiting.[/bold red]")
        sys.exit(1)

bootstrap()
logger = logging.getLogger(__name__)

def main():
    """Application entry point. Initializes and runs the Textual UI."""
    try:
        logger.info("Corvus application starting up.")
        from corvus_app.ui.tui import CorvusTUI
        app = CorvusTUI()
        app.run()
    except Exception:
        logger.critical("A critical unhandled error occurred in the main application.", exc_info=True)
        with open("crash.log", "a", encoding="utf-8") as f:
            f.write(f"\n\n--- Corvus Crash Report (Runtime) ---\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            traceback.print_exc(file=f)
        _console.print(f"\n[bold red on white] AN UNRECOVERABLE ERROR OCCURRED [/]")
        _console.print("[bold red]The full error has been saved to 'crash.log'[/bold red]")
        sys.exit(1)
    finally:
        logger.info("Application shutdown sequence finished.\n\n")

if __name__ == "__main__":
    main()
```

### File: `/corvus_app/screens/__init__.py`
```py
# This file makes the 'screens' directory a Python sub-package.
```

### File: `/corvus_app/screens/conversation_screen.py`
```py
# corvus_app/ui/screens/conversation_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, ListView

from corvus_app import config
from corvus_app.assistant import Assistant
from corvus_app.audio.stt import listen_for_audio
from corvus_app.tts.tts_engine import speak_text
from corvus_app.ui.tui import AssistantResponse, StatusUpdate, ConversationListItem

logger = logging.getLogger(__name__)

class ConversationScreen(Screen):
    BINDINGS = [("tab", "toggle_input_mode", "Toggle Input")]
    
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
        self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")

    def listen_for_wake_word(self):
        self.app.post_message(StatusUpdate("LISTENING..."))
        while self.input_mode == "voice" and self.assistant.is_running:
            text = listen_for_audio()
            if text and config.WAKE_WORD in text:
                prompt = text.replace(config.WAKE_WORD, "", 1).strip()
                if prompt:
                    self.app.post_message(StatusUpdate("PROCESSING..."))
                    self.run_worker(self.process_prompt, prompt, thread=True, exclusive=True, group="processing")
                else:
                    self.app.post_message(StatusUpdate("Yes?"))
                    self.run_worker(self.speak_and_reset_status, "Yes?", thread=True, exclusive=True, group="audio_output")
                return

    def process_prompt(self, prompt: str):
        response = self.assistant.process_prompt(prompt)
        self.post_message(AssistantResponse(response, prompt))
        if not self.assistant.is_running:
            self.app.call_from_thread(self.app.exit)
        else:
            self.run_worker(self.speak_and_reset_status, response, thread=True, exclusive=True, group="audio_output")

    def speak_and_reset_status(self, text: str):
        speak_text(text)
        if self.input_mode == "voice":
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")
        else:
            self.app.post_message(StatusUpdate("TYPING..."))
    
    def action_toggle_input_mode(self) -> None:
        text_input = self.query_one("#text-input", Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.disabled = False
            text_input.focus()
            self.app.cancel_workers(group="audio_input")
            self.post_message(StatusUpdate("TYPING..."))
        else:
            self.input_mode = "voice"
            text_input.disabled = True
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")
            
    async def on_input_submitted(self, message: Input.Submitted) -> None:
        prompt = message.value
        if prompt:
            message.input.value = ""
            self.post_message(StatusUpdate("PROCESSING..."))
            self.run_worker(self.process_prompt, prompt, thread=True, exclusive=True, group="processing")
        self.set_focus(None)

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        list_view = self.query_one(ListView)
        list_view.append(ConversationListItem(message.user_prompt, "user"))
        list_view.append(ConversationListItem(message.text, "assistant"))
        list_view.scroll_end()

    async def on_status_update(self, message: StatusUpdate) -> None:
        self.query_one(Footer).border_title = message.text
```

### File: `/corvus_app/screens/models_screen.py`
```py
# corvus_app/ui/screens/models_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Input, Button, Static, ProgressBar

from corvus_app.app_settings import settings_manager
from models import llm_manager, tts_manager, hf_utils

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
        self.run_worker(self.fetch_remote_tts_models, thread=True)
    
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
                self.run_worker(self.fetch_hf_files, repo_id, thread=True)

    def action_download_selected(self) -> None:
        hf_table = self.query_one("#hf-files-table")
        tts_table = self.query_one("#tts-remote-table")
        try:
            if hf_table.has_focus:
                row_key = hf_table.get_row_key(hf_table.cursor_row)
                filename = hf_table.get_cell(row_key, "GGUF File")
                if row_key and filename: self.app.push_screen(DownloadScreen(url=row_key, filename=filename))
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name: self.app.push_screen(TTSDownloadScreen(model_name=model_name))
        except KeyError: logger.warning("Download triggered with no row selected.")

    def action_delete_selected(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus:
                filepath = llm_table.get_row_key(llm_table.cursor_row)
                if filepath and llm_manager.delete_model(filepath):
                    if settings_manager.get("active_llm_model") == filepath: settings_manager.set("active_llm_model", None)
                    self.update_llm_table()
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name and tts_manager.delete_model(model_name):
                    if settings_manager.get("active_tts_model") == model_name: settings_manager.set("active_tts_model", "tts_models/en/ljspeech/vits")
                    self.update_tts_tables()
        except KeyError: logger.warning("Delete triggered with no row selected.")

    def action_set_active(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus:
                row_key = llm_table.get_row_key(llm_table.cursor_row)
                if row_key: settings_manager.set("active_llm_model", row_key)
                self.update_llm_table()
            elif tts_table.has_focus:
                row_key = tts_table.get_row_key(tts_table.cursor_row)
                if row_key: settings_manager.set("active_tts_model", row_key)
                self.update_tts_tables()
        except KeyError: logger.warning(f"Set Active triggered with no row selected.")

class DownloadScreen(Screen):
    def __init__(self, url: str, filename: str):
        super().__init__()
        self.url = url
        self.filename = filename

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading: {self.filename}", id="progress-label"),
            Horizontal(Static("Starting...", id="progress-stats"), classes="stats_bar"),
            ProgressBar(total=100, id="download-progress"), id="progress-dialog")
    
    def on_mount(self) -> None: self.run_worker(self.download_model_file, thread=True)
    
    def on_download_progress(self, event: str, total_size: int = 0, downloaded: int = 0, message: str = ""):
        def update_ui():
            pb = self.query_one(ProgressBar)
            stats = self.query_one("#progress-stats")
            if event == "start":
                pb.total = total_size or 100
                stats.update("Connecting...")
            elif event == "update":
                pb.update(progress=downloaded)
                total_mb = (pb.total or 0) / (1024 * 1024)
                dl_mb = downloaded / (1024 * 1024)
                percent = (downloaded / pb.total * 100) if pb.total else 0
                stats.update(f"{dl_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)")
            elif event == "finish":
                if (ms := self.app.get_screen("models")): ms.update_llm_table()
                self.app.pop_screen()
            elif event == "error": self.app.pop_screen()
        self.call_from_thread(update_ui)

    def download_model_file(self) -> None: llm_manager.download_model(self.url, self.filename, self.on_download_progress)

class TTSDownloadScreen(Screen):
    def __init__(self, model_name: str):
        super().__init__()
        self.model_name = model_name

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading TTS Model: {self.model_name}", id="progress-label"),
            Static("This may take a few minutes...", id="progress-stats"), id="progress-dialog")

    def on_mount(self) -> None: self.run_worker(self.download_tts_model, thread=True)

    def on_download_finished(self, event: str, message: str = ""):
        def update_ui():
            if (ms := self.app.get_screen("models")): ms.update_tts_tables()
            self.app.pop_screen()
        self.call_from_thread(update_ui)
    
    def download_tts_model(self) -> None: tts_manager.download_model(self.model_name, self.on_download_finished)
```

### File: `/corvus_app/tts/__init__.py`
```py
# This file makes the 'tts' directory a Python sub-package.
```

### File: `/corvus_app/tts/tts_engine.py`
```py
# corvus_app/tts/tts_engine.py
import logging
import sys
import subprocess
from pathlib import Path
from TTS.api import TTS as CoquiTTS
from corvus_app.app_settings import settings_manager

logger = logging.getLogger(__name__)

class TTSEngine:
    _instance = None
    _current_model_name: str | None = None
    _tts: CoquiTTS | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TTSEngine, cls).__new__(cls)
            cls._instance.reload_model()
        return cls._instance

    def reload_model(self):
        model_name = settings_manager.get("active_tts_model")
        if self._tts and self._current_model_name == model_name:
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
        logger.debug(f"Playing audio file: {file_path}")
        try:
            abs_path = Path(file_path).resolve()
            if sys.platform == "win32":
                ps_command = f"(New-Object Media.SoundPlayer '{abs_path}').PlaySync();"
                subprocess.run(["powershell", "-Command", ps_command], check=True, capture_output=True)
            elif sys.platform == "darwin":
                subprocess.run(["afplay", str(abs_path)], check=True, capture_output=True)
            else:
                subprocess.run(["aplay", str(abs_path)], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            logger.error(f"Failed to play audio. Error: {e}", exc_info=True)

    def speak(self, text: str):
        if not text or self._tts is None:
            if self._tts is None: logger.warning("TTS is not available. Cannot speak.")
            return
        
        try:
            logger.debug(f"Synthesizing speech for text: '{text[:50]}...'")
            self._tts.tts_to_file(text=text, file_path="output.wav")
            self._play_audio("output.wav")
        except Exception as e:
            logger.error(f"Failed to synthesize or play speech: {e}", exc_info=True)

def speak_text(text: str):
    engine = TTSEngine()
    engine.speak(text)
```

### File: `/corvus_app/ui/__init__.py`
```py
# This file makes the 'ui' directory a Python sub-package.
```

### File: `/corvus_app/ui/screens/__init__.py`
```py
# This file makes the 'screens' directory a Python sub-package.
```

### File: `/corvus_app/ui/screens/conversation_screen.py`
```py
# corvus_app/ui/screens/conversation_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, Input, ListView

from corvus_app import config
from corvus_app.assistant import Assistant
from corvus_app.audio.stt import listen_for_audio
from corvus_app.tts.tts_engine import speak_text
from corvus_app.ui.tui import AssistantResponse, StatusUpdate, ConversationListItem

logger = logging.getLogger(__name__)

class ConversationScreen(Screen):
    BINDINGS = [("tab", "toggle_input_mode", "Toggle Input")]
    
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
        self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")

    def listen_for_wake_word(self):
        self.app.post_message(StatusUpdate("LISTENING..."))
        while self.input_mode == "voice" and self.assistant.is_running:
            text = listen_for_audio()
            if text and config.WAKE_WORD in text:
                prompt = text.replace(config.WAKE_WORD, "", 1).strip()
                if prompt:
                    self.app.post_message(StatusUpdate("PROCESSING..."))
                    self.run_worker(self.process_prompt, prompt, thread=True, exclusive=True, group="processing")
                else:
                    self.app.post_message(StatusUpdate("Yes?"))
                    self.run_worker(self.speak_and_reset_status, "Yes?", thread=True, exclusive=True, group="audio_output")
                return

    def process_prompt(self, prompt: str):
        response = self.assistant.process_prompt(prompt)
        self.post_message(AssistantResponse(response, prompt))
        if not self.assistant.is_running:
            self.app.call_from_thread(self.app.exit)
        else:
            self.run_worker(self.speak_and_reset_status, response, thread=True, exclusive=True, group="audio_output")

    def speak_and_reset_status(self, text: str):
        speak_text(text)
        if self.input_mode == "voice":
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")
        else:
            self.app.post_message(StatusUpdate("TYPING..."))
    
    def action_toggle_input_mode(self) -> None:
        text_input = self.query_one("#text-input", Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.disabled = False
            text_input.focus()
            self.app.cancel_workers(group="audio_input")
            self.post_message(StatusUpdate("TYPING..."))
        else:
            self.input_mode = "voice"
            text_input.disabled = True
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")
            
    async def on_input_submitted(self, message: Input.Submitted) -> None:
        prompt = message.value
        if prompt:
            message.input.value = ""
            self.post_message(StatusUpdate("PROCESSING..."))
            self.run_worker(self.process_prompt, prompt, thread=True, exclusive=True, group="processing")
        self.set_focus(None)

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        list_view = self.query_one(ListView)
        list_view.append(ConversationListItem(message.user_prompt, "user"))
        list_view.append(ConversationListItem(message.text, "assistant"))
        list_view.scroll_end()

    async def on_status_update(self, message: StatusUpdate) -> None:
        footer = self.query_one(Footer)
        footer.border_title = message.text
```

### File: `/corvus_app/ui/screens/models_screen.py`
```py
# corvus_app/ui/screens/models_screen.py
import logging
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Input, Button, Static, ProgressBar

from corvus_app.app_settings import settings_manager
from models import llm_manager, tts_manager, hf_utils

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
        self.run_worker(self.fetch_remote_tts_models, thread=True)
    
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
                self.run_worker(self.fetch_hf_files, repo_id, thread=True)

    def action_download_selected(self) -> None:
        hf_table = self.query_one("#hf-files-table")
        tts_table = self.query_one("#tts-remote-table")
        try:
            if hf_table.has_focus:
                row_key = hf_table.get_row_key(hf_table.cursor_row)
                filename = hf_table.get_cell(row_key, "GGUF File")
                if row_key and filename: self.app.push_screen(DownloadScreen(url=row_key, filename=filename))
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name: self.app.push_screen(TTSDownloadScreen(model_name=model_name))
        except KeyError: logger.warning("Download triggered with no row selected.")

    def action_delete_selected(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus:
                filepath = llm_table.get_row_key(llm_table.cursor_row)
                if filepath and llm_manager.delete_model(filepath):
                    if settings_manager.get("active_llm_model") == filepath: settings_manager.set("active_llm_model", None)
                    self.update_llm_table()
            elif tts_table.has_focus:
                model_name = tts_table.get_row_key(tts_table.cursor_row)
                if model_name and tts_manager.delete_model(model_name):
                    if settings_manager.get("active_tts_model") == model_name: settings_manager.set("active_tts_model", "tts_models/en/ljspeech/vits")
                    self.update_tts_tables()
        except KeyError: logger.warning("Delete triggered with no row selected.")

    def action_set_active(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus:
                row_key = llm_table.get_row_key(llm_table.cursor_row)
                if row_key: settings_manager.set("active_llm_model", row_key)
                self.update_llm_table()
            elif tts_table.has_focus:
                row_key = tts_table.get_row_key(tts_table.cursor_row)
                if row_key: settings_manager.set("active_tts_model", row_key)
                self.update_tts_tables()
        except KeyError: logger.warning(f"Set Active triggered with no row selected.")

class DownloadScreen(Screen):
    def __init__(self, url: str, filename: str):
        super().__init__()
        self.url = url
        self.filename = filename

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading: {self.filename}", id="progress-label"),
            Horizontal(Static("Starting...", id="progress-stats"), classes="stats_bar"),
            ProgressBar(total=100, id="download-progress"), id="progress-dialog")
    
    def on_mount(self) -> None: self.run_worker(self.download_model_file, thread=True)
    
    def on_download_progress(self, event: str, total_size: int = 0, downloaded: int = 0, message: str = ""):
        def update_ui():
            pb = self.query_one(ProgressBar)
            stats = self.query_one("#progress-stats")
            if event == "start":
                pb.total = total_size or 100
                stats.update("Connecting...")
            elif event == "update":
                pb.update(progress=downloaded)
                total_mb = (pb.total or 0) / (1024 * 1024)
                dl_mb = downloaded / (1024 * 1024)
                percent = (downloaded / pb.total * 100) if pb.total else 0
                stats.update(f"{dl_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)")
            elif event == "finish":
                if (ms := self.app.get_screen("models")): ms.update_llm_table()
                self.app.pop_screen()
            elif event == "error": self.app.pop_screen()
        self.call_from_thread(update_ui)

    def download_model_file(self) -> None: llm_manager.download_model(self.url, self.filename, self.on_download_progress)

class TTSDownloadScreen(Screen):
    def __init__(self, model_name: str):
        super().__init__()
        self.model_name = model_name

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading TTS Model: {self.model_name}", id="progress-label"),
            Static("This may take a few minutes...", id="progress-stats"), id="progress-dialog")

    def on_mount(self) -> None: self.run_worker(self.download_tts_model, thread=True)

    def on_download_finished(self, event: str, message: str = ""):
        def update_ui():
            if (ms := self.app.get_screen("models")): ms.update_tts_tables()
            self.app.pop_screen()
        self.call_from_thread(update_ui)
    
    def download_tts_model(self) -> None: tts_manager.download_model(self.model_name, self.on_download_finished)
```

### File: `/corvus_app/ui/tui.css`
```css
/* corvus_app/ui/tui.css */

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

### File: `/corvus_app/ui/tui.py`
```py
# corvus_app/ui/tui.py
import logging
from textual.app import App, ComposeResult
from textual.widgets import ListItem, Label

from corvus_app.assistant import Assistant
from corvus_app.ui.screens.conversation_screen import ConversationScreen
from corvus_app.ui.screens.models_screen import ModelsScreen

logger = logging.getLogger(__name__)

class AssistantResponse:
    """Posted when the assistant generates a response."""
    def __init__(self, text: str, user_prompt: str):
        self.text = text
        self.user_prompt = user_prompt

class StatusUpdate:
    """Posted to update the status in the footer."""
    def __init__(self, text: str):
        self.text = text

class ConversationListItem(ListItem):
    """A ListItem that displays a formatted conversation entry."""
    def __init__(self, content: str, role: str, **kwargs):
        super().__init__(**kwargs)
        self.content = content
        self.role = role
    
    def compose(self) -> ComposeResult:
        """Create the displayable content for the list item."""
        style = "bold cyan" if self.role == "user" else "bold green"
        yield Label(f"[{style}]{self.role.capitalize()}:[/] {self.content}")

class CorvusTUI(App):
    """The main Textual application for Corvus."""
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
        """Toggles the visibility of the Models screen."""
        if isinstance(self.screen, ModelsScreen):
            self.pop_screen()
            logger.info("Closing models screen, reloading components.")
            # Reload assistant and TTS engine in case models were changed
            self.assistant.reload()
            from corvus_app.tts.tts_engine import TTSEngine
            TTSEngine().reload_model()
        else:
            self.push_screen("models")
    
    async def on_assistant_response(self, message: AssistantResponse):
        """Handles the AssistantResponse message event."""
        if isinstance(self.screen, ConversationScreen):
            await self.screen.on_assistant_response(message)
    
    async def on_status_update(self, message: StatusUpdate):
        """Handles the StatusUpdate message event."""
        if isinstance(self.screen, ConversationScreen):
            await self.screen.on_status_update(message)
```

### File: `/installer.log`
```log
2025-08-03 20:30:31,526 [INFO    ]  Virtual environment is missing or incomplete. Recreating...
2025-08-03 20:30:39,856 [INFO    ]  Virtual environment created successfully.
2025-08-03 20:30:39,861 [INFO    ]  Installing dependencies (this may take several minutes)...
2025-08-03 20:30:39,864 [INFO    ]  Running command: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt

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
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Footer, Header, ProgressBar, RichLog, Static

# --- Basic Setup ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"

if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
    PYTHON_CMD = "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"
    PYTHON_CMD = "python3"

# --- Logging ---
def setup_installer_logging():
    log_formatter = logging.Formatter("%(asctime)s [%(levelname)-8.8s]  %(message)s")
    log_file_handler = RotatingFileHandler(PROJECT_ROOT / "installer.log", maxBytes=2*1024*1024, backupCount=1, encoding="utf-8")
    log_file_handler.setFormatter(log_formatter)
    logger = logging.getLogger("installer")
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(log_file_handler)
    return logger

logger = setup_installer_logging()

class TuiLogHandler(logging.Handler):
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
            self.app.call_from_thread(self.get_widget().write, self.format(record))
        except Exception:
            pass

class InstallerApp(App):
    CSS_PATH = PROJECT_ROOT / "installer" / "installer.css"
    TITLE = "Corvus App Launcher"

    def compose(self) -> ComposeResult:
        with Container(id="installer-container"):
            yield Header("Corvus App Installer")
            yield RichLog(id="installer-log", wrap=True, highlight=True)
            yield ProgressBar(id="progress-bar", show_eta=True)
            with Footer():
                yield Static("Status: Initializing...", id="status-line")

    def on_mount(self) -> None:
        logger.addHandler(TuiLogHandler(self))
        self.run_worker(self.run_installation, thread=True, exclusive=True)

    def update_status(self, message: str):
        self.call_from_thread(self.query_one("#status-line", Static).update, f"Status: {message}")
        logger.info(message)

    def run_installation(self):
        try:
            self.ensure_venv()
            self.install_dependencies()
            self.create_env_file()
            self.update_status("Setup complete. The main application will now launch.")
            self.call_from_thread(self.app.exit, True)
        except Exception as e:
            self.update_status(f"[bold red]Installation failed: {e}[/]")
            logger.error("FATAL ERROR in installation orchestrator:", exc_info=True)
            self.call_from_thread(lambda: setattr(self.query_one(Footer).styles, 'background', 'red'))
            self.call_from_thread(self.app.exit, False)

    def ensure_venv(self):
        if VENV_PYTHON.exists():
            self.update_status("Valid virtual environment found.")
            return
        self.update_status("Virtual environment is missing or incomplete. Recreating...")
        if VENV_DIR.exists():
            shutil.rmtree(VENV_DIR)
        
        sys_python = shutil.which(PYTHON_CMD.replace(".exe", ""))
        if not sys_python: raise RuntimeError("Could not find system Python executable.")
        
        process = subprocess.run([sys_python, "-m", "venv", str(VENV_DIR)], capture_output=True, text=True, encoding='utf-8')
        if process.returncode != 0: raise RuntimeError(f"Venv creation failed: {process.stderr}")
        self.update_status("Virtual environment created successfully.")

    def install_dependencies(self):
        self.update_status("Installing dependencies (this may take several minutes)...")
        progress_bar = self.query_one(ProgressBar)
        self.call_from_thread(progress_bar.add_class, "visible")
        command = [str(VENV_PYTHON), "-m", "pip", "install", "-r", str(PROJECT_ROOT / "requirements.txt")]
        logger.info(f"Running command: {' '.join(command)}")

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        # CORRECTED: The process object must be passed as an argument to the worker.
        self.run_worker(self.simulate_progress, process, thread=True, group="simulation")

        stdout, stderr = process.communicate()
        self.app.cancel_workers(group="simulation")

        if process.returncode == 0:
            for line in (stdout).splitlines():
                if line.strip(): logger.info(line)
            self.call_from_thread(progress_bar.update, progress=100)
            self.update_status("Dependencies installed successfully!")
            MARKER_FILE.touch()
        else:
            for line in (stdout + stderr).splitlines():
                if line.strip(): logger.error(line)
            raise RuntimeError("Dependency installation failed.")

    def simulate_progress(self, process):
        progress_bar = self.query_one(ProgressBar)
        estimated_duration = 420
        start_time = time.time()
        while process.poll() is None:
            progress = min(98, (time.time() - start_time) / estimated_duration * 100)
            self.call_from_thread(progress_bar.update, total=100, progress=progress)
            time.sleep(1)

    def create_env_file(self):
        self.update_status("Setting up configuration...")
        if not (PROJECT_ROOT / ".env").exists():
            shutil.copy(PROJECT_ROOT / ".env.example", PROJECT_ROOT / ".env")
```

### File: `/models/__init__.py`
```py
# This file makes 'models' a Python package.
```

### File: `/models/downloader.py`
```py
# models/downloader.py
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
# models/hf_utils.py
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
# models/llm_manager.py
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
# models/tts_manager.py
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
# plugins/base.py
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corvus_app.assistant import Assistant

class Command(ABC):
    """Abstract base class for all command plugins."""
    @property
    @abstractmethod
    def keywords(self) -> list[str]:
        pass

    def matches(self, text: str) -> bool:
        return any(keyword in text.lower() for keyword in self.keywords)

    @abstractmethod
    def execute(self, assistant: "Assistant") -> str:
        pass
```

### File: `/plugins/exit_command.py`
```py
# plugins/exit_command.py
from .base import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corvus_app.assistant import Assistant

class ExitCommand(Command):
    """Command to gracefully shut down the assistant."""
    @property
    def keywords(self) -> list[str]:
        return ["exit", "shutdown", "stop", "goodbye"]

    def execute(self, assistant: "Assistant") -> str:
        assistant.is_running = False 
        return "Shutting down now. Goodbye!"
```

### File: `/plugins/registry.py`
```py
# plugins/registry.py
import importlib
import logging
from pathlib import Path
from .base import Command

logger = logging.getLogger(__name__)

class CommandRegistry:
    """Discovers, loads, and manages command plugins."""
    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = Path(plugins_dir)
        logger.info(f"Initializing CommandRegistry, scanning '{self.plugins_dir}' for plugins.")
        self.commands: list[Command] = self._discover_plugins()
        logger.info(f"Discovered and loaded {len(self.commands)} command(s).")

    def _discover_plugins(self) -> list[Command]:
        loaded_commands = []
        for file_path in self.plugins_dir.glob("*_command.py"):
            if file_path.name.startswith("__"):
                continue
            
            module_name = ".".join(file_path.with_suffix("").parts)
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
        for command in self.commands:
            if command.matches(text):
                return command
        return None
```

### File: `/plugins/time_command.py`
```py
# plugins/time_command.py
from datetime import datetime
from .base import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corvus_app.assistant import Assistant

class TimeCommand(Command):
    """A command to get the current time."""
    @property
    def keywords(self) -> list[str]:
        return ["time", "date"]

    def execute(self, assistant: "Assistant") -> str:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p").lstrip("0")
        return f"The current time is {current_time}."
```

### File: `/requirements.txt`
```txt
llama-cpp-python
SpeechRecognition
rich
python-dotenv
textual==0.58.0
TTS
requests
beautifulsoup4
```

### File: `/run.py`
```py
# run.py
import sys
import subprocess
import os
from importlib.metadata import version, PackageNotFoundError
from pathlib import Path

# --- Configuration ---
TEXTUAL_VERSION = "0.58.0"
PKG_NAME = "textual"
REQUIRED_PKG = f"{PKG_NAME}=={TEXTUAL_VERSION}"
PROJECT_ROOT = Path(__file__).resolve().parent
VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"
if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"


def check_and_install_textual():
    """Ensures the correct version of Textual is available to run the installer."""
    try:
        if version(PKG_NAME) == TEXTUAL_VERSION:
            print(f"[INFO] Found correct Textual version ({TEXTUAL_VERSION}).")
            return True
        print(f"[BOOTSTRAP] Found Textual {version(PKG_NAME)}, but require {TEXTUAL_VERSION}. Re-installing...")
    except PackageNotFoundError:
        print(f"[BOOTSTRAP] Textual not found. Attempting to install {REQUIRED_PKG}...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", REQUIRED_PKG])
        print("[BOOTSTRAP] Textual prepared successfully.")
        return True
    except subprocess.CalledProcessError:
        print(f"[FATAL] Failed to install {REQUIRED_PKG}. Please check your network and run again.")
        return False

def launch_installer():
    """Runs the installer UI application."""
    print("Launching Installer UI...")
    from installer.installer_tui import InstallerApp
    app = InstallerApp()
    app.run()
    return MARKER_FILE.exists()

def launch_main_app():
    """Launches the main Corvus application."""
    print("Launching Corvus Application...")
    main_app_module = "corvus_app.main"
    command = [str(VENV_PYTHON), "-m", main_app_module]
    env = os.environ.copy()
    env['PYTHONPATH'] = str(PROJECT_ROOT)

    try:
        subprocess.run(command, env=env, check=True)
    except subprocess.CalledProcessError:
        print("[FATAL] Corvus application closed with an error. Check logs for details.")
    except FileNotFoundError:
        print(f"[FATAL] Could not find the application entry point. Venv might be corrupt.")

def main():
    """Main entry point for the application launcher."""
    print("Initializing Corvus...")
    if MARKER_FILE.exists():
        launch_main_app()
    else:
        if not check_and_install_textual():
            input("Press Enter to exit.")
            sys.exit(1)
        if launch_installer():
            launch_main_app()
        else:
            print("[FATAL] Installation did not complete successfully.")
            input("Press Enter to exit.")

if __name__ == "__main__":
    main()
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