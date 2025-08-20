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
│   │   ├── shared.py
│   │   ├── themes.py
│   │   ├── tui.css
│   │   └── tui.py
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
│   ├── hf_utils.py
│   ├── llm_manager.py
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
├── debug.css
├── debug.py
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
2025-08-06 22:37:02,153 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-06 22:37:02,153 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_app.log'. Log Level: INFO
2025-08-06 22:37:02,153 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-06 22:37:02,153 [MainThread  ] [__main__                 ] [INFO    ]  Corvus application starting up.
2025-08-06 22:37:04,460 [MainThread  ] [corvus_app.audio.stt     ] [INFO    ]  Attempting to load STT model: 'medium.en'
2025-08-06 22:37:06,967 [MainThread  ] [corvus_app.audio.stt     ] [INFO    ]  STT model 'medium.en' loaded successfully on cpu.
2025-08-06 22:37:07,078 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Initializing Assistant...
2025-08-06 22:37:07,078 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-06 22:37:07,078 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-06 22:37:07,079 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-06 22:37:07,080 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-06 22:37:07,080 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-06 22:37:07,081 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-06 22:37:07,081 [MainThread  ] [plugins.registry         ] [INFO    ]  Initializing CommandRegistry, scanning 'plugins' for plugins.
2025-08-06 22:37:07,082 [MainThread  ] [plugins.registry         ] [INFO    ]  Discovered and loaded 2 command(s).
2025-08-06 22:37:07,082 [MainThread  ] [corvus_app.llm.llm_client] [INFO    ]  Attempting to load LLM model: 'llm_models\stablelm-zephyr-3b.Q5_K_M.gguf'
2025-08-06 22:37:07,539 [MainThread  ] [corvus_app.llm.llm_client] [INFO    ]  LLM model 'llm_models\stablelm-zephyr-3b.Q5_K_M.gguf' loaded successfully.
2025-08-06 22:37:07,551 [MainThread  ] [corvus_app.audio.sound_pl] [WARNING ]  Sound file not found: C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\assets\sounds\app_start.wav
2025-08-06 22:37:07,720 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-06 22:37:13,889 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-06 22:37:13,890 [asyncio_3   ] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-06 22:37:17,654 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-06 22:37:17,764 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-06 22:37:26,094 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-06 22:37:26,094 [asyncio_3   ] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:04.929
2025-08-06 22:37:30,395 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.  .  .  .  .' (Lang: en, Prob: 1.00)
2025-08-06 22:37:30,502 [asyncio_3   ] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...

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
from models.llm_manager import get_local_models as get_local_llm_models
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

        # --- Validate LLM Model ---
        active_llm = settings_manager.get("active_llm_model")
        if active_llm:
            # get_local_llm_models returns Path objects, so convert to strings for comparison
            local_llm_models = [str(p) for p in get_local_llm_models()]
            if active_llm not in local_llm_models:
                logger.warning(
                    f"Active LLM model '{active_llm}' not found in local models. "
                    "Resetting to None. Please select a new model in settings."
                )
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

# Singleton instance of the engine
stt_engine = STTEngine()

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
        f"OS_Release: {platform.release()}",
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
import re
from llama_cpp import Llama
from corvus_app.app_settings import settings_manager
from corvus_app.tools.user_profile import user_profile_manager

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

    def get_response(self, prompt: str, lang: str | None = None, prob: float | None = None) -> str:
        """
        Generates a text response from the loaded LLM for a given prompt.
        It also handles reading/writing to the user profile based on LLM output.
        """
        if not self._llm:
            logger.error("LLM not loaded, cannot get response.")
            return "I can't respond right now as my language model is not loaded. Please select a model in the settings."

        logger.debug(f"Generating LLM response for prompt: '{prompt}'")
        
        system_prompt = settings_manager.get("system_prompt")
        profile_content = user_profile_manager.read()

        if lang and prob is not None:
            user_line = f"User (speaking {lang} with {prob:.2f} confidence): {prompt}"
        else:
            user_line = f"User: {prompt}"

        full_prompt = (
            f"System: {system_prompt}\n\n"
            f"--- CURRENT USER PROFILE ---\n{profile_content}\n--- END OF PROFILE ---\n\n"
            f"{user_line}\n"
            f"Assistant:"
        )
        
        try:
            output = self._llm(
                full_prompt,
                max_tokens=512,  # Increased to allow space for profile + response
                stop=["User:", "\nSystem:"],
                echo=False,
                temperature=0.7
            )
            raw_response = output['choices'][0]['text'].strip()

            # Check for profile update command from the LLM
            update_match = re.search(r"`\[UPDATE_PROFILE\]`(.+?)`\[/UPDATE_PROFILE\]`", raw_response, re.DOTALL)
            
            if update_match:
                new_profile_content = update_match.group(1).strip()
                user_profile_manager.write(new_profile_content)
                
                # The rest of the string is the spoken response
                spoken_response = raw_response[update_match.end():].strip()
                logger.info("LLM updated user profile.")
            else:
                spoken_response = raw_response

            logger.info(f"LLM generated response: '{spoken_response}'")
            return spoken_response

        except Exception as e:
            logger.error(f"Error during LLM inference: {e}", exc_info=True)
            return "I'm sorry, I encountered an error while thinking of a response."
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
import logging
import traceback
from datetime import datetime
from pathlib import Path
from rich.console import Console

# Must be imported before other app components
from corvus_app.crash_handler import format_crash_report

_console = Console()

