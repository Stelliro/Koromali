# /ui/widgets/add_panel_popup.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem)
from PyQt6.QtCore import Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QIcon
import qtawesome as qta
from app_core.koromali_api import KoromaliPluginAPI

class AddPanelPopup(QWidget):
    """
    A small popup widget for selecting a new panel to add to a tab bar.
    """
    panel_selected = pyqtSignal(str) # Emits the panel_id

    def __init__(self, api: KoromaliPluginAPI, parent=None):
        super().__init__(parent)
        self.api = api
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.setStyleSheet("""
            QWidget { 
                background-color: #3C3F41; 
                border: 1px solid #555;
                color: white;
            }
        """)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Find Panel...")
        self.search_input.textChanged.connect(self.filter_list)
        self.main_layout.addWidget(self.search_input)

        self.panel_list = QListWidget()
        self.panel_list.itemClicked.connect(self.on_item_clicked)
        self.main_layout.addWidget(self.panel_list)
        
        self.populate_list()
        self.setFixedSize(250, 200)

    def populate_list(self):
        """Fills the list with available, but not currently open, panels."""
        self.panel_list.clear()
        registered_panels = self.api.get_registered_panels()
        
        open_panel_classes = []
        main_window = self.api.get_main_window()
        if hasattr(main_window, '_bottom_tab_widget'):
            tab_widget = main_window._bottom_tab_widget
            for i in range(tab_widget.count()):
                open_panel_classes.append(type(tab_widget.widget(i)))

        for panel_id, panel_info in registered_panels.items():
            if panel_info['widget_class'] not in open_panel_classes:
                icon = qta.icon(panel_info.get('icon_name', 'mdi.view-grid-plus-outline'), color='grey')
                item = QListWidgetItem(icon, panel_info.get('title', panel_id))
                item.setData(Qt.ItemDataRole.UserRole, panel_id)
                self.panel_list.addItem(item)
                
    def filter_list(self):
        """Filters the list based on search input."""
        filter_text = self.search_input.text().lower()
        for i in range(self.panel_list.count()):
            item = self.panel_list.item(i)
            item.setHidden(filter_text not in item.text().lower())

    def on_item_clicked(self, item: QListWidgetItem):
        """Emits the signal and closes the popup when an item is selected."""
        panel_id = item.data(Qt.ItemDataRole.UserRole)
        self.panel_selected.emit(panel_id)
        self.close()

    def focusOutEvent(self, event: QEvent):
        """Closes the popup when it loses focus."""
        self.close()
        super().focusOutEvent(event)