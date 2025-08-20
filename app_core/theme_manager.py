# Koromali/app_core/theme_manager.py
import os
import json
import base64
import shutil
from typing import Dict, Any, Optional, TYPE_CHECKING
from PyQt6.QtGui import QColor, QGuiApplication

from utils.logger import log, get_app_data_path
from utils.helpers import get_base_path

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager

SVG_ARROW_PATHS = {'up': "M4 10 L8 6 L12 10", 'down': "M4 6 L8 10 L12 6"}

APP_BASE_PATH = get_base_path()
APP_DATA_ROOT = get_app_data_path()
CUSTOM_THEMES_FILE_PATH = os.path.join(APP_DATA_ROOT, "custom_themes.json")
DEFAULT_CUSTOM_THEMES_FILE_PATH = os.path.join(APP_BASE_PATH, "assets", "themes", "custom_themes.json")
ICON_COLORS_FILE_PATH = os.path.join(APP_DATA_ROOT, "icon_colors.json")
DEFAULT_ICON_COLORS_FILE_PATH = os.path.join(APP_BASE_PATH, "assets", "themes", "icon_colors.json")

BUILT_IN_THEMES = {
    "Koromali_modern_dark": {
        "name": "Koromali Modern (Dark)", "author": "Koromali", "type": "dark", "is_custom": False,
        "colors": {
            "window.background": "#2d2d2d", "sidebar.background": "#252525", "editor.background": "#2d2d2d",
            "editor.foreground": "#cccccc", "editor.selectionBackground": "#3E5674",
            "editor.lineHighlightBackground": "#3c3c3c", "editor.matchingBracketBackground": "#4a4a4a",
            "editor.matchingBracketForeground": "#ffffff",
            "editor.userHighlightBackground": "#4078f24D",
            "editor.breakpoint.color": "#e06c75",
            "editorGutter.background": "#2d2d2d", "editorGutter.foreground": "#6a6a6a",
            "editorGutter.hoverBackground": "#4078f21a",
            "editorLineNumber.foreground": "#6a6a6a", "editorLineNumber.activeForeground": "#cccccc",
            "gutter.activeLineNumberForeground": "#cccccc",
            "menu.background": "#3c3c3c", "menu.foreground": "#cccccc", "statusbar.background": "#252525",
            "statusbar.foreground": "#cccccc", "tab.activeBackground": "#2d2d2d",
            "tab.inactiveBackground": "#252525", "tab.activeForeground": "#ffffff",
            "tab.inactiveForeground": "#888888", "button.background": "#4a4a4a",
            "button.foreground": "#ffffff", "input.background": "#3c3c3c", "input.foreground": "#cccccc",
            "input.border": "#555555", "scrollbar.background": "#252525", "scrollbar.handle": "#4a4a4a",
            "scrollbar.handleHover": "#5a5a5a", "scrollbar.handlePressed": "#6a6a6a",
            "accent": "#4078f2", "syntax.keyword": "#c678dd", "syntax.operator": "#56b6c2",
            "syntax.brace": "#cccccc", "syntax.decorator": "#61afef", "syntax.self": "#e5c07b",
            "syntax.className": "#e5c07b", "syntax.functionName": "#61afef", "syntax.comment": "#7f848e",
            "syntax.string": "#98c379", "syntax.docstring": "#7f848e", "syntax.number": "#d19a66",
            "tree.indentationGuides.stroke": "#555555", "tree.trace.color": "#4078f2",
            "git.added": "#98c379", "git.modified": "#e5c07b", "git.deleted": "#e06c75",
            "git.status.foreground": "#61afef",
            "list.hoverBackground": "#3c3c3c",
            "list.activeSelectionBackground": "#4078f2",
            "list.activeSelectionForeground": "#ffffff",
            "list.inactiveSelectionBackground": "#3c3c3c",
            "list.inactiveSelectionForeground": "#cccccc"
        }
    },
    "Koromali_modern_light": {
        "name": "Koromali Modern (Light)", "author": "Koromali", "type": "light", "is_custom": False,
        "colors": {
            "window.background": "#ffffff", "sidebar.background": "#f5f5f5", "editor.background": "#ffffff",
            "editor.foreground": "#333333", "editor.selectionBackground": "#b3d7ff",
            "editor.lineHighlightBackground": "#f0f0f0", "editor.matchingBracketBackground": "#cce5ff",
            "editor.matchingBracketForeground": "#333333",
            "editor.userHighlightBackground": "#007acc4D",
            "editor.breakpoint.color": "#e45649",
            "editorGutter.background": "#ffffff", "editorGutter.foreground": "#aaaaaa",
            "editorGutter.hoverBackground": "#007acc1a",
            "editorLineNumber.foreground": "#aaaaaa", "editorLineNumber.activeForeground": "#333333",
            "gutter.activeLineNumberForeground": "#333333",
            "menu.background": "#f0f0f0", "menu.foreground": "#333333", "statusbar.background": "#007acc",
            "statusbar.foreground": "#ffffff", "tab.activeBackground": "#ffffff",
            "tab.inactiveBackground": "#f5f5f5", "tab.activeForeground": "#333333",
            "tab.inactiveForeground": "#888888", "button.background": "#f0f0f0",
            "button.foreground": "#333333", "input.background": "#ffffff", "input.foreground": "#333333",
            "input.border": "#cccccc", "scrollbar.background": "#f5f5f5", "scrollbar.handle": "#cccccc",
            "scrollbar.handleHover": "#bbbbbb", "scrollbar.handlePressed": "#aaaaaa",
            "accent": "#007acc", "syntax.keyword": "#d73a49", "syntax.operator": "#333333",
            "syntax.brace": "#333333", "syntax.decorator": "#6f42c1", "syntax.self": "#e36209",
            "syntax.className": "#e5c07b", "syntax.functionName": "#005cc5", "syntax.comment": "#6a737d",
            "syntax.string": "#032f62", "syntax.docstring": "#6a737d", "syntax.number": "#005cc5",
            "tree.indentationGuides.stroke": "#cccccc", "tree.trace.color": "#007acc",
            "git.added": "#28a745", "git.modified": "#f1e05a", "git.deleted": "#d73a49",
            "git.status.foreground": "#007acc",
            "list.hoverBackground": "#f0f0f0",
            "list.activeSelectionBackground": "#007acc",
            "list.activeSelectionForeground": "#ffffff",
            "list.inactiveSelectionBackground": "#dcdcdc",
            "list.inactiveSelectionForeground": "#333333"
        }
    }
}

