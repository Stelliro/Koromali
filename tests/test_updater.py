# /tests/test_updater.py
import os
import shutil
import time
import pytest
from unittest.mock import MagicMock, patch

# Assuming updater.py is in the same directory or accessible via PYTHONPATH
import updater

# --- Fixtures ---

@pytest.fixture
def mock_dirs(tmp_path):
    """Creates temporary install, source, and temp directories for testing."""
    install_dir = tmp_path / "install"
    source_dir = tmp_path / "source"
    temp_extract_dir = tmp_path / "temp_extract"
    
    install_dir.mkdir()
    source_dir.mkdir()
    temp_extract_dir.mkdir()

    # Create some dummy files and folders
    (install_dir / "app.exe").touch()
    (install_dir / "data.db").touch()
    (install_dir / "logs").mkdir()
    (install_dir / "logs" / "app.log").touch()
    (source_dir / "app.exe").touch()
    (source_dir / "new_feature.dll").touch()
    
    return install_dir, source_dir, temp_extract_dir

@pytest.fixture
def mock_protected_items(monkeypatch, tmp_path):
    """Mocks the PROTECTED_ITEMS set and creates them in the install_dir."""
    install_dir, _, _ = mock_dirs(tmp_path)
    
    protected = {
        f"{updater.APP_NAME}_editor_settings.json",
        "logs",
        "assets/themes/custom_themes.json"
    }
    
    # Create the protected items in the mocked install directory
    (install_dir / f"{updater.APP_NAME}_editor_settings.json").write_text("settings content")
    (install_dir / "logs").mkdir()
    (install_dir / "logs" / "user.log").write_text("user log")
    (install_dir / "assets").mkdir()
    (install_dir / "assets" / "themes").mkdir()
    (install_dir / "assets" / "themes" / "custom_themes.json").write_text("custom themes")
    
    monkeypatch.setattr(updater, "PROTECTED_ITEMS", protected)
    return protected

# --- Tests for _copy_protected_items ---

