"""Utility helpers for selecting a Qt binding at runtime."""
from __future__ import annotations

import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import sys
from types import ModuleType
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
_ALIAS_FINDERS: dict[tuple[str, str], "_BindingAliasFinder"] = {}


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
        target_available = False
    else:
        target_available = True

    available_submodules: set[str] = set()
    for submodule in QT_SUBMODULES:
        full_name = f"{source_package}.{submodule}"
        try:
            module = importlib.import_module(full_name)
        except ModuleNotFoundError as exc:
            if submodule in QT_OPTIONAL_SUBMODULES:
                continue
            raise ImportError(
                f"Missing required Qt module {source_package}.{submodule}"
            ) from exc
        except Exception as exc:
            if submodule in QT_OPTIONAL_SUBMODULES:
                continue
            raise ImportError(
                f"Failed to import required Qt module {full_name}"
            ) from exc
        else:
            available_submodules.add(submodule)
            sys.modules.setdefault(full_name, module)

    if not target_available:
        _install_alias_finder(source_package, target_package, available_submodules)

    _sync_signal_api(source_package)

    _sync_signal_api(target_package)


class _BindingAliasFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Meta path finder/loader that aliases *target_root* to *source_root*."""

    def __init__(
        self,
        source_root: str,
        target_root: str,
        submodules: frozenset[str],
    ) -> None:
        self._source_root = source_root
        self._target_root = target_root
        self._submodules = submodules

    def find_spec(
        self,
        fullname: str,
        path: Iterable[str] | None,
        target: ModuleType | None = None,
    ) -> importlib.machinery.ModuleSpec | None:
        if fullname == self._target_root:
            mapped = self._source_root
        elif fullname.startswith(f"{self._target_root}."):
            suffix = fullname[len(self._target_root) + 1 :]
            if suffix.split(".", 1)[0] not in self._submodules:
                return None
            mapped = f"{self._source_root}.{suffix}"
        else:
            return None

        spec = importlib.util.find_spec(mapped)
        if spec is None:
            return None

        is_package = spec.submodule_search_locations is not None
        return importlib.machinery.ModuleSpec(
            fullname,
            self,
            origin=spec.origin,
            is_package=is_package,
        )

    def create_module(self, spec: importlib.machinery.ModuleSpec) -> ModuleType | None:
        return None  # Use default module creation semantics

    def exec_module(self, module: ModuleType) -> None:
        suffix = module.__name__[len(self._target_root) :]
        mapped = f"{self._source_root}{suffix}"
        actual = importlib.import_module(mapped)

        sys.modules[module.__name__] = actual

        parent_name, _, attr_name = module.__name__.rpartition(".")
        if parent_name:
            parent = sys.modules.get(parent_name)
            if parent is not None:
                setattr(parent, attr_name, actual)

        _sync_signal_api(self._target_root)


def _install_alias_finder(
    source_root: str, target_root: str, submodules: set[str]
) -> None:
    """Install a meta path finder to alias *target_root* to *source_root*."""

    key = (source_root, target_root)
    if key in _ALIAS_FINDERS:
        return

    finder = _BindingAliasFinder(source_root, target_root, frozenset(submodules))
    sys.meta_path.insert(0, finder)
    _ALIAS_FINDERS[key] = finder


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

        try:
            if candidate == "PyQt6":
                _alias_binding_modules("PyQt6", "PySide6")
            else:
                _alias_binding_modules(candidate, "PyQt6")
        except ImportError as exc:
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
