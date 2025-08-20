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
│   ├── tts
│   │   ├── __init__.py
│   │   └── tts_engine.py
│   ├── ui
│   │   ├── screens
│   │   │   ├── __init__.py
│   │   │   ├── conversation_screen.py
│   │   │   └── models_screen.py
│   │   ├── __init__.py
│   │   ├── shared.py
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
├── installer.log
├── README.md
├── requirements.txt
├── run.py
├── settings.json
├── start.bat
└── start.sh
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

:: Immediately change to the project's root directory.
:: This is critical for all subsequent delete commands to work correctly.
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

:: Use the robust 'choice' command for user input. It doesn't require pressing Enter.
choice /c YN /m "This action will perform a full factory reset. Are you sure?"

:: The 'choice' command sets the ERRORLEVEL variable based on the key pressed.
:: 1 for the first option (Y), 2 for the second (N).
:: We MUST check for the higher number first.
if %errorlevel% == 2 goto :user_cancelled

:: If the user pressed Y, the script just continues from here without any complex jumps.
echo.
echo [INFO] User confirmed. Starting aggressive project cleanup in directory: '%cd%'
echo.

echo [Step 1/9] Deleting Python virtual environment ('venv')...
if exist "venv" (
    if exist "venv\deps_installed.marker" ( del /f /q "venv\deps_installed.marker" >nul 2>nul )
    rmdir /s /q venv
    if exist "venv" (
        echo [ERROR] Failed to completely delete 'venv'. It might be in use. Please close terminals or editors and re-run.
    ) else (
        echo [INFO] 'venv' directory successfully deleted.
    )
) else (
    echo [INFO] 'venv' directory not found, skipping.
)

echo [Step 2/9] Deleting all downloaded AI models...
if exist "llm_models" ( rmdir /s /q llm_models )
if exist "tts_models" ( rmdir /s /q tts_models )
echo [INFO] Model directories cleared.

echo [Step 3/9] Deleting all logs, settings, and temporary files...
del /q /f .env settings.json *.log corvus_crash_report.log pip_install.log output.wav >nul 2>nul
echo [INFO] Log and settings files cleared.

echo [Step 4/9] Deleting __pycache__ folders...
for /d /r . %%d in (__pycache__) do ( if exist "%%d" rmdir /s /q "%%d" )
echo [INFO] __pycache__ folders cleared.

echo [Step 5/9] Deleting old/obsolete root files...
del /q /f assistant.py config.py logging_config.py main.py tui.css installer_tui.py app_settings.py >nul 2>nul

echo [Step 6/9] Deleting old 'assistant_app' source folder...
if exist "assistant_app" ( rmdir /s /q assistant_app )

echo [Step 7/9] Deleting old top-level UI/TTS folders...
if exist "ui" ( rmdir /s /q ui )
if exist "tts" ( rmdir /s /q tts )

echo [Step 8/9] Deleting obsolete internal 'screens' folder...
if exist "corvus_app\screens" ( rmdir /s /q "corvus_app\screens" )

echo [Step 9/9] Deleting obsolete settings screen file...
del /q /f "corvus_app\ui\screens\settings_screen.py" >nul 2>nul
echo [INFO] Obsolete files and folders cleared.

echo.
echo ============================================================================
echo [SUCCESS] Aggressive cleanup is complete.
echo Your source code is intact. You can now run 'start.bat' for a fresh installation.
echo ============================================================================
echo.
goto :end


:user_cancelled
echo.
echo Cleanup cancelled by user.
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

echo "[1/9] Deleting Python virtual environment ('venv')..."
rm -rf venv

echo "[2/9] Deleting all downloaded AI models..."
rm -rf llm_models tts_models

echo "[3/9] Deleting all logs, settings, and temporary files..."
rm -f .env settings.json *.log corvus_crash_report.log pip_install.log output.wav

echo "[4/9] Deleting __pycache__ folders..."
find . -type d -name "__pycache__" -exec rm -rf {} +

echo "[5/9] Deleting old/obsolete root files from previous structures..."
rm -f assistant.py config.py logging_config.py main.py tui.css installer_tui.py app_settings.py

echo "[6/9] Deleting old 'assistant_app' source folder if it exists..."
rm -rf assistant_app

echo "[7/9] Deleting old top-level UI/TTS folders if they exist..."
rm -rf ui tts

echo "[8/9] Deleting obsolete internal 'screens' folder..."
rm -rf corvus_app/screens

echo "[9/9] Deleting obsolete settings screen file..."
rm -f corvus_app/ui/screens/settings_screen.py

echo ""
echo "============================================================================"
echo "[SUCCESS] Aggressive cleanup is complete."
echo "Your source code is intact. You can now run './start.sh' for a fresh installation."
echo ""```

### File: /corvus_app/ui/screens/conversation_screen.py
```

