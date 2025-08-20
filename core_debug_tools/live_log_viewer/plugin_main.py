# Koromali/core_debug_tools/live_log_viewer/plugin_main.py
import subprocess
import sys
import os
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log, LOG_FILE
from utils.helpers import get_base_path

LOG_VIEWER_SCRIPT_PATH = os.path.join(get_base_path(), "utils", "log_viewer.py")

class LiveLogViewerPlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.log_file = LOG_FILE
        self.action = self.api.add_menu_action(
            menu_name="tools", text="Live Log Viewer",
            callback=self.launch_log_viewer,
            shortcut="Ctrl+Shift+L", icon_name="fa5s.bug"
        )
        self.action.setToolTip("Open a real-time viewer for the application log.")
        log.info("Live Log Viewer action added to Tools menu.")

    def launch_log_viewer(self):
        try:
            python_executable = sys.executable
            command = [python_executable, LOG_VIEWER_SCRIPT_PATH, self.log_file]
            log.info(f"Executing command: {' '.join(command)}")
            subprocess.Popen(command)
        except Exception as e:
            self.api.log_error(f"Failed to launch log viewer: {e}")

def initialize(koromali_api: KoromaliPluginAPI):
    return LiveLogViewerPlugin(koromali_api)