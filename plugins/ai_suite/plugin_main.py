# /plugins/ai_suite/plugin_main.py
import os
from functools import partial
from typing import List
from datetime import datetime

from PyQt6.QtWidgets import QMenu, QApplication, QMessageBox, QInputDialog
from PyQt6.QtCore import Qt, QTimer

try:
    import qtawesome as qta
except ImportError:
    qta = None

from app_core.koromali_api import KoromaliPluginAPI
from app_core import golden_rules

from .ai_studio_dialog import AIStudioDialog
from .new_ai_project_dialog import NewAIProjectDialog
from .persona_manager_dialog import PersonaManagerDialog
from utils.logger import log


class AISuitePlugin:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.studio_dialog_instance = None
        self.persona_dialog_instance = None

        tools_menu = self.api.get_menu("tools")
        if tools_menu:
            tools_menu.addSeparator()

        self.api.add_menu_action(
            menu_name="tools",
            text="AI Studio...",
            callback=self.show_studio_dialog,
            icon_name="fa5s.robot"
        )
        
        self.api.add_menu_action(
            menu_name="tools",
            text="Manage Personas & Rules...",
            callback=self.show_persona_manager_dialog,
            icon_name="fa5s.users-cog"
        )

        file_menu = self.api.get_menu("file")
        if file_menu and hasattr(self.main_window, "actions"):
            new_project_action = self.main_window.actions.get("create_project")
            self.api.add_menu_action(
                menu_name="file",
                text="New Project from AI...",
                callback=self._show_new_project_dialog,
                icon_name="fa5s.magic",
                insert_before=new_project_action
            )

    def show_studio_dialog(self):
        """Shows the AI Studio, creating it if necessary."""
        if self.studio_dialog_instance is None:
            self.studio_dialog_instance = AIStudioDialog(self.api, parent=self.main_window)
            self.studio_dialog_instance.finished.connect(self._on_studio_dialog_closed)
        self.studio_dialog_instance.show()
        self.studio_dialog_instance.activateWindow()
        self.studio_dialog_instance.raise_()

    def _on_studio_dialog_closed(self, result):
        self.studio_dialog_instance = None

    def show_persona_manager_dialog(self):
        """Shows the persona manager dialog."""
        if self.persona_dialog_instance is None:
            self.persona_dialog_instance = PersonaManagerDialog(
                self.api.get_theme_manager(),
                self.api.get_settings_manager(),
                parent=self.main_window
            )
            self.persona_dialog_instance.finished.connect(lambda: setattr(self, 'persona_dialog_instance', None))
        self.persona_dialog_instance.show()
        self.persona_dialog_instance.activateWindow()
        self.persona_dialog_instance.raise_()

    def _show_new_project_dialog(self):
        dialog = NewAIProjectDialog(self.main_window)
        dialog.exec()


def initialize(koromali_api: KoromaliPluginAPI) -> AISuitePlugin:
    """
    Required entry point for the plugin.
    
    Args:
        koromali_api: An instance of the KoromaliPluginAPI.
        
    Returns:
        An instance of the AISuitePlugin.
    """
    return AISuitePlugin(koromali_api)