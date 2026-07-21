# /tests/test_tray_app.py
"""Unit tests for the system-tray helper (stdlib mocks only — no pytest-mock)."""

from __future__ import annotations

import importlib
import os
import sys
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest


class _FakeQApplication:
    def __init__(self, argv=None):
        pass

    def setQuitOnLastWindowClosed(self, value):
        pass

    def quit(self):
        pass


class _FakeQIcon:
    def __init__(self, path=None):
        self.path = path


class _FakeSignal:
    def __init__(self):
        self._callback = None

    def connect(self, callback):
        self._callback = callback


class _FakeQAction:
    def __init__(self, text="", parent=None):
        self.text = text
        self.triggered = _FakeSignal()


class _FakeMenu:
    def __init__(self):
        self.actions = []

    def addAction(self, action):
        self.actions.append(action)

    def addSeparator(self):
        self.actions.append(None)


class _FakeTrayIcon:
    def __init__(self, icon=None, parent=None):
        self.icon = icon
        self.parent = parent
        self.tooltip = None
        self.menu = None
        self.shown = False
        self.messages = []
        self.activated = _FakeSignal()

    def setToolTip(self, text):
        self.tooltip = text

    def setContextMenu(self, menu):
        self.menu = menu

    def show(self):
        self.shown = True

    def showMessage(self, title, message, icon=None):
        self.messages.append((title, message, icon))


@pytest.fixture
def tray_mod():
    saved = {
        key: sys.modules.get(key)
        for key in ("PyQt6", "PyQt6.QtWidgets", "PyQt6.QtGui", "tray_app")
    }

    widgets = SimpleNamespace(
        QApplication=_FakeQApplication,
        QSystemTrayIcon=_FakeTrayIcon,
        QMenu=_FakeMenu,
    )
    # ActivationReason enum used by on_tray_activated
    _FakeTrayIcon.ActivationReason = SimpleNamespace(Trigger=1)
    _FakeTrayIcon.MessageIcon = SimpleNamespace(Critical=3)

    gui = SimpleNamespace(QIcon=_FakeQIcon, QAction=_FakeQAction)

    sys.modules["PyQt6"] = MagicMock()
    sys.modules["PyQt6.QtWidgets"] = widgets
    sys.modules["PyQt6.QtGui"] = gui
    sys.modules.pop("tray_app", None)

    import tray_app

    importlib.reload(tray_app)
    yield tray_app

    for key, mod in saved.items():
        if mod is None:
            sys.modules.pop(key, None)
        else:
            sys.modules[key] = mod
    sys.modules.pop("tray_app", None)


def test_tray_helper_frozen_environment(tray_mod):
    base = os.path.join(os.sep, "opt", "Koromali")
    with patch.object(sys, "frozen", True, create=True), patch.object(
        sys, "executable", os.path.join(base, "KoromaliTray.exe")
    ), patch("os.path.exists", return_value=True):
        helper = tray_mod.TrayHelper()
        assert helper.is_frozen is True
        assert helper.base_dir == base
        assert helper.get_app_name() == "Koromali"
        assert helper.get_executable_path("Koromali") == os.path.join(
            base, "Koromali.exe"
        )
        assert helper.get_icon_path("Koromali") == os.path.join(
            base, "assets", "koromali.ico"
        )


def test_tray_helper_source_environment(tray_mod):
    source_root = os.path.dirname(os.path.abspath(tray_mod.__file__))
    with patch.object(sys, "frozen", False, create=True), patch(
        "os.path.exists", return_value=True
    ):
        helper = tray_mod.TrayHelper()
        assert helper.is_frozen is False
        assert helper.base_dir == source_root
        assert helper.get_app_name() == "Koromali"
        assert helper.get_executable_path("Koromali") == os.path.join(
            source_root, "main.py"
        )
        assert helper.get_icon_path("Koromali") == os.path.join(
            source_root, "assets", "koromali.ico"
        )


def test_tray_helper_failure_no_icon(tray_mod):
    with patch.object(sys, "frozen", True, create=True), patch(
        "os.path.exists", return_value=False
    ):
        helper = tray_mod.TrayHelper()
        assert helper.get_icon_path("Koromali") == ""


def test_KoromaliTrayApp_happy_path(tray_mod):
    with patch.object(
        tray_mod.TrayHelper, "get_app_name", return_value="Koromali"
    ), patch.object(
        tray_mod.TrayHelper, "get_executable_path", return_value="/path/to/Koromali.exe"
    ), patch.object(
        tray_mod.TrayHelper, "get_icon_path", return_value="/path/to/icon.ico"
    ):
        app = tray_mod.KoromaliTrayApp([])
        assert app.tray_icon.tooltip == "Koromali"
        assert isinstance(app.tray_icon.icon, _FakeQIcon)
        assert app.tray_icon.icon.path == "/path/to/icon.ico"
        assert app.tray_icon.menu is not None
        assert app.tray_icon.shown is True


def test_KoromaliTrayApp_edge_no_icon(tray_mod):
    with patch.object(
        tray_mod.TrayHelper, "get_executable_path", return_value="/path/to/Koromali.exe"
    ), patch.object(tray_mod.TrayHelper, "get_icon_path", return_value=""):
        app = tray_mod.KoromaliTrayApp([])
        # Default tray icon (no path) is still constructed.
        assert app.tray_icon is not None
        assert app.tray_icon.icon is None or getattr(app.tray_icon.icon, "path", None) in (
            None,
            "",
        )


def test_open_editor_frozen_happy_path(tray_mod):
    with patch("os.path.exists", return_value=True), patch(
        "subprocess.Popen"
    ) as mock_popen:
        app = tray_mod.KoromaliTrayApp([])
        app.helper.is_frozen = True
        app.main_app_path = "/path/to/Koromali.exe"
        app.open_editor()
        mock_popen.assert_called_once_with(["/path/to/Koromali.exe"])


def test_open_editor_source_happy_path(tray_mod):
    with patch("os.path.exists", return_value=True), patch(
        "subprocess.Popen"
    ) as mock_popen:
        app = tray_mod.KoromaliTrayApp([])
        app.helper.is_frozen = False
        app.main_app_path = "/path/to/project/main.py"
        with patch.object(sys, "executable", "/usr/bin/python3"):
            app.open_editor()
            mock_popen.assert_called_once_with(
                ["/usr/bin/python3", "/path/to/project/main.py"]
            )


def test_open_editor_failure_exe_not_found(tray_mod):
    with patch("os.path.exists", return_value=False), patch(
        "subprocess.Popen"
    ) as mock_popen:
        app = tray_mod.KoromaliTrayApp([])
        app.main_app_path = "/invalid/path/Koromali.exe"
        app.open_editor()
        mock_popen.assert_not_called()
        assert app.tray_icon.messages
        assert app.tray_icon.messages[0][0] == "Error"


def test_open_editor_failure_launch_error(tray_mod):
    with patch("os.path.exists", return_value=True), patch(
        "subprocess.Popen", side_effect=OSError("Permission denied")
    ) as mock_popen:
        app = tray_mod.KoromaliTrayApp([])
        app.helper.is_frozen = True
        app.main_app_path = "/path/to/Koromali.exe"
        app.open_editor()
        mock_popen.assert_called_once()
        assert app.tray_icon.messages
        assert app.tray_icon.messages[0][0] == "Launch Error"
