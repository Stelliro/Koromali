# Koromali/app_core/settings_manager.py
import json
import os
from typing import Any, Dict

from app_core.config import GITHUB_PLUGINS_REPO
from utils.logger import log, get_app_data_path

APP_DATA_ROOT = get_app_data_path()
SETTINGS_FILE = os.path.join(APP_DATA_ROOT, "Koromali_editor_settings.json")
CREDENTIALS_FILE = os.path.join(APP_DATA_ROOT, "credentials.json")

DEFAULT_SETTINGS = {
    "window_size": [1600, 1000], "window_position": None, "splitter_sizes": [300, 1300],
    "last_theme_id": "Koromali_modern_dark", "font_family": "Consolas", "font_size": 11,
    "show_line_numbers": True, "show_indentation_guides": True, "word_wrap": False,
    "indent_style": "spaces", "indent_width": 4, "auto_save_enabled": False,
    "auto_save_delay_seconds": 3, "max_recent_files": 15, "favorites": [],
    "open_files": [], "open_projects": [], "active_project_path": None, "project_sessions": {},
    "explorer_expanded_paths": [], "project_customizations": {},
    "explorer_show_hidden_files": False,
    "python_interpreter_path": "", "source_control_repos": [],
    "active_update_repo_id": None, "plugins_distro_repo": GITHUB_PLUGINS_REPO or "",
    "commit_message_history": [], "max_commit_history": 50, "ai_export_loadouts": {},
    "ai_export_golden_rules": {}, "cleanup_after_build": True, "nsis_path": "",
    "ai_tools_api_mode_enabled": False, "ai_tools_include_linter": True,
    "ai_studio_use_persona": True, "ai_studio_include_patcher_rules": True,
    "ai_studio_selections": {},
    "project_launch_scripts": {},
    "ai_default_model": "",
    "ai_api_keys": {},
}
DEFAULT_CREDENTIALS = {
    "github_access_token": None, "github_user": None, "github_user_info": None, "api_keys": {}
}

class SettingsManager:
    def __init__(self, settings_file: str = SETTINGS_FILE, credentials_file: str = CREDENTIALS_FILE):
        self.settings_file = settings_file
        self.credentials_file = credentials_file
        self.settings = self._load_json_with_defaults(self.settings_file, DEFAULT_SETTINGS)
        self.credentials = self._load_json_with_defaults(self.credentials_file, DEFAULT_CREDENTIALS)
        self._migrate_old_credentials()
        self._remove_deprecated_settings()

    def _load_json_with_defaults(self, filepath: str, defaults: Dict) -> Dict:
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    loaded_data = json.load(f)
                final_data = defaults.copy(); final_data.update(loaded_data)
                return final_data
            else:
                log.info(f"File not found. Creating with defaults at: {filepath}")
                self._save_json(filepath, defaults.copy()); return defaults.copy()
        except (json.JSONDecodeError, IOError) as e:
            log.error(f"Error loading {filepath}: {e}. Reverting to defaults.", exc_info=True)
            return defaults.copy()

    def _save_json(self, filepath: str, data: Dict):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            temp_file = filepath + ".tmp"
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            os.replace(temp_file, filepath)
        except IOError as e:
            log.error(f"Error saving to {filepath}: {e}", exc_info=True)
    
    def _migrate_old_credentials(self):
        migrated = False
        credential_keys = ["github_access_token", "github_user", "github_user_info", "api_keys"]
        for key in credential_keys:
            if key in self.settings:
                self.credentials[key] = self.settings.pop(key); migrated = True
        if migrated:
            log.info("Migrated credentials from main settings file to separate credentials.json.")
            self.save()

    def _remove_deprecated_settings(self):
        deprecated_keys = ["run_in_background"]
        removed = False
        for key in deprecated_keys:
            if key in self.settings:
                self.settings.pop(key, None)
                removed = True
        if removed:
            log.info("Removed deprecated startup settings from configuration file.")
            self.save()

    def get(self, key: str, default: Any = None) -> Any:
        if key in self.credentials: return self.credentials.get(key, default)
        return self.settings.get(key, DEFAULT_SETTINGS.get(key, default))

    def set(self, key: str, value: Any, save_immediately: bool = True):
        if key in DEFAULT_CREDENTIALS: self.credentials[key] = value
        else: self.settings[key] = value
        if save_immediately: self.save()

    def save(self):
        self._save_json(self.settings_file, self.settings)
        self._save_json(self.credentials_file, self.credentials)

    def clear_cached_data(self):
        """Resets settings that cache user session data, but preserves core configuration."""
        keys_to_clear = [
            "open_files",
            "open_projects",
            "active_project_path",
            "project_sessions",
            "explorer_expanded_paths",
            "project_customizations",
            "commit_message_history",
            "ai_export_loadouts",
            "ai_studio_selections",
            "recent_files"
        ]
        
        log.warning("Clearing cached user data from settings file.")
        for key in keys_to_clear:
            if key in self.settings:
                # Reset to default value from DEFAULT_SETTINGS
                self.settings[key] = DEFAULT_SETTINGS.get(key)
        
        self.save()