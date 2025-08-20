# Koromali/tray_app.py
import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction

# Hardcode the app name for true standalone functionality.
# This avoids a fragile import from the main app's code.
APP_NAME = "Koromali"

class TrayHelper:
    """A helper class to manage paths and names for the tray application."""

    def __init__(self):
        self.is_frozen = getattr(sys, 'frozen', False)
        self.base_dir = os.path.dirname(sys.executable) if self.is_frozen else os.path.dirname(os.path.abspath(__file__))

    def get_app_name(self) -> str:
        """Determines the main application's name from its own executable name."""
        if self.is_frozen:
            my_exe_name = os.path.basename(sys.executable)
            # e.g., "KoromaliTray.exe" -> "Koromali"
            if "Tray.exe" in my_exe_name:
                return my_exe_name.replace("Tray.exe", "")
        return APP_NAME

    def get_executable_path(self, app_name: str) -> str:
        """Determines the path of the main application executable."""
        if self.is_frozen:
            # When frozen, the main exe is in the same directory
            return os.path.join(self.base_dir, f"{app_name}.exe")
        else:
            # When running from source, point to the root of the project to find main.py
            return os.path.join(self.base_dir, "main.py")

    def get_icon_path(self, app_name: str) -> str:
        """Determines the path of the application icon."""
        # This path structure is for the installer build and source.
        icon_path = os.path.join(self.base_dir, "assets", "koromali.ico")
        return icon_path if os.path.exists(icon_path) else ""


class KoromaliTrayApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setQuitOnLastWindowClosed(False)

        self.helper = TrayHelper()
        self.app_name = self.helper.get_app_name()
        self.main_app_path = self.helper.get_executable_path(self.app_name)
        icon_path = self.helper.get_icon_path(self.app_name)

        if not icon_path:
            print("Error: Could not find application icon.", file=sys.stderr)
            self.tray_icon = QSystemTrayIcon(self) # Use default icon
        else:
            self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)

        self.tray_icon.setToolTip(self.app_name)

        menu = QMenu()
        open_action = QAction(f"Open {self.app_name}", self)
        open_action.triggered.connect(self.open_editor)
        menu.addAction(open_action)

        menu.addSeparator()

        quit_action = QAction("Quit Background App", self)
        quit_action.triggered.connect(self.quit)
        menu.addAction(quit_action)

        self.tray_icon.setContextMenu(menu)
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.tray_icon.show()

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.open_editor()

    def open_editor(self):
        if not os.path.exists(self.main_app_path):
            self.tray_icon.showMessage(
                "Error",
                f"Could not find {os.path.basename(self.main_app_path)} at:\n{self.main_app_path}",
                QSystemTrayIcon.MessageIcon.Critical
            )
            return
        
        command = []
        if self.helper.is_frozen:
            command = [self.main_app_path]
        else: # Running from source
            python_exe = sys.executable
            command = [python_exe, self.main_app_path]

        try:
            subprocess.Popen(command)
        except Exception as e:
            self.tray_icon.showMessage(
                "Launch Error",
                f"Failed to start {self.app_name}:\n{e}",
                QSystemTrayIcon.MessageIcon.Critical
            )


if __name__ == "__main__":
    app = KoromaliTrayApp(sys.argv)
    sys.exit(app.exec())