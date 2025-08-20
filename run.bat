@echo off
REM Koromali Launcher for Windows

REM Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found on your PATH. Please install Python 3.
    pause
    exit /b 1
)

REM Set the venv directory
set VENV_DIR=%~dp0venv

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
pip install -r "%~dp0requirements.txt"
if %errorlevel% neq 0 (
    echo Failed to install dependencies from requirements.txt.
    pause
    exit /b 1
)

REM Run the main application
echo Starting Koromali...
python "%~dp0main.py" %*

echo Koromali has closed.