# Koromali/plugins/theme_editor/theme_editor_dialog.py
import re
import datetime
import copy
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QWidget, QLabel, QLineEdit, QPushButton,
                             QDialogButtonBox, QScrollArea, QMessageBox,
                             QColorDialog, QListWidget, QListWidgetItem,
                             QSplitter, QFrame, QGroupBox)
from PyQt6.QtGui import QColor, QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from utils.logger import log


class ColorPickerButton(QPushButton):
    """A custom button that displays a color swatch and opens a color picker."""
    color_changed = pyqtSignal(str, QColor)

    def __init__(self, key_name: str, initial_color=QColor("black"), parent=None):
        super().__init__(parent)
        self.key_name = key_name
        self._color = QColor(initial_color)
        self.setFixedSize(QSize(130, 28))
        self.setIconSize(QSize(20, 20))
        self._update_swatch()
        self.clicked.connect(self._pick_color)

    def _update_swatch(self):
        pixmap = QPixmap(self.iconSize())
        pixmap.fill(self._color)
        self.setIcon(QIcon(pixmap))
        self.setText(self._color.name().upper())

    def set_color(self, new_color: QColor, from_picker=False):
        new_color = QColor(new_color)
        if self._color != new_color:
            self._color = new_color
            self._update_swatch()
            if from_picker:
                self.color_changed.emit(self.key_name, self._color)

    def get_color(self) -> QColor:
        return self._color

    def _pick_color(self):
        dialog = QColorDialog(self._color, self)
        if dialog.exec():
            self.set_color(dialog.currentColor(), from_picker=True)