def bootstrap():
    """Initial setup for directories and logging."""
    try:
        Path("tts_models").mkdir(exist_ok=True)
        Path("llm_models").mkdir(exist_ok=True)
        Path("stt_models").mkdir(exist_ok=True)
        from corvus_app.logging_config import setup_logging
        setup_logging(log_filename="corvus_app.log")
    except Exception as e:
        # Bootstrap failures are critical and don't have full app context yet
        with open("bootstrap_crash.log", "w", encoding="utf-8") as f:
            f.write(f"--- Corvus Bootstrap Crash Report ---\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\nError: {e}\n")
            traceback.print_exc(file=f)
        _console.print("[bold red]FATAL: Failed to configure application logging during bootstrap.[/bold red]")
        _console.print("[bold red]A 'bootstrap_crash.log' has been created. Exiting.[/bold red]")
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
    except Exception as e:
        tb_info = traceback.format_exc()
        # On a main app crash, gather more context for the report
        from corvus_app.app_settings import settings_manager
        context = {
            "active_llm_model": settings_manager.get("active_llm_model"),
            "active_tts_model": settings_manager.get("active_tts_model"),
        }
        format_crash_report("Main App", e, tb_info, context)
        sys.exit(1) # Ensure the app closes after a crash
    finally:
        logger.info("Application shutdown sequence finished.\n\n")

