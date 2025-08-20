# Koromali/plugins/github_tools/new_release_dialog.py
from typing import Optional, Dict, Any
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout,
                             QDialogButtonBox, QLineEdit, QTextEdit, QLabel,
                             QCheckBox, QComboBox, QHBoxLayout, QWidget,
                             QGroupBox, QPushButton, QMessageBox)
from app_core.source_control_manager import SourceControlManager
from utils.versioning import suggest_next_version

try:
    import git
except ImportError:
    git = None


class NewReleaseDialog(QDialog):
    """
    A dialog for creating a new GitHub release. It collects tag name, title,
    notes, and other release options.
    """

    def __init__(self, project_path: str, git_manager: SourceControlManager,
                 parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.project_path = project_path
        self.git_manager = git_manager

        self.setWindowTitle("Create New Release")
        self.setMinimumWidth(500)

        self._setup_ui()
        self._connect_signals()
        self._populate_branches()
        self._validate_input()

    def _setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        form_layout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        
        # Tag Name with Tooltip
        tag_layout_widget = QWidget()
        tag_layout = QHBoxLayout(tag_layout_widget)
        tag_layout.setContentsMargins(0, 0, 0, 0)
        suggested_tag = suggest_next_version()
        self.tag_edit = QLineEdit(suggested_tag)
        self.tag_edit.setPlaceholderText("e.g., v1.2.1")
        self.tag_edit.setToolTip("The Git tag to create (e.g., v1.0.0). This should be a unique version number.")
        self.branch_combo = QComboBox()
        self.branch_combo.setToolTip("Select the branch to create the release from. This should be your main, stable branch.")
        tag_layout.addWidget(self.tag_edit, 2)
        tag_layout.addWidget(QLabel("on branch:"))
        tag_layout.addWidget(self.branch_combo, 1)
        form_layout.addRow("<b>Tag Name:</b>", tag_layout_widget)

        # Release Title with Tooltip
        self.title_edit = QLineEdit(suggested_tag)
        self.title_edit.setPlaceholderText("e.g., Feature Update and Bug Fixes")
        self.title_edit.setToolTip("The title of the GitHub Release. Can be the same as the tag.")
        form_layout.addRow("<b>Release Title:</b>", self.title_edit)
        self.main_layout.addLayout(form_layout)

        # Release Notes with Tooltip
        notes_header_layout = QHBoxLayout()
        notes_header_layout.addWidget(QLabel("<b>Release Notes:</b>"))
        notes_header_layout.addStretch()
        self.generate_notes_button = QPushButton("Generate from Commits")
        self.generate_notes_button.setToolTip("Generate release notes automatically from commits since the last tag.")
        notes_header_layout.addWidget(self.generate_notes_button)
        self.main_layout.addLayout(notes_header_layout)
        self.notes_edit = QTextEdit()
        self.notes_edit.setPlaceholderText("Describe the changes in this release (Markdown is supported).")
        self.notes_edit.setMinimumHeight(150)
        self.main_layout.addWidget(self.notes_edit)

        # Options with Tooltips
        options_group = QGroupBox("Options")
        options_layout = QVBoxLayout(options_group)
        self.prerelease_checkbox = QCheckBox("Mark as a pre-release")
        self.prerelease_checkbox.setToolTip("Check this for alpha, beta, or release candidate versions. It indicates the release is not production-ready.")
        options_layout.addWidget(self.prerelease_checkbox)
        self.main_layout.addWidget(options_group)
        
        assets_group = QGroupBox("Release Assets")
        assets_layout = QVBoxLayout(assets_group)
        self.build_installer_checkbox = QCheckBox("Build and attach installer")
        self.build_installer_checkbox.setToolTip("If your project has an installer script, this will run it and upload the result.")
        self.build_installer_checkbox.setChecked(True)
        assets_layout.addWidget(self.build_installer_checkbox)
        self.main_layout.addWidget(assets_group)
        
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.main_layout.addWidget(self.button_box)

    def _connect_signals(self):
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.tag_edit.textChanged.connect(self._validate_input)
        self.title_edit.textChanged.connect(self._validate_input)
        self.generate_notes_button.clicked.connect(self._generate_release_notes)

    def _populate_branches(self):
        branches = self.git_manager.get_local_branches(self.project_path)
        self.branch_combo.addItems(branches)
        if 'main' in branches: self.branch_combo.setCurrentText('main')
        elif 'master' in branches: self.branch_combo.setCurrentText('master')

    def _validate_input(self):
        is_valid = bool(self.tag_edit.text().strip() and self.title_edit.text().strip() and self.branch_combo.currentText())
        self.button_box.button(QDialogButtonBox.StandardButton.Ok).setEnabled(is_valid)

    def _generate_release_notes(self):
        if not git:
            QMessageBox.critical(self, "Missing Dependency", "The 'GitPython' library is required for this feature.")
            return
        try:
            repo = git.Repo(self.project_path, search_parent_directories=True)
            tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
            latest_tag = tags[-1] if tags else None
            rev_range = f"{latest_tag.commit.hexsha}..{self.branch_combo.currentText()}" if latest_tag else self.branch_combo.currentText()
            commits = list(repo.iter_commits(rev_range, no_merges=True))
            if not commits:
                QMessageBox.information(self, "No New Commits", f"No new commits found on branch '{self.branch_combo.currentText()}' since the last tag.")
                return
            commit_log = [f"- {c.summary} ({c.hexsha[:7]})" for c in commits]
            self.notes_edit.setText("\n".join(commit_log))
        except Exception as e:
            QMessageBox.critical(self, "Error Generating Notes", f"An error occurred: {e}")

    def get_release_data(self) -> Dict[str, Any]:
        return {
            "tag": self.tag_edit.text().strip(),
            "title": self.title_edit.text().strip(),
            "notes": self.notes_edit.toPlainText().strip(),
            "prerelease": self.prerelease_checkbox.isChecked(),
            "target_branch": self.branch_combo.currentText(),
            "build_installer": self.build_installer_checkbox.isChecked()
        }