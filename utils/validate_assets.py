# Koromali/utils/validate_assets.py
import os
import json
import re
from typing import List, Dict, Any, Tuple

# --- Configuration ---
# Adjust these paths if your project structure changes
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
CUSTOM_THEMES_FILE = os.path.join(ASSETS_DIR, "themes", "custom_themes.json")
THEME_MANAGER_FILE = os.path.join(ROOT_DIR, "app_core", "theme_manager.py")
BUILT_IN_THEMES_KEY = "BUILT_IN_THEMES"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def _print_header(title: str):
    print(f"\n{bcolors.HEADER}{bcolors.BOLD}===== {title.upper()} "
          f"====={bcolors.ENDC}")


def _load_json_file(filepath: str) -> Tuple[Any, List[str]]:
    """Loads a JSON file and returns its content and any errors found."""
    errors = []
    data = None
    if not os.path.exists(filepath):
        # This is not an error, the file might be optional
        return None, errors

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        err_msg = (f"Invalid JSON in '{os.path.basename(filepath)}':\n"
                   f"  {bcolors.FAIL}L{e.lineno}:C{e.colno} - {e.msg}"
                   f"{bcolors.ENDC}")
        errors.append(err_msg)
    except Exception as e:
        errors.append(f"Could not read '{os.path.basename(filepath)}': {e}")

    return data, errors


def get_built_in_themes_from_code(manager_file: str) -> Tuple[Dict, List[str]]:
    """
    Parses theme_manager.py to extract the BUILT_IN_THEMES dictionary.
    This is more robust than hardcoding keys.
    """
    themes = {}
    errors = []
    try:
        with open(manager_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the start of the dictionary
        start_index = content.find(f"{BUILT_IN_THEMES_KEY} = {")
        if start_index == -1:
            errors.append(f"Could not find '{BUILT_IN_THEMES_KEY}' dictionary in {os.path.basename(manager_file)}.")
            return {}, errors

        content = content[start_index + len(f"{BUILT_IN_THEMES_KEY} = "):]
        
        # Balance braces to find the end of the dictionary
        brace_count = 0
        end_index = -1
        for i, char in enumerate(content):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_index = i
                    break
        
        if end_index == -1:
            errors.append(f"Could not parse '{BUILT_IN_THEMES_KEY}' dictionary; unbalanced braces.")
            return {}, errors

        dict_str = content[:end_index+1]
        
        # The extracted string can be evaluated as a Python literal
        themes = eval(dict_str)
        
    except Exception as e:
        errors.append(f"Error parsing built-in themes from Python file: {e}")
        
    return themes, errors


def validate_json_syntax() -> Tuple[Dict, List[str]]:
    """Checks basic JSON syntax of theme files and loads all theme data."""
    _print_header("1. Theme Syntax and Data Loading")

    all_themes = {}
    all_errors = []

    # Load and validate built-in themes from theme_manager.py
    built_in_themes, errors = get_built_in_themes_from_code(THEME_MANAGER_FILE)
    all_errors.extend(errors)
    if built_in_themes:
        all_themes.update(built_in_themes)

    # Validate custom themes (if they exist)
    custom_data, errors = _load_json_file(CUSTOM_THEMES_FILE)
    all_errors.extend(errors)
    if custom_data:
        all_themes.update(custom_data)

    if not all_errors:
        print(f"{bcolors.OKGREEN}All built-in and custom theme files loaded and parsed successfully.{bcolors.ENDC}")

    return all_themes, all_errors


def get_required_color_keys_from_code(manager_file: str) -> set:
    """Extracts color keys from the QSS and custom drawing in theme_manager.py."""
    required_keys = set()
    if not os.path.exists(manager_file):
        return required_keys

    with open(manager_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find all instances of colors.get("some.key", ...)
    matches = re.findall(r'colors\.get\("([^"]+)"', content)
    for key in matches:
        required_keys.add(key)
        
    return required_keys


def validate_key_completeness(all_themes: Dict, required_keys: set) -> List[str]:
    """Checks if each theme defines all the keys required by the app."""
    _print_header("2. Color Key Completeness Validation")
    all_errors = []

    if not required_keys:
        msg = (f"{bcolors.FAIL}Could not find any required color keys "
               f"in ThemeManager. Check path or regex.{bcolors.ENDC}")
        all_errors.append(msg)
        return all_errors

    print(f"Found {len(required_keys)} required color keys in the code.")

    for theme_id, theme_data in all_themes.items():
        if 'colors' not in theme_data:
             all_errors.append(f"Theme '{bcolors.BOLD}{theme_id}{bcolors.ENDC}' is missing the entire 'colors' dictionary.")
             continue

        theme_keys = set(theme_data["colors"].keys())
        missing_keys = required_keys - theme_keys

        if missing_keys:
            all_errors.append(
                f"Theme '{bcolors.BOLD}{theme_id}{bcolors.ENDC}' "
                f"is missing {len(missing_keys)} required keys:"
            )
            for key in sorted(list(missing_keys)):
                all_errors.append(f"  - {bcolors.WARNING}{key}{bcolors.ENDC}")

    if not all_errors:
        print(f"{bcolors.OKGREEN}All themes have all required keys."
              f"{bcolors.ENDC}")

    return all_errors


def main():
    """Run all validation checks."""
    print(f"{bcolors.BOLD}Running Koromali Asset Validator..."
          f"{bcolors.ENDC}")

    all_themes, errors = validate_json_syntax()
    if errors:
        for error in errors:
            print(f"- {error}")
        print(f"\n{bcolors.FAIL}{bcolors.BOLD}Validation failed at Step 1. "
              f"Cannot continue.{bcolors.ENDC}")
        return 1

    required_keys = get_required_color_keys_from_code(THEME_MANAGER_FILE)
    errors.extend(validate_key_completeness(all_themes, required_keys))

    _print_header("Validation Summary")
    if errors:
        print(f"\n{bcolors.FAIL}{bcolors.BOLD}Validation finished with "
              f"{len(errors)} issue(s).{bcolors.ENDC}")
        for error in errors:
            print(f"- {error}")
        return 1
    else:
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}"
              f"All assets validated successfully!{bcolors.ENDC}")
        return 0


if __name__ == "__main__":
    sys.exit(main())