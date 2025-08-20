# /plugins/ai_suite/persona_logic.py
import os
from typing import List, Optional

# A sensible set of default directories to exclude from context.
EXCLUDE_DIRS = {'__pycache__', '.git', 'venv', '.venv', 'dist', 'build', 'node_modules', 'ai_exports', 'logs'}


def get_files_for_persona(persona_id: str, project_root: str) -> Optional[List[str]]:
    """
    Gets a list of recommended files to select for a given persona.
    Returns a list of files for personas with specific needs, or None for personas
    that should default to including all project files.
    """
    
    file_list = []
    has_specific_logic = False
    
    all_project_files = []
    for root, dirs, files in os.walk(project_root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            all_project_files.append(os.path.normpath(os.path.join(root, file)))

    if persona_id == "anya_the_architect":
        has_specific_logic = True
        patterns = ['main.py', 'app_core/', 'ui/main_window.py', 'plugins/']
        for file_path in all_project_files:
            relative_path = os.path.relpath(file_path, project_root).replace("\\", "/")
            if any(relative_path.startswith(p) for p in patterns):
                file_list.append(file_path)

    elif persona_id == "sofia_the_ux_visionary":
        has_specific_logic = True
        patterns = ['ui/', '.qss', '.css', '.html']
        for file_path in all_project_files:
            relative_path = os.path.relpath(file_path, project_root).replace("\\", "/")
            if any(relative_path.startswith(p) for p in patterns if p.endswith('/')) or \
               any(relative_path.endswith(p) for p in patterns if not p.endswith('/')):
                file_list.append(file_path)

    elif persona_id == "glitch_the_qa_maverick":
        has_specific_logic = True
        patterns = ['test', 'spec', 'fixture']
        for file_path in all_project_files:
            # Include any file that seems test-related
            if any(p in file_path.lower() for p in patterns):
                file_list.append(file_path)
    
    if has_specific_logic:
        return file_list
    else:
        # For other personas, return None to indicate no specific preference (use all files).
        return None