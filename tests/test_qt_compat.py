"""Tests for the Qt binding compatibility helpers."""
from __future__ import annotations

import importlib
import importlib.machinery
import pathlib
import sys
from types import ModuleType
from typing import Callable, Dict

import pytest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import utils.qt_compat as qt_compat


_FAKE_SPECS: Dict[str, importlib.machinery.ModuleSpec] = {}
_FAKE_ERRORS: Dict[str, Callable[[], BaseException]] = {}


def _clear_binding(monkeypatch: pytest.MonkeyPatch, package: str) -> None:
    """Remove *package* and its submodules from ``sys.modules`` if present."""

    prefix = f"{package}."
    for name in list(sys.modules):
        if name == package or name.startswith(prefix):
            monkeypatch.delitem(sys.modules, name, raising=False)

    for name in list(_FAKE_SPECS):
        if name == package or name.startswith(prefix):
            del _FAKE_SPECS[name]

    for name in list(_FAKE_ERRORS):
        if name == package or name.startswith(prefix):
            del _FAKE_ERRORS[name]


def _install_fake_binding(
    monkeypatch: pytest.MonkeyPatch, package: str, submodules: tuple[str, ...]
) -> ModuleType:
    """Create a fake Qt *package* exposing the provided *submodules*."""

    module = ModuleType(package)
    module.__package__ = package
    module.__path__ = []  # type: ignore[attr-defined]
    spec = importlib.machinery.ModuleSpec(package, loader=None, is_package=True)
    module.__spec__ = spec
    _FAKE_SPECS[package] = spec
    monkeypatch.setitem(sys.modules, package, module)

    for submodule in submodules:
        full_name = f"{package}.{submodule}"
        sub = ModuleType(full_name)
        sub.__package__ = package
        sub.__spec__ = importlib.machinery.ModuleSpec(full_name, loader=None)
        monkeypatch.setitem(sys.modules, full_name, sub)
        setattr(module, submodule, sub)
        _FAKE_SPECS[full_name] = sub.__spec__

    return module


def _install_fake_root(monkeypatch: pytest.MonkeyPatch, package: str) -> ModuleType:
    """Install a bare package module without any submodules."""

    module = ModuleType(package)
    module.__package__ = package
    module.__path__ = []  # type: ignore[attr-defined]
    spec = importlib.machinery.ModuleSpec(package, loader=None, is_package=True)
    module.__spec__ = spec
    _FAKE_SPECS[package] = spec
    monkeypatch.setitem(sys.modules, package, module)
    return module


def _patch_qt_imports(monkeypatch: pytest.MonkeyPatch) -> None:
    """Intercept Qt binding imports so tests control availability."""

    original_import_module = importlib.import_module
    original_find_spec = importlib.util.find_spec

    def fake_import(name: str, package: str | None = None):
        if name in sys.modules:
            return sys.modules[name]
        root_name = name.split(".", 1)[0]
        if root_name in {"PyQt6", "PySide6"}:
            for source_root, target_root in qt_compat._ALIAS_FINDERS.keys():
                if name == source_root or name.startswith(f"{source_root}."):
                    break
                if name == target_root or name.startswith(f"{target_root}."):
                    break
            else:
                raise ModuleNotFoundError(name)
        return original_import_module(name, package)

    def fake_find_spec(name: str, package: str | None = None):
        if name in _FAKE_ERRORS:
            raise _FAKE_ERRORS[name]()
        if name in _FAKE_SPECS:
            return _FAKE_SPECS[name]

        spec = original_find_spec(name, package)
        if spec is None:
            return None

        if isinstance(spec.loader, qt_compat._BindingAliasFinder):  # type: ignore[attr-defined]
            return spec

        root_name = name.split(".", 1)[0]
        if root_name in {"PyQt6", "PySide6"}:
            return None

        return spec

    monkeypatch.setattr(importlib, "import_module", fake_import)
    monkeypatch.setattr(qt_compat.importlib, "import_module", fake_import)
    monkeypatch.setattr(importlib.util, "find_spec", fake_find_spec)
    monkeypatch.setattr(qt_compat.importlib.util, "find_spec", fake_find_spec)


def _reload_helpers() -> ModuleType:
    """Reload the compatibility module so caches reset for each test."""

    return importlib.reload(qt_compat)


def _set_spec_error(name: str, error: BaseException | type[BaseException] | None) -> None:
    """Configure a custom error when ``find_spec`` is asked for *name*."""

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
    _install_fake_binding(monkeypatch, "PySide6", ("QtCore", "QtGui", "QtWidgets"))
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


def test_aliasing_skips_optional_modules_that_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """Optional Qt modules that raise during import should not break aliasing."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")
    _install_fake_binding(monkeypatch, "PyQt6", ("QtCore", "QtGui", "QtWidgets"))
    _patch_qt_imports(monkeypatch)
    _set_spec_error("PyQt6.QtWebEngineCore", ImportError("libEGL missing"))

    module = _reload_helpers()
    binding = module.ensure_qt_binding()

    assert binding == "PyQt6"
    assert importlib.import_module("PySide6.QtWidgets") is sys.modules["PyQt6.QtWidgets"]


def test_falls_back_when_required_module_import_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    """If a binding fails to provide required modules, the next option is tried."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")

    _install_fake_root(monkeypatch, "PyQt6")
    _install_fake_binding(monkeypatch, "PySide6", ("QtCore", "QtGui", "QtWidgets"))
    _patch_qt_imports(monkeypatch)
    _FAKE_SPECS["PyQt6.QtWidgets"] = importlib.machinery.ModuleSpec(
        "PyQt6.QtWidgets", loader=None
    )
    _set_spec_error("PyQt6.QtWidgets", ImportError("libGL missing"))

    module = _reload_helpers()
    binding = module.ensure_qt_binding()

    assert binding == "PySide6"


def test_raises_error_when_required_modules_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """A binding that lacks required modules should not be selected."""

    _clear_binding(monkeypatch, "PyQt6")
    _clear_binding(monkeypatch, "PySide6")

    _install_fake_root(monkeypatch, "PyQt6")
    _patch_qt_imports(monkeypatch)
    _FAKE_SPECS["PyQt6.QtWidgets"] = importlib.machinery.ModuleSpec(
        "PyQt6.QtWidgets", loader=None
    )
    _set_spec_error("PyQt6.QtWidgets", ImportError("libGL missing"))

    module = _reload_helpers()

    with pytest.raises(ImportError, match="No supported Qt binding is installed"):
        module.ensure_qt_binding()
