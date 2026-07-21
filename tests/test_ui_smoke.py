"""
UI smoke harness for Koromali.

Boots the real MainWindow (with plugins), exercises core chrome, and saves
window grabs under tests/_smoke_artifacts/ for visual inspection.

Run:
  set PYTHONPATH=.
  set QT_QPA_PLATFORM=windows   # or offscreen
  python -m pytest tests/test_ui_smoke.py -v -s
"""

from __future__ import annotations

import os
import sys
import traceback
from pathlib import Path

import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "windows")

qt_widgets = pytest.importorskip(
    "PyQt6.QtWidgets",
    reason="PyQt6 required for UI smoke",
    exc_type=ImportError,
)
qt_core = pytest.importorskip(
    "PyQt6.QtCore",
    reason="PyQt6 required for UI smoke",
    exc_type=ImportError,
)

QApplication = qt_widgets.QApplication
QDialog = qt_widgets.QDialog
Qt = qt_core.Qt
QTimer = qt_core.QTimer


ARTIFACT_DIR = Path(__file__).resolve().parent / "_smoke_artifacts"
REPO_ROOT = Path(__file__).resolve().parents[1]


def _process_events(app: QApplication, rounds: int = 20) -> None:
    for _ in range(rounds):
        app.processEvents()


def _grab(widget, name: str) -> Path:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    path = ARTIFACT_DIR / f"{name}.png"
    pix = widget.grab()
    ok = pix.save(str(path), "PNG")
    assert ok, f"Failed to save screenshot {path}"
    assert path.is_file() and path.stat().st_size > 0
    return path


@pytest.fixture(scope="module")
def qt_app():
    # Ensure repo root on path for plugin discovery
    root = str(REPO_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)

    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    yield app


@pytest.fixture(scope="module")
def main_window(qt_app):
    from app_core.settings_manager import SettingsManager
    from app_core.theme_manager import ThemeManager
    from app_core.file_handler import FileHandler
    from ui.main_window import MainWindow

    settings = SettingsManager()
    # Avoid restoring huge previous session during smoke
    settings.set("open_projects", [], save_immediately=False)
    settings.set("active_project_path", None, save_immediately=False)
    settings.set("open_files", [], save_immediately=False)
    settings.set("last_theme_id", "Koromali_modern_dark", save_immediately=False)

    theme = ThemeManager(settings)
    theme.apply_theme_to_app(qt_app)
    file_handler = FileHandler(settings)

    window = MainWindow(
        file_handler=file_handler,
        theme_manager=theme,
        settings_manager=settings,
        debug_mode=True,
    )
    window.show()
    _process_events(qt_app, 10)

    # Deferred init loads plugins — pump events until it has run
    window._deferred_initialization()
    _process_events(qt_app, 40)

    yield window

    # Graceful teardown — kill shell processes before destroying the window
    # (avoids intermittent Windows access violations with QProcess).
    try:
        for dock in window.findChildren(qt_widgets.QDockWidget):
            w = dock.widget()
            if w is not None and hasattr(w, "stop_process"):
                try:
                    w.stop_process()
                except Exception:
                    pass
        window.close()
        _process_events(qt_app, 10)
        window.deleteLater()
        _process_events(qt_app, 10)
    except Exception:
        traceback.print_exc()


def test_smoke_main_window_chrome(qt_app, main_window):
    assert main_window.isVisible() or main_window.isHidden() is False
    assert main_window.menuBar() is not None
    assert main_window.menuBar().actions(), "Menu bar has no actions"
    assert main_window.statusBar() is not None
    assert hasattr(main_window, "tab_widget")
    assert main_window.tab_widget is not None

    # Theme stylesheet applied
    ss = qt_app.styleSheet()
    assert ss and "QMainWindow" in ss
    assert "QGroupBox" in ss  # makeover styles present

    path = _grab(main_window, "01_main_window_dark")
    print(f"[smoke] main window grab -> {path}")


def test_smoke_theme_switch(qt_app, main_window):
    tm = main_window.theme_manager
    for theme_id, label in (
        ("Koromali_modern_light", "02_main_window_light"),
        ("Koromali_modern_dark", "03_main_window_dark_again"),
    ):
        tm.set_theme(theme_id, qt_app)
        _process_events(qt_app, 10)
        assert tm.current_theme_id == theme_id
        path = _grab(main_window, label)
        print(f"[smoke] theme {theme_id} -> {path}")