class ThemeEditorDialog(QDialog):
    """A dialog for creating, editing, and deleting UI themes."""
    custom_themes_changed = pyqtSignal()

    def __init__(self, theme_manager, parent=None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        log.info("ThemeEditorDialog initializing...")
        self.setWindowTitle("Theme Customizer")
        self.setMinimumSize(QSize(950, 700))
        self.setModal(True)
        # Added missing color keys to ensure they appear in the editor UI.
        self.COLOR_GROUPS = {
            "Window & General": ["window.background", "sidebar.background", "accent", "icon.foreground"],
            "Editor": ["editor.background", "editor.foreground", "editor.selectionBackground",
                       "editor.lineHighlightBackground", "editor.userHighlightBackground",
                       "editor.breakpoint.color"],
            "Editor Gutter": ["editorGutter.background", "editorGutter.foreground",
                              "editorGutter.hoverBackground", "editorLineNumber.foreground",
                              "editorLineNumber.activeForeground", "gutter.activeLineNumberForeground"],
            "Editor Matching": ["editor.matchingBracketBackground", "editor.matchingBracketForeground"],
            "Controls": ["button.background", "button.foreground",
                         "input.background", "input.foreground", "input.border"],
            "Bars & Menus": ["statusbar.background", "statusbar.foreground",
                             "menu.background", "menu.foreground"],
            "Editor Tabs": ["tab.activeBackground", "tab.inactiveBackground",
                            "tab.activeForeground", "tab.inactiveForeground"],
            "Scrollbar": ["scrollbar.background", "scrollbar.handle",
                          "scrollbar.handleHover", "scrollbar.handlePressed"],
            "Syntax Highlighting": [
                "syntax.keyword", "syntax.operator", "syntax.brace",
                "syntax.decorator", "syntax.self", "syntax.className",
                "syntax.functionName", "syntax.comment", "syntax.string",
                "syntax.docstring", "syntax.number"
            ],
            "Git Status": [
                "git.added", "git.modified", "git.deleted",
                "git.status.foreground"
            ],
            "Tree & List View": [
                "tree.indentationGuides.stroke", "tree.trace.color",
                "tree.trace.shadow", "tree.node.color", "tree.node.fill",
                "list.hoverBackground", "list.activeSelectionBackground",
                "list.activeSelectionForeground", "list.inactiveSelectionBackground",
                "list.inactiveSelectionForeground"
            ]
        }
        self.current_theme_id = None
        self.is_custom_theme = False
        self.color_widgets = {}
        self.unsaved_changes = False
        self._setup_ui()
        self._repopulate_theme_list()
        self._update_ui_state()
        log.info("ThemeEditorDialog initialized successfully.")

    def _setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.main_layout.addWidget(self.splitter, 1)
        self._create_left_pane()
        self._create_right_pane()
        self.splitter.setSizes([240, 710])
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        self.button_box.rejected.connect(self.reject)
        self.main_layout.addWidget(self.button_box)

    def _create_left_pane(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(QLabel("<b>Available Themes:</b>"))
        self.theme_list_widget = QListWidget()
        self.theme_list_widget.setAlternatingRowColors(True)
        self.theme_list_widget.currentItemChanged.connect(
            self._on_theme_selection_changed
        )
        layout.addWidget(self.theme_list_widget, 1)
        actions_layout = QHBoxLayout()
        self.duplicate_button = QPushButton("Duplicate")
        self.delete_button = QPushButton("Delete")
        self.duplicate_button.clicked.connect(self._action_duplicate_theme)
        self.delete_button.clicked.connect(self._action_delete_theme)
        actions_layout.addWidget(self.duplicate_button)
        actions_layout.addWidget(self.delete_button)
        layout.addLayout(actions_layout)
        self.splitter.addWidget(container)

    def _create_right_pane(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(10, 5, 5, 5)
        form_layout = QGridLayout()
        form_layout.addWidget(QLabel("<b>Theme Name:</b>"), 0, 0)
        self.name_edit = QLineEdit()
        self.name_edit.textChanged.connect(self._mark_unsaved_changes)
        form_layout.addWidget(self.name_edit, 0, 1)
        self.info_label = QLabel()
        self.info_label.setStyleSheet("font-style: italic; color: grey;")
        form_layout.addWidget(self.info_label, 1, 1)
        form_layout.setColumnStretch(1, 1)
        layout.addLayout(form_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_content = QWidget()
        self.v_scroll_layout = QVBoxLayout(self.scroll_content)
        self.v_scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(self.scroll_content)
        layout.addWidget(scroll_area, 1)
        actions_layout = QHBoxLayout()
        self.reset_button = QPushButton("Reset Changes")
        self.update_button = QPushButton("Update Custom Theme")
        self.reset_button.clicked.connect(self._load_theme_to_editor)
        self.update_button.clicked.connect(self._action_save)
        actions_layout.addWidget(self.reset_button)
        actions_layout.addStretch()
        actions_layout.addWidget(self.update_button)
        layout.addLayout(actions_layout)
        self.splitter.addWidget(container)

    def _repopulate_theme_list(self, select_theme_id=None):
        self.theme_list_widget.blockSignals(True)
        self.theme_list_widget.clear()
        all_themes = self.theme_manager.get_available_themes_for_ui()
        target_row = 0
        current_selection = (select_theme_id or self.current_theme_id or
                             self.theme_manager.current_theme_id)
        for i, (theme_id, name) in enumerate(all_themes.items()):
            item = QListWidgetItem(name)
            item.setData(Qt.ItemDataRole.UserRole, theme_id)
            theme_data = self.theme_manager.all_themes_data.get(theme_id, {})
            if theme_data and theme_data.get("is_custom"):
                item.setFont(QFont(self.font().family(), -1, QFont.Weight.Bold))
            self.theme_list_widget.addItem(item)
            if theme_id == current_selection:
                target_row = i
        self.theme_list_widget.setCurrentRow(target_row)
        self.theme_list_widget.blockSignals(False)
        self._on_theme_selection_changed(
            self.theme_list_widget.currentItem(), None
        )

    def _on_theme_selection_changed(self, current, previous):
        if not current:
            self._clear_editor()
            return

        if self.unsaved_changes and current is not previous:
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                "Discard changes to the previous theme?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                self.theme_list_widget.blockSignals(True)
                if previous:
                    self.theme_list_widget.setCurrentItem(previous)
                self.theme_list_widget.blockSignals(False)
                return

        new_theme_id = current.data(Qt.ItemDataRole.UserRole)
        if new_theme_id != self.current_theme_id:
            self.current_theme_id = new_theme_id
            self._load_theme_to_editor()

    def _load_theme_to_editor(self):
        theme_data = self.theme_manager.all_themes_data.get(self.current_theme_id, {})
        if not theme_data or "colors" not in theme_data:
            self._clear_editor()
            return

        self._clear_layout(self.v_scroll_layout)
        self.color_widgets.clear()

        self.is_custom_theme = theme_data.get("is_custom", False)
        self.name_edit.setText(theme_data.get("name", ""))
        self.name_edit.setReadOnly(not self.is_custom_theme)
        self.info_label.setText(f"Author: {theme_data.get('author', 'N/A')}")

        all_color_keys = theme_data["colors"].keys()
        sorted_keys = sorted(all_color_keys)

        for group_name, prefixes in self.COLOR_GROUPS.items():
            group_keys = [k for k in sorted_keys if
                          any(k.startswith(p) for p in prefixes)]
            if not group_keys:
                continue

            group_box = QGroupBox(group_name)
            grid = QGridLayout(group_box)
            grid.setSpacing(5)
            row, col = 0, 0
            for key in group_keys:
                color_val = QColor(theme_data["colors"].get(key, '#ff00ff'))
                picker = ColorPickerButton(key, color_val)
                picker.setEnabled(self.is_custom_theme)
                picker.color_changed.connect(self._mark_unsaved_changes)
                self.color_widgets[key] = picker
                grid.addWidget(QLabel(f"{key.split('.')[-1]}:"), row, col)
                grid.addWidget(picker, row, col + 1)
                col += 2
                if col >= 4:
                    col = 0
                    row += 1
            self.v_scroll_layout.addWidget(group_box)

        self.v_scroll_layout.addStretch()
        self.unsaved_changes = False
        self._update_ui_state()

    def _action_duplicate_theme(self):
        if not self.current_theme_id:
            return
        original_theme = copy.deepcopy(
            self.theme_manager.all_themes_data.get(self.current_theme_id)
        )
        if not original_theme:
            return

        new_name = f"{original_theme.get('name', 'New Theme')} (Copy)"
        safe_name = re.sub(r'[^a-z0-9_]', '', new_name.lower())
        timestamp = int(datetime.datetime.now().timestamp())
        new_id = f"custom_{safe_name}_{timestamp}"

        original_theme['name'] = new_name
        original_theme['author'] = "Koromali User"
        original_theme['is_custom'] = True

        self.theme_manager.add_or_update_custom_theme(new_id, original_theme)
        self.custom_themes_changed.emit()
        self._repopulate_theme_list(select_theme_id=new_id)

    def _action_delete_theme(self):
        if not self.current_theme_id or not self.is_custom_theme:
            return
        theme_data = self.theme_manager.all_themes_data.get(self.current_theme_id)
        theme_name = theme_data.get('name', self.current_theme_id)
        reply = QMessageBox.question(
            self, "Confirm Delete",
            f"Are you sure you want to delete the theme '{theme_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.theme_manager.delete_custom_theme(self.current_theme_id)
            self.custom_themes_changed.emit()
            if self.current_theme_id == self.theme_manager.current_theme_id:
                self.theme_manager.set_theme("Koromali_dark")
            self._repopulate_theme_list(select_theme_id="Koromali_dark")

    def _action_save(self):
        if not self.is_custom_theme or not self.unsaved_changes:
            return
        theme_data = copy.deepcopy(
            self.theme_manager.all_themes_data.get(self.current_theme_id)
        )
        theme_data['name'] = self.name_edit.text()
        for key, widget in self.color_widgets.items():
            theme_data['colors'][key] = widget.get_color().name()

        self.theme_manager.add_or_update_custom_theme(self.current_theme_id, theme_data)
        self.custom_themes_changed.emit()
        self.unsaved_changes = False
        self._update_ui_state()
        if self.current_theme_id == self.theme_manager.current_theme_id:
            self.theme_manager.set_theme(self.current_theme_id)
        QMessageBox.information(
            self, "Success", f"Theme '{theme_data['name']}' has been updated."
        )

    def _mark_unsaved_changes(self, *args):
        if self.is_custom_theme:
            self.unsaved_changes = True
            self._update_ui_state()

    def _update_ui_state(self):
        has_selection = self.current_theme_id is not None
        can_edit = self.is_custom_theme
        self.name_edit.setEnabled(can_edit)
        self.reset_button.setEnabled(can_edit and self.unsaved_changes)
        self.update_button.setEnabled(can_edit and self.unsaved_changes)
        self.delete_button.setEnabled(can_edit)
        self.duplicate_button.setEnabled(has_selection)
        for widget in self.color_widgets.values():
            widget.setEnabled(can_edit)

    def _clear_layout(self, layout):
        if layout is None:
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout is not None:
                    self._clear_layout(sub_layout)

    def _clear_editor(self):
        self._clear_layout(self.v_scroll_layout)
        self.name_edit.clear()
        self.info_label.clear()
        self.current_theme_id = None
        self.is_custom_theme = False
        self.unsaved_changes = False
        self._update_ui_state()

    def reject(self):
        if self.unsaved_changes:
            reply = QMessageBox.question(
                self, "Unsaved Changes", "Discard changes and close?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                super().reject()
        else:
            super().reject()