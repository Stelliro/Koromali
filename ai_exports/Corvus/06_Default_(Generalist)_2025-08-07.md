---SYSTEM-PROMPT---

You are an expert software developer. Your task is to modify the user's project based on their instructions.
## Golden Rules
- Your response MUST ONLY contain file modifications, creations, or deletions.
- Enclose each file's content in the standard `### File: /path/to/file.ext` format.
- Do not add any extra commentary, explanations, or summaries outside of the code blocks.
- To modify or create a file, provide its complete content in a markdown code block (e.g., ```python ... ```).
- IMPORTANT: If a file's content itself contains '```', use a fenced code block with more backticks (e.g., `````python) for the outer block to prevent parsing errors.
- To delete a file, follow the file path with `---DELETED---` on a new line.
- If a file from the user's prompt is not being changed, do not include it in your response.
- Ensure file paths are relative to the project root and use forward slashes (e.g., `app_core/main.py`).
- Maintain existing code style and conventions for all unchanged parts of modified files.

---USER-PROMPT---

# Project Task...

## Project File Tree:
```
Corvus
├── corvus_app
│   ├── assets
│   │   ├── sounds
│   │   │   ├── __init__.py
│   │   │   ├── button_press.wav [UNSUPPORTED BINARY]
│   │   │   └── README.md
│   │   └── __init__.py
│   ├── audio
│   │   ├── __init__.py
│   │   ├── device_manager.py
│   │   ├── sound_player.py
│   │   └── stt.py
│   ├── llm
│   │   ├── __init__.py
│   │   └── llm_client.py
│   ├── tools
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   └── user_profile.py
│   ├── tts
│   │   ├── __init__.py
│   │   └── tts_engine.py
│   ├── ui
│   │   ├── screens
│   │   │   ├── __init__.py
│   │   │   ├── confirm_screen.py
│   │   │   ├── download_screen.py
│   │   │   └── main_screen.py
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── shared.py
│   │   ├── themes.py
│   │   ├── tui.css
│   │   ├── tui.py
│   │   └── worker.py
│   ├── __init__.py
│   ├── app_settings.py
│   ├── assistant.py
│   ├── config.py
│   ├── crash_handler.py
│   ├── logging_config.py
│   └── main.py
├── installer
│   ├── __init__.py
│   ├── installer.css
│   └── installer_tui.py
├── models
│   ├── __init__.py
│   ├── downloader.py
│   ├── stt_manager.py
│   └── tts_manager.py
├── plugins
│   ├── __init__.py
│   ├── base.py
│   ├── exit_command.py
│   ├── registry.py
│   └── time_command.py
├── .env
├── .env.example
├── .gitignore
├── __init__.py
├── corvus_app.log
├── corvus_crash_report.log
├── corvus_daemon.log
├── daemon_process.py
├── installer.log
├── README.md
├── requirements.txt
├── run.py
├── settings.json
├── start.bat
├── start.sh
└── user_profile.md
```

## Project Files

### File: `/.env`
```text
# Assistant App Configuration
# This file is used to create your .env file on first run.
# These values can be changed later within the application's settings screen.

# The wake word required to activate the assistant
WAKE_WORD="computer"

# The level of detail for logs. Can be DEBUG, INFO, WARNING, ERROR, CRITICAL.
LOG_LEVEL="INFO"
```

### File: `/.env.example`
```example
# Assistant App Configuration
# This file is used to create your .env file on first run.
# These values can be changed later within the application's settings screen.

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

# Logs and settings
*.log
settings.json
output.wav
user_profile.md

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
# Corvus AI Assistant

Corvus is a voice-activated AI assistant that runs locally on your machine. It uses powerful open-source models for speech recognition, language understanding, and text-to-speech, providing a private and customizable assistant experience.

The application is designed to be adaptive, learning about the user's speech patterns and preferences over time to provide a more personalized interaction.

## Features

-   **Local First**: All models (LLM, STT, TTS) run on your hardware. No data is sent to the cloud.
-   **Adaptive Learning**: The assistant keeps private notes on user speech patterns (like accents or stutters) to improve interactions.
-   **Customizable**: Easily swap out models, change the assistant's personality, and adjust voice settings through a simple terminal UI.
-   **Plugin System**: Extend the assistant's capabilities by adding new commands.

## Getting Started

From the project's root directory (the one containing this `README.md` file), simply run the startup script for your OS:

-   **Windows:**
    ```batch
    .\start.bat
    ```

-   **Linux / macOS:**
    ```bash
    ./start.sh
    ```

The first time you run the script, it will automatically set up a virtual environment and install all necessary dependencies, including the `espeak-ng` engine required for Text-to-Speech.
```

### File: `/__init__.py`
```py
# This file makes 'corvus_app' a Python package.
```

### File: `/corvus_app.log`
```log
2025-08-07 14:14:09,520 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:14:09,520 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_app.log'. Log Level: INFO
2025-08-07 14:14:09,520 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:14:09,520 [MainThread  ] [__main__                 ] [INFO    ]  Main application process starting.
2025-08-07 14:14:11,762 [MainThread  ] [__main__                 ] [INFO    ]  Daemon process started with PID: 36664
2025-08-07 14:14:12,031 [Dummy-1     ] [corvus_app.ui.worker     ] [INFO    ]  QueueListener worker started.
2025-08-07 14:14:16,207 [MainThread  ] [models.tts_manager       ] [INFO    ]  Fetching remote TTS voice index from https://huggingface.co/rhasspy/piper-voices/raw/main/voices.json
2025-08-07 14:14:16,521 [MainThread  ] [models.tts_manager       ] [INFO    ]  Successfully fetched and parsed 133 TTS voices.
2025-08-07 14:14:16,522 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:14:16,523 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:14:16,524 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:14:16,524 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:14:16,525 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'

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

from corvus_app.config import WAKE_WORD as DEFAULT_WAKE_WORD

logger = logging.getLogger(__name__)

class AppSettings:
    """Manages persistent application settings like active models."""
    def __init__(self, file_path: str = "settings.json"):
        self.file_path = Path(file_path)
        self.defaults = {
            "active_llm_model": None,
            "active_tts_model": None, # No default model, user must download one.
            "active_stt_model": "base", # tiny, base, small, medium, large
            "wake_word": DEFAULT_WAKE_WORD,
            "system_prompt": (
                "You are a helpful and adaptive AI assistant. You can learn about the user to improve your interactions.\n"
                "A special file, `user_profile.md`, stores notes about the user's speech and preferences. You will receive its contents with each prompt.\n"
                "You will also receive language detection info with each voice prompt, like `(speaking en with 0.75 confidence)`. A low confidence score may indicate a user's accent.\n\n"
                "YOUR TASK:\n"
                "1. Analyze the user's request, their profile notes, and any language detection info.\n"
                "2. Formulate a direct, helpful response to the user. Be patient and accommodating if an accent is detected.\n"
                "3. If you learn something new about the user (e.g., they have an accent, they stutter, they mispronounce a word), you MUST update their profile.\n\n"
                "HOW TO UPDATE THE PROFILE:\n"
                "Your response MUST be formatted as follows. First the update tag, then the spoken response:\n"
                "`[UPDATE_PROFILE]`\n"
                "The complete, new markdown content for the user's profile.\n"
                "`[/UPDATE_PROFILE]`\n"
                "Your normal, spoken response to the user.\n\n"
                "If no update is needed, just provide the spoken response without any tags.\n\n"
                "EXAMPLE:\n"
                "USER (speaking en with 0.65 confidence): 'Corvus, vhat is ze time?'\n"
                "YOUR RESPONSE SHOULD BE:\n"
                "`[UPDATE_PROFILE]`\n"
                "# User Profile\n\n"
                "## Notes\n"
                "- The user appears to have a German accent (e.g., 'vhat' for 'what').\n"
                "`[/UPDATE_PROFILE]`\n"
                "The current time is 2:30 PM."
            ),
            "input_device_index": None,  # None means system default
            "output_device_index": None, # None means system default
            "stt_pause_threshold": 0.8,
            "stt_dynamic_energy": True,
        }
        self.settings = self._load()

    def _load(self) -> dict:
        if self.file_path.exists():
            with self.file_path.open('r', encoding='utf-8') as f:
                try:
                    loaded_settings = json.load(f)
                    # Ensure all default keys exist in the loaded settings
                    for key, value in self.defaults.items():
                        loaded_settings.setdefault(key, value)
                    return loaded_settings
                except json.JSONDecodeError:
                    # If file is corrupt, start with fresh defaults
                    return self.defaults.copy()
        else:
            # If file doesn't exist, create it with defaults
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

### File: `/corvus_app/assets/__init__.py`
```py
# Makes 'assets' a package
```

### File: `/corvus_app/assets/sounds/README.md`
```md
# Sound Assets

This directory should contain the following sound files in `.wav` format for the application's audio feedback system.

- `app_start.wav`: Played when the main application starts.
- `button_press.wav`: A short click/beep for UI button interactions.
- `install_start.wav`: Played when the installer begins.
- `install_step.wav`: A short notification sound for each major step in the installation.
- `install_success.wav`: An upbeat sound for successful installation.
- `install_fail.wav`: A distinct error sound for failed installation.
- `notification.wav`: A general-purpose notification sound for when the assistant responds.
```

### File: `/corvus_app/assets/sounds/__init__.py`
```py
# Makes 'sounds' a sub-package
```

### File: `/corvus_app/assistant.py`
```py
# corvus_app/assistant.py
import logging

from corvus_app.app_settings import settings_manager
from corvus_app.llm.llm_client import LLMClient
from corvus_app.tts.tts_engine import TTSEngine
from models.tts_manager import get_local_models_list as get_local_tts_models
from models.stt_manager import get_local_models as get_local_stt_models
from plugins.registry import CommandRegistry

logger = logging.getLogger(__name__)

class Assistant:
    def __init__(self):
        logger.info("Initializing Assistant...")
        self.is_running = True
        self.validate_settings()
        self.registry = CommandRegistry()
        self.llm_client = LLMClient()
        self.tts_engine = TTSEngine()
        
    def validate_settings(self):
        """
        Validates critical settings on startup to prevent crashes from bad configs.
        """
        logger.info("Validating settings...")
        
        # --- Validate TTS Model ---
        active_tts = settings_manager.get("active_tts_model")
        if active_tts:
            local_tts_models = get_local_tts_models()
            if active_tts not in local_tts_models:
                logger.warning(
                    f"Active TTS model '{active_tts}' not found in local models. "
                    "Resetting to None. Please select a new model in settings."
                )
                settings_manager.set("active_tts_model", None)
        
        # --- Validate STT Model ---
        active_stt = settings_manager.get("active_stt_model")
        if active_stt:
            local_stt_models = get_local_stt_models()
            if active_stt not in local_stt_models:
                logger.warning(
                    f"Active STT model '{active_stt}' not found in local models. "
                    "Resetting to 'base'. Please select a new model in settings."
                )
                settings_manager.set("active_stt_model", "base")

        # --- LLM model is disabled, ensure it's set to None ---
        settings_manager.set("active_llm_model", None)


    def reload(self):
        """Reloads components like the LLM and TTS models."""
        logger.info("Reloading Assistant components...")
        self.validate_settings()
        self.llm_client.reload_model()
        self.tts_engine.reload_model()

    def process_prompt(self, prompt: str, lang: str | None = None, prob: float | None = None) -> str:
        """
        Processes a user prompt by checking for commands first,
        then falling back to the LLM.
        """
        logger.info(f"Processing prompt: '{prompt}' (lang={lang}, prob={prob})")

        # Check for a matching command plugin first
        command = self.registry.find_command(prompt)
        if command:
            logger.info(f"Executing command: {command.__class__.__name__}")
            return command.execute(self)

        # If no command, use the LLM
        logger.info("No command found, deferring to LLM.")
        return self.llm_client.get_response(prompt, lang, prob)
```

### File: `/corvus_app/audio/__init__.py`
```py
# This file makes the 'audio' directory a Python sub-package.
```

### File: `/corvus_app/audio/device_manager.py`
```py
# corvus_app/audio/device_manager.py
import logging
import sounddevice as sd

logger = logging.getLogger(__name__)

def get_audio_devices():
    """
    Retrieves lists of available input and output audio devices.

    Returns:
        tuple[list[dict], list[dict]]: A tuple containing two lists:
        one for input devices and one for output devices. Each device is a
        dictionary with 'index' and 'name'. Returns empty lists on error.
    """
    input_devices = []
    output_devices = []
    try:
        devices = sd.query_devices()
        for i, device in enumerate(devices):
            # Input devices have at least one input channel
            if device.get("max_input_channels", 0) > 0:
                input_devices.append({"index": i, "name": device.get("name", f"Device {i}")})
            # Output devices have at least one output channel
            if device.get("max_output_channels", 0) > 0:
                output_devices.append({"index": i, "name": device.get("name", f"Device {i}")})
        
        logger.debug(f"Found {len(input_devices)} input and {len(output_devices)} output devices.")

    except Exception as e:
        logger.error(f"Failed to query audio devices using sounddevice: {e}", exc_info=True)
    
    return input_devices, output_devices
```

### File: `/corvus_app/audio/sound_player.py`
```py
# corvus_app/audio/sound_player.py
import logging
import soundfile as sf
import sounddevice as sd
from pathlib import Path

from corvus_app.app_settings import settings_manager

logger = logging.getLogger(__name__)

# --- Sound Asset Definitions ---
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets" / "sounds"
APP_START_SOUND = ASSETS_DIR / "app_start.wav"
BUTTON_PRESS_SOUND = ASSETS_DIR / "button_press.wav"
NOTIFICATION_SOUND = ASSETS_DIR / "notification.wav"
INSTALL_START_SOUND = ASSETS_DIR / "install_start.wav"
INSTALL_STEP_SOUND = ASSETS_DIR / "install_step.wav"
INSTALL_SUCCESS_SOUND = ASSETS_DIR / "install_success.wav"
INSTALL_FAIL_SOUND = ASSETS_DIR / "install_fail.wav"


class SoundPlayer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SoundPlayer, cls).__new__(cls)
        return cls._instance

    def play(self, sound_path: Path | str, asynchronous: bool = True):
        """
        Plays a sound file using the selected output device.

        Args:
            sound_path: Path to the .wav file.
            asynchronous: If True, play in background. If False, block until done.
        """
        sound_path = Path(sound_path)
        if not sound_path.exists():
            logger.warning(f"Sound file not found: {sound_path}")
            return

        try:
            device_index = settings_manager.get("output_device_index")
            # If device_index is None, sounddevice will use the system default
            
            logger.debug(f"Playing '{sound_path}' on device '{device_index}' (Async: {asynchronous})")
            
            data, fs = sf.read(sound_path, dtype='float32')
            
            sd.play(data, fs, device=device_index, blocking=not asynchronous)
            
        except Exception as e:
            logger.error(f"Failed to play audio for '{sound_path}': {e}", exc_info=True)

