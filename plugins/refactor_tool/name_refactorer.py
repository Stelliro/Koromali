# /plugins/refactor_tool/name_refactorer.py
import os
import re
from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple
from PyQt6.QtCore import QObject, QRunnable, pyqtSignal
from PyQt6.QtGui import QTextDocument
from utils.logger import log


class RefactorSignals(QObject):
    """Defines signals for the background refactoring worker."""
    progress = pyqtSignal(str)
    finished = pyqtSignal(list, list)  # modified_files, errors


# A new metaclass that inherits from the metaclasses of both QObject and ABCMeta.
# This resolves the metaclass conflict when a class inherits from both QRunnable (via QObject) and ABC.
class RunnableABCMeta(type(QObject), ABCMeta):
    pass


class ProjectFileWorker(QRunnable, ABC, metaclass=RunnableABCMeta):
    """An abstract base class for workers that process files in a project."""
    TEXT_EXTENSIONS = {
        '.py', '.md', '.json', '.html', '.css', '.js', '.ts', '.qss',
        '.xml', '.yml', '.yaml', '.txt', '.cfg', '.ini', '.c', '.cpp', '.h', '.hpp', '.cs'
    }
    IGNORE_DIRS = {'__pycache__', '.git', 'venv', '.venv', 'dist', 'build', 'node_modules'}

    def __init__(self, project_path: str):
        super().__init__()
        self.project_path = project_path
        self.is_cancelled = False
        self.signals = None # Subclasses must define this

    @abstractmethod
    def process_file(self, file_path: str):
        """Subclasses must implement this to perform work on each matching file."""
        pass

    def run(self):
        try:
            for root, dirs, files in os.walk(self.project_path, topdown=True):
                dirs[:] = [d for d in dirs if d not in self.IGNORE_DIRS]
                if self.is_cancelled:
                    break
                for filename in files:
                    if self.is_cancelled:
                        break
                    if os.path.splitext(filename)[1].lower() not in self.TEXT_EXTENSIONS:
                        continue
                    
                    full_path = os.path.join(root, filename)
                    if self.signals and hasattr(self.signals, 'progress'):
                        self.signals.progress.emit(os.path.relpath(full_path, self.project_path))
                    self.process_file(full_path)
        except Exception as e:
            log.error(f"Unexpected error during project file worker execution: {e}", exc_info=True)
            if self.signals and hasattr(self.signals, 'error'):
                self.signals.error.emit(f"An unexpected error occurred: {e}")

    def cancel(self):
        self.is_cancelled = True


class ProjectReplaceWorker(ProjectFileWorker):
    """A worker that performs find-and-replace across project files."""

    def __init__(self, project_path: str, old_text: str, new_text: str, find_flags):
        super().__init__(project_path)
        self.old_text = old_text
        self.new_text = new_text
        self.find_flags = find_flags
        self.signals = RefactorSignals()
        self.modified_files = []
        self.errors = []
        self.compiled_regex = self._compile_regex()

    def _compile_regex(self):
        re_flags = 0 if self.find_flags & QTextDocument.FindFlag.FindCaseSensitively else re.IGNORECASE
        
        pattern = re.escape(self.old_text)
        if self.find_flags & QTextDocument.FindFlag.FindWholeWords:
            pattern = r'\b' + pattern + r'\b'
        
        try:
            return re.compile(pattern, re_flags)
        except re.error as e:
            self.errors.append(f"Invalid regular expression for find: {e}")
            return None

    def run(self):
        self.modified_files = []
        self.errors = []
        if not self.compiled_regex: # Check if regex compilation failed
            self.signals.finished.emit([], self.errors)
            return
        super().run()
        self.signals.finished.emit(self.modified_files, self.errors)

    def process_file(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            if self.compiled_regex.search(content):
                new_content = self.compiled_regex.sub(self.new_text, content)
                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    self.modified_files.append(file_path)
        except (IOError, OSError) as e:
            log.warning(f"Could not read/write file during refactor: {file_path} - {e}")
            self.errors.append(f"Could not process {os.path.relpath(file_path, self.project_path)}: {e}")