import os

import pytest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

qt_widgets = pytest.importorskip(
    "PyQt6.QtWidgets",
    reason="PyQt6 QtWidgets module is required for this test",
    exc_type=ImportError,
)
qt_core = pytest.importorskip(
    "PyQt6.QtCore",
    reason="PyQt6 QtCore module is required for this test",
    exc_type=ImportError,
)

QApplication = qt_widgets.QApplication  # type: ignore[attr-defined]
Qt = qt_core.Qt  # type: ignore[attr-defined]

from plugins.ai_suite.ai_studio_dialog import CheckableFileSystemModel
from plugins.ai_suite.workers import MAX_TOKEN_ANALYSIS_BYTES, TokenCountWorker


@pytest.fixture(scope="module", autouse=True)
def _qt_app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app


def test_token_worker_marks_overflow(tmp_path):
    large_path = tmp_path / "large.md"
    large_bytes = MAX_TOKEN_ANALYSIS_BYTES + 1024
    large_path.write_text("a" * large_bytes, encoding="utf-8")

    worker = TokenCountWorker(str(tmp_path), [], token_cache=None)
    tokens, overflow = worker._estimate_tokens_for_file(str(large_path), large_bytes)

    assert overflow is True
    assert tokens >= large_bytes // 4


def test_model_formats_overflow_tokens(tmp_path):
    project_root = tmp_path / "project"
    project_root.mkdir()
    file_path = project_root / "file.md"
    file_path.write_text("sample", encoding="utf-8")

    model = CheckableFileSystemModel()
    model.setRootPath(str(project_root))
    model.set_project_root(str(project_root))

    metadata = {
        str(file_path): {
            "tokens": 5000,
            "size": file_path.stat().st_size,
            "tokens_overflow": True,
        }
    }
    model.apply_metadata(metadata)

    display = model._format_tokens_display(str(file_path))
    assert display is not None
    assert display.startswith("Above ")

    index = model.index(str(file_path))
    tooltip = model.data(index, Qt.ItemDataRole.ToolTipRole)
    assert tooltip is None or "lower bound" in tooltip
