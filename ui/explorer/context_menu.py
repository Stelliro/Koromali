# Koromali/ui/explorer/context_menu.py
import os
from functools import partial
from typing import List
from PyQt6.QtWidgets import QMenu, QApplication
from PyQt6.QtCore import QPoint
import qtawesome as qta

from app_core.project_manager import ProjectManager
from utils.logger import log


def populate_project_context_menu(panel, menu: QMenu, paths: List[str], is_dir: bool, project_manager: ProjectManager, target_dir_for_paste: str):
    """
    Populates a given QMenu with context actions for the project explorer.
    """
    if not paths: return

    is_multi_selection = len(paths) > 1
    first_path = paths[0]

    if not is_multi_selection and is_dir:
        menu.addAction(qta.icon('mdi.file-plus-outline'), "New File...", partial(panel._action_new_file, first_path))
        menu.addAction(qta.icon('mdi.folder-plus-outline'), "New Folder...", partial(panel._action_new_folder, first_path))
        menu.addSeparator()

    if not is_multi_selection:
        menu.addAction(qta.icon('mdi.content-cut'), "Cut", partial(panel._action_cut, first_path))
    
    # Pass the whole list of paths to the copy action
    menu.addAction(qta.icon('mdi.content-copy'), "Copy", partial(panel._action_copy, paths))
    
    if panel.file_handler.get_clipboard_status():
        paste_action = menu.addAction(qta.icon('mdi.content-paste'), "Paste")
        paste_action.triggered.connect(partial(panel._action_paste, target_dir_for_paste))
        if is_multi_selection:
            paste_action.setEnabled(False) # Can only paste into a single target directory
    
    menu.addSeparator()

    if not is_multi_selection:
        is_project_root = first_path in project_manager.get_open_projects()
        
        if is_project_root:
            ai_suite = panel.api.get_plugin_instance("ai_suite")
            if ai_suite:
                menu.addAction(qta.icon('mdi.archive-arrow-down-outline'), "Create Backup Export...",
                               partial(panel._action_export_for_backup, first_path))
                menu.addSeparator()

            menu.addAction(qta.icon('mdi.folder-cog-outline'), "Project Settings...",
                           partial(panel._show_project_settings_dialog, first_path))
            menu.addAction(qta.icon('mdi.folder-remove-outline'), "Close Project",
                           partial(project_manager.close_project, first_path))
            menu.addSeparator()

        menu.addAction(qta.icon('mdi.pencil-outline'), "Rename...", partial(panel._action_rename, first_path))

    menu.addAction(qta.icon('mdi.trash-can-outline', color='crimson'), f"Delete {len(paths)} Items" if is_multi_selection else "Delete",
                   partial(panel._action_delete, paths))
    
    if not is_multi_selection:
        menu.addAction(qta.icon('mdi.content-duplicate'), "Duplicate", partial(panel._action_duplicate, first_path))

    menu.addSeparator()

    if not is_multi_selection:
        menu.addAction(qta.icon('mdi.code-tags-check'), "Remove BOM from Files...", partial(panel._action_remove_boms, first_path))
        menu.addSeparator()

    if not is_multi_selection and not is_dir and first_path.lower().endswith(('.py', '.js', '.cpp', '.c', '.cs')):
        runner_plugin = panel.api.get_plugin_instance("script_runner")
        if runner_plugin and hasattr(runner_plugin, 'run_specific_script'):
            menu.addAction(qta.icon('mdi.play-outline', color='#4CAF50'), "Run Script",
                           lambda: runner_plugin.run_specific_script(first_path))
            menu.addSeparator()
            
    path_to_copy = os.path.normpath(first_path) if not is_multi_selection else "\n".join([os.path.normpath(p) for p in paths])
    path_copy_text = "Copy Path" if not is_multi_selection else "Copy Paths"
    abs_path_action = menu.addAction(qta.icon('mdi.link-variant'), path_copy_text)
    abs_path_action.triggered.connect(lambda: _copy_to_clipboard(path_to_copy))

    if not is_multi_selection and (project_path := project_manager.get_active_project_path()):
        try:
            relative_path = os.path.relpath(first_path, start=project_path)
            rel_path_action = menu.addAction(qta.icon('mdi.link-box-variant-outline'), "Copy Relative Path")
            rel_path_action.triggered.connect(lambda: _copy_to_clipboard(relative_path.replace("\\", "/")))
        except ValueError: pass 

    menu.addSeparator()
    menu.addAction("Reveal in Explorer", partial(panel.file_handler.reveal_in_explorer, first_path))

def _copy_to_clipboard(text: str):
    """Helper to copy text to the system clipboard."""
    try:
        QApplication.clipboard().setText(text)
    except Exception as e:
        log.error(f"Failed to copy to clipboard: {e}")