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


def _ensure_package_stub(package_name: str) -> ModuleType:
    """Return a lazily created package module for *package_name*."""

    package = sys.modules.get(package_name)
    if package is None:
        package = ModuleType(package_name)
        package.__path__ = []  # type: ignore[attr-defined]
        sys.modules[package_name] = package
    return package


def _sync_signal_api(package_name: str) -> None:
    """Normalise QtCore signal helpers for the aliased *package_name*."""

    qtcore = sys.modules.get(f"{package_name}.QtCore")
    if qtcore is None:
        return

    if package_name == "PyQt6":
        if not hasattr(qtcore, "pyqtSignal") and hasattr(qtcore, "Signal"):
            setattr(qtcore, "pyqtSignal", getattr(qtcore, "Signal"))
        if not hasattr(qtcore, "pyqtSlot") and hasattr(qtcore, "Slot"):
            setattr(qtcore, "pyqtSlot", getattr(qtcore, "Slot"))
    elif package_name == "PySide6":
        if not hasattr(qtcore, "Signal") and hasattr(qtcore, "pyqtSignal"):
            setattr(qtcore, "Signal", getattr(qtcore, "pyqtSignal"))
        if not hasattr(qtcore, "Slot") and hasattr(qtcore, "pyqtSlot"):
            setattr(qtcore, "Slot", getattr(qtcore, "pyqtSlot"))


def _alias_binding_modules(source_package: str, target_package: str) -> None:
    """Expose *target_package* modules backed by *source_package*."""

    try:
        importlib.import_module(target_package)
    except ModuleNotFoundError:
        pass
    else:
        # A native implementation is available; do not overwrite it.
        return

    package = _ensure_package_stub(target_package)

    for submodule in QT_SUBMODULES:
        try:
            module = importlib.import_module(f"{source_package}.{submodule}")
        except ModuleNotFoundError:
            continue
        sys.modules[f"{target_package}.{submodule}"] = module
        setattr(package, submodule, module)

    _sync_signal_api(target_package)


def ensure_qt_binding(preferred: Iterable[str] | None = None) -> str:
    """Ensure that at least one supported Qt binding is importable."""

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
            _alias_binding_modules("PyQt6", "PySide6")
            _BINDING_NAME = candidate
            return candidate

        _alias_binding_modules(candidate, "PyQt6")
        _BINDING_NAME = candidate
        return candidate

    message = "No supported Qt binding is installed. Please install PyQt6 or PySide6."
    if last_error is not None:
        raise ImportError(message) from last_error
    raise ImportError(message)


def get_available_binding() -> str | None:
    """Return the cached Qt binding name if :func:`ensure_qt_binding` ran."""

    return _BINDING_NAME
