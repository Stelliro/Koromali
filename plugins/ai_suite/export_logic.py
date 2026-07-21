# /plugins/ai_suite/export_logic.py
import os
from typing import List, Set
from datetime import datetime

from app_core import golden_rules
from utils.logger import log

# Directories to always exclude from exports.
EXCLUDE_DIRS: Set[str] = {
    '.git', '__pycache__', 'venv', '.venv', 'ai_exports', 'node_modules', 'dist', 'build', 'backups'
}

# File extensions to exclude because they are binary, compressed, or otherwise not useful as text.
NON_EXPORTABLE_EXTENSIONS: Set[str] = {
    # Images
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.tif', '.tiff', '.svg', '.webp',
    # Audio & Video
    '.mp3', '.wav', '.flac', '.ogg', '.mp4', '.mov', '.avi', '.mkv',
    # Compressed
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
    # Executables and binaries
    '.exe', '.dll', '.so', '.o', '.a', '.lib', '.dylib', '.app', '.msi', '.bin',
    # Documents
    '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx',
}


def is_exportable(file_path: str, include_logs: bool) -> bool:
    """Checks if a file should be included in the export based on its extension and name."""
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension in NON_EXPORTABLE_EXTENSIONS:
        return False

    if not include_logs and extension == '.log':
        return False

    return True


def create_export_content(
    file_paths: List[str],
    project_root: str,
    include_logs: bool,
    *,
    include_instructions: bool = True,
) -> str:
    """Generate a single markdown string containing the content of all specified files."""
    markdown_parts: List[str] = []
    project_name = os.path.basename(project_root) or "project"
    timestamp = datetime.now().isoformat()

    markdown_parts.append(f"# AI Export for Project: `{project_name}`")
    markdown_parts.append(f"Timestamp: {timestamp}")
    markdown_parts.append("")
    if include_instructions:
        markdown_parts.append(golden_rules.get_rules_markdown())
        markdown_parts.append("")
    markdown_parts.append("---")
    markdown_parts.append("")

    for abs_path in sorted(file_paths):
        if not is_exportable(abs_path, include_logs):
            log.info(f"Skipping non-exportable file: {os.path.basename(abs_path)}")
            continue

        try:
            with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            relative_path = os.path.relpath(abs_path, project_root).replace(os.sep, '/')
            lang = os.path.splitext(relative_path)[1].lstrip('.') or 'text'
            fence = "~~~" if "```" in content else "```"

            markdown_parts.append(f"### File: `/{relative_path}`")
            markdown_parts.append(f"{fence}{lang}")
            markdown_parts.append(content.rstrip("\n"))
            markdown_parts.append(fence)
            markdown_parts.append("")
        except Exception as e:
            log.error(f"Could not read file {abs_path} for export: {e}")

    return "\n".join(markdown_parts)