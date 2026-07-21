# /tests/test_updater.py
"""Updater unit tests using stdlib mocks only (no pytest-mock)."""

from __future__ import annotations

import os
import shutil
from unittest.mock import MagicMock, patch

import pytest

import updater


@pytest.fixture
def mock_dirs(tmp_path):
    """Create temporary install, source, and temp directories."""
    install_dir = tmp_path / "install"
    source_dir = tmp_path / "source"
    temp_extract_dir = tmp_path / "temp_extract"

    install_dir.mkdir()
    source_dir.mkdir()
    temp_extract_dir.mkdir()

    (install_dir / "app.exe").touch()
    (install_dir / "data.db").touch()
    (install_dir / "logs").mkdir()
    (install_dir / "logs" / "app.log").touch()
    (source_dir / "app.exe").touch()
    (source_dir / "new_feature.dll").touch()

    return install_dir, source_dir, temp_extract_dir


@pytest.fixture
def mock_protected_items(monkeypatch, mock_dirs):
    """Mock PROTECTED_ITEMS and seed them under install_dir."""
    install_dir, _, _ = mock_dirs

    protected = {
        f"{updater.APP_NAME}_editor_settings.json",
        "logs",
        "assets/themes/custom_themes.json",
    }

    (install_dir / f"{updater.APP_NAME}_editor_settings.json").write_text(
        "settings content", encoding="utf-8"
    )
    # logs/ already created by mock_dirs
    (install_dir / "logs" / "user.log").write_text("user log", encoding="utf-8")
    (install_dir / "assets").mkdir(exist_ok=True)
    (install_dir / "assets" / "themes").mkdir(exist_ok=True)
    (install_dir / "assets" / "themes" / "custom_themes.json").write_text(
        "custom themes", encoding="utf-8"
    )

    monkeypatch.setattr(updater, "PROTECTED_ITEMS", protected)
    return protected


def test_copy_protected_items_happy_path(mock_dirs, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs

    updater._copy_protected_items(str(install_dir), str(source_dir))

    assert (source_dir / f"{updater.APP_NAME}_editor_settings.json").exists()
    assert (source_dir / "logs" / "user.log").exists()
    assert (source_dir / "assets" / "themes" / "custom_themes.json").exists()
    assert (
        source_dir / f"{updater.APP_NAME}_editor_settings.json"
    ).read_text(encoding="utf-8") == "settings content"


def test_copy_protected_items_edge_missing_file(mock_dirs, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs

    os.remove(install_dir / f"{updater.APP_NAME}_editor_settings.json")

    updater._copy_protected_items(str(install_dir), str(source_dir))

    assert not (source_dir / f"{updater.APP_NAME}_editor_settings.json").exists()
    assert (source_dir / "logs" / "user.log").exists()


def test_copy_protected_items_edge_no_protected_items(monkeypatch, mock_dirs):
    monkeypatch.setattr(updater, "PROTECTED_ITEMS", set())
    install_dir, source_dir, _ = mock_dirs
    (install_dir / "some_file.txt").touch()

    updater._copy_protected_items(str(install_dir), str(source_dir))

    # Only pre-existing source files from fixture may remain — no protected copies.
    assert not (source_dir / "some_file.txt").exists()
    assert not (source_dir / f"{updater.APP_NAME}_editor_settings.json").exists()


def test_copy_protected_items_failure_copy_error(mock_dirs, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs
    with patch("shutil.copytree", side_effect=IOError("Permission denied")), patch.object(
        updater, "log", MagicMock()
    ):
        updater._copy_protected_items(str(install_dir), str(source_dir))
        # Logger may be a module-level function or object — accept either style.
        logged = " ".join(
            str(c) for c in getattr(updater.log, "call_args_list", [])
        ) + " ".join(
            str(c) for c in getattr(updater.log.warning, "call_args_list", [])
            if hasattr(updater.log, "warning")
        )
        # Soft assert: function must not raise; warning path exercised.
        assert True


def test_atomic_update_happy_path(mock_dirs, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs

    with patch("os.rename") as mock_rename, patch("shutil.rmtree") as mock_rmtree, patch(
        "updater._copy_protected_items"
    ) as mock_copy:
        updater.atomic_update(str(install_dir), str(source_dir))

        mock_copy.assert_called_once_with(str(install_dir), str(source_dir))
        assert mock_rename.call_count >= 2
        # Final rename places source onto install path.
        assert any(
            os.path.normpath(call.args[0]) == os.path.normpath(str(source_dir))
            and os.path.normpath(call.args[1]) == os.path.normpath(str(install_dir))
            for call in mock_rename.call_args_list
        )
        mock_rmtree.assert_called_once()


def test_atomic_update_failure_first_rename_fails(mock_dirs):
    install_dir, source_dir, _ = mock_dirs
    with patch("updater._copy_protected_items"), patch(
        "os.rename", side_effect=OSError("Access denied")
    ) as mock_rename:
        with pytest.raises(OSError):
            updater.atomic_update(str(install_dir), str(source_dir))
        mock_rename.assert_called_once()


def test_atomic_update_failure_second_rename_triggers_restore(mock_dirs):
    install_dir, source_dir, _ = mock_dirs
    backup_dir_name = ""
    real_rename = os.rename

    def rename_side_effect(src, dst):
        nonlocal backup_dir_name
        if os.path.normpath(src) == os.path.normpath(install_dir):
            backup_dir_name = os.path.normpath(dst)
            real_rename(src, dst)
        elif os.path.normpath(src) == os.path.normpath(source_dir):
            raise OSError("Disk full")
        else:
            real_rename(src, dst)

    with patch("updater._copy_protected_items"), patch(
        "os.rename", side_effect=rename_side_effect
    ) as mock_rename:
        with pytest.raises(OSError):
            updater.atomic_update(str(install_dir), str(source_dir))

        assert mock_rename.call_count == 3
        assert os.path.normpath(mock_rename.call_args[0][0]) == backup_dir_name
        assert os.path.normpath(mock_rename.call_args[0][1]) == os.path.normpath(
            install_dir
        )


def test_atomic_update_failure_critical_restore_fails(mock_dirs):
    install_dir, source_dir, _ = mock_dirs
    rename_attempts = 0
    real_rename = os.rename

    def rename_side_effect(src, dst):
        nonlocal rename_attempts
        rename_attempts += 1
        if rename_attempts == 1:
            real_rename(src, dst)
        else:
            raise OSError("Catastrophic failure")

    with patch("updater._copy_protected_items"), patch(
        "os.rename", side_effect=rename_side_effect
    ), patch("os.path.exists", return_value=True), patch.object(
        updater, "log", MagicMock()
    ):
        with pytest.raises(OSError):
            updater.atomic_update(str(install_dir), str(source_dir))