### File: `/corvus_app.log`
```log
2025-08-05 17:51:31,306 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-05 17:51:31,307 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_app.log'. Log Level: INFO
2025-08-05 17:51:31,307 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-05 17:51:31,307 [MainThread  ] [__main__                 ] [INFO    ]  Corvus application starting up.
2025-08-05 17:52:07,659 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Initializing Assistant...
2025-08-05 17:52:07,660 [MainThread  ] [plugins.registry         ] [INFO    ]  Initializing CommandRegistry, scanning 'plugins' for plugins.
2025-08-05 17:52:07,676 [MainThread  ] [plugins.registry         ] [INFO    ]  Discovered and loaded 2 command(s).
2025-08-05 17:52:07,676 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected. LLM client not loaded.
2025-08-05 17:52:08,406 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:52:17,096 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:52:18,269 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'like map satur'
2025-08-05 17:52:18,872 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:52:21,852 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:52:22,794 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:52:34,824 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:52:36,465 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'how to fuk'
2025-08-05 17:52:37,058 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:52:42,058 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:52:43,231 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:52:49,462 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:52:51,007 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:52:57,697 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:52:59,016 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:03,686 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:04,819 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:15,019 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:16,970 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:20,480 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:21,531 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'no the party'
2025-08-05 17:53:22,134 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:25,184 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:26,605 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:32,155 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:33,500 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:37,080 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:38,614 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:44,004 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:45,367 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:53:52,657 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:53:53,642 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'try try'
2025-08-05 17:53:54,245 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:02,355 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:03,845 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:07,915 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:09,519 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:20,089 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:22,899 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:28,869 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:30,219 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:34,909 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:36,071 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:42,551 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:43,725 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'Nino's supposed to be out'
2025-08-05 17:54:44,327 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:50,507 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:51,877 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:54:57,197 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:54:58,488 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:02,628 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:03,752 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:16,412 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:18,094 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:30,775 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:32,115 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'ornaments'
2025-08-05 17:55:32,715 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:35,806 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:36,931 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:42,161 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:43,439 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:46,759 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:47,962 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:51,522 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:52,774 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:55:55,864 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:55:57,002 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:00,932 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:02,582 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:06,342 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:07,688 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:13,058 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:14,787 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:19,546 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:20,800 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:24,821 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:25,997 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:31,527 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:32,742 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:38,504 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:40,575 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:48,075 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:49,742 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:56:56,273 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:56:57,937 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:04,098 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:05,284 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:10,762 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:12,032 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:22,372 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:23,749 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'very clear that'
2025-08-05 17:57:24,351 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:32,901 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:34,986 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:40,466 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:41,517 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:47,277 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:48,584 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:57:54,185 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:57:55,070 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognized text: 'oh my god yeah Jesus'
2025-08-05 17:57:55,677 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:00,767 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:58:02,325 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:14,445 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:58:16,084 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:27,164 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:58:28,975 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:34,135 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:58:35,423 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:46,312 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:58:47,789 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:49,788 [asyncio_1   ] [models.tts_manager       ] [ERROR   ]  Could not fetch remote TTS model list: [Errno 13] Permission denied: 'C:/Users/gike5/Desktop/AI_Python/Corvus/tts_models'
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\models\tts_manager.py", line 25, in get_remote_models_list
    manager = get_model_manager()
              ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\models\tts_manager.py", line 19, in get_model_manager
    _model_manager = ModelManager(TTS_MODELS_PATH)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\TTS\utils\manage.py", line 56, in __init__
    self.read_models_file(models_file)
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\TTS\utils\manage.py", line 68, in read_models_file
    self.models_dict = read_json_with_comments(file_path)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\TTS\config\__init__.py", line 17, in read_json_with_comments
    with fsspec.open(json_path, "r", encoding="utf-8") as f:
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\fsspec\core.py", line 105, in __enter__
    f = self.fs.open(self.path, mode=mode)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\fsspec\spec.py", line 1338, in open
    f = self._open(
        ^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\fsspec\implementations\local.py", line 210, in _open
    return LocalFileOpener(path, mode, fs=self, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\fsspec\implementations\local.py", line 387, in __init__
    self._open()
  File "C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Lib\site-packages\fsspec\implementations\local.py", line 392, in _open
    self.f = open(self.path, mode=self.mode)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PermissionError: [Errno 13] Permission denied: 'C:/Users/gike5/Desktop/AI_Python/Corvus/tts_models'
2025-08-05 17:58:53,240 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:58:54,483 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:58:59,937 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:03,019 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:10,219 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:11,925 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:16,475 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:17,505 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:25,515 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:29,305 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:30,544 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:43,854 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:45,900 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:51,170 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:52,758 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 17:59:56,338 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 17:59:58,037 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 18:00:10,048 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Recognizing speech...
2025-08-05 18:00:13,436 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...
2025-08-05 20:51:10,559 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-05 20:51:10,559 [MainThread  ] [root                     ] [INFO    ]  Logging configured for 'corvus_app.log'. Log Level: INFO
2025-08-05 20:51:10,559 [MainThread  ] [root                     ] [INFO    ]  ============================================================
2025-08-05 20:51:10,559 [MainThread  ] [__main__                 ] [INFO    ]  Corvus application starting up.
2025-08-05 20:51:16,694 [MainThread  ] [corvus_app.assistant     ] [INFO    ]  Initializing Assistant...
2025-08-05 20:51:16,694 [MainThread  ] [plugins.registry         ] [INFO    ]  Initializing CommandRegistry, scanning 'plugins' for plugins.
2025-08-05 20:51:16,695 [MainThread  ] [plugins.registry         ] [INFO    ]  Discovered and loaded 2 command(s).
2025-08-05 20:51:16,695 [MainThread  ] [corvus_app.llm.llm_client] [WARNING ]  No active LLM model selected. LLM client not loaded.
2025-08-05 20:51:17,345 [asyncio_0   ] [corvus_app.audio.stt     ] [INFO    ]  Listening for wake word or command...

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
            "active_tts_model": "tts_models/en/ljspeech/vits",
            "wake_word": DEFAULT_WAKE_WORD,
            "system_prompt": "You are a helpful assistant."
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
        
        # Fetch the system prompt dynamically from settings
        system_prompt = settings_manager.get("system_prompt")
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

# Must be imported before other app components
from corvus_app.crash_handler import format_crash_report

_console = Console()

def bootstrap():
    """Initial setup for directories and logging."""
    try:
        Path("tts_models").mkdir(exist_ok=True)
        Path("llm_models").mkdir(exist_ok=True)
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
from textual.widgets import Header, Footer, Input, ListView, Button, Static

from corvus_app.app_settings import settings_manager
from corvus_app.assistant import Assistant
from corvus_app.audio.stt import listen_for_audio
from corvus_app.tts.tts_engine import speak_text
from corvus_app.ui.shared import AssistantResponse, StatusUpdate, ConversationListItem

logger = logging.getLogger(__name__)

class ConversationScreen(Screen):
    BINDINGS = [("tab", "toggle_input_mode", "Toggle Input")]
    
    def __init__(self, assistant: Assistant, **kwargs):
        super().__init__(**kwargs)
        self.assistant = assistant
        self.input_mode = "voice"

    def compose(self) -> ComposeResult:
        # This declarative layout is stable and correct.
        with Header():
            yield Static("Corvus Assistant", id="header-title")
            yield Button("Models & Settings", id="models-button")
        
        yield ScrollableContainer(ListView(id="conversation"), id="conversation-container")
        yield Input(placeholder="Type your message...", id="text-input")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(Input).display = False
        self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")

    def listen_for_wake_word(self):
        self.app.post_message(StatusUpdate("LISTENING..."))
        wake_word = settings_manager.get("wake_word").lower()
        
        while self.input_mode == "voice" and self.assistant.is_running:
            text = listen_for_audio()
            if text and wake_word in text:
                prompt = text.replace(wake_word, "", 1).strip()
                if prompt:
                    self.app.post_message(StatusUpdate("PROCESSING..."))
                    self.run_worker(lambda: self.process_prompt(prompt), thread=True, exclusive=True, group="processing")
                else:
                    self.app.post_message(StatusUpdate("Yes?"))
                    self.run_worker(lambda: self.speak_and_reset_status("Yes?"), thread=True, exclusive=True, group="audio_output")
                return

    def process_prompt(self, prompt: str):
        response = self.assistant.process_prompt(prompt)
        self.post_message(AssistantResponse(response, prompt))
        if not self.assistant.is_running:
            self.app.call_from_thread(self.app.exit)
        else:
            self.run_worker(lambda: self.speak_and_reset_status(response), thread=True, exclusive=True, group="audio_output")

    def speak_and_reset_status(self, text: str):
        speak_text(text)
        if self.input_mode == "voice":
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")
        else:
            self.app.post_message(StatusUpdate("TYPING..."))
    
    def action_toggle_input_mode(self) -> None:
        text_input = self.query_one(Input)
        if self.input_mode == "voice":
            self.input_mode = "text"
            text_input.display = True
            text_input.focus()
            self.app.workers.cancel_group(self, "audio_input")
            self.post_message(StatusUpdate("TYPING..."))
        else:
            self.input_mode = "voice"
            text_input.display = False
            self.run_worker(self.listen_for_wake_word, thread=True, exclusive=True, group="audio_input")

    async def on_button_pressed(self, message: Button.Pressed) -> None:
        if message.button.id == "models-button":
            self.app.action_toggle_models_screen()
            
    async def on_input_submitted(self, message: Input.Submitted) -> None:
        prompt = message.value
        if prompt:
            message.input.value = ""
            self.post_message(StatusUpdate("PROCESSING..."))
            self.run_worker(lambda: self.process_prompt(prompt), thread=True, exclusive=True, group="processing")
        self.set_focus(None)
        self.action_toggle_input_mode()

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
from textual.widgets import Header, Footer, DataTable, Input, Button, Static, Label, ProgressBar

from corvus_app.app_settings import settings_manager
from models import llm_manager, tts_manager, hf_utils

logger = logging.getLogger(__name__)

# Pre-defined list of recommended models for easy setup
RECOMMENDED_MODELS = [
    {
        "name": "StableLM-Zephyr-3B (Fast & Light)",
        "vram": "~3-4 GB",
        "filename": "stablelm-zephyr-3b.Q5_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/resolve/main/stablelm-zephyr-3b.Q5_K_M.gguf",
    },
    {
        "name": "Phi-3-Mini-4k-Instruct (Smart & Small)",
        "vram": "~4-5 GB",
        "filename": "phi-3-mini-4k-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Phi-3-mini-4k-instruct-GGUF/resolve/main/phi-3-mini-4k-instruct.Q4_K_M.gguf",
    },
    {
        "name": "Llama-2-7B-Chat (Balanced)",
        "vram": "~5-6 GB",
        "filename": "llama-2-7b-chat.Q5_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf",
    },
    {
        "name": "Llama-2-7B-Chat (High Quality)",
        "vram": "~8-9 GB",
        "filename": "llama-2-7b-chat.Q8_0.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q8_0.gguf",
    },
    {
        "name": "Llama-2-13B-Chat (Powerful)",
        "vram": "~9-10 GB",
        "filename": "llama-2-13b-chat.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-2-13B-Chat-GGUF/resolve/main/llama-2-13b-chat.Q4_K_M.gguf",
    }
]


class ModelsScreen(Screen):
    BINDINGS = [
        ("d", "download_selected", "Download"),
        ("s", "set_active", "Set Active"),
        ("delete", "delete_selected", "Delete Selected"),
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # WORKAROUND: Store keys manually for compatibility with Textual v0.58.0
        self.recommended_keys = []
        self.hf_keys = []
        self.llm_keys = []
        self.tts_local_keys = []
        self.tts_remote_keys = []


    def compose(self) -> ComposeResult:
        yield Header()
        with ScrollableContainer():
            # --- General Settings ---
            yield Static("General Settings", classes="title")
            with Vertical(id="settings-box"):
                yield Label("Wake Word")
                yield Input(id="wake-word-input", placeholder="e.g., computer")
                yield Label("Assistant Personality (System Prompt)")
                yield Input(id="system-prompt-input", placeholder="You are a helpful assistant.")
                yield Button("Save General Settings", variant="success", id="save-settings-button")
                yield Static("", id="save-status-message")

            # --- Recommended Models ---
            yield Static("Recommended Models (Press 'D' to Download)", classes="title")
            yield DataTable(id="recommended-table", cursor_type="row", classes="model_table")

            # --- Custom LLM Models ---
            yield Static("LLM Models - Find Custom", classes="title")
            with Horizontal(classes="input_bar"):
                yield Input(placeholder="HuggingFace Repo (e.g., TheBloke/Mistral-7B-Instruct-v0.2-GGUF)", id="hf-repo-input")
                yield Button("Fetch Files", id="hf-fetch-button")
            yield DataTable(id="hf-files-table", cursor_type="row", classes="model_table")
            
            yield Static("LLM Models - Local", classes="title")
            yield DataTable(id="llm-table", cursor_type="row", classes="model_table")

            # --- TTS Models ---
            yield Static("TTS Models - Local", classes="title")
            yield DataTable(id="tts-local-table", cursor_type="row", classes="model_table")

            yield Static("TTS Models - Remote (Coqui)", classes="title")
            yield DataTable(id="tts-remote-table", cursor_type="row", classes="model_table")
        
        with Footer():
            yield Button("Close", id="close-settings-button", variant="error")

    def on_mount(self) -> None:
        self.query_one("#recommended-table").add_columns("Model Name", "VRAM (Est.)", "Filename")
        self.query_one("#hf-files-table").add_columns("GGUF File", "URL")
        self.query_one("#llm-table").add_columns("Filename", "Path", "Status")
        self.query_one("#tts-local-table").add_columns("Local TTS Model", "Status")
        self.query_one("#tts-remote-table").add_columns("Available TTS Model")
        
        self.populate_recommended_models()
        self.load_settings()
        self.update_llm_table()
        self.update_tts_tables()
        self.run_worker(self.fetch_remote_tts_models, thread=True)
    
    def populate_recommended_models(self):
        table = self.query_one("#recommended-table")
        self.recommended_keys.clear()
        for model in RECOMMENDED_MODELS:
            key = (model["url"], model["filename"])
            self.recommended_keys.append(key)
            table.add_row(model["name"], model["vram"], model["filename"], key=key)

    def load_settings(self):
        self.query_one("#wake-word-input", Input).value = settings_manager.get("wake_word")
        self.query_one("#system-prompt-input", Input).value = settings_manager.get("system_prompt")

    def update_llm_table(self):
        table = self.query_one("#llm-table", DataTable)
        table.clear()
        self.llm_keys.clear()
        local_models = llm_manager.get_local_models()
        active_model = settings_manager.get("active_llm_model")
        for model_path in sorted(local_models):
            status = "[bold green](Active)[/]" if str(model_path) == active_model else ""
            key = str(model_path)
            self.llm_keys.append(key)
            table.add_row(model_path.name, str(model_path), status, key=key)

    def update_tts_tables(self):
        table = self.query_one("#tts-local-table", DataTable)
        table.clear()
        self.tts_local_keys.clear()
        local_models = tts_manager.get_local_models_list()
        active_model = settings_manager.get("active_tts_model")
        for model_name in sorted(local_models):
            status = "[bold green](Active)[/]" if model_name == active_model else ""
            self.tts_local_keys.append(model_name)
            table.add_row(model_name, status, key=model_name)

    def fetch_hf_files(self, repo_id: str):
        table = self.query_one("#hf-files-table")
        self.app.call_from_thread(table.clear)
        self.app.call_from_thread(self.hf_keys.clear)
        self.app.call_from_thread(setattr, table, 'loading', True)
        files = hf_utils.list_gguf_files_from_repo(repo_id)
        self.app.call_from_thread(setattr, table, 'loading', False)
        if files:
            for f in files:
                key = f['url']
                self.app.call_from_thread(self.hf_keys.append, key)
                self.app.call_from_thread(table.add_row, f['filename'], f['url'], key=key)
        else:
            self.app.call_from_thread(table.add_row, "[red]No GGUF files found or repo is invalid.[/red]", "")
            
    def fetch_remote_tts_models(self):
        table = self.query_one("#tts-remote-table")
        self.app.call_from_thread(table.clear)
        self.app.call_from_thread(self.tts_remote_keys.clear)
        self.app.call_from_thread(setattr, table, 'loading', True)
        models = tts_manager.get_remote_models_list()
        self.app.call_from_thread(setattr, table, 'loading', False)
        if models:
            for model_name in models:
                self.app.call_from_thread(self.tts_remote_keys.append, model_name)
                self.app.call_from_thread(table.add_row, model_name, key=model_name)
        else:
            self.app.call_from_thread(table.add_row, "[red]Could not retrieve remote TTS models.[/red]")

    async def on_button_pressed(self, message: Button.Pressed):
        if message.button.id == "hf-fetch-button":
            repo_id = self.query_one("#hf-repo-input", Input).value
            if repo_id:
                self.run_worker(lambda: self.fetch_hf_files(repo_id), thread=True)
        elif message.button.id == "save-settings-button":
            wake_word = self.query_one("#wake-word-input", Input).value
            system_prompt = self.query_one("#system-prompt-input", Input).value
            settings_manager.set("wake_word", wake_word)
            settings_manager.set("system_prompt", system_prompt)
            status_msg = self.query_one("#save-status-message")
            status_msg.update("[green]Settings saved successfully.[/green]")
            async def clear_message():
                import asyncio
                await asyncio.sleep(3)
                status_msg.update("")
            self.run_worker(clear_message)
        elif message.button.id == "close-settings-button":
            self.app.action_toggle_models_screen()

    def action_download_selected(self) -> None:
        rec_table = self.query_one("#recommended-table")
        hf_table = self.query_one("#hf-files-table")
        tts_table = self.query_one("#tts-remote-table")
        try:
            if rec_table.has_focus and rec_table.row_count > 0:
                row_key = self.recommended_keys[rec_table.cursor_row]
                if row_key:
                    url, filename = row_key
                    self.app.push_screen(DownloadScreen(url=url, filename=filename))
            elif hf_table.has_focus and hf_table.row_count > 0:
                row_key = self.hf_keys[hf_table.cursor_row]
                filename = hf_table.get_cell_at((hf_table.cursor_row, 0))
                if row_key and filename: self.app.push_screen(DownloadScreen(url=row_key, filename=filename))
            elif tts_table.has_focus and tts_table.row_count > 0:
                model_name = self.tts_remote_keys[tts_table.cursor_row]
                if model_name: self.app.push_screen(TTSDownloadScreen(model_name=model_name))
        except IndexError: 
            logger.warning("Download triggered with no row selected or table is empty.")

    def action_delete_selected(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus and llm_table.row_count > 0:
                filepath = self.llm_keys[llm_table.cursor_row]
                if filepath and llm_manager.delete_model(filepath):
                    if settings_manager.get("active_llm_model") == filepath: settings_manager.set("active_llm_model", None)
                    self.update_llm_table()
            elif tts_table.has_focus and tts_table.row_count > 0:
                model_name = self.tts_local_keys[tts_table.cursor_row]
                if model_name and tts_manager.delete_model(model_name):
                    if settings_manager.get("active_tts_model") == model_name: settings_manager.set("active_tts_model", "tts_models/en/ljspeech/vits")
                    self.update_tts_tables()
        except IndexError: 
            logger.warning("Delete triggered with no row selected or table is empty.")

    def action_set_active(self) -> None:
        llm_table = self.query_one("#llm-table")
        tts_table = self.query_one("#tts-local-table")
        try:
            if llm_table.has_focus and llm_table.row_count > 0:
                row_key = self.llm_keys[llm_table.cursor_row]
                if row_key: settings_manager.set("active_llm_model", row_key)
                self.update_llm_table()
            elif tts_table.has_focus and tts_table.row_count > 0:
                row_key = self.tts_local_keys[tts_table.cursor_row]
                if row_key: settings_manager.set("active_tts_model", row_key)
                self.update_tts_tables()
        except IndexError: 
            logger.warning(f"Set Active triggered with no row selected or table is empty.")

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
        self.app.call_from_thread(update_ui)

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
        self.app.call_from_thread(update_ui)
    
    def download_tts_model(self) -> None: tts_manager.download_model(self.model_name, self.on_download_finished)
```