def get_arrow_svg_uri(direction: str, color: str) -> str:
    path_data = SVG_ARROW_PATHS.get(direction, "")
    if not path_data:
        return ""
    # Ensure color is a valid hex string for SVG
    safe_color = QColor(color).name()
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="none" stroke="{safe_color}" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="{path_data}"/></svg>'
    b64_content = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{b64_content}"


class ThemeManager:
    def __init__(self, settings_manager: 'SettingsManager'):
        self.settings_manager = settings_manager
        self.all_themes_data: Dict[str, Dict] = {}
        self.icon_colors: Dict[str, str] = {}
        self.current_theme_id: str = "Koromali_modern_dark"
        self.current_theme_data: Dict[str, Any] = {}
        self.reload_themes()
        log.info(f"ThemeManager initialized. Current theme: '{self.current_theme_id}'")

    def reload_themes(self):
        self.icon_colors = self._load_icon_colors()
        self.all_themes_data = self._load_all_themes()
        last_theme_id = self.settings_manager.get("last_theme_id", "Koromali_modern_dark")
        if last_theme_id not in self.all_themes_data:
            last_theme_id = "Koromali_modern_dark"
            self.settings_manager.set("last_theme_id", last_theme_id)
        self.current_theme_id = last_theme_id
        self.current_theme_data = self.all_themes_data.get(self.current_theme_id, {})
        if 'colors' in self.current_theme_data:
            self.current_theme_data['colors']['icon.colors'] = self.icon_colors

    def _load_and_repair_json(self, user_path: str, default_path: str) -> Dict:
        """Loads a user JSON file, repairing it from default if corrupt or missing."""
        if not os.path.exists(default_path):
            log.error(f"FATAL: Default asset file is missing, cannot load or repair: {default_path}")
            return {}

        user_data = None
        should_repair = not os.path.exists(user_path)

        if os.path.exists(user_path):
            try:
                with open(user_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.strip():
                        user_data = json.loads(content)
                        if not isinstance(user_data, dict):
                            log.warning(f"User data at {user_path} is not a dictionary. Will repair.")
                            should_repair = True
                    else:
                        log.warning(f"User file at {user_path} is empty. Will repair.")
                        should_repair = True
            except (IOError, json.JSONDecodeError):
                log.warning(f"User file at {user_path} is corrupt. Will repair.")
                should_repair = True

        if should_repair:
            try:
                os.makedirs(os.path.dirname(user_path), exist_ok=True)
                shutil.copy2(default_path, user_path)
                log.info(f"Initialized/repaired user file at {user_path} from default.")
                with open(default_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                log.error(f"Failed to copy/read default file to {user_path}: {e}")
                return {}
        
        return user_data

    def _load_icon_colors(self) -> Dict[str, str]:
        return self._load_and_repair_json(ICON_COLORS_FILE_PATH, DEFAULT_ICON_COLORS_FILE_PATH)

    def _load_all_themes(self) -> Dict[str, Dict]:
        all_themes = BUILT_IN_THEMES.copy()
        custom_themes = self._load_and_repair_json(CUSTOM_THEMES_FILE_PATH, DEFAULT_CUSTOM_THEMES_FILE_PATH)

        for theme_id, theme_data in custom_themes.items():
            theme_data['is_custom'] = True
            all_themes[theme_id] = theme_data
        
        return all_themes

    def get_available_themes_for_ui(self) -> Dict[str, str]:
        return {tid: d.get("name", tid) for tid, d in
                sorted(self.all_themes_data.items(), key=lambda i: i[1].get("name", i[0]).lower())}

    def set_theme(self, theme_id: str, app_instance: Optional[QGuiApplication] = None):
        if theme_id not in self.all_themes_data: theme_id = "Koromali_modern_dark"
        self.current_theme_id = theme_id
        self.current_theme_data = self.all_themes_data.get(theme_id, {})

        if 'colors' not in self.current_theme_data:
            log.warning(f"Theme '{theme_id}' is missing the 'colors' dictionary.")
        else:
            self.current_theme_data['colors']['icon.colors'] = self.icon_colors

        self.settings_manager.set("last_theme_id", theme_id)
        from PyQt6.QtWidgets import QApplication
        self.apply_theme_to_app(app_instance or QApplication.instance())
        log.info(f"Theme set to '{self.current_theme_data.get('name', 'Unknown')}'")

    def add_or_update_custom_theme(self, theme_id: str, theme_data: dict):
        custom_themes_path = CUSTOM_THEMES_FILE_PATH
        try:
            custom_themes = {}
            if os.path.exists(custom_themes_path):
                 with open(custom_themes_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.strip():
                        custom_themes = json.loads(content)

            custom_themes[theme_id] = theme_data
            with open(custom_themes_path, 'w', encoding='utf-8') as f:
                json.dump(custom_themes, f, indent=4)
            self.reload_themes()
        except (IOError, json.JSONDecodeError) as e:
            log.error(f"Failed to save custom theme '{theme_id}': {e}")

    def delete_custom_theme(self, theme_id: str):
        custom_themes_path = CUSTOM_THEMES_FILE_PATH
        try:
            custom_themes = {}
            if os.path.exists(custom_themes_path) and os.path.getsize(custom_themes_path) > 0:
                with open(custom_themes_path, 'r', encoding='utf-8') as f:
                    custom_themes = json.load(f)
            if theme_id in custom_themes:
                del custom_themes[theme_id]
                with open(custom_themes_path, 'w', encoding='utf-8') as f:
                    json.dump(custom_themes, f, indent=4)
                self.reload_themes()
        except (IOError, json.JSONDecodeError) as e:
            log.error(f"Failed to delete custom theme '{theme_id}': {e}")

    def apply_theme_to_app(self, app: Optional[QGuiApplication]):
        if not app or not self.current_theme_data: return
        colors = self.current_theme_data.get("colors", {})

        def c(key: str, fb: str) -> str: return colors.get(key, fb)

        def adj(h: str, f: int, a: Optional[float] = None) -> str:
            """Adjusts color lightness by a factor 'f'."""
            c_obj = QColor(h)
            # Use HSL for more intuitive lightness adjustments
            h_val, s, l_val, alpha = c_obj.getHslF()
            
            # f is a percentage, e.g., 110 for 10% lighter, 90 for 10% darker
            new_lightness = min(max(l_val * (f / 100.0), 0.0), 1.0)
            
            final_color = QColor.fromHslF(h_val, s, new_lightness, alpha)

            if a is not None:
                final_color.setAlphaF(a)
            
            return f"rgba({final_color.red()}, {final_color.green()}, {final_color.blue()}, {final_color.alphaF()})"

        is_light = self.current_theme_data.get('type') == 'light'
        hover_factor = 85 if is_light else 130
        pressed_factor = 75 if is_light else 150
        
        # Define color variables from theme
        ac, wb, sb, bb, bf, ib, igf, ibd = (c('accent', '#007acc'), c('window.background', '#2d2d2d'),
            c('sidebar.background', '#252525'), c('button.background', '#4a4a4a'), c('button.foreground', '#ffffff'),
            c('input.background', '#3c3c3c'), c('editor.foreground', '#cccccc'), c('input.border', '#555555'))
        
        menu_bg, menu_fg = c('menu.background', '#3c3c3c'), c('menu.foreground', '#cccccc')
        status_bg, status_fg = c('statusbar.background', '#252525'), c('statusbar.foreground', '#cccccc')
        
        tab_active_bg, tab_inactive_bg = c('tab.activeBackground', '#2d2d2d'), c('tab.inactiveBackground', '#252525')
        tab_active_fg, tab_inactive_fg = c('tab.activeForeground', '#ffffff'), c('tab.inactiveForeground', '#888888')
        
        list_hover_bg = c('list.hoverBackground', adj(sb, 110))
        list_active_bg, list_active_fg = c('list.activeSelectionBackground', ac), c('list.activeSelectionForeground', '#ffffff')
        list_inactive_bg, list_inactive_fg = c('list.inactiveSelectionBackground', adj(sb, 105)), c('list.inactiveSelectionForeground', igf)

        scrollbar_bg, scroll_handle = c('scrollbar.background', sb), c('scrollbar.handle', bb)
        
        arrow_color = '#000000' if is_light else '#ffffff'
        combo_arrow, spin_up, spin_down = (get_arrow_svg_uri('down', arrow_color), get_arrow_svg_uri('up', arrow_color), get_arrow_svg_uri('down', arrow_color))

        stylesheet = f"""
            QMainWindow, QDialog {{
                background-color: {wb};
                color: {igf};
            }}
            QDockWidget > QWidget {{
                background-color: {sb};
            }}
            QDockWidget {{
                background-color: {sb};
                color: {igf};
                titlebar-close-icon: url(none);
                titlebar-normal-icon: url(none);
            }}
            QDockWidget::title {{
                background-color: {adj(sb, 95 if is_light else 115)};
                padding: 5px;
                border-bottom: 1px solid {ibd};
            }}
            QTreeView, QListWidget {{
                background-color: {sb};
                border: none;
                color: {igf};
                alternate-background-color: {adj(sb, 98 if is_light else 104)};
            }}
            QTreeView::item:hover, QListWidget::item:hover {{ background-color: {list_hover_bg}; }}
            QTreeView::item:selected:active, QListWidget::item:selected:active {{ background-color: {list_active_bg}; color: {list_active_fg}; }}
            QTreeView::item:selected:!active, QListWidget::item:selected:!active {{ background-color: {list_inactive_bg}; color: {list_inactive_fg}; }}
            QHeaderView::section {{ background-color: {adj(sb, 110)}; padding: 4px; border: 1px solid {ibd}; }}
            QFrame#ExplorerToolbar {{ background-color: {adj(sb, 105)}; border-bottom: 1px solid {ibd}; }}

            /* --- Button Styles --- */
            /* Regular buttons are hollow, using the accent color */
            QPushButton {{
                background-color: transparent;
                color: {ac};
                border: 1px solid {ac};
                border-radius: 4px;
                padding: 5px 10px;
            }}
            QPushButton:hover {{
                background-color: {ac};
                color: {bf};
            }}
            QPushButton:pressed {{
                background-color: {adj(ac, 90 if is_light else 110)};
                color: {bf};
            }}
            QPushButton:disabled {{
                background-color: transparent;
                color: {adj(ac, 100, 0.4)};
                border: 1px solid {adj(ac, 100, 0.4)};
            }}

            /* Tool buttons (for toolbars) are flat and transparent */
            QToolButton {{
                background: transparent;
                border: 1px solid transparent;
                padding: 4px;
                margin: 1px;
                border-radius: 4px;
            }}
            QToolButton:hover {{
                background-color: {adj(sb, 105 if is_light else 120)};
            }}
            QToolButton:pressed {{
                background-color: {adj(sb, 95 if is_light else 130)};
            }}
            QToolButton:checked {{
                background-color: {adj(ac, 100, 0.3)};
                border: 1px solid {adj(ac, 100, 0.5)};
            }}

            QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox {{ background-color: {ib}; color: {igf}; border: 1px solid {ibd}; border-radius: 4px; padding: 4px; }}
            QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus {{ border: 1px solid {ac}; }}
            QComboBox {{ background-color: {bb}; border: 1px solid {ibd}; border-radius: 4px; padding: 4px; }}
            QComboBox::drop-down {{ border: none; }}
            QComboBox::down-arrow {{ image: url({combo_arrow}); }}
            QComboBox QAbstractItemView {{ background-color: {menu_bg}; border: 1px solid {ibd}; color: {menu_fg}; selection-background-color: {ac}; }}
            QSpinBox::up-button, QSpinBox::down-button {{ border: none; }}
            QSpinBox::up-arrow {{ image: url({spin_up}); }}
            QSpinBox::down-arrow {{ image: url({spin_down}); }}
            QMenuBar {{ background-color: {wb}; border-bottom: 1px solid {ibd}; }}
            QMenuBar::item {{ padding: 5px 10px; background: transparent; }}
            QMenuBar::item:selected {{ background-color: {adj(wb, 95 if is_light else 120)}; }}
            QMenu {{ background-color: {menu_bg}; border: 1px solid {ibd}; color: {menu_fg}; }}
            QMenu::item:selected {{ background-color: {ac}; color: {list_active_fg}; }}
            QStatusBar {{ background-color: {status_bg}; color: {status_fg}; }}
            QTabWidget::pane {{ border: none; }}
            QTabBar::tab {{
                background: {tab_inactive_bg}; color: {tab_inactive_fg};
                padding: 8px 15px; border: 1px solid {ibd}; border-bottom: none;
                border-top-left-radius: 4px; border-top-right-radius: 4px;
            }}
            QTabBar::tab:selected {{ background: {tab_active_bg}; color: {tab_active_fg}; }}
            QTabBar::tab:hover {{ background: {adj(tab_inactive_bg, hover_factor)}; }}
            QSplitter::handle {{ background-color: {wb}; }}
            QSplitter::handle:horizontal {{ width: 1px; }}
            QSplitter::handle:vertical {{ height: 1px; }}
            QSplitter::handle:hover {{ background-color: {ac}; }}
            QScrollBar:vertical {{ border: none; background: {scrollbar_bg}; width: 14px; margin: 0; }}
            QScrollBar::handle:vertical {{ background: {scroll_handle}; min-height: 25px; border-radius: 7px; }}
            QScrollBar::handle:vertical:hover {{ background: {adj(scroll_handle, hover_factor)}; }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background: none; }}
            QScrollBar:horizontal {{ border: none; background: {scrollbar_bg}; height: 14px; margin: 0; }}
            QScrollBar::handle:horizontal {{ background: {scroll_handle}; min-width: 25px; border-radius: 7px; }}
            QScrollBar::handle:horizontal:hover {{ background: {adj(scroll_handle, hover_factor)}; }}
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0px; }}
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background: none; }}
        """
        app.setStyleSheet(stylesheet)