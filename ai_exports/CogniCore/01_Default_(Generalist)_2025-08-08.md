---SYSTEM-PROMPT---

You are an expert software developer. Your task is to modify the user's project based on their instructions.
## Golden Rules
- Your response MUST ONLY contain file modifications, creations, or deletions.
- Enclose each file's content in the standard `### File: /path/to/file.ext` format.
- Do not add any extra commentary, explanations, or summaries outside of the code blocks.
- To modify or create a file, provide its complete content in a markdown code block (e.g., ```python ... ```).
- IMPORTANT: If a file's content itself contains '```', use a fenced code block with more backticks (e.g., `````python) for the outer block to prevent parsing errors.
- To delete a file, follow the file path with `---DELETED---` on a new line.
- If a file from the user's prompt is not being changed, do not include it in your response.
- Ensure file paths are relative to the project root and use forward slashes (e.g., `app_core/main.py`).
- Maintain existing code style and conventions for all unchanged parts of modified files.

---USER-PROMPT---

# Project Task...
## Project File Tree:
```
CogniCore
├── assets
│   ├── icons
│   │   └── .gitkeep
│   └── sounds
│       └── .gitkeep
├── cognicore
│   ├── core
│   │   ├── __init__.py
│   │   ├── activity_monitor.py
│   │   ├── api_server.py
│   │   ├── logger.py
│   │   ├── settings.py
│   │   ├── startup.py
│   │   └── system_monitor.py
│   ├── plugin_system
│   │   ├── __init__.py
│   │   ├── interface.py
│   │   └── manager.py
│   ├── plugins
│   │   ├── control_panel
│   │   │   ├── __init__.py
│   │   │   ├── manifest.json
│   │   │   └── widget.py
│   │   ├── daily_reminder
│   │   │   ├── __init__.py
│   │   │   └── manifest.json
│   │   ├── discord_integration
│   │   │   ├── __init__.py
│   │   │   └── manifest.json
│   │   ├── spotify
│   │   │   ├── __init__.py
│   │   │   ├── manifest.json
│   │   │   ├── setup_dialog.py
│   │   │   ├── spotify_client.py
│   │   │   └── widget.py
│   │   ├── system_monitor_widget
│   │   │   ├── __init__.py
│   │   │   ├── manifest.json
│   │   │   └── widget.py
│   │   ├── timer
│   │   │   ├── __init__.py
│   │   │   ├── manifest.json
│   │   │   └── widget.py
│   │   ├── todo
│   │   │   ├── __init__.py
│   │   │   ├── manifest.json
│   │   │   └── widget.py
│   │   └── __init__.py
│   ├── ui
│   │   ├── __init__.py
│   │   ├── base_widget.py
│   │   ├── notification.py
│   │   ├── settings_window.py
│   │   ├── theme.py
│   │   └── window_selector_dialog.py
│   ├── __init__.py
│   ├── app_manager.py
│   └── main.py
├── logs
│   ├── .gitkeep
│   ├── cognicore.log
│   └── crash.log
├── .gitignore
├── README.md
├── requirements.txt
├── run.bat
└── settings.json
```
## Project Files
### File: `/.gitignore`
```text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a PyInstaller script; this is not the
#  case for sane application layouts
*.spec


# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# CogniCore specific
logs/
settings.json
```
### File: `/README.md`
```md
# CogniCore

CogniCore is an overlay and productivity hub designed to enhance focus and act as a central point for system and application integration. It's built for a neurodiverse audience, developers, and anyone looking to minimize distractions while staying informed.

The application provides overlay widgets, background services for tracking, and an API for external data integration.

## Features

-   **Overlay Widgets**: Persistent, always-on-top widgets for various tools. Widgets are now distributed across all available monitors on startup.
-   **Widget Tools**: Right-click any widget to pin it, change its opacity, attach it to a window, or close it.
-   **Spotify Integration**: Display and control your currently playing Spotify song.
-   **Discord Rich Presence**: Automatically updates your Discord status to show if you're gaming, watching media, or working, including an elapsed time counter.
-   **System & Activity Monitoring**: Core services track active applications and system stats (CPU/Memory), making this data available to all plugins.
-   **External API Server**: Run a local server that allows other applications and scripts to send data directly to CogniCore via a simple REST API endpoint.
-   **Settings Menu & Startup Options**: Configure application behavior, including "Start on Startup".
-   **Advanced Logging & Crash Reporting**: Detailed logs for normal operation and crashes are saved to the `logs/` directory.

## Getting Started

Simply double-click the `run.bat` file. It will install the required dependencies and start the application.

## Plugin Configuration

### Setting up Discord Integration

The Discord plugin requires a "Client ID" to function.

1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2.  Click "**New Application**" and give it a name (e.g., "My Activity").
3.  Go to the "**OAuth2**" page for your new application. You will find your **Client ID** here.
4.  Open the `settings.json` file in the CogniCore project directory.
5.  Find the `discord_integration` section and paste your Client ID into the `client_id` field.
6.  Restart CogniCore. Your Discord profile should now show your activity.

### Setting up Spotify Integration

The Spotify plugin requires a Client ID, Client Secret, and a Redirect URI to function.

1.  Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2.  Click "**Create an App**". Give it a name and description.
3.  Once created, you'll see your **Client ID** and you can click to show your **Client Secret**.
4.  Now, click "**Edit Settings**". In the "Redirect URIs" field, add `http://localhost:8888/callback` and click **Save**. This URI is used locally to authenticate.
5.  Open the `settings.json` file in the CogniCore project directory.
6.  Find the `spotify` section inside `plugins` and paste your Client ID and Client Secret.
7.  Restart CogniCore. On the first run, a browser window will open asking you to log into Spotify and authorize the app. After authorization, the widget will start working.

## For Developers: Using the API

CogniCore runs a local Flask server on port `5000`. You can send `POST` requests to the `/api/event` endpoint to push data into the application.

**Example using Python:**
```
### File: `/assets/icons/.gitkeep`
```text
This directory is for icons, e.g. for the system tray.
The app looks for 'icon.png' (24x24 recommended).
```
### File: `/assets/sounds/.gitkeep`
```text
This directory is for user-selectable notification sounds.
Place .wav or .mp3 files here.

A default sound is referenced by the Daily Reminder plugin, but not provided.
You can find royalty-free sounds from many sources online to use here.
```
### File: `/cognicore/__init__.py`
```py

```
### File: `/cognicore/app_manager.py`
```py
import sys
import logging
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QAction, QIcon, QPixmap, QColor

from cognicore.plugin_system.manager import PluginManager
from cognicore.core.activity_monitor import ActivityMonitor
from cognicore.core.system_monitor import SystemMonitor
from cognicore.core.api_server import APIServer
from cognicore.ui.notification import NotificationWidget
from cognicore.ui.settings_window import SettingsWindow
from cognicore.core.settings import SettingsManager

logger = logging.getLogger(__name__)