# Create a singleton instance for easy import and use
sound_player = SoundPlayer()
```

### File: `/corvus_app/audio/stt.py`
```py
# corvus_app/audio/stt.py
import logging
import speech_recognition as sr
import numpy as np
import torch
from faster_whisper import WhisperModel

from corvus_app.app_settings import settings_manager
from models.stt_manager import STT_MODELS_PATH

logger = logging.getLogger(__name__)

class STTEngine:
    _instance = None
    _current_model_name: str | None = None
    _model: WhisperModel | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(STTEngine, cls).__new__(cls)
            cls._instance.reload_model()
        return cls._instance

    def reload_model(self, model_name_override: str | None = None):
        model_name = model_name_override or settings_manager.get("active_stt_model")
        if not model_name:
            logger.warning("No active STT model selected. STT engine not loaded.")
            self._model = None
            self._current_model_name = None
            return

        if self._model and self._current_model_name == model_name:
            logger.debug("STT model is already up-to-date.")
            return

        logger.info(f"Attempting to load STT model: '{model_name}'")
        try:
            # Determine device
            device = "cuda" if torch.cuda.is_available() else "cpu"
            compute_type = "float16" if device == "cuda" else "int8"
            
            self._model = WhisperModel(
                model_name, 
                device=device, 
                compute_type=compute_type,
                download_root=str(STT_MODELS_PATH)
            )
            self._current_model_name = model_name
            logger.info(f"STT model '{model_name}' loaded successfully on {device}.")
        except Exception as e:
            logger.error(f"Failed to load STT model '{model_name}': {e}", exc_info=True)
            self._model = None
            self._current_model_name = None

    def transcribe(self, audio_data: bytes) -> tuple[str, str, float]:
        if not self._model:
            logger.error("STT model not loaded, cannot transcribe.")
            return "", "", 0.0
        
        try:
            # Convert raw WAV data to numpy array
            audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
            
            segments, info = self._model.transcribe(audio_np, beam_size=5)
            
            transcribed_text = " ".join([segment.text for segment in segments]).strip()
            lang = info.language
            lang_prob = info.language_probability

            logger.info(f"Transcribed: '{transcribed_text}' (Lang: {lang}, Prob: {lang_prob:.2f})")
            return transcribed_text, lang, lang_prob

        except Exception as e:
            logger.error(f"Error during STT transcription: {e}", exc_info=True)
            return "", "", 0.0

# Singleton instance of the engine, lazily loaded
_stt_engine_instance = None

def get_stt_engine():
    """Lazily creates and returns the singleton STTEngine instance."""
    global _stt_engine_instance
    if _stt_engine_instance is None:
        _stt_engine_instance = STTEngine()
    return _stt_engine_instance

def listen_for_audio() -> tuple[str, str, float]:
    """Listens for audio and uses the STT engine to transcribe it."""
    r = sr.Recognizer()
    r.pause_threshold = settings_manager.get("stt_pause_threshold")
    r.dynamic_energy_threshold = settings_manager.get("stt_dynamic_energy")
    
    mic_index = settings_manager.get("input_device_index")
    
    try:
        # Whisper is trained on 16kHz audio.
        with sr.Microphone(device_index=mic_index, sample_rate=16000) as source:
            if not r.dynamic_energy_threshold:
                 # adjust_for_ambient_noise is only needed if dynamic energy is off
                r.adjust_for_ambient_noise(source, duration=0.5)

            logger.info(f"Listening on device index: {mic_index}...")
            # These timeouts are still useful to prevent infinite listening
            audio = r.listen(source, timeout=7, phrase_time_limit=30)
            
            logger.info("Recognizing speech with local Whisper model...")
            # Pass the raw WAV data to the engine
            stt_engine = get_stt_engine()
            return stt_engine.transcribe(audio.get_wav_data())
            
    except sr.WaitTimeoutError:
        logger.debug("Listening timed out, no audio detected.")
        return "", "", 0.0
    except Exception as e:
        logger.error(f"An unexpected STT error occurred on device index {mic_index}: {e}", exc_info=True)
        return "", "", 0.0
```

### File: `/corvus_app/config.py`
```py
# corvus_app/config.py
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# This is now only the *initial* wake word, loaded from .env on first run.
# The app will subsequently use the value from settings.json.
WAKE_WORD = os.getenv("WAKE_WORD", "corvus")

_log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, _log_level_str, logging.INFO)
```

### File: `/corvus_app/crash_handler.py`
```py
# corvus_app/crash_handler.py
import platform
import sys
import traceback
from datetime import datetime
from typing import Optional, Dict

REPORT_FILE = "corvus_crash_report.log"

def format_crash_report(
    app_part: str,
    exception: Exception,
    traceback_info: str,
    context: Optional[Dict[str, any]] = None,
):
    """
    Creates a detailed, developer-friendly crash report and saves it to a file.

    Args:
        app_part: The part of the application that crashed (e.g., "Launcher", "Main App").
        exception: The exception object that was caught.
        traceback_info: The formatted traceback string.
        context: Optional dictionary of relevant state information at the time of the crash.
    """
    timestamp = datetime.now().isoformat()
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    
    os_release = platform.release()
    os_note = " (Note: Windows 11 often reports as 10, this is normal)" if platform.system() == "Windows" and os_release == "10" else ""

    # --- Build the Report ---
    report_lines = [
        "============================================================================",
        "==                   GEMINI AI - CORVUS CRASH REPORT                      ==",
        "============================================================================",
        f"Timestamp: {timestamp}",
        f"App_Part: {app_part}",
        "",
        "--- Environment ---",
        f"OS_Platform: {platform.system()}",
        f"OS_Release: {os_release}{os_note}",
        f"OS_Version: {platform.version()}",
        f"Architecture: {platform.machine()}",
        f"Python_Version: {python_version}",
        "",
        "--- Error ---",
        f"Type: {type(exception).__name__}",
        f"Message: {str(exception)}",
        "",
    ]

    # --- Context (Optional) ---
    if context:
        report_lines.append("--- State Context ---")
        for key, value in context.items():
            report_lines.append(f"{key.replace('_', ' ').title()}: {value}")
        report_lines.append("")

    # --- Traceback ---
    report_lines.extend(
        [
            "--- Traceback ---",
            "```",
            traceback_info.strip(),
            "```",
            "\n"
        ]
    )
    
    report = "\n".join(report_lines)

    # --- Save the Report ---
    try:
        with open(REPORT_FILE, "a", encoding="utf-8") as f:
            f.write(report)
        print(f"\n[CRITICAL] A crash report has been saved to '{REPORT_FILE}'.")
        print("[CRITICAL] Please send this file to the developer for analysis.")
    except Exception as log_e:
        print("\n[CRITICAL] A crash occurred but the crash reporter FAILED to write the log file.")
        print(f"[CRITICAL] Logging Error: {log_e}")
        print("[CRITICAL] Please manually copy the error from your console.")
```

### File: `/corvus_app/llm/__init__.py`
```py
# This file makes the 'llm' directory a Python sub-package.
```

### File: `/corvus_app/llm/llm_client.py`
```py
# corvus_app/llm/llm_client.py
import logging
from corvus_app.app_settings import settings_manager
from corvus_app.tools.user_profile import user_profile_manager

logger = logging.getLogger(__name__)

