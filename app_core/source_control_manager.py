# /app_core/source_control_manager.py
import os
import re
import git
from git import Repo, GitCommandError, InvalidGitRepositoryError, Actor
from typing import List, Optional
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from utils.logger import log
import configparser


class GitWorker(QObject):
    """
    Worker that runs all GitPython operations in a background thread.
    """
    summaries_ready = pyqtSignal(dict)
    status_ready = pyqtSignal(list, list, list, str)
    error_occurred = pyqtSignal(str)
    dubious_ownership_detected = pyqtSignal(str)
    operation_success = pyqtSignal(str, dict)
    git_config_ready = pyqtSignal(str, str)

    def _get_commit_author(self, repo: Repo) -> Optional[Actor]:
        """Gets the commit author from the repository's configuration."""
        try:
            with repo.config_reader() as cr:
                name = cr.get_value('user', 'name', None)
                email = cr.get_value('user', 'email', None)
            if name and email:
                return Actor(name, email)
            git_cmd = git.Git(repo.working_dir)
            global_name = git_cmd.config('--global', '--get', 'user.name')
            global_email = git_cmd.config('--global', '--get', 'user.email')
            if global_name and global_email:
                return Actor(global_name, global_email)
            return None
        except Exception as e:
            log.error(f"Could not retrieve commit author: {e}")
            return None

    def get_git_config(self):
        """Reads the global Git user configuration."""
        try:
            git_cmd = git.Git()
            name = git_cmd.config('--global', '--get', 'user.name')
            email = git_cmd.config('--global', '--get', 'user.email')
            self.git_config_ready.emit(name, email)
        except GitCommandError:
            log.warning("Global Git user.name or user.email is not set.")
            self.git_config_ready.emit("", "")

    def set_git_config(self, name: str, email: str):
        """Sets the global Git user configuration."""
        try:
            git_cmd = git.Git()
            if name:
                git_cmd.config('--global', 'user.name', name)
            if email:
                git_cmd.config('--global', 'user.email', email)
            self.operation_success.emit("Global Git config updated.", {})
        except GitCommandError as e:
            log.error(f"Failed to set git config: {e}")
            self.error_occurred.emit(f"Failed to set Git config: {e}")

    def add_safe_directory(self, path: str):
        """Adds a directory to Git's global safe.directory list."""
        try:
            git.Git().config('--global', '--add', 'safe.directory', path)
            log.info(f"Added '{path}' to global git safe.directory list.")
            self.operation_success.emit(f"Marked '{os.path.basename(path)}' as a safe repository.", {'repo_path': path})
        except GitCommandError as e:
            log.error(f"Failed to add safe directory: {e}")
            self.error_occurred.emit(f"Failed to mark repository as safe: {e}")

    def set_default_branch(self):
        """Sets the global Git config to use 'main' for new repositories."""
        try:
            git.Git().config('--global', 'init.defaultBranch', 'main')
            log.info("Set global init.defaultBranch to 'main'.")
            self.operation_success.emit(
                "Default branch for new repos is now 'main'.", {}
            )
        except GitCommandError as e:
            self.error_occurred.emit(f"Could not set default branch: {e}")

    def get_multiple_repo_summaries(self, repo_paths: List[str]):
        summaries = {}
        for path in repo_paths:
            try:
                repo = Repo(path, search_parent_directories=True)
                if repo.bare:
                    summaries[path] = {'branch': '(bare repo)',
                                       'commit': 'N/A'}
                elif not repo.head.is_valid():
                    summaries[path] = {'branch': '(no commits)',
                                       'commit': 'N/A'}
                else:
                    summaries[path] = {
                        'branch': repo.active_branch.name,
                        'commit': repo.head.commit.hexsha[:7]
                    }
            except InvalidGitRepositoryError:
                pass
            except Exception as e:
                log.error(f"Error getting Git summary for {path}: {e}")
                summaries[path] = {'branch': '(error)', 'commit': 'N/A'}
        self.summaries_ready.emit(summaries)

    def get_status(self, repo_path: str):
        try:
            repo = Repo(repo_path)
            staged = [item.a_path for item in repo.index.diff('HEAD')]
            unstaged = [item.a_path for item in repo.index.diff(None)]
            untracked = repo.untracked_files
            conflicted = [path for path, _ in repo.index.unmerged_blobs().items()]
            self.status_ready.emit(staged, unstaged + untracked, conflicted, repo_path)
        except GitCommandError as e:
            stderr_lower = str(e.stderr).lower()
            if "dubious ownership" in stderr_lower:
                log.warning(f"Git 'dubious ownership' error detected for {repo_path}")
                self.dubious_ownership_detected.emit(repo_path)
            else:
                err_msg = (
                    f"Git Status for '{os.path.basename(repo_path)}' "
                    f"failed: {e.stderr.strip()}"
                )
                self.error_occurred.emit(err_msg)
        except (InvalidGitRepositoryError, ValueError) as e:
            err_msg = (
                f"Git Status for '{os.path.basename(repo_path)}' "
                f"failed: {e}"
            )
            self.error_occurred.emit(err_msg)

    def commit_files(self, repo_path: str, message: str):
        try:
            repo = Repo(repo_path)
            author = self._get_commit_author(repo)
            if not author:
                self.error_occurred.emit(
                    "Commit author not found. Please set user.name and user.email in your Git config.")
                return

            repo.git.add(A=True)
            if repo.is_dirty(untracked_files=True):
                repo.index.commit(message, author=author, committer=author)
                self.operation_success.emit(
                    "Changes committed", {'repo_path': repo_path}
                )
            else:
                self.operation_success.emit(
                    "No new changes to commit.",
                    {'repo_path': repo_path, 'no_changes': True}
                )
        except InvalidGitRepositoryError:
            self.error_occurred.emit(f"'{os.path.basename(repo_path)}' is not a valid Git repository.")
        except GitCommandError as e:
            self.error_occurred.emit(f"Git Commit failed: {e.stderr}")

    def push(self, repo_path: str, tag_name: Optional[str] = None):
        try:
            repo = Repo(repo_path)
            origin = repo.remotes.origin
            if tag_name:
                log.info(f"Pushing tag '{tag_name}' to remote '{origin.url}'...")
                origin.push(tag_name)
                self.operation_success.emit(
                    f"Tag '{tag_name}' pushed successfully", {}
                )
            else:
                active_branch = repo.active_branch.name
                log.info(
                    f"Pushing branch '{active_branch}' to remote "
                    f"'{origin.url}'..."
                )
                origin.push(refspec=f'{active_branch}:{active_branch}')
                self.operation_success.emit("Push successful", {})
        except InvalidGitRepositoryError:
            self.error_occurred.emit(f"'{os.path.basename(repo_path)}' is not a valid Git repository.")
        except GitCommandError as e:
            stderr = str(e.stderr).lower()
            if "updates were rejected" in stderr:
                msg = ("Push rejected because the remote has changes you do not have locally. "
                       "Please 'Pull' changes from the remote, resolve any conflicts, and then try pushing again.")
            elif "authentication failed" in stderr:
                msg = ("Authentication failed. Please ensure you have configured a "
                       "Git Credential Manager or are using SSH for your remote URL. "
                       "Using passwords over HTTPS is not supported by GitHub.")
            elif "could not read from remote repository" in stderr:
                msg = ("Could not read from remote repository. Please ensure the URL "
                       "is correct and you have permission to access it.")
            elif "src refspec" in stderr and "does not match any" in stderr:
                msg = ("The local branch does not exist or does not match a remote "
                       "branch. You may need to publish the branch first.")
            else:
                msg = f"Git Push failed. Stderr: {e.stderr.strip()}"
            self.error_occurred.emit(msg)

    def pull(self, repo_path: str):
        try:
            repo = Repo(repo_path)
            origin = repo.remotes.origin
            log.info(f"Pulling from remote '{origin.url}'...")
            origin.pull()
            self.operation_success.emit("Pull successful", {})
            self.get_status(repo_path)
        except InvalidGitRepositoryError:
            self.error_occurred.emit(f"'{os.path.basename(repo_path)}' is not a valid Git repository.")
        except GitCommandError as e:
            stderr = str(e.stderr).lower()
            if "authentication failed" in stderr:
                msg = ("Authentication failed. Please ensure you have configured a "
                       "Git Credential Manager or are using SSH for your remote URL.")
            elif "you have unstaged changes" in stderr or "your local changes to the following files would be overwritten" in stderr:
                msg = "Pull failed. You have local changes that would be overwritten. Please commit or stash them first."
            elif "pull is not possible because you have unmerged files" in stderr:
                msg = "Pull failed because you have unresolved merge conflicts. Please resolve the conflicts, commit the result, and then try again."
            else:
                msg = f"Git Pull failed. Stderr: {e.stderr.strip()}"
            self.error_occurred.emit(msg)

    def force_push(self, repo_path: str):
        """Force pushes the current branch to the remote."""
        try:
            repo = Repo(repo_path)
            origin = repo.remotes.origin
            log.warning(f"FORCE PUSHING branch '{repo.active_branch.name}' to '{origin.url}'")
            origin.push(force=True)
            self.operation_success.emit("Force push successful.", {})
        except GitCommandError as e:
            self.error_occurred.emit(f"Force Push failed: {e.stderr.strip()}")

    def abort_merge(self, repo_path: str):
        """Aborts a conflicted merge state."""
        try:
            repo = Repo(repo_path)
            if os.path.exists(os.path.join(repo.git_dir, 'MERGE_HEAD')):
                log.info(f"Aborting merge in {repo_path}")
                repo.git.merge('--abort')
                self.operation_success.emit("Merge successfully aborted.", {})
            else:
                self.error_occurred.emit("No active merge to abort.")
        except GitCommandError as e:
            self.error_occurred.emit(f"Failed to abort merge: {e.stderr.strip()}")

    def clone_repo(self, url: str, path: str, branch: Optional[str] = None):
        try:
            target_dir = os.path.join(
                path, os.path.basename(url).replace('.git', '')
            )
            kwargs = {'branch': branch} if branch else {}
            log_msg = (
                f"Cloning '{url}' (branch: {branch or 'default'}) "
                f"into '{target_dir}'"
            )
            log.info(log_msg)
            Repo.clone_from(url, target_dir, **kwargs)
            self.operation_success.emit(
                "Clone successful", {"path": target_dir}
            )
        except GitCommandError as e:
            err_str = str(e).lower()
            if "not found in upstream origin" in err_str:
                msg = f"Branch '{branch}' not found in the remote repository."
            elif "authentication failed" in err_str:
                msg = ("Authentication failed. Repository may be private or "
                       "URL is incorrect.")
            else:
                msg = f"Clone failed: {e}"
            self.error_occurred.emit(msg)

    def create_tag(self, repo_path: str, tag: str, title: str):
        try:
            repo = Repo(repo_path)
            author = self._get_commit_author(repo)
            if not author:
                self.error_occurred.emit(
                    "Commit author not found. Please set user.name and user.email in your Git config.")
                return

            if not repo.head.is_valid():
                log.info("No commits found. Creating initial commit.")
                gitignore_path = os.path.join(repo_path, ".gitignore")
                if not os.path.exists(gitignore_path):
                    with open(gitignore_path, 'w', encoding='utf-8') as f:
                        f.write(
                            "# Python\n__pycache__/\n*.pyc\n\n# Env\n.env\nvenv/\n.venv/\n\n# Build\nbuild/\ndist/\n*.egg-info/\n")
                repo.git.add(A=True)
                if repo.is_dirty(untracked_files=True):
                    repo.index.commit("Initial commit", author=author, committer=author)
                else:
                    self.error_occurred.emit("Cannot tag an empty project with no changes to commit.")
                    return

            if tag in repo.tags:
                log.warning(f"Tag '{tag}' already exists. Re-creating it.")
                repo.delete_tag(tag)

            repo.create_tag(tag, message=title)
            self.operation_success.emit(f"Tag created: {tag}", {})
        except GitCommandError as e:
            self.error_occurred.emit(f"Failed to create tag: {e}")

    def delete_tag(self, repo_path: str, tag: str):
        try:
            repo = Repo(repo_path)
            repo.delete_tag(tag)
            self.operation_success.emit(f"Local tag '{tag}' deleted.", {})
        except GitCommandError as e:
            self.error_occurred.emit(f"Failed to delete local tag '{tag}': {e}")

    def delete_remote_tag(self, repo_path: str, tag: str):
        try:
            repo = Repo(repo_path)
            repo.remotes.origin.push(refspec=f":{tag}")
            self.operation_success.emit(f"Remote tag '{tag}' deleted.", {})
        except GitCommandError as e:
            self.error_occurred.emit(
                f"Failed to delete remote tag '{tag}': {e}"
            )

    def publish_repo(self, path: str, url: str):
        try:
            repo = Repo.init(path)
            author = self._get_commit_author(repo)
            if not author:
                self.error_occurred.emit(
                    "Could not determine commit author to publish. Please configure Git user.name and user.email.")
                return

            repo.git.branch('-M', 'main')
            if (repo.is_dirty(untracked_files=True) and
                    not repo.head.is_valid()):
                repo.git.add(A=True)
                repo.index.commit(
                    "Initial commit", author=author, committer=author
                )
            if 'origin' in repo.remotes:
                repo.remotes.origin.set_url(url)
            else:
                repo.create_remote('origin', url)
            repo.remotes.origin.push(refspec='main:main', set_upstream=True)
            self.operation_success.emit(
                f"Successfully published to {url}", {'repo_path': path}
            )
        except (GitCommandError, configparser.Error) as e:
            log.error(f"Publish failed: {e}", exc_info=True)
            self.error_occurred.emit(f"Publish failed: {e}")

    def link_to_remote(self, local_path: str, remote_url: str):
        try:
            repo = Repo.init(local_path)
            if 'origin' in repo.remotes:
                repo.remotes.origin.set_url(remote_url)
            else:
                repo.create_remote('origin', remote_url)
            repo.remotes.origin.fetch()
            remote_head = repo.remote().refs.HEAD
            if remote_head.is_valid():
                branch_name = remote_head.reference.name.split('/')[-1]
            else:
                branch_name = 'main'
            repo.git.branch('-M', branch_name)
            if remote_head.is_valid():
                repo.git.reset('--soft', f'origin/{branch_name}')
            if (repo.is_dirty(untracked_files=True) and
                    not repo.head.is_valid()):
                author = self._get_commit_author(repo)
                if not author:
                    self.error_occurred.emit(
                        "Could not determine commit author. Please configure Git user.name and user.email.")
                    return
                repo.git.add(A=True)
                repo.index.commit(
                    "Initial commit after linking to remote",
                    author=author, committer=author
                )
            self.operation_success.emit(
                f"Successfully linked to {remote_url}", {}
            )
        except (GitCommandError, configparser.Error) as e:
            self.error_occurred.emit(f"Failed to link repository: {e}")

    def fix_main_master_divergence(self, repo_path: str):
        try:
            repo = Repo(repo_path)
            log.info(f"Fixing branch mismatch in {repo_path}")
            repo.git.branch('-M', 'master', 'main')
            repo.git.push('--force', '-u', 'origin', 'main')
            repo.git.push('origin', '--delete', 'master')
            self.operation_success.emit(
                "'main' is now the primary branch.", {'repo_path': repo_path}
            )
        except GitCommandError as e:
            self.error_occurred.emit(f"Failed to fix branch mismatch: {e}")