class AppManager:
    """
    Manages the application lifecycle, core services, and global states like Edit Mode.
    """
    def __init__(self, project_root_path: Path):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

        self.project_root = project_root_path
        self.settings_manager = SettingsManager(self.project_root / "settings.json")
        
        # --- Global State ---
        self.is_edit_mode = False
        
        self.plugins = []
        self.plugin_widgets = []
        self.active_notifications = []
        self.settings_window = None

        # --- Core Services ---
        self.activity_monitor = ActivityMonitor(self.app)
        self.system_monitor = SystemMonitor()
        self.api_server = APIServer()
        self.api_server.start()
        
        # --- Signal Connections ---
        self.activity_monitor.activity_changed.connect(self.on_activity_changed)
        
        self.setup_tray_icon()
        self.load_plugins()
        logger.info("CogniCore application started successfully.")

    def setup_tray_icon(self):
        """Creates and configures the system tray icon and its menu."""
        logger.debug("Setting up system tray icon.")
        self.tray_icon = QSystemTrayIcon()
        
        icon_path = self.project_root / "assets" / "icons" / "icon.png"
        icon = QIcon(str(icon_path)) if icon_path.exists() else self.get_fallback_icon()
        
        self.tray_icon.setIcon(icon)
        self.tray_icon.setToolTip("CogniCore")

        menu = QMenu()
        
        toggle_visibility_action = QAction("Show/Hide All Widgets", self.app)
        toggle_visibility_action.triggered.connect(self.toggle_all_widgets_visibility)
        menu.addAction(toggle_visibility_action)

        self.edit_mode_action = QAction("Enter Edit Mode", self.app)
        self.edit_mode_action.setCheckable(True)
        self.edit_mode_action.triggered.connect(self.toggle_edit_mode)
        menu.addAction(self.edit_mode_action)
        
        menu.addSeparator()

        settings_action = QAction("Settings", self.app)
        settings_action.triggered.connect(self.show_settings_window)
        menu.addAction(settings_action)
        
        menu.addSeparator()
        exit_action = QAction("Exit", self.app)
        exit_action.triggered.connect(self.shutdown)
        menu.addAction(exit_action)

        self.tray_icon.setContextMenu(menu)
        self.tray_icon.show()

    def load_plugins(self):
        """Loads plugins, displays their widgets, and runs setup tasks."""
        logger.info("Starting plugin discovery and loading.")
        plugin_dir = self.project_root / "cognicore" / "plugins"
        plugin_manager = PluginManager(plugin_dir=plugin_dir)
        self.plugins = plugin_manager.load_plugins()
        logger.info(f"Finished plugin loading. {len(self.plugins)} plugins loaded.")

        screens = self.app.screens()
        if not screens:
            screens = [self.app.primaryScreen()]
        
        num_screens = len(screens)
        widget_count = 0

        for plugin in self.plugins:
            logger.debug(f"Setting up plugin: {plugin.__class__.__name__}")
            # Pass the app_manager instance to the plugin
            plugin.setup(self)

            widget = plugin.get_widget()
            if widget:
                self.plugin_widgets.append(widget)
                
                # --- Multi-monitor positioning logic ---
                screen_index = widget_count % num_screens
                target_screen = screens[screen_index]
                screen_geom = target_screen.availableGeometry()
                
                # Position widgets on their assigned screen, offset from top-left
                x_pos = screen_geom.left() + 150 + (widget_count // num_screens) * 250
                y_pos = screen_geom.top() + 150
                widget.move(x_pos, y_pos)

                # Show widgets immediately unless user is already busy
                if not self.activity_monitor.is_user_busy():
                    widget.show()
                widget_count += 1


    def on_activity_changed(self, activity_type: str, window_title: str):
        """Hides or shows widgets based on user activity."""
        is_busy = activity_type != "IDLE"
        logger.info(f"Activity changed. Type: {activity_type}. Busy state: {is_busy}")
        
        # Don't hide widgets if we are in edit mode
        if self.is_edit_mode:
            logger.debug("In Edit Mode, ignoring activity change for visibility.")
            return

        if is_busy:
            for widget in self.plugin_widgets:
                if widget.isVisible():
                    widget.hide()
        else:
            for widget in self.plugin_widgets:
                if not widget.is_programmatically_hidden:
                    widget.show()

    def toggle_edit_mode(self, checked: bool):
        """Toggles widget editing mode for the entire application."""
        self.is_edit_mode = checked
        logger.info(f"Widget Edit Mode {'entered' if self.is_edit_mode else 'exited'}.")
        
        self.edit_mode_action.setText("Exit Edit Mode" if self.is_edit_mode else "Enter Edit Mode")

        # Notify all widgets of the state change
        for widget in self.plugin_widgets:
            widget.set_edit_mode(self.is_edit_mode)
            # Ensure all widgets are visible for editing
            if self.is_edit_mode and not widget.isVisible():
                widget.show()
    
    def toggle_all_widgets_visibility(self):
        """Manually shows or hides all plugin widgets."""
        # In edit mode, this action should be disabled or do nothing
        if self.is_edit_mode:
            self.show_notification("Edit Mode Active", "Exit Edit Mode to hide widgets.")
            return

        are_any_visible = any(w.isVisible() for w in self.plugin_widgets)
        if are_any_visible:
            for widget in self.plugin_widgets:
                widget.hide()
        else:
            if not self.activity_monitor.is_user_busy():
                 for widget in self.plugin_widgets:
                    if not widget.is_programmatically_hidden:
                        widget.show()

    def show_settings_window(self):
        """Creates and shows the settings window."""
        if self.settings_window is None or not self.settings_window.isVisible():
            self.settings_window = SettingsWindow(self.settings_manager)
            self.settings_window.show()
        self.settings_window.activateWindow()

    def show_notification(self, title: str, message: str, sound_name: str | None = None):
        """Displays a temporary notification."""
        if self.activity_monitor.is_user_busy() and not self.is_edit_mode:
            return

        sound_path = self.project_root / "assets" / "sounds" / sound_name if sound_name else None
        notification = NotificationWidget(title, message, sound_path)
        self.active_notifications.append(notification)
        notification.closed.connect(lambda: self.active_notifications.remove(notification))
        
        screen_geometry = self.app.primaryScreen().availableGeometry()
        x = screen_geometry.width() - notification.width() - 20
        y = screen_geometry.height() - notification.height() - 20
        notification.move(x, y)
        notification.show()

    def get_fallback_icon(self) -> QIcon:
        pixmap = QPixmap(24, 24)
        pixmap.fill(QColor("#8A2BE2"))
        return QIcon(pixmap)

    def shutdown(self):
        """Gracefully shuts down all application components."""
        logger.info("Shutdown initiated.")

        logger.debug(f"Shutting down {len(self.plugins)} plugins.")
        for plugin in self.plugins:
            try:
                plugin.shutdown()
            except Exception as e:
                logger.error(f"Error during shutdown of plugin {plugin.__class__.__name__}: {e}", exc_info=True)

        if self.api_server.isRunning():
            self.api_server.stop()
        if self.system_monitor:
            self.system_monitor.stop()
        self.app.quit()

    def run(self) -> int:
        """Starts the application's event loop."""
        self.app.aboutToQuit.connect(self.shutdown)
        return self.app.exec()
```
### File: `/cognicore/core/__init__.py`
```py

```
### File: `/cognicore/core/activity_monitor.py`
```py
import logging
import pygetwindow
from PyQt6.QtCore import QObject, QTimer, pyqtSignal

logger = logging.getLogger(__name__)

class ActivityMonitor(QObject):
    """
    Monitors user activity to determine the type of activity and active window.
    """
    # Emits (activity_type, window_title)
    activity_changed = pyqtSignal(str, str) 

    # Keywords for categorization
    VIDEO_KEYWORDS = ["youtube", "netflix", "twitch", "disney+", "hulu", "plex", "prime video", "vlc"]
    GAME_KEYWORDS = ["steam", "epic games", "gog", "battle.net", "league of legends", "dota 2", "valorant", "cyberpunk", "overwatch"]
    WORK_KEYWORDS = ["visual studio code", "pycharm", "sublime text", "atom", "blender", "photoshop", "word", "excel"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._app = parent
        self._current_activity = "IDLE"
        self._current_title = ""

        self._check_timer = QTimer(self)
        self._check_timer.timeout.connect(self.check_activity_state)
        self._check_timer.start(3000)  # Check every 3 seconds
        self.check_activity_state() # Initial check

    def is_user_busy(self) -> bool:
        """Returns true if the user is not idle."""
        return self._current_activity != "IDLE"

    def check_activity_state(self):
        """
        Determines the current activity type and active window title,
        emitting a signal if they have changed.
        """
        new_activity = "IDLE"
        new_title = ""
        
        try:
            active_window = pygetwindow.getActiveWindow()
            if active_window and active_window.visible and active_window.title:
                new_title = active_window.title
                title_lower = new_title.lower()

                # Check for fullscreen first, often indicates games or videos
                screen_size = self._app.primaryScreen().size()
                is_fullscreen = (
                    active_window.width >= screen_size.width() - 5 and
                    active_window.height >= screen_size.height() - 5
                )

                # Categorize activity
                if any(keyword in title_lower for keyword in self.GAME_KEYWORDS) or is_fullscreen:
                    new_activity = "GAMING"
                elif any(keyword in title_lower for keyword in self.VIDEO_KEYWORDS):
                    new_activity = "WATCHING"
                elif any(keyword in title_lower for keyword in self.WORK_KEYWORDS):
                    new_activity = "WORKING"
                else:
                    new_activity = "WORKING" # Default for any active, non-idle window

            # Update state and emit signal if changed
            if new_activity != self._current_activity or new_title != self._current_title:
                self._current_activity = new_activity
                self._current_title = new_title
                logger.info(f"Activity changed -> Type: {self._current_activity}, Title: {self._current_title}")
                self.activity_changed.emit(self._current_activity, self._current_title)

        except (pygetwindow.PyGetWindowException, Exception) as e:
            if self._current_activity != "IDLE":
                logger.warning(f"Could not check activity state: {e}. Setting to IDLE.")
                self._current_activity = "IDLE"
                self._current_title = ""
                self.activity_changed.emit(self._current_activity, self._current_title)
```
### File: `/cognicore/core/api_server.py`
```py
import logging
from flask import Flask, request, jsonify
from PyQt6.QtCore import QThread, pyqtSignal

logger = logging.getLogger(__name__)

class APIServer(QThread):
    """
    Runs a Flask web server in a separate thread to handle API requests.
    This allows other applications to send data to CogniCore.
    """
    # Signal to emit received data to the main application
    event_received = pyqtSignal(dict)

    def __init__(self, host='127.0.0.1', port=5000):
        super().__init__()
        self.flask_app = Flask(__name__)
        self.host = host
        self.port = port
        self._is_running = False

        # Suppress Flask's default logging to avoid duplicate output
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        @self.flask_app.route('/api/event', methods=['POST'])
        def handle_event():
            if not request.is_json:
                return jsonify({"status": "error", "message": "Request must be JSON"}), 400
            
            data = request.get_json()
            logger.info(f"API event received from source: '{data.get('source', 'Unknown')}'")
            self.event_received.emit(data)
            return jsonify({"status": "success", "message": "Event received"}), 200

    def run(self):
        """The main loop for the thread."""
        self._is_running = True
        logger.info(f"Starting API server on http://{self.host}:{self.port}")
        try:
            self.flask_app.run(host=self.host, port=self.port)
        except Exception as e:
            logger.error(f"Failed to run API server: {e}", exc_info=True)
        finally:
            logger.info("API server has shut down.")

    def stop(self):
        """Stops the thread and the server."""
        if not self._is_running:
            return
        
        logger.info("Stopping API server...")
        self._is_running = False
        # The server doesn't have a built-in stop, so we rely on the thread terminating
        # when the main application exits. This is generally okay for this use case.
        self.terminate() # Forcefully stop the thread
```
### File: `/cognicore/core/logger.py`
```py
import logging
import sys
import traceback
from pathlib import Path
from logging.handlers import RotatingFileHandler

def setup_logging(project_root: Path):
    """
    Configures advanced logging for the application.
    - Logs DEBUG and above to a rotating file.
    - Logs INFO and above to the console.
    """
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "cognicore.log"

    # Define formats
    file_log_format = logging.Formatter(
        '%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s'
    )
    console_log_format = logging.Formatter('%(levelname)s - %(name)s - %(message)s')

    # File handler - rotates logs, keeping up to 5 files of 1MB each
    file_handler = RotatingFileHandler(log_file, maxBytes=1_048_576, backupCount=5, mode='a')
    file_handler.setFormatter(file_log_format)
    file_handler.setLevel(logging.DEBUG) # Log everything to the file

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_log_format)
    console_handler.setLevel(logging.INFO) # Only show important messages on console

    # Get the root logger and add handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG) # Set root logger to lowest level
    
    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

    logging.info("Advanced logging configured.")

def setup_crash_handler(project_root: Path):
    """
    Configures a global exception hook to catch and log all uncaught exceptions.
    Logs crash information to `logs/crash.log`.
    """
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    crash_log_file = log_dir / "crash.log"

    def handle_exception(exc_type, exc_value, exc_traceback):
        """Custom exception handler."""
        # Log to the console if it's the standard hook
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        logging.critical("An uncaught exception occurred!", exc_info=(exc_type, exc_value, exc_traceback))
        
        # Also write to a dedicated crash log
        with open(crash_log_file, 'a') as f:
            f.write("="*80 + "\n")
            f.write(f"CRASH REPORT - {logging.Formatter().formatTime(logging.makeLogRecord({}))}\n")
            f.write("="*80 + "\n")
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
            f.write("\n")

    sys.excepthook = handle_exception
    logging.info("Crash handler configured.")
```
### File: `/cognicore/core/settings.py`
```py
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

class SettingsManager:
    """Handles loading, saving, and accessing application settings from a JSON file."""

    def __init__(self, settings_path: Path):
        self.settings_path = settings_path
        self.settings = self._load_settings()

    def _get_default_settings(self) -> dict:
        """Returns the default settings structure for the application."""
        return {
            "general": {
                "start_on_startup": False
            },
            "plugins": {
                "daily_reminder": {
                    "enabled": True,
                    "hour": 9,
                    "minute": 30,
                    "title": "Daily Reminder",
                    "message": "Time for a quick break! Stretch and rest your eyes.",
                    "sound": "default_notification.wav"
                },
                "discord_integration": {
                    "enabled": True,
                    "client_id": "YOUR_DISCORD_CLIENT_ID_HERE"
                },
                "spotify": {
                    "enabled": True,
                    "client_id": "YOUR_SPOTIFY_CLIENT_ID_HERE",
                    "client_secret": "YOUR_SPOTIFY_CLIENT_SECRET_HERE",
                    "redirect_uri": "http://localhost:8888/callback"
                }
            }
        }

    def _load_settings(self) -> dict:
        """Loads settings from the JSON file, or creates it with defaults."""
        defaults = self._get_default_settings()
        if not self.settings_path.exists():
            logger.info(f"Settings file not found at '{self.settings_path}'. Creating with defaults.")
            self.settings = defaults
            self.save()
            return self.settings
        
        try:
            with open(self.settings_path, 'r') as f:
                loaded_settings = json.load(f)
                
                self.settings = self._merge_defaults(defaults, loaded_settings)
                self.save() # Save back to add any new default keys to the file

                logger.info(f"Settings loaded successfully from '{self.settings_path}'.")
                return self.settings
        except (json.JSONDecodeError, Exception) as e:
            logger.error(f"Failed to load settings from '{self.settings_path}': {e}. Using default settings.", exc_info=True)
            return defaults

    def _merge_defaults(self, default: dict, loaded: dict) -> dict:
        """Recursively merge loaded settings into defaults to ensure all keys exist."""
        for key, value in default.items():
            if key not in loaded:
                loaded[key] = value
            elif isinstance(value, dict) and isinstance(loaded.get(key), dict):
                loaded[key] = self._merge_defaults(value, loaded[key])
        return loaded

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves a setting value. Use dot notation for nested keys.
        Example: `get("plugins.discord_integration.client_id")`
        """
        keys = key.split('.')
        value = self.settings
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def set(self, key: str, value: Any):
        """
        Sets a setting value. Use dot notation for nested keys.
        This automatically saves the settings to the file.
        """
        logger.debug(f"Setting '{key}' to '{value}'.")
        keys = key.split('.')
        d = self.settings
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value
        self.save()

    def save(self):
        """Saves the current settings to the JSON file."""
        try:
            with open(self.settings_path, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save settings: {e}", exc_info=True)
```
### File: `/cognicore/core/startup.py`
```py
import sys
import os
import logging

logger = logging.getLogger(__name__)

APP_NAME = "CogniCore"

def _get_run_script_path() -> str | None:
    """Gets the absolute path to the run.bat script in the project root."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    run_script = os.path.join(project_root, 'run.bat')
    
    if not os.path.exists(run_script):
        logger.error(f"Startup script 'run.bat' not found at expected path: {run_script}")
        return None
    
    # Enclose in quotes to handle spaces in path
    quoted_path = f'"{run_script}"'
    logger.debug(f"Found run script for startup: {quoted_path}")
    return quoted_path

def set_startup(enable: bool):
    """
    Enables or disables the application from starting when the user logs in.
    Currently only implemented for Windows.
    """
    if sys.platform != 'win32':
        logger.warning("Start on startup is only implemented for Windows.")
        return

    import winreg
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        logger.debug(f"Accessing registry key: HKEY_CURRENT_USER\\{key_path}")
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            if enable:
                script_path = _get_run_script_path()
                if script_path:
                    winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, script_path)
                    logger.info(f"Enabled start on startup. Registry value '{APP_NAME}' set.")
            else:
                try:
                    winreg.DeleteValue(key, APP_NAME)
                    logger.info(f"Disabled start on startup. Registry value '{APP_NAME}' deleted.")
                except FileNotFoundError:
                    logger.debug(f"Startup registry key '{APP_NAME}' not found, nothing to disable.")

    except Exception as e:
        logger.error(f"Failed to modify startup registry: {e}", exc_info=True)
        raise # Re-raise to notify the caller of the failure

def is_startup_enabled() -> bool:
    """
    Checks if the application is configured to start on user login.
    Currently only implemented for Windows.
    """
    if sys.platform != 'win32':
        return False

    import winreg
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        logger.debug(f"Checking registry key: HKEY_CURRENT_USER\\{key_path}\\{APP_NAME}")
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
            winreg.QueryValueEx(key, APP_NAME)
        logger.debug("Startup registry key found.")
        return True
    except FileNotFoundError:
        logger.debug("Startup registry key not found.")
        return False
    except Exception as e:
        logger.error(f"Failed to read startup registry: {e}", exc_info=True)
        return False
```
### File: `/cognicore/core/system_monitor.py`
```py
import logging
import psutil
from PyQt6.QtCore import QObject, QTimer

logger = logging.getLogger(__name__)

