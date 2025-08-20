# Koromali/utils/logger.py
import logging
import os
import platform
import sys
from logging.handlers import RotatingFileHandler
from app_core.config import APP_NAME, ORG_NAME


def get_app_data_path() -> str:
    """
    Gets a cross-platform writable directory for application data.
    - During development (source main.py exists), it's the project root.
    - In a packaged app, it's the standard user data location.
    """
    # A simple check for frozen status is more reliable
    # than checking for the existence of main.py
    if getattr(sys, 'frozen', False):
        system = platform.system()
        if system == "Windows":
            path = os.path.join(os.environ.get('LOCALAPPDATA', ''),
                                ORG_NAME, APP_NAME)
        elif system == "Darwin": # macOS
            path = os.path.join(os.path.expanduser(
                '~/Library/Application Support'), ORG_NAME, APP_NAME)
        else: # Linux
            path = os.path.join(os.path.expanduser('~/.local/share'),
                                ORG_NAME, APP_NAME)
        return path
    else:
        # Development mode
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


APP_DATA_ROOT = get_app_data_path()
LOG_DIR_NAME = "logs"
# In dev mode, place logs in a /logs subfolder. For packaged app, use app data.
LOG_DIR = os.path.join(APP_DATA_ROOT, LOG_DIR_NAME)

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")


def setup_logger(name: str = APP_NAME,
                   log_level: int = logging.DEBUG) -> logging.Logger:
    """
    Configures and returns a logger instance.
    """
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - "
        "[%(module)s.%(funcName)s:%(lineno)d] - %(message)s"
    )

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    try:
        fh = RotatingFileHandler(
            LOG_FILE, maxBytes=5*1024*1024, backupCount=5, encoding='utf-8'
        )
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except Exception as e:
        logger.error(
            f"Failed to create file handler for logging: {e}", exc_info=False
        )

    logger.info(f"Logger initialized. Log file at: {LOG_FILE}")
    return logger


# Global logger instance for the application
log = setup_logger()