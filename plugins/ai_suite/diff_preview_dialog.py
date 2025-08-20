# /plugins/ai_suite/diff_preview_dialog.py
import difflib
import traceback
import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTextEdit, QDialogButtonBox, QMessageBox
)
from PyQt6.QtGui import QFont, QTextCursor, QColor, QTextCharFormat
from .response_parser import apply_patch
from utils.logger import log

class DiffPreviewDialog(QDialog):
    """A dialog to show a diff and apply a patch, with detailed error reporting."""

    def __init__(self, file_path: str, original_content: str, patch_content: str, parent=None):
        super().__init__(parent)
        self.file_path = file_path
        self.original_content = original_content
        self.patch_content = patch_content
        self.new_content = ""

        self.setWindowTitle(f"Apply Patch to: {os.path.basename(file_path)}")
        self.setMinimumSize(900, 700)

        layout = QVBoxLayout(self)

        self.diff_view = QTextEdit()
        self.diff_view.setReadOnly(True)
        self.diff_view.setFont(QFont("Monospace", 10))
        self.diff_view.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        layout.addWidget(self.diff_view)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Cancel
        )
        self.button_box.button(QDialogButtonBox.StandardButton.Apply).setText("Apply Patch")
        layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self._apply_changes)
        self.button_box.rejected.connect(self.reject)

        self._generate_and_show_diff()

    def _generate_and_show_diff(self):
        """Generates a unified diff and displays it with syntax highlighting."""
        try:
            self.new_content = apply_patch(self.original_content, self.patch_content)
            diff_lines = difflib.unified_diff(
                self.original_content.splitlines(),
                self.new_content.splitlines(),
                fromfile=f"a/{os.path.basename(self.file_path)}",
                tofile=f"b/{os.path.basename(self.file_path)}"
            )
            self.diff_view.clear()
            cursor = self.diff_view.textCursor()
            
            for line in diff_lines:
                fmt = QTextCharFormat()
                if line.startswith('+'):
                    fmt.setBackground(QColor("#aaffaa"))
                elif line.startswith('-'):
                    fmt.setBackground(QColor("#ffaaaa"))
                elif line.startswith('@@'):
                    fmt.setForeground(QColor("blue"))
                
                cursor.insertText(line + '\n', fmt)
            
            self.diff_view.moveCursor(QTextCursor.MoveOperation.Start)

        except Exception as e:
            log.error(f"Could not generate diff for {self.file_path}: {e}", exc_info=True)
            self.diff_view.setPlainText(f"Error applying patch to generate preview:\n\n{e}")
            self.button_box.button(QDialogButtonBox.StandardButton.Apply).setEnabled(False)

    def _apply_changes(self):
        """Applies the patch to the actual file."""
        try:
            # Create directory if it doesn't exist (for new files)
            if not os.path.exists(os.path.dirname(self.file_path)):
                os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            
            with open(self.file_path, "w", encoding="utf-8", newline='\n') as f:
                f.write(self.new_content)
            log.info(f"Successfully patched file: {self.file_path}")
            self.accept()
        except Exception as e:
            log.error(f"Failed to write patched file {self.file_path}: {e}", exc_info=True)
            error_msg = (
                f"<b>Could not write changes to <code>{os.path.basename(self.file_path)}</code>.</b>\n\n"
                "This could be a permissions issue, or an error in the patch from the AI."
            )
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("File Write Error")
            msg_box.setText(error_msg)
            msg_box.setDetailedText(f"File: {self.file_path}\n\nError:\n{e}\n\nTraceback:\n{traceback.format_exc()}")
            msg_box.exec()