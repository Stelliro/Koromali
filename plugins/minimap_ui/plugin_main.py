# /plugins/minimap_ui/plugin_main.py
import os
from typing import Optional

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer

from app_core.koromali_api import KoromaliPluginAPI
from ui.editor_widget import EditorWidget, MiniMapWidget
from ui.widgets.advanced_minimap import AdvancedMinimap
from utils.logger import log


class MinimapPlugin:
    """
    A plugin that automatically adds a minimap side-panel to any open editor tab.
    """
    def __init__(self, api: KoromaliPluginAPI):
        """Initializes the MinimapPlugin."""
        self.api = api
        self.main_window = api.get_main_window()
        self.tab_widget = None # Will be set in deferred_setup
        QTimer.singleShot(0, self.deferred_setup)

    def deferred_setup(self):
        """
        Performs setup that depends on the main window's UI being fully constructed.
        """
        self.tab_widget = self.api.get_main_tab_widget()

        if not self.tab_widget:
            log.error("MinimapPlugin: Deferred setup failed. Could not get main tab widget.")
            return

        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        log.info("MinimapPlugin initialized and connected to tab changes.")

        # Handle the case where a tab is already open on startup
        if self.tab_widget.currentIndex() != -1:
            self.on_tab_changed(self.tab_widget.currentIndex())


    def on_tab_changed(self, indexx: int):
        """Handles the event triggered when the active tab is changed."""
        if not self.tab_widget:
            return
            
        widget = self.tab_widget.widget(indexx)

        # Check if the widget is an EditorWidget and doesn't already have a minimap
        if not isinstance(widget, EditorWidget) or getattr(widget, '_minimap_installed', False):
            return

        log.info(f"Adding minimap to editor tab: {self.tab_widget.tabText(indexx)}")
        minimap = self._create_minimap(widget)
        widget.install_side_panel_widget(minimap)
        # Mark the widget so we don't add the minimap again
        setattr(widget, '_minimap_installed', True)

    def _create_minimap(self, editor: EditorWidget) -> QWidget:
        """
        Creates the appropriate minimap widget based on the editor's content.
        """
        theme_manager = self.api.get_manager("theme")
        filepath = editor.filepath
        
        if filepath and (file_ext := os.path.splitext(filepath)[1].lower()) in AdvancedMinimap.PARSERS:
            log.debug(f"Creating AdvancedMinimap for {filepath}")
            return AdvancedMinimap(editor, theme_manager, file_ext)
        
        log.debug("Creating standard MiniMapWidget.")
        return MiniMapWidget(editor.text_area, theme_manager)

    def shutdown(self):
        """Performs cleanup when the plugin is being unloaded."""
        if self.tab_widget:
            try:
                self.tab_widget.currentChanged.disconnect(self.on_tab_changed)
                log.info("MinimapPlugin shutdown complete.")
            except TypeError:
                # Signal was already disconnected
                pass

def initialize(api: KoromaliPluginAPI) -> MinimapPlugin:
    """The entry point for the plugin."""
    return MinimapPlugin(api)