### File: `/corvus_app/ui/shared.py`
```py
# corvus_app/ui/shared.py
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
    layout: horizontal;
    align: center middle;
}

#header-title {
    width: 1fr;
    content-align: left middle;
    margin-left: 1;
}

#models-button {
    dock: right;
    width: auto;
    height: 1;
    min-width: 20;
    border: none;
    background: $accent;
}

#models-button:hover {
    background: $accent-darken-1;
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
    height: 1fr; /* This is the flexible part that fills space */
    padding: 1;
}

#text-input {
    dock: bottom;
    height: 3;
    border-top: tall $accent;
}

/* General Title Style */
.title {
    background: $primary-background-darken-2;
    padding: 1;
    text-align: center;
    text-style: bold;
    margin-top: 1;
    margin-bottom: 1;
}

/* Models & Settings Screen */
#settings-box {
    border: round $primary;
    padding: 1;
    margin: 0 2 1 2;
    height: auto;
}

#settings-box Label {
    margin-top: 1;
    margin-bottom: 1;
    text-style: bold;
}

#save-settings-button {
    width: 100%;
    margin-top: 1;
}

#save-status-message {
    margin-top: 1;
    text-align: center;
    height: 1;
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
    height: 8;
    margin-bottom: 1;
    border: tall $primary-darken-2;
}

#close-settings-button {
    width: 100%;
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
from pathlib import Path
from textual.app import App

from corvus_app.assistant import Assistant
from corvus_app.ui.screens.conversation_screen import ConversationScreen
from corvus_app.ui.screens.models_screen import ModelsScreen
from corvus_app.ui.shared import AssistantResponse, StatusUpdate

logger = logging.getLogger(__name__)

class CorvusTUI(App):
    """The main Textual application for Corvus."""
    # The title will now be set by the CustomHeader, so we can clear it here.
    TITLE = ""
    CSS_PATH = Path(__file__).parent / "tui.css"
    SCREENS = {
        "models": ModelsScreen,
    }
    BINDINGS = [
        ("ctrl+c", "request_quit", "Quit"),
        ("ctrl+m", "toggle_models_screen", "Models Menu"),
    ]

    def __init__(self):
        super().__init__()
        self.assistant = Assistant()

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        self.push_screen(ConversationScreen(assistant=self.assistant))

    def action_toggle_models_screen(self) -> None:
        """Toggles the visibility of the Models & Settings screen."""
        if isinstance(self.screen, ModelsScreen):
            self.pop_screen()
            logger.info("Closing models screen, reloading components.")
            # Reload assistant and TTS engine in case models were changed
            self.assistant.reload()
            from corvus_app.tts.tts_engine import TTSEngine
            TTSEngine().reload_model()
        else:
            self.push_screen("models")
    
    async def on_assistant_response(self, message: AssistantResponse) -> None:
        """Handles the AssistantResponse message event."""
        if isinstance(self.screen, ConversationScreen):
            await self.screen.on_assistant_response(message)
    
    async def on_status_update(self, message: StatusUpdate) -> None:
        """Handles the StatusUpdate message event."""
        if isinstance(self.screen, ConversationScreen):
            await self.screen.on_status_update(message)
```