class LLMClient:
    """
    A singleton client to manage the lifecycle of the Llama CPP model.
    It handles loading, reloading, and generating text responses.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMClient, cls).__new__(cls)
        return cls._instance

    def reload_model(self):
        """
        This function is now a stub as local LLM is disabled.
        """
        logger.warning("Local LLM functionality is disabled. Model loading is skipped.")
        return

    def get_response(self, prompt: str, lang: str | None = None, prob: float | None = None) -> str:
        """
        Returns a generic response indicating that LLM features are disabled.
        """
        logger.warning(f"LLM functionality is disabled. Not processing prompt: '{prompt}'")
        return "I'm sorry, my advanced language model features are currently disabled. I can only respond to basic commands."
```

### File: `/corvus_app/logging_config.py`
```py
# corvus_app/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from . import config

def setup_logging(log_filename="corvus_app.log"):
    """Configures the root logger for the application."""
    
    # Clear the log file at the start of the session
    log_path = Path(log_filename)
    if log_path.exists():
        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.truncate(0)
        except Exception as e:
            # If we can't clear it, it's not a fatal error.
            print(f"Warning: Could not clear log file '{log_filename}': {e}")

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
import multiprocessing as mp
from pathlib import Path

# Ensure the project root is in the Python path
_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

import logging
import traceback
from datetime import datetime

from PyQt6.QtWidgets import QApplication

from corvus_app.crash_handler import format_crash_report
from corvus_app.logging_config import setup_logging

def main():
    """Main entry point. Spawns the daemon process and runs the PyQt6 UI."""
    daemon_proc = None
    try:
        # --- Setup Logging ---
        setup_logging(log_filename="corvus_app.log")
        logger = logging.getLogger(__name__)
        logger.info("Main application process starting.")

        # --- Create Shared Queues ---
        ui_to_daemon_queue = mp.Queue()
        daemon_to_ui_queue = mp.Queue()

        # --- Start Daemon Process ---
        from daemon_process import run_daemon_process
        daemon_proc = mp.Process(
            target=run_daemon_process,
            args=(ui_to_daemon_queue, daemon_to_ui_queue),
            name="CorvusDaemon",
            daemon=True  # Ensures daemon exits if the main app crashes unexpectedly
        )
        daemon_proc.start()
        logger.info(f"Daemon process started with PID: {daemon_proc.pid}")

        # --- Start UI ---
        from corvus_app.ui.main_window import MainWindow
        app = QApplication(sys.argv)
        window = MainWindow(
            ui_to_daemon_queue=ui_to_daemon_queue,
            daemon_to_ui_queue=daemon_to_ui_queue,
            daemon_process=daemon_proc
        )
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        # Fallback crash handler for the main process
        tb_info = traceback.format_exc()
        try:
            from corvus_app.app_settings import settings_manager
            context = {"active_llm_model": settings_manager.get("active_llm_model")}
        except Exception:
            context = {"error": "Could not load settings manager."}
        format_crash_report("Main App Bootstrap", e, tb_info, context)
        
        # Ensure daemon is cleaned up on crash
        if daemon_proc and daemon_proc.is_alive():
            daemon_proc.terminate()
        
        sys.exit(1)

if __name__ == "__main__":
    # The 'spawn' start method is required for compatibility on macOS and Windows.
    if sys.platform in ["win32", "darwin"]:
        mp.set_start_method("spawn", force=True)
    main()
```

### File: `/corvus_app/tools/__init__.py`
```py
# corvus_app/tools/__init__.py
# Makes 'tools' a Python package.
```

### File: `/corvus_app/tools/cleaner.py`
```py
# corvus_app/tools/cleaner.py
import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

def _release_main_log_file():
    """Finds, closes, and removes the handler for the main application log file."""
    log_filename = "corvus_app.log"
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:  # Iterate over a copy of the list
        if isinstance(handler, logging.FileHandler) and Path(handler.baseFilename).name == log_filename:
            try:
                handler.close()
                root_logger.removeHandler(handler)
                logger.info(f"Successfully closed and removed log handler for {log_filename}")
            except Exception as e:
                logger.error(f"Error closing log handler for {log_filename}: {e}", exc_info=True)

def _delete_path(path: Path, path_type: str):
    """Safely deletes a file or directory."""
    if not path.exists():
        logger.info(f"Skipping deletion, {path_type} not found: {path}")
        return
    try:
        if path.is_dir():
            shutil.rmtree(path)
            logger.info(f"Successfully deleted directory: {path}")
        else:
            path.unlink()
            logger.info(f"Successfully deleted file: {path}")
    except OSError as e:
        logger.error(f"Failed to delete {path_type} {path}: {e}", exc_info=True)


def clean_models():
    """Deletes all downloaded LLM, TTS and STT models."""
    logger.info("Starting model cleaning process...")
    _delete_path(Path("llm_models"), "LLM models directory")
    _delete_path(Path("tts_models"), "TTS models directory")
    _delete_path(Path("stt_models"), "STT models directory")

def clean_logs_settings():
    """Deletes all log files, the settings file, and the .env file."""
    logger.info("Starting logs and settings cleaning process...")
    
    # Attempting this is best-effort. It may fail on Windows if the daemon process
    # hasn't released the file handle yet, but it's better than doing nothing.
    logging.shutdown()
    
    files_to_delete = [
        "settings.json", ".env", "corvus_app.log", "corvus_crash_report.log", 
        "installer.log", "output.wav", "user_profile.md", "corvus_daemon.log"
    ]
    for filename in files_to_delete:
        _delete_path(Path(filename), "log/settings file")

def clean_pycache():
    """Deletes all __pycache__ directories recursively."""
    logger.info("Starting __pycache__ cleaning process...")
    for path in Path(".").rglob("__pycache__"):
        if path.is_dir():
            _delete_path(path, "__pycache__ directory")
```

### File: `/corvus_app/tools/user_profile.py`
```py
# corvus_app/tools/user_profile.py
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
PROFILE_PATH = Path("user_profile.md")

class UserProfile:
    def __init__(self):
        if not PROFILE_PATH.exists():
            self.create_default_profile()

    def create_default_profile(self):
        logger.info("Creating default user_profile.md.")
        default_content = (
            "# User Profile\n\n"
            "## Notes\n"
            "- This file is for the AI to keep notes on the user's speech patterns and preferences.\n"
            "- The AI will read this file before responding and update it when it learns something new.\n"
        )
        try:
            PROFILE_PATH.write_text(default_content, encoding="utf-8")
        except Exception as e:
            logger.error(f"Failed to create default user profile: {e}")

    def read(self) -> str:
        """Reads the entire content of the user profile."""
        try:
            return PROFILE_PATH.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Failed to read user profile: {e}")
            return "Error: Could not read user profile."

    def write(self, content: str):
        """Overwrites the user profile with new content."""
        try:
            PROFILE_PATH.write_text(content, encoding="utf-8")
            logger.info("User profile was updated.")
        except Exception as e:
            logger.error(f"Failed to write to user profile: {e}")

# Singleton instance for easy import and use across the application
user_profile_manager = UserProfile()
```

### File: `/corvus_app/tts/__init__.py`
```py
# This file makes the 'tts' directory a Python sub-package.
```

### File: `/corvus_app/tts/tts_engine.py`
```py
# corvus_app/tts/tts_engine.py
import logging
import wave
from pathlib import Path
from piper.voice import PiperVoice

from corvus_app.app_settings import settings_manager
from corvus_app.audio.sound_player import sound_player
from models.tts_manager import TTS_MODELS_PATH

logger = logging.getLogger(__name__)

class TTSEngine:
    _instance = None
    _current_model_name: str | None = None
    _voice: PiperVoice | None = None
    _last_error: str | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TTSEngine, cls).__new__(cls)
            cls._instance.reload_model()
        return cls._instance

    def reload_model(self):
        model_name = settings_manager.get("active_tts_model")
        if not model_name:
            self._voice = None
            self._current_model_name = None
            self._last_error = "No active TTS model selected."
            return

        if self._voice and self._current_model_name == model_name:
            self._last_error = None
            return

        logger.info(f"Attempting to load TTS model: '{model_name}'")
        try:
            model_path = TTS_MODELS_PATH / model_name / f"{model_name}.onnx"
            config_path = TTS_MODELS_PATH / model_name / f"{model_name}.onnx.json"

            if not model_path.exists() or not config_path.exists():
                raise FileNotFoundError(f"Model files not found for '{model_name}'")

            self._voice = PiperVoice.load(str(model_path), str(config_path))
            self._current_model_name = model_name
            self._last_error = None
            logger.info(f"TTS model '{model_name}' loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load TTS model '{model_name}': {e}", exc_info=True)
            self._voice = None
            self._current_model_name = None
            self._last_error = str(e)

    def speak(self, text: str) -> str | None:
        """
        Synthesizes and speaks text using Piper TTS.
        Returns: None on success, an error string on failure.
        """
        output_path = "output.wav"
        if not text:
            return None

        if not self._voice:
            logger.warning("TTS is not available. Cannot speak.")
            return self._last_error or "TTS is not available. Please select a model in settings."

        try:
            logger.debug(f"Synthesizing speech for text: '{text[:50]}...'")
            with wave.open(output_path, "wb") as wav_file:
                self._voice.synthesize(text, wav_file)
            
            sound_player.play(output_path, asynchronous=False)
            return None # Success
        except Exception as e:
            logger.error(f"Failed to synthesize or play speech: {e}", exc_info=True)
            return str(e)

def speak_text(text: str) -> str | None:
    """
    Convenience function to speak text using the singleton TTSEngine.
    Returns: None on success, an error string on failure.
    """
    engine = TTSEngine()
    return engine.speak(text)
```

### File: `/corvus_app/ui/__init__.py`
```py
# This file makes the 'ui' directory a Python sub-package.
```

### File: `/corvus_app/ui/main_window.py`
```py
# corvus_app/ui/main_window.py
import logging
from typing import Literal
from multiprocessing import Queue, Process
import speech_recognition as sr

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit,
    QPushButton, QStatusBar, QDockWidget, QTabWidget, QFormLayout,
    QComboBox, QMessageBox, QListWidgetItem, QLabel, QTextEdit, QScrollArea
)
from PyQt6.QtCore import Qt, QThreadPool
import qtawesome as qta

from corvus_app.app_settings import settings_manager
from corvus_app.audio import device_manager
from corvus_app.tools import cleaner
from corvus_app.ui.worker import QueueListener, MicTestWorker
from corvus_app.audio.sound_player import sound_player, BUTTON_PRESS_SOUND
from models import stt_manager, tts_manager

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self, ui_to_daemon_queue: Queue, daemon_to_ui_queue: Queue, daemon_process: Process):
        super().__init__()
        self.ui_to_daemon_queue = ui_to_daemon_queue
        self.daemon_to_ui_queue = daemon_to_ui_queue
        self.daemon_process = daemon_process

        self.thread_pool = QThreadPool()
        self.input_mode = "voice" # or "text"

        self.setWindowTitle("Corvus AI Assistant")
        self.setWindowIcon(qta.icon("fa5s.feather-alt"))
        self.setGeometry(100, 100, 800, 600)
        
        # Apply a dark theme stylesheet
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QWidget { background-color: #1e1e1e; color: #d4d4d4; }
            QListWidget { border: 1px solid #333; background-color: #252526; }
            QLineEdit { border: 1px solid #333; background-color: #3c3c3c; padding: 5px; }
            QPushButton { border: 1px solid #333; background-color: #3c3c3c; padding: 5px; }
            QPushButton:hover { background-color: #555; }
            QStatusBar { color: #cccccc; }
            QDockWidget { titlebar-close-icon: url(none); }
            QDockWidget::title { text-align: center; background: #252526; padding: 5px; }
            QTabWidget::pane { border: 1px solid #333; }
            QTabBar::tab { background: #252526; padding: 8px; }
            QTabBar::tab:selected { background: #3c3c3c; }
            QComboBox { border: 1px solid #333; background-color: #3c3c3c; padding: 3px; }
        """)

        self.init_ui()
        self.start_queue_listener()

    def init_ui(self):
        # --- Header ---
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        title = QLabel("Corvus Assistant")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        
        clear_button = QPushButton("Clear Memory")
        clear_button.clicked.connect(self.on_clear_conversation)
        
        self.settings_button = QPushButton("Settings")
        self.settings_button.setIcon(qta.icon("fa5s.cog"))
        self.settings_button.clicked.connect(self.toggle_settings)

        header_layout.addWidget(clear_button)
        header_layout.addStretch()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(self.settings_button)

        # --- Central Widget ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(header)

        self.conversation_view = QListWidget()
        main_layout.addWidget(self.conversation_view)
        
        input_layout = QHBoxLayout()
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type your message...")
        self.text_input.returnPressed.connect(self.on_text_input_submitted)
        self.text_input.hide()
        
        self.toggle_input_button = QPushButton()
        self.toggle_input_button.setIcon(qta.icon("fa5s.microphone"))
        self.toggle_input_button.setToolTip("Switch to Text Input")
        self.toggle_input_button.clicked.connect(self.on_toggle_input_mode)

        input_layout.addWidget(self.toggle_input_button)
        input_layout.addWidget(self.text_input)
        main_layout.addLayout(input_layout)

        # --- Status Bar ---
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # --- Settings Panel (Dock Widget) ---
        self.settings_dock = QDockWidget("Settings", self)
        self.settings_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.settings_dock)
        
        self.settings_tabs = QTabWidget()
        self.settings_dock.setWidget(self.settings_tabs)
        
        self.setup_models_tab()
        self.setup_personality_tab()
        self.setup_system_tab()
        
        self.settings_dock.hide()

    def create_scrollable_tab(self, layout_class):
        tab_widget = QWidget()
        layout = layout_class(tab_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(tab_widget)
        return scroll, layout

    def setup_models_tab(self):
        scroll, layout = self.create_scrollable_tab(QVBoxLayout)
        self.settings_tabs.addTab(scroll, "Models")
        
        form_layout = QFormLayout()
        # TTS
        self.tts_model_list = QComboBox()
        form_layout.addRow("TTS Model:", self.tts_model_list)
        tts_buttons = QHBoxLayout()
        tts_set_active = QPushButton("Set Active")
        tts_set_active.clicked.connect(lambda: self.set_active_model("tts"))
        tts_delete = QPushButton("Delete")
        tts_delete.clicked.connect(lambda: self.delete_model("tts"))
        tts_buttons.addWidget(tts_set_active)
        tts_buttons.addWidget(tts_delete)
        form_layout.addRow(tts_buttons)
        # STT
        self.stt_model_list = QComboBox()
        form_layout.addRow("STT Model:", self.stt_model_list)
        stt_buttons = QHBoxLayout()
        stt_set_active = QPushButton("Set Active")
        stt_set_active.clicked.connect(lambda: self.set_active_model("stt"))
        stt_delete = QPushButton("Delete")
        stt_delete.clicked.connect(lambda: self.delete_model("stt"))
        stt_buttons.addWidget(stt_set_active)
        stt_buttons.addWidget(stt_delete)
        form_layout.addRow(stt_buttons)

        layout.addLayout(form_layout)

    def setup_personality_tab(self):
        scroll, layout = self.create_scrollable_tab(QVBoxLayout)
        self.settings_tabs.addTab(scroll, "Personality")
        
        layout.addWidget(QLabel("System Prompt (Assistant's Personality):"))
        self.system_prompt_input = QTextEdit()
        self.system_prompt_input.setAcceptRichText(False)
        layout.addWidget(self.system_prompt_input)
        save_button = QPushButton("Save Personality")
        save_button.clicked.connect(self.save_personality)
        layout.addWidget(save_button)

    def setup_system_tab(self):
        scroll, layout = self.create_scrollable_tab(QFormLayout)
        self.settings_tabs.addTab(scroll, "System")
        
        # Wake Word
        self.wake_word_input = QLineEdit()
        layout.addRow("Wake Word:", self.wake_word_input)
        
        # STT Settings
        self.stt_pause_input = QLineEdit()
        layout.addRow("Pause Threshold (s):", self.stt_pause_input)
        
        save_stt_button = QPushButton("Save System Settings")
        save_stt_button.clicked.connect(self.save_system_settings)
        layout.addRow(save_stt_button)

        # Audio Devices
        self.input_device_list = QComboBox()
        self.output_device_list = QComboBox()
        layout.addRow("Input Device:", self.input_device_list)
        layout.addRow("Output Device:", self.output_device_list)
        self.input_device_list.currentIndexChanged.connect(lambda i: self.set_audio_device("input", self.input_device_list.itemData(i)))
        self.output_device_list.currentIndexChanged.connect(lambda i: self.set_audio_device("output", self.output_device_list.itemData(i)))

        # Diagnostics
        self.mic_test_status = QLabel("Mic Test: Status will appear here.")
        test_mic_button = QPushButton("Test Mic")
        test_mic_button.clicked.connect(self.test_mic)
        layout.addRow(test_mic_button, self.mic_test_status)

        # Utilities
        clean_models = QPushButton("Clean All Models")
        clean_logs = QPushButton("Clean Logs & Settings")
        clean_cache = QPushButton("Clean Python Cache")
        clean_models.clicked.connect(lambda: self.run_cleaner("models", cleaner.clean_models))
        clean_logs.clicked.connect(lambda: self.run_cleaner("logs", cleaner.clean_logs_settings))
        clean_cache.clicked.connect(lambda: self.run_cleaner("cache", cleaner.clean_pycache))
        layout.addRow(clean_models)
        layout.addRow(clean_logs)
        layout.addRow(clean_cache)

    # --- UI Logic & Event Handlers ---
    def toggle_settings(self):
        if self.settings_dock.isVisible():
            self.settings_dock.hide()
            self.ui_to_daemon_queue.put({"type": "reload_models"})
        else:
            self.populate_settings()
            self.settings_dock.show()
    
    def on_clear_conversation(self):
        self.conversation_view.clear()
        
    # --- Settings Handlers ---
    def populate_settings(self):
        # TTS Models
        self.tts_model_list.clear()
        active_tts = settings_manager.get("active_tts_model")
        for model_id, name in tts_manager.get_local_models_list().items():
            self.tts_model_list.addItem(name, model_id)
            if model_id == active_tts: self.tts_model_list.setCurrentText(name)
        
        # STT Models
        self.stt_model_list.clear()
        active_stt = settings_manager.get("active_stt_model")
        for name in stt_manager.get_local_models():
            self.stt_model_list.addItem(name, name)
            if name == active_stt: self.stt_model_list.setCurrentText(name)
            
        # Personality
        self.system_prompt_input.setText(settings_manager.get("system_prompt"))
        
        # System
        self.wake_word_input.setText(settings_manager.get("wake_word"))
        self.stt_pause_input.setText(str(settings_manager.get("stt_pause_threshold")))
        
        # Audio Devices
        self.input_device_list.clear()
        self.output_device_list.clear()
        in_devs, out_devs = device_manager.get_audio_devices()
        self.input_device_list.addItem("System Default", None)
        self.output_device_list.addItem("System Default", None)
        for dev in in_devs: self.input_device_list.addItem(dev['name'], dev['index'])
        for dev in out_devs: self.output_device_list.addItem(dev['name'], dev['index'])

    def save_personality(self):
        settings_manager.set("system_prompt", self.system_prompt_input.toPlainText())
        self.status_bar.showMessage("Personality saved.", 2000)

    def save_system_settings(self):
        settings_manager.set("wake_word", self.wake_word_input.text())
        try:
            pause = float(self.stt_pause_input.text())
            settings_manager.set("stt_pause_threshold", pause)
            self.status_bar.showMessage("System settings saved.", 2000)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Pause threshold must be a number.")
    
    def set_audio_device(self, dev_type: Literal["input", "output"], index: int | None):
        settings_manager.set(f"{dev_type}_device_index", index)
        self.status_bar.showMessage(f"{dev_type.capitalize()} device set.", 2000)

    def set_active_model(self, model_type: Literal["tts", "stt"]):
        combo: QComboBox = getattr(self, f"{model_type}_model_list")
        model_id = combo.currentData() or combo.currentText()
        settings_manager.set(f"active_{model_type}_model", model_id)
        self.status_bar.showMessage(f"Active {model_type.upper()} model set.", 2000)
        self.ui_to_daemon_queue.put({"type": "reload_models"})

    def delete_model(self, model_type: Literal["tts", "stt"]):
        combo: QComboBox = getattr(self, f"{model_type}_model_list")
        model_id = combo.currentData() or combo.currentText()
        if not model_id: return
        
        reply = QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete the model '{model_id}'?")
        if reply == QMessageBox.StandardButton.Yes:
            if model_type == "tts": tts_manager.delete_model(model_id)
            else: stt_manager.delete_model(model_id)
            self.populate_settings()

    def test_mic(self):
        self.mic_test_status.setText("Mic Test: Listening...")
        worker = MicTestWorker(settings_manager.get("input_device_index"))
        worker.signals.result.connect(lambda res: self.mic_test_status.setText(f"Mic Test: {res}"))
        self.thread_pool.start(worker)
        
    def run_cleaner(self, name: str, clean_func: callable):
        reply = QMessageBox.question(self, f"Confirm Clean", f"This will delete all {name} and require a restart. Are you sure?")
        if reply == QMessageBox.StandardButton.Yes:
            clean_func()
            QMessageBox.information(self, "Clean Complete", f"All {name} have been deleted. Please restart the application.")
            self.close()

    def on_toggle_input_mode(self):
        if self.input_mode == "voice":
            self.input_mode = "text"
            self.toggle_input_button.setIcon(qta.icon("fa5s.keyboard"))
            self.toggle_input_button.setToolTip("Switch to Voice Input")
            self.text_input.show()
            self.text_input.setFocus()
            self.ui_to_daemon_queue.put({"type": "stop_listening"})
        else:
            self.input_mode = "voice"
            self.toggle_input_button.setIcon(qta.icon("fa5s.microphone"))
            self.toggle_input_button.setToolTip("Switch to Text Input")
            self.text_input.hide()
            self.ui_to_daemon_queue.put({"type": "start_listening"})

    def on_text_input_submitted(self):
        prompt = self.text_input.text().strip()
        if prompt:
            self.ui_to_daemon_queue.put({"type": "process_text", "payload": prompt})
            self.add_conversation_item(prompt, "user")
            self.text_input.clear()

    def start_queue_listener(self):
        self.queue_listener = QueueListener(self.daemon_to_ui_queue)
        self.queue_listener.signals.status_update.connect(self.on_status_update)
        self.queue_listener.signals.assistant_response.connect(self.on_assistant_response)
        self.queue_listener.signals.error.connect(self.on_error)
        self.thread_pool.start(self.queue_listener)
        
    def add_conversation_item(self, text: str, role: str):
        item = QListWidgetItem(f"{role.capitalize()}: {text}")
        if role == "user":
            item.setForeground(Qt.GlobalColor.cyan)
        else:
            item.setForeground(Qt.GlobalColor.green)
        self.conversation_view.addItem(item)
        self.conversation_view.scrollToBottom()

    # --- Signal Handlers ---
    def on_status_update(self, text: str):
        self.status_bar.showMessage(text)

    def on_assistant_response(self, text: str, user_prompt: str):
        self.add_conversation_item(text, "assistant")

    def on_error(self, title: str, message: str):
        QMessageBox.warning(self, title, message)

    def closeEvent(self, event):
        """Ensure the daemon is terminated when the window closes."""
        logger.info("Close event triggered. Shutting down daemon.")
        self.queue_listener.stop()
        self.ui_to_daemon_queue.put({"type": "shutdown"})
        if self.daemon_process.is_alive():
            self.daemon_process.join(timeout=2)
            if self.daemon_process.is_alive():
                logger.warning("Daemon did not shut down gracefully. Terminating.")
                self.daemon_process.terminate()
        super().closeEvent(event)
```

### File: `/corvus_app/ui/screens/__init__.py`
```py
# This file makes the 'screens' directory a Python sub-package.
```

### File: `/corvus_app/ui/screens/confirm_screen.py`
```py
# corvus_app/ui/screens/confirm_screen.py
from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Static

class ConfirmScreen(ModalScreen[bool]):
    """A modal screen to confirm a critical action."""

    def __init__(self, prompt: str):
        super().__init__()
        self.prompt = prompt

    def compose(self) -> ComposeResult:
        yield Grid(
            Static(self.prompt, id="confirm-prompt"),
            Button("Cancel", variant="default", id="confirm-cancel"),
            Button("Confirm", variant="error", id="confirm-ok"),
            id="confirm-dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirm-ok":
            self.dismiss(True)
        else:
            self.dismiss(False)

    def on_key(self, event) -> None:
        if event.key == "escape":
            self.dismiss(False)
```

### File: `/corvus_app/ui/screens/download_screen.py`
```py
# corvus_app/ui/screens/download_screen.py
import logging
from typing import Literal, Optional

from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button, ProgressBar, Static

from corvus_app.ui.shared import ModelDownloaded
from models import tts_manager

logger = logging.getLogger(__name__)

DownloadType = Literal["tts"]

class DownloadScreen(ModalScreen):
    """A modal screen for downloading models."""

    def __init__(self, model_info: dict, download_type: DownloadType):
        super().__init__()
        self.model_info = model_info
        self.download_type = download_type
        self.title = f"TTS: {self.model_info.get('model_name', 'Unknown')}"

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static(f"Downloading {self.title}", id="progress-label"),
            Horizontal(Static("Starting...", id="progress-stats"), classes="stats_bar"),
            ProgressBar(total=100, id="download-progress"),
            Button("Close", variant="error", id="close-download-button", disabled=True),
            id="progress-dialog",
        )

    def on_mount(self) -> None:
        """Start the download worker when the screen is mounted."""
        self.run_worker(self.run_download, thread=True, exclusive=True)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "close-download-button":
            self.app.pop_screen()

    def update_ui_elements(self, event: str, message: str, is_finished: bool = False):
        """Helper to update UI from a worker thread."""
        stats = self.query_one("#progress-stats")
        label = self.query_one("#progress-label")
        button = self.query_one("#close-download-button", Button)
        stats.update(message)
        if is_finished:
            label.update(f"{event.capitalize()}: {self.title}")
            button.disabled = False

    def on_download_progress(self, event: str, total_size: Optional[int] = 0, downloaded: int = 0, message: str = ""):
        def update_ui():
            pb = self.query_one(ProgressBar)
            if event == "start":
                pb.total = total_size
                self.update_ui_elements(event, message or "Connecting...")
            elif event == "update":
                pb.update(progress=downloaded)
                # Show percentage only if we have a total size
                if pb.total is not None and pb.total > 0:
                    total_mb = pb.total / (1024 * 1024)
                    dl_mb = downloaded / (1024 * 1024)
                    percent = (downloaded / pb.total * 100)
                    self.update_ui_elements(event, f"{dl_mb:.2f} / {total_mb:.2f} MB ({percent:.1f}%)")
                else:
                    # For indeterminate progress bar, the message from the 'start' event will persist.
                    # The bar will animate on its own if total is None.
                    pass
            elif event == "finish":
                if pb.total is None:
                    pb.total = 100
                pb.update(progress=pb.total)
                self.update_ui_elements(event, "[green]Download successful![/green]", is_finished=True)
                self.post_message(ModelDownloaded(self.download_type))
            elif event == "error":
                self.update_ui_elements(event, f"[red]Error: {message}[/red]", is_finished=True)
        self.app.call_from_thread(update_ui)

    def run_download(self) -> None:
        """Dispatches the download task to the appropriate manager."""
        # For TTS, we can't get progress. Set indeterminate state, then run blocking download.
        self.on_download_progress("start", total_size=None, message="Downloading... Please wait.")
        tts_manager.download_model(
            self.model_info["model_name"], self.on_download_progress
        )
```

### File: `/corvus_app/ui/screens/main_screen.py`
```py
# corvus_app/ui/screens/main_screen.py
import logging
from typing import Literal

import speech_recognition as sr
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, ScrollableContainer, Vertical
from textual.screen import Screen
from textual.widgets import (
    Button, Footer, Input, Label, ListView, OptionList, TabbedContent, TabPane, Static
)
from textual.widgets.option_list import Option

from corvus_app.app_settings import settings_manager
from corvus_app.audio import device_manager
from corvus_app.tools import cleaner
from corvus_app.ui.screens.confirm_screen import ConfirmScreen
from corvus_app.ui.screens.download_screen import DownloadScreen, DownloadType
from corvus_app.ui.shared import (
    AssistantResponse, ConversationListItem, ModelDownloaded, StatusUpdate, STTModelDownloaded
)
from models import stt_manager, tts_manager

logger = logging.getLogger(__name__)


# --- Settings Panel Component Widgets ---
# By breaking the settings panel into smaller components, the code becomes
# cleaner, more modular, and easier to modify.

class ModelsPane(Container):
    """A widget to display all model-related settings."""
    def compose(self) -> ComposeResult:
        yield Label("Voice Models (TTS)")
        yield OptionList(id="tts-option-list")
        with Horizontal(classes="model-buttons"):
            yield Button("Set Active", id="tts-set-active-button", variant="success")
            yield Button("Delete", id="tts-delete-button", variant="error")
        yield Label("Download New Voice")
        yield OptionList(id="tts-download-list")
        yield Button("Download Selected Voice", id="tts-download-button", classes="download-button")

        yield Static("---", classes="separator")
        yield Label("Speech-to-Text Models (STT / Whisper)")
        yield OptionList(id="stt-option-list")
        with Horizontal(classes="model-buttons"):
            yield Button("Set Active", id="stt-set-active-button", variant="success")
            yield Button("Delete", id="stt-delete-button", variant="error")
        yield Label("Download New STT Model")
        yield Static(
            "[bold]Model Selection Guide:[/]\n"
            "- [cyan]tiny / base[/]: Fastest, lowest VRAM (~500MB), less accurate.\n"
            "- [cyan]small[/]: Good balance of speed & accuracy (~1GB VRAM).\n"
            "- [cyan].en models[/]: English-only, faster and often more accurate.\n"
            "- [cyan]medium[/]: High accuracy, handles accents well (~2.2GB VRAM).\n"
            "- [cyan]large-v3[/]: Best accuracy, but slowest (~5GB VRAM).\n"
            "- [cyan]distil models[/]: Faster than their counterparts with similar accuracy.",
            classes="help-text"
        )
        yield OptionList(id="stt-download-list")
        yield Button("Download Selected STT", id="stt-download-button", classes="download-button")

class PersonalityPane(Container):
    """A widget to display personality/prompt settings."""
    def compose(self) -> ComposeResult:
        yield Label("System Prompt (Assistant's Personality)")
        yield Input(id="system-prompt-input", placeholder="e.g., You are a witty pirate captain.")
        yield Button("Save Personality", id="save-personality-button")

class SystemPane(Container):
    """A widget to display system and hardware settings."""
    def compose(self) -> ComposeResult:
        yield Label("Wake Word")
        yield Input(id="wake-word-input")
        yield Button("Save Wake Word", id="save-wake-word-button")
        yield Static("---", classes="separator")
        yield Label("Speaking Pause Threshold (seconds)")
        yield Input(id="stt-pause-threshold-input", placeholder="e.g., 0.8")
        yield Button("Save STT Settings", id="save-stt-settings-button")
        yield Static("---", classes="separator")
        yield Label("Audio Devices")
        yield Label("Input Device (Microphone)")
        yield OptionList(id="input-device-list")
        yield Label("Output Device (Speaker)")
        yield OptionList(id="output-device-list")
        yield Static("---", classes="separator")
        yield Label("Diagnostics")
        yield Static("Mic Test: Status will appear here.", id="mic-test-status")
        with Horizontal(classes="model-buttons"):
            yield Button("Test Mic", id="test-mic-button")
            yield Button("Test TTS", id="test-tts-button")
            yield Button("Test LLM", id="test-llm-button", disabled=True)
        yield Static("---", classes="separator")
        yield Label("Utilities")
        yield Button("Clean Models", id="clean-models-button", variant="warning")
        yield Button("Clean Logs/Settings", id="clean-logs-button", variant="warning")
        yield Button("Clean Cache", id="clean-cache-button", variant="warning")


# --- Main Screen ---

class MainScreen(Screen):
    BINDINGS = [Binding("tab", "toggle_input_mode", "Toggle Input", show=True)]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_mode = "voice"

    def compose(self) -> ComposeResult:
        with Container(id="app-header"):
            yield Static("Corvus Assistant", id="header-title")
            yield Button("Clear Memory", id="clear-button", classes="header-button")
            yield Button("Settings", id="settings-button", classes="header-button")
        
        with Vertical(id="body-container"):
            yield ScrollableContainer(ListView(id="conversation"), id="conversation-container")
            yield Input(placeholder="Type your message...", id="text-input")
        
        yield Footer()

        # The slide-in settings panel
        with Vertical(id="settings-panel"):
            yield Static("Settings", id="settings-header")
            with TabbedContent(id="settings-tabs"):
                with TabPane("Models"):
                    yield ScrollableContainer(ModelsPane())
                with TabPane("Personality"):
                    yield ScrollableContainer(PersonalityPane())
                with TabPane("System"):
                    yield ScrollableContainer(SystemPane())
            yield Button("Close Settings", id="settings-close-button", variant="primary")

    def on_mount(self) -> None:
        self.query_one("#text-input", Input).display = False

    async def on_button_pressed(self, msg: Button.Pressed) -> None:
        button_id = msg.button.id
        if button_id in ("settings-button", "settings-close-button"): self.action_toggle_settings_panel()
        elif button_id == "clear-button": self.action_clear_conversation()
        elif button_id == "save-wake-word-button": self.action_save_wake_word()
        elif button_id == "save-personality-button": self.action_save_personality()
        elif button_id == "save-stt-settings-button": self.action_save_stt_settings()
        elif button_id == "tts-set-active-button": self.set_active_model("tts")
        elif button_id == "tts-delete-button": await self.delete_model("tts")
        elif button_id == "tts-download-button": self.download_model("tts")
        elif button_id == "stt-set-active-button": self.set_active_model("stt")
        elif button_id == "stt-delete-button": await self.delete_model("stt")
        elif button_id == "stt-download-button": self.download_stt_model()
        elif button_id == "test-mic-button": self.run_worker(self.run_mic_test, thread=True)
        elif button_id == "test-tts-button": 
            self.app.notify("Requesting TTS test from daemon...")
            self.app.ui_to_daemon_queue.put({"type": "test_tts"})
        elif button_id == "test-llm-button": 
            self.app.notify("LLM functionality is disabled.", severity="warning")
        elif button_id == "clean-models-button": await self.run_cleaner("models", "Delete ALL downloaded models?", cleaner.clean_models)
        elif button_id == "clean-logs-button": await self.run_cleaner("logs", "Delete ALL logs/settings? This requires an app restart.", cleaner.clean_logs_settings)
        elif button_id == "clean-cache-button": await self.run_cleaner("cache", "Delete all Python cache files?", cleaner.clean_pycache)

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        if event.option_list.id == "input-device-list":
            settings_manager.set("input_device_index", event.option.id)
            self.app.notify(f"Input device set: {event.option.prompt}")
            self.update_audio_device_options()
        elif event.option_list.id == "output-device-list":
            settings_manager.set("output_device_index", event.option.id)
            self.app.notify(f"Output device set: {event.option.prompt}")
            self.update_audio_device_options()

    async def on_model_downloaded(self, msg: ModelDownloaded) -> None:
        self.app.notify(f"{msg.model_type.upper()} model ready.")
        if msg.model_type == "tts": self.update_tts_options()

    async def on_stt_model_downloaded(self, message: STTModelDownloaded) -> None:
        if message.success:
            self.app.notify(f"STT model '{message.model_name}' downloaded successfully.")
            self.update_stt_options()
        else:
            self.app.notify(
                f"Failed to download '{message.model_name}': {message.error_message}",
                severity="error",
                timeout=10,
            )

    def action_clear_conversation(self):
        self.query_one("#conversation", ListView).clear()
        self.app.notify("Conversation history cleared.")

    def action_save_wake_word(self):
        settings_manager.set("wake_word", self.query_one("#wake-word-input", Input).value)
        self.app.notify("Wake word updated.")
        
    def action_save_personality(self):
        settings_manager.set("system_prompt", self.query_one("#system-prompt-input", Input).value)
        self.app.notify("Personality updated.")
        self.app.ui_to_daemon_queue.put({"type": "reload_models"})

    def action_save_stt_settings(self):
        try:
            value = float(self.query_one("#stt-pause-threshold-input").value)
            settings_manager.set("stt_pause_threshold", value)
            self.app.notify("STT settings saved.")
        except (ValueError, TypeError):
            self.app.notify("Invalid number for pause threshold.", severity="error")
        
    def action_toggle_settings_panel(self) -> None:
        panel = self.query_one("#settings-panel")
        if panel.has_class("visible"):
            panel.remove_class("visible")
            if self.input_mode == "voice":
                self.app.ui_to_daemon_queue.put({"type": "start_listening"})
            self.app.ui_to_daemon_queue.put({"type": "reload_models"})
        else:
            self.app.ui_to_daemon_queue.put({"type": "stop_listening"})
            self.populate_settings()
            panel.add_class("visible")
            
    def populate_settings(self):
        self.query_one("#wake-word-input").value = settings_manager.get("wake_word")
        self.query_one("#system-prompt-input").value = settings_manager.get("system_prompt")
        self.query_one("#stt-pause-threshold-input").value = str(settings_manager.get("stt_pause_threshold"))
        self.update_tts_options()
        self.update_stt_options()
        self.update_audio_device_options()
        self.run_worker(self.fetch_remote_tts_models, thread=True)
        self.populate_stt_download_list()

    def update_tts_options(self):
        opt_list = self.query_one("#tts-option-list", OptionList)
        active_model = settings_manager.get("active_tts_model")
        opt_list.clear_options()
        local_models = tts_manager.get_local_models_list()
        
        if not local_models:
            opt_list.add_option(Option("No local voice models found.", disabled=True))
            return

        for model_id, friendly_name in local_models.items():
            is_active = model_id == active_model
            prompt = f"{friendly_name}{' (Active)' if is_active else ''}"
            opt_list.add_option(Option(prompt, id=model_id))

    def update_stt_options(self):
        opt_list = self.query_one("#stt-option-list", OptionList)
        active_model = settings_manager.get("active_stt_model")
        opt_list.clear_options()
        local_models = stt_manager.get_local_models()
        if not local_models:
            opt_list.add_option(Option("No local STT models found.", disabled=True))

        for model_name in local_models:
            is_active = model_name == active_model
            prompt = f"{model_name}{' (Active)' if is_active else ''}"
            opt_list.add_option(Option(prompt, id=model_name))
            
    def update_audio_device_options(self):
        in_list, out_list = self.query("#input-device-list, #output-device-list")
        in_list.clear_options()
        out_list.clear_options()
        in_devices, out_devices = device_manager.get_audio_devices()
        active_in = settings_manager.get("input_device_index")
        active_out = settings_manager.get("output_device_index")
        in_list.add_option(Option(f"System Default{' (Active)' if active_in is None else ''}", id=None))
        for dev in in_devices:
            is_active = dev['index'] == active_in
            in_list.add_option(Option(f"{dev['name']}{' (Active)' if is_active else ''}", id=dev['index']))
        out_list.add_option(Option(f"System Default{' (Active)' if active_out is None else ''}", id=None))
        for dev in out_devices:
            is_active = dev['index'] == active_out
            out_list.add_option(Option(f"{dev['name']}{' (Active)' if is_active else ''}", id=dev['index']))

    def set_active_model(self, model_type: Literal["tts", "stt"]):
        opt_list = self.query_one(f"#{model_type}-option-list", OptionList)
        if opt_list.highlighted is not None:
            highlighted_option = opt_list.get_option_at_index(opt_list.highlighted)
            if highlighted_option.disabled:
                self.app.bell()
                return
            selected_id = highlighted_option.id
            settings_manager.set(f"active_{model_type}_model", selected_id)
            if model_type == "tts": self.update_tts_options()
            else: self.update_stt_options()
            self.app.notify(f"Active {model_type.upper()} model set.")
            self.app.ui_to_daemon_queue.put({"type": "reload_models"})
            
    async def delete_model(self, model_type: Literal["tts", "stt"]):
        opt_list = self.query_one(f"#{model_type}-option-list", OptionList)
        if opt_list.highlighted is not None:
            highlighted_option = opt_list.get_option_at_index(opt_list.highlighted)
            if highlighted_option.disabled:
                self.app.bell()
                return
            selected_id = highlighted_option.id

            async def on_confirm(confirmed: bool):
                if confirmed:
                    if model_type == "tts":
                        tts_manager.delete_model(selected_id)
                        if settings_manager.get("active_tts_model") == selected_id:
                            settings_manager.set("active_tts_model", None) 
                        self.update_tts_options()
                    elif model_type == "stt":
                        stt_manager.delete_model(selected_id)
                        if settings_manager.get("active_stt_model") == selected_id:
                            settings_manager.set("active_stt_model", "base")
                        self.update_stt_options()

                    self.app.notify(f"{model_type.upper()} model deleted.")
            await self.app.push_screen(ConfirmScreen(f"Delete this {model_type.upper()} model?"), on_confirm)

    def fetch_remote_tts_models(self):
        opt_list = self.query_one("#tts-download-list", OptionList)
        opt_list.clear_options()
        opt_list.add_option(Option("Fetching available voices..."))
        models = tts_manager.get_remote_models_list()
        opt_list.clear_options()
        if models:
            for model_id, friendly_name in models.items():
                if "error" not in model_id.lower():
                    opt_list.add_option(Option(friendly_name, id=model_id))
        else:
            opt_list.add_option(Option("Could not fetch remote models.", disabled=True))

    def populate_stt_download_list(self):
        opt_list = self.query_one("#stt-download-list", OptionList)
        opt_list.clear_options()
        for model_name in stt_manager.AVAILABLE_MODELS:
            opt_list.add_option(Option(model_name, id=model_name))

    def download_model(self, download_type: DownloadType):
        opt_list = self.query_one("#tts-download-list", OptionList)
        if opt_list.highlighted is None: return
        selected_opt = opt_list.get_option_at_index(opt_list.highlighted)
        if selected_opt.disabled: return
        model_id = selected_opt.id
        if not model_id: return
        model_info = {"model_name": model_id}
        self.app.push_screen(DownloadScreen(model_info, download_type))
    
    def download_stt_model(self):
        opt_list = self.query_one("#stt-download-list", OptionList)
        if opt_list.highlighted is None: return
        model_name = opt_list.get_option_at_index(opt_list.highlighted).id
        if not model_name: return
        
        self.app.notify(f"Requesting download for STT model '{model_name}'.")
        self.app.ui_to_daemon_queue.put({"type": "download_stt", "model_name": model_name})

    async def run_cleaner(self, name: str, prompt: str, clean_func: callable):
        async def on_confirm(confirmed: bool):
            if confirmed:
                self.app.notify(f"Running {name} cleaner...")
                clean_func()
                self.app.notify(f"{name.capitalize()} cleanup complete. Please restart the application.")
                self.app.action_request_quit()
        await self.app.push_screen(ConfirmScreen(prompt), on_confirm)

    def run_mic_test(self):
        status = self.query_one("#mic-test-status", Static)
        status.update("TESTING: Say something...")
        self.app.notify("Listening for mic test...")
        r = sr.Recognizer()
        r.pause_threshold = 0.5
        mic_index = settings_manager.get("input_device_index")
        
        try:
            with sr.Microphone(device_index=mic_index, sample_rate=16000) as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                if audio:
                     status.update("[green]Success! Audio was detected from microphone.[/green]")
                else:
                    status.update("[yellow]Mic test inconclusive. No audio data captured.[/yellow]")

        except sr.WaitTimeoutError:
             status.update("[red]FAIL: No audio detected within timeout.[/red]")
        except Exception as e:
            status.update(f"[red]FAIL: {e}[/red]")

    def action_toggle_input_mode(self):
        text_input = self.query_one("#text-input", Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.display = True
            text_input.focus()
            self.app.ui_to_daemon_queue.put({"type": "stop_listening"})
        else:
            self.input_mode = "voice"
            text_input.display = False
            self.app.set_focus(None)
            self.app.ui_to_daemon_queue.put({"type": "start_listening"})
    
    async def on_input_submitted(self, message: Input.Submitted) -> None:
        prompt = message.value.strip()
        if prompt and self.input_mode == "text":
            self.query_one("#text-input", Input).value = ""
            self.app.ui_to_daemon_queue.put({"type": "process_text", "payload": prompt})

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        list_view = self.query_one("#conversation", ListView)
        if message.user_prompt:
            list_view.append(ConversationListItem(message.user_prompt, "user"))
        list_view.append(ConversationListItem(message.text, "assistant"))
        list_view.scroll_end()
        if self.input_mode == "text":
            self.post_message(StatusUpdate("TYPING..."))

    async def on_status_update(self, message: StatusUpdate) -> None:
        # Prevent the status from overriding "TYPING..." if that's the current mode
        if self.input_mode == "text" and "TYPING" not in message.text:
            return
        self.query_one(Footer).border_title = message.text
```

### File: `/corvus_app/ui/shared.py`
```py
# corvus_app/ui/shared.py
from typing import Literal

from textual.app import ComposeResult
from textual.message import Message
from textual.widgets import ListItem, Label

# --- Custom Message Classes for App-wide communication ---

class AssistantResponse(Message):
    """Posted when the assistant generates a response."""
    def __init__(self, text: str, user_prompt: str):
        super().__init__()
        self.text = text
        self.user_prompt = user_prompt

class StatusUpdate(Message):
    """Posted to update the status in the footer."""
    def __init__(self, text: str):
        super().__init__()
        self.text = text

class ModelDownloaded(Message):
    """Posted when a model download completes, to trigger UI refresh."""
    def __init__(self, model_type: Literal["tts"]):
        super().__init__()
        self.model_type = model_type

class STTModelDownloaded(Message):
    """Posted when an STT model is downloaded by the daemon."""
    def __init__(self, success: bool, model_name: str, error_message: str | None = None):
        super().__init__()
        self.success = success
        self.model_name = model_name
        self.error_message = error_message


# --- Custom Widget Classes ---

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
```

### File: `/corvus_app/ui/themes.py`
```py
# corvus_app/ui/themes.py
from dataclasses import dataclass
from textual.app import App

@dataclass
class Theme:
    """A dataclass to hold theme colors."""
    name: str
    primary: str
    secondary: str
    accent: str
    accent_light: str
    background: str
    surface: str
    text: str
    text_muted: str
    error: str

# Define the dark theme (True Black and Deep Red)
DARK_THEME = Theme(
    name="dark",
    primary="#4A0404",      # Darker red
    secondary="#2A0101",   # Very dark red
    accent="#990000",      # Main deep red accent
    accent_light="#B30000",# Lighter red for hover
    background="#000000",  # True black background
    surface="#111111",     # Slightly off-black for panels
    text="#E0E0E0",        # Light grey text
    text_muted="#666666",  # Muted grey for less important text
    error="#FF5555"        # Bright red for errors
)

# Define a professional light theme
LIGHT_THEME = Theme(
    name="light",
    primary="#005f73",      # Dark cyan
    secondary="#e9f5f7",   # Very light cyan
    accent="#0a9396",      # Main cyan accent
    accent_light="#94d2bd",# Lighter cyan for hover
    background="#f8f9fa",  # Off-white background
    surface="#ffffff",     # White for panels
    text="#212529",        # Nearly black text
    text_muted="#6c757d",  # Muted grey
    error="#d00000"        # Dark red for errors
)

def apply_theme(app: App, theme: Theme):
    """Applies a theme's colors to the app's CSS variables."""
    app.dark = (theme.name == "dark")
    # CSS variables in Textual use hyphens (kebab-case).
    # The keys in this dictionary MUST match the variable names in the CSS.
    app.stylesheet.set_variables({
        "primary": theme.primary,
        "secondary": theme.secondary,
        "accent": theme.accent,
        "accent-light": theme.accent_light,
        "background": theme.background,
        "surface": theme.surface,
        "text": theme.text,
        "text-muted": theme.text_muted,
        "error": theme.error
    })
    app.refresh_css()
```

### File: `/corvus_app/ui/tui.css`
```css
/* corvus_app/ui/tui.css */

/*
--- Color Variables ---
Default values are defined here. These are overridden dynamically by
corvus_app/ui/themes.py when the application starts or the theme is toggled.
*/
$primary: #4A0404;
$secondary: #2A0101;
$accent: #990000;
$accent-light: #B30000;
$background: #000000;
$surface: #111111;
$text: #E0E0E0;
$text-muted: #666666;
$error: #FF5555;


/* --- Base Layout --- */
Screen {
    background: $background;
    color: $text;
    layout: vertical;
}

#app-header {
    dock: top;
    height: 1;
    background: $surface;
    border-bottom: solid $accent;
    layout: horizontal;
    align: center middle;
    padding: 0 1;
}

#header-title {
    width: 1fr;
    content-align: center middle;
    text-style: bold;
}

