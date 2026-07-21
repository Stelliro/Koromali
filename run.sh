#!/bin/bash
# Koromali Launcher for macOS/Linux
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="${SCRIPT_DIR}${PYTHONPATH:+:$PYTHONPATH}"
export KOROMALI_ROOT="${SCRIPT_DIR}"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 could not be found. Please install Python 3.10+."
    exit 1
fi

VENV_DIR="${SCRIPT_DIR}/venv"
VENV_PY="${VENV_DIR}/bin/python"
NEED_VENV=0

if [ ! -x "${VENV_PY}" ]; then
    NEED_VENV=1
elif ! "${VENV_PY}" -c "import sys" >/dev/null 2>&1; then
    NEED_VENV=1
fi

if [ "${NEED_VENV}" -eq 1 ]; then
    echo "Creating or repairing virtual environment..."
    rm -rf "${VENV_DIR}"
    python3 -m venv "${VENV_DIR}"
fi

echo "Activating environment and ensuring dependencies..."
# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"
python -m pip install --upgrade pip >/dev/null 2>&1 || true
pip install -r "${SCRIPT_DIR}/requirements.txt"

python -c "import os, sys; sys.path.insert(0, os.environ['KOROMALI_ROOT']); from utils.qt_compat import ensure_qt_binding; ensure_qt_binding()"

echo "Starting Koromali..."
python "${SCRIPT_DIR}/bootstrap.py" "$@"

echo "Koromali has closed."
deactivate || true
