# app_core/project_icon_manager.py
import os
from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QStyle
import qtawesome as qta
from utils.logger import log
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .settings_manager import SettingsManager
    from .theme_manager import ThemeManager

class ProjectIconManager:
    """Handles finding, creating, and customizing icons for projects."""

    def __init__(self, theme_manager: "ThemeManager", settings_manager: "SettingsManager"):
        self.theme_manager = theme_manager
        self.settings_manager = settings_manager

    def get_icon(self, project_path: str) -> QIcon:
        """
        Gets the appropriate icon for a project, considering customizations.
        """
        customizations = self.settings_manager.get('project_customizations', {})
        project_config = customizations.get(project_path, {})

        if custom_icon_path := project_config.get('icon_path'):
            if os.path.exists(custom_icon_path) and not QPixmap(custom_icon_path).isNull():
                return QIcon(QPixmap(custom_icon_path))
        
        if qta_icon_name := project_config.get('qta_icon_name'):
            color = project_config.get('icon_color') or self.theme_manager.current_theme_data.get('colors', {}).get('accent', '#83c092')
            return qta.icon(qta_icon_name, color=color)

        if (system_icon_enum_val := project_config.get('system_icon_enum')) is not None:
            try:
                icon = QApplication.style().standardIcon(QStyle.StandardPixmap(system_icon_enum_val))
                if not icon.isNull():
                    return icon
            except Exception as e:
                log.warning(f"Could not create system icon from enum: {e}")

        for icon_name in ['project.ico', 'favicon.ico', 'icon.ico']:
             if os.path.exists(ico_path := os.path.join(project_path, icon_name)) and not QPixmap(ico_path).isNull():
                 return QIcon(QPixmap(ico_path))

        if custom_color_str := project_config.get('icon_color'):
            return qta.icon('mdi.folder-outline', color=QColor(custom_color_str))
        
        colors = self.theme_manager.current_theme_data.get('colors', {})
        accent_color = colors.get('accent', '#83c092')
        return qta.icon('mdi.folder-open-outline', color=accent_color)

    def set_customization(self, project_path: str, icon_path: str = None, icon_color: str = None, system_icon_enum=None, qta_icon_name: str = None):
        """Saves a customization for a project's icon."""
        customizations = self.settings_manager.get('project_customizations', {})
        if project_path not in customizations:
            customizations[project_path] = {}

        customizations[project_path]['icon_path'] = icon_path or None
        customizations[project_path]['qta_icon_name'] = qta_icon_name or None
        customizations[project_path]['system_icon_enum'] = system_icon_enum if system_icon_enum is not None else None
        
        customizations[project_path]['icon_color'] = None if icon_path else (icon_color or None)

        self.settings_manager.set('project_customizations', customizations)
        log.info(f"Set icon customization for '{project_path}'")

    def clear_customization(self, project_path: str):
        """Removes any icon customizations for a project."""
        customizations = self.settings_manager.get('project_customizations', {})
        if project_path in customizations:
            customizations.pop(project_path)
            self.settings_manager.set('project_customizations', customizations)
            log.info(f"Cleared icon customization for '{project_path}'")