if __name__ == "__main__":
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
    
    # Release the active log file handle before attempting deletion
    _release_main_log_file()
    
    files_to_delete = [
        "settings.json", ".env", "corvus_app.log", "corvus_crash_report.log", 
        "installer.log", "output.wav", "user_profile.md"
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
from models import llm_manager, tts_manager

logger = logging.getLogger(__name__)

DownloadType = Literal["llm", "tts"]

class DownloadScreen(ModalScreen):
    """A modal screen for downloading models."""

    def __init__(self, model_info: dict, download_type: DownloadType):
        super().__init__()
        self.model_info = model_info
        self.download_type = download_type
        if self.download_type == "llm":
            self.title = f"LLM: {self.model_info.get('filename', 'Unknown')}"
        else:
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
        if self.download_type == "llm":
            llm_manager.download_model(
                self.model_info["url"], self.model_info["filename"], self.on_download_progress
            )
        elif self.download_type == "tts":
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
import re
from typing import Literal

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, ScrollableContainer, Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import (
    Button, Footer, Input, Label, ListView, OptionList, Static, TabbedContent, TabPane
)
from textual.widgets.option_list import Option

from corvus_app.app_settings import settings_manager
from corvus_app.assistant import Assistant
from corvus_app.audio import device_manager
from corvus_app.audio.stt import listen_for_audio, stt_engine
from corvus_app.tts.tts_engine import speak_text
from corvus_app.tools import cleaner
from corvus_app.ui.screens.confirm_screen import ConfirmScreen
from corvus_app.ui.screens.download_screen import DownloadScreen, DownloadType
from corvus_app.ui.shared import (
    AssistantResponse, ConversationListItem, ModelDownloaded, StatusUpdate
)
from models import hf_utils, llm_manager, tts_manager, stt_manager

logger = logging.getLogger(__name__)

class MainScreen(Screen):
    BINDINGS = [Binding("tab", "toggle_input_mode", "Toggle Input", show=True)]

    def __init__(self, assistant: Assistant, **kwargs):
        super().__init__(**kwargs)
        self.assistant = assistant
        self.input_mode = "voice"

    def compose(self) -> ComposeResult:
        with Container(id="main-container"):
            with Container(id="app-header"):
                yield Static("Corvus Assistant", id="header-title")
                yield Button("Clear Memory", id="clear-button")
                yield Button("Settings", id="settings-button")
            yield ScrollableContainer(ListView(id="conversation"), id="conversation-container")
            yield Input(placeholder="Type your message...", id="text-input")
            yield Footer()

        with Vertical(id="settings-panel"):
            with ScrollableContainer(id="settings-panel-container"):
                with TabbedContent(id="settings-tabs"):
                    with TabPane("Models", id="tab-models"):
                        yield from self.compose_models_pane()
                    with TabPane("Personality", id="tab-personality"):
                        yield from self.compose_personality_pane()
                    with TabPane("System", id="tab-system"):
                        yield from self.compose_system_pane()
                yield Button("Close Settings", id="settings-close-button", variant="primary")

    def compose_models_pane(self):
        """Compose the content for the Models tab."""
        yield Label("Language Models (LLM)")
        yield OptionList(id="llm-option-list")
        with Horizontal(classes="model-buttons"):
            yield Button("Set Active", id="llm-set-active-button", variant="success")
            yield Button("Delete", id="llm-delete-button", variant="error")
        yield Label("Download New LLM")
        with Horizontal(classes="input_bar"):
            yield Input(id="hf-repo-input", placeholder="TheBloke/Repo-Name-GGUF")
            yield Button("Fetch", id="hf-fetch-button")
        yield OptionList(id="llm-download-list")
        yield Button("Download Selected LLM", id="llm-download-button", classes="download-button")
        
        yield Static("---", classes="separator")
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

    def compose_personality_pane(self):
        """Compose the content for the Personality tab."""
        yield Label("System Prompt (Assistant's Personality)")
        yield Input(id="system-prompt-input", placeholder="e.g., You are a witty pirate captain.")
        yield Button("Save Personality", id="save-personality-button")

    def compose_system_pane(self):
        """Compose the content for the System tab."""
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
            yield Button("Test LLM", id="test-llm-button")
        yield Static("---", classes="separator")
        yield Label("Utilities")
        yield Button("Clean Models", id="clean-models-button", variant="warning")
        yield Button("Clean Logs/Settings", id="clean-logs-button", variant="warning")
        yield Button("Clean Cache", id="clean-cache-button", variant="warning")

    def on_mount(self) -> None:
        self.query_one("#text-input", Input).display = False
        self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True)

    async def on_button_pressed(self, msg: Button.Pressed) -> None:
        button_id = msg.button.id
        if button_id in ("settings-button", "settings-close-button"): self.action_toggle_settings_panel()
        elif button_id == "clear-button": self.action_clear_conversation()
        elif button_id == "save-wake-word-button": self.action_save_wake_word()
        elif button_id == "save-personality-button": self.action_save_personality()
        elif button_id == "save-stt-settings-button": self.action_save_stt_settings()
        elif button_id == "llm-set-active-button": self.set_active_model("llm")
        elif button_id == "llm-delete-button": await self.delete_model("llm")
        elif button_id == "llm-download-button": self.download_model("llm")
        elif button_id == "hf-fetch-button": self.fetch_hf_repo_files()
        elif button_id == "tts-set-active-button": self.set_active_model("tts")
        elif button_id == "tts-delete-button": await self.delete_model("tts")
        elif button_id == "tts-download-button": self.download_model("tts")
        elif button_id == "stt-set-active-button": self.set_active_model("stt")
        elif button_id == "stt-delete-button": await self.delete_model("stt")
        elif button_id == "stt-download-button": self.download_stt_model()
        elif button_id == "test-mic-button": self.run_worker(self.run_mic_test, thread=True)
        elif button_id == "test-tts-button": self.run_worker(self.run_tts_test, thread=True)
        elif button_id == "test-llm-button": self.run_worker(self.run_llm_test, thread=True, exclusive=True)
        elif button_id == "clean-models-button": await self.run_cleaner("models", "Delete ALL downloaded models?", cleaner.clean_models)
        elif button_id == "clean-logs-button": await self.run_cleaner("logs", "Delete ALL logs and user settings?", cleaner.clean_logs_settings)
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
        if msg.model_type == "llm": self.update_llm_options()
        elif msg.model_type == "tts": self.update_tts_options()
        # No STT here, as its download is handled differently

    def action_clear_conversation(self):
        self.query_one("#conversation", ListView).clear()
        self.app.notify("Conversation history cleared.")

    def action_save_wake_word(self):
        settings_manager.set("wake_word", self.query_one("#wake-word-input", Input).value)
        self.app.notify("Wake word updated.")
        
    def action_save_personality(self):
        settings_manager.set("system_prompt", self.query_one("#system-prompt-input", Input).value)
        self.app.notify("Personality updated.")
        self.assistant.llm_client.reload_model()

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
            if self.input_mode == "voice": self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True)
            self.assistant.reload()
        else:
            self.app.workers.cancel_group(self, "audio_input")
            self.populate_settings()
            panel.add_class("visible")
            
    def populate_settings(self):
        self.query_one("#wake-word-input").value = settings_manager.get("wake_word")
        self.query_one("#system-prompt-input").value = settings_manager.get("system_prompt")
        self.query_one("#stt-pause-threshold-input").value = str(settings_manager.get("stt_pause_threshold"))
        self.update_llm_options()
        self.update_tts_options()
        self.update_stt_options()
        self.update_audio_device_options()
        self.run_worker(self.fetch_remote_tts_models, thread=True)
        self.populate_stt_download_list()

    def update_llm_options(self):
        opt_list = self.query_one("#llm-option-list", OptionList)
        active_model = settings_manager.get("active_llm_model")
        opt_list.clear_options()
        for model_path in llm_manager.get_local_models():
            model_str = str(model_path)
            is_active = model_str == active_model
            opt_list.add_option(Option(f"{model_path.name}{' (Active)' if is_active else ''}", id=model_str))

    def update_tts_options(self):
        opt_list = self.query_one("#tts-option-list", OptionList)
        active_model = settings_manager.get("active_tts_model")
        opt_list.clear_options()
        local_models = tts_manager.get_local_models_list()
        
        if not local_models:
            opt_list.add_option(Option("No local voice models found.", disabled=True))
            return

        all_voices = tts_manager.get_remote_models_list()

        for model_id in local_models:
            is_active = model_id == active_model
            friendly_name = all_voices.get(model_id, model_id)
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

    def set_active_model(self, model_type: Literal["llm", "tts", "stt"]):
        opt_list = self.query_one(f"#{model_type}-option-list", OptionList)
        if opt_list.highlighted is not None:
            highlighted_option = opt_list.get_option_at_index(opt_list.highlighted)
            if highlighted_option.disabled:
                self.app.bell()
                return
            selected_id = highlighted_option.id
            settings_manager.set(f"active_{model_type}_model", selected_id)
            if model_type == "llm": self.update_llm_options()
            elif model_type == "tts": self.update_tts_options()
            else: self.update_stt_options()
            self.app.notify(f"Active {model_type.upper()} model set.")
            
    async def delete_model(self, model_type: Literal["llm", "tts", "stt"]):
        opt_list = self.query_one(f"#{model_type}-option-list", OptionList)
        if opt_list.highlighted is not None:
            highlighted_option = opt_list.get_option_at_index(opt_list.highlighted)
            if highlighted_option.disabled:
                self.app.bell()
                return
            selected_id = highlighted_option.id

            async def on_confirm(confirmed: bool):
                if confirmed:
                    if model_type == "llm":
                        llm_manager.delete_model(selected_id)
                        if settings_manager.get("active_llm_model") == selected_id:
                            settings_manager.set("active_llm_model", None)
                        self.update_llm_options()
                    elif model_type == "tts":
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

    def fetch_hf_repo_files(self):
        repo_id = self.query_one("#hf-repo-input").value
        if not repo_id: return
        opt_list = self.query_one("#llm-download-list")
        self.app.call_from_thread(opt_list.clear_options)
        self.app.call_from_thread(opt_list.add_option, Option("Fetching..."))
        files = hf_utils.list_gguf_files_from_repo(repo_id)
        self.app.call_from_thread(opt_list.clear_options)
        if files:
            for file_info in files:
                self.app.call_from_thread(opt_list.add_option, Option(file_info['filename'], id=file_info['url']))
        else:
             self.app.call_from_thread(opt_list.add_option, Option("No GGUF files found."))

    def fetch_remote_tts_models(self):
        """Fetches the list of downloadable TTS models from Piper."""
        opt_list = self.query_one("#tts-download-list", OptionList)
        self.app.call_from_thread(opt_list.clear_options)
        self.app.call_from_thread(opt_list.add_option, Option("Fetching available voices..."))
        
        models = tts_manager.get_remote_models_list()
        
        self.app.call_from_thread(opt_list.clear_options)
        if models:
            for model_id, friendly_name in models.items():
                self.app.call_from_thread(opt_list.add_option, Option(friendly_name, id=model_id))
        else:
            self.app.call_from_thread(opt_list.add_option, Option("Could not fetch remote models."))

    def populate_stt_download_list(self):
        opt_list = self.query_one("#stt-download-list", OptionList)
        opt_list.clear_options()
        for model_name in stt_manager.AVAILABLE_MODELS:
            opt_list.add_option(Option(model_name, id=model_name))

    def download_model(self, download_type: DownloadType):
        list_id = f"#{'llm' if download_type == 'llm' else 'tts'}-download-list"
        opt_list = self.query_one(list_id, OptionList)
        if opt_list.highlighted is None: return
        selected_opt = opt_list.get_option_at_index(opt_list.highlighted)
        model_id = selected_opt.id
        if not model_id: return
        if download_type == "llm": model_info = {"url": model_id, "filename": str(selected_opt.prompt)}
        else: model_info = {"model_name": model_id}
        self.app.push_screen(DownloadScreen(model_info, download_type))
    
    def download_stt_model(self):
        opt_list = self.query_one("#stt-download-list", OptionList)
        if opt_list.highlighted is None: return
        model_name = opt_list.get_option_at_index(opt_list.highlighted).id
        if not model_name: return

        self.app.notify(f"Downloading STT model '{model_name}'. App may freeze.", timeout=10)
        
        def _download():
            # This is a blocking operation, so it's run in a worker.
            stt_engine.reload_model(model_name_override=model_name)
            
            # After download/load, update the UI from the worker thread
            def _update_ui():
                self.update_stt_options()
                self.app.notify(f"STT model '{model_name}' ready.")
            self.app.call_from_thread(_update_ui)

        self.run_worker(_download, thread=True, exclusive=True, group="model_download")

    async def run_cleaner(self, name: str, prompt: str, clean_func: callable):
        async def on_confirm(confirmed: bool):
            if confirmed:
                self.app.notify(f"Running {name} cleaner...")
                clean_func()
                if "logs" in name or "models" in name: self.populate_settings()
                self.app.notify(f"{name.capitalize()} cleanup complete.")
        await self.app.push_screen(ConfirmScreen(prompt), on_confirm)

    def run_mic_test(self):
        status = self.query_one("#mic-test-status", Static)
        status.update("TESTING: Say something...")
        self.app.notify("Listening for mic test...")
        text, lang, prob = listen_for_audio()
        if text:
            status.update(f"[green]Success! Heard: '{text}' (Lang: {lang}, Conf: {prob:.2f})[/green]")
        else:
            status.update("[red]FAIL: No clear audio recognized.[/red]")

    def run_tts_test(self):
        self.app.notify("Testing TTS... you should hear audio.")

        def _tts_test_worker():
            error = speak_text("This is a text to speech test.")
            if error:
                self.app.call_from_thread(
                    self.app.notify,
                    f"TTS Test Failed: {error}",
                    title="TTS Error",
                    severity="error",
                    timeout=10,
                )
        self.run_worker(_tts_test_worker, thread=True)

    def run_llm_test(self):
        self.app.notify("Testing LLM... this may take a moment.")
        self.process_prompt("Test: Say 'ok'")

    def process_prompt(self, prompt: str, lang: str | None = None, prob: float | None = None):
        self.post_message(StatusUpdate("THINKING..."))
        is_test = prompt.startswith("Test:")
        response = self.assistant.process_prompt(prompt, lang, prob)
        self.post_message(AssistantResponse(response, "" if is_test else prompt))
        if not self.assistant.is_running: self.app.call_from_thread(self.app.exit)
        elif not is_test: self.run_worker(lambda: self.speak_and_reset_status(response), thread=True)

    def speak_and_reset_status(self, text: str):
        error = speak_text(text)
        if error:
            self.app.call_from_thread(
                self.app.notify,
                f"Could not speak response: {error}",
                title="TTS Error",
                severity="error",
                timeout=10,
            )
        if self.input_mode == "voice": self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True)
        else: self.post_message(StatusUpdate("TYPING..."))
    
    def action_toggle_input_mode(self):
        text_input = self.query_one("#text-input", Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.display = True
            text_input.focus()
            self.app.workers.cancel_group(self, "audio_input")
            self.post_message(StatusUpdate("TYPING..."))
        else:
            self.input_mode = "voice"
            text_input.display = False
            self.app.set_focus(None)
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True)
    
    def listen_for_wake_word(self):
        self.post_message(StatusUpdate("LISTENING..."))
        wake_word = settings_manager.get("wake_word")
        while self.input_mode == "voice" and self.assistant.is_running:
            text, lang, prob = listen_for_audio()
            if text and wake_word.lower() in text.lower():
                # Use a case-insensitive regex to remove the wake word and leading punctuation/space
                prompt = re.sub(rf'^\s*{re.escape(wake_word)}[\s,.]*', '', text, flags=re.IGNORECASE).strip()
                
                self.post_message(StatusUpdate("PROCESSING..."))
                if prompt: 
                    self.run_worker(lambda: self.process_prompt(prompt, lang, prob), thread=True, exclusive=True)
                else: 
                    self.run_worker(lambda: self.speak_and_reset_status("Yes?"), thread=True)
                return

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        prompt = message.value.strip()
        if prompt and self.input_mode == "text":
            self.query_one("#text-input", Input).value = ""
            self.run_worker(lambda: self.process_prompt(prompt), thread=True, exclusive=True)

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        list_view = self.query_one("#conversation", ListView)
        if message.user_prompt:
            list_view.append(ConversationListItem(message.user_prompt, "user"))
        list_view.append(ConversationListItem(message.text, "assistant"))
        list_view.scroll_end()
        # Reset status only after a real response, not tests
        if message.user_prompt:
             self.post_message(StatusUpdate("LISTENING..."))

    async def on_status_update(self, message: StatusUpdate) -> None:
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
    def __init__(self, model_type: Literal["llm", "tts"]):
        super().__init__()
        self.model_type = model_type


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
}

