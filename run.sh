#!/bin/bash
# Koromali Launcher for macOS/Linux

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install it."
    exit 1
fi

# Set the venv directory
VENV_DIR="$(dirname "$0")/venv"

# If venv doesn't exist, create it
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
fi

# Activate venv and install dependencies
echo "Activating environment and installing dependencies..."
source "$VENV_DIR/bin/activate"
pip install -r "$(dirname "$0")/requirements.txt"
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies from requirements.txt."
    deactivate
    exit 1
fi

# Run the main application
echo "Starting Koromali..."
python3 "$(dirname "$0")/main.py" "$@"

echo "Koromali has closed."
deactivate