# Attack Vector: Test the ideal scenario with all protected items present.
def test_copy_protected_items_happy_path(mocker, tmp_path, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    
    # Run the function
    updater._copy_protected_items(str(install_dir), str(source_dir))

    # Assertions
    assert (source_dir / f"{updater.APP_NAME}_editor_settings.json").exists()
    assert (source_dir / "logs" / "user.log").exists()
    assert (source_dir / "assets" / "themes" / "custom_themes.json").exists()
    assert (source_dir / f"{updater.APP_NAME}_editor_settings.json").read_text() == "settings content"

# Attack Vector: Test with a protected file that does not exist in the source.
def test_copy_protected_items_edge_missing_file(mocker, tmp_path, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    
    # Remove one of the protected files from the install directory
    os.remove(install_dir / f"{updater.APP_NAME}_editor_settings.json")

    # Run the function
    updater._copy_protected_items(str(install_dir), str(source_dir))
    
    # Assertions
    assert not (source_dir / f"{updater.APP_NAME}_editor_settings.json").exists()
    assert (source_dir / "logs" / "user.log").exists() # Ensure others were still copied

# Attack Vector: Test with an empty PROTECTED_ITEMS set.
def test_copy_protected_items_edge_no_protected_items(mocker, tmp_path):
    monkeypatch = mocker.patch.object(updater, "PROTECTED_ITEMS", new=set())
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    (install_dir / "some_file.txt").touch()

    updater._copy_protected_items(str(install_dir), str(source_dir))

    assert not any(source_dir.iterdir()) # Source dir should remain empty

# Attack Vector: Test when a copy operation fails.
def test_copy_protected_items_failure_copy_error(mocker, tmp_path, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    mocker.patch('shutil.copytree', side_effect=IOError("Permission denied"))
    mocker.patch('updater.log') # Mock the logger to check calls
    
    updater._copy_protected_items(str(install_dir), str(source_dir))
    
    # Assert that a warning was logged
    updater.log.assert_any_call("  - WARNING: Could not preserve 'logs': Permission denied")

# --- Tests for atomic_update ---

# Attack Vector: Test the standard, successful update process.
def test_atomic_update_happy_path(mocker, tmp_path, mock_protected_items):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    
    # Mock os and shutil functions
    mocker.patch('os.rename')
    mocker.patch('shutil.rmtree')
    mock_copy_protected = mocker.patch('updater._copy_protected_items')

    updater.atomic_update(str(install_dir), str(source_dir))

    # Assertions
    mock_copy_protected.assert_called_once_with(str(install_dir), str(source_dir))
    os.rename.assert_any_call(str(install_dir), mocker.ANY) # first rename to backup
    os.rename.assert_any_call(str(source_dir), str(install_dir)) # second rename to final
    shutil.rmtree.assert_called_once() # The backup is removed

# Attack Vector: Test failure during the first rename (install -> backup).
def test_atomic_update_failure_first_rename_fails(mocker, tmp_path):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    mocker.patch('updater._copy_protected_items')
    mock_rename = mocker.patch('os.rename', side_effect=OSError("Access denied"))
    
    with pytest.raises(OSError):
        updater.atomic_update(str(install_dir), str(source_dir))

    # Ensure no cleanup was attempted and no second rename happened
    mock_rename.assert_called_once()
    
# Attack Vector: Test failure during the second rename (source -> install), triggering a restore.
def test_atomic_update_failure_second_rename_triggers_restore(mocker, tmp_path):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    backup_dir_name = ""

    def rename_side_effect(src, dst):
        nonlocal backup_dir_name
        # Use normpath to handle potential OS differences in path separators
        if os.path.normpath(src) == os.path.normpath(install_dir):
            # This is the first rename, let it succeed and capture the backup path
            backup_dir_name = os.path.normpath(dst)
            os.rename(src, dst)
        elif os.path.normpath(src) == os.path.normpath(source_dir):
            # This is the second rename, make it fail
            raise OSError("Disk full")
        else:
            # This is the restore rename
            os.rename(src, dst)

    mocker.patch('updater._copy_protected_items')
    mock_rename = mocker.patch('os.rename', side_effect=rename_side_effect)
    
    original_exists = os.path.exists
    def exists_side_effect(path):
        if backup_dir_name and os.path.normpath(path) == backup_dir_name:
            return True
        return original_exists(path)
    mocker.patch('os.path.exists', side_effect=exists_side_effect)

    with pytest.raises(OSError):
        updater.atomic_update(str(install_dir), str(source_dir))

    # Assert the restore was attempted
    assert mock_rename.call_count == 3
    # The last call should be the restore
    assert os.path.normpath(mock_rename.call_args[0][0]) == backup_dir_name
    assert os.path.normpath(mock_rename.call_args[0][1]) == os.path.normpath(install_dir)

# Attack Vector: Test a critical failure where even the restore fails.
def test_atomic_update_failure_critical_restore_fails(mocker, tmp_path):
    install_dir, source_dir, _ = mock_dirs(tmp_path)
    
    # Make the second and third renames fail
    rename_attempts = 0
    def rename_side_effect(src, dst):
        nonlocal rename_attempts
        rename_attempts += 1
        if rename_attempts == 1:
            # First rename (backup) succeeds. Let the real rename happen
            # so the path exists for the subsequent failed restore attempt.
            os.rename(src, dst)
        else:
            # All subsequent renames fail
            raise OSError("Catastrophic failure")

    mocker.patch('updater._copy_protected_items')
    mocker.patch('os.rename', side_effect=rename_side_effect)
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('updater.log')

    with pytest.raises(OSError):
        updater.atomic_update(str(install_dir), str(source_dir))

    updater.log.assert_any_call("CRITICAL: FAILED TO RESTORE BACKUP. Catastrophic failure")