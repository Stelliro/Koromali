# Koromali/utils/helpers.py
import sys
import os
import re
import difflib
import hashlib
from typing import List, Optional
from PyQt6.QtGui import QFontDatabase
from .logger import log, get_app_data_path

# Define constants at the module level for easy import
LARGE_FILE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB
LARGE_TOKEN_COUNT = 1_000_000
SELECTION_TOKEN_THRESHOLD = 2_000_000


def get_base_path():
    """Return the application's base path for resource loading."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def human_readable_size(size_bytes: int | float | None) -> str:
    """Format a byte count as a short human-readable string."""
    if not size_bytes:
        return "0 B"
    try:
        value = float(size_bytes)
    except (TypeError, ValueError):
        return "0 B"
    units = ("B", "KB", "MB", "GB", "TB", "PB")
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024.0
        idx += 1
    if idx == 0:
        return f"{int(value)} B"
    return f"{value:.2f} {units[idx]}"


def get_projects_path() -> str:
    """Return the path to the internal projects directory, ensuring it exists."""
    projects_dir = os.path.join(get_app_data_path(), "projects")
    os.makedirs(projects_dir, exist_ok=True)
    return projects_dir


def get_session_path() -> str:
    """Return the path to the session data directory, creating it if needed."""
    session_dir = os.path.join(get_app_data_path(), "session_data", "drafts")
    os.makedirs(session_dir, exist_ok=True)
    return session_dir


def get_draft_path(original_filepath: str) -> str:
    """Generate a consistent, safe filename for a draft file."""
    path_hash = hashlib.sha256(original_filepath.encode('utf-8')).hexdigest()
    return os.path.join(get_session_path(), f"{path_hash}.draft")


def clean_git_conflict_markers(content: str) -> str:
    """Remove Git conflict markers from *content*, keeping the ``HEAD`` block."""
    if '<<<<<<<' not in content:
        return content

    lines = content.splitlines()
    cleaned_lines = []
    in_conflict = False
    keep_current_version = True

    for line in lines:
        if line.startswith('<<<<<<<'):
            in_conflict = True
            keep_current_version = True
            continue

        if line.startswith('======='):
            if in_conflict:
                keep_current_version = False
                continue

        if line.startswith('>>>>>>>'):
            if in_conflict:
                in_conflict = False
                keep_current_version = False
                continue

        if not in_conflict or (in_conflict and keep_current_version):
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def generate_unified_diff(original_content: str, new_content: str, fromfile='original', tofile='new') -> str:
    """Generate a git-style unified diff string."""
    original_lines = original_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)
    diff = difflib.unified_diff(original_lines, new_lines, fromfile=fromfile, tofile=tofile)
    return "".join(diff)


def apply_patch(original_content: str, patch_content: str) -> str:
    """Apply a unified diff patch to *original_content* and return the result.

    Pure-Python implementation — no system ``patch`` binary required (Windows-safe).
    """
    # Normalize line endings of both original and patch to LF for processing
    original_lines = original_content.replace('\r\n', '\n').replace('\r', '\n').splitlines()
    patch_lines = patch_content.replace('\r\n', '\n').replace('\r', '\n').splitlines()

    # Detect original ending to restore it later
    original_ending = '\r\n' if '\r\n' in original_content else '\n'

    if not any(line.startswith('@@') for line in patch_lines):
        raise ValueError("Patch contains no unified-diff hunks (missing @@ lines).")

    output_lines: List[str] = []
    original_line_idx = 0
    patch_idx = 0
    hunk_pattern = re.compile(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@')

    def _lines_match(expected: str, actual: str) -> bool:
        if expected == actual:
            return True
        # Tolerate trailing whitespace drift from copy/paste through browsers.
        return expected.rstrip() == actual.rstrip()

    # Skip header lines of the patch (---, +++, diff --git, index, …)
    while patch_idx < len(patch_lines) and not hunk_pattern.match(patch_lines[patch_idx]):
        patch_idx += 1

    if patch_idx >= len(patch_lines):
        raise ValueError("Patch contains no unified-diff hunks (missing @@ lines).")

    while patch_idx < len(patch_lines):
        line = patch_lines[patch_idx]
        match = hunk_pattern.match(line)
        if not match:
            # Outside a hunk (secondary headers, trailing noise) — skip.
            patch_idx += 1
            continue

        old_start = int(match.group(1))
        # Unified diffs use 0 for empty files; otherwise 1-based line numbers.
        old_start_idx = 0 if old_start == 0 else max(0, old_start - 1)

        # Add lines from original file before the hunk
        if old_start_idx < original_line_idx:
            raise ValueError(
                f"Patch hunks out of order or overlapping at original line {old_start}."
            )
        output_lines.extend(original_lines[original_line_idx:old_start_idx])
        original_line_idx = old_start_idx

        patch_idx += 1

        # Process lines within the hunk
        while patch_idx < len(patch_lines) and not patch_lines[patch_idx].startswith('@@'):
            hunk_line = patch_lines[patch_idx]
            # Completely empty lines between hunks can appear; ignore them.
            if hunk_line == '':
                patch_idx += 1
                continue

            # Some models omit the leading space on context lines. Treat a bare
            # non-diff line as context when it matches the next original line.
            if hunk_line[0] not in {'+', '-', ' ', '\\'} and original_line_idx < len(original_lines):
                if _lines_match(hunk_line, original_lines[original_line_idx]):
                    op, data = ' ', hunk_line
                else:
                    raise ValueError(
                        f"Invalid patch format: unexpected line in hunk: {hunk_line!r}"
                    )
            else:
                op, data = hunk_line[0], hunk_line[1:]

            if op == '+':
                output_lines.append(data)
            elif op == '-':
                if original_line_idx >= len(original_lines) or not _lines_match(
                    data, original_lines[original_line_idx]
                ):
                    got = (
                        original_lines[original_line_idx]
                        if original_line_idx < len(original_lines)
                        else '<EOF>'
                    )
                    raise ValueError(
                        f"Patch context mismatch at original line {original_line_idx + 1}. "
                        f"Expected {data!r}, found {got!r}."
                    )
                original_line_idx += 1
            elif op == ' ':
                if original_line_idx >= len(original_lines) or not _lines_match(
                    data, original_lines[original_line_idx]
                ):
                    got = (
                        original_lines[original_line_idx]
                        if original_line_idx < len(original_lines)
                        else '<EOF>'
                    )
                    raise ValueError(
                        f"Patch context mismatch at original line {original_line_idx + 1}. "
                        f"Expected {data!r}, found {got!r}."
                    )
                output_lines.append(original_lines[original_line_idx])
                original_line_idx += 1
            elif op == '\\':
                # "\ No newline at end of file" — informational only.
                pass
            else:
                raise ValueError(f"Invalid patch format: unexpected line prefix '{op}' in hunk.")

            patch_idx += 1

    # Add any remaining lines from the original file
    output_lines.extend(original_lines[original_line_idx:])

    # Re-join using the original detected line ending
    result = original_ending.join(output_lines)
    if original_content.endswith(('\n', '\r\n')) and result and not result.endswith(('\n', '\r\n')):
        result += original_ending
    return result


def get_best_available_font(preferred_list: List[str]) -> Optional[str]:
    """Scan *preferred_list* and return the first installed font family."""
    if not isinstance(preferred_list, list):
        log.warning(f"Font list provided is not a list: {preferred_list}. No font selected.")
        return None

    font_db = QFontDatabase()
    installed_fonts = {font.lower() for font in font_db.families()}

    for font_name in preferred_list:
        if font_name.lower() in installed_fonts:
            log.info(f"Font suggestion: Found '{font_name}' installed on system.")
            return font_name

    log.warning(f"Could not find any preferred fonts: {preferred_list}. Using system default.")
    return None

def is_binary_file(filepath: str) -> bool:
    """Return ``True`` when *filepath* looks like a binary file."""
    text_extensions = {'.txt', '.py', '.md', '.json', '.html', '.css', '.js', '.xml', '.yml', '.yaml', '.toml', '.ini', '.cfg', '.h', '.hpp', '.c', '.cpp', '.cs', '.java', '.rs', '.go', '.qss', '.sh', '.bat', '.spec'}
    binary_extensions = {'.exe', '.dll', '.so', '.o', '.a', '.lib', '.dylib', '.app', '.msi', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg', '.zip', '.rar', '.7z', '.gz', '.tar', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.mp3', '.wav', '.mp4', '.mkv', '.avi', '.mov', '.eot', '.woff', '.woff2', '.ttf', '.otf', '.db', '.sqlite3', '.dat'}

    _name, ext = os.path.splitext(filepath)
    ext = ext.lower()
    
    if ext in text_extensions:
        return False
    if ext in binary_extensions:
        return True

    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            return b'\0' in chunk
    except (IOError, OSError):
        return True