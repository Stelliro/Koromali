# Koromali/ui/widgets/problems_panel.py
import os
from typing import Dict, List, Optional, TYPE_CHECKING
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QHeaderView, QWidget
from PyQt6.QtCore import pyqtSignal, Qt
from utils.logger import log

if TYPE_CHECKING:
    from app_core.theme_manager import ThemeManager

class ProblemsPanel(QTreeWidget):
    """
    A widget that displays linting problems in a hierarchical tree view,
    grouped by file.
    """
    problem_selected = pyqtSignal(str, int, int)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        log.info("ProblemsPanel initializing...")

        self.setColumnCount(4)
        self.setHeaderLabels(["Description", "File", "Line", "Code"])
        self.setSelectionBehavior(QTreeWidget.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTreeWidget.SelectionMode.SingleSelection)
        self.setEditTriggers(QTreeWidget.EditTrigger.NoEditTriggers)
        self.setAlternatingRowColors(True)
        self.setIndentation(12)
        self.setSortingEnabled(True)

        header = self.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        self.itemDoubleClicked.connect(self._on_item_double_clicked)
        log.info("ProblemsPanel initialized as QTreeWidget.")
        
    def update_theme(self):
        # Placeholder for theme updates if specific styling is needed in the future
        pass

    def update_problems(self, problems_by_file: Dict[str, List[Dict]]):
        """
        Clears and repopulates the tree with a new set of problems.
        """
        self.clear()
        self.setSortingEnabled(False)

        if not problems_by_file:
            self.show_info_message("No problems found.")
            return

        for filepath, problems in problems_by_file.items():
            if not problems:
                continue

            file_node = QTreeWidgetItem(self)
            file_node.setText(
                0, f"{os.path.basename(filepath)} ({len(problems)} issues)")
            file_node.setData(
                0, Qt.ItemDataRole.UserRole, {'is_file_node': True})
            file_node.setFirstColumnSpanned(True)

            for problem in problems:
                problem_node = QTreeWidgetItem(file_node)
                problem_node.setText(0, problem.get("description", ""))
                problem_node.setText(1, os.path.basename(filepath))
                problem_node.setText(2, str(problem.get("line", "")))
                problem_node.setText(3, problem.get("code", ""))
                problem_node.setData(0, Qt.ItemDataRole.UserRole, {
                    'filepath': filepath,
                    'line': problem.get("line"),
                    'col': problem.get("col")
                })
        self.expandAll()
        self.setSortingEnabled(True)
        self.sortByColumn(1, Qt.SortOrder.AscendingOrder)

    def clear_problems(self):
        """Clears all items from the panel."""
        self.clear()

    def show_info_message(self, message: str):
        """Displays a single, un-clickable informational message."""
        self.clear()
        info_item = QTreeWidgetItem(self, [message])
        info_item.setFirstColumnSpanned(True)
        info_item.setDisabled(True)

    def _on_item_double_clicked(self, item: QTreeWidgetItem, column: int):
        """Emits a signal when a specific problem item is double-clicked."""
        problem_data = item.data(0, Qt.ItemDataRole.UserRole)
        if problem_data and not problem_data.get('is_file_node', False):
            filepath = problem_data.get("filepath")
            line = problem_data.get("line")
            col = problem_data.get("col")
            if filepath and line is not None:
                log.debug(f"Problem selected: Go to {filepath}:{line}:{col}")
                self.problem_selected.emit(filepath, line, col)