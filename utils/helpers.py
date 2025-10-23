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
    """
    Returns the application's base path for resource loading.
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_projects_path() -> str:
    """Returns the path to the internal projects directory, ensuring it exists."""
    projects_dir = os.path.join(get_app_data_path(), "projects")
    os.makedirs(projects_dir, exist_ok=True)
    return projects_dir


def get_session_path() -> str:
    """Returns the path to the session data directory, creating it if needed."""
    session_dir = os.path.join(get_app_data_path(), "session_data", "drafts")
    os.makedirs(session_dir, exist_ok=True)
    return session_dir


def get_draft_path(original_filepath: str) -> str:
    """Generates a consistent, safe filename for a draft file."""
    path_hash = hashlib.sha256(original_filepath.encode('utf-8')).hexdigest()
    return os.path.join(get_session_path(), f"{path_hash}.draft")


def clean_git_conflict_markers(content: str) -> str:
    """
    Removes Git conflict markers from a string, keeping the 'HEAD' version.
    """
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
    """Generates a git-style unified diff string."""
    original_lines = original_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)
    diff = difflib.unified_diff(original_lines, new_lines, fromfile=fromfile, tofile=tofile)
    return "".join(diff)


def apply_patch(original_content: str, patch_content: str) -> str:
    """
    Applies a unified diff patch to a string content, resilient to
    line ending differences.
    Raises ValueError if the patch cannot be applied cleanly.
    """
    # Normalize line endings of both original and patch to LF for processing
    original_lines = original_content.replace('\r\n', '\n').splitlines()
    patch_lines = patch_content.replace('\r\n', '\n').splitlines()
    
    # Detect original ending to restore it later
    original_ending = '\r\n' if '\r\n' in original_content else '\n'

    output_lines = []
    original_line_idx = 0
    patch_idx = 0
    hunk_pattern = re.compile(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@.*$')

    # Skip header lines of the patch (---, +++)
    while patch_idx < len(patch_lines) and not hunk_pattern.match(patch_lines[patch_idx]):
        patch_idx += 1

    while patch_idx < len(patch_lines):
        line = patch_lines[patch_idx]
        match = hunk_pattern.match(line)
        if not match:
            # We are outside a hunk, just continue
            patch_idx += 1
            continue

        old_start = int(match.group(1))
        old_start_idx = max(0, old_start - 1)
        
        # Add lines from original file before the hunk
        output_lines.extend(original_lines[original_line_idx:old_start_idx])
        original_line_idx = old_start_idx
        
        patch_idx += 1
        
        # Process lines within the hunk
        while patch_idx < len(patch_lines) and not patch_lines[patch_idx].startswith('@@'):
            hunk_line = patch_lines[patch_idx]
            if not hunk_line: # Skip empty lines in patch that are not part of content
                patch_idx += 1
                continue
            
            op, data = hunk_line[0], hunk_line[1:]
            
            if op == '+':
                output_lines.append(data)
            elif op == '-':
                if original_line_idx >= len(original_lines) or original_lines[original_line_idx] != data:
                    raise ValueError(f"Patch context mismatch at original line {original_line_idx + 1}. Expected content does not match file.")
                original_line_idx += 1
            elif op == ' ':
                if original_line_idx >= len(original_lines) or original_lines[original_line_idx] != data:
                     raise ValueError(f"Patch context mismatch at original line {original_line_idx + 1}. Expected content does not match file.")
                output_lines.append(original_lines[original_line_idx])
                original_line_idx += 1
            elif op == '\\':
                # This informational line from diff can be ignored in our logic
                pass
            else:
                 raise ValueError(f"Invalid patch format: unexpected line prefix '{op}' in hunk.")

            patch_idx += 1
            
    # Add any remaining lines from the original file
    output_lines.extend(original_lines[original_line_idx:])
    
    # Re-join using the original detected line ending
    return original_ending.join(output_lines)


def get_best_available_font(preferred_list: List[str]) -> Optional[str]:
    """
    Scans a preferred list of font families and returns the first one found.
    """
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
    """
    Checks if a file is likely binary based on its extension and, if needed,
    by reading a chunk to check for null bytes.
    """
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