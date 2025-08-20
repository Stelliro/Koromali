# /app_core/golden_rules.py
import os
import json
import shutil
import re
from typing import Dict
from utils.helpers import get_base_path
from utils.logger import log

ASSETS_PATH = os.path.join(get_base_path(), "assets")
GOLDEN_RULES_PATH = os.path.join(ASSETS_PATH, "golden_rules.json")
# This is a fallback and should not ideally be used for patcher rules.
# The initialization logic has been updated to use a hardcoded default.
DEFAULT_RULES_PATH = os.path.join(ASSETS_PATH, "style_presets", "default_koromali_style.json")


def _get_default_patcher_rules() -> Dict:
    """Returns the default, hardcoded golden rules for the AI patcher."""
    return {
        "name": "Default Patcher Rules",
        "description": "Fundamental rules for how an AI should format responses to be machine-parsable for file operations.",
        "rules": [
            "Your response MUST ONLY contain file modifications, creations, deletions, or renames.",
            "Enclose each file's operation in the standard `### File: /path/to/file.ext` format.",
            "Do not add any commentary, explanations, or summaries outside of the formatted blocks.",
            "To MODIFY or CREATE a file, provide its complete content in a markdown code block (e.g., ```python ... ```).",
            "To DELETE a file, follow the file path with `---DELETED---` on a new line.",
            "To RENAME or MOVE a file, follow the old file path with `---MOVED-TO: /new/path/to/file.ext---` on a new line.",
            "If a file from the user's prompt is not being changed, DO NOT include it in your response.",
            "File paths must be relative to the project root and use forward slashes.",
            "If a file's content contains '```', use more backticks for the outer block (e.g., `````python).",
            "You can use `~~~` as an alternative to ``` for code blocks; the system will automatically convert it. This is useful for markdown files."
        ]
    }


def _initialize_rules():
    """Ensure golden_rules.json exists, creating it from a hardcoded default if not."""
    if not os.path.exists(GOLDEN_RULES_PATH):
        try:
            os.makedirs(os.path.dirname(GOLDEN_RULES_PATH), exist_ok=True)
            with open(GOLDEN_RULES_PATH, 'w', encoding='utf-8') as f:
                json.dump(_get_default_patcher_rules(), f, indent=4)
            log.info(f"Initialized golden rules with default patcher format at {GOLDEN_RULES_PATH}")
        except Exception as e:
            log.error(f"Could not create initial golden rules: {e}")

def get_golden_rules() -> list[str]:
    """
    Returns a list of fundamental, non-negotiable rules for the AI.
    These rules are loaded from the editable golden_rules.json.
    """
    _initialize_rules()
    try:
        with open(GOLDEN_RULES_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Ensure the loaded data is a dictionary and has the 'rules' key which is a list.
            if isinstance(data, dict) and isinstance(data.get("rules"), list):
                return data["rules"]
            else:
                log.warning(f"Golden rules file at {GOLDEN_RULES_PATH} has incorrect format. Re-initializing.")
                # The file is malformed, so we reset it to the default patcher rules.
                os.remove(GOLDEN_RULES_PATH)
                _initialize_rules()
                return _get_default_patcher_rules()["rules"]

    except (IOError, json.JSONDecodeError) as e:
        log.error(f"Failed to load golden rules from {GOLDEN_RULES_PATH}: {e}. Returning default list.")
        return _get_default_patcher_rules()["rules"]

def get_golden_rules_text() -> str:
    """Returns the golden rules as a numbered text block for editing."""
    rules = get_golden_rules()
    if not rules:
        return ""
    return "\n".join(f"{i+1}. {rule}" for i, rule in enumerate(rules))

def save_golden_rules_from_text(text: str) -> bool:
    """
    Parses a numbered or un-numbered text block and saves the rules.
    """
    rules = []
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        # Improved regex to strip optional leading numbers and various punctuation.
        match = re.match(r'^\s*\d+\s*[.\-:]?\s*(.*)', line)
        if match:
            cleaned_line = match.group(1).strip()
        else:
            cleaned_line = line
        if cleaned_line:
            rules.append(cleaned_line)

    _initialize_rules() # Ensure file exists before reading
    try:
        with open(GOLDEN_RULES_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            data = {} # Handle cases where JSON is valid but not an object
    except (IOError, json.JSONDecodeError):
        data = {}
        
    data["rules"] = rules
    data.setdefault("name", "Custom Golden Rules")
    data.setdefault("description", "User-defined golden rules for AI interaction.")

    try:
        with open(GOLDEN_RULES_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        log.info("Golden rules saved successfully.")
        return True
    except IOError as e:
        log.error(f"Failed to save golden rules: {e}")
        return False

def reset_golden_rules_to_default() -> bool:
    """Resets the user's golden rules to the default patcher format."""
    try:
        _initialize_rules() # Ensure the directory exists
        with open(GOLDEN_RULES_PATH, 'w', encoding='utf-8') as f:
            json.dump(_get_default_patcher_rules(), f, indent=4)
        log.info(f"Reset golden rules at {GOLDEN_RULES_PATH} to default.")
        return True
    except Exception as e:
        log.error(f"Could not reset golden rules: {e}")
        return False