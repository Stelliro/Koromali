"""Utilities for managing AI style presets stored on disk.

This module loads and persists style preset definitions for the AI Suite plugin.
Presets are lightweight dictionaries of string keys and values that control how
personas present responses (for example, their tone). The default presets ship
with the plugin and cannot be deleted, while user-defined presets are saved
inside the ``.koromali`` application data directory.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List

from utils.helpers import get_base_path
from utils.logger import log

PresetDict = Dict[str, str]

# Built-in presets that should always be available. These are merged with any
# user-defined presets loaded from disk, and they are never written back to the
# JSON file to keep the on-disk format clean.
DEFAULT_PRESETS: Dict[str, PresetDict] = {
    "Default": {"tone": "balanced"},
    "Detailed": {"tone": "detailed"},
    "Friendly": {"tone": "friendly"},
}


def _validate_preset(data: Dict[str, Any] | None) -> PresetDict:
    """Return a sanitized copy of a preset mapping."""

    sanitized: PresetDict = {}
    for key, value in (data or {}).items():
        if isinstance(key, str) and isinstance(value, str):
            sanitized[key] = value
    return sanitized


class StylePresetManager:
    """Manage reading, writing, and querying AI style presets."""

    def __init__(self) -> None:
        base_path = get_base_path()
        self._directory = os.path.join(base_path, ".koromali")
        self._file_path = os.path.join(self._directory, "style_presets.json")
        self._presets: Dict[str, PresetDict] = {}
        self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def list_presets(self) -> List[str]:
        """Return the available preset names with built-ins sorted first."""

        names = list(self._presets.keys())
        names.sort(key=lambda name: (0 if name in DEFAULT_PRESETS else 1, name.lower()))
        return names

    def get_preset(self, name: str) -> PresetDict:
        """Return a copy of the preset for *name* or the default preset."""

        preset = self._presets.get(name) or DEFAULT_PRESETS["Default"]
        return dict(preset)

    def upsert_preset(self, name: str, data: Dict[str, Any]) -> None:
        """Create or update a user-defined preset."""

        normalized_name = (name or "Unnamed").strip()
        if not normalized_name:
            normalized_name = "Preset"
        if normalized_name.lower() == "default":
            normalized_name = "Default"
        else:
            normalized_name = normalized_name[:1].upper() + normalized_name[1:]

        if normalized_name in DEFAULT_PRESETS:
            raise ValueError("Default presets cannot be modified.")

        clean_data = _validate_preset(data)
        if not clean_data:
            raise ValueError("Preset must contain at least one string key/value pair.")

        self._presets[normalized_name] = clean_data
        self._save()

    def delete_preset(self, name: str) -> bool:
        """Delete a user-defined preset. Returns ``True`` if removed."""

        if name in DEFAULT_PRESETS:
            return False

        removed = self._presets.pop(name, None) is not None
        if removed:
            self._save()
        return removed

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _load(self) -> None:
        """Load presets from disk and merge them with defaults."""

        try:
            os.makedirs(self._directory, exist_ok=True)
            if os.path.exists(self._file_path):
                with open(self._file_path, "r", encoding="utf-8") as handle:
                    raw_data = json.load(handle)
            else:
                raw_data = {}
            if not isinstance(raw_data, dict):
                raw_data = {}
        except Exception as exc:  # pragma: no cover - defensive logging
            log.warning("Could not load style presets: %s", exc)
            raw_data = {}

        sanitized: Dict[str, PresetDict] = {}
        for preset_name, preset_data in raw_data.items():
            if not isinstance(preset_name, str) or not isinstance(preset_data, dict):
                continue
            if preset_name in DEFAULT_PRESETS:
                # Always prefer the built-in definitions for default presets.
                continue
            clean_preset = _validate_preset(preset_data)
            if clean_preset:
                sanitized[preset_name] = clean_preset

        self._presets = {**{name: dict(data) for name, data in DEFAULT_PRESETS.items()}, **sanitized}

    def _save(self) -> None:
        """Persist user-defined presets to disk."""

        try:
            os.makedirs(self._directory, exist_ok=True)
            to_write: Dict[str, PresetDict] = {}
            for name, preset in self._presets.items():
                if name in DEFAULT_PRESETS and preset == DEFAULT_PRESETS[name]:
                    continue
                to_write[name] = preset
            with open(self._file_path, "w", encoding="utf-8") as handle:
                json.dump(to_write, handle, indent=2, ensure_ascii=False)
        except Exception as exc:  # pragma: no cover - defensive logging
            log.warning("Could not save style presets: %s", exc)
