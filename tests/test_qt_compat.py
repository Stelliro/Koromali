"""Tests for the Qt binding compatibility helpers."""
from __future__ import annotations

import importlib
import importlib.machinery
import pathlib
import sys
from types import ModuleType

import pytest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import utils.qt_compat as qt_compat


def _clear_binding(monkeypatch: pytest.MonkeyPatch, package: str) -> None:
    """Remove *package* and its submodules from ``sys.modules`` if present."""

    prefix = f"{package}."
    for name in list(sys.modules):
        if name == package or name.startswith(prefix):
            monkeypatch.delitem(sys.modules, name, raising=False)


def _install_fake_binding(
    monkeypatch: pytest.MonkeyPatch, package: str, submodules: tuple[str, ...]
) -> ModuleType:
    """Create a fake Qt *package* exposing the provided *submodules*."""

    module = ModuleType(package)
    module.__package__ = package
    module.__path__ = []  # type: ignore[attr-defined]
    module.__spec__ = importlib.machinery.ModuleSpec(
        package, loader=None, is_package=True
    )
    monkeypatch.setitem(sys.modules, package, module)

    for submodule in submodules:
        full_name = f"{package}.{submodule}"
        sub = ModuleType(full_name)
        monkeypatch.setitem(sys.modules, full_name, sub)
        setattr(module, submodule, sub)

    return module


def _patch_qt_imports(monkeypatch: pytest.MonkeyPatch) -> None:
    """Intercept Qt binding imports so tests control availability."""

    original_import_module = importlib.import_module

    def fake_import(name: str, package: str | None = None):
        root_name = name.split(".", 1)[0]
        if root_name in {"PyQt6", "PySide6"} and name not in sys.modules:
            raise ModuleNotFoundError(name)
        return original_import_module(name, package)

    monkeypatch.setattr(importlib, "import_module", fake_import)


def _reload_helpers() -> ModuleType:
    """Reload the compatibility module so caches reset for each test."""

    return importlib.reload(qt_compat)


def test_aliases_pyside6_modules_when_only_pyqt6_present(monkeypatch: pytest.MonkeyPatch) -> None:
    """A PyQt6 installation should provide PySide6 imports via the alias shim."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _install_fake_binding(monkeypatch, "PyQt6", ("QtCore", "QtWidgets"))
    _patch_qt_imports(monkeypatch)

    module = _reload_helpers()
    binding = module.ensure_qt_binding()

    assert binding == "PyQt6"
    assert importlib.import_module("PySide6") is sys.modules["PySide6"]
    assert importlib.import_module("PySide6.QtWidgets") is sys.modules["PyQt6.QtWidgets"]


def test_aliases_pyqt6_modules_when_only_pyside6_present(monkeypatch: pytest.MonkeyPatch) -> None:
    """A PySide6 installation should expose PyQt6 module imports."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _install_fake_binding(monkeypatch, "PySide6", ("QtCore", "QtWidgets"))
    _patch_qt_imports(monkeypatch)

    module = _reload_helpers()
    binding = module.ensure_qt_binding()

    assert binding == "PySide6"
    assert importlib.import_module("PyQt6") is sys.modules["PyQt6"]
    assert importlib.import_module("PyQt6.QtWidgets") is sys.modules["PySide6.QtWidgets"]


def test_raises_error_when_no_binding_present(monkeypatch: pytest.MonkeyPatch) -> None:
    """The helper should raise a descriptive error when no bindings are installed."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _patch_qt_imports(monkeypatch)

    module = _reload_helpers()

    with pytest.raises(ImportError, match="No supported Qt binding is installed"):
        module.ensure_qt_binding()
