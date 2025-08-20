# /plugins/live_share_studio/editor_integration.py
from typing import Dict
from PyQt6.QtCore import QObject, QTimer, pyqtSlot
from PyQt6.QtWidgets import QWidget, QMessageBox

from app_core.koromali_api import KoromaliPluginAPI
from .collaboration_client import CollaborationClient
from .remote_cursor_widget import RemoteCursorWidget
from utils.helpers import generate_unified_diff

class EditorIntegration(QObject):
    """Manages interaction between the client and editor widgets."""

    def __init__(self, api: KoromaliPluginAPI, client: CollaborationClient):
        super().__init__()
        self.api = api
        self.client = client
        self.main_window = api.get_main_window()
        self.active_editors: Dict[QWidget, RemoteCursorWidget] = {}
        self._is_applying_remote_change = False
        self.current_editor = None

        self._connect_signals()

    def _connect_signals(self):
        self.client.text_update_received.connect(self._apply_remote_text_change)
        # self.client.cursor_update_received.connect(self._apply_remote_cursor_change)
        # self.client.file_locked_received.connect(self._handle_file_lock)
        # self.client.file_unlocked_received.connect(self._handle_file_unlock)
        self.main_window.tab_widget.currentChanged.connect(self._on_tab_changed)
        QTimer.singleShot(100, lambda: self._on_tab_changed(self.main_window.tab_widget.currentIndex()))

    def shutdown(self):
        self.client.text_update_received.disconnect(self._apply_remote_text_change)
        self.main_window.tab_widget.currentChanged.disconnect(self._on_tab_changed)
        if self.current_editor:
            self.current_editor.text_area.textChanged.disconnect(self._on_local_text_changed)

    def _on_tab_changed(self, index: int):
        # Detach from old editor
        if self.current_editor and hasattr(self.current_editor, 'text_area'):
            try:
                self.current_editor.text_area.textChanged.disconnect(self._on_local_text_changed)
            except TypeError:
                pass # Already disconnected

        # Attach to new editor
        new_widget = self.main_window.tab_widget.widget(index)
        if hasattr(new_widget, 'text_area') and hasattr(new_widget, 'filepath'):
            self.current_editor = new_widget
            self.current_editor.text_area.textChanged.connect(self._on_local_text_changed)
        else:
            self.current_editor = None

    def _on_local_text_changed(self):
        if self._is_applying_remote_change or not self.current_editor: return
        
        filepath = self.current_editor.filepath
        if not filepath: return
        
        current_content = self.current_editor.get_text()
        original_content = self.main_window.editor_tabs_data[self.current_editor]['original_content_for_diff']
        
        if current_content != original_content:
            diff = generate_unified_diff(original_content, current_content, fromfile=filepath, tofile=filepath)
            
            payload = {
                "file_path": filepath,
                "diff": diff
            }
            self.client.send_message("text_update", payload)
            
            # Update the base content for the next diff
            self.main_window.editor_tabs_data[self.current_editor]['original_content_for_diff'] = current_content

    @pyqtSlot(dict)
    def _apply_remote_text_change(self, change_data: dict):
        self._is_applying_remote_change = True
        try:
            file_path = change_data.get("file_path")
            diff_text = change_data.get("diff")

            # Find the editor for the file
            target_editor = None
            for i in range(self.main_window.tab_widget.count()):
                widget = self.main_window.tab_widget.widget(i)
                if hasattr(widget, 'filepath') and widget.filepath == file_path:
                    target_editor = widget
                    break
            
            if not target_editor:
                # File is not open, maybe prompt user to open it? For now, we ignore.
                return

            original_content = target_editor.get_text()
            # Simple patch application logic (can be improved)
            # This assumes a very simple diff format for now
            # A proper implementation would use a diff/patch library
            new_content = original_content # Placeholder
            lines = original_content.splitlines()
            diff_lines = diff_text.splitlines()[2:] # Skip --- and +++ lines
            
            # This is a highly simplified patch logic and should be replaced
            # by a proper library in a real application.
            # For now, it will just replace the whole content for demonstration.
            # TODO: Implement robust patching.
            patched_lines = []
            original_line_idx = 0
            for line in diff_lines:
                if line.startswith('+'):
                    patched_lines.append(line[1:])
                elif line.startswith('-'):
                    original_line_idx += 1 # Skip this line
                elif line.startswith(' '):
                    patched_lines.append(line[1:])
                    original_line_idx += 1
                elif line.startswith('@@'):
                    continue

            new_content = "\n".join(patched_lines)

            target_editor.set_text(new_content)
            # Update the base content for next local diff
            self.main_window.editor_tabs_data[target_editor]['original_content_for_diff'] = new_content
            
        finally:
            self._is_applying_remote_change = False