"""Utility helpers for selecting a Qt binding at runtime."""
from __future__ import annotations

import importlib
import sys
from types import ModuleType
from typing import Iterable

__all__ = ["ensure_qt_binding", "get_available_binding", "QT_SUBMODULES"]

QT_SUBMODULES: tuple[str, ...] = (
    "QtCore",
    "QtGui",
    "QtWidgets",
    "QtWebEngineCore",
    "QtWebEngineWidgets",
)

_BINDING_NAME: str | None = None


def _install_alias_modules(source_package: str) -> None:
    """Expose ``PyQt6`` style modules backed by *source_package*.

    The function registers lightweight aliases inside :mod:`sys.modules` so that
    ``from PyQt6.QtWidgets import QWidget`` keeps working even if the runtime
    only ships with an alternative binding such as :mod:`PySide6`.
    """

    package = sys.modules.get("PyQt6")
    if package is None:
        package = ModuleType("PyQt6")
        package.__path__ = []  # type: ignore[attr-defined]
        sys.modules["PyQt6"] = package

    for submodule in QT_SUBMODULES:
        module = importlib.import_module(f"{source_package}.{submodule}")
        sys.modules[f"PyQt6.{submodule}"] = module
        setattr(package, submodule, module)

    if source_package == "PySide6":
        qtcore = sys.modules.get("PyQt6.QtCore")
        if qtcore is not None:
            # PySide6 exposes ``Signal``/``Slot`` while Koromali imports the
            # PyQt6 equivalents. Mirror the expected attribute names.
            if not hasattr(qtcore, "pyqtSignal") and hasattr(qtcore, "Signal"):
                setattr(qtcore, "pyqtSignal", getattr(qtcore, "Signal"))
            if not hasattr(qtcore, "pyqtSlot") and hasattr(qtcore, "Slot"):
                setattr(qtcore, "pyqtSlot", getattr(qtcore, "Slot"))


def ensure_qt_binding(preferred: Iterable[str] | None = None) -> str:
    """Ensure that at least one supported Qt binding is importable.

    The project imports :mod:`PyQt6` across the codebase, but some
    environments (especially Windows distributions) may only provide
    :mod:`PySide6`.  This function looks for a usable binding in
    *preferred* order and, when necessary, installs shim modules so the
    rest of the code continues to import from :mod:`PyQt6`.

    Returns the resolved binding name.
    Raises :class:`ImportError` if no supported binding is available.
    """

    global _BINDING_NAME
    if _BINDING_NAME:
        return _BINDING_NAME

    search_order = tuple(preferred) if preferred is not None else ("PyQt6", "PySide6")

    last_error: Exception | None = None
    for candidate in search_order:
        try:
            importlib.import_module(candidate)
        except Exception as exc:  # pragma: no cover - pass error to next candidate
            last_error = exc
            continue

        if candidate == "PyQt6":
            _BINDING_NAME = candidate
            return candidate

        _install_alias_modules(candidate)
        _BINDING_NAME = candidate
        return candidate

    message = "No supported Qt binding is installed. Please install PyQt6 or PySide6."
    if last_error is not None:
        raise ImportError(message) from last_error
    raise ImportError(message)


def get_available_binding() -> str | None:
    """Return the cached Qt binding name if :func:`ensure_qt_binding` ran."""

    return _BINDING_NAME
