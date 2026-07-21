# /main.py
import sys
import traceback
import os
import datetime

# --- Failsafe Logger ---
# This is a simple logger used ONLY for critical startup errors before the main logger is initialized.
def failsafe_log(message: str):
    """A simple logger that writes to a file in the user's home directory."""
    try:
        log_path = os.path.join(os.path.expanduser("~"), "koromali_crash.log")
        with open(log_path, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")
    except Exception:
        # If this fails, we have no other recourse.
        pass

# This must be the very first thing done to ensure all subsequent imports work correctly.
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


# --- Global objects and functions ---
# These are defined globally so they can be referenced by the functions below,
# but they will be initialized inside main() to catch import errors.
app_state = {
    "app": None, "splash": None, "main_window": None,
    "theme_manager": None, "file_handler": None, "settings_manager": None,
    "debug_mode": False,
    "log": None # Main logger will be assigned here
}


def fallback_excepthook(exc_type, exc_value, exc_tb):
    """A final safety net to catch and log any unhandled exceptions."""
    main_log = app_state.get("log")
    if main_log:
        main_log.error("--- FALLBACK EXCEPTHOOK TRIGGERED ---")
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return

        main_log.critical("--- FATAL UNHANDLED EXCEPTION ---", exc_info=(exc_type, exc_value, exc_tb))
    
    tb_text = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    failsafe_log("--- FALLBACK EXCEPTHOOK CAUGHT FATAL ERROR ---\n" + tb_text)
    print(f"FATAL ERROR:\n{tb_text}", file=sys.stderr)
    sys.__excepthook__(exc_type, exc_value, exc_tb)


def run_loading_step(tasks, args_to_process=None):
    """
    Executes a series of loading tasks sequentially using QTimer events.
    """
    from PyQt6.QtCore import QTimer

    if tasks:
        task_name, task_func = tasks.pop(0)
        app_state["log"].info(f"Executing loading task: '{task_name}'")
        if splash := app_state.get("splash"):
            splash.set_status(task_name)

        task_func()
        QTimer.singleShot(50, lambda: run_loading_step(tasks, args_to_process))
    else:
        app_state["log"].info("All loading tasks complete. Application is running.")
        if main_window := app_state.get("main_window"):
            splash = app_state.get("splash")
            
            # After the UI is shown and stable, process any command-line file arguments.
            if args_to_process:
                app_state["log"].info(f"Processing command-line arguments: {args_to_process}")
                for file_path in args_to_process:
                    # Defer with a timer to ensure the main window is fully settled
                    QTimer.singleShot(100, lambda fp=file_path: main_window._process_command_line_arg(fp))

            main_window.finalize_and_show(splash)


def load_step_1_managers():
    """Initializes and configures core application managers."""
    # These imports are safe because they were loaded in main()
    from app_core.settings_manager import SettingsManager
    from app_core.theme_manager import ThemeManager
    from app_core.file_handler import FileHandler
    
    # SettingsManager is created first and passed to others.
    app_state["settings_manager"] = SettingsManager()
    app_state["theme_manager"] = ThemeManager(app_state["settings_manager"])
    app_state["file_handler"] = FileHandler(app_state["settings_manager"])
    
    app_state["theme_manager"].apply_theme_to_app(app_state["app"])
    app_state["log"].debug("Step 1: Core managers loaded.")


def load_step_2_create_main_window():
    """Creates the main application window instance."""
    from ui.main_window import MainWindow

    app_state["main_window"] = MainWindow(
        file_handler=app_state["file_handler"],
        theme_manager=app_state["theme_manager"],
        settings_manager=app_state["settings_manager"],
        debug_mode=app_state["debug_mode"]
    )
    app_state["log"].info("MainWindow instance created successfully.")


def main():
    """The main entry point for the Koromali application."""
    # Assign the exception hook immediately
    sys.excepthook = fallback_excepthook

    try:
        from utils.qt_compat import ensure_qt_binding
        ensure_qt_binding()

        # Move all critical imports inside this block.
        # If any of these fail, it indicates a fundamental issue.
        from PyQt6.QtWidgets import QApplication, QMessageBox
        from PyQt6.QtCore import QTimer

        from app_core.config import APP_NAME, ORG_NAME
        from utils.versioning import APP_VERSION
        from utils.logger import log, get_app_data_path

        # Assign the main logger to the global state
        app_state["log"] = log

    except Exception:
        tb_text = traceback.format_exc()
        failsafe_log("--- FATAL STARTUP ERROR ---\n"
                     "An error occurred during initial module loading, which prevented the application from starting.\n"
                     "This is often caused by a syntax error or a missing/corrupted dependency.\n\n" + tb_text)
        
        # Try to show a GUI message box. This may fail if PyQt is the problem, but it's a best effort.
        try:
            # We must create a dummy app to show a message box if the main one couldn't be created.
            app = QApplication.instance() or QApplication([])
            error_log_path = os.path.join(os.path.expanduser("~"), "koromali_crash.log")
            QMessageBox.critical(None, "Fatal Startup Error",
                                 "Koromali could not start due to a critical error.\n\n"
                                 "This is often caused by a syntax error in the source code.\n"
                                 f"Please check the log file for details:\n{error_log_path}")
        except Exception:
            # If PyQt itself is broken, this will fail. Just print to stderr.
            print("CRITICAL: Failed to show error message box. PyQt may be corrupted.", file=sys.stderr)

        sys.exit(1)

    # These imports can be done after the initial block since they are for the UI.
    from ui.widgets.splash_screen import SplashScreen

    app_state["debug_mode"] = "--debug" in sys.argv
    files_to_open = [arg for arg in sys.argv[1:] if not arg.startswith('--')]

    log.info("=" * 53)
    log.info(f"{APP_NAME} Application Starting... (Version: {APP_VERSION}, Debug: {app_state['debug_mode']})")
    log.info(f"Python version: {sys.version.splitlines()[0]}")
    log.info(f"Operating System: {sys.platform}")
    log.info("=" * 53)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(ORG_NAME)
    app.setQuitOnLastWindowClosed(False)
    log.info("Application 'QuitOnLastWindowClosed' set to FALSE.")
    app_state["app"] = app

    try:
        splash = SplashScreen()
        app_state["splash"] = splash
        splash.show()
        log.info("Splash screen displayed.")
    except Exception as e:
        log.critical(f"Fatal error initializing splash screen: {e}", exc_info=True)
        return

    loading_tasks = [
        ("Loading core managers...", load_step_1_managers),
        ("Creating main window...", load_step_2_create_main_window),
    ]

    QTimer.singleShot(100, lambda: run_loading_step(loading_tasks, files_to_open))

    log.info("Entering main event loop...")
    exit_code = app.exec()
    log.info(f"Exited main event loop with code: {exit_code}")
    sys.exit(exit_code)


if __name__ == '__main__':
    # Initial check for PyQt6, as it's needed to even show an error dialog.
    try:
        from utils.qt_compat import ensure_qt_binding
        ensure_qt_binding()
        from PyQt6.QtWidgets import QApplication
    except ImportError:
        # A simple console print for the most basic failure case.
        print(
            "FATAL ERROR: PyQt6 or PySide6 is not installed or could not be imported.",
            file=sys.stderr,
        )
        print(
            "Please ensure a supported Qt binding is installed: pip install PyQt6 or pip install PySide6",
            file=sys.stderr,
        )
        sys.exit(1)
    
    main()
