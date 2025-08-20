# Koromali/app_core/update_manager.py
import requests
from packaging import version
from typing import Dict, List, Optional, TYPE_CHECKING
from PyQt6.QtCore import QObject, pyqtSignal

from utils.versioning import APP_VERSION
from utils.logger import log

if TYPE_CHECKING:
    from .settings_manager import SettingsManager


class UpdateManager(QObject):
    """
    Checks for new application versions from a configured GitHub repository.
    """
    update_check_finished = pyqtSignal(dict)

    def __init__(self, settings_manager: "SettingsManager", parent: Optional[QObject] = None):
        super().__init__(parent)
        self.settings_manager = settings_manager

    def _find_latest_release(self, releases: List[Dict]) -> Optional[Dict]:
        """
        Parses a list of release objects from the GitHub API and returns the
        one with the highest semantic version.
        """
        latest_release = None
        latest_parsed_version = version.parse("0.0.0")

        for release in releases:
            tag_name = release.get("tag_name", "").lstrip('v')
            if not tag_name:
                continue

            try:
                current_parsed_version = version.parse(tag_name)
                if current_parsed_version > latest_parsed_version:
                    latest_parsed_version = current_parsed_version
                    latest_release = release
            except version.InvalidVersion:
                log.warning(f"Skipping release with invalid tag version: {tag_name}")
                continue

        return latest_release

    def check_for_updates(self):
        """
        Fetches the latest release data from GitHub and compares it with the
        current application version. Emits `update_check_finished`.
        """
        log.info(f"Checking for updates... Current version: {APP_VERSION}")

        active_repo_id = self.settings_manager.get("active_update_repo_id")
        if not active_repo_id:
            msg = "No active repository set for updates in Preferences."
            log.warning(f"Update check failed: {msg}")
            self.update_check_finished.emit({"error": msg})
            return

        all_repos = self.settings_manager.get("source_control_repos", [])
        repo_config = next(
            (r for r in all_repos if r.get("id") == active_repo_id), None
        )

        if not repo_config:
            msg = f"Update repo with ID '{active_repo_id}' not found."
            log.error(f"Update check failed: {msg}")
            self.update_check_finished.emit({"error": msg})
            return

        owner = repo_config.get("owner")
        repo = repo_config.get("repo")

        if not owner or not repo:
            msg = f"Repo '{repo_config.get('name')}' is misconfigured."
            log.error(f"Update check failed: {msg}")
            self.update_check_finished.emit({"error": msg})
            return

        api_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
        log.info(f"Fetching release list from: {api_url}")

        try:
            response = requests.get(api_url, timeout=15)
            response.raise_for_status()

            release_data = self._find_latest_release(response.json())
            if not release_data:
                msg = "No valid releases found in the repository."
                log.warning(msg)
                self.update_check_finished.emit({"update_available": False, "message": msg})
                return

            latest_version_tag = release_data.get("tag_name", "").lstrip('v')
            if not latest_version_tag:
                msg = "Latest release has no version tag."
                self.update_check_finished.emit({"error": msg})
                return

            if version.parse(latest_version_tag) > version.parse(APP_VERSION):
                log.info(f"New version found: {latest_version_tag}")
                result: Dict = {
                    "update_available": True,
                    "latest_version": latest_version_tag,
                    "release_notes": release_data.get(
                        "body", "No release notes provided."
                    ),
                    "download_url": None
                }
                for asset in release_data.get("assets", []):
                    if asset.get("name", "").lower().endswith(".zip"):
                        result["download_url"] = asset.get(
                            "browser_download_url")
                        break

                if result["download_url"]:
                    self.update_check_finished.emit(result)
                else:
                    log.warning(
                        "New version found, but no suitable .zip asset "
                        "was available for download."
                    )
                    self.update_check_finished.emit(
                        {"update_available": False, "message": "Update found but no .zip file attached."})
            else:
                log.info("Application is up to date.")
                self.update_check_finished.emit({"update_available": False, "message": "You are on the latest version."})

        except requests.exceptions.HTTPError as e:
            msg = f"Could not fetch update info (HTTP {e.response.status_code})."
            log.error(f"{msg} URL: {api_url}")
            self.update_check_finished.emit({"error": msg})
        except requests.exceptions.RequestException as e:
            msg = f"Network error checking for updates: {e}"
            log.error(msg)
            self.update_check_finished.emit(
                {"error": "A network error occurred."})
        except Exception as e:
            msg = f"An unexpected error occurred during update check: {e}"
            log.critical(msg, exc_info=True)
            self.update_check_finished.emit(
                {"error": "An unexpected error occurred."})