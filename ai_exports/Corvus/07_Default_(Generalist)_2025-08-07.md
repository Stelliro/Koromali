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
2025-08-07 14:52:24,572 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:52:24,572 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_app.log'. Log Level: INFO
2025-08-07 14:52:24,572 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:52:24,572 [MainThread  ] [__main__                 ] [INFO    ]  Main application process starting.
2025-08-07 14:52:26,709 [MainThread  ] [__main__                 ] [INFO    ]  Daemon process started with PID: 27204
2025-08-07 14:52:27,075 [Dummy-1     ] [corvus_app.ui.worker     ] [INFO    ]  QueueListener worker started.
2025-08-07 14:53:28,279 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:53:28,280 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:53:28,280 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:53:28,281 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:53:28,281 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:53:28,283 [MainThread  ] [models.tts_manager       ] [INFO    ]  Fetching remote TTS voice index from https://huggingface.co/rhasspy/piper-voices/raw/main/voices.json
2025-08-07 14:53:28,704 [MainThread  ] [models.tts_manager       ] [INFO    ]  Successfully fetched and parsed 129 TTS voices.
2025-08-07 15:00:06,418 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:06,422 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:06,423 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:06,424 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:06,424 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:34,341 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:34,342 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:34,342 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:34,343 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:34,344 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:39,767 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:39,769 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:39,769 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:39,770 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:39,771 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:42,207 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:42,223 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:42,223 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:42,224 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:42,224 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:44,188 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:44,189 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:44,189 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:44,191 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:44,191 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:46,530 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:46,530 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:46,531 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:46,531 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:46,532 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:47,810 [MainThread  ] [models.stt_manager       ] [INFO    ]  Deleting STT model directory: stt_models\models--Systran--faster-distil-whisper-small.en
2025-08-07 15:00:47,812 [MainThread  ] [models.stt_manager       ] [INFO    ]  Successfully deleted model: small.en
2025-08-07 15:00:47,813 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:47,814 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:47,815 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:47,815 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:50,308 [MainThread  ] [models.stt_manager       ] [INFO    ]  Deleting STT model directory: stt_models\models--Systran--faster-distil-whisper-medium.en
2025-08-07 15:00:50,313 [MainThread  ] [models.stt_manager       ] [INFO    ]  Successfully deleted model: medium.en
2025-08-07 15:00:50,316 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:50,318 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:50,319 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:51,241 [MainThread  ] [models.stt_manager       ] [INFO    ]  Deleting STT model directory: stt_models\models--Systran--faster-whisper-base
2025-08-07 15:00:51,243 [MainThread  ] [models.stt_manager       ] [INFO    ]  Successfully deleted model: base
2025-08-07 15:00:51,245 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:51,246 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:52,149 [MainThread  ] [models.stt_manager       ] [INFO    ]  Deleting STT model directory: stt_models\models--Systran--faster-whisper-medium.en
2025-08-07 15:00:52,153 [MainThread  ] [models.stt_manager       ] [INFO    ]  Successfully deleted model: medium.en
2025-08-07 15:00:52,155 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:52,156 [MainThread  ] [models.stt_manager       ] [WARNING ]  Could not identify any valid STT model subdirectories.
2025-08-07 15:01:33,686 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:33,687 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:40,589 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:40,590 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:57,010 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:57,011 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'

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
import re
from typing import Optional

from corvus_app.app_settings import settings_manager
from corvus_app.llm.llm_client import LLMClient
from corvus_app.tools.user_profile import user_profile_manager
from corvus_app.tts.tts_engine import TTSEngine
from models.tts_manager import get_local_models_list as get_local_tts_models
from models.stt_manager import get_local_models as get_local_stt_models
from models.llm_manager import get_local_models as get_local_llm_models
from plugins.registry import CommandRegistry

logger = logging.getLogger(__name__)

class Assistant:
    def __init__(self):
        logger.info("Initializing Assistant...")
        self.is_running = True
        self.registry = CommandRegistry()
        # Initialize clients and engines after validation
        self.validate_settings()
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
                    f"Active TTS model '{active_tts}' not found. Resetting to None."
                )
                settings_manager.set("active_tts_model", None)
        
        # --- Validate STT Model ---
        active_stt = settings_manager.get("active_stt_model")
        if active_stt:
            local_stt_models = get_local_stt_models()
            if active_stt not in local_stt_models:
                logger.warning(
                    f"Active STT model '{active_stt}' not found. Resetting to 'base'."
                )
                settings_manager.set("active_stt_model", "base")

        # --- Validate LLM Model ---
        active_llm = settings_manager.get("active_llm_model")
        if active_llm:
            local_llm_models = get_local_llm_models()
            if active_llm not in local_llm_models:
                logger.warning(
                    f"Active LLM model '{active_llm}' not found. Resetting to None."
                )
                settings_manager.set("active_llm_model", None)


    def reload(self):
        """Reloads components like the LLM and TTS models."""
        logger.info("Reloading Assistant components...")
        self.validate_settings()
        self.llm_client.reload_model()
        self.tts_engine.reload_model()

    def _parse_and_update_profile(self, llm_response: str) -> str:
        """Checks for profile update tags, updates profile, and returns clean response."""
        update_match = re.search(
            r"`\[UPDATE_PROFILE\]`(.+?)`\[/UPDATE_PROFILE\]`",
            llm_response,
            re.DOTALL | re.IGNORECASE
        )
        
        if update_match:
            new_profile_content = update_match.group(1).strip()
            spoken_response = llm_response.split("`[/UPDATE_PROFILE]`", 1)[-1].strip()
            
            logger.info("LLM requested a profile update.")
            user_profile_manager.write(new_profile_content)
            
            # Return just the part to be spoken
            return spoken_response
        else:
            # No update tag found, return original response
            return llm_response

    def process_prompt(self, prompt: str, lang: Optional[str] = None, prob: Optional[float] = None) -> str:
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
        raw_response = self.llm_client.get_response(prompt, lang, prob)
        
        # Check response for profile update instructions
        final_response = self._parse_and_update_profile(raw_response)
        
        return final_response
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
from typing import Optional
from faster_whisper import WhisperModel

from corvus_app.app_settings import settings_manager
from models.stt_manager import STT_MODELS_PATH

logger = logging.getLogger(__name__)

class STTEngine:
    _instance = None
    _current_model_name: Optional[str] = None
    _model: Optional[WhisperModel] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(STTEngine, cls).__new__(cls)
            cls._instance.reload_model()
        return cls._instance

    def reload_model(self, model_name_override: Optional[str] = None):
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
from typing import Optional, Dict, Any

REPORT_FILE = "corvus_crash_report.log"

def format_crash_report(
    app_part: str,
    exception: Exception,
    traceback_info: str,
    context: Optional[Dict[str, Any]] = None,
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
from pathlib import Path
from typing import Optional

from corvus_app.app_settings import settings_manager
from corvus_app.tools.user_profile import user_profile_manager
from models.llm_manager import LLM_MODELS_PATH

logger = logging.getLogger(__name__)

# Lazy import llama_cpp
try:
    from llama_cpp import Llama
    LLAMA_CPP_AVAILABLE = True
except ImportError:
    LLAMA_CPP_AVAILABLE = False
    logger.warning("llama-cpp-python not found. LLM functionality will be disabled.")
    logger.warning("Install it with: pip install llama-cpp-python")

class LLMClient:
    _instance = None
    _model_name: Optional[str] = None
    _llm: Optional["Llama"] = None
    _last_error: Optional[str] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMClient, cls).__new__(cls)
            if LLAMA_CPP_AVAILABLE:
                cls._instance.reload_model()
        return cls._instance

    def reload_model(self):
        if not LLAMA_CPP_AVAILABLE:
            self._last_error = "llama-cpp-python is not installed."
            return

        model_filename = settings_manager.get("active_llm_model")
        
        if not model_filename:
            self._llm = None
            self._model_name = None
            self._last_error = "No active LLM model selected."
            logger.warning(self._last_error)
            return
        
        if self._llm and self._model_name == model_filename:
            logger.debug("LLM model is already up-to-date.")
            return
        
        model_path = LLM_MODELS_PATH / model_filename
        if not model_path.exists():
            self._llm = None
            self._model_name = None
            self._last_error = f"LLM model file not found: {model_path}"
            logger.error(self._last_error)
            return

        logger.info(f"Attempting to load LLM model: '{model_filename}'")
        try:
            self._llm = Llama(
                model_path=str(model_path),
                n_ctx=4096,      # Context window
                n_gpu_layers=-1, # Offload all possible layers to GPU
                verbose=False    # Keep llama.cpp quiet
            )
            self._model_name = model_filename
            self._last_error = None
            logger.info(f"LLM model '{model_filename}' loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load LLM model '{model_filename}': {e}", exc_info=True)
            self._llm = None
            self._model_name = None
            self._last_error = str(e)


    def get_response(self, prompt: str, lang: Optional[str] = None, prob: Optional[float] = None) -> str:
        if not self._llm:
            logger.warning(f"LLM not loaded. Cannot process prompt: '{prompt}'")
            return self._last_error or "My language model is not available. Please select one in settings."

        system_prompt = settings_manager.get("system_prompt")
        user_profile = user_profile_manager.read()
        
        lang_info = ""
        if lang and prob:
            lang_info = f"\n(User is speaking {lang} with {prob:.2f} confidence)"

        full_prompt = f"""
{system_prompt}

Current User Profile:
---
{user_profile}
---

USER'S PROMPT:{lang_info}
{prompt}

ASSISTANT'S RESPONSE:
"""
        try:
            logger.info("Generating LLM response...")
            output = self._llm(
                full_prompt,
                max_tokens=512,
                stop=["USER'S PROMPT:", "\n\n", "user:"],
                echo=False
            )
            response_text = output['choices'][0]['text'].strip()
            logger.info(f"LLM generated response: '{response_text[:100]}...'")
            return response_text
        except Exception as e:
            logger.error(f"Error during LLM generation: {e}", exc_info=True)
            return "I'm sorry, I encountered an error while trying to think of a response."
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
from typing import Optional
from piper.voice import PiperVoice

