# /plugins/ai_suite/workers.py
from __future__ import annotations
import os
from typing import Dict, Iterator, List, Optional, Tuple

from PyQt6.QtCore import QRunnable, QObject, pyqtSignal

try:
    from utils.logger import log
except Exception:  # pragma: no cover
    class _L:
        def info(self, *a, **k): print("[INFO]", *a)
        def warning(self, *a, **k): print("[WARN]", *a)
        def error(self, *a, **k): print("[ERROR]", *a)
    log = _L()

class _Signals(QObject):
    finished = pyqtSignal(bool, dict)  # (success, {path: {"tokens": int, "size": int}})


MAX_TOKEN_ANALYSIS_BYTES = 512 * 1024  # 512 KiB cap for full token analysis

class TokenCountWorker(QRunnable):
    """Background token counting for a list of files.

    Uses a simple estimator (~4 chars per token) and caches results by file
    mtime + size via TokenCache.
    """
    def __init__(
        self,
        project_root: str,
        file_paths: List[str],
        token_cache,
        *,
        exclude_dirs: Optional[set[str]] = None,
        skip_extensions: Optional[set[str]] = None,
    ) -> None:
        super().__init__()
        self.project_root = project_root
        self.file_paths = list(file_paths or [])
        self.token_cache = token_cache
        self.signals = _Signals()
        self.exclude_dirs = {d.lower() for d in (exclude_dirs or set())}
        self.skip_extensions = {ext.lower() for ext in (skip_extensions or set())}

    # crude but fast
    @staticmethod
    def _estimate_tokens_for_text(text: str) -> int:
        # 1 token ~ 4 chars heuristic
        return max(1, int(len(text) / 4))

    def _estimate_tokens_for_file(
        self, path: str, file_size: Optional[int]
    ) -> Tuple[Optional[int], bool]:
        """Return a token estimate and whether the file exceeded the analysis cap."""

        try:
            # Skip obviously binary by scanning for NUL bytes in first chunk
            with open(path, "rb") as fb:
                head = fb.read(4096)
                if b"\x00" in head:
                    return None, False
        except Exception:
            return None, False

        try:
            size = file_size if file_size is not None else os.path.getsize(path)
        except OSError:
            size = None

        if size is not None and size > MAX_TOKEN_ANALYSIS_BYTES:
            approx = max(1, int(size / 4))
            return approx, True

        try:
            # Read as text ignoring errors for manageable files
            with open(path, "r", encoding="utf-8", errors="ignore") as ft:
                text = ft.read()
            return self._estimate_tokens_for_text(text), False
        except Exception:
            return None, False

    def _iter_files(self) -> Iterator[str]:
        for path in self.file_paths:
            if not path:
                continue
            norm_path = os.path.abspath(path)
            if os.path.isdir(norm_path):
                yield from self._walk_directory(norm_path)
            else:
                yield norm_path

    def _walk_directory(self, root: str) -> Iterator[str]:
        root = os.path.abspath(root)
        for current_root, dirnames, filenames in os.walk(root):
            filtered_dirs = []
            for name in dirnames:
                if name.lower() in self.exclude_dirs:
                    continue
                filtered_dirs.append(name)
            dirnames[:] = filtered_dirs

            for name in filenames:
                file_path = os.path.join(current_root, name)
                yield file_path

    def _should_skip(self, path: str) -> bool:
        ext = os.path.splitext(path)[1].lower()
        return bool(ext and ext in self.skip_extensions)

    def run(self) -> None:
        try:
            results: Dict[str, Dict[str, object]] = {}
            for fp in self._iter_files():
                if self._should_skip(fp):
                    continue

                cached = self.token_cache.get(fp) if self.token_cache else None
                try:
                    size = os.path.getsize(fp)
                except OSError:
                    size = None

                if cached is not None:
                    payload: Dict[str, object] = {"tokens": int(cached)}
                    if size is not None:
                        payload["size"] = int(size)
                    results[fp] = payload
                    continue

                est, overflow = self._estimate_tokens_for_file(fp, size)
                if est is not None:
                    payload: Dict[str, object] = {"tokens": int(est)}
                    if size is not None:
                        payload["size"] = int(size)
                    if overflow:
                        payload["tokens_overflow"] = True
                    results[fp] = payload
                    if self.token_cache and not overflow:
                        self.token_cache.set(fp, est)
                elif size is not None:
                    results[fp] = {"size": int(size)}
            if self.token_cache:
                self.token_cache.save()
            self.signals.finished.emit(True, results)
        except Exception as e:
            log.error(f"TokenCountWorker failed: {e}")
            self.signals.finished.emit(False, {})