class SystemMonitor(QObject):
    """
    A core service that periodically polls for system metrics like CPU and
    memory usage. Data is accessible for any plugin to use.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cpu_percent = 0.0
        self.memory_percent = 0.0
        
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.poll_metrics)
        self._timer.start(5000)  # Poll every 5 seconds
        self.poll_metrics() # Initial poll

    def poll_metrics(self):
        """Updates the system metrics."""
        try:
            self.cpu_percent = psutil.cpu_percent()
            self.memory_percent = psutil.virtual_memory().percent
            logger.debug(f"System Metrics Polled - CPU: {self.cpu_percent}%, Memory: {self.memory_percent}%")
        except Exception as e:
            logger.error(f"Failed to poll system metrics: {e}")
            self.cpu_percent = -1
            self.memory_percent = -1

    def get_cpu_usage(self) -> float:
        """Returns the last polled CPU usage percentage."""
        return self.cpu_percent

    def get_memory_usage(self) -> float:
        """Returns the last polled virtual memory usage percentage."""
        return self.memory_percent

    def stop(self):
        """Stops the polling timer."""
        logger.info("Stopping System Monitor.")
        self._timer.stop()
```
### File: `/cognicore/main.py`
```py
import sys
import os
import traceback
from pathlib import Path

# --- Failsafe Configuration ---
# This section must have NO imports from the project itself.
# It's a last resort for catching errors during the earliest startup phase.
try:
    project_root = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    log_dir = project_root / "logs"
    crash_log_path = log_dir / "crash.log"
except Exception:
    # If even path calculation fails, we can't do much.
    # This is highly unlikely.
    project_root = None


def main():
    """The main entry point for the CogniCore application."""
    try:
        # --- Normal Startup Sequence ---

        # 1. Ensure log directory exists. This is critical for both failsafe and normal logging.
        if project_root:
            log_dir.mkdir(exist_ok=True)
        
        # 2. Add project to path FIRST to make all subsequent imports work reliably.
        if project_root and str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))

        # 3. Setup logging and the primary crash handler. This is the next most likely failure point.
        from cognicore.core.logger import setup_logging, setup_crash_handler
        setup_logging(project_root)
        setup_crash_handler(project_root)

        # 4. Now that logging is configured, we can safely import the rest of the app.
        import logging
        logger = logging.getLogger(__name__)

        from cognicore.app_manager import AppManager
        
        logger.info("--- Initializing CogniCore ---")
        manager = AppManager(project_root_path=project_root)
        return manager.run()

    except Exception:
        # --- Failsafe Crash Handling ---
        # This block executes if ANY part of the startup process inside main() fails.
        # It uses no project modules, only built-ins and standard libraries.
        print(f"A critical error occurred during startup.", file=sys.stderr)
        
        if project_root:
            print(f"A crash report has been saved to:\n{crash_log_path}", file=sys.stderr)
            with open(crash_log_path, 'a') as f:
                f.write("="*80 + "\n")
                # Use a standard library for timestamping to avoid dependencies
                f.write(f"FAILSAFE CRASH REPORT - {__import__('datetime').datetime.now().isoformat()}\n")
                f.write("="*80 + "\n")
                f.write("A critical error occurred during application startup, before the main crash handler was ready.\n")
                f.write("This usually indicates a problem with a core module import or a configuration error.\n\n")
                traceback.print_exc(file=f)
                f.write("\n")
        else:
            print("Could not determine project path. Cannot write crash log.", file=sys.stderr)

        traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == "__main__":
    # This final check ensures that if main() itself has a syntax error,
    # it doesn't just disappear.
    try:
        sys.exit(main())
    except Exception:
        print("A fatal error occurred executing the main function.", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
```
### File: `/cognicore/plugin_system/__init__.py`
```py

```
### File: `/cognicore/plugin_system/interface.py`
```py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QWidget
    from cognicore.app_manager import AppManager


class CogniCorePlugin(ABC):
    """
    The abstract base class for all CogniCore plugins.
    
    Plugins must implement the methods defined in this interface
    to be successfully loaded and integrated into the overlay.
    """

    @abstractmethod
    def get_widget(self) -> QWidget | None:
        """
        This method should return the main Qt widget for the plugin.
        This widget will be displayed on the CogniCore overlay.
        Return None if the plugin has no UI (e.g., a background service).

        Returns:
            QWidget or None: The plugin's main widget, or None if it has no UI.
        """
        pass

    def setup(self, app_manager: AppManager) -> None:
        """
        An optional setup method called once after the plugin is loaded.
        Use this for background tasks, connecting to app-wide signals, etc.
        
        Args:
            app_manager: The central application manager instance.
        """
        pass

    def shutdown(self) -> None:
        """
        An optional shutdown method called when the application is closing.
        Use this to clean up resources like threads or network connections.
        """
        pass
```
### File: `/cognicore/plugin_system/manager.py`
```py
import json
import logging
import importlib
from pathlib import Path
from cognicore.plugin_system.interface import CogniCorePlugin

logger = logging.getLogger(__name__)

class PluginManager:
    """
    Discovers, loads, and manages all CogniCore plugins.
    """
    def __init__(self, plugin_dir: Path):
        self.plugin_dir = plugin_dir
        if not self.plugin_dir.is_dir():
            logger.error(f"Plugin directory not found: {self.plugin_dir}")
            raise FileNotFoundError(f"Plugin directory not found: {self.plugin_dir}")


    def load_plugins(self) -> list[CogniCorePlugin]:
        """
        Scans the plugin directory, validates, and loads all valid plugins.

        Returns:
            A list of instantiated plugin objects.
        """
        loaded_plugins = []
        for item in self.plugin_dir.iterdir():
            if item.is_dir() and (item / "manifest.json").exists():
                try:
                    with open(item / "manifest.json", 'r') as f:
                        manifest = json.load(f)
                    
                    plugin_instance = self._load_plugin_from_manifest(manifest)
                    if plugin_instance:
                        loaded_plugins.append(plugin_instance)
                        logger.info(f"Successfully loaded plugin: {manifest.get('name')}")
                except Exception as e:
                    logger.error(f"Failed to load plugin from {item.name}: {e}", exc_info=True)
        return loaded_plugins

    def _load_plugin_from_manifest(self, manifest: dict) -> CogniCorePlugin | None:
        """
        Loads a single plugin using its manifest data.
        """
        entry_point_str = manifest.get("entry_point")
        if not entry_point_str:
            raise ValueError("Manifest missing 'entry_point'")

        module_name, class_name = entry_point_str.rsplit(':', 1)
        
        module = importlib.import_module(module_name)
        plugin_class = getattr(module, class_name)
        
        if issubclass(plugin_class, CogniCorePlugin):
            return plugin_class()
        
        return None
```
### File: `/cognicore/plugins/__init__.py`
```py

```
### File: `/cognicore/plugins/control_panel/__init__.py`
```py
from __future__ import annotations
from typing import TYPE_CHECKING
from cognicore.plugin_system.interface import CogniCorePlugin

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QWidget
    from cognicore.app_manager import AppManager
    from .widget import ControlPanelWidget

class ControlPanelPlugin(CogniCorePlugin):
    """
    A plugin that provides a main control panel for global application actions.
    """
    def __init__(self):
        super().__init__()
        self._widget: ControlPanelWidget | None = None
        self.app_manager: AppManager | None = None

    def get_widget(self) -> QWidget | None:
        """Returns the ControlPanelWidget instance."""
        if self._widget is None:
            from .widget import ControlPanelWidget # Defer import
            self._widget = ControlPanelWidget(self.app_manager)
        return self._widget

    def setup(self, app_manager: AppManager):
        """
        Stores a reference to the AppManager to be passed to the widget.
        """
        self.app_manager = app_manager
```
### File: `/cognicore/plugins/control_panel/manifest.json`
```json
{
  "name": "Control Panel",
  "version": "1.0.0",
  "author": "CogniCore Team",
  "description": "A central widget with buttons for controlling global app states like Edit Mode.",
  "entry_point": "cognicore.plugins.control_panel:ControlPanelPlugin"
}
```
### File: `/cognicore/plugins/control_panel/widget.py`
```py
from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QHBoxLayout, QPushButton
from cognicore.ui.base_widget import BasePluginWidget
from cognicore.ui.theme import Theme

if TYPE_CHECKING:
    from cognicore.app_manager import AppManager

logger = logging.getLogger(__name__)

class ControlPanelWidget(BasePluginWidget):
    """
    A widget containing global action buttons for the application.
    """
    def __init__(self, app_manager: AppManager | None, parent=None):
        super().__init__(parent)
        if not app_manager:
            raise ValueError("AppManager instance is required for ControlPanelWidget.")
        
        self.app_manager = app_manager
        self.app_manager.edit_mode_action.toggled.connect(self.update_button_text)

        self.setWindowTitle("CogniCore Controls")
        
        self.content_layout.setContentsMargins(10, 10, 10, 10)

        # Edit Mode Button
        self.edit_mode_button = QPushButton("Enter Edit Mode")
        self.edit_mode_button.setCheckable(True)
        self.edit_mode_button.setStyleSheet(Theme.get_button_stylesheet())
        self.edit_mode_button.clicked.connect(self.on_edit_mode_clicked)
        
        self.content_layout.addWidget(self.edit_mode_button)
        self.adjustSize()

    def on_edit_mode_clicked(self, checked: bool):
        """Toggles the global edit mode by triggering the tray menu's action."""
        logger.debug(f"Control panel button clicked. Setting edit mode to: {checked}")
        # We trigger the action from the tray menu to keep the state logic centralized.
        self.app_manager.edit_mode_action.setChecked(checked)
        self.app_manager.edit_mode_action.trigger()

    def update_button_text(self, checked: bool):
        """Updates the button text when the state changes from another source (like the tray)."""
        self.edit_mode_button.setChecked(checked)
        self.edit_mode_button.setText("Exit Edit Mode" if checked else "Enter Edit Mode")
```
### File: `/cognicore/plugins/daily_reminder/__init__.py`
```py
from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from PyQt6.QtCore import QTimer, QTime, QDateTime

from cognicore.plugin_system.interface import CogniCorePlugin

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QWidget
    from cognicore.app_manager import AppManager

logger = logging.getLogger(__name__)

class DailyReminderPlugin(CogniCorePlugin):
    """
    A background plugin that shows a single daily notification based on settings.
    """
    def __init__(self):
        super().__init__()
        self.app_manager: AppManager | None = None
        self.last_shown_date: QDateTime.date | None = None
        self.config = {}

    def get_widget(self) -> QWidget | None:
        """This plugin runs in the background and has no widget."""
        return None

    def setup(self, app_manager: AppManager):
        """Initializes the timer to check for the reminder time."""
        self.app_manager = app_manager
        self.config = self.app_manager.settings_manager.get("plugins.daily_reminder")

        if not self.config or not self.config.get("enabled"):
            logger.info("Daily Reminder plugin is disabled in settings.")
            return

        self.schedule_timer = QTimer()
        self.schedule_timer.timeout.connect(self._check_and_trigger_reminder)
        self.schedule_timer.start(60 * 1000)
        
        hour = self.config.get('hour', 9)
        minute = self.config.get('minute', 30)
        logger.info(f"Daily Reminder scheduled for {hour:02d}:{minute:02d}.")

    def _check_and_trigger_reminder(self):
        """Checks the time and shows the notification if conditions are met."""
        if not self.app_manager:
            return

        now = QDateTime.currentDateTime()
        today = now.date()
        
        reminder_time = QTime(self.config.get('hour', 9), self.config.get('minute', 30))

        time_match = now.time().hour() == reminder_time.hour() and \
                     now.time().minute() == reminder_time.minute()
        
        if time_match and today != self.last_shown_date:
            logger.info(f"Triggering Daily Reminder notification.")
            self.app_manager.show_notification(
                title=self.config.get('title', 'Reminder'),
                message=self.config.get('message', 'Check your tasks!'),
                sound_name=self.config.get('sound')
            )
            self.last_shown_date = today
```
### File: `/cognicore/plugins/daily_reminder/manifest.json`
```json
{
  "name": "Daily Reminder",
  "version": "0.1.0",
  "author": "CogniCore Team",
  "description": "A background plugin to show a notification at a specific time each day.",
  "entry_point": "cognicore.plugins.daily_reminder:DailyReminderPlugin"
}
```
### File: `/cognicore/plugins/discord_integration/__init__.py`
```py
from __future__ import annotations
import logging
import time
from typing import TYPE_CHECKING

from cognicore.plugin_system.interface import CogniCorePlugin

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QWidget
    from cognicore.app_manager import AppManager

logger = logging.getLogger(__name__)

# Attempt to import pypresence, handle if not installed
try:
    from pypresence import Presence, exceptions
except ImportError:
    Presence = None
    exceptions = None
    logger.warning("Discord Integration: 'pypresence' library not found. Plugin will be disabled.")
    logger.warning("Install it with: pip install pypresence")


class DiscordIntegrationPlugin(CogniCorePlugin):
    """
    Integrates with Discord to show the user's current activity
    via Rich Presence (RPC).
    """
    def __init__(self):
        super().__init__()
        self.app_manager: AppManager | None = None
        self.rpc: Presence | None = None
        self.config: dict = {}
        self.current_activity_start_time: float | None = None

    def get_widget(self) -> QWidget | None:
        """This plugin is a background service and has no widget."""
        return None

    def setup(self, app_manager: AppManager):
        """Initializes the RPC connection and subscribes to activity events."""
        if not Presence or not exceptions:
            return # Don't run if pypresence is not installed

        self.app_manager = app_manager
        self.config = self.app_manager.settings_manager.get("plugins.discord_integration", {})

        if not self.config.get("enabled"):
            logger.info("Discord Integration plugin is disabled in settings.")
            return

        client_id = self.config.get("client_id")
        if not client_id or client_id == "YOUR_DISCORD_CLIENT_ID_HERE":
            logger.error("Discord Integration: Client ID is not set in settings.json. Plugin will not run.")
            return

        try:
            self.rpc = Presence(client_id)
            self.rpc.connect()
            logger.info("Successfully connected to Discord RPC.")
            
            # Connect to the activity monitor signal
            self.app_manager.activity_monitor.activity_changed.connect(self.on_activity_changed)
            
            # Set initial status
            self.on_activity_changed(
                self.app_manager.activity_monitor._current_activity,
                self.app_manager.activity_monitor._current_title
            )

        except exceptions.DiscordNotFound:
            logger.error("Discord Integration: Could not find a running Discord client.")
        except Exception as e:
            logger.error(f"Discord Integration: Failed to connect to RPC: {e}", exc_info=True)
            self.rpc = None

    def on_activity_changed(self, activity_type: str, window_title: str):
        """Callback function when the user's activity changes."""
        if not self.rpc:
            return
        
        logger.debug(f"Updating Discord presence. Activity: {activity_type}, Window: {window_title}")
        self.current_activity_start_time = time.time()
        
        try:
            if activity_type == "IDLE":
                self.rpc.clear()
            else:
                # Format the details and state strings
                state = f"In: {self.format_title(window_title)}"
                details = f"{activity_type.capitalize()}"
                
                # Update presence
                self.rpc.update(
                    state=state,
                    details=details,
                    start=int(self.current_activity_start_time),
                    large_image="cognicore_logo", # Asset key in Discord Dev Portal
                    large_text="CogniCore"
                )
        except Exception as e:
            logger.error(f"Discord Integration: Failed to update presence: {e}")

    def format_title(self, title: str, max_length: int = 40) -> str:
        """Truncates and cleans up the window title for display."""
        if len(title) > max_length:
            return title[:max_length-3] + "..."
        return title

    def shutdown(self):
        """Clears presence and closes the RPC connection."""
        if self.rpc:
            logger.info("Shutting down Discord RPC connection.")
            try:
                self.rpc.clear()
                self.rpc.close()
            except Exception as e:
                logger.error(f"Error during Discord RPC shutdown: {e}")
```
### File: `/cognicore/plugins/discord_integration/manifest.json`
```json
{
  "name": "Discord Integration",
  "version": "1.0.0",
  "author": "CogniCore Team",
  "description": "Shows your current activity (gaming, working, watching) as your Discord status using Rich Presence.",
  "entry_point": "cognicore.plugins.discord_integration:DiscordIntegrationPlugin"
}
```
### File: `/cognicore/plugins/spotify/__init__.py`
```py
from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from PyQt6.QtCore import QThread, QObject, pyqtSignal

from cognicore.plugin_system.interface import CogniCorePlugin

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QWidget
    from cognicore.app_manager import AppManager
    from .widget import SpotifyWidget
    from .spotify_client import SpotifyClient

logger = logging.getLogger(__name__)

# Helper for running spotify auth in a thread
class SpotifyAuthWorker(QObject):
    finished = pyqtSignal()
    
    def __init__(self, client: SpotifyClient):
        super().__init__()
        self.client = client
    
    def run(self):
        self.client.initialize()
        self.finished.emit()

class SpotifyPlugin(CogniCorePlugin):
    """
    A plugin to control and display music from Spotify.
    """
    def __init__(self):
        super().__init__()
        self._widget: SpotifyWidget | None = None
        self.app_manager: AppManager | None = None
        self.client: SpotifyClient | None = None
        self.config: dict | None = None
        self.auth_thread: QThread | None = None
        self.auth_worker: SpotifyAuthWorker | None = None

    def get_widget(self) -> QWidget | None:
        """Returns the SpotifyWidget instance."""
        if not self.config or not self.config.get("enabled", False):
            return None
            
        if self._widget is None:
            if self.app_manager and not self.client:
                 self._initialize_client()
            
            if self.client:
                from .widget import SpotifyWidget # Defer import
                self._widget = SpotifyWidget(self.app_manager, self.client, self) # Pass self (plugin) to widget
            else:
                logger.error("Spotify client not available for widget creation.")
                
        return self._widget

    def setup(self, app_manager: AppManager):
        """
        Initializes the Spotify client and starts the authentication
        process in a separate thread to avoid blocking the UI.
        """
        self.app_manager = app_manager
        self.config = self.app_manager.settings_manager.get("plugins.spotify", {})

        if not self.config.get("enabled", False):
            logger.info("Spotify plugin is disabled in settings.")
            return
        
        self.attempt_authentication()


    def attempt_authentication(self):
        """Initializes client and starts the authentication thread."""
        # Ensure config is fresh
        if self.app_manager:
            self.config = self.app_manager.settings_manager.get("plugins.spotify", {})

        # Stop any previous auth thread
        if self.auth_thread and self.auth_thread.isRunning():
            self.auth_thread.quit()
            self.auth_thread.wait()

        # Check if credentials are valid enough to even try
        if (not self.config.get("client_id") or "YOUR_SPOTIFY_CLIENT_ID" in self.config.get("client_id")
            or not self.config.get("client_secret") or "YOUR_SPOTIFY_CLIENT_SECRET" in self.config.get("client_secret")):
            logger.warning("Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.")
            if self.client:
                # Manually set an error state so the widget can react
                self.client.last_auth_error = "Credentials not configured."
                self.client.auth_error.emit(self.client.last_auth_error)
            return

        if not self.client:
            self._initialize_client()
        else: # Re-initialize client with potentially new config
            self._initialize_client()

        if self.client:
            self.auth_thread = QThread()
            self.auth_worker = SpotifyAuthWorker(self.client)
            self.auth_worker.moveToThread(self.auth_thread)
            
            self.auth_thread.started.connect(self.auth_worker.run)
            self.auth_worker.finished.connect(self.auth_thread.quit)
            
            self.auth_thread.finished.connect(self.auth_thread.deleteLater)
            self.auth_worker.finished.connect(self.auth_worker.deleteLater)
            
            logger.info("Starting Spotify authentication thread.")
            self.auth_thread.start()


    def _initialize_client(self):
        """Instantiates the SpotifyClient."""
        if not self.app_manager or self.config is None:
            return
            
        try:
            from .spotify_client import SpotifyClient
            self.client = SpotifyClient(self.config)
            # Connect signals from the new client to the widget if it exists
            if self._widget:
                self.client.auth_success.connect(self._widget.on_auth_success)
                self.client.auth_error.connect(self._widget.on_auth_error)

        except ImportError:
            logger.error("Could not import 'spotipy' library. Spotify plugin will be disabled. Please install it via 'pip install spotipy'")
            self.client = None
            if self.config:
                self.config["enabled"] = False


    def shutdown(self):
        """Stops the authentication thread if it is running."""
        if self.auth_thread and self.auth_thread.isRunning():
            logger.info("Stopping Spotify auth thread.")
            self.auth_thread.quit()
            self.auth_thread.wait()
