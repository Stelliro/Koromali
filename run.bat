@echo off
setlocal
REM Koromali Launcher for Windows

REM Resolve repository directory and ensure it is on PYTHONPATH
set "SCRIPT_DIR=%~dp0"
set "KOROMALI_ROOT=%SCRIPT_DIR%"
if defined PYTHONPATH (
    set "PYTHONPATH=%SCRIPT_DIR%;%PYTHONPATH%"
    ) else (
    set "PYTHONPATH=%SCRIPT_DIR%"
)

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found on your PATH. Please install Python 3.
    pause
    exit /b 1
)

REM Set the venv directory
set "VENV_DIR=%SCRIPT_DIR%venv"

REM If venv doesn't exist, create it
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if %errorlevel% neq 0 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Activate venv and install dependencies
echo Activating environment and installing dependencies...
call "%VENV_DIR%\Scripts\activate.bat"
python -m pip install -r "%SCRIPT_DIR%requirements.txt"
if %errorlevel% neq 0 (
    echo Failed to install dependencies from requirements.txt.
    pause
    exit /b 1
)

REM Verify that a supported Qt binding is available
python -c "import os, sys; sys.path.insert(0, os.environ['KOROMALI_ROOT']); from utils.qt_compat import ensure_qt_binding; ensure_qt_binding()" >nul 2>&1
if %errorlevel% neq 0 (
    echo Koromali requires PyQt6 or PySide6. Please install one of these packages and try again.
    pause
    exit /b 1
)

REM Run the main application through the bootstrapper so compatibility hooks are in place
echo Starting Koromali...
python "%SCRIPT_DIR%bootstrap.py" %*

echo Koromali has closed.
endlocal