from corvus_app.app_settings import settings_manager
from corvus_app.audio.sound_player import sound_player
from models.tts_manager import TTS_MODELS_PATH

logger = logging.getLogger(__name__)

class TTSEngine:
    _instance = None
    _current_model_name: Optional[str] = None
    _voice: Optional[PiperVoice] = None
    _last_error: Optional[str] = None

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

    def speak(self, text: str) -> Optional[str]:
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

def speak_text(text: str) -> Optional[str]:
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
import webbrowser
from typing import Literal, Optional
from multiprocessing import Queue, Process

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit,
    QPushButton, QStatusBar, QDockWidget, QTabWidget, QFormLayout,
    QComboBox, QMessageBox, QListWidgetItem, QLabel, QTextEdit, QScrollArea,
    QProgressDialog
)
from PyQt6.QtCore import Qt, QThreadPool

import qtawesome as qta

from corvus_app.app_settings import settings_manager
from corvus_app.audio import device_manager
from corvus_app.tools import cleaner
from corvus_app.ui.worker import QueueListener, MicTestWorker
from corvus_app.audio.sound_player import sound_player, BUTTON_PRESS_SOUND
from models import stt_manager, tts_manager, llm_manager

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self, ui_to_daemon_queue: Queue, daemon_to_ui_queue: Queue, daemon_process: Process):
        super().__init__()
        self.ui_to_daemon_queue = ui_to_daemon_queue
        self.daemon_to_ui_queue = daemon_to_ui_queue
        self.daemon_process = daemon_process

        self.thread_pool = QThreadPool()
        self.input_mode = "voice" # or "text"
        self.progress_dialog: Optional[QProgressDialog] = None

        self.setWindowTitle("Corvus AI Assistant")
        self.setWindowIcon(qta.icon("fa5s.feather-alt"))
        self.setGeometry(100, 100, 900, 700)
        
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; }
            QWidget { background-color: #1e1e1e; color: #d4d4d4; }
            QListWidget, QComboBox, QTextEdit { border: 1px solid #333; background-color: #252526; }
            QLineEdit { border: 1px solid #333; background-color: #3c3c3c; padding: 5px; }
            QPushButton { border: 1px solid #333; background-color: #3c3c3c; padding: 5px; }
            QPushButton:hover { background-color: #555; }
            QStatusBar { color: #cccccc; }
            QDockWidget { titlebar-close-icon: url(none); }
            QDockWidget::title { text-align: center; background: #252526; padding: 5px; }
            QTabWidget::pane { border: 1px solid #333; }
            QTabBar::tab { background: #252526; padding: 8px; min-width: 80px;}
            QTabBar::tab:selected { background: #3c3c3c; }
            QComboBox::drop-down { border: none; }
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
        
        self.clear_button = QPushButton("Clear Memory")
        self.clear_button.setIcon(qta.icon("fa5s.broom"))
        self.clear_button.clicked.connect(self.on_clear_conversation)
        
        self.settings_button = QPushButton("Settings")
        self.settings_button.setIcon(qta.icon("fa5s.cog"))
        self.settings_button.clicked.connect(self.toggle_settings)

        header_layout.addWidget(self.clear_button)
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
        
        # --- TTS ---
        layout.addWidget(QLabel("Voice Models (TTS)"))
        self.tts_model_list = QComboBox()
        tts_buttons = QHBoxLayout()
        self.tts_preview_button = QPushButton("Preview"); self.tts_preview_button.clicked.connect(lambda: self.preview_model("tts"))
        self.tts_set_active_button = QPushButton("Set Active"); self.tts_set_active_button.clicked.connect(lambda: self.set_active_model("tts"))
        self.tts_delete_button = QPushButton("Delete"); self.tts_delete_button.clicked.connect(lambda: self.delete_model("tts"))
        tts_buttons.addWidget(self.tts_preview_button); tts_buttons.addWidget(self.tts_set_active_button); tts_buttons.addWidget(self.tts_delete_button)
        layout.addWidget(self.tts_model_list); layout.addLayout(tts_buttons)
        self.tts_visit_button = QPushButton("Visit Model Page"); self.tts_visit_button.clicked.connect(lambda: self.visit_model_page("tts"))
        layout.addWidget(self.tts_visit_button)
        layout.addWidget(QLabel("Download New Voice:"))
        self.tts_download_list = QComboBox(); layout.addWidget(self.tts_download_list)
        self.tts_download_button = QPushButton("Download Selected"); self.tts_download_button.clicked.connect(lambda: self.download_model("tts")); layout.addWidget(self.tts_download_button)

        # --- STT ---
        layout.addWidget(QLabel("Speech-to-Text Models (STT)"))
        self.stt_model_list = QComboBox()
        stt_buttons = QHBoxLayout()
        self.stt_set_active_button = QPushButton("Set Active"); self.stt_set_active_button.clicked.connect(lambda: self.set_active_model("stt"))
        self.stt_delete_button = QPushButton("Delete"); self.stt_delete_button.clicked.connect(lambda: self.delete_model("stt"))
        stt_buttons.addWidget(self.stt_set_active_button); stt_buttons.addWidget(self.stt_delete_button)
        layout.addWidget(self.stt_model_list); layout.addLayout(stt_buttons)
        layout.addWidget(QLabel("Download New STT Model:"))
        self.stt_download_list = QComboBox(); layout.addWidget(self.stt_download_list)
        self.stt_download_button = QPushButton("Download Selected"); self.stt_download_button.clicked.connect(lambda: self.download_model("stt")); layout.addWidget(self.stt_download_button)

        # --- LLM ---
        layout.addWidget(QLabel("Language Models (LLM)"))
        self.llm_model_list = QComboBox()
        llm_buttons = QHBoxLayout()
        self.llm_set_active_button = QPushButton("Set Active"); self.llm_set_active_button.clicked.connect(lambda: self.set_active_model("llm"))
        self.llm_delete_button = QPushButton("Delete"); self.llm_delete_button.clicked.connect(lambda: self.delete_model("llm"))
        llm_buttons.addWidget(self.llm_set_active_button); llm_buttons.addWidget(self.llm_delete_button)
        layout.addWidget(self.llm_model_list); layout.addLayout(llm_buttons)
        self.llm_visit_button = QPushButton("Visit Model Page"); self.llm_visit_button.clicked.connect(lambda: self.visit_model_page("llm"))
        layout.addWidget(self.llm_visit_button)
        layout.addWidget(QLabel("Download New LLM:"))
        self.llm_download_list = QListWidget(); layout.addWidget(self.llm_download_list)
        self.llm_download_button = QPushButton("Download Selected"); self.llm_download_button.clicked.connect(lambda: self.download_model("llm")); layout.addWidget(self.llm_download_button)

    def setup_personality_tab(self):
        scroll, layout = self.create_scrollable_tab(QVBoxLayout)
        self.settings_tabs.addTab(scroll, "Personality")
        layout.addWidget(QLabel("System Prompt (Assistant's Personality):"))
        self.system_prompt_input = QTextEdit()
        self.system_prompt_input.setAcceptRichText(False)
        layout.addWidget(self.system_prompt_input)
        save_button = QPushButton("Save Personality"); save_button.clicked.connect(self.save_personality)
        layout.addWidget(save_button)

    def setup_system_tab(self):
        scroll, layout = self.create_scrollable_tab(QFormLayout)
        self.settings_tabs.addTab(scroll, "System")
        
        self.wake_word_input = QLineEdit(); layout.addRow("Wake Word:", self.wake_word_input)
        self.stt_pause_input = QLineEdit(); layout.addRow("Pause Threshold (s):", self.stt_pause_input)
        save_stt_button = QPushButton("Save System Settings"); save_stt_button.clicked.connect(self.save_system_settings)
        layout.addRow(save_stt_button)

        self.input_device_list = QComboBox(); self.output_device_list = QComboBox()
        layout.addRow("Input Device:", self.input_device_list)
        layout.addRow("Output Device:", self.output_device_list)
        self.input_device_list.currentIndexChanged.connect(lambda i: self.set_audio_device("input", self.input_device_list.itemData(i)))
        self.output_device_list.currentIndexChanged.connect(lambda i: self.set_audio_device("output", self.output_device_list.itemData(i)))

        self.mic_test_status = QLabel("Mic Test: Status will appear here.")
        test_mic_button = QPushButton("Test Mic"); test_mic_button.clicked.connect(self.test_mic)
        layout.addRow(test_mic_button, self.mic_test_status)

        clean_models = QPushButton("Clean All Models"); clean_models.clicked.connect(lambda: self.run_cleaner("models", cleaner.clean_models))
        clean_logs = QPushButton("Clean Logs & Settings"); clean_logs.clicked.connect(lambda: self.run_cleaner("logs", cleaner.clean_logs_settings))
        clean_cache = QPushButton("Clean Python Cache"); clean_cache.clicked.connect(lambda: self.run_cleaner("cache", cleaner.clean_pycache))
        layout.addRow(clean_models); layout.addRow(clean_logs); layout.addRow(clean_cache)

    # --- UI Logic ---
    def toggle_settings(self):
        if self.settings_dock.isVisible():
            self.settings_dock.hide()
        else:
            self.populate_settings()
            self.settings_dock.show()
    
    def on_clear_conversation(self):
        sound_player.play(BUTTON_PRESS_SOUND)
        self.conversation_view.clear()
        
    def populate_settings(self):
        # Models
        self.populate_local_models("tts", self.tts_model_list, tts_manager.get_local_models_list())
        self.populate_local_models("stt", self.stt_model_list, stt_manager.get_local_models())
        self.populate_local_models("llm", self.llm_model_list, llm_manager.get_local_models())
        self.populate_remote_tts_list()
        self.populate_remote_stt_list()
        self.populate_remote_llm_list()
        # Personality
        self.system_prompt_input.setText(settings_manager.get("system_prompt"))
        # System
        self.wake_word_input.setText(settings_manager.get("wake_word"))
        self.stt_pause_input.setText(str(settings_manager.get("stt_pause_threshold")))
        self.populate_audio_devices()

    def populate_local_models(self, mtype: str, combo: QComboBox, local_models):
        combo.clear()
        active_model = settings_manager.get(f"active_{mtype}_model")
        
        models_dict = local_models if isinstance(local_models, dict) else {m: m for m in local_models}

        if not models_dict:
            combo.addItem("No local models found", None)
            combo.setEnabled(False)
            return
        
        combo.setEnabled(True)
        for model_id, name in models_dict.items():
            combo.addItem(name, model_id)
            if model_id == active_model:
                combo.setCurrentText(name)

    def populate_remote_tts_list(self):
        self.tts_download_list.clear()
        models = tts_manager.get_remote_models_list()
        for model_id, name in models.items():
            if "error" not in model_id.lower():
                self.tts_download_list.addItem(name, model_id)

    def populate_remote_stt_list(self):
        self.stt_download_list.clear()
        for model_name in stt_manager.AVAILABLE_MODELS:
            self.stt_download_list.addItem(model_name, model_name)
    
    def populate_remote_llm_list(self):
        self.llm_download_list.clear()
        models = llm_manager.get_remote_models_list()
        for key, info in models.items():
            self.llm_download_list.addItem(f"{key} ({info['notes']})")
            self.llm_download_list.item(self.llm_download_list.count() - 1).setData(Qt.ItemDataRole.UserRole, key)

    def populate_audio_devices(self):
        self.input_device_list.clear(); self.output_device_list.clear()
        in_devs, out_devs = device_manager.get_audio_devices()
        self.input_device_list.addItem("System Default", None)
        self.output_device_list.addItem("System Default", None)
        for dev in in_devs: self.input_device_list.addItem(dev['name'], dev['index'])
        for dev in out_devs: self.output_device_list.addItem(dev['name'], dev['index'])

    # --- Action Handlers ---
    def save_personality(self):
        settings_manager.set("system_prompt", self.system_prompt_input.toPlainText())
        self.status_bar.showMessage("Personality saved.", 3000)
        self.ui_to_daemon_queue.put({"type": "reload_models"})

    def save_system_settings(self):
        settings_manager.set("wake_word", self.wake_word_input.text())
        try:
            settings_manager.set("stt_pause_threshold", float(self.stt_pause_input.text()))
            self.status_bar.showMessage("System settings saved.", 3000)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Pause threshold must be a number.")
    
    def set_audio_device(self, dev_type: Literal["input", "output"], index: Optional[int]):
        settings_manager.set(f"{dev_type}_device_index", index)
        self.status_bar.showMessage(f"{dev_type.capitalize()} device set.", 3000)
        self.ui_to_daemon_queue.put({"type": "reload_models"})

    def set_active_model(self, mtype: Literal["tts", "stt", "llm"]):
        combo: QComboBox = getattr(self, f"{mtype}_model_list")
        model_id = combo.currentData()
        if model_id is None: return
        settings_manager.set(f"active_{mtype}_model", model_id)
        self.status_bar.showMessage(f"Active {mtype.upper()} model set to '{combo.currentText()}'.", 3000)
        self.ui_to_daemon_queue.put({"type": "reload_models"})
        self.populate_settings()

    def delete_model(self, mtype: Literal["tts", "stt", "llm"]):
        combo: QComboBox = getattr(self, f"{mtype}_model_list")
        model_id = combo.currentData()
        if not model_id: return
        
        reply = QMessageBox.question(self, "Confirm Delete", f"Are you sure you want to delete model '{model_id}'?")
        if reply == QMessageBox.StandardButton.Yes:
            if mtype == "tts": tts_manager.delete_model(model_id)
            elif mtype == "stt": stt_manager.delete_model(model_id)
            else: llm_manager.delete_model(model_id)
            self.populate_settings()

    def download_model(self, mtype: Literal["tts", "stt", "llm"]):
        if mtype == "llm":
            item = self.llm_download_list.currentItem()
            if not item: return
            model_name = item.data(Qt.ItemDataRole.UserRole)
        else:
            combo: QComboBox = getattr(self, f"{mtype}_download_list")
            model_name = combo.currentData()
        
        if not model_name: return
        self.ui_to_daemon_queue.put({"type": f"download_{mtype}", "model_name": model_name})
        self.show_progress_dialog(f"Downloading {mtype.upper()} model: {model_name}")

    def preview_model(self, mtype: Literal["tts"]):
        if mtype == "tts":
            combo: QComboBox = getattr(self, f"tts_model_list")
            model_id = combo.currentData()
            if not model_id: return
            url = tts_manager.get_model_sample_url(model_id)
            if url:
                self.ui_to_daemon_queue.put({"type": "play_audio_url", "url": url})
            else:
                QMessageBox.information(self, "No Preview", "A preview is not available for this model.")

    def visit_model_page(self, mtype: Literal["tts", "stt", "llm"]):
        combo: QComboBox = getattr(self, f"{mtype}_model_list")
        model_id = combo.currentData()
        if not model_id: return
        url = ""
        if mtype == "tts": url = tts_manager.get_model_repo_url(model_id)
        elif mtype == "stt": url = stt_manager.get_model_repo_url(model_id)
        else: url = llm_manager.get_model_repo_url(model_id)
        
        if url: webbrowser.open(url)
        else: QMessageBox.information(self, "No Page", "Could not find a web page for this model.")

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
        sound_player.play(BUTTON_PRESS_SOUND)
        if self.input_mode == "voice":
            self.input_mode = "text"
            self.toggle_input_button.setIcon(qta.icon("fa5s.keyboard")); self.toggle_input_button.setToolTip("Switch to Voice")
            self.text_input.show(); self.text_input.setFocus()
            self.ui_to_daemon_queue.put({"type": "stop_listening"})
        else:
            self.input_mode = "voice"
            self.toggle_input_button.setIcon(qta.icon("fa5s.microphone")); self.toggle_input_button.setToolTip("Switch to Text")
            self.text_input.hide()
            self.ui_to_daemon_queue.put({"type": "start_listening"})

    def on_text_input_submitted(self):
        prompt = self.text_input.text().strip()
        if prompt:
            self.ui_to_daemon_queue.put({"type": "process_text", "payload": prompt})
            self.add_conversation_item(prompt, "user")
            self.text_input.clear()

    # --- Worker Communication ---
    def start_queue_listener(self):
        self.queue_listener = QueueListener(self.daemon_to_ui_queue)
        self.queue_listener.signals.status_update.connect(self.on_status_update)
        self.queue_listener.signals.assistant_response.connect(self.on_assistant_response)
        self.queue_listener.signals.error.connect(self.on_error)
        self.queue_listener.signals.download_progress.connect(self.on_download_progress)
        self.thread_pool.start(self.queue_listener)
        
    def add_conversation_item(self, text: str, role: str):
        item = QListWidgetItem(f"{role.capitalize()}: {text}")
        item.setForeground(Qt.GlobalColor.cyan if role == "user" else Qt.GlobalColor.green)
        self.conversation_view.addItem(item)
        self.conversation_view.scrollToBottom()

    def show_progress_dialog(self, title: str):
        self.progress_dialog = QProgressDialog(title, "Cancel", 0, 100, self)
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.setAutoClose(False)
        self.progress_dialog.show()

    def on_status_update(self, text: str):
        self.status_bar.showMessage(text)

    def on_assistant_response(self, text: str, user_prompt: str):
        if user_prompt: # Don't show user prompt for wake word activations
            self.add_conversation_item(user_prompt, "user")
        self.add_conversation_item(text, "assistant")

    def on_error(self, title: str, message: str):
        if self.progress_dialog:
            self.progress_dialog.close()
            self.progress_dialog = None
        QMessageBox.warning(self, title, message)

    def on_download_progress(self, event: str, total: int, current: int, msg: str):
        if not self.progress_dialog: return

        if event == "start":
            self.progress_dialog.setLabelText(msg or "Starting download...")
            if total: self.progress_dialog.setMaximum(total)
            else: self.progress_dialog.setMaximum(0) # Indeterminate
        elif event == "update":
            self.progress_dialog.setValue(current)
        elif event == "finish":
            self.progress_dialog.close()
            self.progress_dialog = None
            QMessageBox.information(self, "Download Complete", "Model successfully downloaded.")
            self.populate_settings()
        elif event == "error":
            self.on_error("Download Failed", msg)
    
    def closeEvent(self, event):
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
---DELETED---
```

### File: `/corvus_app/ui/screens/confirm_screen.py`
```py
---DELETED---
```

### File: `/corvus_app/ui/screens/download_screen.py`
```py
---DELETED---
```

### File: `/corvus_app/ui/screens/main_screen.py`
```py
---DELETED---
```

### File: `/corvus_app/ui/shared.py`
```py
---DELETED---
```

### File: `/corvus_app/ui/themes.py`
```py
---DELETED---
```

### File: `/corvus_app/ui/tui.css`
```css
---DELETED---
```

### File: `/corvus_app/ui/tui.py`
```py
---DELETED---
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
    download_progress = pyqtSignal(str, int, int, str)
    result = pyqtSignal(str)

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
                elif msg_type == "download_progress":
                    self.signals.download_progress.emit(
                        msg["event"], msg.get("total_size", 0), msg.get("downloaded", 0), msg.get("message", "")
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

============================================================================
==                   GEMINI AI - CORVUS CRASH REPORT                      ==
============================================================================
Timestamp: 2025-08-07T14:26:07.575020
App_Part: Main App Bootstrap

--- Environment ---
OS_Platform: Windows
OS_Release: 10 (Note: Windows 11 often reports as 10, this is normal)
OS_Version: 10.0.26100
Architecture: AMD64
Python_Version: 3.11.8

--- Error ---
Type: TypeError
Message: unsupported operand type(s) for |: 'str' and 'NoneType'

--- State Context ---
Active Llm Model: None

--- Traceback ---
```
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\main.py", line 32, in main
    from daemon_process import run_daemon_process
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\daemon_process.py", line 17, in <module>
    from corvus_app.assistant import Assistant
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\assistant.py", line 6, in <module>
    from corvus_app.llm.llm_client import LLMClient
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\llm\llm_client.py", line 20, in <module>
    class LLMClient:
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\corvus_app\llm\llm_client.py", line 23, in LLMClient
    _llm: "Llama" | None = None
          ~~~~~~~~^~~~~~
TypeError: unsupported operand type(s) for |: 'str' and 'NoneType'
```


```

### File: `/corvus_daemon.log`
```log
2025-08-07 14:52:28,969 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:52:28,969 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_daemon.log'. Log Level: INFO
2025-08-07 14:52:28,969 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-07 14:52:28,969 [MainThread  ] [Daemon                   ] [INFO    ]  Daemon process initializing.
2025-08-07 14:52:28,970 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Initializing Assistant...
2025-08-07 14:52:28,970 [MainThread  ] [plugins.registry         ] [INFO    ]  Initializing CommandRegistry, scanning 'plugins' for plugins.
2025-08-07 14:52:28,971 [MainThread  ] [plugins.registry         ] [INFO    ]  Discovered and loaded 2 command(s).
2025-08-07 14:52:28,971 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 14:52:28,971 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:52:28,972 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:52:28,973 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:52:28,973 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:52:28,973 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:52:28,974 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 14:52:28,974 [Thread-1 (_w] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 14:52:28,974 [MainThread  ] [Daemon                   ] [INFO    ]  Wake word listener started.
2025-08-07 14:52:28,974 [Thread-1 (_w] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 14:52:28,974 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:52:28,975 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:52:28,976 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:52:28,976 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:52:28,976 [Thread-1 (_w] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:52:28,977 [Thread-1 (_w] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 14:52:28,977 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Attempting to load STT model: 'medium.en'
2025-08-07 14:52:31,601 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  STT model 'medium.en' loaded successfully on cpu.
2025-08-07 14:52:31,691 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:52:35,656 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:52:35,656 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.665
2025-08-07 14:52:39,706 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'I saw him on the right hand corner.' (Lang: en, Prob: 1.00)
2025-08-07 14:52:39,798 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:52:45,622 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:52:45,622 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.985
2025-08-07 14:52:49,561 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Oh, Japan as well actually yeah' (Lang: en, Prob: 1.00)
2025-08-07 14:52:49,656 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:52:55,421 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:52:55,421 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.665
2025-08-07 14:52:59,007 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Hahahaha' (Lang: en, Prob: 1.00)
2025-08-07 14:52:59,104 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:53:03,910 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:53:03,910 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.049
2025-08-07 14:53:07,693 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'They're like, they're like fucking' (Lang: en, Prob: 1.00)
2025-08-07 14:53:07,784 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:53:11,369 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:53:11,369 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.305
2025-08-07 14:53:14,938 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Hahahaha' (Lang: en, Prob: 1.00)
2025-08-07 14:53:15,031 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:53:19,446 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:53:19,446 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 14:53:23,229 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:53:23,334 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:53:28,711 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 14:53:28,711 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 14:53:28,711 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:53:28,712 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:53:28,713 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:53:28,713 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:53:28,713 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:53:28,714 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 14:53:28,720 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 14:53:28,720 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 14:53:28,721 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 14:53:28,722 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 14:53:28,722 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 14:53:28,723 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 14:53:28,723 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 14:53:28,723 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 14:53:31,020 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:53:31,020 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.497
2025-08-07 14:53:34,878 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.' (Lang: en, Prob: 1.00)
2025-08-07 14:53:34,985 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:53:43,429 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:53:43,430 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.433
2025-08-07 14:53:46,329 [Thread-4 (do] [models.llm_manager       ] [INFO    ]  Starting download of mistral-7b-instruct-v0.2.Q4_K_M.gguf from TheBloke/Mistral-7B-Instruct-v0.2-GGUF
2025-08-07 14:53:46,331 [Thread-4 (do] [py.warnings              ] [WARNING ]  C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\huggingface_hub\file_download.py:945: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
  warnings.warn(

2025-08-07 14:53:47,100 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:53:47,204 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:53:56,099 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:53:56,099 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.753
2025-08-07 14:54:00,428 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'I'll pull this fire off the line at least slightly.' (Lang: en, Prob: 1.00)
2025-08-07 14:54:00,535 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:54:07,603 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:54:14,968 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:54:14,969 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.793
2025-08-07 14:54:18,842 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Just feel the house shining.' (Lang: en, Prob: 1.00)
2025-08-07 14:54:18,945 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:54:26,024 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:54:32,680 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:54:32,680 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:03.521
2025-08-07 14:54:36,677 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:54:36,780 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:54:41,456 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:54:41,456 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.345
2025-08-07 14:54:45,120 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:54:45,223 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:54:52,458 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:54:52,459 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.753
2025-08-07 14:54:56,715 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'I've been brainwashing every single kid in the past, dude.' (Lang: en, Prob: 1.00)
2025-08-07 14:54:56,820 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:55:01,234 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:55:01,235 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.473
2025-08-07 14:55:05,092 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Yeah, no, honestly.' (Lang: en, Prob: 1.00)
2025-08-07 14:55:05,194 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:55:14,730 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:55:14,730 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:04.225
2025-08-07 14:55:19,073 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'and then when it when it comes down to it and when it when it comes' (Lang: en, Prob: 1.00)
2025-08-07 14:55:19,176 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:55:25,701 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:55:25,701 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.537
2025-08-07 14:55:29,499 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'And show them that when...' (Lang: en, Prob: 1.00)
2025-08-07 14:55:29,602 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:55:33,567 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:55:33,567 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.985
2025-08-07 14:55:37,418 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'What, in the past couple days?' (Lang: en, Prob: 1.00)
2025-08-07 14:55:37,521 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:55:44,176 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:55:44,177 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.241
2025-08-07 14:55:47,783 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:55:47,882 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:55:53,126 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:55:53,126 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 14:55:56,956 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'I' (Lang: en, Prob: 1.00)
2025-08-07 14:55:57,058 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:01,732 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:01,733 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.857
2025-08-07 14:56:05,403 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:56:05,504 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:09,220 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:09,220 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.857
2025-08-07 14:56:12,788 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:56:12,887 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:20,572 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:20,573 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:04.545
2025-08-07 14:56:24,991 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Where are we at?  In that one we lost  Why?' (Lang: en, Prob: 1.00)
2025-08-07 14:56:25,091 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:28,806 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:28,806 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.049
2025-08-07 14:56:32,497 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Laughter' (Lang: en, Prob: 1.00)
2025-08-07 14:56:32,598 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:36,633 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:36,633 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 14:56:40,571 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'We now have the 1,200 back.' (Lang: en, Prob: 1.00)
2025-08-07 14:56:40,671 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:44,197 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:44,197 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.665
2025-08-07 14:56:48,090 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'because we've never had' (Lang: en, Prob: 1.00)
2025-08-07 14:56:48,191 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:56:56,576 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:56:56,577 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:03.393
2025-08-07 14:57:00,530 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'They signed up with the nine native tribes' (Lang: en, Prob: 1.00)
2025-08-07 14:57:00,633 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:57:07,158 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:57:07,158 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.601
2025-08-07 14:57:10,923 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:57:11,022 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:57:17,747 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:57:17,747 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.817
2025-08-07 14:57:26,449 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'What would an indigenous man, an indigenous soul,  an American soul,' (Lang: en, Prob: 1.00)
2025-08-07 14:57:26,563 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:57:32,388 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:57:32,388 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.985
2025-08-07 14:57:36,027 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.' (Lang: en, Prob: 1.00)
2025-08-07 14:57:36,126 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:57:39,901 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:57:39,901 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.113
2025-08-07 14:57:43,413 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'But' (Lang: en, Prob: 1.00)
2025-08-07 14:57:43,509 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:57:47,475 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:57:47,475 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.241
2025-08-07 14:57:51,010 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Oh' (Lang: en, Prob: 1.00)
2025-08-07 14:57:51,109 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:57:59,814 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:57:59,814 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:04.993
2025-08-07 14:58:24,999 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Laughter  Alright, was that what you woke up on?  Laughter' (Lang: en, Prob: 1.00)
2025-08-07 14:58:25,107 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:58:31,702 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:58:31,702 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 14:58:35,500 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:58:35,596 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:58:39,821 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:58:39,821 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.537
2025-08-07 14:58:43,524 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:58:43,619 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:58:50,704 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:58:56,209 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:58:56,209 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:03.137
2025-08-07 14:59:00,127 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'They completely stopped the whole space.' (Lang: en, Prob: 1.00)
2025-08-07 14:59:00,226 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:59:08,162 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:59:08,162 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:04.673
2025-08-07 14:59:12,290 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 14:59:12,385 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:59:19,360 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:59:19,360 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.113
2025-08-07 14:59:22,962 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.' (Lang: en, Prob: 1.00)
2025-08-07 14:59:23,055 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:59:27,271 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:59:27,271 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.601
2025-08-07 14:59:30,970 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '.' (Lang: en, Prob: 1.00)
2025-08-07 14:59:31,065 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:59:38,300 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:59:38,301 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:03.073
2025-08-07 14:59:42,221 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'It was because they had the fresh space.' (Lang: en, Prob: 1.00)
2025-08-07 14:59:42,319 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:59:48,784 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:59:48,785 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.625
2025-08-07 14:59:52,719 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '3, 2, 1...' (Lang: en, Prob: 1.00)
2025-08-07 14:59:52,819 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 14:59:56,594 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 14:59:56,594 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.857
2025-08-07 15:00:00,614 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'It's because I've actually got a jazz song.' (Lang: en, Prob: 1.00)
2025-08-07 15:00:00,709 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:00:04,805 [Thread-4 (do] [py.warnings              ] [WARNING ]  C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\huggingface_hub\file_download.py:143: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\Users\gike5\.cache\huggingface\hub\models--TheBloke--Mistral-7B-Instruct-v0.2-GGUF. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)

2025-08-07 15:00:04,806 [Thread-4 (do] [models.llm_manager       ] [INFO    ]  Successfully downloaded and moved LLM to llm_models\mistral-7b-instruct-v0.2.Q4_K_M.gguf
2025-08-07 15:00:06,154 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:00:06,155 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.177
2025-08-07 15:00:06,428 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:06,428 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:06,429 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:06,430 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:06,431 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:06,432 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:06,432 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:06,432 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:06,433 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:06,433 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:06,433 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:06,434 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:06,435 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:06,435 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:06,436 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:06,436 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:06,436 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:06,437 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:06,437 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:06,438 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:06,439 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:06,440 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:06,440 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:06,440 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:06,441 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:06,441 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:06,441 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:06,442 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:06,443 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:06,444 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:06,445 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:06,445 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:09,915 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 15:00:10,008 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:00:17,244 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:00:17,244 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:04.161
2025-08-07 15:00:21,378 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 15:00:21,479 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:00:28,394 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:00:28,395 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.793
2025-08-07 15:00:32,032 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 15:00:32,135 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:00:34,341 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:34,341 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:34,341 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:34,342 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:34,343 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:34,343 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:34,343 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:34,344 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:34,346 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:34,346 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:34,346 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:34,347 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:34,347 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:34,348 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:34,348 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:34,348 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:34,348 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:34,348 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:34,349 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:34,349 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:34,349 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:34,351 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:34,351 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:34,351 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:34,351 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:34,351 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:34,352 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:34,352 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:34,353 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:34,353 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:34,354 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:34,354 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:34,354 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:34,354 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:34,354 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:34,355 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:34,355 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:34,356 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:34,356 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:34,356 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:39,559 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:00:39,559 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.241
2025-08-07 15:00:39,767 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:39,767 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:39,767 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:39,769 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:39,769 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:39,770 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:39,771 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:39,771 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:39,776 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:39,776 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:39,776 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:39,778 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:39,778 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:39,779 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:39,780 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:39,780 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:39,780 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:39,780 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:39,781 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:39,782 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:39,782 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:39,783 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:39,783 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:39,783 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:39,784 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:39,784 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:39,784 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:39,785 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:39,786 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:39,786 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:39,787 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:39,787 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:39,787 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:39,787 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:39,788 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:39,789 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:39,790 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:39,790 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:39,791 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:39,791 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:42,206 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:42,206 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:42,207 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:42,223 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:42,223 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:42,224 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:42,225 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:42,225 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:42,228 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:42,228 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:42,229 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:42,230 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:42,231 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:42,231 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:42,232 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:42,232 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:42,232 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:42,232 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:42,233 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:42,234 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:42,234 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:42,235 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:42,235 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:42,236 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:42,236 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:42,236 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:42,236 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:42,237 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:42,238 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:42,238 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:42,239 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:42,239 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:42,239 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:42,239 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:42,239 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:42,240 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:42,241 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:42,241 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:42,242 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:42,242 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:43,444 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '...the Spanish or the French in Australia...' (Lang: en, Prob: 1.00)
2025-08-07 15:00:43,545 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:00:44,188 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:44,188 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:44,188 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:44,189 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:44,189 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:44,191 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:44,191 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:44,191 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:44,193 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:44,194 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:44,194 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:44,195 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:44,195 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:44,196 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:44,196 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:44,196 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:44,196 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:44,196 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:44,197 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:44,197 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:44,198 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:44,198 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:44,199 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:44,199 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:44,199 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:44,199 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:44,199 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:44,200 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:44,200 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:44,201 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:44,201 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:44,201 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:44,201 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:44,201 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:44,202 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:44,202 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:44,203 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:44,203 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:44,204 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:44,204 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:46,529 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:46,529 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:46,530 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:46,530 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:46,531 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:46,531 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:46,532 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:46,532 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:46,534 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:46,534 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:46,534 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:46,535 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:46,536 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:46,536 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:46,537 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:46,537 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:46,537 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:46,537 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:46,537 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:46,538 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:46,538 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:46,539 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:46,539 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:46,539 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:46,539 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:46,539 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:46,540 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:46,540 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:46,541 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:46,541 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:46,542 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:46,542 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:46,542 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:46,542 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:46,542 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:46,543 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:46,543 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'small.en' in directory 'models--Systran--faster-distil-whisper-small.en'
2025-08-07 15:00:46,544 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:46,544 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:46,544 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:47,818 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:47,818 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:47,818 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:47,819 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:47,820 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:47,820 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:47,821 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:47,821 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:47,821 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:47,821 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:47,822 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:47,822 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:47,823 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:47,823 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:47,823 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:47,823 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:47,823 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:47,824 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:47,824 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:47,825 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:47,825 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:47,825 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:47,825 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:47,825 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:47,826 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-distil-whisper-medium.en'
2025-08-07 15:00:47,827 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:47,827 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:47,827 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:48,090 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:00:48,090 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.793
2025-08-07 15:00:50,327 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:50,327 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:50,328 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:50,330 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:50,331 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:50,331 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:50,331 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:50,331 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:50,332 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:50,333 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:50,334 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:50,334 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:50,334 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:50,334 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:50,335 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:50,336 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:50,337 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:50,337 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:50,337 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:50,337 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:50,338 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:50,339 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:00:50,340 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:50,340 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:51,250 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:51,250 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:51,251 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:51,253 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:51,254 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:51,254 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:51,254 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:51,255 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:51,257 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:51,257 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:51,257 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:51,257 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:51,257 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:51,260 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:51,260 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:51,260 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:51,260 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:51,261 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:51,262 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'medium.en' in directory 'models--Systran--faster-whisper-medium.en'
2025-08-07 15:00:51,262 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:52,161 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:52,161 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:52,161 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:52,162 [MainThread  ] [models.stt_manager       ] [WARNING ]  Could not identify any valid STT model subdirectories.
2025-08-07 15:00:52,163 [MainThread  ] [corvus_app.assistant     ] [WARNING ]  Active STT model 'medium.en' not found. Resetting to 'base'.
2025-08-07 15:00:52,163 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:52,164 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:52,164 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:52,164 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:52,165 [MainThread  ] [models.stt_manager       ] [WARNING ]  Could not identify any valid STT model subdirectories.
2025-08-07 15:00:52,165 [MainThread  ] [corvus_app.assistant     ] [WARNING ]  Active STT model 'base' not found. Resetting to 'base'.
2025-08-07 15:00:52,166 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:52,166 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:52,166 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:52,167 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:52,168 [MainThread  ] [models.stt_manager       ] [WARNING ]  Could not identify any valid STT model subdirectories.
2025-08-07 15:00:52,168 [MainThread  ] [corvus_app.assistant     ] [WARNING ]  Active STT model 'base' not found. Resetting to 'base'.
2025-08-07 15:00:52,168 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:52,169 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:00:52,169 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:00:52,169 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:00:52,170 [MainThread  ] [models.stt_manager       ] [WARNING ]  Could not identify any valid STT model subdirectories.
2025-08-07 15:00:52,170 [MainThread  ] [corvus_app.assistant     ] [WARNING ]  Active STT model 'base' not found. Resetting to 'base'.
2025-08-07 15:00:52,171 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:00:52,182 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'And just try to leave, we actually...' (Lang: en, Prob: 1.00)
2025-08-07 15:00:52,291 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:00:55,816 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:00:55,816 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.537
2025-08-07 15:00:59,388 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 15:00:59,505 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:04,369 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:01:04,369 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.921
2025-08-07 15:01:07,952 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '...' (Lang: en, Prob: 1.00)
2025-08-07 15:01:08,054 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:12,029 [Thread-5 (_d] [models.stt_manager       ] [INFO    ]  Requesting faster-whisper to download model: 'base'
2025-08-07 15:01:12,583 [ThreadPoolEx] [huggingface_hub.file_down] [WARNING ]  Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
2025-08-07 15:01:12,615 [ThreadPoolEx] [py.warnings              ] [WARNING ]  C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\huggingface_hub\file_download.py:143: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models\models--Systran--faster-whisper-base. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)

2025-08-07 15:01:13,240 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:01:13,240 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:02.561
2025-08-07 15:01:17,222 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'We didn't just go in there.' (Lang: en, Prob: 1.00)
2025-08-07 15:01:17,324 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:21,999 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:01:21,999 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.857
2025-08-07 15:01:25,159 [Thread-5 (_d] [models.stt_manager       ] [INFO    ]  Model 'base' downloaded/verified successfully.
2025-08-07 15:01:25,944 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Install it, I install it' (Lang: en, Prob: 1.00)
2025-08-07 15:01:26,035 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:33,105 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:33,690 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:33,690 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:33,690 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:33,691 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:33,692 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:33,692 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:33,692 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:33,692 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:33,693 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:33,693 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:33,693 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:33,693 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:33,693 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:33,694 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:33,695 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:33,695 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:33,695 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:33,695 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:33,696 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:33,696 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:40,183 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:40,588 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:40,589 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:40,589 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:40,590 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:40,590 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:40,592 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:40,592 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:40,593 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:40,594 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:40,594 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:40,594 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:40,594 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:40,594 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:40,596 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:40,596 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:40,596 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:40,596 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:40,597 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:40,597 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:40,598 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:40,598 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:40,598 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:40,598 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:40,599 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:40,599 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:44,859 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:01:44,859 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.217
2025-08-07 15:01:48,703 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Yeah, but would you like to hear my?' (Lang: en, Prob: 1.00)
2025-08-07 15:01:48,797 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:01:56,674 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:01:56,674 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.473
2025-08-07 15:01:57,009 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:57,009 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:57,010 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:57,011 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:57,012 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:57,015 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:57,016 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:57,016 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:57,018 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:57,019 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:57,019 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:57,019 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:57,019 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:57,021 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:57,021 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:57,021 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:57,021 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:57,022 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:57,023 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:57,024 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:01:57,024 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Reloading Assistant components...
2025-08-07 15:01:57,024 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Validating settings...
2025-08-07 15:01:57,024 [MainThread  ] [models.stt_manager       ] [INFO    ]  Scanning for local STT models in: C:\Users\gike5\Desktop\AI_Python\Corvus\stt_models
2025-08-07 15:01:57,026 [MainThread  ] [models.stt_manager       ] [INFO    ]  Found STT model 'base' in directory 'models--Systran--faster-whisper-base'
2025-08-07 15:01:57,026 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected.
2025-08-07 15:02:00,506 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 15:02:00,604 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:02:05,659 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:02:05,659 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.601
2025-08-07 15:02:09,098 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: '' (Lang: en, Prob: 1.00)
2025-08-07 15:02:09,195 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:02:13,931 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:02:13,931 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 15:02:17,806 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'Hello.  Hi.  Hello.' (Lang: en, Prob: 1.00)
2025-08-07 15:02:17,899 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:02:25,631 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...
2025-08-07 15:02:30,306 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech with local Whisper model...
2025-08-07 15:02:30,306 [Thread-1 (_w] [faster_whisper           ] [INFO    ]  Processing audio with duration 00:01.409
2025-08-07 15:02:34,174 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Transcribed: 'To get to Australia' (Lang: en, Prob: 1.00)
2025-08-07 15:02:34,286 [Thread-1 (_w] [corvus_app.audio.stt     ] [INFO    ]  Listening on device index: None...

```

### File: `/daemon_process.py`
```py
# daemon_process.py
import logging
import re
import sys
import threading
import requests
from pathlib import Path
from queue import Empty
from typing import Optional

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
from models import tts_manager, stt_manager, llm_manager

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
        self.daemon_to_ui_queue.put(message)

    def _update_status(self, text: str):
        self._send_to_ui({"type": "status_update", "text": text})

    def _wake_word_loop(self):
        """Dedicated thread to listen for the wake word."""
        if not self.assistant: self.assistant = Assistant()
        self.assistant.reload()
        get_stt_engine() # Pre-load STT model
        self._update_status("LISTENING...")
        
        while self._listening and self._running:
            wake_word = settings_manager.get("wake_word")
            text, lang, prob = listen_for_audio()
            if not self._listening or not self._running: break
            
            if text and wake_word.lower() in text.lower():
                prompt = re.sub(rf'^\s*{re.escape(wake_word)}[\s,.]*', '', text, flags=re.IGNORECASE).strip()
                self._update_status("PROCESSING...")
                if prompt: self.process_prompt(prompt, lang, prob)
                else: self._speak_and_reset_status("Yes?")
                
                if self._listening: self._update_status("LISTENING...")

    def process_prompt(self, prompt: str, lang: Optional[str] = None, prob: Optional[float] = None):
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
        if error: self._send_to_ui({"type": "error", "message": f"TTS Error: {error}"})

    def _play_audio_from_url(self, url: str):
        try:
            logger.info(f"Playing audio from URL: {url}")
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()
            # This is a bit of a hack. We pass the raw http response body
            # to soundfile, which can handle it like a file object.
            sound_player.play(response.raw, asynchronous=False)
        except Exception as e:
            logger.error(f"Failed to play audio from URL {url}: {e}", exc_info=True)
            self._send_to_ui({"type": "error", "message": f"Failed to play audio: {e}"})

    def _create_progress_callback(self):
        def callback(event, **kwargs):
            self._send_to_ui({"type": "download_progress", "event": event, **kwargs})
        return callback

    def _download_stt_model(self, model_name: str):
        progress_callback = self._create_progress_callback()
        progress_callback("start", message="Downloading with faster-whisper...", total_size=None)
        try:
            stt_manager.download_model(model_name)
            progress_callback("finish")
        except Exception as e:
            logger.error(f"Failed to download STT model '{model_name}': {e}", exc_info=True)
            progress_callback("error", message=str(e))

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
        self.assistant = Assistant()
        TTSEngine()
        self._running = True
        self.start_listening()

        while self._running:
            try:
                command = self.ui_to_daemon_queue.get(timeout=0.2)
                cmd_type = command.get("type")
                logger.debug(f"Daemon received command: {cmd_type}")

                if cmd_type == "process_text": self.process_prompt(command.get("payload"))
                elif cmd_type == "reload_models": self.assistant.reload()
                elif cmd_type == "shutdown": self._running = False
                elif cmd_type == "test_tts": self._speak_and_reset_status("This is a text to speech test.")
                elif cmd_type == "test_llm": self.process_prompt("Test: Say 'ok'")
                elif cmd_type == "start_listening": self.start_listening()
                elif cmd_type == "stop_listening": self.stop_listening()
                elif cmd_type == "play_audio_url": threading.Thread(target=self._play_audio_from_url, args=(command["url"],), daemon=True).start()
                elif cmd_type == "download_tts": threading.Thread(target=tts_manager.download_model, args=(command["model_name"], self._create_progress_callback()), daemon=True).start()
                elif cmd_type == "download_stt": threading.Thread(target=self._download_stt_model, args=(command["model_name"],), daemon=True).start()
                elif cmd_type == "download_llm": threading.Thread(target=llm_manager.download_model, args=(command["model_name"], self._create_progress_callback()), daemon=True).start()

            except Empty: continue
            except (KeyboardInterrupt, SystemExit): self._running = False
            except Exception as e: logger.error(f"Error in daemon loop: {e}", exc_info=True)
        
        logger.info("Daemon process loop finished, sending shutdown acknowledgement.")
        self._send_to_ui({"type": "shutdown_ack"})

def run_daemon_process(ui_to_daemon_queue, daemon_to_ui_queue):
    setup_logging("corvus_daemon.log")
    logger.info("Daemon process initializing.")
    daemon = Daemon(ui_to_daemon_queue, daemon_to_ui_queue)
    daemon.run()
```

### File: `/installer.log`
```log
2025-08-07 14:52:21,754 [INFO    ]  Valid virtual environment found.
2025-08-07 14:52:21,757 [INFO    ]  Installing dependencies (this may take several minutes)...
2025-08-07 14:52:21,759 [INFO    ]  Running command: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt
2025-08-07 14:52:22,332 [INFO    ]  Requirement already satisfied: PyQt6 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (6.9.1)
2025-08-07 14:52:22,336 [INFO    ]  Requirement already satisfied: qtawesome in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 2)) (1.4.0)
2025-08-07 14:52:22,337 [INFO    ]  Requirement already satisfied: SpeechRecognition in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 3)) (3.14.3)
2025-08-07 14:52:22,338 [INFO    ]  Requirement already satisfied: PyAudio in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 4)) (0.2.14)
2025-08-07 14:52:22,339 [INFO    ]  Requirement already satisfied: rich in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (14.1.0)
2025-08-07 14:52:22,339 [INFO    ]  Requirement already satisfied: python-dotenv in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6)) (1.1.1)
2025-08-07 14:52:22,340 [INFO    ]  Requirement already satisfied: requests in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2.32.4)
2025-08-07 14:52:22,341 [INFO    ]  Requirement already satisfied: sounddevice in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (0.5.2)
2025-08-07 14:52:22,342 [INFO    ]  Requirement already satisfied: soundfile in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9)) (0.13.1)
2025-08-07 14:52:22,342 [INFO    ]  Requirement already satisfied: onnxruntime==1.15.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.15.1)
2025-08-07 14:52:22,343 [INFO    ]  Requirement already satisfied: faster-whisper in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (1.2.0)
2025-08-07 14:52:22,344 [INFO    ]  Requirement already satisfied: piper-tts in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 12)) (1.3.0)
2025-08-07 14:52:22,344 [INFO    ]  Requirement already satisfied: llama-cpp-python in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 13)) (0.3.14)
2025-08-07 14:52:22,345 [INFO    ]  Requirement already satisfied: huggingface-hub in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 14)) (0.34.3)
2025-08-07 14:52:22,346 [INFO    ]  Requirement already satisfied: coloredlogs in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (15.0.1)
2025-08-07 14:52:22,346 [INFO    ]  Requirement already satisfied: flatbuffers in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (25.2.10)
2025-08-07 14:52:22,349 [INFO    ]  Requirement already satisfied: numpy>=1.24.2 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.26.4)
2025-08-07 14:52:22,350 [INFO    ]  Requirement already satisfied: packaging in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (25.0)
2025-08-07 14:52:22,351 [INFO    ]  Requirement already satisfied: protobuf in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (6.31.1)
2025-08-07 14:52:22,352 [INFO    ]  Requirement already satisfied: sympy in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.14.0)
2025-08-07 14:52:22,356 [INFO    ]  Requirement already satisfied: PyQt6-sip<14,>=13.8 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from PyQt6->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (13.10.2)
2025-08-07 14:52:22,357 [INFO    ]  Requirement already satisfied: PyQt6-Qt6<6.10.0,>=6.9.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from PyQt6->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1)) (6.9.1)
2025-08-07 14:52:22,358 [INFO    ]  Requirement already satisfied: qtpy in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from qtawesome->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 2)) (2.4.3)
2025-08-07 14:52:22,362 [INFO    ]  Requirement already satisfied: typing-extensions in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from SpeechRecognition->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 3)) (4.14.1)
2025-08-07 14:52:22,365 [INFO    ]  Requirement already satisfied: markdown-it-py>=2.2.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (3.0.0)
2025-08-07 14:52:22,366 [INFO    ]  Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (2.19.2)
2025-08-07 14:52:22,372 [INFO    ]  Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (3.4.2)
2025-08-07 14:52:22,373 [INFO    ]  Requirement already satisfied: idna<4,>=2.5 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (3.10)
2025-08-07 14:52:22,374 [INFO    ]  Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2.5.0)
2025-08-07 14:52:22,374 [INFO    ]  Requirement already satisfied: certifi>=2017.4.17 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (2025.8.3)
2025-08-07 14:52:22,376 [INFO    ]  Requirement already satisfied: CFFI>=1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from sounddevice->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (1.17.1)
2025-08-07 14:52:22,383 [INFO    ]  Requirement already satisfied: ctranslate2<5,>=4.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (4.6.0)
2025-08-07 14:52:22,384 [INFO    ]  Requirement already satisfied: tokenizers<1,>=0.13 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.21.4)
2025-08-07 14:52:22,385 [INFO    ]  Requirement already satisfied: av>=11 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (15.0.0)
2025-08-07 14:52:22,389 [INFO    ]  Requirement already satisfied: tqdm in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (4.67.1)
2025-08-07 14:52:22,405 [INFO    ]  Requirement already satisfied: diskcache>=5.6.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 13)) (5.6.3)
2025-08-07 14:52:22,407 [INFO    ]  Requirement already satisfied: jinja2>=2.11.3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 13)) (3.1.6)
2025-08-07 14:52:22,438 [INFO    ]  Requirement already satisfied: filelock in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 14)) (3.18.0)
2025-08-07 14:52:22,439 [INFO    ]  Requirement already satisfied: fsspec>=2023.5.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 14)) (2025.7.0)
2025-08-07 14:52:22,440 [INFO    ]  Requirement already satisfied: pyyaml>=5.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from huggingface-hub->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 14)) (6.0.2)
2025-08-07 14:52:22,444 [INFO    ]  Requirement already satisfied: pycparser in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from CFFI>=1.0->sounddevice->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8)) (2.22)
2025-08-07 14:52:22,448 [INFO    ]  Requirement already satisfied: setuptools in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from ctranslate2<5,>=4.0->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (65.5.0)
2025-08-07 14:52:22,481 [INFO    ]  Requirement already satisfied: MarkupSafe>=2.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from jinja2>=2.11.3->llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 13)) (3.0.2)
2025-08-07 14:52:22,488 [INFO    ]  Requirement already satisfied: mdurl~=0.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from markdown-it-py>=2.2.0->rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5)) (0.1.2)
2025-08-07 14:52:22,508 [INFO    ]  Requirement already satisfied: colorama in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from tqdm->faster-whisper->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 11)) (0.4.6)
2025-08-07 14:52:22,516 [INFO    ]  Requirement already satisfied: humanfriendly>=9.1 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from coloredlogs->onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (10.0)
2025-08-07 14:52:22,529 [INFO    ]  Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from sympy->onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (1.3.0)
2025-08-07 14:52:22,533 [INFO    ]  Requirement already satisfied: pyreadline3 in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from humanfriendly>=9.1->coloredlogs->onnxruntime==1.15.1->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 10)) (3.5.4)
2025-08-07 14:52:23,284 [INFO    ]  [notice] A new release of pip is available: 24.0 -> 25.2
2025-08-07 14:52:23,287 [INFO    ]  [notice] To update, run: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install --upgrade pip
2025-08-07 14:52:23,341 [INFO    ]  Dependencies installed successfully!
2025-08-07 14:52:23,342 [INFO    ]  Wrote requirements hash '7e32bf03559f22f54692fdcba3b5ebad' to marker file.
2025-08-07 14:52:23,343 [INFO    ]  Setting up configuration...
2025-08-07 14:52:23,344 [INFO    ]  .env file already exists, skipping creation.
2025-08-07 14:52:23,345 [INFO    ]  Setup complete. The main application will now launch.

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

