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
├── audio
│   ├── __init__.py
│   └── stt.py
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
├── .env
├── .env.example
├── .gitignore
├── __init__.py
├── app_settings.py
├── assistant.py
├── assistant_app.log
├── assistant_app.py
├── config.py
├── logging_config.py
├── main.py
├── README.md
├── requirements.txt
├── start.bat
└── start.sh
```

## Project Files

### File: `/.env`
```text
# Assistant App Configuration
# Rename this file to .env and fill in the values.

# The model name to use for the assistant (e.g., "llama3", "mistral")
# Make sure you have pulled this model using 'ollama pull <model_name>'
MODEL="llama3"

# The host URL for the Ollama service
OLLAMA_HOST="http://localhost:11434"

# The wake word required to activate the assistant
WAKE_WORD="computer"

# Set to "true" to see verbose logs, otherwise "false"
DEBUG="false"
```

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
.Python
env/
venv/
pip-selfcheck.json
.DS_Store

# IDEs
.idea/
.vscode/

# Build artifacts
build/
dist/
*.egg-info/

# Log files
*.log
crash.log

# Local data and models
settings.json
tts_models/
llm_models/
output.wav
```

### File: `/README.md`
```md
# Assistant App

This project is a fully interactive AI assistant for your terminal, powered by locally-run GGUF language models and a customizable TTS engine. It operates completely offline and privately.

## !! Critical Troubleshooting !!

If you see logs mentioning **"NiceGUI"** or **"Ollama"**, it means old, conflicting files are present in your project directory. Please perform a manual cleanup:

1.  **Delete the entire `venv` folder.**
2.  **Delete any `.py` files in the main project folder** EXCEPT for `start.bat`, `start.sh`, and `requirements.txt`.
3.  Ensure the `assistant_app` folder and all its contents match the files provided in the latest update.
4.  Run `start.bat` or `start.sh` again. This will create a fresh, clean environment.

## Features

-   **No External Dependencies:** Runs without requiring any external service.
-   **Direct GGUF Model Support:** Uses `llama-cpp-python` to run GGUF model files directly.
-   **Hugging Face Integration:** Browse and download LLM models directly from Hugging Face repositories.
-   **Interactive Model Management:** A dedicated UI screen to find, download, delete, and manage both LLM (GGUF) and TTS models.
-   **Truly Interactive TUI:** A modern terminal application with distinct modes for voice or text input.
-   **One-Step Setup:** A single script handles environment creation, dependency installation, and application launch.

## Quickstart

Just run the script for your operating system. The first run will handle all setup.

**On macOS or Linux:**
```bash
# Make the script executable first (only needs to be done once)
chmod +x start.sh

./start.sh```

**On Windows:**
```bat
start.bat
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

### File: `/assistant_app.log`
```log
2025-07-31 12:04:36,662 - INFO - Verifying Dependencies...
2025-07-31 12:04:36,733 - INFO - All dependencies are met. Ollama is running.
2025-07-31 12:04:41,789 - INFO - Loading core AI models. This may take a moment on first run...
2025-07-31 12:04:47,315 - INFO - Generating default voice speaker embedding...
2025-07-31 12:04:47,315 - INFO - All core models loaded successfully.

```