```
### File: `/cognicore/plugins/spotify/manifest.json`
```json
{
  "name": "Spotify Controller",
  "version": "1.0.0",
  "author": "CogniCore Team",
  "description": "Displays the currently playing song on Spotify and provides playback controls.",
  "entry_point": "cognicore.plugins.spotify:SpotifyPlugin"
}
```
### File: `/cognicore/plugins/spotify/setup_dialog.py`
```py
import logging
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
    QPushButton, QHBoxLayout, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt
from cognicore.ui.theme import Theme

# Assuming AppManager is accessible or its relevant parts like settings_manager are passed
# For now, let's assume settings_manager is passed directly.
# from cognicore.app_manager import AppManager
from cognicore.core.settings import SettingsManager

logger = logging.getLogger(__name__)

class SpotifySetupDialog(QDialog):
    """A dialog to guide users through setting up Spotify API credentials."""

    def __init__(self, settings_manager: SettingsManager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager

        self.setWindowTitle("Spotify Setup")
        self.setModal(True)
        self.setMinimumWidth(500)
        self.setStyleSheet(f"""
            QDialog {{ background-color: {Theme.BACKGROUND}; }}
            QWidget {{
                color: {Theme.FOREGROUND};
                font-family: {Theme.FONT_FAMILY};
                font-size: {Theme.FONT_SIZE_NORMAL};
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Instructions
        info_label = QLabel(
            'To use the Spotify widget, you need a Client ID and Secret from Spotify\'s Developer Dashboard.'
        )
        info_label.setWordWrap(True)
        layout.addWidget(info_label)

        link_label = QLabel(
            '<a href="https://developer.spotify.com/dashboard/" style="color: #8A2BE2;">'
            '1. Go to Spotify Developer Dashboard and create an app.'
            '</a>'
        )
        link_label.setOpenExternalLinks(True)
        layout.addWidget(link_label)
        
        redirect_uri_label = QLabel(
            '2. In the app settings, add this Redirect URI: <b>http://localhost:8888/callback</b>'
        )
        redirect_uri_label.setTextFormat(Qt.TextFormat.RichText)
        layout.addWidget(redirect_uri_label)

        step3_label = QLabel('3. Copy the Client ID and Client Secret into the fields below.')
        layout.addWidget(step3_label)

        # Form for credentials
        form_layout = QFormLayout()
        form_layout.setContentsMargins(0, 10, 0, 10)
        self.client_id_input = QLineEdit()
        self.client_secret_input = QLineEdit()
        self.client_secret_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        input_style = f"""
            QLineEdit {{
                background-color: {Theme.SECONDARY};
                border: 1px solid {Theme.BORDER};
                border-radius: 5px;
                padding: 8px;
            }}
        """
        self.client_id_input.setStyleSheet(input_style)
        self.client_secret_input.setStyleSheet(input_style)

        # Pre-fill with existing values if they exist
        self.client_id_input.setText(self.settings_manager.get("plugins.spotify.client_id", ""))
        self.client_secret_input.setText(self.settings_manager.get("plugins.spotify.client_secret", ""))

        form_layout.addRow("Client ID:", self.client_id_input)
        form_layout.addRow("Client Secret:", self.client_secret_input)
        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save & Authenticate")
        save_button.clicked.connect(self.save_and_accept)
        save_button.setStyleSheet(Theme.get_button_stylesheet())
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        layout.addLayout(button_layout)

    def save_and_accept(self):
        """Validates input, saves settings, and closes the dialog."""
        client_id = self.client_id_input.text().strip()
        client_secret = self.client_secret_input.text().strip()

        if not client_id or not client_secret or "YOUR_" in client_id or "YOUR_" in client_secret:
            QMessageBox.warning(self, "Missing Information", "Please provide a valid Client ID and Client Secret.")
            return

        self.settings_manager.set("plugins.spotify.client_id", client_id)
        self.settings_manager.set("plugins.spotify.client_secret", client_secret)
        
        logger.info("New Spotify credentials saved from setup dialog.")
        self.accept()
```
### File: `/cognicore/plugins/spotify/spotify_client.py`
```py
import logging
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError
from PyQt6.QtCore import QObject, pyqtSignal, QTimer

logger = logging.getLogger(__name__)

class SpotifyClient(QObject):
    """Handles authentication and communication with the Spotify API."""
    
    auth_success = pyqtSignal()
    auth_error = pyqtSignal(str)

    def __init__(self, config: dict, parent=None):
        super().__init__(parent)
        self.config = config
        self.sp = None
        self.last_auth_error: str | None = None

    def initialize(self):
        """
        Sets up the Spotipy client with credentials and attempts to authenticate.
        This may involve opening a browser for user login.
        """
        self.last_auth_error = None # Reset error state on new attempt
        try:
            # Validate config before attempting to connect
            if ("YOUR_SPOTIFY_CLIENT_ID" in self.config.get("client_id", "") or
                "YOUR_SPOTIFY_CLIENT_SECRET" in self.config.get("client_secret", "")):
                raise SpotifyOauthError("Client ID or Secret not configured in settings.json.")

            scope = "user-read-playback-state,user-modify-playback-state,user-read-currently-playing"
            cache_path = ".spotify_cache"

            auth_manager = SpotifyOAuth(
                client_id=self.config.get("client_id"),
                client_secret=self.config.get("client_secret"),
                redirect_uri=self.config.get("redirect_uri"),
                scope=scope,
                cache_path=cache_path,
                open_browser=webbrowser.open # Use the default browser
            )
            self.sp = spotipy.Spotify(auth_manager=auth_manager)
            
            # This call will trigger auth flow if token is not cached or is expired
            self.sp.current_playback() 
            
            logger.info("Spotify client initialized and authenticated successfully.")
            self.auth_success.emit()
            return True
            
        except SpotifyOauthError as e:
            logger.error(f"Spotify authentication failed: {e}", exc_info=False) # No need for full traceback for config errors
            error_msg = f"Auth Error: {e}. Check settings.json."
            self.last_auth_error = error_msg
            self.auth_error.emit(error_msg)
            return False
        except Exception as e:
            logger.error(f"An unexpected error occurred during Spotify client initialization: {e}", exc_info=True)
            if "client_id" in str(e).lower():
                error_msg = "Spotify Auth Error. Check your Client ID in settings."
            else:
                 error_msg = f"Connection to Spotify failed."
            self.last_auth_error = error_msg
            self.auth_error.emit(error_msg)
            return False

    def get_current_track(self):
        """Retrieves the currently playing track from Spotify."""
        if not self.sp: return None
        try:
            track = self.sp.current_playback()
            return track
        except spotipy.exceptions.SpotifyException as e:
            # Typically happens if auth token expires. Spotipy should handle refresh, but good to log.
            logger.warning(f"Spotify API call failed, may need to re-authenticate: {e}")
            return None
        except Exception as e:
            logger.error(f"Failed to get current Spotify track: {e}")
            return None

    def play_pause(self):
        """Toggles play/pause on the current Spotify device."""
        if not self.sp: return
        QTimer.singleShot(0, self._play_pause_worker)

    def _play_pause_worker(self):
        try:
            playback = self.sp.current_playback()
            if playback and playback.get('is_playing'):
                logger.info("Pausing Spotify playback.")
                self.sp.pause_playback()
            else:
                logger.info("Starting/Resuming Spotify playback.")
                self.sp.start_playback()
        except Exception as e:
            logger.error(f"Spotify play/pause command failed: {e}")

    def next_track(self):
        """Skips to the next track."""
        if not self.sp: return
        logger.info("Skipping to next Spotify track.")
        QTimer.singleShot(0, lambda: self._try_sp_command(self.sp.next_track))

    def prev_track(self):
        """Goes to the previous track."""
        if not self.sp: return
        logger.info("Skipping to previous Spotify track.")
        QTimer.singleShot(0, lambda: self._try_sp_command(self.sp.previous_track))
    
    def _try_sp_command(self, command):
        """Wrapper to safely call a spotipy command."""
        try:
            command()
        except Exception as e:
            logger.error(f"Spotify command failed: {e}")
```
### File: `/cognicore/plugins/spotify/widget.py`
```py
from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, Qt, QDialog
from cognicore.ui.base_widget import BasePluginWidget

if TYPE_CHECKING:
    from cognicore.app_manager import AppManager
    from .spotify_client import SpotifyClient
    from . import SpotifyPlugin

logger = logging.getLogger(__name__)

class SpotifyWidget(BasePluginWidget):
    """A widget for displaying and controlling Spotify playback."""

    def __init__(self, app_manager: AppManager | None, spotify_client: SpotifyClient, plugin: SpotifyPlugin, parent=None):
        super().__init__(parent)
        self.app_manager = app_manager
        self.client = spotify_client
        self.plugin = plugin
        
        self.setWindowTitle("Spotify")
        self.setMinimumWidth(320)

        self.content_layout.setContentsMargins(15, 15, 15, 15)
        self.content_layout.setSpacing(8)

        # --- Player UI ---
        self.player_widget = QWidget()
        player_layout = QVBoxLayout(self.player_widget)
        player_layout.setContentsMargins(0,0,0,0)
        player_layout.setSpacing(8)

        self.song_label = QLabel("Connecting...")
        self.song_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_label.setStyleSheet("background: transparent; font-weight: bold; font-size: 14px;")
        self.song_label.setWordWrap(True)

        self.artist_label = QLabel("Waiting for Spotify...")
        self.artist_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.artist_label.setStyleSheet("background: transparent; font-size: 12px; color: #aaa;")
        
        player_layout.addWidget(self.song_label)
        player_layout.addWidget(self.artist_label)
        
        controls_layout = QHBoxLayout()
        self.prev_button = QPushButton("⏮")
        self.play_pause_button = QPushButton("▶")
        self.next_button = QPushButton("⏭")

        button_style = "QPushButton { background-color: transparent; border: none; font-size: 22px; color: #ddd; } QPushButton:hover { color: #fff; }"
        self.prev_button.setStyleSheet(button_style)
        self.play_pause_button.setStyleSheet(button_style)
        self.next_button.setStyleSheet(button_style)
        
        self.prev_button.clicked.connect(self.client.prev_track)
        self.play_pause_button.clicked.connect(self.client.play_pause)
        self.next_button.clicked.connect(self.client.next_track)

        controls_layout.addStretch()
        controls_layout.addWidget(self.prev_button)
        controls_layout.addStretch()
        controls_layout.addWidget(self.play_pause_button)
        controls_layout.addStretch()
        controls_layout.addWidget(self.next_button)
        controls_layout.addStretch()
        player_layout.addLayout(controls_layout)

        # --- Setup UI ---
        self.setup_widget = QWidget()
        setup_layout = QVBoxLayout(self.setup_widget)
        setup_layout.setContentsMargins(0,0,0,0)
        setup_layout.setSpacing(10)
        
        self.setup_info_label = QLabel("Spotify not configured.")
        self.setup_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setup_info_label.setWordWrap(True)
        self.setup_button = QPushButton("Configure Spotify")
        from cognicore.ui.theme import Theme
        self.setup_button.setStyleSheet(Theme.get_button_stylesheet())
        self.setup_button.clicked.connect(self.show_setup_dialog)
        
        setup_layout.addWidget(self.setup_info_label)
        setup_layout.addWidget(self.setup_button)

        # Add both to main layout
        self.content_layout.addWidget(self.player_widget)
        self.content_layout.addWidget(self.setup_widget)
        
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_track_info)
        
        # Connect signals
        self.client.auth_success.connect(self.on_auth_success)
        self.client.auth_error.connect(self.on_auth_error)
        
        # Initial state check
        config = self.app_manager.settings_manager.get("plugins.spotify", {})
        if "YOUR_SPOTIFY_CLIENT_ID" in config.get("client_id", "") or self.client.last_auth_error:
            self.on_auth_error(self.client.last_auth_error or "Credentials not configured.")
        else:
            self.show_player_ui()

        self.adjustSize()

    def show_player_ui(self):
        """Shows the playback controls and hides the setup view."""
        self.player_widget.show()
        self.setup_widget.hide()
        self.adjustSize()

    def show_setup_ui(self, message: str):
        """Shows the setup button and hides the playback controls."""
        self.player_widget.hide()
        self.setup_widget.show()
        self.setup_info_label.setText(message)
        self.update_timer.stop()
        self.adjustSize()
    
    def show_setup_dialog(self):
        """Opens the Spotify credentials setup dialog."""
        from .setup_dialog import SpotifySetupDialog
        dialog = SpotifySetupDialog(self.app_manager.settings_manager, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            logger.info("Spotify setup dialog accepted. Attempting re-authentication.")
            # Show a connecting message while auth happens
            self.show_player_ui()
            self.song_label.setText("Connecting...")
            self.artist_label.setText("Please authorize via your browser if prompted.")
            self.set_controls_enabled(False)
            self.adjustSize()
            # Trigger the plugin to re-run its auth logic
            self.plugin.attempt_authentication()

    def set_controls_enabled(self, enabled: bool):
        self.prev_button.setEnabled(enabled)
        self.play_pause_button.setEnabled(enabled)
        self.next_button.setEnabled(enabled)

    def on_auth_success(self):
        logger.info("Spotify auth successful, starting status polling.")
        self.show_player_ui()
        self.artist_label.setText("Connected")
        self.set_controls_enabled(True)
        self.update_timer.start(3000) # Poll every 3 seconds
        self.update_track_info()

    def on_auth_error(self, error_message: str):
        logger.error(f"Displaying Spotify auth error on widget: {error_message}")
        self.show_setup_ui("Spotify Authorization Failed.\nPlease check your credentials.")
        self.adjustSize()

    def update_track_info(self):
        """Fetches the current track and updates the UI."""
        track_info = self.client.get_current_track()
        if track_info and track_info.get('item'):
            song = track_info['item']['name']
            artists = ", ".join([a['name'] for a in track_info['item']['artists']])
            is_playing = track_info['is_playing']
            
            self.song_label.setText(song)
            self.artist_label.setText(artists)
            self.play_pause_button.setText("❚❚" if is_playing else "▶")
            self.set_controls_enabled(True)
        else:
            self.song_label.setText("Nothing Playing")
            self.artist_label.setText("Spotify")
            self.play_pause_button.setText("▶")
            # Keep controls enabled to allow starting playback on a device.
            self.set_controls_enabled(True) 
        
        self.adjustSize()
```
### File: `/cognicore/plugins/system_monitor_widget/__init__.py`
```py
from __future__ import annotations
from typing import TYPE_CHECKING
from cognicore.plugin_system.interface import CogniCorePlugin

if TYPE_CHECKING:
    from PyQt6.QtWidgets import QWidget
    from cognicore.app_manager import AppManager
    from .widget import SystemMonitorWidget

class SystemMonitorWidgetPlugin(CogniCorePlugin):
    """
    A plugin that provides a widget to display system metrics.
    """
    def __init__(self):
        super().__init__()
        self._widget: SystemMonitorWidget | None = None
        self.app_manager: AppManager | None = None

    def get_widget(self) -> QWidget | None:
        """Returns the SystemMonitorWidget instance."""
        if self._widget is None:
            from .widget import SystemMonitorWidget # Defer import
            self._widget = SystemMonitorWidget(self.app_manager)
        return self._widget

    def setup(self, app_manager: AppManager):
        """
        Stores a reference to the AppManager to access its core services.
        """
        self.app_manager = app_manager
```
### File: `/cognicore/plugins/system_monitor_widget/manifest.json`
```json
{
  "name": "System Monitor",
  "version": "1.0.0",
  "author": "CogniCore Team",
  "description": "A simple widget that displays real-time CPU and Memory usage.",
  "entry_point": "cognicore.plugins.system_monitor_widget:SystemMonitorWidgetPlugin"
}
```
### File: `/cognicore/plugins/system_monitor_widget/widget.py`
```py
from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QGridLayout, QLabel
from PyQt6.QtCore import QTimer
from cognicore.ui.base_widget import BasePluginWidget
from cognicore.ui.theme import Theme

if TYPE_CHECKING:
    from cognicore.app_manager import AppManager

logger = logging.getLogger(__name__)

class SystemMonitorWidget(BasePluginWidget):
    """
    A widget that displays current CPU and Memory usage.
    """
    def __init__(self, app_manager: AppManager | None, parent=None):
        super().__init__(parent)
        if not app_manager or not app_manager.system_monitor:
            raise ValueError("AppManager with SystemMonitor is required.")
        
        self.system_monitor = app_manager.system_monitor

        self.setWindowTitle("System Info")
        
        # Layout for this specific plugin's content
        plugin_layout = QGridLayout()
        plugin_layout.setContentsMargins(15, 15, 15, 15)
        
        # Labels
        self.cpu_label = QLabel("CPU:")
        self.cpu_value = QLabel("0.0%")
        self.mem_label = QLabel("Mem:")
        self.mem_value = QLabel("0.0%")

        for label in [self.cpu_label, self.mem_label, self.cpu_value, self.mem_value]:
            label.setStyleSheet("background: transparent; font-size: 16px;")

        # Add to plugin_layout
        plugin_layout.addWidget(self.cpu_label, 0, 0)
        plugin_layout.addWidget(self.cpu_value, 0, 1)
        plugin_layout.addWidget(self.mem_label, 1, 0)
        plugin_layout.addWidget(self.mem_value, 1, 1)
        
        # Add this plugin's layout to the content area provided by the base widget
        self.content_layout.addLayout(plugin_layout)

        # Timer to update metrics
        self._update_timer = QTimer(self)
        self._update_timer.timeout.connect(self.update_metrics)
        self._update_timer.start(2000) # Update every 2 seconds
        
        self.update_metrics()
        self.adjustSize()

    def update_metrics(self):
        """Fetches the latest data from the core service and updates the labels."""
        cpu = self.system_monitor.get_cpu_usage()
        mem = self.system_monitor.get_memory_usage()

        self.cpu_value.setText(f"{cpu:.1f}%")
        self.mem_value.setText(f"{mem:.1f}%")
```
### File: `/cognicore/plugins/timer/__init__.py`
```py
from cognicore.plugin_system.interface import CogniCorePlugin
from cognicore.plugins.timer.widget import TimerWidget
from PyQt6.QtWidgets import QWidget

class TimerPlugin(CogniCorePlugin):
    """
    A simple timer plugin for CogniCore.
    """
    def __init__(self):
        super().__init__()
        self._widget = None

    def get_widget(self) -> QWidget | None:
        """
        Returns the TimerWidget instance.
        """
        if self._widget is None:
            self._widget = TimerWidget()
        return self._widget
```
### File: `/cognicore/plugins/timer/manifest.json`
```json
{
  "name": "Focus Timer",
  "version": "0.1.0",
  "author": "CogniCore Team",
  "description": "A simple draggable timer that shows the current time.",
  "entry_point": "cognicore.plugins.timer:TimerPlugin"
}
```
### File: `/cognicore/plugins/timer/widget.py`
```py
from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QTime, Qt
from cognicore.ui.base_widget import BasePluginWidget
from cognicore.ui.theme import Theme

class TimerWidget(BasePluginWidget):
    """
    A simple widget that displays the current time and can be dragged.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Clock")
        
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet(f"""
            background-color: transparent;
            color: {Theme.FOREGROUND};
            font-size: {Theme.FONT_SIZE_LARGE};
            font-weight: bold;
            padding: 15px;
        """)
        self.content_layout.addWidget(self.time_label)

        # Timer to update the clock every second
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.update_time()
        self.adjustSize()

    def update_time(self):
        """ Updates the label with the current time. """
        time_str = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(time_str)
```
### File: `/cognicore/plugins/todo/__init__.py`
```py
from cognicore.plugin_system.interface import CogniCorePlugin
from cognicore.plugins.todo.widget import ToDoWidget
from PyQt6.QtWidgets import QWidget

class ToDoPlugin(CogniCorePlugin):
    """
    A to-do list plugin for CogniCore.
    """
    def __init__(self):
        super().__init__()
        self._widget = None

    def get_widget(self) -> QWidget | None:
        """
        Returns the ToDoWidget instance.
        """
        if self._widget is None:
            self._widget = ToDoWidget()
        return self._widget
```
### File: `/cognicore/plugins/todo/manifest.json`
```json
{
  "name": "To-Do List",
  "version": "0.1.0",
  "author": "CogniCore Team",
  "description": "A draggable to-do list widget.",
  "entry_point": "cognicore.plugins.todo:ToDoPlugin"
}
```
### File: `/cognicore/plugins/todo/widget.py`
```py
from PyQt6.QtWidgets import (
    QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem
)
from PyQt6.QtGui import QColor
from cognicore.ui.base_widget import BasePluginWidget
from cognicore.ui.theme import Theme

class ToDoWidget(BasePluginWidget):
    """
    A widget for managing a simple to-do list. Allows adding tasks
    and marking them as complete by double-clicking.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("To-Do List")
        self.setMinimumSize(280, 350)

        # Plugin-specific layout
        plugin_layout = QVBoxLayout()
        plugin_layout.setContentsMargins(15, 15, 15, 15)
        plugin_layout.setSpacing(10)
        
        # Input field for new tasks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Add a task and press Enter...")
        self.task_input.returnPressed.connect(self.add_task)
        self.task_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: {Theme.SECONDARY};
                color: {Theme.FOREGROUND};
                border: 1px solid {Theme.BORDER};
                border-radius: 5px;
                padding: 10px;
                font-size: {Theme.FONT_SIZE_NORMAL};
            }}
        """)

        # List widget to display tasks
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.toggle_task_complete)
        self.task_list.setStyleSheet(f"""
            QListWidget {{
                background-color: {Theme.SECONDARY};
                border: 1px solid {Theme.BORDER};
                border-radius: 5px;
            }}
            QListWidget::item {{
                color: {Theme.FOREGROUND};
                padding: 10px;
                font-size: {Theme.FONT_SIZE_NORMAL};
                border-bottom: 1px solid {Theme.BORDER};
            }}
            QListWidget::item:hover {{
                background-color: {Theme.PRIMARY}20; /* 20 is hex for alpha */
            }}
        """)

        # Add widgets to the plugin-specific layout
        plugin_layout.addWidget(self.task_input)
        plugin_layout.addWidget(self.task_list)
        
        # Add the plugin layout to the main content area from the base widget
        self.content_layout.addLayout(plugin_layout)

    def add_task(self):
        """Adds the text from the input field as a new task to the list."""
        task_text = self.task_input.text().strip()
        if not task_text:
            return

        item = QListWidgetItem(task_text)
        item.setForeground(QColor(Theme.FOREGROUND))
        self.task_list.addItem(item)
        self.task_input.clear()

    def toggle_task_complete(self, item: QListWidgetItem):
        """Toggles the 'completed' state of a task item."""
        font = item.font()
        is_complete = not font.strikeOut()
        font.setStrikeOut(is_complete)
        item.setFont(font)

        if is_complete:
            item.setForeground(QColor("#888888")) # Gray out
        else:
            item.setForeground(QColor(Theme.FOREGROUND))
