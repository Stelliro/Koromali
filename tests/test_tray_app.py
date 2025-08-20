# /tests/test_tray_app.py
import sys
import os
from unittest.mock import MagicMock, patch
import pytest

# Mock PyQt6 before it's imported by the app
# This is crucial for running tests in an environment without a display.
mock_qt_widgets = {
    'QApplication': MagicMock(),
    'QSystemTrayIcon': MagicMock(),
    'QMenu': MagicMock(),
}
sys.modules['PyQt6.QtWidgets'] = MagicMock(**mock_qt_widgets)
sys.modules['PyQt6.QtGui'] = MagicMock()

# Now we can import the tray_app
import tray_app

# --- Tests for TrayHelper ---

# Attack Vector: Test helper class when running in a bundled (frozen) environment.
def test_tray_helper_frozen_environment(mocker):
    mocker.patch.object(sys, 'frozen', True)
    mocker.patch.object(sys, 'executable', '/opt/Koromali/KoromaliTray.exe')
    mocker.patch('os.path.exists', return_value=True)

    helper = tray_app.TrayHelper()
    
    assert helper.is_frozen is True
    assert helper.base_dir == '/opt/Koromali'
    assert helper.get_app_name() == "Koromali"
    assert helper.get_executable_path("Koromali") == '/opt/Koromali/Koromali.exe'
    assert helper.get_icon_path("Koromali") == '/opt/Koromali/assets/koromali.ico'

# Attack Vector: Test helper class when running from source code.
def test_tray_helper_source_environment(mocker):
    mocker.patch.object(sys, 'frozen', False, create=True)
    # The path is relative to the file's location in the test directory
    mocker.patch('os.path.exists', return_value=True)
    
    helper = tray_app.TrayHelper()
    source_root = os.path.dirname(os.path.dirname(os.path.abspath(tray_app.__file__)))

    assert helper.is_frozen is False
    assert helper.base_dir == source_root
    assert helper.get_app_name() == "Koromali"
    assert helper.get_executable_path("Koromali") == os.path.join(source_root, 'main.py')
    assert helper.get_icon_path("Koromali") == os.path.join(source_root, 'assets/koromali.ico')

# Attack Vector: Test when no icon file can be found at all.
def test_tray_helper_failure_no_icon(mocker):
    mocker.patch.object(sys, 'frozen', True)
    mocker.patch('os.path.exists', return_value=False)

    helper = tray_app.TrayHelper()
    assert helper.get_icon_path("Koromali") == ""


# --- Tests for KoromaliTrayApp ---

# Attack Vector: Test the ideal initialization of the tray application.
def test_KoromaliTrayApp_happy_path(mocker):
    # This test is limited because we can't easily test the GUI logic,
    # but we can test that the setup calls are made correctly.
    mocker.patch('tray_app.TrayHelper.get_app_name', return_value='Koromali')
    mocker.patch('tray_app.TrayHelper.get_executable_path', return_value='/path/to/Koromali.exe')
    mocker.patch('tray_app.TrayHelper.get_icon_path', return_value='/path/to/icon.ico')
    mock_qicon = mocker.patch('PyQt6.QtGui.QIcon')
    
    app = tray_app.KoromaliTrayApp([])

    # Assertions
    app.tray_icon.setToolTip.assert_called_with("Koromali")
    mock_qicon.assert_called_with('/path/to/icon.ico')
    app.tray_icon.setContextMenu.assert_called_once()
    app.tray_icon.show.assert_called_once()

# Attack Vector: Test initialization when the icon file is not found.
def test_KoromaliTrayApp_edge_no_icon(mocker):
    mocker.patch('tray_app.TrayHelper.get_executable_path', return_value='/path/to/Koromali.exe')
    mocker.patch('tray_app.TrayHelper.get_icon_path', return_value='') # Empty string for not found
    mock_qicon = mocker.patch('PyQt6.QtGui.QIcon')

    app = tray_app.KoromaliTrayApp([])

    # Assert that QIcon was NOT called with a path, meaning the default icon was used.
    mock_qicon.assert_not_called()
    assert isinstance(app.tray_icon, MagicMock) # Ensure it was still created

# --- Tests for open_editor ---

# Attack Vector: Test opening the editor when frozen and the executable exists.
def test_open_editor_frozen_happy_path(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('tray_app.TrayHelper.is_frozen', True)
    mock_popen = mocker.patch('subprocess.Popen')
    
    app = tray_app.KoromaliTrayApp([])
    app.main_app_path = '/path/to/Koromali.exe'
    app.open_editor()
    
    mock_popen.assert_called_once_with(['/path/to/Koromali.exe'])

# Attack Vector: Test opening the editor from source.
def test_open_editor_source_happy_path(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('tray_app.TrayHelper.is_frozen', False)
    mock_popen = mocker.patch('subprocess.Popen')
    
    app = tray_app.KoromaliTrayApp([])
    app.main_app_path = '/path/to/project/main.py'
    # Mock sys.executable for consistency
    with patch.object(sys, 'executable', '/usr/bin/python3'):
        app.open_editor()
        mock_popen.assert_called_once_with(['/usr/bin/python3', '/path/to/project/main.py'])

# Attack Vector: Test trying to open the editor when the executable is not found.
def test_open_editor_failure_exe_not_found(mocker):
    mocker.patch('os.path.exists', return_value=False)
    mock_popen = mocker.patch('subprocess.Popen')
    
    app = tray_app.KoromaliTrayApp([])
    app.main_app_path = '/invalid/path/Koromali.exe'
    app.open_editor()
    
    mock_popen.assert_not_called()
    app.tray_icon.showMessage.assert_called_once()
    # Check that the title of the error message is "Error"
    assert app.tray_icon.showMessage.call_args[0][0] == "Error"

# Attack Vector: Test when subprocess.Popen raises an exception during launch.
def test_open_editor_failure_launch_error(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mock_popen = mocker.patch('subprocess.Popen', side_effect=OSError("Permission denied"))

    app = tray_app.KoromaliTrayApp([])
    app.main_app_path = '/path/to/Koromali.exe'
    app.open_editor()

    mock_popen.assert_called_once()
    app.tray_icon.showMessage.assert_called_once()
    assert app.tray_icon.showMessage.call_args[0][0] == "Launch Error"