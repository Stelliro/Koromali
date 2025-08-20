# Koromali/core_debug_tools/enhanced_exceptions/exception_dialog.py
import traceback
import platform
import sys
from urllib.parse import quote_plus
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QTextEdit, QLabel,
                             QDialogButtonBox, QApplication)
from PyQt6.QtGui import QFont, QDesktopServices
from PyQt6.QtCore import QUrl
from utils.versioning import APP_VERSION
from utils.logger import log


class ExceptionDialog(QDialog):
    """A dialog to display unhandled exceptions with developer-friendly actions."""

    def __init__(self, exc_type, exc_value, exc_tb, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Koromali - Unhandled Exception")
        self.setMinimumSize(700, 500)

        # Format the traceback
        tb_list = traceback.format_exception(exc_type, exc_value, exc_tb)
        self.traceback_text = "".join(tb_list)
        self.exception_type = exc_type.__name__
        self.system_info = (
            f"Koromali Version: {APP_VERSION}\n"
            f"Python Version: {sys.version.split()[0]}\n"
            f"Platform: {platform.system()} {platform.release()}"
        )
        self.full_report_display = (
            "--- System Information ---\n"
            f"{self.system_info}\n\n"
            "--- Traceback ---\n"
            f"{self.traceback_text}"
        )

        # UI Setup
        layout = QVBoxLayout(self)
        label = QLabel(
            "An unexpected error occurred. You can help improve Koromali "
            "by reporting this issue on GitHub."
        )
        label.setWordWrap(True)
        layout.addWidget(label)

        self.details_box = QTextEdit()
        self.details_box.setReadOnly(True)
        self.details_box.setFont(QFont("Consolas", 10))
        self.details_box.setText(self.full_report_display)
        layout.addWidget(self.details_box)

        self.button_box = QDialogButtonBox()
        copy_button = self.button_box.addButton(
            "Copy Details", QDialogButtonBox.ButtonRole.ActionRole
        )
        report_button = self.button_box.addButton(
            "Report on GitHub", QDialogButtonBox.ButtonRole.HelpRole
        )
        quit_button = self.button_box.addButton(
            "Quit Application", QDialogButtonBox.ButtonRole.DestructiveRole
        )

        copy_button.clicked.connect(self._copy_to_clipboard)
        report_button.clicked.connect(self._open_github_issues)
        quit_button.clicked.connect(self._force_quit_app)

        layout.addWidget(self.button_box)

    def _copy_to_clipboard(self):
        """Copies the full report to the clipboard."""
        QApplication.clipboard().setText(self.full_report_display)
        self.details_box.selectAll()

    def _open_github_issues(self):
        """Opens a new issue on GitHub with pre-filled information."""
        issue_title = quote_plus(f"Crash Report: {self.exception_type}")
        issue_body_template = """
**Describe the bug**
A clear and concise description of what the bug is. What were you doing when the crash occurred?

**Steps to Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Automatic Crash Report Details**

---
<details>
<summary>Click to expand</summary>

```
{traceback}
```

</details>
""".format(traceback=self.full_report_display)

        issue_body = quote_plus(issue_body_template.strip())

        url = QUrl(
            f"https://github.com/Stelliro/Koromali/issues/new?title="
            f"{issue_title}&body={issue_body}"
        )
        QDesktopServices.openUrl(url)

    def _force_quit_app(self):
        """A failsafe to ensure the application quits immediately."""
        log.warning("Force quit initiated from exception dialog.")
        QApplication.instance().quit()