```
### File: `/cognicore/ui/__init__.py`
```py

```
### File: `/cognicore/ui/base_widget.py`
```py
import logging
import pygetwindow
from PyQt6.QtWidgets import QWidget, QMenu, QSizeGrip, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt, QPoint, QTimer
from PyQt6.QtGui import QAction
from .theme import Theme
from .window_selector_dialog import WindowSelectorDialog

logger = logging.getLogger(__name__)

class BasePluginWidget(QWidget):
    """
    A base class for plugin widgets providing dragging, a context menu for tools,
    window attachment, edit mode visuals, and resizing.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # --- Widget State ---
        self.is_pinned = False
        self.background_opacity = 0.95
        self._is_in_edit_mode = False

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # --- Main Layout & Container ---
        # The single, top-level layout for the entire widget.
        # This is the only place `setLayout` is effectively called for this widget's lifecycle.
        self.container_layout = QVBoxLayout(self)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        
        self.container_frame = QFrame(self)
        self.container_layout.addWidget(self.container_frame)
        
        # The layout where subclasses must place their content.
        self.content_layout = QVBoxLayout(self.container_frame)
        
        # --- Resizing Handle ---
        self.size_grip = QSizeGrip(self.container_frame) # Attach grip to the frame itself
        self.size_grip.setFixedSize(16, 16)
        self.size_grip.setVisible(False)

        self._update_style()

        # --- Window Attachment Logic ---
        self.target_window_title: str | None = None
        self.target_window = None
        self.is_programmatically_hidden = False
        self._position_update_timer = QTimer(self)
        self._position_update_timer.timeout.connect(self._update_attached_position)
        self._position_update_timer.start(100)

    def resizeEvent(self, event):
        """Ensures the size grip is always in the bottom-right corner."""
        super().resizeEvent(event)
        rect = self.rect()
        self.size_grip.move(rect.right() - self.size_grip.width(), rect.bottom() - self.size_grip.height())
        self.size_grip.raise_()

    def _update_style(self):
        """Applies the stylesheet based on the widget's current state."""
        bg_color = Theme.BACKGROUND.format(alpha=self.background_opacity)
        border_style = Theme.EDIT_MODE_BORDER if self._is_in_edit_mode else "border: none;"
        
        self.container_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {bg_color};
                border-radius: {Theme.BORDER_RADIUS};
                {border_style}
            }}
        """)

    def set_edit_mode(self, enabled: bool):
        """Enables or disables the visual and behavioral indicators for edit mode."""
        self._is_in_edit_mode = enabled
        self.size_grip.setVisible(enabled)
        self._update_style()
        
        if enabled:
            self.size_grip.raise_()

    # --- Widget Tools (Context Menu) ---
    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        context_menu.setStyleSheet(Theme.get_menu_stylesheet())

        pin_action = QAction("Pin Widget", self, checkable=True, checked=self.is_pinned)
        pin_action.triggered.connect(self.toggle_pin)
        context_menu.addAction(pin_action)
        
        context_menu.addSeparator()

        opacity_menu = context_menu.addMenu("Set Opacity")
        self.create_opacity_actions(opacity_menu)

        attach_action = QAction("Attach to Window...", self)
        attach_action.triggered.connect(self.show_window_selector)
        context_menu.addAction(attach_action)

        if self.target_window_title:
            detach_action = QAction(f"Detach from '{self.target_window_title}'", self)
            detach_action.triggered.connect(self.detach_from_window)
            context_menu.addAction(detach_action)

        context_menu.addSeparator()

        close_action = QAction("Close Widget", self)
        close_action.triggered.connect(self.hide)
        context_menu.addAction(close_action)

        context_menu.exec(event.globalPos())

    def create_opacity_actions(self, menu: QMenu):
        for percent in [100, 90, 75, 50, 25]:
            opacity_val = percent / 100.0
            action = QAction(f"{percent}%", self, checkable=True)
            action.setChecked(abs(self.background_opacity - opacity_val) < 0.01)
            action.triggered.connect(lambda _, ov=opacity_val: self.set_opacity(ov))
            menu.addAction(action)

    def set_opacity(self, opacity: float):
        self.background_opacity = opacity
        self._update_style()
        
    def toggle_pin(self):
        self.is_pinned = not self.is_pinned
        logger.info(f"Widget '{self.windowTitle()}' pinned state: {self.is_pinned}")

    def show_window_selector(self):
        dialog = WindowSelectorDialog(self)
        if dialog.exec():
            selected_title = dialog.get_selected_title()
            if selected_title:
                self.attach_to_window(selected_title)

    def attach_to_window(self, title: str):
        self.target_window_title = title
        logger.info(f"Widget '{self.windowTitle()}' attached to '{title}'.")

    def detach_from_window(self):
        logger.info(f"Widget '{self.windowTitle()}' detached.")
        self.target_window_title = None
        self.target_window = None

    def _update_attached_position(self):
        if not self.target_window_title: return
        try:
            windows = pygetwindow.getWindowsWithTitle(self.target_window_title)
            self.target_window = windows[0] if windows else None
            if self.target_window and self.target_window.visible:
                if self.isHidden(): self.show()
                self.move(self.target_window.left, self.target_window.top)
            elif self.isVisible():
                self.hide()
        except (pygetwindow.PyGetWindowException, IndexError):
            self.target_window = None
            if self.isVisible(): self.hide()


    # --- Event Handlers ---
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            can_drag = self._is_in_edit_mode or (not self.is_pinned and not self.target_window_title)
            if can_drag:
                self.drag_position = event.globalPosition().toPoint() - self.pos()
                event.accept()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'drag_position') and event.buttons() == Qt.MouseButton.LeftButton and self.drag_position:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None
        event.accept()

    def hideEvent(self, event):
        if not self.isVisible() and not self._is_in_edit_mode:
            self.is_programmatically_hidden = True
        super().hideEvent(event)

    def showEvent(self, event):
        self.is_programmatically_hidden = False
        super().showEvent(event)
```
### File: `/cognicore/ui/notification.py`
```py
import logging
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QPropertyAnimation, QEasingCurve
from cognicore.ui.theme import Theme

logger = logging.getLogger(__name__)

try:
    from playsound import playsound
except ImportError:
    playsound = None


class NotificationWidget(QWidget):
    """
    A pop-up widget for displaying temporary notifications.
    It appears, plays a sound, and then fades out and closes automatically.
    """
    closed = pyqtSignal()

    def __init__(self, title: str, message: str, sound_path: Path | None = None, parent=None):
        super().__init__(parent)
        self.sound_path = sound_path

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setMinimumWidth(340)
        self.setMaximumWidth(340)

        container = QWidget()
        container.setStyleSheet(f"""
            background-color: {Theme.BACKGROUND};
            border-radius: {Theme.BORDER_RADIUS};
            border: 1px solid {Theme.PRIMARY};
        """)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.addWidget(container)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(15, 10, 15, 15)
        layout.setSpacing(5)

        title_label = QLabel(title)
        title_label.setStyleSheet(f"background: transparent; border: none; font-weight: bold; color: {Theme.PRIMARY}; padding-bottom: 5px;")
        
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("background: transparent; border: none;")

        close_button = QPushButton("✕")
        close_button.setFixedSize(20, 20)
        close_button.setStyleSheet(f"""
            QPushButton {{ background: transparent; border: none; font-weight: bold; font-size: 16px; color: {Theme.FOREGROUND}; }}
            QPushButton:hover {{ color: #ff5555; }}
        """)
        close_button.clicked.connect(self.fade_out_and_close)

        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0,0,0,0)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(close_button)

        layout.addLayout(header_layout)
        layout.addWidget(message_label)
        
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        QTimer.singleShot(7000, self.fade_out_and_close)

    def showEvent(self, event):
        super().showEvent(event)
        self._play_sound()
        self.animation.start()
        event.accept()

    def fade_out_and_close(self):
        if self.animation.direction() == QPropertyAnimation.Direction.Forward:
            self.animation.setDirection(QPropertyAnimation.Direction.Backward)
            self.animation.finished.connect(self.close)
            self.animation.start()

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def _play_sound(self):
        if playsound and self.sound_path and self.sound_path.exists():
            try:
                QTimer.singleShot(0, lambda: playsound(str(self.sound_path)))
            except Exception as e:
                logger.error(f"Could not play sound {self.sound_path}: {e}")
        elif not playsound:
            logger.warning("'playsound' library not installed. Cannot play notification sounds.")
```
### File: `/cognicore/ui/settings_window.py`
```py
import logging
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QCheckBox, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from cognicore.core.settings import SettingsManager
from cognicore.core.startup import set_startup, is_startup_enabled
from cognicore.ui.theme import Theme

logger = logging.getLogger(__name__)

class SettingsWindow(QWidget):
    """A window for configuring application-wide settings."""

    def __init__(self, settings_manager: SettingsManager, parent=None):
        super().__init__(parent)
        self.settings_manager = settings_manager

        self.setWindowTitle("CogniCore Settings")
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint) # Use Window flag for standard controls
        self.setMinimumWidth(450)
        
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {Theme.BACKGROUND};
                color: {Theme.FOREGROUND};
                font-family: {Theme.FONT_FAMILY};
                font-size: {Theme.FONT_SIZE_NORMAL};
            }}
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel("Settings")
        title_label.setStyleSheet(f"font-size: 18px; font-weight: bold; color: {Theme.PRIMARY}; padding-bottom: 15px;")
        main_layout.addWidget(title_label)

        form_layout = QFormLayout()
        form_layout.setSpacing(15)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.startup_checkbox = QCheckBox()
        self.startup_checkbox.setStyleSheet(self.get_checkbox_style())
        self.startup_checkbox.setChecked(is_startup_enabled())
        self.startup_checkbox.stateChanged.connect(self.on_startup_changed)
        form_layout.addRow("Start CogniCore on system login:", self.startup_checkbox)

        main_layout.addLayout(form_layout)
        main_layout.addStretch()

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        close_button = QPushButton("Close")
        close_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Theme.PRIMARY};
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #9B40E8;
            }}
        """)
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)
        main_layout.addLayout(button_layout)

    def on_startup_changed(self, state: int):
        """Handles the 'Start on Startup' checkbox state change."""
        enable = state == Qt.CheckState.Checked.value
        try:
            set_startup(enable)
            self.settings_manager.set("general.start_on_startup", enable)
            logger.info(f"Successfully set 'Start on Startup' to {enable}")
        except Exception as e:
            logger.error(f"Failed to apply 'Start on Startup' setting: {e}", exc_info=True)
            # Revert checkbox state on failure
            self.startup_checkbox.blockSignals(True)
            self.startup_checkbox.setChecked(not enable)
            self.startup_checkbox.blockSignals(False)
            # Show error message to user
            QMessageBox.critical(self, "Error", "Could not modify the startup setting.\nPlease run CogniCore as an administrator if the problem persists.")

    
    def get_checkbox_style(self) -> str:
        """Returns the stylesheet for QCheckBox to match the theme."""
        return f"""
            QCheckBox::indicator {{
                width: 20px;
                height: 20px;
                border: 2px solid {Theme.BORDER};
                border-radius: 5px;
            }}
            QCheckBox::indicator:unchecked {{
                background-color: {Theme.SECONDARY};
            }}
            QCheckBox::indicator:unchecked:hover {{
                border: 2px solid {Theme.PRIMARY};
            }}
            QCheckBox::indicator:checked {{
                background-color: {Theme.PRIMARY};
                border: 2px solid {Theme.PRIMARY};
            }}
        """

    def closeEvent(self, event):
        logger.debug("Settings window closed.")
        super().closeEvent(event)
