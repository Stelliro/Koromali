@echo off
setlocal EnableExtensions
REM Koromali Launcher for Windows

set "SCRIPT_DIR=%~dp0"
set "KOROMALI_ROOT=%SCRIPT_DIR%"
if defined PYTHONPATH (
    set "PYTHONPATH=%SCRIPT_DIR%;%PYTHONPATH%"
) else (
    set "PYTHONPATH=%SCRIPT_DIR%"
)

REM Prefer py launcher, then python on PATH
set "PYTHON_CMD="
where py >nul 2>&1 && set "PYTHON_CMD=py -3"
if not defined PYTHON_CMD (
    where python >nul 2>&1 && set "PYTHON_CMD=python"
)
if not defined PYTHON_CMD (
    echo Python is not found on your PATH. Please install Python 3.10+.
    pause
    exit /b 1
)

set "VENV_DIR=%SCRIPT_DIR%venv"
set "VENV_PY=%VENV_DIR%\Scripts\python.exe"
set "NEED_VENV=0"

if not exist "%VENV_PY%" (
    set "NEED_VENV=1"
) else (
    REM Detect broken venv (home path moved / deleted)
    "%VENV_PY%" -c "import sys" >nul 2>&1
    if errorlevel 1 set "NEED_VENV=1"
)

if "%NEED_VENV%"=="1" (
    echo Creating or repairing virtual environment...
    if exist "%VENV_DIR%" (
        echo Removing broken venv at "%VENV_DIR%"...
        rmdir /s /q "%VENV_DIR%" 2>nul
    )
    %PYTHON_CMD% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

echo Activating environment and ensuring dependencies...
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r "%SCRIPT_DIR%requirements.txt"
if errorlevel 1 (
    echo Failed to install dependencies from requirements.txt.
    pause
    exit /b 1
)

python -c "import os, sys; sys.path.insert(0, os.environ['KOROMALI_ROOT']); from utils.qt_compat import ensure_qt_binding; ensure_qt_binding()" >nul 2>&1
if errorlevel 1 (
    echo Koromali requires PyQt6 or PySide6. Please install one of these packages and try again.
    pause
    exit /b 1
)

echo Starting Koromali...
python "%SCRIPT_DIR%bootstrap.py" %*

echo Koromali has closed.
endlocal
