"""Utility helpers for selecting a Qt binding at runtime."""
from __future__ import annotations

import importlib
import sys
from typing import Iterable

__all__ = [
    "ensure_qt_binding",
    "get_available_binding",
    "QT_OPTIONAL_SUBMODULES",
    "QT_SUBMODULES",
]

QT_SUBMODULES: tuple[str, ...] = (
    "QtCore",
    "QtGui",
    "QtWidgets",
    "QtWebEngineCore",
    "QtWebEngineWidgets",
)

QT_OPTIONAL_SUBMODULES: frozenset[str] = frozenset(
    {
        "QtWebEngineCore",
        "QtWebEngineWidgets",
    }
)

_BINDING_NAME: str | None = None


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


def _import_binding(binding: str) -> set[str]:
    """Import *binding* and return the set of available submodules."""

    importlib.import_module(binding)

    available_submodules: set[str] = set()
    for submodule in QT_SUBMODULES:
        full_name = f"{binding}.{submodule}"
        try:
            importlib.import_module(full_name)
        except ModuleNotFoundError as exc:
            if submodule in QT_OPTIONAL_SUBMODULES:
                continue
            raise ImportError(
                f"Missing required Qt module {full_name}"
            ) from exc
        except Exception as exc:
            if submodule in QT_OPTIONAL_SUBMODULES:
                continue
            raise ImportError(
                f"Failed to import required Qt module {full_name}"
            ) from exc
        else:
            available_submodules.add(submodule)

    return available_submodules


def _alias_binding_modules(
    source_package: str, target_package: str, available_submodules: set[str]
) -> None:
    """Expose *target_package* modules backed by *source_package*."""

    if target_package in sys.modules:
        return

    source_module = sys.modules[source_package]
    sys.modules[target_package] = source_module

    for submodule in available_submodules:
        source_name = f"{source_package}.{submodule}"
        target_name = f"{target_package}.{submodule}"
        module = sys.modules.get(source_name)
        if module is not None:
            sys.modules[target_name] = module

    _sync_signal_api(source_package)
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
            available = _import_binding(candidate)
        except Exception as exc:  # pragma: no cover - pass error to next candidate
            last_error = exc
            continue

        other = "PySide6" if candidate == "PyQt6" else "PyQt6"
        try:
            _alias_binding_modules(candidate, other, available)
        except Exception as exc:  # pragma: no cover - aliasing errors are fatal
            last_error = exc
            continue

        _BINDING_NAME = candidate
        return candidate

    message = "No supported Qt binding is installed. Please install PyQt6 or PySide6."
    if last_error is not None:
        raise ImportError(message) from last_error
    raise ImportError(message)


def get_available_binding() -> str | None:
    """Return the cached Qt binding name if :func:`ensure_qt_binding` ran."""

    return _BINDING_NAME