.header-button {
    width: auto;
    height: 1;
    min-width: 10;
    border: none;
    background: $accent;
}
.header-button:hover {
    background: $accent-light;
}

Footer {
    dock: bottom;
    height: 1;
    background: $surface;
    border-top: solid $accent;
    border-title-style: bold;
    border-title-align: center;
}

/* New Body Container for stable layout */
#body-container {
    height: 1fr;
    width: 100%;
    layout: vertical;
}

/* --- Conversation View --- */
#conversation-container {
    height: 1fr;
    width: 100%;
    padding: 1;
    background: $background;
    border: none;
}

ConversationListItem {
    height: auto;
    padding: 0 1 1 1;
}

#text-input {
    /* No longer docked. Its parent container manages its position. */
    height: 3;
    width: 100%;
    border-top: tall $accent;
    background: $surface;
}

/* --- Settings Panel (Slide-in) --- */
#settings-panel {
    layer: top;
    layout: vertical;
    background: $background;
    width: 55%;
    max-width: 80;
    min-width: 60;
    height: 100%;
    dock: right;
    display: none;
    border-left: wide $accent;
    offset-x: 100%;
    transition: offset 200ms in_out_cubic;
}

#settings-panel.visible {
    display: block;
    offset-x: 0;
}

#settings-header {
    width: 100%;
    height: 3;
    content-align: center middle;
    text-style: bold;
    background: $surface;
    border-bottom: solid $accent;
    dock: top;
}

