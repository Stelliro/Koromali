# /core_debug_tools/plugin_initializer/plugin_main.py
import os
import json
from PyQt6.QtWidgets import QMessageBox

from app_core.koromali_api import KoromaliPluginAPI
from utils.helpers import get_base_path
from utils.logger import log
from .new_plugin_dialog import NewPluginDialog

# Boilerplate content for the new plugin's main Python file
PLUGIN_MAIN_BOILERPLATE = """
from app_core.koromali_api import KoromaliPluginAPI
from utils.logger import log

class {class_name}:
    \"\"\"
    Main class for the {plugin_name} plugin.
    \"\"\"
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        
        # TODO: Add your plugin's initialization logic here.
        # This is a good place to add menu items, connect signals, etc.
        #
        # Example:
        # self.api.add_menu_action(
        #     menu_name="tools",
        #     text="{plugin_name}",
        #     callback=self.say_hello,
        #     icon_name="fa5s.hand-spock"
        # )
        
        log.info("{plugin_name} plugin initialized.")

    def say_hello(self):
        self.api.show_message("info", "{plugin_name}", "Hello from your new plugin!")
        
    def shutdown(self):
        \"\"\"
        (Optional) Called by the editor when the plugin is being unloaded.
        Use this to clean up resources, like disconnecting signals or removing UI.
        \"\"\"
        log.info("{plugin_name} is shutting down.")


def initialize(koromali_api: KoromaliPluginAPI):
    \"\"\"
    Entry point for the plugin. Koromali calls this to create an
    instance of your plugin.
    \"\"\"
    return {class_name}(koromali_api)

"""

class PluginInitializer:
    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api
        self.main_window = self.api.get_main_window()
        self.base_plugins_path = os.path.join(get_base_path(), 'plugins')
        
        # Add the action to the 'Tools' menu
        self.api.add_menu_action(
            menu_name="tools",
            text="Create New Plugin...",
            callback=self.show_creation_dialog,
            icon_name="fa5s.magic"
        )
        log.info("Plugin Initializer is ready.")
        
    def show_creation_dialog(self):
        """Shows the dialog to get details for the new plugin."""
        dialog = NewPluginDialog(self.main_window)
        if dialog.exec():
            plugin_data = dialog.get_plugin_data()
            self._create_plugin_scaffold(plugin_data)

    def _create_plugin_scaffold(self, data: dict):
        """Creates the necessary directory and files for the new plugin."""
        plugin_id = data.get('id')
        plugin_path = os.path.join(self.base_plugins_path, plugin_id)

        try:
            # 1. Validate: Check if directory already exists
            if os.path.exists(plugin_path):
                self.api.show_message(
                    "critical", "Plugin Exists",
                    f"A plugin with the ID '{plugin_id}' already exists at:\n{plugin_path}"
                )
                return

            # 2. Create Directory Structure
            log.info(f"Creating plugin directory at: {plugin_path}")
            os.makedirs(plugin_path)

            # 3. Create __init__.py
            with open(os.path.join(plugin_path, '__init__.py'), 'w', encoding='utf-8') as f:
                f.write("# This file makes this directory a Python package.\n")
                
            # 4. Create plugin.json
            json_path = os.path.join(plugin_path, 'plugin.json')
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indexnt=4)

            # 5. Create plugin_main.py
            main_py_path = os.path.join(plugin_path, data['entry_point'])
            class_name = data['name'].replace(' ', '') + "Plugin" # e.g., MyAwesomeToolsPlugin
            
            boilerplate = PLUGIN_MAIN_BOILERPLATE.format(
                class_name=class_name,
                plugin_name=data['name']
            )
            with open(main_py_path, 'w', encoding='utf-8') as f:
                f.write(boilerplate)

            log.info("Plugin scaffold created successfully.")
            self._on_creation_success(data, main_py_path)
        
        except Exception as e:
            log.error(f"Failed to create plugin scaffold for '{plugin_id}': {e}", exc_info=True)
            self.api.show_message("critical", "Creation Failed", f"An unexpected error occurred:\n{e}")

    def _on_creation_success(self, data: dict, main_py_path: str):
        """Handles post-creation steps, like showing a success message."""
        reply = QMessageBox.information(
            self.main_window,
            "Plugin Created",
            f"Successfully created the '{data['name']}' plugin.\n\n"
            "Would you like to open its main file to start editing?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.main_window._action_open_file(main_py_path)
            
        # Notify user that a reload/restart is needed to see the plugin in menus etc.
        self.api.show_status_message(
            "Reload required to see new plugin in Preferences list.", 5000
        )


def initialize(koromali_api: KoromaliPluginAPI):
    """Entry point for the Plugin Initializer tool."""
    return PluginInitializer(koromali_api)