### File: `/models/llm_manager.py`
```py
# models/llm_manager.py
import logging
import shutil
from pathlib import Path

# Lazy import to avoid crashing if not installed
try:
    from huggingface_hub import hf_hub_download
    HUGGINGFACE_HUB_AVAILABLE = True
except ImportError:
    HUGGINGFACE_HUB_AVAILABLE = False


logger = logging.getLogger(__name__)

LLM_MODELS_PATH = Path("llm_models")
LLM_MODELS_PATH.mkdir(exist_ok=True)

# A curated list of some popular GGUF models.
REMOTE_MODELS = {
    "Mistral-7B-Instruct-v0.2-Q4_K_M": {
        "repo_id": "TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
        "filename": "mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "notes": "Good balance of speed and quality. Needs ~8GB RAM.",
        "url": "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
    },
    "Llama-3-8B-Instruct-Q4_K_M": {
        "repo_id": "MaziyarJes/Meta-Llama-3-8B-Instruct-GGUF",
        "filename": "Meta-Llama-3-8B-Instruct.Q4_K_M.gguf",
        "notes": "Excellent all-rounder by Meta. Needs ~8GB RAM.",
        "url": "https://huggingface.co/MaziyarJes/Meta-Llama-3-8B-Instruct-GGUF"
    },
    "Phi-3-mini-4k-instruct-q4": {
        "repo_id": "microsoft/Phi-3-mini-4k-instruct-gguf",
        "filename": "Phi-3-mini-4k-instruct-q4.gguf",
        "notes": "Very small, fast model from Microsoft. Works with <4GB RAM.",
        "url": "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf"
    },
}

def get_remote_models_list() -> dict[str, dict]:
    """Returns the curated list of remote GGUF models."""
    return REMOTE_MODELS

def get_local_models() -> list[str]:
    """Returns a list of locally downloaded LLM models (by filename)."""
    if not LLM_MODELS_PATH.exists(): return []
    return [f.name for f in LLM_MODELS_PATH.iterdir() if f.suffix == '.gguf']

def get_model_repo_url(model_filename: str) -> str:
    """Finds the repo URL for a given local model filename."""
    for model_key, info in REMOTE_MODELS.items():
        if info["filename"] == model_filename:
            return info["url"]
    return ""

def download_model(model_key: str, progress_callback: callable):
    """Downloads a GGUF model from the remote list using its key."""
    if not HUGGINGFACE_HUB_AVAILABLE:
        msg = "huggingface-hub is not installed. Cannot download models."
        logger.error(msg)
        progress_callback("error", message=msg)
        return

    if model_key not in REMOTE_MODELS:
        msg = f"Model key '{model_key}' not found in remote list."
        logger.error(msg)
        progress_callback("error", message=msg)
        return

    model_info = REMOTE_MODELS[model_key]
    repo_id = model_info["repo_id"]
    filename = model_info["filename"]
    
    logger.info(f"Starting download of {filename} from {repo_id}")
    # hf_hub_download doesn't have a simple progress hook. We send an indeterminate start signal.
    progress_callback("start", message=f"Downloading {filename}...", total_size=None)
    
    try:
        cached_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir_use_symlinks=False,
            resume_download=True,
        )
        
        dest_path = LLM_MODELS_PATH / filename
        shutil.move(cached_path, dest_path)

        logger.info(f"Successfully downloaded and moved LLM to {dest_path}")
        progress_callback("finish")
    except Exception as e:
        logger.error(f"Failed to download LLM '{filename}': {e}", exc_info=True)
        progress_callback("error", message=str(e))

def delete_model(filename: str):
    """Deletes a local LLM model file."""
    try:
        model_path = LLM_MODELS_PATH / filename
        if model_path.exists():
            logger.info(f"Deleting LLM model: {model_path}")
            model_path.unlink()
            return True
        return False
    except Exception as e:
        logger.error(f"Failed to delete LLM {filename}: {e}", exc_info=True)
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

def get_model_repo_url(model_name: str) -> str:
    """Constructs a plausible Hugging Face repo URL for a given model name."""
    base_url = "https://huggingface.co/Systran"
    if "distil" in model_name:
        return f"{base_url}/faster-distil-whisper-{model_name}"
    else:
        return f"{base_url}/faster-whisper-{model_name}"

def get_local_models():
    """Returns a list of locally downloaded Whisper models."""
    logger.info(f"Scanning for local STT models in: {STT_MODELS_PATH.resolve()}")
    if not STT_MODELS_PATH.exists():
        logger.warning(f"STT models path does not exist.")
        return []

    local_models = set()
    sorted_available_models = sorted(AVAILABLE_MODELS, key=len, reverse=True)

    for model_dir in STT_MODELS_PATH.iterdir():
        if not model_dir.is_dir(): continue
        if not list(model_dir.rglob("model.bin")): continue

        dir_name_lower = model_dir.name.lower()
        for model_name in sorted_available_models:
            # Handle both '...-base' and '...-base.en' style directory names
            if model_name in dir_name_lower:
                if model_name not in local_models:
                    local_models.add(model_name)
                    logger.info(f"Found STT model '{model_name}' in directory '{model_dir.name}'")
                    break
    
    if not local_models:
        logger.warning("Could not identify any valid STT model subdirectories.")
        
    return sorted(list(local_models))

def download_model(model_name: str):
    """
    Uses the faster-whisper library to download a model. This is a blocking call.
    The library handles the actual download from Hugging Face.
    """
    logger.info(f"Requesting faster-whisper to download model: '{model_name}'")
    try:
        from faster_whisper import WhisperModel
        import torch
        # Download the model by initializing it.
        device = "cuda" if torch.cuda.is_available() else "cpu"
        compute_type = "float16" if device == "cuda" else "int8"
        WhisperModel(
            model_name,
            device=device,
            compute_type=compute_type,
            download_root=str(STT_MODELS_PATH)
        )
        logger.info(f"Model '{model_name}' downloaded/verified successfully.")
    except Exception as e:
        logger.error(f"Faster-whisper failed to download model '{model_name}': {e}", exc_info=True)
        raise # Re-raise the exception to be caught by the daemon thread.

def delete_model(model_name: str):
    """Deletes a local Whisper model directory."""
    if not STT_MODELS_PATH.exists(): return False
    try:
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
VOICES_REPO_URL = "https://huggingface.co/rhasspy/piper-voices"

_voices_index = {}

def get_remote_models_list() -> dict[str, str]:
    """
    Downloads and caches the official Piper voices index.
    Returns a dictionary of model_id: user_friendly_name.
    """
    global _voices_index
    if _voices_index:
        return {model_id: info['friendly_name'] for model_id, info in _voices_index.items()}

    logger.info(f"Fetching remote TTS voice index from {VOICES_URL}")
    try:
        with urllib.request.urlopen(VOICES_URL, timeout=10) as response:
            remote_data = json.load(response)

        formatted_voices = {}
        for model_id, model_info in remote_data.items():
            name = model_info.get("name", model_id)
            language = model_info.get("language", {}).get("name_english", "Unknown")
            quality = model_info.get("quality", "Unknown")
            
            if quality.lower() != "x_low": # Filter out the worst quality
                friendly_name = f"{language} - {name} ({quality.capitalize()})"
                model_info['friendly_name'] = friendly_name
                formatted_voices[model_id] = model_info
        
        _voices_index = formatted_voices
        logger.info(f"Successfully fetched and parsed {len(_voices_index)} TTS voices.")
        return {model_id: info['friendly_name'] for model_id, info in _voices_index.items()}

    except Exception as e:
        logger.error(f"Failed to fetch or parse remote voices index: {e}", exc_info=True)
        return {"error": "Could not fetch remote voice list."}

def get_local_models_list() -> dict[str, str]:
    """Finds installed Piper TTS models and returns a dict of model_id to friendly_name."""
    if not TTS_MODELS_PATH.exists(): return {}
    
    local_models = {}
    for model_dir in TTS_MODELS_PATH.iterdir():
        model_id = model_dir.name
        if model_dir.is_dir() and (model_dir / f"{model_id}.onnx").exists():
            friendly_name = model_id
            if _voices_index: # If remote index is loaded, get friendly name
                friendly_name = _voices_index.get(model_id, {}).get("friendly_name", model_id)
            local_models[model_id] = friendly_name
            
    return local_models

def get_model_sample_url(model_id: str) -> str | None:
    if not _voices_index: get_remote_models_list()
    model_info = _voices_index.get(model_id)
    if not model_info: return None
    
    for filename, file_info in model_info.get("files", {}).items():
        if filename.endswith(".mp3"):
            return file_info.get("url")
    return None

def get_model_repo_url(model_id: str) -> str:
    return f"{VOICES_REPO_URL}/tree/main/{model_id}"

def download_model(model_id: str, progress_callback: callable):
    """Downloads a Piper TTS model using URLs from the fetched index."""
    logger.info(f"Starting download for TTS model: {model_id}")
    if not _voices_index: get_remote_models_list()

    model_info = _voices_index.get(model_id)
    if not model_info:
        progress_callback("error", message=f"Model '{model_id}' not found in remote index.")
        return

    model_files = model_info.get("files", {})
    onnx_url = next((d.get("url") for f, d in model_files.items() if f.endswith(".onnx")), None)
    json_url = next((d.get("url") for f, d in model_files.items() if f.endswith(".onnx.json")), None)
    
    if not onnx_url or not json_url:
        progress_callback("error", message="Could not find model/config URL in index.")
        return
        
    model_dir = TTS_MODELS_PATH / model_id
    model_dir.mkdir(exist_ok=True)
    onnx_filename = f"{model_id}.onnx"
    json_filename = f"{model_id}.onnx.json"

    logger.info(f"Downloading ONNX model from {onnx_url}")
    if not download_file(onnx_url, model_dir, onnx_filename, progress_callback):
        return
        
    logger.info(f"Downloading model config from {json_url}")
    # No progress needed for the small JSON file
    def no_op_callback(*args, **kwargs): pass
    if not download_file(json_url, model_dir, json_filename, no_op_callback):
        progress_callback("error", message="Failed to download model config.")
        return

    logger.info(f"Successfully downloaded all files for TTS model: {model_id}")

def delete_model(model_id: str):
    """Deletes a local TTS model directory."""
    try:
        model_path = TTS_MODELS_PATH / model_id
        if model_path.exists() and model_path.is_dir():
            shutil.rmtree(model_path)
            logger.info(f"Successfully deleted model: {model_id}")
            return True
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
llama-cpp-python
huggingface-hub
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

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from corvus_app.crash_handler import format_crash_report

VENV_DIR = PROJECT_ROOT / "venv"
MARKER_FILE = VENV_DIR / "deps_installed.marker"

if sys.platform == "win32":
    VENV_PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    VENV_PYTHON = VENV_DIR / "bin" / "python"

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
    try:
        # This module is needed to run the installer itself.
        from installer.installer_tui import InstallerApp
    except ImportError as e:
        print(f"[LAUNCHER] A module needed for the installer is missing: {e}")
        print("[LAUNCHER] This can happen on a fresh clone. Attempting to install 'textual'...")
        try:
            # Use the system's Python to install Textual just for the installer.
            # The installer will then handle all dependencies for the venv.
            subprocess.check_call([sys.executable, "-m", "pip", "install", "textual"])
            print("\n[LAUNCHER] Textual installed. Please re-run the startup script to launch the installer.")
        except subprocess.CalledProcessError as install_error:
            print(f"\n[FATAL] Could not install Textual automatically. Error: {install_error}")
            print("Please install it manually by running: pip install textual")
        return False
        
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
    "active_llm_model": "mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    "active_tts_model": null,
    "active_stt_model": "base",
    "wake_word": "Corvus",
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