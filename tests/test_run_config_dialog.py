"""Smoke tests for RunConfigDialog."""
from __future__ import annotations

import os
import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

qt_widgets = pytest.importorskip("PyQt6.QtWidgets", reason="PyQt6 required", exc_type=ImportError)
QApplication = qt_widgets.QApplication


@pytest.fixture(scope="module", autouse=True)
def _qt_app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app


def test_run_config_dialog_lists_python_files(tmp_path):
    from ui.dialogs.run_config_dialog import RunConfigDialog

    (tmp_path / "main.py").write_text("print(1)\n", encoding="utf-8")
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "mod.py").write_text("x=1\n", encoding="utf-8")
    (tmp_path / "venv").mkdir()
    (tmp_path / "venv" / "skip.py").write_text("no\n", encoding="utf-8")

    dlg = RunConfigDialog(str(tmp_path))
    rels = [rel for rel, _ in dlg.files]
    assert "main.py" in rels
    assert "pkg/mod.py" in rels or any(r.endswith("mod.py") for r in rels)
    assert not any("venv" in r for r in rels)
