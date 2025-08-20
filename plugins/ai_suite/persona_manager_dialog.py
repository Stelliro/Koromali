# /plugins/ai_suite/persona_manager_dialog.py
import os
import re
import json
import shutil
import importlib.util
from typing import Dict, List, Any, TYPE_CHECKING
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTabWidget, QWidget, QSplitter,
    QListWidget, QListWidgetItem, QGroupBox, QFormLayout, QLineEdit,
    QPlainTextEdit, QPushButton, QDialogButtonBox, QMessageBox,
    QLabel, QHBoxLayout, QInputDialog, QTextEdit
)
from PyQt6.QtGui import QFont, QTextCursor
from PyQt6.QtCore import Qt

try:
    import qtawesome as qta
except ImportError:
    qta = None

from app_core.highlighters.python_syntax_highlighter import PythonSyntaxHighlighter
from utils.logger import log
from utils.helpers import get_base_path
from .style_preset_manager import StylePresetManager
from app_core import golden_rules

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager
    from app_core.theme_manager import ThemeManager

PERSONA_TEMPLATE = """
# /assets/ai_personas/{file_name}.py
import os

def get_persona_info():
    \"\"\"
    {description}
    \"\"\"
    return {{
        "id": os.path.splitext(os.path.basename(__file__))[0],
        "name": "{name}",
        "expertise": "{expertise}",
        "system_prompt": '''{system_prompt_logic}'''
    }}

"""