#main-container {
    layout: vertical;
    height: 100%;
    width: 100%;
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

/* --- Conversation View --- */
#conversation-container {
    height: 1fr;
    padding: 1;
    background: $background;
    border: none;
}

ConversationListItem {
    height: auto;
    padding: 0 1 1 1;
}

#text-input {
    dock: bottom;
    height: 3;
    border-top: tall $accent;
    background: $surface;
}

/* --- Settings Panel (Slide-in) --- */
#settings-panel {
    layer: top;
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

TabbedContent {
    height: 1fr;
}

TabPane > ScrollableContainer {
    padding: 0 1;
}

#settings-close-button {
    width: 100%;
    margin: 1;
    background: $accent;
    border: none;
}
#settings-close-button:hover {
    background: $accent-light;
}

/* --- Widgets inside Settings --- */
.settings-group {
    border: round $surface;
    padding: 1;
    margin-bottom: 1;
    height: auto;
}
.settings-group > Label {
    margin-bottom: 1;
    text-style: bold;
}
.settings-group > Input {
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

.model-buttons, .diag-buttons {
    layout: horizontal;
    height: 3;
    margin-top: 1;
    grid-size: 3;
    grid-gutter: 1;
}

.model-buttons Button, .diag-buttons Button {
    width: 1fr;
}
.model-buttons Button:disabled {
    background: $surface;
    color: $text-muted;
    border: tall $secondary;
}

.input_bar {
    layout: horizontal;
    height: auto;
    align: center middle;
}
.input_bar Input {
    width: 1fr;
}
.input_bar Button {
    width: auto;
    height: 3;
    margin-left: 1;
    border: none;
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
from pathlib import Path

from textual.app import App
from textual.widgets import Button

from corvus_app.assistant import Assistant
# Import the unified MainScreen
from corvus_app.ui.screens.main_screen import MainScreen
from corvus_app.ui.shared import AssistantResponse, ModelDownloaded, StatusUpdate
from corvus_app.ui.themes import apply_theme, DARK_THEME, LIGHT_THEME
from corvus_app.audio.sound_player import sound_player, APP_START_SOUND, BUTTON_PRESS_SOUND, NOTIFICATION_SOUND

logger = logging.getLogger(__name__)

class CorvusTUI(App):
    """The main Textual application for Corvus."""
    TITLE = "Corvus AI Assistant"
    CSS_PATH = Path(__file__).parent / "tui.css"
    BINDINGS = [
        ("ctrl+c", "request_quit", "Quit"),
        ("ctrl+s", "toggle_settings", "Settings"),
        ("ctrl+t", "toggle_theme", "Theme"),
    ]

    def __init__(self):
        super().__init__()
        self.assistant = Assistant()
        self.current_theme = DARK_THEME

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        apply_theme(self, self.current_theme)
        sound_player.play(APP_START_SOUND)
        self.push_screen(MainScreen(assistant=self.assistant))

    def action_toggle_settings(self) -> None:
        """Toggles the settings panel on the main screen."""
        if isinstance(self.screen, MainScreen):
            self.screen.action_toggle_settings_panel()
            
    def action_toggle_theme(self) -> None:
        """Switches between light and dark themes."""
        if self.current_theme.name == "dark":
            self.current_theme = LIGHT_THEME
        else:
            self.current_theme = DARK_THEME
        apply_theme(self, self.current_theme)

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
        # Events bubble up automatically, no need to forward them.

    # --- Relay app-wide messages to the main screen for handling ---

    async def on_assistant_response(self, message: AssistantResponse) -> None:
        if isinstance(self.screen, MainScreen):
            await self.screen.on_assistant_response(message)
        sound_player.play(NOTIFICATION_SOUND)

    async def on_status_update(self, message: StatusUpdate) -> None:
        if isinstance(self.screen, MainScreen):
            await self.screen.on_status_update(message)

    async def on_model_downloaded(self, message: ModelDownloaded) -> None:
        if isinstance(self.screen, MainScreen):
            await self.screen.on_model_downloaded(message)
```

### File: `/debug.css`
```css
/* debug.css */
Screen {
    layout: vertical;
    background: $surface;
}

#log-view {
    height: 100%;
    width: 100%;
}
```

### File: `/debug.py`
```py
# debug.py
import time
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, RichLog

LOG_FILE = Path(__file__).parent / "corvus_app.log"
POLL_INTERVAL_S = 0.25

class LogViewer(App):
    """A simple live log file viewer using Textual."""

    TITLE = "Corvus Live Log Viewer"
    CSS_PATH = Path(__file__).parent / "debug.css"
    BINDINGS = [("ctrl+c", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog(id="log-view", wrap=True, highlight=True, auto_scroll=True)

    def on_mount(self) -> None:
        """Start tailing the log file when the app starts."""
        self.log_widget = self.query_one(RichLog)
        self.run_worker(self.tail_log_file, thread=True)

    def tail_log_file(self) -> None:
        """Worker to continuously read and display new log lines."""
        self.log_widget.write("[bold green]Tailing log file...[/]")
        
        # Wait for the log file to be created if it doesn't exist
        while not LOG_FILE.exists():
            time.sleep(POLL_INTERVAL_S)

        try:
            with open(LOG_FILE, "r", encoding="utf-8") as file:
                # Go to the end of the file
                file.seek(0, 2)
                while True:
                    line = file.readline()
                    if not line:
                        time.sleep(POLL_INTERVAL_S)
                        continue
                    self.log_widget.write(line.strip())
        except Exception as e:
            self.log_widget.write(f"[bold red]Error reading log file: {e}[/]")

if __name__ == "__main__":
    app = LogViewer()
    app.run()
```

### File: `/installer.log`
```log
2025-08-06 18:14:33,049 [INFO    ]  Valid virtual environment found.
2025-08-06 18:14:33,051 [INFO    ]  Installing dependencies (this may take several minutes)...
2025-08-06 18:14:33,054 [INFO    ]  Running command: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt
2025-08-06 18:14:39,647 [INFO    ]  Requirement already satisfied: llama-cpp-python in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (0.3.14)
2025-08-06 18:14:39,648 [INFO    ]  Requirement already satisfied: SpeechRecognition in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 2)) (3.14.3)
2025-08-06 18:14:39,652 [INFO    ]  Requirement already satisfied: PyAudio in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 3)) (0.2.14)
2025-08-06 18:14:39,653 [INFO    ]  Requirement already satisfied: rich in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 4)) (14.1.0)
2025-08-06 18:14:39,654 [INFO    ]  Requirement already satisfied: python-dotenv in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (1.1.1)
2025-08-06 18:14:39,655 [INFO    ]  Requirement already satisfied: textual==0.58.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (0.58.0)
2025-08-06 18:14:39,656 [INFO    ]  Requirement already satisfied: requests in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2.32.4)
2025-08-06 18:14:39,657 [INFO    ]  Requirement already satisfied: beautifulsoup4 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (4.13.4)
2025-08-06 18:14:39,657 [INFO    ]  Requirement already satisfied: sounddevice in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9)) (0.5.2)
2025-08-06 18:14:39,658 [INFO    ]  Requirement already satisfied: soundfile in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (0.13.1)
2025-08-06 18:14:39,659 [INFO    ]  Requirement already satisfied: faster-whisper in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (1.2.0)
2025-08-06 18:14:39,659 [INFO    ]  Collecting piper-tts (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 12))
2025-08-06 18:14:39,660 [INFO    ]    Downloading piper_tts-1.3.0-cp39-abi3-win_amd64.whl.metadata (4.5 kB)
2025-08-06 18:14:39,661 [INFO    ]  Requirement already satisfied: markdown-it-py>=2.1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (3.0.0)
2025-08-06 18:14:39,662 [INFO    ]  Requirement already satisfied: typing-extensions<5.0.0,>=4.4.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (4.14.1)
2025-08-06 18:14:39,663 [INFO    ]  Requirement already satisfied: numpy>=1.20.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (1.26.4)
2025-08-06 18:14:39,668 [INFO    ]  Requirement already satisfied: diskcache>=5.6.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (5.6.3)
2025-08-06 18:14:39,669 [INFO    ]  Requirement already satisfied: jinja2>=2.11.3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (3.1.6)
2025-08-06 18:14:39,670 [INFO    ]  Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 4)) (2.19.2)
2025-08-06 18:14:39,671 [INFO    ]  Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (3.4.2)
2025-08-06 18:14:39,672 [INFO    ]  Requirement already satisfied: idna<4,>=2.5 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (3.10)
2025-08-06 18:14:39,672 [INFO    ]  Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2.5.0)
2025-08-06 18:14:39,673 [INFO    ]  Requirement already satisfied: certifi>=2017.4.17 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2025.8.3)
2025-08-06 18:14:39,674 [INFO    ]  Requirement already satisfied: soupsieve>1.2 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from beautifulsoup4->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (2.7)
2025-08-06 18:14:39,675 [INFO    ]  Requirement already satisfied: CFFI>=1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from sounddevice->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9)) (1.17.1)
2025-08-06 18:14:39,675 [INFO    ]  Requirement already satisfied: ctranslate2<5,>=4.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (4.6.0)
2025-08-06 18:14:39,676 [INFO    ]  Requirement already satisfied: huggingface-hub>=0.13 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.34.3)
2025-08-06 18:14:39,677 [INFO    ]  Requirement already satisfied: tokenizers<1,>=0.13 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.21.4)
2025-08-06 18:14:39,678 [INFO    ]  Requirement already satisfied: onnxruntime<2,>=1.14 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (1.22.1)
2025-08-06 18:14:39,678 [INFO    ]  Requirement already satisfied: av>=11 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (15.0.0)
2025-08-06 18:14:39,679 [INFO    ]  Requirement already satisfied: tqdm in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (4.67.1)
2025-08-06 18:14:39,683 [INFO    ]  Requirement already satisfied: pycparser in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from CFFI>=1.0->sounddevice->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9)) (2.22)
2025-08-06 18:14:39,684 [INFO    ]  Requirement already satisfied: setuptools in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from ctranslate2<5,>=4.0->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (65.5.0)
2025-08-06 18:14:39,684 [INFO    ]  Requirement already satisfied: pyyaml<7,>=5.3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from ctranslate2<5,>=4.0->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (6.0.2)
2025-08-06 18:14:39,686 [INFO    ]  Requirement already satisfied: filelock in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub>=0.13->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (3.18.0)
2025-08-06 18:14:39,687 [INFO    ]  Requirement already satisfied: fsspec>=2023.5.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub>=0.13->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (2025.7.0)
2025-08-06 18:14:39,688 [INFO    ]  Requirement already satisfied: packaging>=20.9 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub>=0.13->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (25.0)
2025-08-06 18:14:39,688 [INFO    ]  Requirement already satisfied: MarkupSafe>=2.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from jinja2>=2.11.3->llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (3.0.2)
2025-08-06 18:14:39,690 [INFO    ]  Requirement already satisfied: mdurl~=0.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from markdown-it-py>=2.1.0->markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (0.1.2)
2025-08-06 18:14:39,690 [INFO    ]  Requirement already satisfied: linkify-it-py<3,>=1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (2.0.3)
2025-08-06 18:14:39,691 [INFO    ]  Requirement already satisfied: mdit-py-plugins in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (0.4.2)
2025-08-06 18:14:39,692 [INFO    ]  Requirement already satisfied: coloredlogs in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (15.0.1)
2025-08-06 18:14:39,693 [INFO    ]  Requirement already satisfied: flatbuffers in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (25.2.10)
2025-08-06 18:14:39,693 [INFO    ]  Requirement already satisfied: protobuf in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (6.31.1)
2025-08-06 18:14:39,694 [INFO    ]  Requirement already satisfied: sympy in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (1.14.0)
2025-08-06 18:14:39,695 [INFO    ]  Requirement already satisfied: colorama in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from tqdm->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.4.6)
2025-08-06 18:14:39,696 [INFO    ]  Requirement already satisfied: uc-micro-py in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from linkify-it-py<3,>=1->markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (1.0.3)
2025-08-06 18:14:39,701 [INFO    ]  Requirement already satisfied: humanfriendly>=9.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from coloredlogs->onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (10.0)
2025-08-06 18:14:39,702 [INFO    ]  Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from sympy->onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (1.3.0)
2025-08-06 18:14:39,703 [INFO    ]  Requirement already satisfied: pyreadline3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from humanfriendly>=9.1->coloredlogs->onnxruntime<2,>=1.14->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (3.5.4)
2025-08-06 18:14:39,703 [INFO    ]  Downloading piper_tts-1.3.0-cp39-abi3-win_amd64.whl (13.8 MB)
2025-08-06 18:14:39,704 [INFO    ]     ---------------------------------------- 13.8/13.8 MB 4.5 MB/s eta 0:00:00
2025-08-06 18:14:39,704 [INFO    ]  Installing collected packages: piper-tts
2025-08-06 18:14:39,705 [INFO    ]  Successfully installed piper-tts-1.3.0
2025-08-06 18:14:39,706 [INFO    ]  Dependencies installed successfully!
2025-08-06 18:14:39,707 [INFO    ]  Wrote requirements hash 'fff8854b3e7be85531746ca83ca9ce85' to marker file.
2025-08-06 18:14:39,708 [INFO    ]  Setting up configuration...
2025-08-06 18:14:39,709 [INFO    ]  .env file already exists, skipping creation.
2025-08-06 18:14:39,710 [INFO    ]  Setup complete. The main application will now launch.

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