TabbedContent {
    height: 1fr; /* This is key, it should fill the space */
}

TabPane {
    padding: 1;
    layout: vertical; /* Ensure panes lay out their content vertically */
}

TabPane > ScrollableContainer {
    height: 1fr;
    width: 100%;
}

#settings-close-button {
    width: 100%;
    height: 3;
    dock: bottom;
    background: $accent;
    border: none;
    margin: 0;
}
#settings-close-button:hover {
    background: $accent-light;
}

/* --- Widgets inside Settings --- */
/* Add some spacing for visual clarity */
ScrollableContainer > * {
    margin-bottom: 1;
}

Input {
    background: $surface;
    border: tall $secondary;
}
Input:focus {
    border: tall $accent;
}

OptionList {
    background: $surface;
    border: round $secondary;
    padding: 1;
    height: auto;
    max-height: 7;
}
OptionList:focus {
    border: round $accent;
}
OptionList > Option {
    background: transparent;
}
OptionList > .option--highlight {
    background: $accent;
    color: $text;
}

.model-buttons {
    layout: horizontal;
    height: 3;
    grid-size: 2;
    grid-gutter: 1;
}

.model-buttons Button {
    width: 1fr;
}
.model-buttons Button:disabled {
    background: $surface;
    color: $text-muted;
    border: tall $secondary;
}

