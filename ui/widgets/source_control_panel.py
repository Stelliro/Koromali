# Koromali/ui/widgets/source_control_panel.py
import os
from typing import List, Dict, Optional
from git import Repo, InvalidGitRepositoryError, Actor
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTreeWidget,
                             QTreeWidgetItem, QMenu, QMessageBox, QLabel, QHeaderView, QLineEdit, QComboBox,
                             QSizePolicy, QFrame, QInputDialog)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt, pyqtSignal, QPoint
import qtawesome as qta

from app_core.project_manager import ProjectManager
from app_core.source_control_manager import SourceControlManager
from app_core.github_manager import GitHubManager
from app_core.koromali_api import KoromaliPluginAPI


class ProjectSourceControlPanel(QWidget):
    """
    A widget that displays the Git status for all open projects and provides
    controls for common Git operations.
    """
    publish_repo_requested = pyqtSignal(str)
    create_release_requested = pyqtSignal(str)
    link_to_remote_requested = pyqtSignal(str)
    change_visibility_requested = pyqtSignal(str)

    def __init__(self, project_manager: ProjectManager,
                 git_manager: SourceControlManager,
                 github_manager: GitHubManager,
                 koromali_api: KoromaliPluginAPI, parent=None):
        super().__init__(parent)
        self.project_manager = project_manager
        self.git_manager = git_manager
        self.github_manager = github_manager
        self.api = koromali_api
        self.settings_manager = koromali_api.get_manager("settings")
        self.staged_color = QColor("#A7C080")
        self.unstaged_color = QColor("#DBBC7F")
        self.conflicted_color = QColor("#E53935")  # Added color for conflicts
        self._setup_ui()
        self._connect_signals()
        self.update_icons()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        # Main actions toolbar
        main_actions_layout = QHBoxLayout()
        self.refresh_all_button = QPushButton("Refresh")
        self.pull_button = QPushButton("Pull")
        self.push_button = QPushButton("Push")
        self.new_release_button = QPushButton("New Release...")

        main_actions_layout.addWidget(self.refresh_all_button)
        main_actions_layout.addWidget(self.pull_button)
        main_actions_layout.addWidget(self.push_button)
        main_actions_layout.addStretch()
        main_actions_layout.addWidget(self.new_release_button)
        layout.addLayout(main_actions_layout)

        # Advanced/dangerous actions toolbar
        advanced_actions_frame = QFrame()
        advanced_actions_frame.setObjectName("AdvancedActionsFrame")
        advanced_actions_layout = QHBoxLayout(advanced_actions_frame)
        advanced_actions_layout.setContentsMargins(0, 2, 0, 2)
        advanced_actions_layout.addWidget(QLabel("Advanced:"))
        self.force_push_button = QPushButton("Force Push")
        self.force_push_button.setToolTip("DANGER: Overwrites remote history with your local branch.")
        self.abort_merge_button = QPushButton("Abort Merge")
        self.abort_merge_button.setToolTip("Aborts a conflicted merge and resets your branch.")
        self.cleanup_tags_button = QPushButton("Cleanup Tags")
        self.cleanup_tags_button.setToolTip("Delete remote tags that are not part of a release.")

        advanced_actions_layout.addWidget(self.force_push_button)
        advanced_actions_layout.addWidget(self.abort_merge_button)
        advanced_actions_layout.addStretch()
        advanced_actions_layout.addWidget(self.cleanup_tags_button)
        self.abort_merge_button.hide()  # Hide by default
        layout.addWidget(advanced_actions_frame)

        self.project_tree = QTreeWidget()
        self.project_tree.setHeaderLabels(["Project / Changes", ""])
        self.project_tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        header = self.project_tree.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.project_tree)

        self.commit_message_edit = QComboBox()
        self.commit_message_edit.setEditable(True)
        self.commit_message_edit.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.commit_message_edit.setToolTip("Enter a commit message or select a previous one.")
        self.commit_message_edit.lineEdit().setPlaceholderText("Commit message...")
        self.commit_message_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.commit_button = QPushButton("Commit All")
        commit_layout = QHBoxLayout()
        commit_layout.addWidget(self.commit_message_edit)
        commit_layout.addWidget(self.commit_button)
        layout.addLayout(commit_layout)
        self.status_label = QLabel("Ready.")
        layout.addWidget(self.status_label)

        self.action_buttons = [self.refresh_all_button, self.pull_button, self.push_button,
                               self.new_release_button, self.commit_button, self.cleanup_tags_button,
                               self.force_push_button, self.abort_merge_button]

    def _connect_signals(self):
        self.git_manager.status_updated.connect(self._update_project_files)
        self.git_manager.summaries_ready.connect(self._populate_tree)
        self.git_manager.git_error.connect(self._handle_git_error)
        self.git_manager.dubious_ownership_detected.connect(self._handle_dubious_ownership)
        self.git_manager.git_success.connect(self._handle_git_success)
        self.github_manager.operation_success.connect(self._handle_github_success)
        self.github_manager.operation_failed.connect(self._handle_git_error)

        self.refresh_all_button.clicked.connect(self.refresh_all_projects)
        self.push_button.clicked.connect(self._on_push_clicked)
        self.pull_button.clicked.connect(self._on_pull_clicked)
        self.new_release_button.clicked.connect(self._on_new_release_clicked)
        self.commit_button.clicked.connect(self._on_commit_clicked)
        self.force_push_button.clicked.connect(self._on_force_push_clicked)
        self.abort_merge_button.clicked.connect(self._on_abort_merge_clicked)
        self.cleanup_tags_button.clicked.connect(self._on_cleanup_tags_clicked)
        self.project_tree.customContextMenuRequested.connect(self._show_context_menu)

    def set_ui_locked(self, locked: bool, message: str = ""):
        for button in self.action_buttons:
            if button != self.abort_merge_button:
                button.setEnabled(not locked)
        self.commit_message_edit.setEnabled(not locked)
        self.status_label.setText(message)

    def update_theme(self):
        pass # placeholder

    def update_icons(self):
        self.refresh_all_button.setIcon(qta.icon('mdi.refresh'))
        self.pull_button.setIcon(qta.icon('mdi.arrow-down-bold-outline'))
        self.push_button.setIcon(qta.icon('mdi.arrow-up-bold-outline'))
        self.new_release_button.setIcon(qta.icon('mdi.tag-outline'))
        self.cleanup_tags_button.setIcon(qta.icon('mdi.tag-remove-outline'))
        self.commit_button.setIcon(qta.icon('mdi.check'))
        self.force_push_button.setIcon(qta.icon('mdi.upload-off-outline', color='orange'))
        self.abort_merge_button.setIcon(qta.icon('mdi.close-octagon-outline', color='red'))

    def showEvent(self, event):
        super().showEvent(event)
        self._populate_commit_history()

    def _populate_commit_history(self):
        history = self.settings_manager.get("commit_message_history", [])
        self.commit_message_edit.clear()
        self.commit_message_edit.addItems(history)
        self.commit_message_edit.setCurrentText("")

    def _get_selected_project_path(self) -> Optional[str]:
        item = self.project_tree.currentItem()
        if not item:
            return self.project_manager.get_active_project_path()
        while parent := item.parent():
            item = parent
        data = item.data(0, Qt.ItemDataRole.UserRole)
        return data.get('path') if data else None

    def _on_push_clicked(self):
        if path := self._get_selected_project_path():
            self.set_ui_locked(True, f"Pushing {os.path.basename(path)}...")
            self.git_manager.push(path)

    def _on_force_push_clicked(self):
        if not (path := self._get_selected_project_path()):
            return

        reply = QMessageBox.warning(
            self,
            "Confirm Force Push",
            "<b>DANGER:</b> Force pushing overwrites the remote history with your local "
            "branch. This can discard commits for other team members.\n\n"
            "Only do this if you are absolutely sure. Are you sure you want to force push?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.set_ui_locked(True, f"Force pushing {os.path.basename(path)}...")
            self.git_manager.force_push(path)

    def _on_abort_merge_clicked(self):
        if not (path := self._get_selected_project_path()):
            return
        self.set_ui_locked(True, f"Aborting merge in {os.path.basename(path)}...")
        self.git_manager.abort_merge(path)

    def _on_pull_clicked(self):
        if path := self._get_selected_project_path():
            self.set_ui_locked(True, f"Pulling {os.path.basename(path)}...")
            self.git_manager.pull(path)

    def _on_new_release_clicked(self):
        if path := self._get_selected_project_path():
            self.create_release_requested.emit(path)

    def _on_commit_clicked(self):
        path = self._get_selected_project_path()
        message = self.commit_message_edit.currentText().strip()

        if message.lower().startswith("git commit"):
            QMessageBox.warning(self, "Invalid Message",
                                "Please enter only the commit message, not the full 'git commit' command.")
            return

        if not path or not message:
            QMessageBox.warning(self, "Commit Failed",
                                "A project must be selected and a commit message must be provided.")
            return

        # FIX: The manager now handles the author, so we don't need to create the Actor here.
        self.set_ui_locked(True, f"Committing changes in {os.path.basename(path)}...")
        self.git_manager.commit_files(path, message)

    def _on_cleanup_tags_clicked(self):
        path = self._get_selected_project_path()
        if not path:
            QMessageBox.warning(self, "No Project Selected", "Please select a Git project.")
            return

        try:
            repo = Repo(path)
            if not repo.remotes:
                QMessageBox.warning(self, "No Remote", "The selected project does not have a remote configured.")
                return
            remote_url = repo.remotes.origin.url
            owner, repo_name = self.git_manager.parse_git_url(remote_url)
            if not owner or not repo_name:
                QMessageBox.critical(self, "Error", "Could not parse owner/repo from the remote URL.")
                return
        except Exception as e:
            QMessageBox.critical(self, "Git Error", f"Could not analyze repository: {e}")
            return

        reply = QMessageBox.question(
            self,
            "Confirm Tag Cleanup",
            "This will permanently delete all tags from the remote repository "
            f"<b>{owner}/{repo_name}</b> that are NOT associated with a GitHub Release.\n\n"
            "This action cannot be undone. Are you sure you want to continue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.set_ui_locked(True, f"Cleaning up tags for {owner}/{repo_name}...")
            self.github_manager.cleanup_orphaned_tags(owner, repo_name)

    def _on_fix_branch_mismatch_clicked(self, path: str):
        reply = QMessageBox.warning(
            self, "Confirm Branch Fix", "This will perform a force-push and delete "
                                        "the 'master' branch from the remote. Are you sure?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.set_ui_locked(True, f"Fixing branch mismatch for {os.path.basename(path)}...")
            self.git_manager.fix_branch_mismatch(path)

    def _handle_git_success(self, message: str, data: dict):
        if "committed" in message.lower() and not data.get('no_changes'):
            commit_message = self.commit_message_edit.currentText().strip()
            history = self.settings_manager.get("commit_message_history", [])
            if commit_message in history:
                history.remove(commit_message)
            history.insert(0, commit_message)
            max_history = self.settings_manager.get("max_commit_history", 50)
            self.settings_manager.set("commit_message_history", history[:max_history])
            self._populate_commit_history()

        self.set_ui_locked(False, f"Success: {message}")
        self.refresh_all_projects()

    def _handle_github_success(self, message: str, data: dict):
        if data.get("operation") == "update" and (repo_data := data.get("repo_data")):
            self.set_ui_locked(True, "Updating local remote URL...")
            repo_path = self._get_selected_project_path()
            if repo_path:
                self.git_manager.set_remote_url(repo_path, repo_data['clone_url'])
        else:
            self.set_ui_locked(False, f"Success: {message}")
            self.refresh_all_projects()

    def _handle_dubious_ownership(self, repo_path: str):
        """Shows a user-friendly dialog for the 'dubious ownership' error."""
        self.set_ui_locked(False, "Git ownership issue detected.")
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Git Security Warning")
        msg_box.setText(
            f"Git has detected a potential security issue with the repository at:\n<b>{repo_path}</b>"
        )
        msg_box.setInformativeText(
            "This can happen if the repository was cloned by a different user or with different permissions. "
            "To resolve this, you can mark this directory as safe in your global Git configuration.\n\n"
            "Would you like to do this automatically?"
        )
        fix_button = msg_box.addButton("Fix Automatically", QMessageBox.ButtonRole.AcceptRole)
        cancel_button = msg_box.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
        msg_box.exec()

        if msg_box.clickedButton() == fix_button:
            self.set_ui_locked(True, f"Marking '{os.path.basename(repo_path)}' as safe...")
            self.git_manager.add_safe_directory(repo_path)

    def _handle_git_error(self, error_message: str):
        self.set_ui_locked(False, "Operation Failed.")
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Operation Failed")
        msg_box.setText("A Git operation failed to complete.")
        msg_box.setInformativeText(f"<b>Reason:</b><br><pre>{error_message}</pre>")
        msg_box.exec()
        self.refresh_all_projects()

    def refresh_all_projects(self):
        self.set_ui_locked(True, "Fetching project statuses...")
        all_projects = self.project_manager.get_open_projects()
        if all_projects:
            self.git_manager.get_summaries(all_projects)
        else:
            self.project_tree.clear()
            self.set_ui_locked(False, "No projects open.")

    def _populate_tree(self, summaries: Dict[str, Dict]):
        self.project_tree.clear()
        git_project_paths = summaries.keys()
        for path in self.project_manager.get_open_projects():
            project_name = os.path.basename(path)
            if path in git_project_paths:
                summary = summaries[path]
                item = QTreeWidgetItem(self.project_tree, [project_name, f"Branch: {summary.get('branch', 'N/A')}"])
                item.setData(0, Qt.ItemDataRole.UserRole, {'type': 'project', 'path': path})
                item.setIcon(0, qta.icon('mdi.git'))
                self.git_manager.get_status(path)
            else:
                item = QTreeWidgetItem(self.project_tree, [project_name])
                item.setData(0, Qt.ItemDataRole.UserRole, {'type': 'non-git-project', 'path': path})
                item.setIcon(0, qta.icon('mdi.folder-outline', color='gray'))
                actions_widget = QWidget()
                actions_layout = QHBoxLayout(actions_widget)
                actions_layout.setContentsMargins(0, 0, 0, 0)
                link_button = QPushButton("Link...")
                link_button.setToolTip("Link this local folder to an existing GitHub repository")
                link_button.clicked.connect(lambda _, p=path: self.link_to_remote_requested.emit(p))
                publish_button = QPushButton("Publish...")
                publish_button.setToolTip("Create a new repository on GitHub from this project")
                publish_button.clicked.connect(lambda _, p=path: self.publish_repo_requested.emit(p))
                actions_layout.addStretch()
                actions_layout.addWidget(link_button)
                actions_layout.addWidget(publish_button)
                self.project_tree.setItemWidget(item, 1, actions_widget)
        self.set_ui_locked(False, "Ready.")
        if self.project_tree.topLevelItemCount() > 0:
            self.project_tree.setCurrentItem(self.project_tree.topLevelItem(0))

    def _update_project_files(self, staged: List[str], unstaged: List[str], conflicted: List[str], repo_path: str):
        root = self.project_tree.invisibleRootItem()
        for i in range(root.childCount()):
            project_item = root.child(i)
            item_data = project_item.data(0, Qt.ItemDataRole.UserRole)
            if item_data and item_data.get('path') == repo_path:
                project_item.takeChildren()

                repo = Repo(repo_path)
                is_merging = os.path.exists(os.path.join(repo.git_dir, 'MERGE_HEAD'))
                self.abort_merge_button.setVisible(is_merging)

                if conflicted:
                    conflicts_header = QTreeWidgetItem(project_item, ["Conflicts (Resolve Manually)"])
                    conflicts_header.setForeground(0, self.conflicted_color)
                    for f in sorted(conflicted):
                        child = QTreeWidgetItem(conflicts_header, [f])
                        child.setForeground(0, self.conflicted_color)

                if staged:
                    staged_header = QTreeWidgetItem(project_item, ["Staged Changes"])
                    staged_header.setForeground(0, self.staged_color)
                    for f in sorted(staged):
                        child = QTreeWidgetItem(staged_header, [f])
                        child.setForeground(0, self.staged_color)

                if unstaged:
                    unstaged_header = QTreeWidgetItem(project_item, ["Changes"])
                    unstaged_header.setForeground(0, self.unstaged_color)
                    for f in sorted(unstaged):
                        child = QTreeWidgetItem(unstaged_header, [f])
                        child.setForeground(0, self.unstaged_color)

                project_item.setExpanded(True)
                break

    def _show_context_menu(self, position: QPoint):
        item = self.project_tree.itemAt(position)
        if not item:
            return
        data = item.data(0, Qt.ItemDataRole.UserRole)
        if not (data and (path := data.get('path'))):
            return

        menu = QMenu()
        if data['type'] == 'project':
            menu.addAction(qta.icon('mdi.pencil-outline'), "Rename Repository...",
                           lambda: self._action_rename_repo(path))
            menu.addSeparator()
            menu.addAction(qta.icon('mdi.refresh'), "Refresh Status",
                           lambda: self.git_manager.get_status(path))
            vis_action = menu.addAction(qta.icon('mdi.eye-outline'), "Change GitHub Visibility...")
            vis_action.triggered.connect(lambda: self.change_visibility_requested.emit(path))

            repo = Repo(path)
            is_merging = os.path.exists(os.path.join(repo.git_dir, 'MERGE_HEAD'))
            if is_merging:
                menu.addSeparator()
                abort_action = menu.addAction(qta.icon('mdi.close-octagon-outline', color='red'), "Abort Merge")
                abort_action.triggered.connect(lambda: self._on_abort_merge_clicked())

            try:
                branches = [b.name for b in repo.branches]
                if 'main' in branches and 'master' in branches:
                    menu.addSeparator()
                    fix_action = menu.addAction(qta.icon('mdi.alert-outline',
                                                         color='orange'), "Fix Branch Mismatch...")
                    fix_action.triggered.connect(lambda: self._on_fix_branch_mismatch_clicked(path))
            except (InvalidGitRepositoryError, TypeError):
                pass
        elif data['type'] == 'non-git-project':
            menu.addAction(qta.icon('mdi.link-variant'), "Link to GitHub Repo...",
                           lambda: self.link_to_remote_requested.emit(path))
            menu.addAction(qta.icon('mdi.cloud-upload-outline'), "Publish to GitHub...",
                           lambda: self.publish_repo_requested.emit(path))

        if menu.actions():
            menu.exec(self.project_tree.viewport().mapToGlobal(position))

    def _action_rename_repo(self, path: str):
        """Handles the repository renaming workflow."""
        try:
            repo = Repo(path)
            if not repo.remotes.origin:
                QMessageBox.warning(self, "No Remote", "This project does not have an 'origin' remote configured.")
                return

            remote_url = repo.remotes.origin.url
            owner, old_repo_name = self.git_manager.parse_git_url(remote_url)

            if not owner or not old_repo_name:
                QMessageBox.critical(self, "Error", "Could not parse the owner and repository name from the remote URL.")
                return

            new_repo_name, ok = QInputDialog.getText(self, "Rename Repository", "Enter the new repository name:", text=old_repo_name)

            if ok and new_repo_name and new_repo_name != old_repo_name:
                self.set_ui_locked(True, f"Renaming '{old_repo_name}' to '{new_repo_name}'...")
                self.github_manager.update_repo(owner, old_repo_name, {'name': new_repo_name})
            elif ok:
                 self.set_ui_locked(False, "") # Clear status if user entered same name

        except (InvalidGitRepositoryError, GitCommandError) as e:
            QMessageBox.critical(self, "Git Error", f"Could not access repository details: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Unexpected Error", str(e))