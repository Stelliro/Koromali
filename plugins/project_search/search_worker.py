# /plugins/project_search/search_worker.py
import os
import re
from typing import Dict, List, Set, Tuple
from abc import ABC, abstractmethod, ABCMeta
from PyQt6.QtCore import QObject, pyqtSignal, QRunnable
from PyQt6.QtGui import QTextDocument
from utils.logger import log

class SearchWorkerSignals(QObject):
    """Defines signals for the background search worker."""
    progress = pyqtSignal(str)
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)


# A metaclass to resolve conflicts between QObject's metaclass and ABCMeta.
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
        self.signals = None  # Subclasses must define this

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


class ProjectSearchWorker(ProjectFileWorker):
    """A worker that performs find operations across project files."""
    
    def __init__(self, project_path, query, find_flags):
        super().__init__(project_path)
        self.query = query
        self.find_flags = find_flags
        self.signals = SearchWorkerSignals()
        self.results = {}
        self.compiled_regex = None

    def run(self):
        self.results = {}
        re_flags = 0 if self.find_flags & QTextDocument.FindFlag.FindCaseSensitively else re.IGNORECASE
        
        # Build the regex pattern based on find flags
        if self.find_flags & QTextDocument.FindFlag.FindWholeWords:
            query_regex = r'\b' + re.escape(self.query) + r'\b'
        else:
            query_regex = re.escape(self.query)
            
        try:
            self.compiled_regex = re.compile(query_regex, re_flags)
            super().run()  # Calls the parent run() which iterates through files
        except re.error as e:
            self.signals.error.emit(f"Invalid regular expression: {e}")
        finally:
            self.signals.finished.emit(self.results)
            
    def process_file(self, file_path: str):
        """Processes a single file, finding all matches for the query."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # This comprehension efficiently finds all matches in the file
                matches = [{'line': line_num, 'col': match.start(), 'line_text': line_text.strip()}
                           for line_num, line_text in enumerate(f, 1)
                           for match in self.compiled_regex.finditer(line_text)]
                
                if matches:
                    self.results[file_path] = matches
        except IOError as e:
            log.warning(f"Could not read file {file_path} during search: {e}")