# --- Add sound player import
from corvus_app.audio.sound_player import (
    sound_player, INSTALL_START_SOUND, INSTALL_STEP_SOUND, 
    INSTALL_SUCCESS_SOUND, INSTALL_FAIL_SOUND
)

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
    """Configures logging for the installer, clearing the log on startup."""
    log_path = PROJECT_ROOT / "installer.log"
    # Clear the log file at the start of the session
    if log_path.exists():
        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.truncate(0)
        except Exception as e:
            print(f"Warning: Could not clear installer log file: {e}")

    log_formatter = logging.Formatter("%(asctime)s [%(levelname)-8.8s]  %(message)s")
    log_file_handler = RotatingFileHandler(log_path, maxBytes=2*1024*1024, backupCount=1, encoding="utf-8")
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
        """Updates the status line and optionally plays a sound."""
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
            time.sleep(1) # Give the sound time to play
            self.call_from_thread(self.app.exit, True)
        except Exception as e:
            self.update_status(f"[bold red]Installation failed: {e}[/]", play_sound=False)
            sound_player.play(INSTALL_FAIL_SOUND)
            logger.error("FATAL ERROR in installation orchestrator:", exc_info=True)
            self.call_from_thread(lambda: setattr(self.query_one(Footer).styles, 'background', 'red'))
            # Keep window open to show the error

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

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')

        self.run_worker(
            lambda: self.simulate_progress(process),
            thread=True,
            group="simulation",
            name=f"pip_install_progress_{process.pid}"
        )

        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            for line in (stdout).splitlines():
                if line.strip(): logger.info(line)
            self.call_from_thread(progress_bar.update, progress=100)
            self.update_status("Dependencies installed successfully!")
            
            # Write hash of requirements.txt to marker file
            with open(req_path, 'rb') as f:
                req_hash = hashlib.md5(f.read()).hexdigest()
            with open(MARKER_FILE, 'w', encoding='utf-8') as f:
                f.write(req_hash)
            logger.info(f"Wrote requirements hash '{req_hash}' to marker file.")

        else:
            for line in (stdout + stderr).splitlines():
                if line.strip(): logger.error(line)
            raise RuntimeError("Dependency installation failed.")

    def simulate_progress(self, process: subprocess.Popen):
        """Worker that simulates a steady progress increase."""
        progress_bar = self.query_one(ProgressBar)
        estimated_duration = 420
        start_time = time.time()
        while process.poll() is None:
            elapsed = time.time() - start_time
            progress = min(98, (elapsed / estimated_duration) * 100)
            self.call_from_thread(progress_bar.update, total=100, progress=progress)
            time.sleep(1)

    def create_env_file(self):
        self.update_status("Setting up configuration...")
        env_file = PROJECT_ROOT / ".env"
        if not env_file.exists():
            shutil.copy(PROJECT_ROOT / ".env.example", env_file)
            self.update_status(".env file created successfully from example.")
        else:
            self.update_status(".env file already exists, skipping creation.")
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
    """
    Returns a list of locally installed GGUF models.
    This search is case-insensitive and only includes files.
    """
    if not LLM_MODELS_PATH.exists():
        return []
    
    # Perform a case-insensitive search for files ending with .gguf
    return sorted([
        f for f in LLM_MODELS_PATH.glob("*") 
        if f.is_file() and f.suffix.lower() == ".gguf"
    ])

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
llama-cpp-python
SpeechRecognition
PyAudio
rich
python-dotenv
textual==0.58.0
requests
beautifulsoup4
sounddevice
soundfile
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
from importlib import import_module
from importlib.metadata import version, PackageNotFoundError
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
# Ensure 'corvus_app' can be imported by adding the project root to the Python path.
sys.path.insert(0, str(PROJECT_ROOT))