```
### File: `/cognicore/ui/theme.py`
```py
class Theme:
    """
    Centralized theme for the CogniCore application.
    Provides consistent styling for all UI components.
    """
    # Colors
    BACKGROUND      = "rgba(28, 30, 33, {alpha})" # Alpha will be replaced
    FOREGROUND      = "#e0e0e0"
    PRIMARY         = "#8A2BE2"  # BlueViolet
    SECONDARY       = "rgba(45, 47, 51, 1.0)"
    BORDER          = "#444444"
    MENU_HIGHLIGHT  = "#9B40E8"
    
    # Dimensions
    BORDER_RADIUS   = "10px"
    
    # Fonts
    FONT_FAMILY     = "Segoe UI"
    FONT_SIZE_NORMAL = "14px"
    FONT_SIZE_LARGE = "28px"

    # Styles
    EDIT_MODE_BORDER = f"border: 2px dashed {PRIMARY};"

    @staticmethod
    def get_menu_stylesheet() -> str:
        """Returns a consistent stylesheet for QMenu context menus."""
        return f"""
            QMenu {{
                background-color: {Theme.BACKGROUND.format(alpha=1.0)};
                color: {Theme.FOREGROUND};
                border: 1px solid {Theme.BORDER};
                border-radius: 5px;
                padding: 5px;
            }}
            QMenu::item {{
                padding: 8px 25px;
                border-radius: 4px;
            }}
            QMenu::item:selected {{
                background-color: {Theme.MENU_HIGHLIGHT};
            }}
            QMenu::item:disabled {{ color: #888; }}
            QMenu::separator {{
                height: 1px;
                background-color: {Theme.BORDER};
                margin: 5px 0px;
            }}
        """

    @staticmethod
    def get_button_stylesheet() -> str:
        """Returns a consistent stylesheet for standard QPushButtons."""
        return f"""
            QPushButton {{
                background-color: {Theme.PRIMARY};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 5px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {Theme.MENU_HIGHLIGHT};
            }}
            QPushButton:checked {{
                background-color: {Theme.SECONDARY};
                border: 1px solid {Theme.PRIMARY};
            }}
        """
```
### File: `/cognicore/ui/window_selector_dialog.py`
```py
import logging
import pygetwindow
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, QLabel
from .theme import Theme

logger = logging.getLogger(__name__)

