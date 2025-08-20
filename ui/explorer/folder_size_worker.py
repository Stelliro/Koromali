# Koromali/ui/explorer/folder_size_worker.py
import os
from typing import Optional, TYPE_CHECKING
from PyQt6.QtCore import QObject, QRunnable, pyqtSignal
from utils.helpers import LARGE_TOKEN_COUNT
from utils.logger import log

if TYPE_CHECKING:
    from plugins.ai_suite.token_cache import TokenCache


class WorkerSignals(QObject):
    """Defines signals available from a running worker."""
    # path, total_size, total_tokens, dict of {filepath: (size, token_count, is_binary)}
    finished = pyqtSignal(str, int, int, dict)


class FolderSizeWorker(QRunnable):
    """
    A QRunnable worker that recursively scans a path to calculate total size
    and estimate token counts for text files, using a cache for efficiency.
    """
    TOKEN_ESTIMATE_DIVISOR = 4
    TOKEN_COUNT_LIMIT = 1_000_000
    CHUNK_SIZE = 16 * 1024 
    BINARY_EXTENSIONS = {
        '.exe', '.dll', '.so', '.o', '.a', '.lib', '.dylib', '.app', '.msi',
        '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
        '.zip', '.rar', '.7z', '.gz', '.tar', '.bz2', '.iso',
        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
        '.mp3', '.wav', '.flac', '.mp4', '.mkv', '.avi', '.mov', '.wmv',
        '.eot', '.woff', '.woff2', '.ttf', '.otf',
        '.db', '.sqlite3', '.dat', '.gguf', '.bin', '.pth', '.safetensors', '.onnx'
    }

    def __init__(self, path: str, token_cache: Optional['TokenCache'] = None):
        super().__init__()
        self.path = path
        self.token_cache = token_cache
        self.signals = WorkerSignals()
        self.is_cancelled = False

    def run(self):
        total_size, total_tokens, file_data = 0, 0, {}
        try:
            for dirpath, _, filenames in os.walk(self.path, topdown=True, onerror=None):
                if self.is_cancelled: break
                for f in filenames:
                    if self.is_cancelled: break
                    filepath = os.path.join(dirpath, f)
                    try:
                        if os.path.islink(filepath): continue
                        
                        size = os.path.getsize(filepath)
                        total_size += size
                        is_binary, token_count = False, 0
                        
                        cached_tokens = self.token_cache.get(filepath) if self.token_cache else None
                        if cached_tokens is not None:
                            token_count = cached_tokens
                        else:
                            _name, ext = os.path.splitext(f); ext = ext.lower()
                            if ext in self.BINARY_EXTENSIONS:
                                is_binary = True
                            else:
                                try:
                                    if size // self.TOKEN_ESTIMATE_DIVISOR > self.TOKEN_COUNT_LIMIT:
                                        token_count = -self.TOKEN_COUNT_LIMIT
                                    else:
                                        char_count = 0
                                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as fo:
                                            while chunk := fo.read(self.CHUNK_SIZE):
                                                char_count += len(chunk)
                                                if char_count // self.TOKEN_ESTIMATE_DIVISOR > self.TOKEN_COUNT_LIMIT:
                                                    token_count = -self.TOKEN_COUNT_LIMIT
                                                    break
                                        if token_count == 0:
                                            token_count = char_count // self.TOKEN_ESTIMATE_DIVISOR
                                except (IOError, OSError, UnicodeDecodeError):
                                    is_binary = True
                            
                            if self.token_cache:
                                self.token_cache.set(filepath, token_count if not is_binary else 0)

                        if not is_binary and token_count != 0:
                            total_tokens += abs(token_count)
                        file_data[filepath] = (size, token_count, is_binary)
                    except (OSError, FileNotFoundError):
                        continue
            
            if not self.is_cancelled:
                self.signals.finished.emit(self.path, total_size, total_tokens, file_data)
        except Exception as e:
            log.error(f"FolderSizeWorker failed unexpectedly for path '{self.path}': {e}", exc_info=True)
            if not self.is_cancelled:
                self.signals.finished.emit(self.path, -1, -1, {})
        finally:
            if self.token_cache:
                self.token_cache.save()

    def cancel(self):
        """Stops the worker."""
        self.is_cancelled = True