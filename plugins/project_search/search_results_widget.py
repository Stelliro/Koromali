# /plugins/project_search/search_results_widget.py
import os
from typing import Dict, List, Optional, TYPE_CHECKING
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem,
                             QHeaderView, QLabel, QHBoxLayout)
from PyQt6.QtGui import QFont, QBrush, QColor, QTextDocument
from PyQt6.QtCore import pyqtSignal, Qt
import qtawesome as qta

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager
    from app_core.theme_manager import ThemeManager

class SearchResultsWidget(QWidget):
    """
    A widget that displays project-wide search results in a hierarchical tree view,
    grouped by file, with line previews.
    """
    result_selected = pyqtSignal(str, int, int)

    def __init__(self, theme_manager: "ThemeManager", settings_manager: "SettingsManager", parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.settings_manager = settings_manager
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.summary_widget = QWidget()
        self.summary_layout = QHBoxLayout(self.summary_widget)
        self.summary_layout.setContentsMargins(5, 5, 5, 5)
        self.summary_icon = QLabel()
        self.summary_label = QLabel("Ready for a new search.")
        self.summary_layout.addWidget(self.summary_icon)
        self.summary_layout.addWidget(self.summary_label, 1)
        self.main_layout.addWidget(self.summary_widget)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["File / Match", "Line"])
        header = self.tree.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.tree.setAlternatingRowColors(True)
        self.tree.setIndentation(15)
        self.tree.itemDoubleClicked.connect(self._on_item_double_clicked)
        self.main_layout.addWidget(self.tree)

        self.update_theme()

    def update_theme(self):
        """Applies colors and fonts from the current theme."""
        colors = self.theme_manager.current_theme_data.get('colors', {})
        font_family = self.settings_manager.get("font_family", "Consolas")
        font_size = self.settings_manager.get("font_size", 10)
        
        bg_color = colors.get('sidebar.background', '#2a3338')
        fg_color = colors.get('editor.foreground', '#d3c6aa')
        border_color = colors.get('input.border', '#5f6c6d')
        accent_color = colors.get('accent', '#83c092')
        comment_color = colors.get('syntax.comment', '#808080')

        self.summary_widget.setStyleSheet(f"background-color: {bg_color}; border-bottom: 1px solid {border_color};")
        self.summary_label.setStyleSheet("border: none; background: transparent;")
        self.tree.setFont(QFont(font_family, font_size))
        
        self.match_brush = QBrush(QColor(accent_color))
        self.path_brush = QBrush(QColor(comment_color)) # Dim the path text a bit
        self.line_number_brush = QBrush(QColor(fg_color))

    def clear_results(self):
        """Clears all items from the results tree."""
        self.tree.clear()
        
    def set_search_summary(self, query: str, file_count: int, match_count: int, is_searching: bool = False):
        """Updates the summary label with search statistics."""
        if is_searching:
            self.summary_icon.setPixmap(qta.icon('mdi.magnify-scan', color='grey').pixmap(16, 16))
            self.summary_label.setText(f"Searching for '<b>{query}</b>'...")
        elif match_count > 0:
            self.summary_icon.setPixmap(qta.icon('fa5s.check-circle', color='green').pixmap(16, 16))
            plural_f = "s" if file_count != 1 else ""
            plural_m = "s" if match_count != 1 else ""
            self.summary_label.setText(f"Found {match_count} result{plural_m} for '<b>{query}</b>' in {file_count} file{plural_f}.")
        else:
            self.summary_icon.setPixmap(qta.icon('mdi.information-outline', color='orange').pixmap(16, 16))
            self.summary_label.setText(f"No results found for '<b>{query}</b>'.")

    def populate_results(self, results: Dict[str, List[Dict]], project_root: str):
        """Clears and repopulates the tree with a new set of search results."""
        self.tree.clear()
        self.tree.setSortingEnabled(False)

        for filepath, matches in sorted(results.items()):
            if not matches: continue

            relative_path = os.path.relpath(filepath, project_root).replace("\\", "/")
            file_node = QTreeWidgetItem(self.tree)
            file_node.setText(0, f"{relative_path}")
            file_node.setData(0, Qt.ItemDataRole.UserRole, {'is_file_node': True, 'path': filepath})
            file_node.setIcon(0, qta.icon('mdi.file-code-outline'))
            file_node.setForeground(0, self.path_brush)
            file_node.setToolTip(0, filepath)
            
            # Add match count to a non-sorting column if you want
            # file_node.setText(1, f"({len(matches)})")

            for match in matches:
                line_text_preview = match['line_text'].strip()
                problem_node = QTreeWidgetItem(file_node)
                problem_node.setText(0, line_text_preview)
                problem_node.setText(1, str(match['line']))
                problem_node.setData(0, Qt.ItemDataRole.UserRole, {
                    'filepath': filepath, 'line': match['line'], 'col': match['col']
                })
                problem_node.setForeground(0, self.match_brush)
                problem_node.setForeground(1, self.line_number_brush)

        self.tree.expandAll()
        for i in range(self.tree.columnCount()):
            self.tree.resizeColumnToContents(i)
        self.tree.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tree.setSortingEnabled(True)

    def _on_item_double_clicked(self, item: QTreeWidgetItem, column: int):
        """Emits a signal when a specific result item is double-clicked."""
        data = item.data(0, Qt.ItemDataRole.UserRole)
        if data and not data.get('is_file_node', False):
            if (filepath := data.get("filepath")) and (line := data.get("line")) is not None:
                self.result_selected.emit(filepath, line, data.get("col", 0))