.download-button {
    width: 100%;
    margin-top: 1;
}

.help-text {
    margin-top: 1;
    background: $surface;
    color: $text-muted;
    padding: 1;
    border: round $secondary;
    height: auto;
    text-style: italic;
}

/* --- Dialog Screens --- */
ConfirmScreen, DownloadScreen {
    align: center middle;
    background: $background 50%;
}

#confirm-dialog, #progress-dialog {
    padding: 1;
    border: wide $accent;
    background: $surface;
    width: 60;
}

#confirm-prompt {
    column-span: 2;
    width: 100%;
    content-align: center middle;
    margin: 1;
}
```

### File: `/corvus_app/ui/tui.py`
```py
# corvus_app/ui/tui.py
import logging
import webbrowser
from multiprocessing import Queue, Process
from queue import Empty
from pathlib import Path

from textual.app import App
from textual.widgets import Button

from corvus_app.audio.sound_player import sound_player, APP_START_SOUND, BUTTON_PRESS_SOUND
from corvus_app.ui.screens.main_screen import MainScreen
from corvus_app.ui.shared import (
    AssistantResponse, ModelDownloaded, StatusUpdate, STTModelDownloaded
)
from corvus_app.ui.themes import apply_theme, DARK_THEME, LIGHT_THEME

logger = logging.getLogger(__name__)

class CorvusTUI(App):
    """The main Textual application for Corvus."""
    TITLE = "Corvus AI Assistant"
    CSS_PATH = Path(__file__).parent / "tui.css"
    BINDINGS = [
        ("ctrl+c", "request_quit", "Quit"),
        ("ctrl+s", "toggle_settings", "Settings"),
        ("ctrl+t", "toggle_theme", "Theme"),
        ("ctrl+l", "open_logs", "Logs"),
    ]

    def __init__(self, ui_to_daemon_queue: Queue, daemon_to_ui_queue: Queue, daemon_process: Process):
        super().__init__()
        self.current_theme = DARK_THEME
        self.ui_to_daemon_queue = ui_to_daemon_queue
        self.daemon_to_ui_queue = daemon_to_ui_queue
        self.daemon_process = daemon_process
        self._listener_running = True

    def _listen_for_daemon_messages(self):
        """Worker to listen for messages from the daemon and post them to the app."""
        while self._listener_running:
            try:
                msg = self.daemon_to_ui_queue.get(timeout=0.2)
                
                msg_type = msg.get("type")
                if msg_type == "status_update":
                    self.post_message(StatusUpdate(msg["text"]))
                elif msg_type == "assistant_response":
                    self.post_message(AssistantResponse(msg["text"], msg["user_prompt"]))
                elif msg_type == "stt_download_complete":
                    self.post_message(STTModelDownloaded(msg["success"], msg["model_name"], msg.get("error")))
                elif msg_type == "shutdown_ack":
                    self.call_from_thread(self.exit)
                elif msg_type == "error":
                    self.call_from_thread(
                        self.notify,
                        msg["message"],
                        title=msg.get("title", "Error"),
                        severity="error",
                        timeout=10,
                    )
            except Empty:
                continue
            except Exception as e:
                logger.error(f"Error in listener thread: {e}", exc_info=True)

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        apply_theme(self, self.current_theme)
        sound_player.play(APP_START_SOUND)
        self.push_screen(MainScreen()) 
        self.run_worker(self._listen_for_daemon_messages, thread=True, name="daemon_listener")

    def on_unmount(self) -> None:
        """Called when the app is shutting down."""
        logger.info("UI shutting down, stopping listener.")
        self._listener_running = False

    def action_request_quit(self) -> None:
        """Gracefully shuts down the app and daemon."""
        logger.info("Quit requested, sending shutdown signal to daemon.")
        try:
            # Tell the daemon to shut down. The listener will get an ack and call self.exit()
            self.ui_to_daemon_queue.put({"type": "shutdown"}, timeout=1)
        except Exception:
            logger.error("Failed to send shutdown signal, forcing exit.")
            self.exit()
            
    def action_toggle_settings(self) -> None:
        """Toggles the settings panel on the main screen."""
        if isinstance(self.screen, MainScreen):
            self.screen.action_toggle_settings_panel()
            
    def action_toggle_theme(self) -> None:
        """Switches between light and dark themes."""
        self.current_theme = DARK_THEME if self.current_theme.name == "light" else LIGHT_THEME
        apply_theme(self, self.current_theme)

    def action_open_logs(self) -> None:
        """Opens the directory containing the log files."""
        log_dir = Path.cwd()
        self.action_open_url(f"file:///{log_dir.resolve()}")

    def action_open_url(self, url: str) -> None:
        """Opens a URL in the user's default web browser."""
        try:
            logger.info(f"Opening URL: {url}")
            webbrowser.open(url)
        except Exception as e:
            logger.error(f"Failed to open URL '{url}': {e}")
            self.notify(f"Could not open URL: {url}", title="Browser Error", severity="error")

    async def on_button_pressed(self, message: Button.Pressed) -> None:
        """Global handler for all button presses to play a sound."""
        sound_player.play(BUTTON_PRESS_SOUND)

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        if isinstance(self.screen, MainScreen):
            await self.screen.on_assistant_response(message)

    async def on_status_update(self, message: StatusUpdate) -> None:
        if isinstance(self.screen, MainScreen):
            await self.screen.on_status_update(message)

    async def on_model_downloaded(self, message: ModelDownloaded) -> None:
        if isinstance(self.screen, MainScreen):
            self.ui_to_daemon_queue.put({"type": "reload_models"})
            await self.screen.on_model_downloaded(message)
            
    async def on_stt_model_downloaded(self, message: STTModelDownloaded) -> None:
        if isinstance(self.screen, MainScreen):
            self.ui_to_daemon_queue.put({"type": "reload_models"})
            await self.screen.on_stt_model_downloaded(message)
```

### File: `/corvus_app/ui/worker.py`
```py
# corvus_app/ui/worker.py
import logging
from multiprocessing import Queue
from queue import Empty
import speech_recognition as sr

from PyQt6.QtCore import QObject, QRunnable, pyqtSignal

logger = logging.getLogger(__name__)

class WorkerSignals(QObject):
    status_update = pyqtSignal(str)
    assistant_response = pyqtSignal(str, str)
    error = pyqtSignal(str, str)
    stt_download_complete = pyqtSignal(bool, str, str)
    result = pyqtSignal(str) # Generic result signal for tasks like mic test

class QueueListener(QRunnable):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue
        self.signals = WorkerSignals()
        self.is_running = True

    def run(self):
        logger.info("QueueListener worker started.")
        while self.is_running:
            try:
                msg = self.queue.get(timeout=0.2)
                msg_type = msg.get("type")

                if msg_type == "status_update":
                    self.signals.status_update.emit(msg["text"])
                elif msg_type == "assistant_response":
                    self.signals.assistant_response.emit(msg["text"], msg["user_prompt"])
                elif msg_type == "error":
                    self.signals.error.emit(msg.get("title", "Error"), msg["message"])
                elif msg_type == "stt_download_complete":
                    self.signals.stt_download_complete.emit(
                        msg["success"], msg["model_name"], msg.get("error", "")
                    )

            except Empty:
                continue
            except Exception as e:
                logger.error(f"Error in QueueListener: {e}", exc_info=True)
        logger.info("QueueListener worker stopped.")

    def stop(self):
        self.is_running = False

class MicTestWorker(QRunnable):
    def __init__(self, device_index: int | None):
        super().__init__()
        self.device_index = device_index
        self.signals = WorkerSignals()

    def run(self):
        r = sr.Recognizer()
        r.pause_threshold = 0.5
        try:
            with sr.Microphone(device_index=self.device_index, sample_rate=16000) as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                if audio:
                    self.signals.result.emit("Success! Audio was detected.")
                else:
                    self.signals.result.emit("Inconclusive. No audio captured.")
        except sr.WaitTimeoutError:
            self.signals.result.emit("FAIL: No audio detected.")
        except Exception as e:
            self.signals.result.emit(f"FAIL: {e}")
```

### File: `/corvus_crash_report.log`
```log
============================================================================
==                   GEMINI AI - CORVUS CRASH REPORT                      ==
============================================================================
Timestamp: 2025-08-07T14:01:13.606161
App_Part: Main App Bootstrap

--- Environment ---
OS_Platform: Windows
OS_Release: 10 (Note: Windows 11 often reports as 10, this is normal)
OS_Version: 10.0.26100
Architecture: AMD64
Python_Version: 3.11.8

--- Error ---
Type: ImportError
Message: DLL load failed while importing onnxruntime_pybind11_state: A dynamic link library (DLL) initialization routine failed.

--- State Context ---
Active Llm Model: None

--- Traceback ---
```
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\main.py", line 34, in main
    from daemon_process import run_daemon_process
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\daemon_process.py", line 16, in <module>
    from corvus_app.assistant import Assistant
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\assistant.py", line 6, in <module>
    from corvus_app.tts.tts_engine import TTSEngine
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\tts\tts_engine.py", line 5, in <module>
    from piper.voice import PiperVoice
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\piper\__init__.py", line 4, in <module>
    from .voice import AudioChunk, PiperVoice
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\piper\voice.py", line 14, in <module>
    import onnxruntime
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\onnxruntime\__init__.py", line 61, in <module>
    raise import_capi_exception
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\onnxruntime\__init__.py", line 24, in <module>
    from onnxruntime.capi._pybind_state import (
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\onnxruntime\capi\_pybind_state.py", line 32, in <module>
    from .onnxruntime_pybind11_state import *  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ImportError: DLL load failed while importing onnxruntime_pybind11_state: A dynamic link library (DLL) initialization routine failed.
```

============================================================================
==                   GEMINI AI - CORVUS CRASH REPORT                      ==
============================================================================
Timestamp: 2025-08-07T14:11:13.795985
App_Part: Main App Bootstrap

--- Environment ---
OS_Platform: Windows
OS_Release: 10 (Note: Windows 11 often reports as 10, this is normal)
OS_Version: 10.0.26100
Architecture: AMD64
Python_Version: 3.11.8

--- Error ---
Type: ImportError
Message: cannot import name 'MicTestWorker' from 'corvus_app.ui.worker' (C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\ui\worker.py)

--- State Context ---
Active Llm Model: None

--- Traceback ---
```
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\main.py", line 45, in main
    from corvus_app.ui.main_window import MainWindow
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\ui\main_window.py", line 18, in <module>
    from corvus_app.ui.worker import QueueListener, MicTestWorker
ImportError: cannot import name 'MicTestWorker' from 'corvus_app.ui.worker' (C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\ui\worker.py)
```