class PersonaManagerDialog(QDialog):
    """A dialog for managing AI Personas and Style Presets."""
    def __init__(self, theme_manager: "ThemeManager", settings_manager: "SettingsManager", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Manage Personas & Rules")
        self.setMinimumSize(900, 700)
        self.theme_manager = theme_manager
        self.settings_manager = settings_manager
        self.preset_manager = StylePresetManager()
        self.main_layout = QVBoxLayout(self)
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        self.tab_widget.addTab(self._create_personas_tab(), "Personas")
        self.tab_widget.addTab(self._create_style_presets_tab(), "Style Presets")
        self.tab_widget.addTab(self._create_golden_rules_tab(), "Golden Rules")
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        button_box.rejected.connect(self.reject)
        self.main_layout.addWidget(button_box)
        self.update_theme()
        
    def _create_personas_tab(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        splitter = QSplitter()
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.addWidget(QLabel("<b>Personas:</b>"))
        self.personas_list = QListWidget()
        self.personas_list.currentItemChanged.connect(self._on_persona_selected)
        left_layout.addWidget(self.personas_list)

        persona_actions = QHBoxLayout()
        self.new_persona_button = QPushButton("New...")
        self.delete_persona_button = QPushButton("Delete")
        persona_actions.addWidget(self.new_persona_button)
        persona_actions.addWidget(self.delete_persona_button)
        left_layout.addLayout(persona_actions)
        splitter.addWidget(left_widget)

        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        self.persona_editor_edit = QPlainTextEdit()
        self.persona_editor_edit.setFont(QFont("Consolas", 10))
        self.persona_highlighter = PythonSyntaxHighlighter(self.persona_editor_edit.document(), self.theme_manager)
        right_layout.addWidget(self.persona_editor_edit)
        
        save_layout = QHBoxLayout()
        save_layout.addStretch()
        self.save_persona_button = QPushButton("Save Persona File")
        self.save_persona_button.clicked.connect(self._action_save_persona)
        save_layout.addWidget(self.save_persona_button)
        right_layout.addLayout(save_layout)
        
        splitter.addWidget(right_widget)
        layout.addWidget(splitter)

        self.new_persona_button.clicked.connect(self._action_new_persona)
        self.delete_persona_button.clicked.connect(self._action_delete_persona)

        self._populate_personas_list()
        return tab

    def _create_style_presets_tab(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        splitter = QSplitter()
        
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.addWidget(QLabel("<b>Style Presets:</b>"))
        self.presets_list = QListWidget()
        self.presets_list.currentItemChanged.connect(self._on_preset_selected)
        left_layout.addWidget(self.presets_list)

        preset_actions = QHBoxLayout()
        self.new_preset_button = QPushButton("New...")
        self.delete_preset_button = QPushButton("Delete")
        preset_actions.addWidget(self.new_preset_button)
        preset_actions.addWidget(self.delete_preset_button)
        left_layout.addLayout(preset_actions)
        splitter.addWidget(left_widget)

        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        form_group = QGroupBox("Preset Details")
        form = QFormLayout(form_group)
        self.preset_name_edit = QLineEdit()
        self.preset_tone_edit = QLineEdit()
        form.addRow("Name:", self.preset_name_edit)
        form.addRow("Tone:", self.preset_tone_edit)
        self.preset_name_edit.setReadOnly(True) # Name is the key

        self.save_preset_button = QPushButton("Save Preset")
        self.save_preset_button.clicked.connect(self._action_save_preset)

        right_layout.addWidget(form_group)
        right_layout.addStretch(1)
        right_layout.addWidget(self.save_preset_button, 0, Qt.AlignmentFlag.AlignRight)

        splitter.addWidget(right_widget)
        layout.addWidget(splitter)
        
        self.new_preset_button.clicked.connect(self._action_new_preset)
        self.delete_preset_button.clicked.connect(self._action_delete_preset)

        self._populate_presets_list()
        self._on_preset_selected(self.presets_list.currentItem())

        return tab

    def _create_golden_rules_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.addWidget(QLabel("These are fundamental rules applied to all AI prompts, including patcher format rules."))
        self.golden_rules_edit = QPlainTextEdit()
        self.golden_rules_edit.setPlainText(golden_rules.get_golden_rules_text())
        layout.addWidget(self.golden_rules_edit)
        button_layout = QHBoxLayout()
        reset_button = QPushButton("Reset to Default")
        save_button = QPushButton("Save Golden Rules")
        reset_button.clicked.connect(self._reset_golden_rules)
        save_button.clicked.connect(self._save_golden_rules)
        button_layout.addStretch()
        button_layout.addWidget(reset_button)
        button_layout.addWidget(save_button)
        layout.addLayout(button_layout)
        return tab

    def _populate_personas_list(self, select_id=None):
        self.personas_list.clear()
        persona_dir = os.path.join(get_base_path(), "assets", "ai_personas")
        os.makedirs(persona_dir, exist_ok=True)
        for filename in sorted(os.listdir(persona_dir)):
            if filename.endswith(".py") and not filename.startswith("__"):
                persona_id = os.path.splitext(filename)[0]
                item = QListWidgetItem(persona_id)
                item.setData(Qt.ItemDataRole.UserRole, os.path.join(persona_dir, filename))
                self.personas_list.addItem(item)
                if persona_id == select_id:
                    self.personas_list.setCurrentItem(item)
        if not select_id and self.personas_list.count() > 0:
            self.personas_list.setCurrentRow(0)

    def _on_persona_selected(self, current, previous):
        if current:
            filepath = current.data(Qt.ItemDataRole.UserRole)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.persona_editor_edit.setPlainText(f.read())
            except Exception as e:
                self.persona_editor_edit.setPlainText(f"# Error reading {os.path.basename(filepath)}\n# {e}")
    
    def _action_new_persona(self):
        name, ok = QInputDialog.getText(self, "New Persona", "Enter persona name (e.g., 'Anya the Architect'):")
        if not (ok and name): return
        
        file_name = name.lower().replace(" ", "_").replace("'", "")
        file_name = re.sub(r'[^a-z0-9_]', '', file_name)
        
        persona_dir = os.path.join(get_base_path(), "assets", "ai_personas")
        filepath = os.path.join(persona_dir, f"{file_name}.py")

        if os.path.exists(filepath):
            QMessageBox.warning(self, "File Exists", f"A file named '{file_name}.py' already exists.")
            return

        content = PERSONA_TEMPLATE.format(
            file_name=file_name,
            name=name,
            expertise="...",
            description="A new persona.",
            system_prompt_logic="You are a helpful assistant."
        )
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            self._populate_personas_list(select_id=file_name)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not create persona file: {e}")

    def _action_delete_persona(self):
        current = self.personas_list.currentItem()
        if not current: return
        filepath = current.data(Qt.ItemDataRole.UserRole)
        
        if QMessageBox.question(self, "Confirm Delete", f"Delete '{current.text()}'?") == QMessageBox.StandardButton.Yes:
            try:
                os.remove(filepath)
                self.persona_editor_edit.clear()
                self._populate_personas_list()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not delete persona file: {e}")

    def _action_save_persona(self):
        current_item = self.personas_list.currentItem()
        if not current_item:
            return
        filepath = current_item.data(Qt.ItemDataRole.UserRole)
        content = self.persona_editor_edit.toPlainText()
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            QMessageBox.information(self, "Success", f"Saved '{os.path.basename(filepath)}'.\nChanges will apply next time AI Studio is opened.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def _populate_presets_list(self, select_id=None):
        current_selection = select_id
        if not current_selection and self.presets_list.currentItem():
            current_selection = self.presets_list.currentItem().data(Qt.ItemDataRole.UserRole)

        self.presets_list.clear()
        for preset_id in self.preset_manager.list_presets():
            item = QListWidgetItem(preset_id)
            item.setData(Qt.ItemDataRole.UserRole, preset_id)
            self.presets_list.addItem(item)
            if preset_id == current_selection:
                self.presets_list.setCurrentItem(item)

        if not self.presets_list.currentItem() and self.presets_list.count() > 0:
            self.presets_list.setCurrentRow(0)

    def _on_preset_selected(self, current, _=None):
        is_default = False
        if not current:
            self.preset_name_edit.clear()
            self.preset_tone_edit.clear()
            self.preset_name_edit.setEnabled(False)
            self.preset_tone_edit.setEnabled(False)
            self.save_preset_button.setEnabled(False)
            self.delete_preset_button.setEnabled(False)
            return
        
        preset_id = current.data(Qt.ItemDataRole.UserRole)
        data = self.preset_manager.get_preset(preset_id)
        is_default = preset_id in ["Default", "Detailed", "Friendly"]

        self.preset_name_edit.setText(preset_id)
        self.preset_tone_edit.setText(data.get("tone", ""))
        self.preset_tone_edit.setEnabled(not is_default)
        self.save_preset_button.setEnabled(not is_default)
        self.delete_preset_button.setEnabled(not is_default)

    def _action_new_preset(self):
        name, ok = QInputDialog.getText(self, "New Style Preset", "Enter preset name:")
        if ok and name:
            if name in self.preset_manager.list_presets():
                QMessageBox.warning(self, "Preset Exists", "A preset with that name already exists.")
                return
            
            new_data = {"tone": "custom"}
            self.preset_manager.upsert_preset(name, new_data)
            self._populate_presets_list(select_id=name)

    def _action_delete_preset(self):
        current = self.presets_list.currentItem()
        if not current: return
        preset_id = current.data(Qt.ItemDataRole.UserRole)
        if preset_id in ["Default", "Detailed", "Friendly"]:
            QMessageBox.warning(self, "Cannot Delete", "Default presets cannot be deleted.")
            return

        if QMessageBox.question(self, "Confirm Delete", f"Delete '{current.text()}'?") == QMessageBox.StandardButton.Yes:
            self.preset_manager.delete_preset(preset_id)
            self._populate_presets_list()

    def _action_save_preset(self):
        current = self.presets_list.currentItem()
        if not current: return
        preset_id = current.data(Qt.ItemDataRole.UserRole)
        
        data = {"tone": self.preset_tone_edit.text().strip()}
        
        self.preset_manager.upsert_preset(preset_id, data)
        QMessageBox.information(self, "Success", "Preset saved.")
        self._populate_presets_list(select_id=preset_id)

    def _save_golden_rules(self):
        if golden_rules.save_golden_rules_from_text(self.golden_rules_edit.toPlainText()):
            QMessageBox.information(self, "Success", "Golden Rules saved.")
        else:
            QMessageBox.critical(self, "Error", "Failed to save Golden Rules.")
            
    def _reset_golden_rules(self):
        if QMessageBox.question(self, "Confirm Reset", "Reset to default?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes:
            if golden_rules.reset_golden_rules_to_default():
                self.golden_rules_edit.setPlainText(golden_rules.get_golden_rules_text())
                QMessageBox.information(self, "Success", "Golden Rules reset.")
            else:
                QMessageBox.critical(self, "Error", "Failed to reset Golden Rules.")

    def update_theme(self):
        colors = self.theme_manager.current_theme_data.get('colors', {})
        bg = colors.get("window.background", "#2d2d2d")
        text = colors.get("editor.foreground", "#cccccc")
        pane_bg = colors.get("sidebar.background", "#333333")
        border = colors.get("input.border", "#555")
        input_bg = colors.get("input.background", bg)
        self.setStyleSheet(f"""
            QDialog {{ background-color: {bg}; color: {text}; }}
            QGroupBox {{ background-color: {pane_bg}; border: 1px solid {border}; border-radius: 4px; margin-top: 6px; }}
            QGroupBox::title {{ subcontrol-origin: margin; left: 10px; padding: 0 4px; }}
            QPlainTextEdit, QTextEdit, QLineEdit {{
                background-color: {input_bg};
                border: 1px solid {border};
                border-radius: 4px;
                padding: 4px;
                color: {text};
            }}
        """)