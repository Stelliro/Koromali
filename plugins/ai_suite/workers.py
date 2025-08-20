# /plugins/ai_suite/workers.py
from __future__ import annotations
import os
from typing import Dict, List, Optional

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
    finished = pyqtSignal(bool, dict)  # (success, {path: tokens})

class TokenCountWorker(QRunnable):
    """Background token counting for a list of files.

    Uses a simple estimator (~4 chars per token) and caches results by file
    mtime + size via TokenCache.
    """
    def __init__(self, project_root: str, file_paths: List[str], token_cache) -> None:
        super().__init__()
        self.project_root = project_root
        self.file_paths = list(file_paths or [])
        self.token_cache = token_cache
        self.signals = _Signals()

    # crude but fast
    @staticmethod
    def _estimate_tokens_for_text(text: str) -> int:
        # 1 token ~ 4 chars heuristic
        return max(1, int(len(text) / 4))

    def _estimate_tokens_for_file(self, path: str) -> Optional[int]:
        try:
            # Skip obviously binary by scanning for NUL bytes in first chunk
            with open(path, "rb") as fb:
                head = fb.read(4096)
                if b"\x00" in head:
                    return None
            # Read as text ignoring errors
            with open(path, "r", encoding="utf-8", errors="ignore") as ft:
                text = ft.read()
            return self._estimate_tokens_for_text(text)
        except Exception:
            return None

    def run(self) -> None:
        try:
            results: Dict[str, int] = {}
            for fp in self.file_paths:
                cached = self.token_cache.get(fp) if self.token_cache else None
                if cached is not None:
                    results[fp] = int(cached)
                    continue
                est = self._estimate_tokens_for_file(fp)
                if est is not None:
                    results[fp] = int(est)
                    if self.token_cache:
                        self.token_cache.set(fp, est)
            if self.token_cache:
                self.token_cache.save()
            self.signals.finished.emit(True, results)
        except Exception as e:
            log.error(f"TokenCountWorker failed: {e}")
            self.signals.finished.emit(False, {})