### File: `/assistant_app.py`
```py
# ==============================================================================
# Local AI Voice Assistant - A Final, Radically Simplified, and Correct Application
# ==============================================================================

# --- Step 1: Check and Install Dependencies ---
import subprocess
import sys
import pkg_resources

# Minimal requirements to ensure the welcome screen and download works
REQUIRED_PACKAGES = [ "nicegui", "ollama" ]

def check_dependencies():
    print("--- Verifying Dependencies ---")
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = [p for p in REQUIRED_PACKAGES if p.lower() not in installed]
    if missing:
        print(f"Installing missing packages: {', '.join(missing)}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        subprocess.check_call(["ollama", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("All dependencies are met. Ollama is running.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nFATAL ERROR: Ollama is not running. Please start it and run this script again.")
        return False

if not check_dependencies():
    sys.exit(1)


# --- Step 2: Import all necessary libraries ---
import asyncio
import ollama
from nicegui import ui, app

# --- Step 3: Define Static Data ---
TOP_RECOMMENDATIONS = {
    'Small': {'name': 'Phi-3 Mini (3.8B)', 'tag': 'phi3:mini', 'vram': '~3.5 GB'},
    'Medium': {'name': 'Llama 3.1 (8B)', 'tag': 'llama3.1:8b', 'vram': '~5.0 GB'},
    'Large': {'name': 'Mistral (7B)', 'tag': 'mistral:7b', 'vram': '~4.5 GB'}
}
OTHER_GOOD_MODELS = [
    {'name': 'Gemma (7B)', 'tag': 'gemma:7b', 'vram': '~5.0 GB'},
    {'name': 'Llama 3.1 (70B)', 'tag': 'llama3.1:70b', 'vram': '>40 GB'}
]

# --- Step 4: The UI Application ---
@ui.page('/')
async def main_page():
    
    try:
        # --- DEFINITIVE FIX for Ollama connection error ---
        # This function correctly handles the new library format and provides debug info.
        print("Attempting to connect to Ollama...")
        response = ollama.list()
        print(f"DEBUG: Successfully received response from ollama.list(). Raw data type: {type(response)}")
        print(f"DEBUG: Raw data content: {response}")

        # Defensively parse the response, handling both old and new formats
        if isinstance(response, dict) and 'models' in response:
            installed_models = [m['name'] for m in response['models']]
        elif isinstance(response, list):
            installed_models = [m['name'] for m in response]
        else:
            # This handles the case where the response is an object, not a simple dict or list
            installed_models = [m['name'] for m in response.get('models', [])] if hasattr(response, 'get') else []

        print(f"Found installed models: {installed_models}")

    except Exception as e:
        ui.label(f"FATAL ERROR: Could not connect to or parse Ollama's response.").classes('text-red-500 text-2xl p-4')
        ui.label(f"Please ensure Ollama is running and accessible.").classes('text-lg p-4')
        ui.label(f"Details: {e}").classes('text-red-300 p-4')
        return

    # ------------------- WELCOME SCREEN -------------------
    if not installed_models:
        models_to_download = []
        
        def toggle_model_selection(add: bool, tag: str):
            """Simple, direct, and foolproof handler for the checkbox."""
            if add and tag not in models_to_download:
                models_to_download.append(tag)
            elif not add and tag in models_to_download:
                models_to_download.remove(tag)
            
            # This explicitly sets the button state every single time.
            download_button.set_enabled(bool(models_to_download))

        async def download_selected(button, status_container):
            if not models_to_download: return
            button.set_visibility(False)
            with status_container:
                for tag in models_to_download:
                    ui.label(f"Downloading {tag}...")
                    try:
                        await asyncio.to_thread(ollama.pull, tag)
                        ui.label(f"Successfully downloaded {tag}.").classes('text-positive')
                    except Exception as e:
                        ui.label(f"Failed to download {tag}: {e}").classes('text-negative')
            with status_container:
                ui.label("Setup complete! Refreshing...", 'text-positive font-bold mt-4')
                await asyncio.sleep(2)
            ui.navigate.reload()

        with ui.column().classes('w-full h-screen items-center justify-center gap-4 bg-gray-100 dark:bg-gray-900'):
            ui.label("Welcome to Your Local AI Assistant").classes('text-3xl font-bold')
            with ui.column().classes('w-full max-w-4xl gap-4'):
                ui.label("Top Recommendations").classes('text-2xl font-semibold self-center')
                with ui.row().classes('w-full justify-around no-wrap items-stretch'):
                    for category, model in TOP_RECOMMENDATIONS.items():
                        with ui.card().classes('flex-1'):
                            ui.label(category).classes('text-lg font-bold text-primary')
                            ui.label(model['name'])
                            ui.label(f"VRAM: {model['vram']}").classes('text-accent font-bold')
                            ui.checkbox("Select").on('change', lambda e, tag=model['tag']: toggle_model_selection(e.value, tag))

                ui.label("Other Great Models").classes('text-2xl font-semibold self-center mt-4')
                for model in OTHER_GOOD_MODELS:
                    with ui.card().classes('w-full'):
                        with ui.row().classes('w-full items-center'):
                            with ui.column().classes('flex-grow'):
                                ui.label(model['name']).classes('text-md font-semibold')
                                ui.label(f"VRAM: {model['vram']}").classes('font-bold text-accent')
                            ui.checkbox("Select").on('change', lambda e, tag=model['tag']: toggle_model_selection(e.value, tag))
            
            download_button = ui.button("Download Selected & Continue", on_click=lambda: download_selected(download_button, download_status)).props('icon=download size=lg mt-4')
            download_button.disable()
            download_status = ui.column().classes('w-full max-w-4xl items-center mt-4')
    
    # ------------------- MAIN APP SCREEN (Simplified Placeholder) -------------------
    else:
        with ui.column().classes('w-full h-screen items-center justify-center gap-4'):
            ui.icon('check_circle', size='xl').classes('text-green-500')
            ui.label("Setup Complete!").classes('text-4xl font-bold text-green-500')
            ui.label("You have successfully downloaded and installed a model.").classes('text-lg')
            ui.label("The main application chat interface will be built in the next step.").classes('text-md')
            ui.label("Installed Models:").classes('text-lg font-bold mt-4')
            for model in installed_models:
                ui.label(model)
            ui.button('Restart Application', on_click=ui.navigate.reload, color='info').props('icon=refresh')

# --- Entry Point ---
ui.run(title="Local AI Voice Assistant", reload=False, uvicorn_reload_excludes='.*')
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
    from assistant_app.logging_config import setup_logging
    setup_logging()
except Exception:
    # If logging itself fails, we must use the fallback and generate a crash log
    _console.print("[bold red]FATAL: Failed to configure application logging.[/bold red]")
    with open("crash.log", "w", encoding="utf-8") as f:
        f.write(f"--- Assistant App Crash Report (Logging Failure) ---\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("-" * 30 + "\n\n")
        traceback.print_exc(file=f)
    _console.print("[bold red]A 'crash.log' has been created. Exiting.[/bold red]")
    sys.exit(1)

logger = logging.getLogger(__name__)

def main():
    """Application entry point. Initializes and runs the Textual UI."""
    try:
        logger.info("Application starting up.")
        from assistant_app.ui.tui import AssistantTUI
        
        app = AssistantTUI()
        app.run()
    except Exception:
        logger.critical("A critical unhandled error occurred. The application will terminate.", exc_info=True)
        with open("crash.log", "w", encoding="utf-8") as f:
            f.write(f"--- Assistant App Crash Report ---\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write("-" * 30 + "\n\n")
            traceback.print_exc(file=f)

        _console.print(f"\n[bold red on white] AN UNRECOVERABLE ERROR OCCURRED [/]")
        _console.print(f"[bold red]A 'crash.log' file has been created with the full error details.[/bold red]")
        sys.exit(1)
    finally:
        logger.info("Application shutdown sequence finished.\n\n")

if __name__ == "__main__":
    main()
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

logger = logging.getLogger(__name__)

# The directory where TTS models will be stored
TTS_MODELS_PATH = Path("tts_models")
TTS_MODELS_PATH.mkdir(exist_ok=True)

_model_manager = None

def get_model_manager():
    global _model_manager
    if _model_manager is None:
        _model_manager = ModelManager(TTS_MODELS_PATH)
    return _model_manager

def get_remote_models_list():
    """Gets the list of available TTS models from Coqui."""
    try:
        manager = get_model_manager()
        # The `list_models` returns a huge list, we need to filter for tts_models
        all_models = manager.list_models()
        tts_models = [m for m in all_models if "/tts/" in m]
        return sorted(tts_models)
    except Exception as e:
        logger.error(f"Could not fetch remote TTS model list: {e}", exc_info=True)
        return []

def get_local_models_list():
    """Finds installed TTS models by checking for 'model_file.pth'."""
    local_models = set()
    base_path_len = len(TTS_MODELS_PATH.parts)
    for pth_file in TTS_MODELS_PATH.rglob("*.pth"):
        # The model name is the path relative to the TTS_MODELS_PATH directory
        model_path_parts = pth_file.parts[base_path_len:-1]
        if model_path_parts:
            local_models.add("/".join(model_path_parts))
    return sorted(list(local_models))

def download_model(model_name: str, progress_callback: callable):
    """Downloads a Coqui TTS model with progress."""
    logger.info(f"Starting download for TTS model: {model_name}")
    try:
        manager = get_model_manager()
        manager.download_model(model_name, progress_bar=True)
        logger.info(f"Successfully downloaded TTS model: {model_name}")
        progress_callback("finish")
    except Exception as e:
        logger.error(f"Failed to download TTS model {model_name}: {e}", exc_info=True)
        progress_callback("error", message=str(e))
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
llama-cpp-python
SpeechRecognition
rich
python-dotenv
textual
TTS
requests
beautifulsoup4
```