### File: `/installer.log`
```log
2025-08-05 17:46:55,879 [INFO    ]  Virtual environment is missing or incomplete. Recreating...
2025-08-05 17:47:07,188 [INFO    ]  Virtual environment created successfully.
2025-08-05 17:47:07,189 [INFO    ]  Installing dependencies (this may take several minutes)...
2025-08-05 17:47:07,193 [INFO    ]  Running command: C:\Users\gike5\Desktop\AI_Python\Corvus\venv\Scripts\python.exe -m pip install -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt
2025-08-05 17:51:30,456 [INFO    ]  Collecting llama-cpp-python (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1))
2025-08-05 17:51:30,462 [INFO    ]    Using cached llama_cpp_python-0.3.14-cp311-cp311-win_amd64.whl
2025-08-05 17:51:30,465 [INFO    ]  Collecting SpeechRecognition (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 2))
2025-08-05 17:51:30,465 [INFO    ]    Using cached speechrecognition-3.14.3-py3-none-any.whl.metadata (30 kB)
2025-08-05 17:51:30,466 [INFO    ]  Collecting PyAudio (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 3))
2025-08-05 17:51:30,467 [INFO    ]    Using cached PyAudio-0.2.14-cp311-cp311-win_amd64.whl.metadata (2.7 kB)
2025-08-05 17:51:30,468 [INFO    ]  Collecting rich (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 4))
2025-08-05 17:51:30,468 [INFO    ]    Using cached rich-14.1.0-py3-none-any.whl.metadata (18 kB)
2025-08-05 17:51:30,469 [INFO    ]  Collecting python-dotenv (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 5))
2025-08-05 17:51:30,469 [INFO    ]    Using cached python_dotenv-1.1.1-py3-none-any.whl.metadata (24 kB)
2025-08-05 17:51:30,470 [INFO    ]  Collecting textual==0.58.0 (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,471 [INFO    ]    Using cached textual-0.58.0-py3-none-any.whl.metadata (5.6 kB)
2025-08-05 17:51:30,471 [INFO    ]  Collecting TTS (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,472 [INFO    ]    Using cached tts-0.22.0-cp311-cp311-win_amd64.whl
2025-08-05 17:51:30,472 [INFO    ]  Collecting requests (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8))
2025-08-05 17:51:30,474 [INFO    ]    Using cached requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
2025-08-05 17:51:30,474 [INFO    ]  Collecting beautifulsoup4 (from -r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9))
2025-08-05 17:51:30,474 [INFO    ]    Using cached beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)
2025-08-05 17:51:30,476 [INFO    ]  Collecting markdown-it-py>=2.1.0 (from markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,481 [INFO    ]    Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
2025-08-05 17:51:30,482 [INFO    ]  Collecting typing-extensions<5.0.0,>=4.4.0 (from textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,483 [INFO    ]    Using cached typing_extensions-4.14.1-py3-none-any.whl.metadata (3.0 kB)
2025-08-05 17:51:30,483 [INFO    ]  Collecting numpy>=1.20.0 (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1))
2025-08-05 17:51:30,484 [INFO    ]    Using cached numpy-2.3.2-cp311-cp311-win_amd64.whl.metadata (60 kB)
2025-08-05 17:51:30,485 [INFO    ]  Collecting diskcache>=5.6.1 (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1))
2025-08-05 17:51:30,485 [INFO    ]    Using cached diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
2025-08-05 17:51:30,486 [INFO    ]  Collecting jinja2>=2.11.3 (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1))
2025-08-05 17:51:30,487 [INFO    ]    Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
2025-08-05 17:51:30,487 [INFO    ]  Collecting pygments<3.0.0,>=2.13.0 (from rich->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 4))
2025-08-05 17:51:30,488 [INFO    ]    Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
2025-08-05 17:51:30,489 [INFO    ]  Collecting cython>=0.29.30 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,489 [INFO    ]    Using cached cython-3.1.2-cp311-cp311-win_amd64.whl.metadata (6.0 kB)
2025-08-05 17:51:30,490 [INFO    ]  Collecting scipy>=1.11.2 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,491 [INFO    ]    Using cached scipy-1.16.1-cp311-cp311-win_amd64.whl.metadata (60 kB)
2025-08-05 17:51:30,491 [INFO    ]  Collecting torch>=2.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,492 [INFO    ]    Using cached torch-2.7.1-cp311-cp311-win_amd64.whl.metadata (28 kB)
2025-08-05 17:51:30,497 [INFO    ]  Collecting torchaudio (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,498 [INFO    ]    Using cached torchaudio-2.7.1-cp311-cp311-win_amd64.whl.metadata (6.6 kB)
2025-08-05 17:51:30,499 [INFO    ]  Collecting soundfile>=0.12.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,499 [INFO    ]    Using cached soundfile-0.13.1-py2.py3-none-win_amd64.whl.metadata (16 kB)
2025-08-05 17:51:30,500 [INFO    ]  Collecting librosa>=0.10.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,501 [INFO    ]    Using cached librosa-0.11.0-py3-none-any.whl.metadata (8.7 kB)
2025-08-05 17:51:30,501 [INFO    ]  Collecting scikit-learn>=1.3.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,502 [INFO    ]    Using cached scikit_learn-1.7.1-cp311-cp311-win_amd64.whl.metadata (11 kB)
2025-08-05 17:51:30,502 [INFO    ]  Collecting numba>=0.57.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,504 [INFO    ]    Using cached numba-0.61.2-cp311-cp311-win_amd64.whl.metadata (2.9 kB)
2025-08-05 17:51:30,504 [INFO    ]  Collecting inflect>=5.6.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,505 [INFO    ]    Using cached inflect-7.5.0-py3-none-any.whl.metadata (24 kB)
2025-08-05 17:51:30,506 [INFO    ]  Collecting tqdm>=4.64.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,506 [INFO    ]    Using cached tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
2025-08-05 17:51:30,507 [INFO    ]  Collecting anyascii>=0.3.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,508 [INFO    ]    Using cached anyascii-0.3.3-py3-none-any.whl.metadata (1.6 kB)
2025-08-05 17:51:30,508 [INFO    ]  Collecting pyyaml>=6.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,509 [INFO    ]    Using cached PyYAML-6.0.2-cp311-cp311-win_amd64.whl.metadata (2.1 kB)
2025-08-05 17:51:30,514 [INFO    ]  Collecting fsspec>=2023.6.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,514 [INFO    ]    Using cached fsspec-2025.7.0-py3-none-any.whl.metadata (12 kB)
2025-08-05 17:51:30,515 [INFO    ]  Collecting aiohttp>=3.8.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,516 [INFO    ]    Using cached aiohttp-3.12.15-cp311-cp311-win_amd64.whl.metadata (7.9 kB)
2025-08-05 17:51:30,516 [INFO    ]  Collecting packaging>=23.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,517 [INFO    ]    Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-08-05 17:51:30,518 [INFO    ]  Collecting flask>=2.0.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,518 [INFO    ]    Using cached flask-3.1.1-py3-none-any.whl.metadata (3.0 kB)
2025-08-05 17:51:30,519 [INFO    ]  Collecting pysbd>=0.3.4 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,521 [INFO    ]    Using cached pysbd-0.3.4-py3-none-any.whl.metadata (6.1 kB)
2025-08-05 17:51:30,521 [INFO    ]  Collecting umap-learn>=0.5.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,522 [INFO    ]    Using cached umap_learn-0.5.9.post2-py3-none-any.whl.metadata (25 kB)
2025-08-05 17:51:30,522 [INFO    ]  Collecting pandas<2.0,>=1.4 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,523 [INFO    ]    Using cached pandas-1.5.3-cp311-cp311-win_amd64.whl.metadata (12 kB)
2025-08-05 17:51:30,524 [INFO    ]  Collecting matplotlib>=3.7.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,524 [INFO    ]    Using cached matplotlib-3.10.5-cp311-cp311-win_amd64.whl.metadata (11 kB)
2025-08-05 17:51:30,525 [INFO    ]  Collecting trainer>=0.0.32 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,530 [INFO    ]    Using cached trainer-0.0.36-py3-none-any.whl.metadata (8.1 kB)
2025-08-05 17:51:30,531 [INFO    ]  Collecting coqpit>=0.0.16 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,532 [INFO    ]    Using cached coqpit-0.0.17-py3-none-any.whl.metadata (11 kB)
2025-08-05 17:51:30,532 [INFO    ]  Collecting jieba (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,533 [INFO    ]    Using cached jieba-0.42.1-py3-none-any.whl
2025-08-05 17:51:30,534 [INFO    ]  Collecting pypinyin (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,535 [INFO    ]    Using cached pypinyin-0.55.0-py2.py3-none-any.whl.metadata (12 kB)
2025-08-05 17:51:30,535 [INFO    ]  Collecting hangul_romanize (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,536 [INFO    ]    Using cached hangul_romanize-0.1.0-py3-none-any.whl.metadata (1.2 kB)
2025-08-05 17:51:30,537 [INFO    ]  Collecting gruut==2.2.3 (from gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,538 [INFO    ]    Using cached gruut-2.2.3-py3-none-any.whl
2025-08-05 17:51:30,538 [INFO    ]  Collecting jamo (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,539 [INFO    ]    Using cached jamo-0.4.1-py3-none-any.whl.metadata (2.3 kB)
2025-08-05 17:51:30,539 [INFO    ]  Collecting nltk (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,540 [INFO    ]    Using cached nltk-3.9.1-py3-none-any.whl.metadata (2.9 kB)
2025-08-05 17:51:30,541 [INFO    ]  Collecting g2pkk>=0.1.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,541 [INFO    ]    Using cached g2pkk-0.1.2-py3-none-any.whl.metadata (2.0 kB)
2025-08-05 17:51:30,542 [INFO    ]  Collecting bangla (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,548 [INFO    ]    Using cached bangla-0.0.5-py3-none-any.whl.metadata (4.7 kB)
2025-08-05 17:51:30,548 [INFO    ]  Collecting bnnumerizer (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,549 [INFO    ]    Using cached bnnumerizer-0.0.2-py3-none-any.whl
2025-08-05 17:51:30,550 [INFO    ]  Collecting bnunicodenormalizer (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,550 [INFO    ]    Using cached bnunicodenormalizer-0.1.7-py3-none-any.whl.metadata (22 kB)
2025-08-05 17:51:30,551 [INFO    ]  Collecting einops>=0.6.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,552 [INFO    ]    Using cached einops-0.8.1-py3-none-any.whl.metadata (13 kB)
2025-08-05 17:51:30,552 [INFO    ]  Collecting transformers>=4.33.0 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,552 [INFO    ]    Using cached transformers-4.54.1-py3-none-any.whl.metadata (41 kB)
2025-08-05 17:51:30,553 [INFO    ]  Collecting encodec>=0.1.1 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,554 [INFO    ]    Using cached encodec-0.1.1-py3-none-any.whl
2025-08-05 17:51:30,554 [INFO    ]  Collecting unidecode>=1.3.2 (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,555 [INFO    ]    Using cached Unidecode-1.4.0-py3-none-any.whl.metadata (13 kB)
2025-08-05 17:51:30,556 [INFO    ]  Collecting num2words (from TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,556 [INFO    ]    Using cached num2words-0.5.14-py3-none-any.whl.metadata (13 kB)
2025-08-05 17:51:30,557 [INFO    ]  Collecting spacy>=3 (from spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,557 [INFO    ]    Using cached spacy-3.8.7-cp311-cp311-win_amd64.whl.metadata (28 kB)
2025-08-05 17:51:30,559 [INFO    ]  Collecting Babel<3.0.0,>=2.8.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,564 [INFO    ]    Using cached babel-2.17.0-py3-none-any.whl.metadata (2.0 kB)
2025-08-05 17:51:30,564 [INFO    ]  Collecting dateparser~=1.1.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,565 [INFO    ]    Using cached dateparser-1.1.8-py2.py3-none-any.whl.metadata (27 kB)
2025-08-05 17:51:30,566 [INFO    ]  Collecting gruut-ipa<1.0,>=0.12.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,567 [INFO    ]    Using cached gruut_ipa-0.13.0-py3-none-any.whl
2025-08-05 17:51:30,567 [INFO    ]  Collecting gruut_lang_en~=2.0.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,568 [INFO    ]    Using cached gruut_lang_en-2.0.1-py3-none-any.whl
2025-08-05 17:51:30,569 [INFO    ]  Collecting jsonlines~=1.2.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,570 [INFO    ]    Using cached jsonlines-1.2.0-py2.py3-none-any.whl.metadata (1.3 kB)
2025-08-05 17:51:30,570 [INFO    ]  Collecting networkx<3.0.0,>=2.5.0 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,571 [INFO    ]    Using cached networkx-2.8.8-py3-none-any.whl.metadata (5.1 kB)
2025-08-05 17:51:30,572 [INFO    ]  Collecting numpy>=1.20.0 (from llama-cpp-python->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 1))
2025-08-05 17:51:30,572 [INFO    ]    Using cached numpy-1.26.4-cp311-cp311-win_amd64.whl.metadata (61 kB)
2025-08-05 17:51:30,572 [INFO    ]  Collecting python-crfsuite~=0.9.7 (from gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,574 [INFO    ]    Using cached python_crfsuite-0.9.11-cp311-cp311-win_amd64.whl.metadata (4.4 kB)
2025-08-05 17:51:30,574 [INFO    ]  Collecting gruut_lang_de~=2.0.0 (from gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,574 [INFO    ]    Using cached gruut_lang_de-2.0.1-py3-none-any.whl
2025-08-05 17:51:30,580 [INFO    ]  Collecting gruut_lang_es~=2.0.0 (from gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,581 [INFO    ]    Using cached gruut_lang_es-2.0.1-py3-none-any.whl
2025-08-05 17:51:30,581 [INFO    ]  Collecting gruut_lang_fr~=2.0.0 (from gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,582 [INFO    ]    Using cached gruut_lang_fr-2.0.2-py3-none-any.whl
2025-08-05 17:51:30,583 [INFO    ]  Collecting charset_normalizer<4,>=2 (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8))
2025-08-05 17:51:30,583 [INFO    ]    Using cached charset_normalizer-3.4.2-cp311-cp311-win_amd64.whl.metadata (36 kB)
2025-08-05 17:51:30,583 [INFO    ]  Collecting idna<4,>=2.5 (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8))
2025-08-05 17:51:30,585 [INFO    ]    Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
2025-08-05 17:51:30,585 [INFO    ]  Collecting urllib3<3,>=1.21.1 (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8))
2025-08-05 17:51:30,586 [INFO    ]    Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
2025-08-05 17:51:30,587 [INFO    ]  Collecting certifi>=2017.4.17 (from requests->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 8))
2025-08-05 17:51:30,588 [INFO    ]    Using cached certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
2025-08-05 17:51:30,588 [INFO    ]  Collecting soupsieve>1.2 (from beautifulsoup4->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 9))
2025-08-05 17:51:30,589 [INFO    ]    Using cached soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)
2025-08-05 17:51:30,590 [INFO    ]  Collecting aiohappyeyeballs>=2.5.0 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,590 [INFO    ]    Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
2025-08-05 17:51:30,591 [INFO    ]  Collecting aiosignal>=1.4.0 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,591 [INFO    ]    Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
2025-08-05 17:51:30,592 [INFO    ]  Collecting attrs>=17.3.0 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,598 [INFO    ]    Using cached attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
2025-08-05 17:51:30,598 [INFO    ]  Collecting frozenlist>=1.1.1 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,599 [INFO    ]    Using cached frozenlist-1.7.0-cp311-cp311-win_amd64.whl.metadata (19 kB)
2025-08-05 17:51:30,599 [INFO    ]  Collecting multidict<7.0,>=4.5 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,600 [INFO    ]    Using cached multidict-6.6.3-cp311-cp311-win_amd64.whl.metadata (5.4 kB)
2025-08-05 17:51:30,601 [INFO    ]  Collecting propcache>=0.2.0 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,601 [INFO    ]    Using cached propcache-0.3.2-cp311-cp311-win_amd64.whl.metadata (12 kB)
2025-08-05 17:51:30,602 [INFO    ]  Collecting yarl<2.0,>=1.17.0 (from aiohttp>=3.8.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,603 [INFO    ]    Using cached yarl-1.20.1-cp311-cp311-win_amd64.whl.metadata (76 kB)
2025-08-05 17:51:30,603 [INFO    ]  Collecting blinker>=1.9.0 (from flask>=2.0.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,604 [INFO    ]    Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
2025-08-05 17:51:30,604 [INFO    ]  Collecting click>=8.1.3 (from flask>=2.0.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,605 [INFO    ]    Using cached click-8.2.1-py3-none-any.whl.metadata (2.5 kB)
2025-08-05 17:51:30,605 [INFO    ]  Collecting itsdangerous>=2.2.0 (from flask>=2.0.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,606 [INFO    ]    Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
2025-08-05 17:51:30,607 [INFO    ]  Collecting markupsafe>=2.1.1 (from flask>=2.0.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,607 [INFO    ]    Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
2025-08-05 17:51:30,607 [INFO    ]  Collecting werkzeug>=3.1.0 (from flask>=2.0.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,612 [INFO    ]    Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
2025-08-05 17:51:30,614 [INFO    ]  Collecting more_itertools>=8.5.0 (from inflect>=5.6.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,614 [INFO    ]    Using cached more_itertools-10.7.0-py3-none-any.whl.metadata (37 kB)
2025-08-05 17:51:30,615 [INFO    ]  Collecting typeguard>=4.0.1 (from inflect>=5.6.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,616 [INFO    ]    Using cached typeguard-4.4.4-py3-none-any.whl.metadata (3.3 kB)
2025-08-05 17:51:30,617 [INFO    ]  Collecting audioread>=2.1.9 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,617 [INFO    ]    Using cached audioread-3.0.1-py3-none-any.whl.metadata (8.4 kB)
2025-08-05 17:51:30,618 [INFO    ]  Collecting joblib>=1.0 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,619 [INFO    ]    Using cached joblib-1.5.1-py3-none-any.whl.metadata (5.6 kB)
2025-08-05 17:51:30,619 [INFO    ]  Collecting decorator>=4.3.0 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,620 [INFO    ]    Using cached decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
2025-08-05 17:51:30,621 [INFO    ]  Collecting pooch>=1.1 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,621 [INFO    ]    Using cached pooch-1.8.2-py3-none-any.whl.metadata (10 kB)
2025-08-05 17:51:30,622 [INFO    ]  Collecting soxr>=0.3.2 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,622 [INFO    ]    Using cached soxr-0.5.0.post1-cp311-cp311-win_amd64.whl.metadata (5.6 kB)
2025-08-05 17:51:30,624 [INFO    ]  Collecting lazy_loader>=0.1 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,624 [INFO    ]    Using cached lazy_loader-0.4-py3-none-any.whl.metadata (7.6 kB)
2025-08-05 17:51:30,625 [INFO    ]  Collecting msgpack>=1.0 (from librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,625 [INFO    ]    Using cached msgpack-1.1.1-cp311-cp311-win_amd64.whl.metadata (8.6 kB)
2025-08-05 17:51:30,630 [INFO    ]  Collecting mdurl~=0.1 (from markdown-it-py>=2.1.0->markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,631 [INFO    ]    Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
2025-08-05 17:51:30,632 [INFO    ]  Collecting linkify-it-py<3,>=1 (from markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,632 [INFO    ]    Using cached linkify_it_py-2.0.3-py3-none-any.whl.metadata (8.5 kB)
2025-08-05 17:51:30,632 [INFO    ]  Collecting mdit-py-plugins (from markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,633 [INFO    ]    Using cached mdit_py_plugins-0.4.2-py3-none-any.whl.metadata (2.8 kB)
2025-08-05 17:51:30,634 [INFO    ]  Collecting contourpy>=1.0.1 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,634 [INFO    ]    Using cached contourpy-1.3.3-cp311-cp311-win_amd64.whl.metadata (5.5 kB)
2025-08-05 17:51:30,635 [INFO    ]  Collecting cycler>=0.10 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,636 [INFO    ]    Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
2025-08-05 17:51:30,636 [INFO    ]  Collecting fonttools>=4.22.0 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,637 [INFO    ]    Using cached fonttools-4.59.0-cp311-cp311-win_amd64.whl.metadata (110 kB)
2025-08-05 17:51:30,637 [INFO    ]  Collecting kiwisolver>=1.3.1 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,638 [INFO    ]    Using cached kiwisolver-1.4.8-cp311-cp311-win_amd64.whl.metadata (6.3 kB)
2025-08-05 17:51:30,639 [INFO    ]  Collecting pillow>=8 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,639 [INFO    ]    Using cached pillow-11.3.0-cp311-cp311-win_amd64.whl.metadata (9.2 kB)
2025-08-05 17:51:30,640 [INFO    ]  Collecting pyparsing>=2.3.1 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,641 [INFO    ]    Using cached pyparsing-3.2.3-py3-none-any.whl.metadata (5.0 kB)
2025-08-05 17:51:30,641 [INFO    ]  Collecting python-dateutil>=2.7 (from matplotlib>=3.7.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,642 [INFO    ]    Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
2025-08-05 17:51:30,647 [INFO    ]  Collecting docopt>=0.6.2 (from num2words->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,648 [INFO    ]    Using cached docopt-0.6.2-py2.py3-none-any.whl
2025-08-05 17:51:30,648 [INFO    ]  Collecting llvmlite<0.45,>=0.44.0dev0 (from numba>=0.57.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,649 [INFO    ]    Using cached llvmlite-0.44.0-cp311-cp311-win_amd64.whl.metadata (5.0 kB)
2025-08-05 17:51:30,650 [INFO    ]  Collecting pytz>=2020.1 (from pandas<2.0,>=1.4->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,650 [INFO    ]    Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
2025-08-05 17:51:30,651 [INFO    ]  Collecting threadpoolctl>=3.1.0 (from scikit-learn>=1.3.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,652 [INFO    ]    Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
2025-08-05 17:51:30,652 [INFO    ]  Collecting cffi>=1.0 (from soundfile>=0.12.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,654 [INFO    ]    Using cached cffi-1.17.1-cp311-cp311-win_amd64.whl.metadata (1.6 kB)
2025-08-05 17:51:30,654 [INFO    ]  Collecting spacy-legacy<3.1.0,>=3.0.11 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,655 [INFO    ]    Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl.metadata (2.8 kB)
2025-08-05 17:51:30,655 [INFO    ]  Collecting spacy-loggers<2.0.0,>=1.0.0 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,656 [INFO    ]    Using cached spacy_loggers-1.0.5-py3-none-any.whl.metadata (23 kB)
2025-08-05 17:51:30,656 [INFO    ]  Collecting murmurhash<1.1.0,>=0.28.0 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,658 [INFO    ]    Using cached murmurhash-1.0.13-cp311-cp311-win_amd64.whl.metadata (2.2 kB)
2025-08-05 17:51:30,658 [INFO    ]  Collecting cymem<2.1.0,>=2.0.2 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,659 [INFO    ]    Using cached cymem-2.0.11-cp311-cp311-win_amd64.whl.metadata (8.8 kB)
2025-08-05 17:51:30,664 [INFO    ]  Collecting preshed<3.1.0,>=3.0.2 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,665 [INFO    ]    Using cached preshed-3.0.10-cp311-cp311-win_amd64.whl.metadata (2.5 kB)
2025-08-05 17:51:30,666 [INFO    ]  Collecting thinc<8.4.0,>=8.3.4 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,666 [INFO    ]    Using cached thinc-8.3.6-cp311-cp311-win_amd64.whl.metadata (15 kB)
2025-08-05 17:51:30,667 [INFO    ]  Collecting wasabi<1.2.0,>=0.9.1 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,668 [INFO    ]    Using cached wasabi-1.1.3-py3-none-any.whl.metadata (28 kB)
2025-08-05 17:51:30,668 [INFO    ]  Collecting srsly<3.0.0,>=2.4.3 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,669 [INFO    ]    Using cached srsly-2.5.1-cp311-cp311-win_amd64.whl.metadata (20 kB)
2025-08-05 17:51:30,670 [INFO    ]  Collecting catalogue<2.1.0,>=2.0.6 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,671 [INFO    ]    Using cached catalogue-2.0.10-py3-none-any.whl.metadata (14 kB)
2025-08-05 17:51:30,671 [INFO    ]  Collecting weasel<0.5.0,>=0.1.0 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,672 [INFO    ]    Using cached weasel-0.4.1-py3-none-any.whl.metadata (4.6 kB)
2025-08-05 17:51:30,672 [INFO    ]  Collecting typer<1.0.0,>=0.3.0 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,673 [INFO    ]    Using cached typer-0.16.0-py3-none-any.whl.metadata (15 kB)
2025-08-05 17:51:30,674 [INFO    ]  Collecting pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,697 [INFO    ]    Using cached pydantic-2.11.7-py3-none-any.whl.metadata (67 kB)
2025-08-05 17:51:30,702 [INFO    ]  Requirement already satisfied: setuptools in c:\users\gike5\desktop\ai_python\corvus\venv\lib\site-packages (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7)) (65.5.0)
2025-08-05 17:51:30,703 [INFO    ]  Collecting langcodes<4.0.0,>=3.2.0 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,704 [INFO    ]    Using cached langcodes-3.5.0-py3-none-any.whl.metadata (29 kB)
2025-08-05 17:51:30,705 [INFO    ]  Collecting sudachipy!=0.6.1,>=0.5.2 (from spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,705 [INFO    ]    Using cached SudachiPy-0.6.10-cp311-cp311-win_amd64.whl.metadata (13 kB)
2025-08-05 17:51:30,706 [INFO    ]  Collecting sudachidict_core>=20211220 (from spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,707 [INFO    ]    Using cached sudachidict_core-20250515-py3-none-any.whl.metadata (2.7 kB)
2025-08-05 17:51:30,708 [INFO    ]  Collecting filelock (from torch>=2.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,708 [INFO    ]    Using cached filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
2025-08-05 17:51:30,709 [INFO    ]  Collecting sympy>=1.13.3 (from torch>=2.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,714 [INFO    ]    Using cached sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
2025-08-05 17:51:30,714 [INFO    ]  Collecting colorama (from tqdm>=4.64.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,716 [INFO    ]    Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
2025-08-05 17:51:30,717 [INFO    ]  Collecting psutil (from trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,717 [INFO    ]    Using cached psutil-7.0.0-cp37-abi3-win_amd64.whl.metadata (23 kB)
2025-08-05 17:51:30,718 [INFO    ]  Collecting tensorboard (from trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,719 [INFO    ]    Using cached tensorboard-2.20.0-py3-none-any.whl.metadata (1.8 kB)
2025-08-05 17:51:30,719 [INFO    ]  Collecting huggingface-hub<1.0,>=0.34.0 (from transformers>=4.33.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,720 [INFO    ]    Using cached huggingface_hub-0.34.3-py3-none-any.whl.metadata (14 kB)
2025-08-05 17:51:30,721 [INFO    ]  Collecting regex!=2019.12.17 (from transformers>=4.33.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,722 [INFO    ]    Using cached regex-2025.7.34-cp311-cp311-win_amd64.whl.metadata (41 kB)
2025-08-05 17:51:30,722 [INFO    ]  Collecting tokenizers<0.22,>=0.21 (from transformers>=4.33.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,723 [INFO    ]    Using cached tokenizers-0.21.4-cp39-abi3-win_amd64.whl.metadata (6.9 kB)
2025-08-05 17:51:30,723 [INFO    ]  Collecting safetensors>=0.4.3 (from transformers>=4.33.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,724 [INFO    ]    Using cached safetensors-0.5.3-cp38-abi3-win_amd64.whl.metadata (3.9 kB)
2025-08-05 17:51:30,724 [INFO    ]  Collecting pynndescent>=0.5 (from umap-learn>=0.5.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,725 [INFO    ]    Using cached pynndescent-0.5.13-py3-none-any.whl.metadata (6.8 kB)
2025-08-05 17:51:30,730 [INFO    ]  Collecting pycparser (from cffi>=1.0->soundfile>=0.12.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,731 [INFO    ]    Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
2025-08-05 17:51:30,732 [INFO    ]  Collecting tzlocal (from dateparser~=1.1.0->gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,732 [INFO    ]    Using cached tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
2025-08-05 17:51:30,732 [INFO    ]  Collecting six (from jsonlines~=1.2.0->gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,734 [INFO    ]    Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-08-05 17:51:30,735 [INFO    ]  Collecting language-data>=1.2 (from langcodes<4.0.0,>=3.2.0->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,736 [INFO    ]    Using cached language_data-1.3.0-py3-none-any.whl.metadata (4.3 kB)
2025-08-05 17:51:30,736 [INFO    ]  Collecting uc-micro-py (from linkify-it-py<3,>=1->markdown-it-py[linkify,plugins]>=2.1.0->textual==0.58.0->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 6))
2025-08-05 17:51:30,737 [INFO    ]    Using cached uc_micro_py-1.0.3-py3-none-any.whl.metadata (2.0 kB)
2025-08-05 17:51:30,738 [INFO    ]  Collecting platformdirs>=2.5.0 (from pooch>=1.1->librosa>=0.10.0->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,738 [INFO    ]    Using cached platformdirs-4.3.8-py3-none-any.whl.metadata (12 kB)
2025-08-05 17:51:30,739 [INFO    ]  Collecting annotated-types>=0.6.0 (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,740 [INFO    ]    Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-08-05 17:51:30,740 [INFO    ]  Collecting pydantic-core==2.33.2 (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,741 [INFO    ]    Using cached pydantic_core-2.33.2-cp311-cp311-win_amd64.whl.metadata (6.9 kB)
2025-08-05 17:51:30,741 [INFO    ]  Collecting typing-inspection>=0.4.0 (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,747 [INFO    ]    Using cached typing_inspection-0.4.1-py3-none-any.whl.metadata (2.6 kB)
2025-08-05 17:51:30,748 [INFO    ]  Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch>=2.1->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,748 [INFO    ]    Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
2025-08-05 17:51:30,749 [INFO    ]  Collecting blis<1.4.0,>=1.3.0 (from thinc<8.4.0,>=8.3.4->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,750 [INFO    ]    Using cached blis-1.3.0-cp311-cp311-win_amd64.whl.metadata (7.6 kB)
2025-08-05 17:51:30,750 [INFO    ]  Collecting confection<1.0.0,>=0.0.1 (from thinc<8.4.0,>=8.3.4->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,751 [INFO    ]    Using cached confection-0.1.5-py3-none-any.whl.metadata (19 kB)
2025-08-05 17:51:30,752 [INFO    ]  INFO: pip is looking at multiple versions of thinc to determine which version is compatible with other requirements. This could take a while.
2025-08-05 17:51:30,752 [INFO    ]  Collecting thinc<8.4.0,>=8.3.4 (from spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,754 [INFO    ]    Using cached thinc-8.3.4-cp311-cp311-win_amd64.whl.metadata (15 kB)
2025-08-05 17:51:30,754 [INFO    ]  Collecting blis<1.3.0,>=1.2.0 (from thinc<8.4.0,>=8.3.4->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,754 [INFO    ]    Using cached blis-1.2.1-cp311-cp311-win_amd64.whl.metadata (7.6 kB)
2025-08-05 17:51:30,756 [INFO    ]  Collecting shellingham>=1.3.0 (from typer<1.0.0,>=0.3.0->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,756 [INFO    ]    Using cached shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
2025-08-05 17:51:30,757 [INFO    ]  Collecting cloudpathlib<1.0.0,>=0.7.0 (from weasel<0.5.0,>=0.1.0->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,758 [INFO    ]    Using cached cloudpathlib-0.21.1-py3-none-any.whl.metadata (14 kB)
2025-08-05 17:51:30,758 [INFO    ]  Collecting smart-open<8.0.0,>=5.2.1 (from weasel<0.5.0,>=0.1.0->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,759 [INFO    ]    Using cached smart_open-7.3.0.post1-py3-none-any.whl.metadata (24 kB)
2025-08-05 17:51:30,764 [INFO    ]  Collecting absl-py>=0.4 (from tensorboard->trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,765 [INFO    ]    Using cached absl_py-2.3.1-py3-none-any.whl.metadata (3.3 kB)
2025-08-05 17:51:30,765 [INFO    ]  Collecting grpcio>=1.48.2 (from tensorboard->trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,766 [INFO    ]    Using cached grpcio-1.74.0-cp311-cp311-win_amd64.whl.metadata (4.0 kB)
2025-08-05 17:51:30,767 [INFO    ]  Collecting markdown>=2.6.8 (from tensorboard->trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,767 [INFO    ]    Using cached markdown-3.8.2-py3-none-any.whl.metadata (5.1 kB)
2025-08-05 17:51:30,768 [INFO    ]  Collecting protobuf!=4.24.0,>=3.19.6 (from tensorboard->trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,769 [INFO    ]    Using cached protobuf-6.31.1-cp310-abi3-win_amd64.whl.metadata (593 bytes)
2025-08-05 17:51:30,769 [INFO    ]  Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard->trainer>=0.0.32->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,770 [INFO    ]    Using cached tensorboard_data_server-0.7.2-py3-none-any.whl.metadata (1.1 kB)
2025-08-05 17:51:30,771 [INFO    ]  Collecting marisa-trie>=1.1.0 (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,772 [INFO    ]    Using cached marisa_trie-1.2.1-cp311-cp311-win_amd64.whl.metadata (9.3 kB)
2025-08-05 17:51:30,772 [INFO    ]  Collecting wrapt (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy>=3->spacy[ja]>=3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,774 [INFO    ]    Using cached wrapt-1.17.2-cp311-cp311-win_amd64.whl.metadata (6.5 kB)
2025-08-05 17:51:30,774 [INFO    ]  Collecting tzdata (from tzlocal->dateparser~=1.1.0->gruut==2.2.3->gruut[de,es,fr]==2.2.3->TTS->-r C:\Users\gike5\Desktop\AI_Python\Corvus\requirements.txt (line 7))
2025-08-05 17:51:30,775 [INFO    ]    Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
2025-08-05 17:51:30,779 [INFO    ]  Using cached textual-0.58.0-py3-none-any.whl (549 kB)
2025-08-05 17:51:30,780 [INFO    ]  Using cached speechrecognition-3.14.3-py3-none-any.whl (32.9 MB)
2025-08-05 17:51:30,780 [INFO    ]  Using cached PyAudio-0.2.14-cp311-cp311-win_amd64.whl (164 kB)
2025-08-05 17:51:30,781 [INFO    ]  Using cached rich-14.1.0-py3-none-any.whl (243 kB)
2025-08-05 17:51:30,781 [INFO    ]  Using cached python_dotenv-1.1.1-py3-none-any.whl (20 kB)
2025-08-05 17:51:30,782 [INFO    ]  Using cached requests-2.32.4-py3-none-any.whl (64 kB)
2025-08-05 17:51:30,782 [INFO    ]  Using cached beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)
2025-08-05 17:51:30,784 [INFO    ]  Using cached aiohttp-3.12.15-cp311-cp311-win_amd64.whl (453 kB)
2025-08-05 17:51:30,784 [INFO    ]  Using cached anyascii-0.3.3-py3-none-any.whl (345 kB)
2025-08-05 17:51:30,785 [INFO    ]  Using cached certifi-2025.8.3-py3-none-any.whl (161 kB)
2025-08-05 17:51:30,786 [INFO    ]  Using cached charset_normalizer-3.4.2-cp311-cp311-win_amd64.whl (105 kB)
2025-08-05 17:51:30,786 [INFO    ]  Using cached coqpit-0.0.17-py3-none-any.whl (13 kB)
2025-08-05 17:51:30,787 [INFO    ]  Using cached cython-3.1.2-cp311-cp311-win_amd64.whl (2.7 MB)
2025-08-05 17:51:30,788 [INFO    ]  Using cached diskcache-5.6.3-py3-none-any.whl (45 kB)
2025-08-05 17:51:30,788 [INFO    ]  Using cached einops-0.8.1-py3-none-any.whl (64 kB)
2025-08-05 17:51:30,789 [INFO    ]  Using cached flask-3.1.1-py3-none-any.whl (103 kB)
2025-08-05 17:51:30,789 [INFO    ]  Using cached fsspec-2025.7.0-py3-none-any.whl (199 kB)
2025-08-05 17:51:30,790 [INFO    ]  Using cached g2pkk-0.1.2-py3-none-any.whl (25 kB)
2025-08-05 17:51:30,790 [INFO    ]  Using cached idna-3.10-py3-none-any.whl (70 kB)
2025-08-05 17:51:30,791 [INFO    ]  Using cached inflect-7.5.0-py3-none-any.whl (35 kB)
2025-08-05 17:51:30,791 [INFO    ]  Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
2025-08-05 17:51:30,792 [INFO    ]  Using cached librosa-0.11.0-py3-none-any.whl (260 kB)
2025-08-05 17:51:30,798 [INFO    ]  Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
2025-08-05 17:51:30,798 [INFO    ]  Using cached matplotlib-3.10.5-cp311-cp311-win_amd64.whl (8.1 MB)
2025-08-05 17:51:30,799 [INFO    ]  Using cached num2words-0.5.14-py3-none-any.whl (163 kB)
2025-08-05 17:51:30,800 [INFO    ]  Using cached numba-0.61.2-cp311-cp311-win_amd64.whl (2.8 MB)
2025-08-05 17:51:30,800 [INFO    ]  Using cached numpy-1.26.4-cp311-cp311-win_amd64.whl (15.8 MB)
2025-08-05 17:51:30,801 [INFO    ]  Using cached packaging-25.0-py3-none-any.whl (66 kB)
2025-08-05 17:51:30,802 [INFO    ]  Using cached pandas-1.5.3-cp311-cp311-win_amd64.whl (10.3 MB)
2025-08-05 17:51:30,802 [INFO    ]  Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
2025-08-05 17:51:30,802 [INFO    ]  Using cached pysbd-0.3.4-py3-none-any.whl (71 kB)
2025-08-05 17:51:30,804 [INFO    ]  Using cached PyYAML-6.0.2-cp311-cp311-win_amd64.whl (161 kB)
2025-08-05 17:51:30,804 [INFO    ]  Using cached scikit_learn-1.7.1-cp311-cp311-win_amd64.whl (8.9 MB)
2025-08-05 17:51:30,805 [INFO    ]  Using cached scipy-1.16.1-cp311-cp311-win_amd64.whl (38.6 MB)
2025-08-05 17:51:30,806 [INFO    ]  Using cached soundfile-0.13.1-py2.py3-none-win_amd64.whl (1.0 MB)
2025-08-05 17:51:30,806 [INFO    ]  Using cached soupsieve-2.7-py3-none-any.whl (36 kB)
2025-08-05 17:51:30,807 [INFO    ]  Using cached spacy-3.8.7-cp311-cp311-win_amd64.whl (14.9 MB)
2025-08-05 17:51:30,808 [INFO    ]  Using cached torch-2.7.1-cp311-cp311-win_amd64.whl (216.1 MB)
2025-08-05 17:51:30,808 [INFO    ]  Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
2025-08-05 17:51:30,809 [INFO    ]  Using cached trainer-0.0.36-py3-none-any.whl (51 kB)
2025-08-05 17:51:30,814 [INFO    ]  Using cached transformers-4.54.1-py3-none-any.whl (11.2 MB)
2025-08-05 17:51:30,815 [INFO    ]  Using cached typing_extensions-4.14.1-py3-none-any.whl (43 kB)
2025-08-05 17:51:30,816 [INFO    ]  Using cached umap_learn-0.5.9.post2-py3-none-any.whl (90 kB)
2025-08-05 17:51:30,816 [INFO    ]  Using cached Unidecode-1.4.0-py3-none-any.whl (235 kB)
2025-08-05 17:51:30,817 [INFO    ]  Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
2025-08-05 17:51:30,817 [INFO    ]  Using cached bangla-0.0.5-py3-none-any.whl (5.1 kB)
2025-08-05 17:51:30,818 [INFO    ]  Using cached bnunicodenormalizer-0.1.7-py3-none-any.whl (23 kB)
2025-08-05 17:51:30,819 [INFO    ]  Using cached hangul_romanize-0.1.0-py3-none-any.whl (4.6 kB)
2025-08-05 17:51:30,819 [INFO    ]  Using cached jamo-0.4.1-py3-none-any.whl (9.5 kB)
2025-08-05 17:51:30,820 [INFO    ]  Using cached nltk-3.9.1-py3-none-any.whl (1.5 MB)
2025-08-05 17:51:30,820 [INFO    ]  Using cached pypinyin-0.55.0-py2.py3-none-any.whl (840 kB)
2025-08-05 17:51:30,821 [INFO    ]  Using cached torchaudio-2.7.1-cp311-cp311-win_amd64.whl (2.5 MB)
2025-08-05 17:51:30,822 [INFO    ]  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
2025-08-05 17:51:30,822 [INFO    ]  Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
2025-08-05 17:51:30,822 [INFO    ]  Using cached attrs-25.3.0-py3-none-any.whl (63 kB)
2025-08-05 17:51:30,823 [INFO    ]  Using cached audioread-3.0.1-py3-none-any.whl (23 kB)
2025-08-05 17:51:30,824 [INFO    ]  Using cached babel-2.17.0-py3-none-any.whl (10.2 MB)
2025-08-05 17:51:30,824 [INFO    ]  Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
2025-08-05 17:51:30,825 [INFO    ]  Using cached catalogue-2.0.10-py3-none-any.whl (17 kB)
2025-08-05 17:51:30,829 [INFO    ]  Using cached cffi-1.17.1-cp311-cp311-win_amd64.whl (181 kB)
2025-08-05 17:51:30,830 [INFO    ]  Using cached click-8.2.1-py3-none-any.whl (102 kB)
2025-08-05 17:51:30,830 [INFO    ]  Using cached contourpy-1.3.3-cp311-cp311-win_amd64.whl (225 kB)
2025-08-05 17:51:30,831 [INFO    ]  Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
2025-08-05 17:51:30,832 [INFO    ]  Using cached cymem-2.0.11-cp311-cp311-win_amd64.whl (39 kB)
2025-08-05 17:51:30,832 [INFO    ]  Using cached dateparser-1.1.8-py2.py3-none-any.whl (293 kB)
2025-08-05 17:51:30,833 [INFO    ]  Using cached decorator-5.2.1-py3-none-any.whl (9.2 kB)
2025-08-05 17:51:30,834 [INFO    ]  Using cached fonttools-4.59.0-cp311-cp311-win_amd64.whl (2.3 MB)
2025-08-05 17:51:30,834 [INFO    ]  Using cached frozenlist-1.7.0-cp311-cp311-win_amd64.whl (44 kB)
2025-08-05 17:51:30,834 [INFO    ]  Using cached huggingface_hub-0.34.3-py3-none-any.whl (558 kB)
2025-08-05 17:51:30,835 [INFO    ]  Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
2025-08-05 17:51:30,836 [INFO    ]  Using cached joblib-1.5.1-py3-none-any.whl (307 kB)
2025-08-05 17:51:30,837 [INFO    ]  Using cached jsonlines-1.2.0-py2.py3-none-any.whl (7.6 kB)
2025-08-05 17:51:30,837 [INFO    ]  Using cached kiwisolver-1.4.8-cp311-cp311-win_amd64.whl (71 kB)
2025-08-05 17:51:30,838 [INFO    ]  Using cached langcodes-3.5.0-py3-none-any.whl (182 kB)
2025-08-05 17:51:30,838 [INFO    ]  Using cached lazy_loader-0.4-py3-none-any.whl (12 kB)
2025-08-05 17:51:30,839 [INFO    ]  Using cached linkify_it_py-2.0.3-py3-none-any.whl (19 kB)
2025-08-05 17:51:30,839 [INFO    ]  Using cached llvmlite-0.44.0-cp311-cp311-win_amd64.whl (30.3 MB)
2025-08-05 17:51:30,840 [INFO    ]  Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl (15 kB)
2025-08-05 17:51:30,842 [INFO    ]  Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
2025-08-05 17:51:30,847 [INFO    ]  Using cached more_itertools-10.7.0-py3-none-any.whl (65 kB)
2025-08-05 17:51:30,848 [INFO    ]  Using cached msgpack-1.1.1-cp311-cp311-win_amd64.whl (72 kB)
2025-08-05 17:51:30,849 [INFO    ]  Using cached multidict-6.6.3-cp311-cp311-win_amd64.whl (45 kB)
2025-08-05 17:51:30,849 [INFO    ]  Using cached murmurhash-1.0.13-cp311-cp311-win_amd64.whl (24 kB)
2025-08-05 17:51:30,850 [INFO    ]  Using cached networkx-2.8.8-py3-none-any.whl (2.0 MB)
2025-08-05 17:51:30,850 [INFO    ]  Using cached pillow-11.3.0-cp311-cp311-win_amd64.whl (7.0 MB)
2025-08-05 17:51:30,851 [INFO    ]  Using cached pooch-1.8.2-py3-none-any.whl (64 kB)
2025-08-05 17:51:30,852 [INFO    ]  Using cached preshed-3.0.10-cp311-cp311-win_amd64.whl (117 kB)
2025-08-05 17:51:30,852 [INFO    ]  Using cached propcache-0.3.2-cp311-cp311-win_amd64.whl (41 kB)
2025-08-05 17:51:30,852 [INFO    ]  Using cached pydantic-2.11.7-py3-none-any.whl (444 kB)
2025-08-05 17:51:30,854 [INFO    ]  Using cached pydantic_core-2.33.2-cp311-cp311-win_amd64.whl (2.0 MB)
2025-08-05 17:51:30,855 [INFO    ]  Using cached pynndescent-0.5.13-py3-none-any.whl (56 kB)
2025-08-05 17:51:30,856 [INFO    ]  Using cached pyparsing-3.2.3-py3-none-any.whl (111 kB)
2025-08-05 17:51:30,856 [INFO    ]  Using cached python_crfsuite-0.9.11-cp311-cp311-win_amd64.whl (301 kB)
2025-08-05 17:51:30,857 [INFO    ]  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
2025-08-05 17:51:30,857 [INFO    ]  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
2025-08-05 17:51:30,858 [INFO    ]  Using cached regex-2025.7.34-cp311-cp311-win_amd64.whl (276 kB)
2025-08-05 17:51:30,859 [INFO    ]  Using cached safetensors-0.5.3-cp38-abi3-win_amd64.whl (308 kB)
2025-08-05 17:51:30,864 [INFO    ]  Using cached soxr-0.5.0.post1-cp311-cp311-win_amd64.whl (166 kB)
2025-08-05 17:51:30,864 [INFO    ]  Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl (29 kB)
2025-08-05 17:51:30,865 [INFO    ]  Using cached spacy_loggers-1.0.5-py3-none-any.whl (22 kB)
2025-08-05 17:51:30,866 [INFO    ]  Using cached srsly-2.5.1-cp311-cp311-win_amd64.whl (632 kB)
2025-08-05 17:51:30,866 [INFO    ]  Using cached sudachidict_core-20250515-py3-none-any.whl (72.1 MB)
2025-08-05 17:51:30,867 [INFO    ]  Using cached SudachiPy-0.6.10-cp311-cp311-win_amd64.whl (1.4 MB)
2025-08-05 17:51:30,867 [INFO    ]  Using cached sympy-1.14.0-py3-none-any.whl (6.3 MB)
2025-08-05 17:51:30,868 [INFO    ]  Using cached thinc-8.3.4-cp311-cp311-win_amd64.whl (1.5 MB)
2025-08-05 17:51:30,868 [INFO    ]  Using cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
2025-08-05 17:51:30,869 [INFO    ]  Using cached tokenizers-0.21.4-cp39-abi3-win_amd64.whl (2.5 MB)
2025-08-05 17:51:30,870 [INFO    ]  Using cached typeguard-4.4.4-py3-none-any.whl (34 kB)
2025-08-05 17:51:30,870 [INFO    ]  Using cached typer-0.16.0-py3-none-any.whl (46 kB)
2025-08-05 17:51:30,871 [INFO    ]  Using cached wasabi-1.1.3-py3-none-any.whl (27 kB)
2025-08-05 17:51:30,871 [INFO    ]  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
2025-08-05 17:51:30,872 [INFO    ]  Using cached weasel-0.4.1-py3-none-any.whl (50 kB)
2025-08-05 17:51:30,872 [INFO    ]  Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
2025-08-05 17:51:30,874 [INFO    ]  Using cached yarl-1.20.1-cp311-cp311-win_amd64.whl (86 kB)
2025-08-05 17:51:30,874 [INFO    ]  Using cached filelock-3.18.0-py3-none-any.whl (16 kB)
2025-08-05 17:51:30,874 [INFO    ]  Using cached mdit_py_plugins-0.4.2-py3-none-any.whl (55 kB)
2025-08-05 17:51:30,874 [INFO    ]  Using cached psutil-7.0.0-cp37-abi3-win_amd64.whl (244 kB)
2025-08-05 17:51:30,880 [INFO    ]  Using cached tensorboard-2.20.0-py3-none-any.whl (5.5 MB)
2025-08-05 17:51:30,881 [INFO    ]  Using cached absl_py-2.3.1-py3-none-any.whl (135 kB)
2025-08-05 17:51:30,882 [INFO    ]  Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-08-05 17:51:30,882 [INFO    ]  Using cached blis-1.2.1-cp311-cp311-win_amd64.whl (6.2 MB)
2025-08-05 17:51:30,883 [INFO    ]  Using cached cloudpathlib-0.21.1-py3-none-any.whl (52 kB)
2025-08-05 17:51:30,883 [INFO    ]  Using cached confection-0.1.5-py3-none-any.whl (35 kB)
2025-08-05 17:51:30,884 [INFO    ]  Using cached grpcio-1.74.0-cp311-cp311-win_amd64.whl (4.5 MB)
2025-08-05 17:51:30,884 [INFO    ]  Using cached language_data-1.3.0-py3-none-any.whl (5.4 MB)
2025-08-05 17:51:30,885 [INFO    ]  Using cached markdown-3.8.2-py3-none-any.whl (106 kB)
2025-08-05 17:51:30,885 [INFO    ]  Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
2025-08-05 17:51:30,886 [INFO    ]  Using cached platformdirs-4.3.8-py3-none-any.whl (18 kB)
2025-08-05 17:51:30,887 [INFO    ]  Using cached protobuf-6.31.1-cp310-abi3-win_amd64.whl (435 kB)
2025-08-05 17:51:30,887 [INFO    ]  Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
2025-08-05 17:51:30,888 [INFO    ]  Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-08-05 17:51:30,888 [INFO    ]  Using cached smart_open-7.3.0.post1-py3-none-any.whl (61 kB)
2025-08-05 17:51:30,889 [INFO    ]  Using cached tensorboard_data_server-0.7.2-py3-none-any.whl (2.4 kB)
2025-08-05 17:51:30,890 [INFO    ]  Using cached typing_inspection-0.4.1-py3-none-any.whl (14 kB)
2025-08-05 17:51:30,890 [INFO    ]  Using cached pycparser-2.22-py3-none-any.whl (117 kB)
2025-08-05 17:51:30,891 [INFO    ]  Using cached tzlocal-5.3.1-py3-none-any.whl (18 kB)
2025-08-05 17:51:30,892 [INFO    ]  Using cached uc_micro_py-1.0.3-py3-none-any.whl (6.2 kB)
2025-08-05 17:51:30,898 [INFO    ]  Using cached marisa_trie-1.2.1-cp311-cp311-win_amd64.whl (152 kB)
2025-08-05 17:51:30,899 [INFO    ]  Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
2025-08-05 17:51:30,900 [INFO    ]  Using cached wrapt-1.17.2-cp311-cp311-win_amd64.whl (38 kB)
2025-08-05 17:51:30,901 [INFO    ]  Installing collected packages: sudachipy, pytz, PyAudio, mpmath, jieba, jamo, hangul_romanize, gruut_lang_fr, gruut_lang_es, gruut_lang_en, gruut_lang_de, docopt, cymem, bnunicodenormalizer, bnnumerizer, bangla, wrapt, urllib3, unidecode, uc-micro-py, tzdata, typing-extensions, threadpoolctl, tensorboard-data-server, sympy, sudachidict_core, spacy-loggers, spacy-legacy, soupsieve, six, shellingham, safetensors, regex, pyyaml, python-dotenv, python-crfsuite, pysbd, pypinyin, pyparsing, pygments, pycparser, psutil, protobuf, propcache, platformdirs, pillow, packaging, numpy, num2words, networkx, murmurhash, multidict, msgpack, more_itertools, mdurl, markupsafe, markdown, marisa-trie, llvmlite, kiwisolver, joblib, itsdangerous, idna, gruut-ipa, grpcio, fsspec, frozenlist, fonttools, filelock, einops, diskcache, decorator, cython, cycler, coqpit, colorama, cloudpathlib, charset_normalizer, certifi, catalogue, blinker, Babel, audioread, attrs, anyascii, annotated-types, aiohappyeyeballs, absl-py, yarl, werkzeug, wasabi, tzlocal, typing-inspection, typeguard, tqdm, srsly, SpeechRecognition, soxr, smart-open, scipy, requests, python-dateutil, pydantic-core, preshed, numba, markdown-it-py, linkify-it-py, lazy_loader, language-data, jsonlines, jinja2, contourpy, click, cffi, blis, beautifulsoup4, aiosignal, torch, tensorboard, soundfile, scikit-learn, rich, pydantic, pooch, pandas, nltk, mdit-py-plugins, matplotlib, llama-cpp-python, langcodes, inflect, huggingface-hub, flask, dateparser, aiohttp, typer, trainer, torchaudio, tokenizers, pynndescent, librosa, gruut, g2pkk, confection, weasel, umap-learn, transformers, thinc, textual, encodec, spacy, TTS
2025-08-05 17:51:30,904 [INFO    ]  Successfully installed Babel-2.17.0 PyAudio-0.2.14 SpeechRecognition-3.14.3 TTS-0.22.0 absl-py-2.3.1 aiohappyeyeballs-2.6.1 aiohttp-3.12.15 aiosignal-1.4.0 annotated-types-0.7.0 anyascii-0.3.3 attrs-25.3.0 audioread-3.0.1 bangla-0.0.5 beautifulsoup4-4.13.4 blinker-1.9.0 blis-1.2.1 bnnumerizer-0.0.2 bnunicodenormalizer-0.1.7 catalogue-2.0.10 certifi-2025.8.3 cffi-1.17.1 charset_normalizer-3.4.2 click-8.2.1 cloudpathlib-0.21.1 colorama-0.4.6 confection-0.1.5 contourpy-1.3.3 coqpit-0.0.17 cycler-0.12.1 cymem-2.0.11 cython-3.1.2 dateparser-1.1.8 decorator-5.2.1 diskcache-5.6.3 docopt-0.6.2 einops-0.8.1 encodec-0.1.1 filelock-3.18.0 flask-3.1.1 fonttools-4.59.0 frozenlist-1.7.0 fsspec-2025.7.0 g2pkk-0.1.2 grpcio-1.74.0 gruut-2.2.3 gruut-ipa-0.13.0 gruut_lang_de-2.0.1 gruut_lang_en-2.0.1 gruut_lang_es-2.0.1 gruut_lang_fr-2.0.2 hangul_romanize-0.1.0 huggingface-hub-0.34.3 idna-3.10 inflect-7.5.0 itsdangerous-2.2.0 jamo-0.4.1 jieba-0.42.1 jinja2-3.1.6 joblib-1.5.1 jsonlines-1.2.0 kiwisolver-1.4.8 langcodes-3.5.0 language-data-1.3.0 lazy_loader-0.4 librosa-0.11.0 linkify-it-py-2.0.3 llama-cpp-python-0.3.14 llvmlite-0.44.0 marisa-trie-1.2.1 markdown-3.8.2 markdown-it-py-3.0.0 markupsafe-3.0.2 matplotlib-3.10.5 mdit-py-plugins-0.4.2 mdurl-0.1.2 more_itertools-10.7.0 mpmath-1.3.0 msgpack-1.1.1 multidict-6.6.3 murmurhash-1.0.13 networkx-2.8.8 nltk-3.9.1 num2words-0.5.14 numba-0.61.2 numpy-1.26.4 packaging-25.0 pandas-1.5.3 pillow-11.3.0 platformdirs-4.3.8 pooch-1.8.2 preshed-3.0.10 propcache-0.3.2 protobuf-6.31.1 psutil-7.0.0 pycparser-2.22 pydantic-2.11.7 pydantic-core-2.33.2 pygments-2.19.2 pynndescent-0.5.13 pyparsing-3.2.3 pypinyin-0.55.0 pysbd-0.3.4 python-crfsuite-0.9.11 python-dateutil-2.9.0.post0 python-dotenv-1.1.1 pytz-2025.2 pyyaml-6.0.2 regex-2025.7.34 requests-2.32.4 rich-14.1.0 safetensors-0.5.3 scikit-learn-1.7.1 scipy-1.16.1 shellingham-1.5.4 six-1.17.0 smart-open-7.3.0.post1 soundfile-0.13.1 soupsieve-2.7 soxr-0.5.0.post1 spacy-3.8.7 spacy-legacy-3.0.12 spacy-loggers-1.0.5 srsly-2.5.1 sudachidict_core-20250515 sudachipy-0.6.10 sympy-1.14.0 tensorboard-2.20.0 tensorboard-data-server-0.7.2 textual-0.58.0 thinc-8.3.4 threadpoolctl-3.6.0 tokenizers-0.21.4 torch-2.7.1 torchaudio-2.7.1 tqdm-4.67.1 trainer-0.0.36 transformers-4.54.1 typeguard-4.4.4 typer-0.16.0 typing-extensions-4.14.1 typing-inspection-0.4.1 tzdata-2025.2 tzlocal-5.3.1 uc-micro-py-1.0.3 umap-learn-0.5.9.post2 unidecode-1.4.0 urllib3-2.5.0 wasabi-1.1.3 weasel-0.4.1 werkzeug-3.1.3 wrapt-1.17.2 yarl-1.20.1
2025-08-05 17:51:30,916 [INFO    ]  Dependencies installed successfully!
2025-08-05 17:51:30,918 [INFO    ]  Setting up configuration...
2025-08-05 17:51:30,930 [INFO    ]  .env file created successfully from example.
2025-08-05 17:51:30,932 [INFO    ]  Setup complete. The main application will now launch.

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

        self.run_worker(
            lambda: self.simulate_progress(process),
            thread=True,
            group="simulation",
            name=f"pip_install_progress_{process.pid}"
        )

        stdout, stderr = process.communicate()
        
        # REMOVED: The problematic line that caused the crash. The simulation worker
        # will now exit gracefully on its own when it detects that `process` has finished.
        # self.cancel_workers(group="simulation")

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
PyAudio
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
import traceback
from importlib.metadata import version, PackageNotFoundError
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
# Ensure 'corvus_app' can be imported by adding the project root to the Python path.
sys.path.insert(0, str(PROJECT_ROOT))

# Now that the path is set, we can import the crash handler.
from corvus_app.crash_handler import format_crash_report

# --- Configuration ---
TEXTUAL_VERSION = "0.58.0"
PKG_NAME = "textual"
REQUIRED_PKG = f"{PKG_NAME}=={TEXTUAL_VERSION}"
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
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to install Textual via pip. Is pip working? Error: {e}")


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
        # This error is now caught inside main_app.main, which will generate its own detailed log.
        print("\n[INFO] Corvus application closed with an error. See 'corvus_crash_report.log'.")
    except FileNotFoundError:
        raise RuntimeError(f"Could not find the application entry point at '{VENV_PYTHON}'. The virtual environment might be corrupt.")


def main():
    """Main entry point for the application launcher."""
    try:
        print("Initializing Corvus...")
        if MARKER_FILE.exists():
            launch_main_app()
        else:
            if not check_and_install_textual():
                sys.exit(1)

            if launch_installer():
                if not MARKER_FILE.exists():
                     raise RuntimeError("Installer reported success, but the installation marker is missing.")
                launch_main_app()
            else:
                # The installer UI's internal error handler should catch most things, but if it doesn't...
                print("\n[INFO] Installation was cancelled or failed. Check 'installer.log' for details.")
    
    except Exception as e:
        # Catch any crash from the launcher/installer process itself
        tb_info = traceback.format_exc()
        format_crash_report("Launcher/Installer", e, tb_info)
        sys.exit(1)


if __name__ == "__main__":
    main()
    # On Windows, the 'pause' in the start.bat is more effective. On other OS, this provides a clear exit message.
    if sys.platform != "win32":
        print("\nLauncher has finished.")
```

### File: `/settings.json`
```json
{
    "active_llm_model": null,
    "active_tts_model": "tts_models/en/ljspeech/vits",
    "wake_word": "computer",
    "system_prompt": "You are a helpful assistant."
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