# Now that the path is set, we can import the crash handler.
from corvus_app.crash_handler import format_crash_report

# --- Configuration ---
TEXTUAL_VERSION = "0.58.0"
VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"

if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"

def check_textual_for_installer():
    """
    Ensures the correct version of Textual is available for the installer UI.
    This is run with the system python, not the venv python.
    """
    try:
        if version("textual") == TEXTUAL_VERSION:
            return True
        print(f"[BOOTSTRAP] Found Textual {version('textual')}, but installer requires {TEXTUAL_VERSION}. Re-installing...")
    except PackageNotFoundError:
        print(f"[BOOTSTRAP] Textual not found. Installing for installer UI...")
    
    try:
        # Use --user to avoid permission errors if global python is in a protected location
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"textual=={TEXTUAL_VERSION}", "--user"])
        print("[BOOTSTRAP] Textual prepared successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[FATAL] Could not install Textual. Pip may be broken. Error: {e}")
        return False

def is_venv_ok():
    """Checks if venv exists and if requirements are up-to-date via a hash check."""
    if not (VENV_PYTHON.exists() and MARKER_FILE.exists()):
        return False # Venv or marker is missing, definitely not ok.

    try:
        with open(PROJECT_ROOT / 'requirements.txt', 'rb') as f:
            current_hash = hashlib.md5(f.read()).hexdigest()
        
        with open(MARKER_FILE, 'r', encoding='utf-8') as f:
            installed_hash = f.read().strip()

        if current_hash == installed_hash:
            return True
        else:
            print("[INFO] 'requirements.txt' has changed. Re-installing dependencies.")
            return False
            
    except Exception as e:
        print(f"[INFO] Could not verify dependencies, running installer. Reason: {e}")
        return False

