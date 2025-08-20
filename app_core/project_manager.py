# Koromali/app_core/project_manager.py
import os
import datetime
import zipfile
from pathlib import Path
from typing import List, Tuple, Optional, Dict

from PyQt6.QtCore import QObject, pyqtSignal

from .settings_manager import SettingsManager
from utils.logger import log
from utils.helpers import clean_git_conflict_markers


class ProjectManager(QObject):
    """Manages the state of open projects and project-wide operations."""

    projects_changed = pyqtSignal()

    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.settings = settings_manager
        self._open_projects: List[str] = []
        self._active_project_path: Optional[str] = None
        self._load_session()
        log.info(f"ProjectManager initialized.")

    def _load_session(self):
        """Loads the list of open projects from the settings."""
        open_projects = self.settings.get("open_projects", [])
        active_project = self.settings.get("active_project_path")
        self._open_projects = [os.path.normpath(p) for p in open_projects if os.path.isdir(p)]
        if (active_project and os.path.normpath(active_project) in self._open_projects):
            self._active_project_path = os.path.normpath(active_project)
        elif self._open_projects:
            self._active_project_path = self._open_projects[0]
        else:
            self._active_project_path = None
        log.info(f"Loaded project session. Active project: {self._active_project_path}")

    def save_session(self):
        """Saves the current list of open projects to the settings."""
        self.settings.set("open_projects", self._open_projects, False)
        self.settings.set("active_project_path", self._active_project_path, False)
        log.info("Project session saved.")

    def open_project(self, path: str) -> bool:
        if not os.path.isdir(path): return False
        norm_path = os.path.normpath(path)
        if norm_path not in self._open_projects:
            self._open_projects.append(norm_path)
            self.projects_changed.emit()
        self.set_active_project(norm_path)
        return True

    def close_project(self, path: str):
        norm_path = os.path.normpath(path)
        if norm_path in self._open_projects:
            was_active = (self.get_active_project_path() == norm_path)
            self._open_projects.remove(norm_path)
            if was_active:
                new_active = self._open_projects[0] if self._open_projects else None
                if self._active_project_path != new_active:
                    self._active_project_path = new_active
            self.save_session()
            self.projects_changed.emit()

    def reorder_projects(self, new_order: List[str]):
        if set(self._open_projects) != set(new_order): return
        self._open_projects = new_order
        self.save_session()
    
    def get_open_projects(self) -> List[str]:
        return self._open_projects

    def set_active_project(self, path: Optional[str]):
        norm_path = os.path.normpath(path) if path else None
        if norm_path and norm_path not in self._open_projects: return
        if self._active_project_path != norm_path:
            self._active_project_path = norm_path
            self.projects_changed.emit()

    def get_active_project_path(self) -> Optional[str]:
        return self._active_project_path

    def is_project_open(self) -> bool:
        return self._active_project_path is not None

    def create_project_zip(self, output_zip_path: str) -> bool:
        if not self.is_project_open(): return False
        project_root = self.get_active_project_path()
        ignore_dirs = {'__pycache__', '.git', 'venv', '.venv', 'dist', 'build', 'logs'}
        ignore_files = {'OverlayApp', 'Koromali_editor_settings.json'}
        try:
            with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
                for root, dirs, files in os.walk(project_root):
                    dirs[:] = [d for d in dirs if d not in ignore_dirs]
                    for file in files:
                        if file in ignore_files: continue
                        z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_root))
            return True
        except (IOError, OSError, zipfile.BadZipFile):
            return False
    def generate_file_tree_from_list(
            self, project_root: str, file_list: List[str]
    ) -> List[str]:
        """Generates a text-based file tree from a specific list of files."""
        tree = {}
        for file_path in file_list:
            relative_path = os.path.relpath(file_path, project_root)
            parts = Path(relative_path).parts
            current_level = tree
            for part in parts:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

        def build_tree_lines(d: dict, prefix: str = "") -> List[str]:
            lines = []
            entries = sorted(
                d.keys(), key=lambda k: (not bool(d[k]), k.lower())
            )
            for i, name in enumerate(entries):
                is_last = (i == len(entries) - 1)
                connector = "└── " if is_last else "├── "
                lines.append(f"{prefix}{connector}{name}")
                if d[name]:
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    lines.extend(build_tree_lines(d[name], new_prefix))
            return lines

        return build_tree_lines(tree)

    def export_project_for_ai(
            self,
            output_filepath: str,
            selected_files: List[str],
            instructions: str,
            guidelines: List[str],
            golden_rules: List[str],
            all_problems: Optional[Dict[str, List[Dict]]] = None
    ) -> Tuple[bool, str]:
        """
        Exports selected project files into a single Markdown file for AI.
        """
        if not self.is_project_open():
            return False, "No project is open."

        project_root = self.get_active_project_path()
        project_name = os.path.basename(project_root)
        output_lines = [
            f"# Project Export: {project_name}",
            f"## Export Timestamp: {datetime.datetime.now().isoformat()}",
            "---",
            "\n## 📝 AI Instructions", "```text",
            instructions or "No specific instructions were provided.", "```",
            "\n## 📜 AI Guidelines & Rules", "```text",
        ]
        guideline_text = "\n".join(
            [f"- {g}" for g in guidelines]
        ) if guidelines else "No specific guidelines were provided."
        output_lines.append(guideline_text)
        output_lines.extend(["```", "---"])

        output_lines.append("\n## ✨ Golden Rules\n```text")
        golden_rules_text = "\n".join(
            [f"{i + 1}. {g}" for i, g in enumerate(golden_rules)]
        ) if golden_rules else "No specific golden rules were provided."
        output_lines.append(golden_rules_text)
        output_lines.extend(["```", "---"])

        output_lines.append("\n## 🗂️ File Tree of Included Files:\n```")
        output_lines.append(f"/{project_name}")
        tree_text_lines = self.generate_file_tree_from_list(project_root, selected_files)
        output_lines.extend(tree_text_lines)
        output_lines.append("```\n---")
        output_lines.append("\n## 📄 File Contents:\n")

        file_count = 0
        for filepath in sorted(selected_files):
            norm_filepath = os.path.normpath(filepath)
            relative_path = Path(
                filepath).relative_to(project_root).as_posix()
            language = Path(filepath).suffix.lstrip('.') or 'text'
            if language == 'py':
                language = 'python'

            output_lines.append(f"### File: `/{relative_path}`\n")

            if all_problems and norm_filepath in all_problems:
                output_lines.append("#### Linter Issues Found:")
                output_lines.append("```")
                for problem in all_problems[norm_filepath]:
                    output_lines.append(
                        f"- Line {problem['line']}, Col {problem['col']} "
                        f"({problem['code']}): {problem['description']}"
                    )
                output_lines.append("```\n")

            output_lines.append(f"```{language}")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                    cleaned_content = clean_git_conflict_markers(original_content)
                    if original_content != cleaned_content:
                        log.info(f"Cleaned git conflict markers from {filepath} for export.")
                    output_lines.append(cleaned_content)
                file_count += 1
            except (IOError, UnicodeDecodeError) as e:
                log.warning(
                    "Could not read file during AI export: "
                    f"{filepath}. Error: {e}"
                )
                output_lines.append(f"[Error reading file: {e}]")
            output_lines.append("```\n---")

        try:
            with open(output_filepath, 'w', encoding='utf-8') as f:
                f.write("\n".join(output_lines))
            return True, (
                f"Project exported to {Path(output_filepath).name}. "
                f"Included {file_count} files."
            )
        except IOError as e:
            log.error(f"Failed to write AI export file: {e}", exc_info=True)
            return False, f"Failed to write export file: {e}"