```

### File: `/corvus_daemon.log`
```log
2025-08-07 14:14:14,127 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:14:14,127 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_daemon.log'. Log Level: INFO
2025-08-07 14:14:14,127 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:14:14,127 [MainThread  ] [Daemon                   ] [INFO    ]  Daemon process initializing.
2025-08-07 14:14:14,127 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Initializing Assistant...
2025-08-07 14:14:14,127 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 14:14:14,128 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:14:14,129 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:14:14,129 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:14:14,130 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:14:14,130 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:14:14,130 [MainThread  ] [plugins.registry         ] [INFO    ]  Initializing CommandRegistry, scanning 'plugins' for plugins.
2025-08-07 14:14:14,131 [MainThread  ] [plugins.registry         ] [INFO    ]  Discovered and loaded 2 command(s).
2025-08-07 14:14:14,132 [Thread-1 (_w] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 14:14:14,132 [MainThread  ] [Daemon                   ] [INFO    ]  Wake word listener started.
2025-08-07 14:14:14,132 [Thread-1 (_w] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 14:14:14,132 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:14:14,133 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:14:14,133 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:14:14,134 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:14:14,135 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:14:14,135 [Thread-1 (_w] [corvus_app.llm.llm_client] [WARNING ]  Local LLM functionality is disabled. Model loading is skipped.
2025-08-07 14:14:14,135 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Attempting to load STT model: 'medium.en'
2025-08-07 14:14:16,958 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  STT model 'medium.en' loaded successfully on cpu.
2025-08-07 14:14:17,058 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:14:24,135 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:14:32,071 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:14:32,071 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.921
2025-08-07 14:14:35,963 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.' (Lang: en, Prob: 1.00)
2025-08-07 14:14:36,060 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:14:40,415 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:14:40,415 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 14:14:44,298 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.' (Lang: en, Prob: 1.00)
2025-08-07 14:14:44,413 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:14:49,528 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:14:49,528 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.921
2025-08-07 14:14:53,883 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.  .  .  .  .' (Lang: en, Prob: 1.00)
2025-08-07 14:14:53,986 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:14:57,441 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:14:57,441 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 14:15:01,233 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:15:01,331 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:15:08,410 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:15:20,825 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:15:20,825 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:06.017

```

### File: `/daemon_process.py`
```py
# daemon_process.py
import logging
import re
import sys
import threading
from pathlib import Path
from queue import Empty

# We cannot assume the project root is in the path when run as a subprocess,
# so we add it manually.
_project_root = Path(__file__).resolve().parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

from corvus_app.app_settings import settings_manager
from corvus_app.assistant import Assistant
from corvus_app.audio.sound_player import sound_player, NOTIFICATION_SOUND
from corvus_app.audio.stt import listen_for_audio, get_stt_engine
from corvus_app.logging_config import setup_logging
from corvus_app.tts.tts_engine import speak_text, TTSEngine

# Logging is configured when the process starts in run_daemon_process
logger = logging.getLogger("Daemon")

class Daemon:
    """The background process that handles all AI and audio processing."""

    def __init__(self, ui_to_daemon_queue, daemon_to_ui_queue):
        self.ui_to_daemon_queue = ui_to_daemon_queue
        self.daemon_to_ui_queue = daemon_to_ui_queue
        self.assistant = None
        self._running = False
        self._listening = False
        self._listener_thread = None

    def _send_to_ui(self, message: dict):
        """Helper to put a message on the queue to the UI."""
        self.daemon_to_ui_queue.put(message)

    def _update_status(self, text: str):
        self._send_to_ui({"type": "status_update", "text": text})

    def _wake_word_loop(self):
        """Dedicated thread to listen for the wake word."""
        if not self.assistant:
             self.assistant = Assistant()
        self.assistant.reload()
        get_stt_engine() # Pre-load STT model in the thread
        self._update_status("LISTENING...")
        
        while self._listening and self._running:
            wake_word = settings_manager.get("wake_word")
            text, lang, prob = listen_for_audio()
            
            if not self._listening or not self._running: break
            
            if text and wake_word.lower() in text.lower():
                prompt = re.sub(rf'^\s*{re.escape(wake_word)}[\s,.]*', '', text, flags=re.IGNORECASE).strip()
                self._update_status("PROCESSING...")
                if prompt:
                    self.process_prompt(prompt, lang, prob)
                else:
                    self._speak_and_reset_status("Yes?")
                
                if self._listening: self._update_status("LISTENING...")

    def process_prompt(self, prompt: str, lang: str | None = None, prob: float | None = None):
        """Processes a prompt and speaks the response."""
        is_test = prompt.startswith("Test:")
        response = self.assistant.process_prompt(prompt, lang, prob)
        
        self._send_to_ui({"type": "assistant_response", "text": response, "user_prompt": "" if is_test else prompt})

        if not self.assistant.is_running:
            self._running = False
            self._send_to_ui({"type": "shutdown_ack"})
        elif not is_test:
            self._speak_and_reset_status(response)

    def _speak_and_reset_status(self, text: str):
        sound_player.play(NOTIFICATION_SOUND)
        error = speak_text(text)
        if error:
            self._send_to_ui({"type": "error", "message": f"TTS Error: {error}"})

    def _download_stt_model(self, model_name: str):
        """
        Handles the download of an STT model in a background thread.
        """
        logger.info(f"Starting STT model download for: {model_name}")
        try:
            import torch
            from faster_whisper import WhisperModel
            from models.stt_manager import STT_MODELS_PATH

            device = "cuda" if torch.cuda.is_available() else "cpu"
            compute_type = "float16" if device == "cuda" else "int8"
            
            WhisperModel(
                model_name,
                device=device,
                compute_type=compute_type,
                download_root=str(STT_MODELS_PATH)
            )
            
            logger.info(f"STT model '{model_name}' download/verification successful.")
            self._send_to_ui({"type": "stt_download_complete", "success": True, "model_name": model_name})

        except Exception as e:
            logger.error(f"Failed to download STT model '{model_name}': {e}", exc_info=True)
            self._send_to_ui({"type": "stt_download_complete", "success": False, "model_name": model_name, "error": str(e)})

    
    def start_listening(self):
        if self._listener_thread and self._listener_thread.is_alive(): return
        self._listening = True
        self._listener_thread = threading.Thread(target=self._wake_word_loop, daemon=True)
        self._listener_thread.start()
        logger.info("Wake word listener started.")

    def stop_listening(self):
        self._listening = False
        self._update_status("IDLE")
        logger.info("Wake word listener stopped.")

    def run(self):
        """Main loop for the daemon process."""
        self.assistant = Assistant()
        TTSEngine()  # Pre-load TTS
        self._running = True
        self.start_listening()

        while self._running:
            try:
                command = self.ui_to_daemon_queue.get(timeout=0.2)
                cmd_type = command.get("type")
                logger.debug(f"Daemon received command: {cmd_type}")

                if cmd_type == "process_text":
                    self.stop_listening()
                    self.process_prompt(command.get("payload"))
                    self.start_listening()
                elif cmd_type == "reload_models": self.assistant.reload()
                elif cmd_type == "shutdown": self._running = False
                elif cmd_type == "test_tts": self._speak_and_reset_status("This is a text to speech test.")
                elif cmd_type == "test_llm": self.process_prompt("Test: Say 'ok'")
                elif cmd_type == "start_listening": self.start_listening()
                elif cmd_type == "stop_listening": self.stop_listening()
                elif cmd_type == "download_stt":
                    model_name = command.get("model_name")
                    if model_name:
                        threading.Thread(target=self._download_stt_model, args=(model_name,), daemon=True).start()
                
            except Empty: continue
            except (KeyboardInterrupt, SystemExit):
                self._running = False
            except Exception as e: logger.error(f"Error in daemon loop: {e}", exc_info=True)
        
        logger.info("Daemon process loop finished, sending shutdown acknowledgement.")
        self._send_to_ui({"type": "shutdown_ack"})

def run_daemon_process(ui_to_daemon_queue, daemon_to_ui_queue):
    """Entry point for the daemon process, run by multiprocessing.Process."""
    setup_logging("corvus_daemon.log")
    logger.info("Daemon process initializing.")
    daemon = Daemon(ui_to_daemon_queue, daemon_to_ui_queue)
    daemon.run()
```

### File: `/installer.log`
```log
2025-08-07 14:07:22,515 [INFO    ]  Valid virtual environment found.
2025-08-07 14:07:22,519 [INFO    ]  Installing dependencies (this may take several minutes)...
2025-08-07 14:07:22,521 [INFO    ]  Running command: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt
2025-08-07 14:07:23,137 [INFO    ]  Requirement already satisfied: PyQt6 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (6.9.1)
2025-08-07 14:07:23,142 [INFO    ]  Requirement already satisfied: qtawesome in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 2)) (1.4.0)
2025-08-07 14:07:23,143 [INFO    ]  Requirement already satisfied: SpeechRecognition in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 3)) (3.14.3)
2025-08-07 14:07:23,144 [INFO    ]  Requirement already satisfied: PyAudio in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 4)) (0.2.14)
2025-08-07 14:07:23,144 [INFO    ]  Requirement already satisfied: rich in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (14.1.0)
2025-08-07 14:07:23,149 [INFO    ]  Requirement already satisfied: python-dotenv in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (1.1.1)
2025-08-07 14:07:23,150 [INFO    ]  Requirement already satisfied: requests in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2.32.4)
2025-08-07 14:07:23,151 [INFO    ]  Requirement already satisfied: sounddevice in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (0.5.2)
2025-08-07 14:07:23,152 [INFO    ]  Requirement already satisfied: soundfile in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9)) (0.13.1)
2025-08-07 14:07:23,435 [INFO    ]  Collecting onnxruntime==1.15.1 (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10))
2025-08-07 14:07:23,897 [INFO    ]  Downloading onnxruntime-1.15.1-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
2025-08-07 14:07:23,918 [INFO    ]  Requirement already satisfied: faster-whisper in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (1.2.0)
2025-08-07 14:07:23,919 [INFO    ]  Requirement already satisfied: piper-tts in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 12)) (1.3.0)
2025-08-07 14:07:23,920 [INFO    ]  Requirement already satisfied: coloredlogs in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (15.0.1)
2025-08-07 14:07:23,922 [INFO    ]  Requirement already satisfied: flatbuffers in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (25.2.10)
2025-08-07 14:07:23,926 [INFO    ]  Requirement already satisfied: numpy>=1.24.2 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.26.4)
2025-08-07 14:07:23,927 [INFO    ]  Requirement already satisfied: packaging in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (25.0)
2025-08-07 14:07:23,928 [INFO    ]  Requirement already satisfied: protobuf in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (6.31.1)
2025-08-07 14:07:23,932 [INFO    ]  Requirement already satisfied: sympy in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.14.0)
2025-08-07 14:07:23,934 [INFO    ]  Requirement already satisfied: PyQt6-sip<14,>=13.8 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from PyQt6->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (13.10.2)
2025-08-07 14:07:23,935 [INFO    ]  Requirement already satisfied: PyQt6-Qt6<6.10.0,>=6.9.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from PyQt6->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (6.9.1)
2025-08-07 14:07:23,936 [INFO    ]  Requirement already satisfied: qtpy in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from qtawesome->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 2)) (2.4.3)
2025-08-07 14:07:23,940 [INFO    ]  Requirement already satisfied: typing-extensions in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from SpeechRecognition->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 3)) (4.14.1)
2025-08-07 14:07:23,945 [INFO    ]  Requirement already satisfied: markdown-it-py>=2.2.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (3.0.0)
2025-08-07 14:07:23,951 [INFO    ]  Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (2.19.2)
2025-08-07 14:07:23,953 [INFO    ]  Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (3.4.2)
2025-08-07 14:07:23,954 [INFO    ]  Requirement already satisfied: idna<4,>=2.5 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (3.10)
2025-08-07 14:07:23,954 [INFO    ]  Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2.5.0)
2025-08-07 14:07:23,957 [INFO    ]  Requirement already satisfied: certifi>=2017.4.17 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2025.8.3)
2025-08-07 14:07:23,958 [INFO    ]  Requirement already satisfied: CFFI>=1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from sounddevice->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (1.17.1)
2025-08-07 14:07:23,968 [INFO    ]  Requirement already satisfied: ctranslate2<5,>=4.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (4.6.0)
2025-08-07 14:07:23,970 [INFO    ]  Requirement already satisfied: huggingface-hub>=0.13 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.34.3)
2025-08-07 14:07:23,971 [INFO    ]  Requirement already satisfied: tokenizers<1,>=0.13 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.21.4)
2025-08-07 14:07:23,972 [INFO    ]  Requirement already satisfied: av>=11 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (15.0.0)
2025-08-07 14:07:23,973 [INFO    ]  Requirement already satisfied: tqdm in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (4.67.1)
2025-08-07 14:07:23,988 [INFO    ]  Requirement already satisfied: pycparser in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from CFFI>=1.0->sounddevice->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (2.22)
2025-08-07 14:07:23,993 [INFO    ]  Requirement already satisfied: setuptools in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from ctranslate2<5,>=4.0->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (65.5.0)
2025-08-07 14:07:23,998 [INFO    ]  Requirement already satisfied: pyyaml<7,>=5.3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from ctranslate2<5,>=4.0->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (6.0.2)
2025-08-07 14:07:24,041 [INFO    ]  Requirement already satisfied: filelock in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub>=0.13->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (3.18.0)
2025-08-07 14:07:24,043 [INFO    ]  Requirement already satisfied: fsspec>=2023.5.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub>=0.13->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (2025.7.0)
2025-08-07 14:07:24,073 [INFO    ]  Requirement already satisfied: mdurl~=0.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from markdown-it-py>=2.2.0->rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (0.1.2)
2025-08-07 14:07:24,092 [INFO    ]  Requirement already satisfied: colorama in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from tqdm->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.4.6)
2025-08-07 14:07:24,102 [INFO    ]  Requirement already satisfied: humanfriendly>=9.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from coloredlogs->onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (10.0)
2025-08-07 14:07:24,111 [INFO    ]  Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from sympy->onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.3.0)
2025-08-07 14:07:24,144 [INFO    ]  Requirement already satisfied: pyreadline3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from humanfriendly>=9.1->coloredlogs->onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (3.5.4)
2025-08-07 14:07:24,420 [INFO    ]  Downloading onnxruntime-1.15.1-cp311-cp311-win_amd64.whl (6.7 MB)
2025-08-07 14:07:26,977 [INFO    ]  ---------------------------------------- 6.7/6.7 MB 2.6 MB/s eta 0:00:00
2025-08-07 14:07:27,609 [INFO    ]  Installing collected packages: onnxruntime
2025-08-07 14:07:27,614 [INFO    ]  Attempting uninstall: onnxruntime
2025-08-07 14:07:27,634 [INFO    ]  Found existing installation: onnxruntime 1.22.1
2025-08-07 14:07:27,683 [INFO    ]  Uninstalling onnxruntime-1.22.1:
2025-08-07 14:07:27,698 [INFO    ]  Successfully uninstalled onnxruntime-1.22.1
2025-08-07 14:07:30,034 [INFO    ]  Successfully installed onnxruntime-1.15.1
2025-08-07 14:07:30,189 [INFO    ]  [notice] A new release of pip is available: 24.0 -> 25.2
2025-08-07 14:07:30,190 [INFO    ]  [notice] To update, run: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install --upgrade pip
2025-08-07 14:07:30,275 [INFO    ]  Dependencies installed successfully!
2025-08-07 14:07:30,276 [INFO    ]  Wrote requirements hash 'd79e0cec9b2b65983bfd5721450070ec' to marker file.
2025-08-07 14:07:30,277 [INFO    ]  Setting up configuration...
2025-08-07 14:07:30,283 [INFO    ]  .env file already exists, skipping creation.
2025-08-07 14:07:30,283 [INFO    ]  Setup complete. The main application will now launch.

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
import hashlib
from logging.handlers import RotatingFileHandler
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, ProgressBar, RichLog, Static

# This script is run by the system python, so we need to add the project root to the path
# to find corvus_app for the sound player.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# --- Add sound player import ---
from corvus_app.audio.sound_player import (
    sound_player, INSTALL_START_SOUND, INSTALL_STEP_SOUND, 
    INSTALL_SUCCESS_SOUND, INSTALL_FAIL_SOUND
)

# --- Basic Setup ---
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
    log_path = PROJECT_ROOT / "installer.log"
    if log_path.exists():
        try:
            with open(log_path, 'w', encoding='utf-8') as f: f.truncate(0)
        except Exception: pass

    log_formatter = logging.Formatter("%(asctime)s [%(levelname)-8.8s]  %(message)s")
    log_file_handler = RotatingFileHandler(log_path, maxBytes=2*1024*1024, backupCount=1, encoding="utf-8")
    log_file_handler.setFormatter(log_formatter)
    logger = logging.getLogger("installer")
    logger.setLevel(logging.INFO)
    if logger.hasHandlers(): logger.handlers.clear()
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

