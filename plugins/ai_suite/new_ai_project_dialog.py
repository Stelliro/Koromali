# /plugins/ai_suite/new_ai_project_dialog.py
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit,
                             QTextEdit, QPushButton, QDialogButtonBox,
                             QMessageBox, QApplication, QHBoxLayout)
from app_core import golden_rules
try:
    import qtawesome as qta
except ImportError:
    qta = None


class NewAIProjectDialog(QDialog):
    """A dialog to create a prompt for generating a new project."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Project from AI")
        self.setMinimumWidth(500)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.project_name_edit = QLineEdit()
        self.project_name_edit.setPlaceholderText("e.g., My Awesome App")
        
        self.instructions_edit = QTextEdit()
        self.instructions_edit.setPlaceholderText("Describe your new application. For example:\n"
                                                  "\"Create a simple PyQt6 app that shows a button. "
                                                  "When clicked, the button's text should change.\"")

        form_layout.addRow("<b>Project Name:</b>", self.project_name_edit)
        form_layout.addRow("<b>Instructions:</b>", self.instructions_edit)
        layout.addLayout(form_layout)

        button_bar = QHBoxLayout()
        button_bar.addStretch()
        self.generate_button = QPushButton(qta.icon('fa5s.copy'), "Generate & Copy Prompt") if qta else QPushButton("Generate & Copy Prompt")
        self.cancel_button = QPushButton("Cancel")
        button_bar.addWidget(self.cancel_button)
        button_bar.addWidget(self.generate_button)
        layout.addLayout(button_bar)
        
        self.generate_button.clicked.connect(self._generate_prompt)
        self.cancel_button.clicked.connect(self.reject)
    
    def _generate_prompt(self):
        project_name = self.project_name_edit.text().strip()
        instructions = self.instructions_edit.toPlainText().strip()

        if not project_name or not instructions:
            QMessageBox.warning(self, "Missing Information",
                                "Project Name and Instructions are required.")
            return

        system_prompt = "\n".join([
            "You are an expert software developer specializing in rapid project scaffolding. Your purpose is to take a user's high-level idea and generate a complete, logical, and runnable project structure with clean boilerplate code.",
            "Your response MUST start with the `## Project Name: <name>` from the user prompt.",
            "Your output MUST ONLY be a series of file blocks, each containing the complete code for that file, conforming to the Golden Rules.",
            "\n" + golden_rules.get_rules_markdown()
        ])

        user_prompt_lines = [
            "# New Project Request",
            "",
            f"## Project Name: {project_name}",
            "",
            "## User Instructions",
            "```text",
            instructions,
            "```"
        ]
        user_prompt = "\n".join(user_prompt_lines)
        
        full_prompt = f"---SYSTEM-PROMPT---\n\n{system_prompt.strip()}\n\n---USER-PROMPT---\n\n{user_prompt.strip()}"
        QApplication.clipboard().setText(full_prompt)
        QMessageBox.information(self, "Prompt Copied",
                                "The prompt has been copied to your clipboard. "
                                "Paste it into your AI model to generate the project.")
        self.accept()