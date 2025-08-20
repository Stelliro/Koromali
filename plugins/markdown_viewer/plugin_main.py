# /plugins/markdown_viewer/plugin_main.py
import os
from .markdown_editor_widget import MarkdownEditorWidget
from utils.logger import log
from app_core.koromali_api import KoromaliPluginAPI


class MarkdownPlugin:
    """
    Manages the lifecycle and functionality of the Markdown Editor plugin.
    Provides a dual-pane editor with live preview for Markdown files.
    """

    def __init__(self, koromali_api: KoromaliPluginAPI):
        self.api = koromali_api

        # Register our custom editor widget as the handler for .md files
        # The handler is expected to return a widget instance for the main window to manage.
        self.api.register_file_opener('.md', self.open_markdown_editor)
        log.info("Markdown Editor: Registered dual-pane handler for .md files.")

    def open_markdown_editor(self, filepath: str, content: str) -> MarkdownEditorWidget:
        """
        Callback to create and return our custom MarkdownEditorWidget.

        The MainWindow will be responsible for adding it to the tab widget. This
        method accepts pre-read content to avoid redundant file I/O.
        """
        log.info(f"Markdown Editor: Creating new dual-pane view for '{filepath}'.")

        # Create the widget with the main window as its parent
        editor = MarkdownEditorWidget(
            koromali_api=self.api,
            parent=self.api.get_main_window()
        )

        # Use a new method to set the content directly
        editor.set_initial_content(filepath, content)

        # Connect its changed signal to the main window's handler
        editor.content_changed.connect(
            lambda: self.api.get_main_window()._on_content_changed(editor)
        )

        return editor


def initialize(koromali_api: KoromaliPluginAPI):
    """
    Entry point for Koromali to load the plugin.
    """
    try:
        plugin_instance = MarkdownPlugin(koromali_api)
        log.info("Markdown Editor Plugin (dual-pane) initialized successfully.")
        return plugin_instance
    except Exception as e:
        log.error(f"Failed to initialize Markdown Editor Plugin: {e}", exc_info=True)
        return None