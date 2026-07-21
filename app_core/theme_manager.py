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
    # Refined default palette — cooler slate surfaces, soft borders, single accent.
    "Koromali_modern_dark": {
        "name": "Koromali Modern (Dark)", "author": "Koromali", "type": "dark", "is_custom": False,
        "colors": {
            "window.background": "#1e1f24", "sidebar.background": "#17181d", "editor.background": "#1e1f24",
            "editor.foreground": "#d8dbe3", "editor.selectionBackground": "#2f3f5c",
            "editor.lineHighlightBackground": "#262830", "editor.matchingBracketBackground": "#343848",
            "editor.matchingBracketForeground": "#ffffff",
            "editor.userHighlightBackground": "#6c9ef84D",
            "editor.breakpoint.color": "#f07178",
            "editorGutter.background": "#1e1f24", "editorGutter.foreground": "#5c6370",
            "editorGutter.hoverBackground": "#6c9ef81a",
            "editorLineNumber.foreground": "#5c6370", "editorLineNumber.activeForeground": "#c8ccd6",
            "gutter.activeLineNumberForeground": "#c8ccd6",
            "menu.background": "#23252c", "menu.foreground": "#d8dbe3",
            "statusbar.background": "#14151a", "statusbar.foreground": "#aeb4c0",
            "tab.activeBackground": "#1e1f24", "tab.inactiveBackground": "#17181d",
            "tab.activeForeground": "#ffffff", "tab.inactiveForeground": "#7a8190",
            "button.background": "#2a2d36", "button.foreground": "#ffffff",
            "input.background": "#23252c", "input.foreground": "#d8dbe3", "input.border": "#3a3e4a",
            "scrollbar.background": "#17181d", "scrollbar.handle": "#3a3e4a",
            "scrollbar.handleHover": "#4b5160", "scrollbar.handlePressed": "#5c6370",
            "accent": "#6c9ef8", "syntax.keyword": "#c792ea", "syntax.operator": "#89ddff",
            "syntax.brace": "#d8dbe3", "syntax.decorator": "#82aaff", "syntax.self": "#ffcb6b",
            "syntax.className": "#ffcb6b", "syntax.functionName": "#82aaff", "syntax.comment": "#676e7b",
            "syntax.string": "#c3e88d", "syntax.docstring": "#676e7b", "syntax.number": "#f78c6c",
            "tree.indentationGuides.stroke": "#3a3e4a", "tree.trace.color": "#6c9ef8",
            "git.added": "#c3e88d", "git.modified": "#ffcb6b", "git.deleted": "#f07178",
            "git.status.foreground": "#82aaff",
            "list.hoverBackground": "#262830",
            "list.activeSelectionBackground": "#3d5a8a",
            "list.activeSelectionForeground": "#ffffff",
            "list.inactiveSelectionBackground": "#2a2d36",
            "list.inactiveSelectionForeground": "#d8dbe3"
        }
    },
    "Koromali_modern_light": {
        "name": "Koromali Modern (Light)", "author": "Koromali", "type": "light", "is_custom": False,
        "colors": {
            "window.background": "#f7f8fa", "sidebar.background": "#eef0f4", "editor.background": "#ffffff",
            "editor.foreground": "#1f2430", "editor.selectionBackground": "#c7dbff",
            "editor.lineHighlightBackground": "#f0f3f8", "editor.matchingBracketBackground": "#dbe8ff",
            "editor.matchingBracketForeground": "#1f2430",
            "editor.userHighlightBackground": "#3b82f64D",
            "editor.breakpoint.color": "#dc2626",
            "editorGutter.background": "#ffffff", "editorGutter.foreground": "#9aa3b2",
            "editorGutter.hoverBackground": "#3b82f61a",
            "editorLineNumber.foreground": "#9aa3b2", "editorLineNumber.activeForeground": "#1f2430",
            "gutter.activeLineNumberForeground": "#1f2430",
            "menu.background": "#ffffff", "menu.foreground": "#1f2430",
            "statusbar.background": "#3b82f6", "statusbar.foreground": "#ffffff",
            "tab.activeBackground": "#ffffff", "tab.inactiveBackground": "#eef0f4",
            "tab.activeForeground": "#1f2430", "tab.inactiveForeground": "#6b7280",
            "button.background": "#e8ebf0", "button.foreground": "#1f2430",
            "input.background": "#ffffff", "input.foreground": "#1f2430", "input.border": "#d0d5dd",
            "scrollbar.background": "#eef0f4", "scrollbar.handle": "#c5cbd6",
            "scrollbar.handleHover": "#aeb6c4", "scrollbar.handlePressed": "#98a2b3",
            "accent": "#3b82f6", "syntax.keyword": "#c026d3", "syntax.operator": "#1f2430",
            "syntax.brace": "#1f2430", "syntax.decorator": "#7c3aed", "syntax.self": "#d97706",
            "syntax.className": "#b45309", "syntax.functionName": "#2563eb", "syntax.comment": "#6b7280",
            "syntax.string": "#0f766e", "syntax.docstring": "#6b7280", "syntax.number": "#b45309",
            "tree.indentationGuides.stroke": "#d0d5dd", "tree.trace.color": "#3b82f6",
            "git.added": "#16a34a", "git.modified": "#ca8a04", "git.deleted": "#dc2626",
            "git.status.foreground": "#2563eb",
            "list.hoverBackground": "#e8ebf0",
            "list.activeSelectionBackground": "#3b82f6",
            "list.activeSelectionForeground": "#ffffff",
            "list.inactiveSelectionBackground": "#d9dee8",
            "list.inactiveSelectionForeground": "#1f2430"
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

        # Surface elevation helpers for a cleaner layered chrome look.
        surface_1 = adj(wb, 98 if is_light else 108)
        surface_2 = adj(sb, 97 if is_light else 112)
        muted_fg = adj(igf, 70 if is_light else 65)
        border_soft = adj(ibd, 100, 0.85)
        radius = "6px"
        radius_sm = "4px"

        stylesheet = f"""
            /* ===== Global shell ===== */
            * {{
                selection-background-color: {list_active_bg};
                selection-color: {list_active_fg};
            }}
            QWidget {{
                font-size: 13px;
            }}
            QMainWindow, QDialog, QWizard {{
                background-color: {wb};
                color: {igf};
            }}
            QToolTip {{
                background-color: {menu_bg};
                color: {menu_fg};
                border: 1px solid {border_soft};
                border-radius: {radius_sm};
                padding: 6px 8px;
            }}
            QLabel {{
                background: transparent;
                color: {igf};
            }}
            QLabel[muted="true"] {{
                color: {muted_fg};
            }}
            QFrame[frameShape="4"], QFrame[frameShape="5"] {{
                color: {ibd};
            }}
            QGroupBox {{
                background-color: {surface_1};
                border: 1px solid {border_soft};
                border-radius: {radius};
                margin-top: 14px;
                padding: 12px 10px 10px 10px;
                font-weight: 600;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                color: {muted_fg};
                font-weight: 600;
            }}
            QProgressBar {{
                background-color: {ib};
                border: 1px solid {border_soft};
                border-radius: {radius_sm};
                text-align: center;
                color: {igf};
                min-height: 14px;
            }}
            QProgressBar::chunk {{
                background-color: {ac};
                border-radius: {radius_sm};
            }}
            QCheckBox, QRadioButton {{
                spacing: 8px;
                color: {igf};
            }}
            QCheckBox::indicator, QRadioButton::indicator {{
                width: 15px;
                height: 15px;
            }}
            QCheckBox::indicator {{
                border: 1px solid {ibd};
                border-radius: 3px;
                background: {ib};
            }}
            QCheckBox::indicator:checked {{
                background: {ac};
                border-color: {ac};
            }}
            QRadioButton::indicator {{
                border: 1px solid {ibd};
                border-radius: 8px;
                background: {ib};
            }}
            QRadioButton::indicator:checked {{
                background: {ac};
                border-color: {ac};
            }}

            /* ===== Docks / explorer ===== */
            QDockWidget > QWidget {{
                background-color: {sb};
            }}
            QDockWidget {{
                background-color: {sb};
                color: {igf};
                titlebar-close-icon: url(none);
                titlebar-normal-icon: url(none);
                border: none;
            }}
            QDockWidget::title {{
                background-color: {surface_2};
                padding: 7px 10px;
                border-bottom: 1px solid {border_soft};
                text-align: left;
                font-weight: 600;
            }}
            QTreeView, QListWidget, QListView, QTableView {{
                background-color: {sb};
                border: none;
                color: {igf};
                outline: 0;
                alternate-background-color: {adj(sb, 98 if is_light else 104)};
                show-decoration-selected: 1;
            }}
            QTreeView::item, QListWidget::item, QListView::item {{
                padding: 3px 4px;
                min-height: 22px;
                border-radius: 3px;
            }}
            QTreeView::item:hover, QListWidget::item:hover, QListView::item:hover {{
                background-color: {list_hover_bg};
            }}
            QTreeView::item:selected:active, QListWidget::item:selected:active, QListView::item:selected:active {{
                background-color: {list_active_bg};
                color: {list_active_fg};
            }}
            QTreeView::item:selected:!active, QListWidget::item:selected:!active, QListView::item:selected:!active {{
                background-color: {list_inactive_bg};
                color: {list_inactive_fg};
            }}
            QHeaderView::section {{
                background-color: {surface_2};
                color: {muted_fg};
                padding: 6px 8px;
                border: none;
                border-bottom: 1px solid {border_soft};
                border-right: 1px solid {border_soft};
                font-weight: 600;
            }}
            QFrame#ExplorerToolbar {{
                background-color: {surface_2};
                border-bottom: 1px solid {border_soft};
                padding: 4px;
            }}

            /* ===== Buttons ===== */
            QPushButton {{
                background-color: {adj(bb, 100, 0.55)};
                color: {igf};
                border: 1px solid {border_soft};
                border-radius: {radius};
                padding: 6px 14px;
                min-height: 18px;
            }}
            QPushButton:hover {{
                background-color: {adj(bb, hover_factor)};
                border-color: {adj(ac, 100, 0.55)};
            }}
            QPushButton:pressed {{
                background-color: {adj(bb, pressed_factor)};
            }}
            QPushButton:default, QPushButton[primary="true"] {{
                background-color: {ac};
                color: #ffffff;
                border: 1px solid {adj(ac, 90 if is_light else 110)};
                font-weight: 600;
            }}
            QPushButton:default:hover, QPushButton[primary="true"]:hover {{
                background-color: {adj(ac, hover_factor)};
            }}
            QPushButton:disabled {{
                background-color: transparent;
                color: {adj(igf, 100, 0.35)};
                border: 1px solid {adj(ibd, 100, 0.35)};
            }}
            QToolButton {{
                background: transparent;
                border: 1px solid transparent;
                padding: 5px;
                margin: 1px;
                border-radius: {radius_sm};
            }}
            QToolButton:hover {{
                background-color: {adj(sb, 105 if is_light else 120)};
                border-color: {border_soft};
            }}
            QToolButton:pressed {{
                background-color: {adj(sb, 95 if is_light else 130)};
            }}
            QToolButton:checked {{
                background-color: {adj(ac, 100, 0.28)};
                border: 1px solid {adj(ac, 100, 0.55)};
            }}
            QToolBar {{
                background: {wb};
                border: none;
                border-bottom: 1px solid {border_soft};
                spacing: 4px;
                padding: 4px 6px;
            }}
            QToolBar::separator {{
                background: {border_soft};
                width: 1px;
                margin: 4px 6px;
            }}

            /* ===== Inputs ===== */
            QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QAbstractSpinBox {{
                background-color: {ib};
                color: {igf};
                border: 1px solid {border_soft};
                border-radius: {radius};
                padding: 6px 8px;
                selection-background-color: {list_active_bg};
            }}
            QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus,
            QSpinBox:focus, QDoubleSpinBox:focus, QAbstractSpinBox:focus {{
                border: 1px solid {ac};
            }}
            QComboBox {{
                background-color: {bb};
                color: {igf};
                border: 1px solid {border_soft};
                border-radius: {radius};
                padding: 5px 8px;
                min-height: 18px;
            }}
            QComboBox:hover {{
                border-color: {adj(ac, 100, 0.5)};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 22px;
            }}
            QComboBox::down-arrow {{ image: url({combo_arrow}); }}
            QComboBox QAbstractItemView {{
                background-color: {menu_bg};
                border: 1px solid {border_soft};
                color: {menu_fg};
                selection-background-color: {list_active_bg};
                selection-color: {list_active_fg};
                outline: 0;
                padding: 4px;
            }}
            QSpinBox::up-button, QSpinBox::down-button,
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {{
                border: none;
                width: 16px;
            }}
            QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {{ image: url({spin_up}); }}
            QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {{ image: url({spin_down}); }}

            /* ===== Menus / status ===== */
            QMenuBar {{
                background-color: {wb};
                border-bottom: 1px solid {border_soft};
                spacing: 2px;
            }}
            QMenuBar::item {{
                padding: 6px 12px;
                background: transparent;
                border-radius: {radius_sm};
                margin: 2px 1px;
            }}
            QMenuBar::item:selected {{
                background-color: {adj(wb, 95 if is_light else 120)};
            }}
            QMenu {{
                background-color: {menu_bg};
                border: 1px solid {border_soft};
                border-radius: {radius};
                color: {menu_fg};
                padding: 4px;
            }}
            QMenu::item {{
                padding: 6px 28px 6px 12px;
                border-radius: {radius_sm};
            }}
            QMenu::item:selected {{
                background-color: {list_active_bg};
                color: {list_active_fg};
            }}
            QMenu::separator {{
                height: 1px;
                background: {border_soft};
                margin: 4px 8px;
            }}
            QStatusBar {{
                background-color: {status_bg};
                color: {status_fg};
                border-top: 1px solid {border_soft};
            }}
            QStatusBar QLabel {{
                color: {status_fg};
                padding: 0 4px;
            }}
            QStatusBar::item {{
                border: none;
            }}

            /* ===== Tabs ===== */
            QTabWidget::pane {{
                border: 1px solid {border_soft};
                border-radius: 0 0 {radius} {radius};
                top: -1px;
                background: {wb};
            }}
            QTabBar::tab {{
                background: {tab_inactive_bg};
                color: {tab_inactive_fg};
                padding: 8px 16px;
                margin-right: 2px;
                border: 1px solid transparent;
                border-bottom: 2px solid transparent;
                border-top-left-radius: {radius};
                border-top-right-radius: {radius};
                min-width: 60px;
            }}
            QTabBar::tab:selected {{
                background: {tab_active_bg};
                color: {tab_active_fg};
                border-bottom: 2px solid {ac};
                font-weight: 600;
            }}
            QTabBar::tab:hover:!selected {{
                background: {adj(tab_inactive_bg, hover_factor)};
                color: {tab_active_fg};
            }}
            QTabBar::close-button {{
                margin: 2px;
            }}

            /* ===== Splitters / scrollbars ===== */
            QSplitter::handle {{
                background-color: {wb};
            }}
            QSplitter::handle:horizontal {{ width: 3px; }}
            QSplitter::handle:vertical {{ height: 3px; }}
            QSplitter::handle:hover {{ background-color: {adj(ac, 100, 0.55)}; }}
            QScrollBar:vertical {{
                border: none;
                background: {scrollbar_bg};
                width: 11px;
                margin: 0;
            }}
            QScrollBar::handle:vertical {{
                background: {scroll_handle};
                min-height: 28px;
                border-radius: 5px;
                margin: 2px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {adj(scroll_handle, hover_factor)};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background: none; }}
            QScrollBar:horizontal {{
                border: none;
                background: {scrollbar_bg};
                height: 11px;
                margin: 0;
            }}
            QScrollBar::handle:horizontal {{
                background: {scroll_handle};
                min-width: 28px;
                border-radius: 5px;
                margin: 2px;
            }}
            QScrollBar::handle:horizontal:hover {{
                background: {adj(scroll_handle, hover_factor)};
            }}
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0px; }}
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background: none; }}

            /* ===== Dialog chrome ===== */
            QDialogButtonBox QPushButton {{
                min-width: 84px;
            }}
            QMessageBox {{
                background-color: {wb};
            }}
            QMessageBox QLabel {{
                color: {igf};
            }}
        """
        app.setStyleSheet(stylesheet)