class SourceControlManager(QObject):
    summaries_ready = pyqtSignal(dict)
    status_updated = pyqtSignal(list, list, list, str)
    git_error = pyqtSignal(str)
    dubious_ownership_detected = pyqtSignal(str)
    git_success = pyqtSignal(str, dict)
    git_config_ready = pyqtSignal(str, str)

    _request_summaries = pyqtSignal(list)
    _request_status = pyqtSignal(str)
    _request_commit = pyqtSignal(str, str)
    _request_push = pyqtSignal(str, str)
    _request_pull = pyqtSignal(str)
    _request_clone = pyqtSignal(str, str, object)
    _request_publish = pyqtSignal(str, str)
    _request_create_tag = pyqtSignal(str, str, str)
    _request_delete_tag = pyqtSignal(str, str)
    _request_delete_remote_tag = pyqtSignal(str, str)
    _request_link_to_remote = pyqtSignal(str, str)
    _request_get_git_config = pyqtSignal()
    _request_set_git_config = pyqtSignal(str, str)
    _request_fix_branches = pyqtSignal(str)
    _request_set_default_branch = pyqtSignal()
    _request_force_push = pyqtSignal(str)
    _request_abort_merge = pyqtSignal(str)
    _request_add_safe_directory = pyqtSignal(str)

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)
        self.thread = QThread()
        self.worker = GitWorker()
        self.worker.moveToThread(self.thread)
        self._request_summaries.connect(self.worker.get_multiple_repo_summaries)
        self._request_status.connect(self.worker.get_status)
        self._request_commit.connect(self.worker.commit_files)
        self._request_push.connect(self.worker.push)
        self._request_pull.connect(self.worker.pull)
        self._request_clone.connect(self.worker.clone_repo)
        self._request_publish.connect(self.worker.publish_repo)
        self._request_create_tag.connect(self.worker.create_tag)
        self._request_delete_tag.connect(self.worker.delete_tag)
        self._request_delete_remote_tag.connect(self.worker.delete_remote_tag)
        self._request_link_to_remote.connect(self.worker.link_to_remote)
        self._request_get_git_config.connect(self.worker.get_git_config)
        self._request_set_git_config.connect(self.worker.set_git_config)
        self._request_fix_branches.connect(
            self.worker.fix_main_master_divergence)
        self._request_set_default_branch.connect(
            self.worker.set_default_branch)
        self._request_force_push.connect(self.worker.force_push)
        self._request_abort_merge.connect(self.worker.abort_merge)
        self._request_add_safe_directory.connect(self.worker.add_safe_directory)

        self.worker.summaries_ready.connect(self.summaries_ready)
        self.worker.status_ready.connect(self.status_updated)
        self.worker.error_occurred.connect(self.git_error)
        self.worker.dubious_ownership_detected.connect(self.dubious_ownership_detected)
        self.worker.operation_success.connect(self.git_success)
        self.worker.git_config_ready.connect(self.git_config_ready)
        self.thread.start()

    @staticmethod
    def parse_git_url(url: str) -> tuple[Optional[str], Optional[str]]:
        if match := re.search(r"github\.com/([^/]+)/([^/.]+)", url):
            return match.group(1), match.group(2)
        if match := re.search(r"github\.com:([^/]+)/([^/.]+)", url):
            return match.group(1), match.group(2)
        return None, None

    def _get_commit_author(self, repo_path: str) -> Optional[Actor]:
        try:
            repo = Repo(repo_path)
            return self.worker._get_commit_author(repo)
        except Exception:
            return None

    def get_local_branches(self, repo_path: str) -> List[str]:
        try:
            return [b.name for b in Repo(repo_path).branches]
        except (InvalidGitRepositoryError, TypeError):
            return []

    def get_git_config(self):
        self._request_get_git_config.emit()

    def set_git_config(self, name: str, email: str):
        self._request_set_git_config.emit(name, email)

    def add_safe_directory(self, path: str):
        self._request_add_safe_directory.emit(path)

    def set_default_branch_to_main(self):
        self._request_set_default_branch.emit()

    def link_to_remote(self, path: str, url: str):
        self._request_link_to_remote.emit(path, url)

    def fix_branch_mismatch(self, path: str):
        self._request_fix_branches.emit(path)

    def get_summaries(self, paths: List[str]):
        self._request_summaries.emit(paths)

    def get_status(self, path: str):
        self._request_status.emit(path)

    def commit_files(self, path: str, msg: str):
        self._request_commit.emit(path, msg)

    def push(self, path: str):
        self._request_push.emit(path, None)

    def push_specific_tag(self, path: str, tag_name: str):
        self._request_push.emit(path, tag_name)

    def pull(self, path: str):
        self._request_pull.emit(path)

    def force_push(self, path: str):
        self._request_force_push.emit(path)

    def abort_merge(self, path: str):
        self._request_abort_merge.emit(path)

    def clone_repo(self, url: str, path: str, branch: Optional[str] = None):
        self._request_clone.emit(url, path, branch)

    def publish_repo(self, path: str, url: str):
        self._request_publish.emit(path, url)

    def create_tag(self, path: str, tag: str, title: str):
        self._request_create_tag.emit(path, tag, title)

    def delete_tag(self, path: str, tag: str):
        self._request_delete_tag.emit(path, tag)

    def delete_remote_tag(self, path: str, tag: str):
        self._request_delete_remote_tag.emit(path, tag)

    def shutdown(self):
        if self.thread and self.thread.isRunning():
            log.info("Shutting down SourceControlManager thread.")
            self.thread.quit()
            if not self.thread.wait(3000):
                log.warning(
                    "SourceControlManager thread did not shut down "
                    "gracefully. Terminating."
                )
                self.thread.terminate()