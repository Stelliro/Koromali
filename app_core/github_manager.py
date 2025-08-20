# Koromali/app_core/github_manager.py
import requests
import time
import os
import json
from typing import Dict, Optional, List, TYPE_CHECKING
from PyQt6.QtCore import QObject, QThread, pyqtSignal

from utils.versioning import APP_VERSION
from utils.logger import log

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager

CLIENT_ID = "178c6fc778ccc68e1d6a"
DEVICE_CODE_URL = "https://github.com/login/device/code"
ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"


class GitHubWorker(QObject):
    """
    Worker that runs all GitHub API requests in a background thread.
    """
    device_code_ready = pyqtSignal(dict)
    auth_successful = pyqtSignal(str)
    auth_failed = pyqtSignal(str)
    auth_polling_lapsed = pyqtSignal()
    repos_ready = pyqtSignal(list)
    branches_ready = pyqtSignal(list)
    plugin_index_ready = pyqtSignal(list)
    operation_success = pyqtSignal(str, dict)
    operation_failed = pyqtSignal(str)

    def __init__(self, settings_manager: "SettingsManager"):
        super().__init__()
        self.settings_manager = settings_manager
        self.access_token: Optional[str] = self.settings_manager.get(
            "github_access_token")
        self.user_agent = f"Koromali/{APP_VERSION}"

    def _get_headers(self) -> Dict[str, str]:
        """Constructs the standard headers for authenticated API requests."""
        return {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {self.access_token}",
            "User-Agent": self.user_agent
        }

    def start_device_flow(self):
        log.info("Starting GitHub device authorization flow.")
        try:
            headers = {"Accept": "application/json",
                       "User-Agent": self.user_agent}
            payload = {"client_id": CLIENT_ID, "scope": "repo user"}
            response = requests.post(
                DEVICE_CODE_URL, data=payload, headers=headers, timeout=30
            )
            response.raise_for_status()
            data = response.json()
            log.info(f"Received device code: {data.get('user_code')}")
            self.device_code_ready.emit(data)
        except requests.RequestException as e:
            log.error(f"Failed to start device flow: {e}", exc_info=True)
            self.auth_failed.emit(
                "Could not connect to GitHub. Check network and logs."
            )

    def poll_for_token(self, device_code: str, interval: int, expires_in: int):
        log.info("Polling for GitHub access token...")
        start_time = time.time()
        headers = {"Accept": "application/json", "User-Agent": self.user_agent}
        payload = {
            "client_id": CLIENT_ID,
            "device_code": device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
        }
        while time.time() - start_time < expires_in:
            try:
                response = requests.post(
                    ACCESS_TOKEN_URL, data=payload,
                    headers=headers, timeout=30
                )
                data = response.json()
                if "access_token" in data:
                    self.access_token = data["access_token"]
                    user_info = self._get_authenticated_user_info()
                    user_login = user_info.get("login") if user_info else "user"
                    self.settings_manager.set(
                        "github_access_token", self.access_token, False
                    )
                    self.settings_manager.set("github_user", user_login, False)
                    self.settings_manager.set(
                        "github_user_info", user_info, False
                    )
                    self.settings_manager.save()
                    log.info(
                        "Successfully authenticated as GitHub user: "
                        f"{user_login}"
                    )
                    self.auth_successful.emit(user_login)
                    return
                elif data.get("error") == "authorization_pending":
                    time.sleep(interval)
                else:
                    error_desc = data.get(
                        "error_description", "Unknown authentication error"
                    )
                    log.error(f"GitHub authentication error: {error_desc}")
                    self.auth_failed.emit(error_desc)
                    return
            except requests.RequestException as e:
                log.error(f"Exception while polling for token: {e}",
                          exc_info=True)
                self.auth_failed.emit(f"Network error during auth: {e}")
                return
        log.warning("Device flow expired before user authorized.")
        self.auth_polling_lapsed.emit()

    def _get_authenticated_user_info(self) -> Optional[Dict]:
        if not self.access_token:
            return None
        try:
            response = requests.get(
                "https://api.github.com/user",
                headers=self._get_headers(), timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            log.error(f"Failed to get user info from GitHub: {e}")
            return None

    def _paginated_request(self, url: str) -> List[Dict]:
        """Helper to handle paginated GitHub API requests."""
        all_items = []
        page = 1
        while True:
            paginated_url = f"{url}?page={page}&per_page=100"
            response = requests.get(
                paginated_url, headers=self._get_headers(), timeout=30
            )
            response.raise_for_status()
            data = response.json()
            if not data:
                break
            all_items.extend(data)
            page += 1
        return all_items

    def list_user_repos(self):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        try:
            all_repos = self._paginated_request("https://api.github.com/user/repos")
            self.repos_ready.emit(sorted(all_repos, key=lambda r: r.get('pushed_at', ''), reverse=True))
        except requests.RequestException as e:
            self.operation_failed.emit(f"Failed to list repositories: {e}")

    def list_repo_branches(self, full_repo_name: str):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        try:
            url = f"https://api.github.com/repos/{full_repo_name}/branches"
            response = requests.get(
                url, headers=self._get_headers(), timeout=30
            )
            response.raise_for_status()
            self.branches_ready.emit(response.json())
        except requests.RequestException as e:
            self.operation_failed.emit(
                f"Failed to list branches for {full_repo_name}: {e}")

    def create_github_release(self, owner: str, repo: str, tag_name: str,
                              name: str, body: str, prerelease: bool):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        url = f"https://api.github.com/repos/{owner}/{repo}/releases"
        payload = {"tag_name": tag_name, "name": name, "body": body,
                   "prerelease": prerelease}
        try:
            response = requests.post(
                url, headers=self._get_headers(), json=payload, timeout=30
            )
            response.raise_for_status()
            self.operation_success.emit(
                "Release created", {"release_data": response.json()}
            )
        except requests.exceptions.HTTPError as e:
            msg = f"HTTP {e.response.status_code}: "
            try:
                error_body = e.response.json()
                errs = error_body.get('errors', [])
                if any(err.get('code') == 'already_exists' for err in errs):
                    msg += f"A release for tag '{tag_name}' already exists."
                else:
                    msg += error_body.get(
                        'message', 'Failed to create release.'
                    )
            except json.JSONDecodeError:
                msg += "Failed to create GitHub release."
            self.operation_failed.emit(msg)
        except requests.RequestException as e:
            self.operation_failed.emit(f"Failed to create GitHub release: {e}")

    def upload_release_asset(self, upload_url: str, asset_path: str):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        upload_url = upload_url.split('{')[0]
        asset_name = os.path.basename(asset_path)
        headers = self._get_headers()
        headers['Content-Type'] = 'application/octet-stream'
        try:
            with open(asset_path, 'rb') as f:
                data = f.read()
            response = requests.post(
                f"{upload_url}?name={asset_name}",
                headers=headers, data=data, timeout=300
            )
            response.raise_for_status()
            self.operation_success.emit(
                "Asset uploaded", {"asset_data": response.json()}
            )
        except (requests.RequestException, IOError) as e:
            self.operation_failed.emit(f"Failed to upload asset: {e}")

    def delete_release(self, owner: str, repo: str, release_id: int):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        url = (f"https://api.github.com/repos/{owner}/{repo}/releases/"
               f"{release_id}")
        log.info(f"ROLLBACK: Attempting to delete release at {url}")
        try:
            response = requests.delete(
                url, headers=self._get_headers(), timeout=30
            )
            response.raise_for_status()
            self.operation_success.emit(
                "Release deleted", {"release_id": release_id}
            )
        except requests.RequestException as e:
            msg = f"Failed to delete release: {e}"
            if hasattr(e, 'response') and e.response:
                msg += f" (Status: {e.response.status_code})"
            self.operation_failed.emit(msg)

    def create_repo(self, name: str, description: str, is_private: bool):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        api_url = "https://api.github.com/user/repos"
        payload = {"name": name, "description": description,
                   "private": is_private}
        try:
            response = requests.post(
                api_url, headers=self._get_headers(), json=payload, timeout=30
            )
            response.raise_for_status()
            self.operation_success.emit(
                f"Repository '{name}' created.", response.json()
            )
        except requests.RequestException as e:
            error_msg = e.response.json().get('message', str(e)) if hasattr(e, 'response') and e.response else str(e)
            self.operation_failed.emit(
                f"Failed to create repository: {error_msg}")

    def fetch_plugin_index(self, repo_path: str):
        url = f"https://raw.githubusercontent.com/{repo_path}/main/index.json"
        log.info(f"Fetching plugin index from: {url}")
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            self.plugin_index_ready.emit(response.json())
        except requests.RequestException as e:
            self.operation_failed.emit(f"Failed to fetch plugin index: {e}")
        except json.JSONDecodeError:
            self.operation_failed.emit(
                "Invalid plugin index format (not valid JSON).")

    def update_repo_visibility(self, owner: str, repo: str, is_private: bool):
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        payload = {"private": is_private}
        try:
            response = requests.patch(
                api_url, headers=self._get_headers(), json=payload, timeout=30
            )
            response.raise_for_status()
            visibility = "private" if is_private else "public"
            self.operation_success.emit(
                f"Repository visibility changed to {visibility}.",
                response.json()
            )
        except requests.RequestException as e:
            error_msg = e.response.json().get('message', str(e)) if hasattr(e, 'response') and e.response else str(e)
            self.operation_failed.emit(
                f"Failed to change visibility: {error_msg}")

    def update_repo(self, owner: str, repo: str, payload: dict):
        """Generic method to update a repository using a PATCH request."""
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        log.info(f"Sending PATCH to {api_url} with payload: {payload}")
        try:
            response = requests.patch(
                api_url, headers=self._get_headers(), json=payload, timeout=30
            )
            response.raise_for_status()
            new_data = response.json()
            self.operation_success.emit(
                "Repository updated.",
                {"operation": "update", "repo_data": new_data}
            )
        except requests.RequestException as e:
            error_msg = e.response.json().get('message', str(e)) if hasattr(e, 'response') and e.response else str(e)
            self.operation_failed.emit(f"Failed to update repository: {error_msg}")

    def list_repo_tags(self, owner: str, repo: str) -> List[Dict]:
        """Fetches all tags for a repository."""
        url = f"https://api.github.com/repos/{owner}/{repo}/tags"
        return self._paginated_request(url)

    def list_repo_releases(self, owner: str, repo: str) -> List[Dict]:
        """Fetches all releases for a repository."""
        url = f"https://api.github.com/repos/{owner}/{repo}/releases"
        return self._paginated_request(url)

    def delete_remote_tag_ref(self, owner: str, repo: str, tag: str) -> bool:
        """Deletes a tag reference from the remote repository."""
        url = f"https://api.github.com/repos/{owner}/{repo}/git/refs/tags/{tag}"
        try:
            response = requests.delete(url, headers=self._get_headers(), timeout=30)
            response.raise_for_status()
            log.info(f"Successfully deleted remote tag ref: {tag}")
            return True
        except requests.RequestException as e:
            log.error(f"Failed to delete tag '{tag}': {e}")
            return False

    def cleanup_orphaned_tags(self, owner: str, repo: str):
        """Finds and deletes tags that are not associated with any release."""
        if not self.access_token:
            self.operation_failed.emit("Not logged in to GitHub.")
            return

        try:
            log.info(f"Starting orphaned tag cleanup for {owner}/{repo}")
            all_tags_data = self.list_repo_tags(owner, repo)
            all_releases_data = self.list_repo_releases(owner, repo)

            all_tag_names = {tag['name'] for tag in all_tags_data}
            release_tag_names = {rel['tag_name'] for rel in all_releases_data}

            orphaned_tags = all_tag_names - release_tag_names
            log.info(f"Found {len(orphaned_tags)} orphaned tags: {orphaned_tags}")

            if not orphaned_tags:
                self.operation_success.emit("No orphaned tags found to clean up.", {})
                return

            deleted_tags, failed_tags = [], []
            for tag in orphaned_tags:
                if self.delete_remote_tag_ref(owner, repo, tag):
                    deleted_tags.append(tag)
                else:
                    failed_tags.append(tag)

            summary_lines = []
            if deleted_tags:
                summary_lines.append(f"Successfully deleted {len(deleted_tags)} orphaned tags: {', '.join(deleted_tags)}")
            if failed_tags:
                summary_lines.append(f"Failed to delete {len(failed_tags)} tags: {', '.join(failed_tags)}")

            final_message = "\n".join(summary_lines)
            if failed_tags:
                self.operation_failed.emit(final_message)
            else:
                self.operation_success.emit(final_message, {"deleted_tags": deleted_tags})

        except requests.RequestException as e:
            self.operation_failed.emit(f"Failed to fetch repo data for cleanup: {e}")
        except Exception as e:
            log.error(f"Unexpected error during tag cleanup: {e}", exc_info=True)
            self.operation_failed.emit("An unexpected error occurred during cleanup.")


class GitHubManager(QObject):
    """
    Manages all interaction with the GitHub API by delegating to a background
    worker thread.
    """
    device_code_ready = pyqtSignal(dict)
    auth_successful = pyqtSignal(str)
    auth_failed = pyqtSignal(str)
    auth_polling_lapsed = pyqtSignal()
    repos_ready = pyqtSignal(list)
    branches_ready = pyqtSignal(list)
    plugin_index_ready = pyqtSignal(list)
    operation_success = pyqtSignal(str, dict)
    operation_failed = pyqtSignal(str)

    _start_device_flow = pyqtSignal()
    _poll_for_token = pyqtSignal(str, int, int)
    _request_repos = pyqtSignal()
    _request_branches = pyqtSignal(str)
    _request_create_repo = pyqtSignal(str, str, bool)
    _request_create_release = pyqtSignal(str, str, str, str, str, bool)
    _request_upload_asset = pyqtSignal(str, str)
    _request_update_visibility = pyqtSignal(str, str, bool)
    _request_update_repo = pyqtSignal(str, str, dict)
    _request_plugin_index = pyqtSignal(str)
    _request_delete_release = pyqtSignal(str, str, int)
    _request_cleanup_tags = pyqtSignal(str, str)

    def __init__(self, settings_manager: "SettingsManager", parent: Optional[QObject] = None):
        super().__init__(parent)
        self.settings_manager = settings_manager
        self.thread = QThread()
        self.worker = GitHubWorker(self.settings_manager)
        self.worker.moveToThread(self.thread)
        self.user_info = self.settings_manager.get("github_user_info")
        log.info(f"Loaded stored GitHub user info on startup: "
                 f"{bool(self.user_info)}")

        self._start_device_flow.connect(self.worker.start_device_flow)
        self._poll_for_token.connect(self.worker.poll_for_token)
        self._request_repos.connect(self.worker.list_user_repos)
        self._request_branches.connect(self.worker.list_repo_branches)
        self._request_create_repo.connect(self.worker.create_repo)
        self._request_create_release.connect(self.worker.create_github_release)
        self._request_upload_asset.connect(self.worker.upload_release_asset)
        self._request_update_visibility.connect(
            self.worker.update_repo_visibility)
        self._request_update_repo.connect(self.worker.update_repo)
        self._request_plugin_index.connect(self.worker.fetch_plugin_index)
        self._request_delete_release.connect(self.worker.delete_release)
        self._request_cleanup_tags.connect(self.worker.cleanup_orphaned_tags)

        self.worker.device_code_ready.connect(self.device_code_ready)
        self.worker.auth_successful.connect(self._on_auth_successful)
        self.worker.auth_failed.connect(self.auth_failed)
        self.worker.auth_polling_lapsed.connect(self.auth_polling_lapsed)
        self.worker.repos_ready.connect(self.repos_ready)
        self.worker.branches_ready.connect(self.branches_ready)
        self.worker.plugin_index_ready.connect(self.plugin_index_ready)
        self.worker.operation_success.connect(self.operation_success)
        self.worker.operation_failed.connect(self.operation_failed)

        self.thread.start()

    def _on_auth_successful(self, username: str):
        self.user_info = self.settings_manager.get("github_user_info")
        log.info(
            f"Authentication successful. Loaded user info for {username}.")
        self.auth_successful.emit(username)

    def get_authenticated_user(self) -> Optional[str]:
        return self.settings_manager.get("github_user")

    def get_user_info(self) -> Optional[Dict]:
        return self.user_info

    def get_active_repo_config(self) -> Optional[Dict]:
        """
        Retrieves the configuration dictionary for the repo marked as active.
        This is the single source of truth for the project's main repository.

        Returns:
            A dictionary with 'owner' and 'repo' keys, or None if not set.
        """
        active_repo_id = self.settings_manager.get("active_update_repo_id")
        if not active_repo_id:
            return None

        all_repos = self.settings_manager.get("source_control_repos", [])
        active_repo_config = next(
            (r for r in all_repos if r.get("id") == active_repo_id), None
        )
        return active_repo_config

    def start_device_flow(self):
        self._start_device_flow.emit()

    def poll_for_token(self, device_code: str, interval: int, expires_in: int):
        self._poll_for_token.emit(device_code, interval, expires_in)

    def logout(self):
        self.settings_manager.set("github_access_token", None, False)
        self.settings_manager.set("github_user", None, False)
        self.settings_manager.set("github_user_info", None, False)
        self.settings_manager.save()
        self.worker.access_token = None
        self.user_info = None
        log.info("Logged out of GitHub and cleared session data.")

    def list_repos(self):
        self._request_repos.emit()

    def list_branches(self, full_repo_name: str):
        self._request_branches.emit(full_repo_name)

    def create_repo(self, name: str, description: str, is_private: bool):
        self._request_create_repo.emit(name, description, is_private)

    def create_github_release(self, owner: str, repo: str, tag_name: str,
                              name: str, body: str, prerelease: bool):
        self._request_create_release.emit(
            owner, repo, tag_name, name, body, prerelease
        )

    def upload_asset(self, upload_url: str, asset_path: str):
        self._request_upload_asset.emit(upload_url, asset_path)

    def delete_release(self, owner: str, repo: str, release_id: int):
        self._request_delete_release.emit(owner, repo, release_id)

    def update_repo_visibility(self, owner: str, repo: str, is_private: bool):
        self._request_update_visibility.emit(owner, repo, is_private)

    def update_repo(self, owner: str, repo: str, payload: dict):
        self._request_update_repo.emit(owner, repo, payload)

    def fetch_plugin_index(self, repo_path: str):
        self._request_plugin_index.emit(repo_path)
        
    def cleanup_orphaned_tags(self, owner: str, repo: str):
        """Requests a cleanup of orphaned tags for the specified repository."""
        self._request_cleanup_tags.emit(owner, repo)

    def shutdown(self):
        if self.thread and self.thread.isRunning():
            log.info("Shutting down GitHubManager thread.")
            self.thread.quit()
            if not self.thread.wait(3000):
                log.warning(
                    "GitHubManager thread did not shut down "
                    "gracefully. Terminating."
                )
                self.thread.terminate()