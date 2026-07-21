"""Tests for the Qt binding compatibility helpers."""
from __future__ import annotations

import importlib
import pathlib
import sys
from types import ModuleType
from typing import Callable, Dict

import pytest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import utils.qt_compat as qt_compat


_FAKE_ERRORS: Dict[str, Callable[[], BaseException]] = {}


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
    monkeypatch.setitem(sys.modules, package, module)

    for submodule in submodules:
        full_name = f"{package}.{submodule}"
        sub = ModuleType(full_name)
        sub.__package__ = package
        monkeypatch.setitem(sys.modules, full_name, sub)
        setattr(module, submodule, sub)

    return module


def _install_fake_root(monkeypatch: pytest.MonkeyPatch, package: str) -> ModuleType:
    """Install a bare package module without any submodules."""

    module = ModuleType(package)
    module.__package__ = package
    module.__path__ = []  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, package, module)
    return module


def _patch_imports(monkeypatch: pytest.MonkeyPatch) -> None:
    """Intercept Qt binding imports so tests control availability."""

    def fake_import(name: str, package: str | None = None):
        if name in _FAKE_ERRORS:
            raise _FAKE_ERRORS[name]()
        if name in sys.modules:
            return sys.modules[name]
        raise ModuleNotFoundError(name)

    monkeypatch.setattr(importlib, "import_module", fake_import)
    monkeypatch.setattr(qt_compat.importlib, "import_module", fake_import)


def _reload_helpers(monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    """Reload the compatibility module so caches reset for each test."""

    monkeypatch.setitem(qt_compat.__dict__, "_BINDING_NAME", None)
    return importlib.reload(qt_compat)


def _set_import_error(name: str, error: BaseException | type[BaseException] | None) -> None:
    """Configure a custom error when ``import_module`` is asked for *name*."""

    if error is None:
        _FAKE_ERRORS.pop(name, None)
        return

    if isinstance(error, type) and issubclass(error, BaseException):
        _FAKE_ERRORS[name] = error
    else:
        _FAKE_ERRORS[name] = lambda error=error: error


def test_aliases_pyside6_modules_when_only_pyqt6_present(monkeypatch: pytest.MonkeyPatch) -> None:
    """A PyQt6 installation should provide PySide6 imports via the alias shim."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _install_fake_binding(monkeypatch, "PyQt6", ("QtCore", "QtGui", "QtWidgets"))
    _patch_imports(monkeypatch)

    module = _reload_helpers(monkeypatch)
    binding = module.ensure_qt_binding()

    assert binding == "PyQt6"
    assert sys.modules["PySide6"] is sys.modules["PyQt6"]
    assert sys.modules["PySide6.QtWidgets"] is sys.modules["PyQt6.QtWidgets"]


def test_aliases_pyqt6_modules_when_only_pyside6_present(monkeypatch: pytest.MonkeyPatch) -> None:
    """A PySide6 installation should expose PyQt6 module imports."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _install_fake_binding(monkeypatch, "PySide6", ("QtCore", "QtGui", "QtWidgets"))
    _patch_imports(monkeypatch)

    module = _reload_helpers(monkeypatch)
    binding = module.ensure_qt_binding()

    assert binding == "PySide6"
    assert sys.modules["PyQt6"] is sys.modules["PySide6"]
    assert sys.modules["PyQt6.QtWidgets"] is sys.modules["PySide6.QtWidgets"]


def test_raises_error_when_no_binding_present(monkeypatch: pytest.MonkeyPatch) -> None:
    """The helper should raise a descriptive error when no bindings are installed."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _patch_imports(monkeypatch)

    module = _reload_helpers(monkeypatch)

    with pytest.raises(ImportError, match="No supported Qt binding is installed"):
        module.ensure_qt_binding()


def test_aliasing_skips_optional_modules_that_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """Optional Qt modules that raise during import should not break aliasing."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _install_fake_binding(monkeypatch, "PyQt6", ("QtCore", "QtGui", "QtWidgets"))
    _patch_imports(monkeypatch)
    _set_import_error("PyQt6.QtWebEngineCore", ImportError("libEGL missing"))
    _set_import_error("PyQt6.QtWebEngineWidgets", ImportError("libEGL missing"))

    module = _reload_helpers(monkeypatch)
    binding = module.ensure_qt_binding()

    assert binding == "PyQt6"
    assert sys.modules["PySide6.QtWidgets"] is sys.modules["PyQt6.QtWidgets"]


def test_falls_back_when_required_module_import_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    """If a binding fails to provide required modules, the next option is tried."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")

    _install_fake_root(monkeypatch, "PyQt6")
    _install_fake_binding(monkeypatch, "PySide6", ("QtCore", "QtGui", "QtWidgets"))
    _patch_imports(monkeypatch)
    _set_import_error("PyQt6.QtWidgets", ImportError("libGL missing"))

    module = _reload_helpers(monkeypatch)
    binding = module.ensure_qt_binding()

    assert binding == "PySide6"


def test_raises_error_when_required_modules_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """A binding that lacks required modules should not be selected."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")

    _install_fake_root(monkeypatch, "PyQt6")
    _patch_imports(monkeypatch)
    _set_import_error("PyQt6.QtWidgets", ImportError("libGL missing"))

    module = _reload_helpers(monkeypatch)

    with pytest.raises(ImportError, match="No supported Qt binding is installed"):
        module.ensure_qt_binding()
