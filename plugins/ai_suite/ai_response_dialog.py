# /plugins/ai_suite/ai_response_dialog.py
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTextEdit, QDialogButtonBox, QPushButton,
    QApplication, QFileDialog, QHBoxLayout
)
try:
    import qtawesome as qta
except Exception:
    qta = None


class AIResponseDialog(QDialog):
    """Simple viewer for AI responses, with copy + save."""
    def __init__(self, response_text: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AI Response")
        self.setMinimumSize(760, 560)

        layout = QVBoxLayout(self)

        bar = QHBoxLayout()
        self.btn_copy = QPushButton(qta.icon('fa5s.copy'), "Copy") if qta else QPushButton("Copy")
        self.btn_save = QPushButton(qta.icon('fa5s.save'), "Save As…") if qta else QPushButton("Save As…")
        bar.addStretch()
        bar.addWidget(self.btn_copy)
        bar.addWidget(self.btn_save)
        layout.addLayout(bar)

        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
        self.text_edit.setPlainText(response_text or "")
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit, 1)

        bb = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        layout.addWidget(bb)

        self.btn_copy.clicked.connect(self._copy)
        self.btn_save.clicked.connect(self._save)
        bb.rejected.connect(self.reject)

    def _copy(self):
        QApplication.clipboard().setText(self.text_edit.toPlainText())

    def _save(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Save Response", "", "Markdown (*.md);;Text (*.txt);;All Files (*.*)"
        )
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.text_edit.toPlainText())