class WindowSelectorDialog(QDialog):
    """A dialog for selecting an open application window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_title = None

        self.setWindowTitle("Attach to Window")
        self.setModal(True)
        self.setMinimumSize(450, 500)
        self.setStyleSheet(f"background-color: {Theme.BACKGROUND}; color: {Theme.FOREGROUND};")

        # Layout
        layout = QVBoxLayout(self)
        
        # Instructions
        info_label = QLabel("Select a window to attach the widget to:")
        info_label.setStyleSheet("padding-bottom: 10px;")
        layout.addWidget(info_label)

        # List of windows
        self.window_list = QListWidget()
        self.window_list.setStyleSheet(f"""
            QListWidget {{
                background-color: {Theme.SECONDARY};
                border: 1px solid {Theme.BORDER};
                border-radius: 5px;
                padding: 5px;
            }}
            QListWidget::item {{
                padding: 8px;
            }}
            QListWidget::item:hover {{
                background-color: #3c3f41;
            }}
            QListWidget::item:selected {{
                background-color: {Theme.PRIMARY};
                color: white;
            }}
        """)
        self.populate_window_list()
        self.window_list.itemDoubleClicked.connect(self.accept)
        layout.addWidget(self.window_list)

        # Buttons
        button_layout = QHBoxLayout()
        ok_button = QPushButton("Attach")
        ok_button.clicked.connect(self.accept)
        ok_button.setStyleSheet(f"""
            QPushButton {{ background-color: {Theme.PRIMARY}; color: white; border: none; padding: 8px 16px; border-radius: 5px; }}
            QPushButton:hover {{ background-color: {Theme.MENU_HIGHLIGHT}; }}
        """)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        cancel_button.setStyleSheet(f"""
            QPushButton {{ background-color: {Theme.SECONDARY}; border: 1px solid {Theme.BORDER}; padding: 8px 16px; border-radius: 5px; }}
            QPushButton:hover {{ background-color: #3c3f41; }}
        """)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(ok_button)
        layout.addLayout(button_layout)

    def populate_window_list(self):
        """Fetches and displays all valid, visible windows."""
        try:
            windows = pygetwindow.getAllWindows()
            # Filter out windows that are not visible or have no title
            valid_windows = [w for w in windows if w.visible and w.title]
            
            # Sort windows by title for easier navigation
            valid_windows.sort(key=lambda w: w.title.lower())
            
            for window in valid_windows:
                item = QListWidgetItem(window.title)
                self.window_list.addItem(item)
                
        except Exception as e:
            logger.error(f"Failed to get window list: {e}", exc_info=True)
            self.window_list.addItem("Error: Could not load window list.")

    def accept(self):
        """Sets the selected title when the dialog is accepted."""
        current_item = self.window_list.currentItem()
        if current_item:
            self.selected_title = current_item.text()
            logger.info(f"Window selected for attachment: '{self.selected_title}'")
        super().accept()

    def get_selected_title(self) -> str | None:
        """Returns the title of the window that was selected."""
        return self.selected_title
```
### File: `/logs/.gitkeep`
```text
This directory is for log files.
```
### File: `/logs/cognicore.log`
```log
2025-08-08 21:51:57,676 - root:41 - INFO - Advanced logging configured.
2025-08-08 21:51:57,677 - root:70 - INFO - Crash handler configured.
2025-08-08 21:51:57,934 - __main__:43 - INFO - --- Initializing CogniCore ---
2025-08-08 21:51:57,955 - cognicore.core.settings:59 - INFO - Settings loaded successfully from 'C:\Users\gike5\Desktop\AI_Python\CogniCore\settings.json'.
2025-08-08 21:51:57,956 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 21:51:57,965 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 19.0%, Memory: 73.1%
2025-08-08 21:51:57,967 - cognicore.app_manager:51 - DEBUG - Setting up system tray icon.
2025-08-08 21:51:57,968 - cognicore.core.api_server:39 - INFO - Starting API server on http://127.0.0.1:5000
2025-08-08 21:51:57,991 - cognicore.app_manager:87 - INFO - Starting plugin discovery and loading.
2025-08-08 21:51:57,994 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Control Panel
2025-08-08 21:51:57,995 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Daily Reminder
2025-08-08 21:51:58,029 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Discord Integration
2025-08-08 21:51:58,031 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Spotify Controller
2025-08-08 21:51:58,032 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: System Monitor
2025-08-08 21:51:58,036 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Focus Timer
2025-08-08 21:51:58,037 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: To-Do List
2025-08-08 21:51:58,037 - cognicore.app_manager:91 - INFO - Finished plugin loading. 7 plugins loaded.
2025-08-08 21:51:58,037 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ControlPanelPlugin
2025-08-08 21:51:58,044 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DailyReminderPlugin
2025-08-08 21:51:58,044 - cognicore.plugins.daily_reminder:43 - INFO - Daily Reminder scheduled for 09:30.
2025-08-08 21:51:58,044 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DiscordIntegrationPlugin
2025-08-08 21:51:58,044 - cognicore.plugins.discord_integration:54 - ERROR - Discord Integration: Client ID is not set in settings.json. Plugin will not run.
2025-08-08 21:51:58,045 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SpotifyPlugin
2025-08-08 21:51:58,045 - cognicore.plugins.spotify:72 - WARNING - Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.
2025-08-08 21:51:58,345 - cognicore.plugins.spotify:88 - INFO - Starting Spotify authentication thread.
2025-08-08 21:51:58,346 - cognicore.plugins.spotify.spotify_client:52 - ERROR - Spotify authentication failed: Client ID or Secret not configured in settings.json.
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\plugins\spotify\spotify_client.py", line 29, in initialize
    raise SpotifyOauthError("Client ID or Secret not configured in settings.json.")
spotipy.exceptions.SpotifyOauthError: Client ID or Secret not configured in settings.json.
2025-08-08 21:51:58,375 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SystemMonitorWidgetPlugin
2025-08-08 21:51:58,379 - cognicore.app_manager:101 - DEBUG - Setting up plugin: TimerPlugin
2025-08-08 21:51:58,382 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ToDoPlugin
2025-08-08 21:51:58,385 - cognicore.app_manager:47 - INFO - CogniCore application started successfully.
2025-08-08 21:52:02,949 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 8.3%, Memory: 73.2%
2025-08-08 21:52:06,943 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Project File Modific | Google AI Studio  Mozilla Firefox
2025-08-08 21:52:06,944 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 21:52:07,953 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 13.7%, Memory: 73.4%
2025-08-08 22:01:40,172 - root:41 - INFO - Advanced logging configured.
2025-08-08 22:01:40,172 - root:70 - INFO - Crash handler configured.
2025-08-08 22:01:40,407 - __main__:43 - INFO - --- Initializing CogniCore ---
2025-08-08 22:01:40,432 - cognicore.core.settings:59 - INFO - Settings loaded successfully from 'C:\Users\gike5\Desktop\AI_Python\CogniCore\settings.json'.
2025-08-08 22:01:40,433 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 22:01:40,441 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 20.1%, Memory: 79.5%
2025-08-08 22:01:40,443 - cognicore.app_manager:51 - DEBUG - Setting up system tray icon.
2025-08-08 22:01:40,444 - cognicore.core.api_server:39 - INFO - Starting API server on http://127.0.0.1:5000
2025-08-08 22:01:40,468 - cognicore.app_manager:87 - INFO - Starting plugin discovery and loading.
2025-08-08 22:01:40,470 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Control Panel
2025-08-08 22:01:40,471 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Daily Reminder
2025-08-08 22:01:40,500 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Discord Integration
2025-08-08 22:01:40,501 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Spotify Controller
2025-08-08 22:01:40,502 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: System Monitor
2025-08-08 22:01:40,514 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Focus Timer
2025-08-08 22:01:40,526 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: To-Do List
2025-08-08 22:01:40,526 - cognicore.app_manager:91 - INFO - Finished plugin loading. 7 plugins loaded.
2025-08-08 22:01:40,527 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ControlPanelPlugin
2025-08-08 22:01:40,541 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DailyReminderPlugin
2025-08-08 22:01:40,541 - cognicore.plugins.daily_reminder:43 - INFO - Daily Reminder scheduled for 09:30.
2025-08-08 22:01:40,541 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DiscordIntegrationPlugin
2025-08-08 22:01:40,542 - cognicore.plugins.discord_integration:54 - ERROR - Discord Integration: Client ID is not set in settings.json. Plugin will not run.
2025-08-08 22:01:40,542 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SpotifyPlugin
2025-08-08 22:01:40,542 - cognicore.plugins.spotify:72 - WARNING - Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.
2025-08-08 22:01:40,859 - cognicore.plugins.spotify:88 - INFO - Starting Spotify authentication thread.
2025-08-08 22:01:40,861 - cognicore.plugins.spotify.spotify_client:52 - ERROR - Spotify authentication failed: Client ID or Secret not configured in settings.json.
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\plugins\spotify\spotify_client.py", line 29, in initialize
    raise SpotifyOauthError("Client ID or Secret not configured in settings.json.")
spotipy.exceptions.SpotifyOauthError: Client ID or Secret not configured in settings.json.
2025-08-08 22:01:40,884 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SystemMonitorWidgetPlugin
2025-08-08 22:01:40,898 - cognicore.app_manager:101 - DEBUG - Setting up plugin: TimerPlugin
2025-08-08 22:01:40,900 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ToDoPlugin
2025-08-08 22:01:40,903 - cognicore.app_manager:47 - INFO - CogniCore application started successfully.
2025-08-08 22:01:40,903 - cognicore.plugins.spotify.widget:91 - ERROR - Displaying Spotify auth error: Auth Error: Client ID or Secret not configured in settings.json.. Check settings.json.
2025-08-08 22:01:45,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.5%, Memory: 79.6%
2025-08-08 22:01:46,433 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Project File Modific | Google AI Studio  Mozilla Firefox
2025-08-08 22:01:46,433 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:01:49,435 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: C:\Users\gike5\Desktop\AI_Python\CogniCore and 3 more tabs - File Explorer
2025-08-08 22:01:49,436 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:01:50,443 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 20.3%, Memory: 79.2%
2025-08-08 22:01:52,429 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: AI Suit Plugin:File Token Limi | Google AI Studio  Mozilla Firefox
2025-08-08 22:01:52,429 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:01:55,444 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 13.0%, Memory: 79.6%
2025-08-08 22:01:58,426 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: GuardianComm Code Security Aud | Google AI Studio  Mozilla Firefox
2025-08-08 22:01:58,427 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:02:00,435 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.9%, Memory: 79.6%
2025-08-08 22:02:05,435 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.3%, Memory: 79.6%
2025-08-08 22:02:10,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.8%, Memory: 79.5%
2025-08-08 22:02:10,434 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: AI Studio
2025-08-08 22:02:10,434 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:02:15,433 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.1%, Memory: 79.7%
2025-08-08 22:02:20,447 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.0%, Memory: 79.2%
2025-08-08 22:02:22,449 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: helpers.py - GuardianComm - Koromali
2025-08-08 22:02:22,449 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:02:25,435 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.8%, Memory: 79.2%
2025-08-08 22:02:30,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.9%, Memory: 79.2%
2025-08-08 22:02:35,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.2%, Memory: 78.8%
2025-08-08 22:02:40,444 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.6%, Memory: 78.9%
2025-08-08 22:02:45,435 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.5%, Memory: 79.0%
2025-08-08 22:02:46,441 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Project File Modific | Google AI Studio  Mozilla Firefox
2025-08-08 22:02:46,441 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:02:50,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 20.9%, Memory: 79.1%
2025-08-08 22:02:52,446 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: helpers.py - GuardianComm - Koromali
2025-08-08 22:02:52,446 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:02:55,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 16.3%, Memory: 79.2%
2025-08-08 22:02:55,444 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Branch of LLM Response Patchin | Google AI Studio  Mozilla Firefox
2025-08-08 22:02:55,444 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:02:58,448 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: NVIDIA Installer
2025-08-08 22:02:58,448 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:03:00,435 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 8.5%, Memory: 79.3%
2025-08-08 22:03:04,448 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Mozilla Firefox
2025-08-08 22:03:04,448 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:03:05,437 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.6%, Memory: 79.4%
2025-08-08 22:03:10,433 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 7.5%, Memory: 79.5%
2025-08-08 22:03:15,433 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 8.5%, Memory: 79.5%
2025-08-08 22:03:19,453 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: nvidia cuda stuck on installing nsight visual studio edition - Google Search  Mozilla Firefox
2025-08-08 22:03:19,453 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:03:20,436 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.6%, Memory: 80.1%
2025-08-08 22:03:22,447 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: IDLE, Title: 
2025-08-08 22:03:22,447 - cognicore.app_manager:128 - INFO - Activity changed. Type: IDLE. Busy state: False
2025-08-08 22:03:25,436 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 18.2%, Memory: 80.6%
2025-08-08 22:03:25,444 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Task Manager
2025-08-08 22:03:25,444 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:03:30,442 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.1%, Memory: 80.6%
2025-08-08 22:03:35,434 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.1%, Memory: 80.0%
2025-08-08 22:03:40,435 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.2%, Memory: 80.0%
2025-08-08 22:03:45,449 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 15.1%, Memory: 80.0%
2025-08-08 22:03:50,449 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 17.2%, Memory: 75.1%
2025-08-08 22:03:52,442 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: nvidia cuda stuck on installing nsight visual studio edition - Google Search  Mozilla Firefox
2025-08-08 22:03:52,442 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:03:55,450 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 22.2%, Memory: 76.7%
2025-08-08 22:04:00,451 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 20.1%, Memory: 79.8%
2025-08-08 22:04:04,445 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: NVIDIA Installer
2025-08-08 22:04:04,445 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:05,452 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.1%, Memory: 80.0%
2025-08-08 22:04:07,441 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: nvidia cuda stuck on installing nsight visual studio edition - Google Search  Mozilla Firefox
2025-08-08 22:04:07,441 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:10,453 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 8.4%, Memory: 79.8%
2025-08-08 22:04:15,452 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 6.5%, Memory: 79.6%
2025-08-08 22:04:19,442 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: NVIDIA Installer
2025-08-08 22:04:19,442 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:20,457 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 8.2%, Memory: 79.5%
2025-08-08 22:04:22,442 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Microsoft Visual Studio Community 2022
2025-08-08 22:04:22,444 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:25,450 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 16.3%, Memory: 80.6%
2025-08-08 22:04:25,451 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: NVIDIA Installer
2025-08-08 22:04:25,451 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:30,453 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 22.0%, Memory: 80.5%
2025-08-08 22:04:31,442 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: IDLE, Title: 
2025-08-08 22:04:31,443 - cognicore.app_manager:128 - INFO - Activity changed. Type: IDLE. Busy state: False
2025-08-08 22:04:34,452 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Task Manager
2025-08-08 22:04:34,452 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:35,461 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 17.1%, Memory: 81.0%
2025-08-08 22:04:40,464 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.0%, Memory: 75.8%
2025-08-08 22:04:43,454 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: nvidia cuda stuck on installing nsight visual studio edition - Google Search  Mozilla Firefox
2025-08-08 22:04:43,454 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:04:45,460 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 16.7%, Memory: 74.9%
2025-08-08 22:04:50,458 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.9%, Memory: 75.0%
2025-08-08 22:04:55,450 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 24.6%, Memory: 74.8%
2025-08-08 22:04:55,450 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Mozilla Firefox
2025-08-08 22:04:55,451 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:05:00,480 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 23.5%, Memory: 75.4%
2025-08-08 22:05:01,452 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: IDLE, Title: 
2025-08-08 22:05:01,452 - cognicore.app_manager:128 - INFO - Activity changed. Type: IDLE. Busy state: False
2025-08-08 22:05:04,448 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: 10% NVIDIA Installer Extraction
2025-08-08 22:05:04,448 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:05:05,454 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 53.5%, Memory: 80.6%
2025-08-08 22:05:07,452 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Project File Modific | Google AI Studio  Mozilla Firefox
2025-08-08 22:05:07,452 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:05:10,458 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 42.6%, Memory: 80.8%
2025-08-08 22:05:15,452 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 30.9%, Memory: 82.0%
2025-08-08 22:05:19,442 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: helpers.py - GuardianComm - Koromali
2025-08-08 22:05:19,442 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:05:20,450 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 39.9%, Memory: 81.0%
2025-08-08 22:05:22,446 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: AI Studio
2025-08-08 22:05:22,446 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:05:25,455 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 42.1%, Memory: 81.5%
2025-08-08 22:05:30,451 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 25.4%, Memory: 75.1%
2025-08-08 22:05:35,450 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.2%, Memory: 75.0%
2025-08-08 22:05:37,454 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: IDLE, Title: 
2025-08-08 22:05:37,454 - cognicore.app_manager:128 - INFO - Activity changed. Type: IDLE. Busy state: False
2025-08-08 22:05:40,454 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.1%, Memory: 74.7%
2025-08-08 22:05:40,455 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 22:05:40,455 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:05:47,724 - root:41 - INFO - Advanced logging configured.
2025-08-08 22:05:47,724 - root:70 - INFO - Crash handler configured.
2025-08-08 22:05:47,940 - __main__:43 - INFO - --- Initializing CogniCore ---
2025-08-08 22:05:47,963 - cognicore.core.settings:59 - INFO - Settings loaded successfully from 'C:\Users\gike5\Desktop\AI_Python\CogniCore\settings.json'.
2025-08-08 22:05:47,964 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 22:05:47,971 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 16.7%, Memory: 74.0%
2025-08-08 22:05:47,972 - cognicore.app_manager:51 - DEBUG - Setting up system tray icon.
2025-08-08 22:05:47,979 - cognicore.core.api_server:39 - INFO - Starting API server on http://127.0.0.1:5000
2025-08-08 22:05:47,993 - cognicore.app_manager:87 - INFO - Starting plugin discovery and loading.
2025-08-08 22:05:47,994 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Control Panel
2025-08-08 22:05:47,995 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Daily Reminder
2025-08-08 22:05:48,041 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Discord Integration
2025-08-08 22:05:48,042 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Spotify Controller
2025-08-08 22:05:48,042 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: System Monitor
2025-08-08 22:05:48,065 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Focus Timer
2025-08-08 22:05:48,073 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: To-Do List
2025-08-08 22:05:48,074 - cognicore.app_manager:91 - INFO - Finished plugin loading. 7 plugins loaded.
2025-08-08 22:05:48,074 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ControlPanelPlugin
2025-08-08 22:05:48,086 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DailyReminderPlugin
2025-08-08 22:05:48,086 - cognicore.plugins.daily_reminder:43 - INFO - Daily Reminder scheduled for 09:30.
2025-08-08 22:05:48,087 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DiscordIntegrationPlugin
2025-08-08 22:05:48,087 - cognicore.plugins.discord_integration:54 - ERROR - Discord Integration: Client ID is not set in settings.json. Plugin will not run.
2025-08-08 22:05:48,087 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SpotifyPlugin
2025-08-08 22:05:48,087 - cognicore.plugins.spotify:72 - WARNING - Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.
2025-08-08 22:05:48,397 - cognicore.plugins.spotify:88 - INFO - Starting Spotify authentication thread.
2025-08-08 22:05:48,398 - cognicore.plugins.spotify.spotify_client:52 - ERROR - Spotify authentication failed: Client ID or Secret not configured in settings.json.
Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\plugins\spotify\spotify_client.py", line 29, in initialize
    raise SpotifyOauthError("Client ID or Secret not configured in settings.json.")
spotipy.exceptions.SpotifyOauthError: Client ID or Secret not configured in settings.json.
2025-08-08 22:05:48,431 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SystemMonitorWidgetPlugin
2025-08-08 22:05:48,442 - cognicore.app_manager:101 - DEBUG - Setting up plugin: TimerPlugin
2025-08-08 22:05:48,444 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ToDoPlugin
2025-08-08 22:05:48,446 - cognicore.app_manager:47 - INFO - CogniCore application started successfully.
2025-08-08 22:05:52,965 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.3%, Memory: 74.0%
2025-08-08 22:05:53,958 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Project File Modific | Google AI Studio  Mozilla Firefox
2025-08-08 22:05:53,958 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:45:07,250 - root:41 - INFO - Advanced logging configured.
2025-08-08 22:45:07,251 - root:70 - INFO - Crash handler configured.
2025-08-08 22:45:07,535 - __main__:43 - INFO - --- Initializing CogniCore ---
2025-08-08 22:45:07,583 - cognicore.core.settings:59 - INFO - Settings loaded successfully from 'C:\Users\gike5\Desktop\AI_Python\CogniCore\settings.json'.
2025-08-08 22:45:07,587 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 22:45:07,595 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 16.8%, Memory: 84.3%
2025-08-08 22:45:07,598 - cognicore.app_manager:51 - DEBUG - Setting up system tray icon.
2025-08-08 22:45:07,599 - cognicore.core.api_server:39 - INFO - Starting API server on http://127.0.0.1:5000
2025-08-08 22:45:07,627 - cognicore.app_manager:87 - INFO - Starting plugin discovery and loading.
2025-08-08 22:45:07,629 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Control Panel
2025-08-08 22:45:07,631 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Daily Reminder
2025-08-08 22:45:07,661 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Discord Integration
2025-08-08 22:45:07,671 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Spotify Controller
2025-08-08 22:45:07,672 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: System Monitor
2025-08-08 22:45:07,674 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Focus Timer
2025-08-08 22:45:07,675 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: To-Do List
2025-08-08 22:45:07,676 - cognicore.app_manager:91 - INFO - Finished plugin loading. 7 plugins loaded.
2025-08-08 22:45:07,676 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ControlPanelPlugin
2025-08-08 22:45:07,698 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DailyReminderPlugin
2025-08-08 22:45:07,699 - cognicore.plugins.daily_reminder:43 - INFO - Daily Reminder scheduled for 09:30.
2025-08-08 22:45:07,699 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DiscordIntegrationPlugin
2025-08-08 22:45:07,699 - cognicore.plugins.discord_integration:54 - ERROR - Discord Integration: Client ID is not set in settings.json. Plugin will not run.
2025-08-08 22:45:07,699 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SpotifyPlugin
2025-08-08 22:45:07,699 - cognicore.plugins.spotify:72 - WARNING - Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.
2025-08-08 22:45:08,032 - cognicore.plugins.spotify:91 - INFO - Starting Spotify authentication thread.
2025-08-08 22:45:08,033 - cognicore.plugins.spotify.spotify_client:54 - ERROR - Spotify authentication failed: Client ID or Secret not configured in settings.json.
2025-08-08 22:45:08,045 - cognicore.plugins.spotify.widget:94 - ERROR - Displaying Spotify auth error on widget: Auth Error: Client ID or Secret not configured in settings.json.. Check settings.json.
2025-08-08 22:45:08,070 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SystemMonitorWidgetPlugin
2025-08-08 22:45:08,072 - cognicore.app_manager:101 - DEBUG - Setting up plugin: TimerPlugin
2025-08-08 22:45:08,073 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ToDoPlugin
2025-08-08 22:45:08,081 - cognicore.app_manager:47 - INFO - CogniCore application started successfully.
2025-08-08 22:45:12,593 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 13.1%, Memory: 84.4%
2025-08-08 22:45:16,585 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Project File Modific | Google AI Studio  Mozilla Firefox
2025-08-08 22:45:16,586 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:45:17,596 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 17.8%, Memory: 84.9%
2025-08-08 22:45:19,585 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: GuardianComm Code Security Aud | Google AI Studio  Mozilla Firefox
2025-08-08 22:45:19,586 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:45:22,595 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 18.6%, Memory: 85.3%
2025-08-08 22:45:22,595 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Branch of LLM Response Patchin | Google AI Studio  Mozilla Firefox
2025-08-08 22:45:22,595 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:45:27,598 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.4%, Memory: 85.3%
2025-08-08 22:45:28,588 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: AI Studio
2025-08-08 22:45:28,588 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:45:32,590 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 20.4%, Memory: 86.8%
2025-08-08 22:45:37,605 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 21.2%, Memory: 86.6%
2025-08-08 22:45:40,596 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Corvus AI Assistant Launcher
2025-08-08 22:45:40,596 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 22:45:42,594 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.9%, Memory: 86.5%
2025-08-08 22:45:43,590 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 22:45:43,590 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 23:13:46,922 - root:41 - INFO - Advanced logging configured.
2025-08-08 23:13:46,922 - root:70 - INFO - Crash handler configured.
2025-08-08 23:13:47,182 - __main__:43 - INFO - --- Initializing CogniCore ---
2025-08-08 23:13:47,230 - cognicore.core.settings:59 - INFO - Settings loaded successfully from 'C:\Users\gike5\Desktop\AI_Python\CogniCore\settings.json'.
2025-08-08 23:13:47,234 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 23:13:47,242 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.6%, Memory: 83.1%
2025-08-08 23:13:47,245 - cognicore.app_manager:51 - DEBUG - Setting up system tray icon.
2025-08-08 23:13:47,245 - cognicore.core.api_server:39 - INFO - Starting API server on http://127.0.0.1:5000
2025-08-08 23:13:47,273 - cognicore.app_manager:87 - INFO - Starting plugin discovery and loading.
2025-08-08 23:13:47,274 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Control Panel
2025-08-08 23:13:47,275 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Daily Reminder
2025-08-08 23:13:47,303 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Discord Integration
2025-08-08 23:13:47,304 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Spotify Controller
2025-08-08 23:13:47,304 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: System Monitor
2025-08-08 23:13:47,306 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Focus Timer
2025-08-08 23:13:47,308 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: To-Do List
2025-08-08 23:13:47,308 - cognicore.app_manager:91 - INFO - Finished plugin loading. 7 plugins loaded.
2025-08-08 23:13:47,308 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ControlPanelPlugin
2025-08-08 23:13:47,332 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DailyReminderPlugin
2025-08-08 23:13:47,333 - cognicore.plugins.daily_reminder:43 - INFO - Daily Reminder scheduled for 09:30.
2025-08-08 23:13:47,333 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DiscordIntegrationPlugin
2025-08-08 23:13:47,333 - cognicore.plugins.discord_integration:54 - ERROR - Discord Integration: Client ID is not set in settings.json. Plugin will not run.
2025-08-08 23:13:47,333 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SpotifyPlugin
2025-08-08 23:13:47,333 - cognicore.plugins.spotify:72 - WARNING - Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.
2025-08-08 23:13:47,634 - cognicore.plugins.spotify:91 - INFO - Starting Spotify authentication thread.
2025-08-08 23:13:47,638 - cognicore.plugins.spotify.spotify_client:54 - ERROR - Spotify authentication failed: Client ID or Secret not configured in settings.json.
2025-08-08 23:13:47,742 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SystemMonitorWidgetPlugin
2025-08-08 23:13:47,744 - cognicore.app_manager:101 - DEBUG - Setting up plugin: TimerPlugin
2025-08-08 23:13:47,746 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ToDoPlugin
2025-08-08 23:13:47,754 - cognicore.app_manager:47 - INFO - CogniCore application started successfully.
2025-08-08 23:13:47,754 - cognicore.plugins.spotify.widget:94 - ERROR - Displaying Spotify auth error on widget: Auth Error: Client ID or Secret not configured in settings.json.. Check settings.json.
2025-08-08 23:13:52,243 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 7.0%, Memory: 83.2%
2025-08-08 23:13:57,231 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 7.9%, Memory: 83.3%
2025-08-08 23:14:02,244 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 6.4%, Memory: 83.3%
2025-08-08 23:14:07,231 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.7%, Memory: 83.1%
2025-08-08 23:14:08,238 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Project File Modification | Google AI Studio  Mozilla Firefox
2025-08-08 23:14:08,239 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 23:14:12,231 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 7.0%, Memory: 83.1%
2025-08-08 23:14:17,229 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 7.3%, Memory: 83.1%
2025-08-08 23:14:22,243 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 7.3%, Memory: 83.3%
2025-08-08 23:14:27,233 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.1%, Memory: 83.2%
2025-08-08 23:14:32,233 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.4%, Memory: 83.3%
2025-08-08 23:14:37,233 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.1%, Memory: 83.3%
2025-08-08 23:14:42,245 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.6%, Memory: 83.5%
2025-08-08 23:14:47,258 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 9.2%, Memory: 83.3%
2025-08-08 23:14:52,255 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.9%, Memory: 83.3%
2025-08-08 23:14:57,250 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 10.9%, Memory: 83.3%
2025-08-08 23:15:02,254 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.0%, Memory: 83.3%
2025-08-08 23:15:07,257 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.6%, Memory: 83.2%
2025-08-08 23:15:12,251 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.8%, Memory: 83.2%
2025-08-08 23:15:17,248 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 13.0%, Memory: 83.0%
2025-08-08 23:15:22,257 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.9%, Memory: 82.6%
2025-08-08 23:15:27,248 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 13.8%, Memory: 82.5%
2025-08-08 23:15:32,260 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 15.6%, Memory: 82.6%
2025-08-08 23:15:37,254 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 17.7%, Memory: 82.4%
2025-08-08 23:15:42,249 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 14.9%, Memory: 82.5%
2025-08-08 23:15:47,256 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.3%, Memory: 82.5%
2025-08-08 23:15:52,253 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.6%, Memory: 82.6%
2025-08-08 23:15:57,252 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 12.9%, Memory: 83.0%
2025-08-08 23:16:02,264 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 18.8%, Memory: 83.4%
2025-08-08 23:16:07,254 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 18.0%, Memory: 83.5%
2025-08-08 23:16:08,319 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Daemon Initialization Error | Google AI Studio  Mozilla Firefox
2025-08-08 23:16:08,320 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 23:16:11,317 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: AI Studio
2025-08-08 23:16:11,317 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 23:16:12,251 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 11.7%, Memory: 83.3%
2025-08-08 23:16:17,253 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 21.9%, Memory: 83.7%
2025-08-08 23:16:17,321 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: Project Modification Instructi | Google AI Studio  Mozilla Firefox
2025-08-08 23:16:17,321 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 23:16:20,333 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: IDLE, Title: 
2025-08-08 23:16:20,334 - cognicore.app_manager:128 - INFO - Activity changed. Type: IDLE. Busy state: False
2025-08-08 23:16:22,248 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 13.1%, Memory: 83.5%
2025-08-08 23:16:23,334 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: AI Studio
2025-08-08 23:16:23,334 - cognicore.app_manager:128 - INFO - Activity changed. Type: WORKING. Busy state: True
2025-08-08 23:19:44,831 - root:41 - INFO - Advanced logging configured.
2025-08-08 23:19:44,831 - root:70 - INFO - Crash handler configured.
2025-08-08 23:19:45,021 - __main__:43 - INFO - --- Initializing CogniCore ---
2025-08-08 23:19:45,042 - cognicore.core.settings:59 - INFO - Settings loaded successfully from 'C:\Users\gike5\Desktop\AI_Python\CogniCore\settings.json'.
2025-08-08 23:19:45,043 - cognicore.core.activity_monitor:69 - INFO - Activity changed -> Type: WORKING, Title: CogniCore Launcher
2025-08-08 23:19:45,058 - cognicore.core.system_monitor:27 - DEBUG - System Metrics Polled - CPU: 60.8%, Memory: 84.6%
2025-08-08 23:19:45,059 - cognicore.app_manager:51 - DEBUG - Setting up system tray icon.
2025-08-08 23:19:45,084 - cognicore.core.api_server:39 - INFO - Starting API server on http://127.0.0.1:5000
2025-08-08 23:19:45,086 - cognicore.app_manager:87 - INFO - Starting plugin discovery and loading.
2025-08-08 23:19:45,088 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Control Panel
2025-08-08 23:19:45,090 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Daily Reminder
2025-08-08 23:19:45,119 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Discord Integration
2025-08-08 23:19:45,140 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Spotify Controller
2025-08-08 23:19:45,141 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: System Monitor
2025-08-08 23:19:45,143 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: Focus Timer
2025-08-08 23:19:45,144 - cognicore.plugin_system.manager:37 - INFO - Successfully loaded plugin: To-Do List
2025-08-08 23:19:45,145 - cognicore.app_manager:91 - INFO - Finished plugin loading. 7 plugins loaded.
2025-08-08 23:19:45,145 - cognicore.app_manager:101 - DEBUG - Setting up plugin: ControlPanelPlugin
2025-08-08 23:19:45,150 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DailyReminderPlugin
2025-08-08 23:19:45,150 - cognicore.plugins.daily_reminder:43 - INFO - Daily Reminder scheduled for 09:30.
2025-08-08 23:19:45,150 - cognicore.app_manager:101 - DEBUG - Setting up plugin: DiscordIntegrationPlugin
2025-08-08 23:19:45,150 - cognicore.plugins.discord_integration:54 - ERROR - Discord Integration: Client ID is not set in settings.json. Plugin will not run.
2025-08-08 23:19:45,150 - cognicore.app_manager:101 - DEBUG - Setting up plugin: SpotifyPlugin
2025-08-08 23:19:45,150 - cognicore.plugins.spotify:87 - WARNING - Spotify plugin is enabled, but Client ID or Secret are not configured in settings.json.

```
### File: `/logs/crash.log`
```log
================================================================================
FAILSAFE CRASH REPORT - 2025-08-08T23:19:45.574610
================================================================================
A critical error occurred during application startup, before the main crash handler was ready.
This usually indicates a problem with a core module import or a configuration error.

Traceback (most recent call last):
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\main.py", line 44, in main
    manager = AppManager(project_root_path=project_root)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\app_manager.py", line 46, in __init__
    self.load_plugins()
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\app_manager.py", line 105, in load_plugins
    widget = plugin.get_widget()
             ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\plugins\spotify\__init__.py", line 51, in get_widget
    from .widget import SpotifyWidget # Defer import
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\gike5\Desktop\AI_Python\CogniCore\cognicore\plugins\spotify\widget.py", line 5, in <module>
    from PyQt6.QtCore import QTimer, Qt, QDialog
ImportError: cannot import name 'QDialog' from 'PyQt6.QtCore' (C:\Users\gike5\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt6\QtCore.pyd)


```
### File: `/requirements.txt`
```txt
PyQt6
pygetwindow
playsound==1.2.2
psutil
Flask
pypresence
spotipy
PyWin32; sys_platform == 'win32'
```
### File: `/run.bat`
```bat
@echo off
TITLE CogniCore Launcher

REM Get the directory of this batch file, which is the project root
set "batch_dir=%~dp0"

echo [CogniCore] Starting up...
echo.

REM --- Step 1: Install Dependencies ---
echo [CogniCore] Checking and installing required Python packages...
pip install -r "%batch_dir%requirements.txt"
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Failed to install dependencies from requirements.txt.
    echo Please ensure Python and pip are installed and accessible from your terminal.
    pause
    exit /b %ERRORLEVEL%
)
echo [CogniCore] Dependencies are up to date.
echo.


REM --- Step 2: Run the Application ---
echo [CogniCore] Launching application...
echo If the window closes immediately with an error, check the 'logs' directory for
echo 'cognicore.log' or 'crash.log'.
python "%batch_dir%cognicore\main.py"

echo.
echo [CogniCore] Application has been closed. Press any key to exit.
pause > nul
```
### File: `/settings.json`
```json
{
    "general": {
        "start_on_startup": true
    },
    "plugins": {
        "daily_reminder": {
            "enabled": true,
            "hour": 9,
            "minute": 30,
            "title": "Daily Reminder",
            "message": "Time for a quick break! Stretch and rest your eyes.",
            "sound": "default_notification.wav"
        },
        "discord_integration": {
            "enabled": true,
            "client_id": "YOUR_DISCORD_CLIENT_ID_HERE"
        },
        "spotify": {
            "enabled": true,
            "client_id": "YOUR_SPOTIFY_CLIENT_ID_HERE",
            "client_secret": "YOUR_SPOTIFY_CLIENT_SECRET_HERE",
            "redirect_uri": "http://localhost:8888/callback"
        }
    }
}
```