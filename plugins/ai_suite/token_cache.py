# AI Suite token_cache version: 2025-08-20-v1
from __future__ import annotations

import json
import os
from typing import Dict, Optional

try:
    from utils.logger import log
except Exception:  # pragma: no cover
    class _L:
        def info(self, *a, **k): print("[INFO]", *a)
        def warning(self, *a, **k): print("[WARN]", *a)
        def error(self, *a, **k): print("[ERROR]", *a)
    log = _L()

class TokenCache:
    """Project-scoped token count cache.

    Stores a mapping of FILE PATH -> {mtime, size, tokens} under
    <project_root>/.koromali/token_cache.json

    The cache is validated by file mtime and size. If either changes,
    the entry is considered stale.
    """
    def __init__(self, project_root: str) -> None:
        self.project_root = os.path.abspath(project_root)
        self.cache_dir = os.path.join(self.project_root, ".koromali")
        self.cache_file = os.path.join(self.cache_dir, "token_cache.json")
        self._data: Dict[str, Dict] = {}
        self._ensure_dirs()
        self._data = self._load()

    # ---------- public API ----------
    def get(self, path: str) -> Optional[int]:
        """Return cached token count for 'path' if still valid, else None."""
        try:
            path = os.path.abspath(path)
            st = os.stat(path)
        except Exception:
            return None
        entry = self._data.get(path)
        if not entry:
            return None
        if entry.get("mtime") == st.st_mtime and entry.get("size") == st.st_size:
            return int(entry.get("tokens", 0))
        return None

    def set(self, path: str, tokens: int) -> None:
        path = os.path.abspath(path)
        try:
            st = os.stat(path)
            self._data[path] = {"mtime": st.st_mtime, "size": st.st_size, "tokens": int(tokens)}
        except Exception:
            # If file vanished mid-run, drop the entry
            self._data.pop(path, None)

    def set_many(self, mapping: Dict[str, int]) -> None:
        for p, t in (mapping or {}).items():
            self.set(p, t)

    def save(self) -> None:
        try:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            log.warning(f"Failed to save token cache: {e}")

    # ---------- internals ----------
    def _ensure_dirs(self) -> None:
        try:
            os.makedirs(self.cache_dir, exist_ok=True)
        except Exception as e:
            log.warning(f"Failed to create cache dir: {e}")

    def _load(self) -> Dict[str, Dict]:
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data if isinstance(data, dict) else {}
            return {}
        except Exception as e:
            log.warning(f"Failed to load token cache: {e}")
            return {}
