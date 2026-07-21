# /plugins/ai_export_viewer/restore_logic.py
import os
import re
import shutil
from datetime import datetime
from typing import Dict, List, Tuple
from PyQt6.QtWidgets import QMessageBox
from utils.logger import log
from utils.helpers import get_base_path


def parse_export_file(export_path: str) -> Dict[str, str]:
    """Parses an AI export file and returns a dict of relative_path: content."""
    parsed_files = {}
    try:
        with open(export_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find file blocks, robustly handling optional language specifiers
        # Looks for ### File: `/path/to/file.ext`
        pattern = re.compile(
            r"### File:\s*`(/.*?)`\s*\n```(?:\w*\n)?(.*?)\n```", re.DOTALL
        )

        matches = pattern.finditer(content)
        for match in matches:
            # path is like /folder/file.py, so we remove the leading slash
            rel_path = match.group(1).strip().lstrip('/')
            file_content = match.group(2).strip()
            # Normalize path separators for cross-platform consistency
            parsed_files[os.path.normpath(rel_path)] = file_content
    except Exception as e:
        log.error(f"Failed to parse export file {export_path}: {e}", exc_info=True)

    return parsed_files


def perform_restore(export_path: str, target_paths: List[str], project_root: str, parent_widget) -> Tuple[bool, str]:
    """Restores files/folders from an AI export, with a backup option."""
    parsed_export = parse_export_file(export_path)
    if not parsed_export:
        return False, "Failed to parse the selected export file. It may be empty or malformed."

    files_to_restore = set()
    for path in target_paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    files_to_restore.add(os.path.normpath(os.path.join(root, file)))
        elif os.path.isfile(path):
            files_to_restore.add(os.path.normpath(path))

    # Filter for files that actually exist in the export
    final_restore_map = {}  # {destination_path: content_from_export}
    for file_path in files_to_restore:
        rel_path = os.path.normpath(os.path.relpath(file_path, project_root))
        if rel_path in parsed_export:
            final_restore_map[file_path] = parsed_export[rel_path]

    if not final_restore_map:
        return False, "None of the selected files were found in the chosen export."

    # Ask for backup
    reply = QMessageBox.question(
        parent_widget,
        "Backup Before Restoring?",
        f"You are about to restore {len(final_restore_map)} file(s) from '{os.path.basename(export_path)}'.\n\n"
        "Would you like to back up the current versions of these files before overwriting them?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
        QMessageBox.StandardButton.Yes
    )
    if reply == QMessageBox.StandardButton.Cancel:
        return False, "Restore operation cancelled."

    # Perform backup if requested
    if reply == QMessageBox.StandardButton.Yes:
        backup_dir = os.path.join(
            get_base_path(), "ai_exports", "backups",
            datetime.now().strftime('%Y-%m-%d_%H%M%S')
        )
        try:
            os.makedirs(backup_dir, exist_ok=True)
            for file_path in final_restore_map.keys():
                if os.path.exists(file_path):
                    rel_path = os.path.relpath(file_path, project_root)
                    backup_file_path = os.path.join(backup_dir, rel_path)
                    os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
                    shutil.copy2(file_path, backup_file_path)
            log.info(f"Backed up {len(final_restore_map)} files to {backup_dir}")
        except Exception as e:
            log.error(f"Failed to create backup: {e}", exc_info=True)
            return False, f"Failed to create backup: {e}"

    # Perform restore
    restored_count = 0
    errors = []
    for dest_path, content in final_restore_map.items():
        try:
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(content)
            restored_count += 1
        except Exception as e:
            errors.append(f"Could not write to '{os.path.basename(dest_path)}': {e}")

    message = f"Successfully restored {restored_count} file(s)."
    if errors:
        message += "\n\nErrors:\n" + "\n".join(errors)
        return False, message
    
    return True, message