### File: `/start.bat`
```bat
@echo off
setlocal

REM ============================================================================
REM == Assistant App Setup & Launch Script for Windows                      ==
REM ============================================================================
echo [INFO] Starting Assistant App...

REM ** IMPORTANT: Change to the script's directory to ensure all paths are correct. **
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

echo [DIAG] Current working directory: %cd%

REM 1. Check for Python
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH. Please install it to continue.
    pause
    exit /b 1
)

REM 2. Setup Virtual Environment
if not exist "venv" (
    echo [INFO] Virtual environment not found. Creating one...
    python -m venv venv
    echo [SUCCESS] Virtual environment created.
)

REM 3. Activate Virtual Environment and Install Dependencies
echo [INFO] Activating virtual environment...
call "venv\Scripts\activate"

REM Using a marker file to avoid reinstalling dependencies every time
if not exist "venv\deps_installed.marker" (
    echo [INFO] Installing/Verifying required Python packages. This may take several minutes...
    echo [INFO] Note: A C++ compiler is required for the llama-cpp-python package.
    pip install --quiet -r "requirements.txt"
    if %errorlevel% neq 0 (
      echo [ERROR] Failed to install dependencies. Please check your C++ compiler setup and network connection.
      pause
      exit /b 1
    )
    echo. > "venv\deps_installed.marker"
    echo [SUCCESS] Dependencies installed.
) else (
    echo [INFO] Dependencies are already installed.
)

REM 4. Setup Configuration File
if not exist ".env" (
    echo [INFO] Configuration file '.env' not found. Creating from example...
    copy ".env.example" ".env" > nul
    echo [SUCCESS] '.env' created. You can edit this file to change settings.
)

echo.
echo ======================================================
echo [INFO] Launching the Assistant. Press Ctrl+C to exit.
echo ======================================================
echo.

REM Execute the python script. If it exits with an error (||), pause the console.
python -m assistant_app.main || pause

call "venv\Scripts\deactivate"
echo [INFO] Application closed.
endlocal
```