def test_smoke_ai_studio_dialog(qt_app, main_window):
    from plugins.ai_suite.ai_studio_dialog import AIStudioDialog

    dlg = AIStudioDialog(main_window.koromali_api, parent=main_window)
    dlg.show()
    _process_events(qt_app, 15)

    assert dlg.windowTitle()
    # Tabs: Export + AI Patcher (simplified studio)
    assert hasattr(dlg, "btn_copy") or hasattr(dlg, "txt_preview") or hasattr(dlg, "patch_input")
    # Empty state must not root the file tree at the entire filesystem.
    assert not dlg.tree.isEnabled() or dlg.project_root is not None
    preview = dlg.txt_preview.toPlainText().lower()
    assert "no open project" in preview or dlg.project_root is not None

    path = _grab(dlg, "04_ai_studio")
    print(f"[smoke] AI Studio -> {path}")

    dlg.close()
    _process_events(qt_app, 5)


def test_smoke_run_config_dialog(qt_app, main_window, tmp_path):
    from ui.dialogs.run_config_dialog import RunConfigDialog

    (tmp_path / "main.py").write_text("print('ok')\n", encoding="utf-8")
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "util.py").write_text("x=1\n", encoding="utf-8")

    dlg = RunConfigDialog(str(tmp_path), parent=main_window)
    dlg.show()
    _process_events(qt_app, 10)

    assert dlg.file_list.count() >= 2
    path = _grab(dlg, "05_run_config")
    print(f"[smoke] RunConfig -> {path}")
    dlg.close()


def test_smoke_preferences_dialog(qt_app, main_window):
    from ui.preferences_dialog import PreferencesDialog

    dlg = PreferencesDialog(
        main_window.theme_manager,
        main_window.source_control_manager
        if hasattr(main_window, "source_control_manager")
        else main_window.koromali_api.get_manager("git"),
        main_window.github_manager
        if hasattr(main_window, "github_manager")
        else main_window.koromali_api.get_manager("github"),
        main_window.plugin_manager,
        main_window.koromali_api,
        main_window.settings,
        parent=main_window,
    )
    dlg.show()
    _process_events(qt_app, 15)
    path = _grab(dlg, "06_preferences")
    print(f"[smoke] Preferences -> {path}")
    dlg.close()


def test_smoke_splash_screen(qt_app):
    from ui.widgets.splash_screen import SplashScreen

    splash = SplashScreen()
    splash.show()
    splash.set_status("UI smoke")
    _process_events(qt_app, 20)
    path = _grab(splash, "07_splash")
    print(f"[smoke] Splash -> {path}")
    try:
        splash.timer.stop()
    except Exception:
        pass
    splash.close()
    _process_events(qt_app, 5)


def test_smoke_plugin_menus_present(qt_app, main_window):
    """After deferred init, expect Tools menu to exist and have actions."""
    tools = getattr(main_window, "tools_menu", None)
    # Menu may be created via plugin API as tools_menu
    if tools is None:
        for action in main_window.menuBar().actions():
            menu = action.menu()
            if menu and "tool" in action.text().lower():
                tools = menu
                break
    assert tools is not None, "Tools menu not found"
    texts = [a.text() for a in tools.actions() if a.text()]
    print(f"[smoke] Tools menu actions: {texts}")
    # Soft check — AI Studio is registered by plugin
    joined = " | ".join(texts).lower()
    assert "ai" in joined or "studio" in joined or len(texts) > 0


def test_smoke_open_project_folder(qt_app, main_window, tmp_path):
    """Open a tiny project and ensure explorer does not explode."""
    proj = tmp_path / "smoke_proj"
    proj.mkdir()
    (proj / "hello.py").write_text("print('smoke')\n", encoding="utf-8")

    pm = main_window.project_manager
    if hasattr(pm, "open_project"):
        pm.open_project(str(proj))
    elif hasattr(pm, "add_project"):
        pm.add_project(str(proj))
    _process_events(qt_app, 20)

    if hasattr(main_window, "explorer_panel") and main_window.explorer_panel:
        main_window.explorer_panel.refresh()
        _process_events(qt_app, 15)

    path = _grab(main_window, "08_with_project")
    print(f"[smoke] with project -> {path}")
