# /ui/widgets/find_panel.py
from typing import Optional, TYPE_CHECKING
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLineEdit,
                             QPushButton, QCheckBox, QToolButton, QFrame, QApplication)
from PyQt6.QtGui import QTextDocument, QKeyEvent
from PyQt6.QtCore import Qt, pyqtSignal
import qtawesome as qta


if TYPE_CHECKING:
    from ..editor_widget import EditorWidget
    from app_core.theme_manager import ThemeManager
    from app_core.settings_manager import SettingsManager


class FindPanel(QFrame):
    """An integrated panel for find and replace operations."""
    close_requested = pyqtSignal()
    status_message_requested = pyqtSignal(str, int)
    find_in_project_requested = pyqtSignal(str, object)
    replace_in_project_requested = pyqtSignal(str, str, object)

    def __init__(self, theme_manager: "ThemeManager", settings_manager: "SettingsManager", parent: QWidget):
        super().__init__(parent)
        self.editor: Optional["EditorWidget"] = None
        self.theme_manager = theme_manager
        self.settings_manager = settings_manager
        self.setObjectName("FindPanelFrame")
        self._setup_ui()
        self._connect_signals()
        self.load_settings()
        self.update_theme()

    def _setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.main_layout.setSpacing(5)

        find_layout = QHBoxLayout()
        self.toggle_button = QToolButton()
        self.toggle_button.setCheckable(True)
        self.toggle_button.setAutoRaise(True)
        self.toggle_button.setIcon(qta.icon('mdi.chevron-right'))
        find_layout.addWidget(self.toggle_button)

        self.find_input = QLineEdit()
        self.find_input.setPlaceholderText("Find")
        find_layout.addWidget(self.find_input)

        self.find_prev_button = self._create_tool_button(
            'mdi.arrow-up', "Find Previous (Shift+F3)")
        self.find_next_button = self._create_tool_button(
            'mdi.arrow-down', "Find Next (F3)")
        self.find_all_button = self._create_tool_button(
            'mdi.folder-search-outline', "Find All in Project")
        self.close_button = self._create_tool_button(
            'mdi.close', "Close (Esc)")

        find_layout.addWidget(self.find_prev_button)
        find_layout.addWidget(self.find_next_button)
        find_layout.addWidget(self.find_all_button)
        find_layout.addWidget(self.close_button)
        self.main_layout.addLayout(find_layout)

        self.expandable_widget = QWidget()
        expandable_layout = QVBoxLayout(self.expandable_widget)
        expandable_layout.setContentsMargins(0, 5, 0, 0)
        expandable_layout.setSpacing(5)

        replace_layout = QHBoxLayout()
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Replace")
        self.replace_button = self._create_tool_button(
            'mdi.find-replace', "Replace", text="Replace")
        self.replace_all_button = self._create_tool_button(
            'mdi.auto-fix',
            "Replace all in current file.\nHold Ctrl to replace in all project files.",
            text="All"
        )
        replace_layout.addWidget(self.replace_input)
        replace_layout.addWidget(self.replace_button)
        replace_layout.addWidget(self.replace_all_button)
        expandable_layout.addLayout(replace_layout)

        options_layout = QHBoxLayout()
        options_layout.setContentsMargins(25, 0, 0, 0)
        self.case_checkbox = QCheckBox("Case Sensitive")
        self.whole_word_checkbox = QCheckBox("Whole Word")
        options_layout.addWidget(self.case_checkbox)
        options_layout.addWidget(self.whole_word_checkbox)
        options_layout.addStretch()
        expandable_layout.addLayout(options_layout)

        self.main_layout.addWidget(self.expandable_widget)
        self.expandable_widget.hide()

    def _create_tool_button(
            self, icon_name: str, tooltip: str, text: Optional[str] = None
    ) -> QToolButton:
        button = QToolButton()
        button.setAutoRaise(True)
        button.setToolTip(tooltip)
        button.setProperty("icon_name", icon_name)
        if text:
            button.setText(text)
            button.setToolButtonStyle(
                Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        return button

    def _connect_signals(self):
        self.close_button.clicked.connect(self.close_requested.emit)
        self.toggle_button.toggled.connect(self.expandable_widget.setVisible)
        self.find_input.textChanged.connect(self._update_button_states)
        self.find_input.returnPressed.connect(self.find_next_button.click)
        self.find_next_button.clicked.connect(
            lambda: self._find(backwards=False))
        self.find_prev_button.clicked.connect(
            lambda: self._find(backwards=True))
        self.find_all_button.clicked.connect(self._on_find_all_in_project)
        self.replace_button.clicked.connect(self._replace)
        self.replace_all_button.clicked.connect(self._replace_all)

    def connect_editor(self, editor: "EditorWidget"):
        self.editor = editor
        initial_text = editor.text_area.textCursor().selectedText()
        if initial_text:
            self.find_input.setText(initial_text)
        self.focus_find_input()
        self._update_button_states()

    def focus_find_input(self):
        self.find_input.setFocus()
        self.find_input.selectAll()

    def update_theme(self):
        colors = self.theme_manager.current_theme_data['colors']
        frame_bg = colors.get('sidebar.background', '#333')
        self.setStyleSheet(
            f"#FindPanelFrame {{ background-color: {frame_bg}; "
            f"border-bottom: 1px solid {colors.get('input.border')}; }}")
        for button in self.findChildren((QToolButton, QPushButton)):
            if icon_name := button.property("icon_name"):
                button.setIcon(qta.icon(icon_name))

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            self.close_requested.emit()
            return
        super().keyPressEvent(event)

    def load_settings(self):
        self.case_checkbox.setChecked(
            self.settings_manager.get("search_case_sensitive", False))
        self.whole_word_checkbox.setChecked(
            self.settings_manager.get("search_whole_word", False))

    def save_settings(self):
        self.settings_manager.set(
            "search_case_sensitive", self.case_checkbox.isChecked())
        self.settings_manager.set(
            "search_whole_word", self.whole_word_checkbox.isChecked())

    def _update_button_states(self):
        has_text = bool(self.find_input.text())
        is_project_open = self.editor and self.editor.koromali_api.get_manager("project").is_project_open()
        
        self.find_next_button.setEnabled(has_text)
        self.find_prev_button.setEnabled(has_text)
        self.find_all_button.setEnabled(has_text and is_project_open)
        self.replace_button.setEnabled(has_text)
        self.replace_all_button.setEnabled(has_text)

    def _get_find_flags(self) -> QTextDocument.FindFlag:
        flags = QTextDocument.FindFlag(0)
        if self.case_checkbox.isChecked():
            flags |= QTextDocument.FindFlag.FindCaseSensitively
        if self.whole_word_checkbox.isChecked():
            flags |= QTextDocument.FindFlag.FindWholeWords
        return flags

    def _on_find_all_in_project(self):
        query = self.find_input.text()
        if not query:
            return
        flags = self._get_find_flags()
        self.find_in_project_requested.emit(query, flags)

    def _find(self, backwards: bool = False):
        if not self.editor:
            return
        query = self.find_input.text()
        flags = self._get_find_flags()
        if backwards:
            flags |= QTextDocument.FindFlag.FindBackward
        if not self.editor.find_next(query, flags):
            self.status_message_requested.emit(
                f"No more occurrences of '{query}' found.", 2000)
        self.save_settings()

    def _replace(self):
        if not self.editor:
            return
        query = self.find_input.text()
        replace_text = self.replace_input.text()
        flags = self._get_find_flags()
        if not self.editor.replace_current(query, replace_text, flags):
            self.status_message_requested.emit(
                "Nothing selected to replace.", 2000)
        self.save_settings()

    def _replace_all(self):
        if not self.editor:
            return
        
        query = self.find_input.text()
        replace_text = self.replace_input.text()
        flags = self._get_find_flags()
        
        # Check for Ctrl key modifier
        if QApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier:
            self.replace_in_project_requested.emit(query, replace_text, flags)
            return

        count = self.editor.replace_all(query, replace_text, flags)
        self.save_settings()
        self.status_message_requested.emit(
            f"Replaced {count} occurrence(s) in current file.", 3000)