class InstallerApp(App[bool]):
    CSS_PATH = PROJECT_ROOT / "installer" / "installer.css"
    TITLE = "Corvus App Installer"

    def compose(self) -> ComposeResult:
        with Container(id="installer-container"):
            yield Header("Corvus App Installer")
            yield RichLog(id="installer-log", wrap=True, highlight=True)
            yield ProgressBar(id="progress-bar", show_eta=True)
            with Footer():
                yield Static("Status: Initializing...", id="status-line")

    def on_mount(self) -> None:
        logger.addHandler(TuiLogHandler(self))
        sound_player.play(INSTALL_START_SOUND)
        self.run_worker(self.run_installation, thread=True, exclusive=True)

    def update_status(self, message: str, play_sound: bool = True):
        self.call_from_thread(self.query_one("#status-line", Static).update, f"Status: {message}")
        logger.info(message)
        if play_sound:
            sound_player.play(INSTALL_STEP_SOUND)

    def run_installation(self):
        try:
            self.ensure_venv()
            self.install_dependencies()
            self.create_env_file()
            self.update_status("Setup complete. The main application will now launch.", play_sound=False)
            sound_player.play(INSTALL_SUCCESS_SOUND)
            time.sleep(1)
            self.call_from_thread(self.exit, True) # Exit with success
        except Exception as e:
            self.update_status(f"[bold red]Installation failed: {e}[/]", play_sound=False)
            sound_player.play(INSTALL_FAIL_SOUND)
            logger.error("FATAL ERROR in installation orchestrator:", exc_info=True)
            self.call_from_thread(lambda: setattr(self.query_one(Footer).styles, 'background', 'red'))
            # On failure, we don't exit, so the user can see the error.

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
        req_path = PROJECT_ROOT / "requirements.txt"
        command = [str(VENV_PYTHON), "-m", "pip", "install", "-r", str(req_path)]
        logger.info(f"Running command: {' '.join(command)}")

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
        
        # Log pip output line by line
        if process.stdout:
            for line in iter(process.stdout.readline, ''):
                if line.strip(): logger.info(line.strip())
        
        process.wait() # Wait for the process to complete

        if process.returncode == 0:
            self.call_from_thread(progress_bar.update, progress=100)
            self.update_status("Dependencies installed successfully!")
            with open(req_path, 'rb') as f:
                req_hash = hashlib.md5(f.read()).hexdigest()
            with open(MARKER_FILE, 'w', encoding='utf-8') as f:
                f.write(req_hash)
            logger.info(f"Wrote requirements hash '{req_hash}' to marker file.")
        else:
            raise RuntimeError("Dependency installation failed. Check installer.log for details.")

    def create_env_file(self):
        self.update_status("Setting up configuration...")
        env_file = PROJECT_ROOT / ".env"
        if not env_file.exists():
            shutil.copy(PROJECT_ROOT / ".env.example", env_file)
            self.update_status(".env file created successfully from example.")
        else:
            self.update_status(".env file already exists, skipping creation.")

if __name__ == "__main__":
    app = InstallerApp()
    app.run()
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

### File: `/models/stt_manager.py`
```py
# models/stt_manager.py
import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

STT_MODELS_PATH = Path("stt_models")
STT_MODELS_PATH.mkdir(exist_ok=True)

# Official model sizes from faster-whisper and distil-whisper
AVAILABLE_MODELS = sorted([
    "tiny", "tiny.en",
    "base", "base.en",
    "small", "small.en",
    "medium", "medium.en",
    "large-v1", "large-v2", "large-v3",
    "distil-small.en", "distil-medium.en", "distil-large-v2"
])

def get_local_models():
    """Returns a list of locally downloaded Whisper models."""
    logger.info(f"Scanning for local STT models in: {STT_MODELS_PATH.resolve()}")
    if not STT_MODELS_PATH.exists():
        logger.warning(f"STT models path does not exist.")
        return []

    local_models = set()
    
    # Sort available models by length, descending, to match specific names first
    # e.g., match 'distil-medium.en' before 'medium'
    sorted_available_models = sorted(AVAILABLE_MODELS, key=len, reverse=True)

    # We iterate through the top-level directories in our STT models path
    for model_dir in STT_MODELS_PATH.iterdir():
        if not model_dir.is_dir():
            continue

        # Confirm that a model file actually exists before considering this a valid model directory.
        if not list(model_dir.rglob("model.bin")):
            logger.debug(f"No 'model.bin' found in {model_dir}, skipping.")
            continue

        dir_name_lower = model_dir.name.lower()
        logger.debug(f"Checking directory for model name: {dir_name_lower}")

        # Check which of our known models this directory corresponds to
        for model_name in sorted_available_models:
            # Check if the model name is present in the directory name. This handles various
            # huggingface naming conventions like '...-faster-whisper-base' and '...-faster-distil-whisper-medium.en'
            if model_name in dir_name_lower:
                if model_name not in local_models:
                    local_models.add(model_name)
                    logger.info(f"Found STT model '{model_name}' in directory '{model_dir.name}'")
                    # Found the most specific match for this directory, so we can move to the next directory.
                    break
    
    if not local_models:
        logger.warning("Could not identify any valid STT model subdirectories.")
        
    return sorted(list(local_models))

def delete_model(model_name: str):
    """Deletes a local Whisper model directory."""
    if not STT_MODELS_PATH.exists():
        return False
    try:
        # Find the directory that contains the model name
        for model_dir in STT_MODELS_PATH.iterdir():
            dir_name_lower = model_dir.name.lower()
            if model_dir.is_dir() and model_name.lower() in dir_name_lower:
                logger.info(f"Deleting STT model directory: {model_dir}")
                shutil.rmtree(model_dir)
                logger.info(f"Successfully deleted model: {model_name}")
                return True
        logger.warning(f"Could not find directory for STT model to delete: {model_name}")
        return False
    except Exception as e:
        logger.error(f"Failed to delete STT model {model_name}: {e}", exc_info=True)
        return False

# Download is handled by the STT engine's initialization, so no direct download function here.
# The engine will be responsible for calling its own loader, which will use this path.
```

### File: `/models/tts_manager.py`
```py
# models/tts_manager.py
import logging
import shutil
import json
from pathlib import Path
import urllib.request

from .downloader import download_file

logger = logging.getLogger(__name__)

TTS_MODELS_PATH = Path("tts_models")
TTS_MODELS_PATH.mkdir(exist_ok=True)

VOICES_URL = "https://huggingface.co/rhasspy/piper-voices/raw/main/voices.json"
_voices_index = {}

def get_remote_models_list() -> dict[str, str]:
    """
    Downloads and caches the official Piper voices index from Hugging Face.
    Returns a dictionary of model_id: user_friendly_name for UI display.
    The full data is stored in the internal _voices_index.
    """
    global _voices_index
    if _voices_index:
        # Return only the user-friendly names for the UI list
        return {model_id: info['friendly_name'] for model_id, info in _voices_index.items()}

    logger.info(f"Fetching remote TTS voice index from {VOICES_URL}")
    try:
        with urllib.request.urlopen(VOICES_URL) as response:
            remote_data = json.load(response)

        # Reformat the data into a more usable dictionary
        formatted_voices = {}
        for model_id, model_info in remote_data.items():
            # Create a user-friendly name, e.g., "English (US) - Lessac Medium"
            name = model_info.get("name", model_id)
            language = model_info.get("language", {}).get("name_english", "Unknown")
            quality = model_info.get("quality", "Unknown")
            
            # Filter out low quality voices for a better user experience
            if quality.lower() != "high":
                friendly_name = f"{language} - {name} ({quality.capitalize()})"
                # Store the full data internally, but prepare the friendly name
                formatted_voices[model_id] = model_info
                formatted_voices[model_id]['friendly_name'] = friendly_name
        
        _voices_index = formatted_voices
        logger.info(f"Successfully fetched and parsed {len(_voices_index)} TTS voices.")
        return {model_id: info['friendly_name'] for model_id, info in _voices_index.items()}

    except Exception as e:
        logger.error(f"Failed to fetch or parse remote voices index: {e}", exc_info=True)
        return {"error": "Could not fetch remote voice list."}


def get_local_models_list() -> dict[str, str]:
    """
    Finds installed Piper TTS models and returns a dict of model_id to friendly_name.
    """
    if not _voices_index:
        get_remote_models_list() # Ensure index is loaded to get friendly names

    if not TTS_MODELS_PATH.exists():
        return {}
    
    local_models = {}
    for model_dir in TTS_MODELS_PATH.iterdir():
        model_id = model_dir.name
        if model_dir.is_dir() and (model_dir / f"{model_id}.onnx").exists():
            friendly_name = _voices_index.get(model_id, {}).get("friendly_name", model_id)
            local_models[model_id] = friendly_name
            
    return local_models

def _find_file_url(model_files: dict, suffix: str) -> str | None:
    """Intelligently finds the URL for a file in the model's file index, regardless of its key."""
    for key, file_info in model_files.items():
        if key.endswith(suffix):
            return file_info.get("url")
    return None

def download_model(model_id: str, progress_callback: callable):
    """
    Downloads a Piper TTS model using the official download URLs from the fetched index.
    """
    logger.info(f"Starting download for TTS model: {model_id}")
    if not _voices_index:
        get_remote_models_list() # Ensure index is loaded

    model_info = _voices_index.get(model_id)
    if not model_info:
        progress_callback("error", message=f"Model '{model_id}' not found in remote index.")
        return

    model_files = model_info.get("files", {})
    
    # --- Download ONNX model ---
    onnx_url = _find_file_url(model_files, ".onnx")
    onnx_filename = f"{model_id}.onnx"
    if not onnx_url:
        progress_callback("error", message="Could not find model URL in index.")
        return
        
    model_dir = TTS_MODELS_PATH / model_id
    model_dir.mkdir(exist_ok=True)

    logger.info(f"Downloading ONNX model from {onnx_url}")
    onnx_path = download_file(onnx_url, model_dir, onnx_filename, progress_callback)
    if not onnx_path:
        return # download_file already called the error callback
        
    # --- Download JSON config ---
    json_url = _find_file_url(model_files, ".onnx.json")
    json_filename = f"{model_id}.onnx.json"
    if not json_url:
        progress_callback("error", message="Could not find config URL in index.")
        return

    logger.info(f"Downloading model config from {json_url}")
    json_path = download_file(json_url, model_dir, json_filename, lambda *args: None) # No progress
    
    if not json_path:
        progress_callback("error", message="Failed to download model config.")
        return

    logger.info(f"Successfully downloaded all files for TTS model: {model_id}")

def delete_model(model_id: str):
    """Deletes a local TTS model directory."""
    try:
        model_path = TTS_MODELS_PATH / model_id
        if model_path.exists() and model_path.is_dir():
            logger.info(f"Attempting to delete TTS model directory: {model_path}")
            shutil.rmtree(model_path)
            logger.info(f"Successfully deleted model: {model_id}")
            return True
        else:
            logger.warning(f"Attempted to delete a non-existent TTS model: {model_id}")
            return False
    except Exception as e:
        logger.error(f"Failed to delete model {model_id}: {e}", exc_info=True)
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
PyQt6
qtawesome
SpeechRecognition
PyAudio
rich
python-dotenv
requests
sounddevice
soundfile
onnxruntime==1.15.1
faster-whisper
piper-tts
```

### File: `/run.py`
```py
# run.py
import sys
import subprocess
import os
import traceback
import hashlib
from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from corvus_app.crash_handler import format_crash_report

TEXTUAL_VERSION = "0.58.0"
VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"

if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"

def check_textual_for_installer():
    """Ensures Textual is available for the installer UI, installing it if necessary."""
    try:
        # Don't check version, just ensure it's installed. The specific version
        # isn't critical for this simple UI.
        import textual
        return True
    except ImportError:
        print("[LAUNCHER] Textual not found. Installing for installer UI...")
    
    try:
        # Use --user to avoid permission errors
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"textual=={TEXTUAL_VERSION}", "--user"])
        print("[LAUNCHER] Textual prepared successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[FATAL] Could not install Textual for the installer. Pip may be broken. Error: {e}")
        return False

def is_venv_ok():
    """Checks if venv exists and if requirements are up-to-date via a hash check."""
    if not (VENV_PYTHON.exists() and MARKER_FILE.exists()):
        return False

    try:
        with open(PROJECT_ROOT / 'requirements.txt', 'rb') as f:
            current_hash = hashlib.md5(f.read()).hexdigest()
        
        with open(MARKER_FILE, 'r', encoding='utf-8') as f:
            installed_hash = f.read().strip()

        return current_hash == installed_hash
    except Exception as e:
        print(f"[LAUNCHER] Could not verify dependencies, running setup. Reason: {e}")
        return False

def launch_installer():
    """Runs the Textual installer UI application."""
    print("[LAUNCHER] Launching Installer/Repair UI...")
    if not check_textual_for_installer():
        return False
        
    from installer.installer_tui import InstallerApp
    app = InstallerApp()
    # The TUI app returns True on success, False or nothing on failure/exit
    success = app.run()
    return success is True

def launch_main_app():
    """Launches the main Corvus application entry point."""
    print("[LAUNCHER] Launching Corvus Application...")
    main_app_module = "corvus_app.main"
    command = [str(VENV_PYTHON), "-m", main_app_module]
    env = os.environ.copy()
    env['PYTHONPATH'] = str(PROJECT_ROOT)

    try:
        subprocess.run(command, env=env, check=False)
    except FileNotFoundError:
        raise RuntimeError(f"Could not find Python executable in venv: '{VENV_PYTHON}'.")
    except Exception as e:
        tb_info = traceback.format_exc()
        format_crash_report("Launcher", e, tb_info)
    finally:
        print("\n[LAUNCHER] Corvus application has closed.")

def main():
    """Main entry point for the application launcher."""
    try:
        print("[LAUNCHER] Initializing Corvus...")
        if is_venv_ok():
            launch_main_app()
        else:
            print("[LAUNCHER] Virtual environment not found or outdated. Starting setup process...")
            if launch_installer():
                print("[LAUNCHER] Setup complete. Launching application...")
                launch_main_app()
            else:
                print("\n[LAUNCHER] Setup was cancelled or failed. The application cannot start.")
    except Exception as e:
        tb_info = traceback.format_exc()
        format_crash_report("Launcher Bootstrap", e, tb_info)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### File: `/settings.json`
```json
{
    "active_llm_model": null,
    "active_tts_model": null,
    "active_stt_model": "medium.en",
    "wake_word": "computer",
    "system_prompt": "You are a helpful and adaptive AI assistant. You can learn about the user to improve your interactions.\nA special file, `user_profile.md`, stores notes about the user's speech and preferences. You will receive its contents with each prompt.\nYou will also receive language detection info with each voice prompt, like `(speaking en with 0.75 confidence)`. A low confidence score may indicate a user's accent.\n\nYOUR TASK:\n1. Analyze the user's request, their profile notes, and any language detection info.\n2. Formulate a direct, helpful response to the user. Be patient and accommodating if an accent is detected.\n3. If you learn something new about the user (e.g., they have an accent, they stutter, they mispronounce a word), you MUST update their profile.\n\nHOW TO UPDATE THE PROFILE:\nYour response MUST be formatted as follows. First the update tag, then the spoken response:\n`[UPDATE_PROFILE]`\nThe complete, new markdown content for the user's profile.\n`[/UPDATE_PROFILE]`\nYour normal, spoken response to the user.\n\nIf no update is needed, just provide the spoken response without any tags.\n\nEXAMPLE:\nUSER (speaking en with 0.65 confidence): 'Corvus, vhat is ze time?'\nYOUR RESPONSE SHOULD BE:\n`[UPDATE_PROFILE]`\n# User Profile\n\n## Notes\n- The user appears to have a German accent (e.g., 'vhat' for 'what').\n`[/UPDATE_PROFILE]`\nThe current time is 2:30 PM.",
    "input_device_index": null,
    "output_device_index": null,
    "stt_pause_threshold": 0.8,
    "stt_dynamic_energy": true
}
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

### File: `/user_profile.md`
```md
# User Profile

## Notes
- This file is for the AI to keep notes on the user's speech patterns and preferences.
- The AI will read this file before responding and update it when it learns something new.
```