def launch_installer():
    """Runs the installer UI application."""
    print("Launching Installer/Repair UI...")
    if not check_textual_for_installer():
        return False # Abort if we can't even get the installer running.
        
    from installer.installer_tui import InstallerApp
    app = InstallerApp()
    app.run()
    # The installer returns True on success, False on failure/exit.
    # We double-check the marker file as the ultimate source of truth.
    return MARKER_FILE.exists()

def launch_debug_viewer():
    """Launches the debug.py script in a new window if it exists."""
    debug_script = PROJECT_ROOT / "debug.py"
    if debug_script.exists():
        print("[INFO] Found debug.py, launching live log viewer...")
        if sys.platform == "win32":
            # This flag opens the process in a new console window on Windows.
            subprocess.Popen([sys.executable, str(debug_script)], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            # For macOS/Linux, it's harder to do this portably.
            # We'll launch it as a background process and inform the user.
            print("[INFO] On Linux/macOS, run 'python3 debug.py' in a separate terminal for the best experience.")
            subprocess.Popen([sys.executable, str(debug_script)])

def launch_main_app():
    """Launches the main Corvus application."""
    launch_debug_viewer() # Attempt to launch the debugger first
    print("Launching Corvus Application...")
    main_app_module = "corvus_app.main"
    command = [str(VENV_PYTHON), "-m", main_app_module]
    env = os.environ.copy()
    env['PYTHONPATH'] = str(PROJECT_ROOT)

    try:
        # Using Popen and waiting would allow us to capture output, but check_run is simpler
        # if we just want to wait for it to finish.
        subprocess.run(command, env=env, check=True)
    except subprocess.CalledProcessError:
        print("\n[INFO] Corvus application closed. This may have been due to an error. See 'corvus_crash_report.log'.")
    except FileNotFoundError:
        raise RuntimeError(f"Could not find the Python executable in the venv: '{VENV_PYTHON}'. The environment is corrupt.")


def main():
    """Main entry point for the application launcher."""
    try:
        print("Initializing Corvus...")
        if is_venv_ok():
            launch_main_app()
        else:
            print("[INFO] Corrupt or incomplete environment detected. Starting repair process...")
            if launch_installer():
                print("[INFO] Repair complete. Launching application...")
                launch_main_app()
            else:
                print("\n[INFO] Repair/Installation was cancelled or failed. Check 'installer.log'.")
    
    except Exception as e:
        # This is a fallback for any unhandled launcher/bootstrap crash
        tb_info = traceback.format_exc()
        format_crash_report("Launcher", e, tb_info)
        sys.exit(1)


if __name__ == "__main__":
    main()
    if sys.platform != "win32":
        print("\nLauncher has finished.")
```

### File: `/settings.json`
```json
{
    "active_llm_model": "llm_models\\stablelm-zephyr-3b.Q5_K_M.gguf",
    "active_tts_model": null,
    "wake_word": "corvus",
    "system_prompt": "You are a helpful assistant.",
    "input_device_index": null,
    "output_device_index": null,
    "active_stt_model": "medium.en",
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