### File: `/start.sh`
```sh
#!/bin/bash
set -e

# Helper functions for colored output
print_info() { echo -e "\033[0;36m[INFO]\033[0m $1"; }
print_success() { echo -e "\033[0;32m[SUCCESS]\033[0m $1"; }
print_error() { echo -e "\033[0;31m[ERROR]\033[0m $1"; }

# ** IMPORTANT: Change to the script's directory before doing anything else. **
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"

print_info "Starting Assistant App..."
print_info "Current working directory: $(pwd)"

# 1. Check for Python 3
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install it to continue."
    exit 1
fi

# 2. Setup Virtual Environment
if [ ! -d "venv" ]; then
    print_info "Virtual environment not found. Creating..."
    python3 -m venv venv
    print_success "Virtual environment created."
fi

# 3. Activate Virtual Environment
source venv/bin/activate

# 4. Install Dependencies
if [ ! -f "venv/deps_installed.marker" ]; then
    print_info "Installing/Verifying Python packages. This may take several minutes..."
    print_info "Note: A C++ compiler (build-essential, Xcode tools) is required."
    pip install --quiet -r requirements.txt
    touch venv/deps_installed.marker
    print_success "Dependencies installed."
else
    print_info "Dependencies are already installed."
fi

# 5. Create .env file
if [ ! -f ".env" ]; then
    print_info "Configuration file '.env' not found. Creating from example..."
    cp .env.example .env
    print_success "'.env' created. You can edit this file to change settings."
fi

echo
echo "======================================================"
print_info "Launching the Assistant. Press Ctrl+C to exit."
echo "======================================================"
echo

# 6. Launch the main application
python3 -m assistant_app.main

deactivate
print_info "Application closed."
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
from pathlib import Path
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, DataTable, Input, Button, Static
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
    """A modal screen for showing download progress."""
    def __init__(self, url: str, filename: str):
        super().__init__()
        self.url = url
        self.filename = filename

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading {self.filename}", id="progress-label"),
            Static("[...]", id="progress-percent"),
            ProgressBar(total=100, show_eta=True, id="download-progress"),
            id="progress-dialog"
        )
    
    def on_mount(self) -> None:
        self.download_model_file()
    
    @work(exclusive=True)
    def download_model_file(self):
        llm_manager.download_model(self.url, self.filename, self.on_download_progress)

    def on_download_progress(self, event, total_size=0, downloaded=0, message=""):
        progress_bar = self.query_one("#download-progress")
        percent_label = self.query_one("#progress-percent")
        if event == "start":
            progress_bar.total = total_size
        elif event == "update":
            progress_bar.update(progress=downloaded)
            if progress_bar.total:
                percent = (downloaded / progress_bar.total) * 100
                percent_label.update(f"{percent:.1f}%")
        elif event == "finish":
            # Update the models screen underneath before closing
            self.app.get_screen("models").update_llm_table()
            self.app.pop_screen()
        elif event == "error":
            # Could add an error message, but for now just close
            self.app.pop_screen()
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