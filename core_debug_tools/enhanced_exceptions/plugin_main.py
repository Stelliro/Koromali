# Koromali/core_debug_tools/enhanced_exceptions/plugin_main.py
import sys
from utils.logger import log
from .exception_dialog import ExceptionDialog
from app_core.koromali_api import KoromaliPluginAPI

class EnhancedExceptionsPlugin:
    _instance = None

    def __init__(self, koromali_api: KoromaliPluginAPI, original_hook):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.original_excepthook = original_hook or sys.excepthook
        sys.excepthook = self.show_exception_dialog
        log.info("Enhanced Exception Reporter initialized and hook installed.")

    def show_exception_dialog(self, exc_type, exc_value, exc_tb):
        # Specifically ignore KeyboardInterrupt to allow clean exits via Ctrl+C.
        if issubclass(exc_type, KeyboardInterrupt):
            log.warning("KeyboardInterrupt caught and ignored by the main thread.")
            # Still call the original hook so it can be handled normally (e.g., exiting the app)
            self.original_excepthook(exc_type, exc_value, exc_tb)
            return

        log.critical("Unhandled exception caught by Enhanced Reporter:",
                     exc_info=(exc_type, exc_value, exc_tb))
        dialog = ExceptionDialog(exc_type, exc_value, exc_tb, self.main_window)
        dialog.exec()
        self.original_excepthook(exc_type, exc_value, exc_tb)

def initialize(koromali_api: KoromaliPluginAPI, original_hook=None):
    if EnhancedExceptionsPlugin._instance is None:
        EnhancedExceptionsPlugin._instance = EnhancedExceptionsPlugin(
            koromali_api, original_hook
        )
    return EnhancedExceptionsPlugin._instance