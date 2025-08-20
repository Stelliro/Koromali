# Koromali/app_core/file_handler.py
import os
import sys
import shutil
import subprocess
import re
from typing import Optional, Tuple, Any, Dict, List, TYPE_CHECKING
from PyQt6.QtWidgets import (QFileDialog, QMessageBox, QComboBox, QLabel, QDialogButtonBox, QGridLayout,
                             QProgressDialog)
from PyQt6.QtGui import QGuiApplication, QDesktopServices
from PyQt6.QtCore import QUrl, pyqtSignal, QObject, Qt, QRunnable, QThreadPool

from utils.logger import log
from utils.helpers import clean_git_conflict_markers, is_binary_file, LARGE_FILE_SIZE_BYTES

if TYPE_CHECKING:
    from app_core.settings_manager import SettingsManager

class BOMWorkerSignals(QObject):
    """Defines signals available from a running BOMRemovalWorker."""
    progress = pyqtSignal(str)
    finished = pyqtSignal(int, int, list) # processed_count, fixed_count, errors

class BOMRemovalWorker(QRunnable):
    """
    A QRunnable worker that recursively finds and removes UTF-8 BOMs from text files.
    """
    TEXT_EXTENSIONS = {'.txt', '.py', '.md', '.json', '.html', '.css', '.js', '.xml', '.yml', '.yaml', '.toml', '.ini', '.cfg', '.h', '.hpp', '.c', '.cpp', '.cs', '.java', '.rs', '.go'}

    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.signals = BOMWorkerSignals()
        self.is_cancelled = False

    def run(self):
        processed = 0
        fixed = 0
        errors = []

        try:
            if os.path.isfile(self.path):
                processed, fixed = self._process_file(self.path)
            elif os.path.isdir(self.path):
                for root, _, files in os.walk(self.path):
                    if self.is_cancelled: break
                    for filename in files:
                        if self.is_cancelled: break
                        if os.path.splitext(filename)[1].lower() in self.TEXT_EXTENSIONS:
                            filepath = os.path.join(root, filename)
                            p, f = self._process_file(filepath)
                            processed += p
                            fixed += f
            else:
                errors.append(f"Path is not a valid file or directory: {self.path}")
        except Exception as e:
            errors.append(f"An unexpected error occurred: {e}")
            log.error(f"Error during BOM removal: {e}", exc_info=True)
        
        self.signals.finished.emit(processed, fixed, errors)

    def _process_file(self, filepath: str) -> Tuple[int, int]:
        """Checks and fixes a single file for a BOM. Returns (processed, fixed) count."""
        self.signals.progress.emit(os.path.basename(filepath))
        try:
            with open(filepath, 'rb') as f:
                bom = f.read(3)
            
            if bom == b'\xef\xbb\xbf':
                with open(filepath, 'rb') as f: content = f.read()
                with open(filepath, 'wb') as f: f.write(content[3:])
                return 1, 1 
            else:
                return 1, 0
        except (IOError, OSError):
            return 1, 0

    def cancel(self):
        self.is_cancelled = True

class SaveAsDialog(QFileDialog):
    """A custom file dialog that includes an encoding selector."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Save File As")
        self.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        self.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        self.encoding_map = {"UTF-8": "utf-8", "UTF-8 with BOM": "utf-8-sig", "UTF-16 LE": "utf-16le",
                             "UTF-16 BE": "utf-16be", "Latin-1 (ISO-8859-1)": "latin-1", "Windows-1252": "cp1252"}
        self.encoding_combo = QComboBox()
        self.encoding_combo.addItems(self.encoding_map.keys())
        layout = self.layout()
        if isinstance(layout, QGridLayout):
            if button_box := self.findChild(QDialogButtonBox):
                row, _, _, _ = layout.getItemPosition(layout.indexOf(button_box))
                layout.addWidget(QLabel("Encoding:"), row - 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)
                layout.addWidget(self.encoding_combo, row - 1, 1, 1, 2)

    def get_selected_encoding(self) -> str:
        return self.encoding_map.get(self.encoding_combo.currentText(), "utf-8")


class FileHandler(QObject):
    item_created = pyqtSignal(str, str)
    item_renamed = pyqtSignal(str, str, str)
    item_deleted = pyqtSignal(str, str)
    recent_files_changed = pyqtSignal()
    COMMON_ENCODINGS = ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1', 'cp1252']
    
    def __init__(self, settings_manager: "SettingsManager", parent_window: Optional[Any] = None):
        super().__init__()
        self.settings_manager = settings_manager
        self.parent_window = parent_window
        self.threadpool = QThreadPool()
        self.bom_worker = None
        self.progress_dialog = None
        self._internal_clipboard: Dict[str, Optional[str]] = { "operation": None, "path": None }

    def _read_with_encoding_detection(self, filepath: str) -> Tuple[Optional[str], Optional[str]]:
        for encoding in self.COMMON_ENCODINGS:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    content = f.read()
                log.info(f"Read file {filepath} with encoding {encoding}")
                return content, encoding
            except (UnicodeDecodeError, TypeError):
                continue
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            log.warning(f"Read {filepath} with UTF-8, ignoring errors.")
            return content, 'utf-8'
        except Exception:
            return None, None

    def new_file(self) -> Dict[str, Optional[str]]:
        log.info("FileHandler: new_file action invoked.")
        return { "content": "", "filepath": None, "new_file_default_name": "Untitled", "encoding": "utf-8" }

    def open_file_dialog(self) -> Optional[str]:
        last_dir = self.settings_manager.get("last_opened_directory", os.path.expanduser("~"))
        filepath, _ = QFileDialog.getOpenFileName(
            self.parent_window, 
            "Open File", 
            last_dir, 
            "All Supported Files (*.py *.pyw *.txt *.md *.json *.js *.html *.css *.c *.cpp *.h *.hpp *.cs *.rs);;All Files (*)"
        )
        if filepath:
            self.settings_manager.set("last_opened_directory", os.path.dirname(filepath))
        return filepath

    def save_file_content(self, filepath: Optional[str], content: str, save_as: bool = False, encoding: str = 'utf-8') -> Tuple[Optional[str], Optional[str]]:
        dir_exists = filepath and os.path.exists(os.path.dirname(filepath))
        final_encoding = encoding

        if save_as or not filepath or not dir_exists:
            last_dir = os.path.dirname(filepath) if dir_exists else self.settings_manager.get("last_saved_directory", os.path.expanduser("~"))
            sugg_name = os.path.basename(filepath) if filepath else "Untitled.py"

            dialog = SaveAsDialog(self.parent_window); dialog.setDirectory(last_dir); dialog.selectFile(sugg_name)
            dialog.setNameFilters(["Python Files (*.py *.pyw)", "Text Files (*.txt)", "Markdown (*.md)", "JSON (*.json)", "JavaScript (*.js)", "HTML (*.html *.htm)", "CSS (*.css)", "C++ Source (*.cpp *.cxx *.cc)", "C/C++ Header (*.h *.hpp)", "C# Source (*.cs)", "Rust (*.rs)", "All Files (*)"])

            if dialog.exec(): path_from_dialog, final_encoding = dialog.selectedFiles()[0], dialog.get_selected_encoding()
            else: return None, None 

            filepath = path_from_dialog
            self.settings_manager.set("last_saved_directory", os.path.dirname(filepath))
        
        try:
            temp_file = filepath + ".Koromali-save.tmp"
            with open(temp_file, 'w', encoding=final_encoding) as f: f.write(content)
            os.replace(temp_file, filepath)
            log.info(f"Atomically saved file '{filepath}' with encoding '{final_encoding}'.")
            return filepath, final_encoding
        except (IOError, OSError, UnicodeEncodeError) as e:
            msg = f"Error saving file '{filepath}' with encoding '{final_encoding}': {e}"
            log.error(msg, exc_info=True); QMessageBox.critical(self.parent_window, "Error Saving File", msg)
            if 'temp_file' in locals() and os.path.exists(temp_file): os.remove(temp_file)
            return None, None
            
    def remove_boms_in_path(self, path: str):
        if QMessageBox.question(self, "Confirm BOM Removal", "This will scan and remove the UTF-8 BOM from text files in place. Continue?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel) == QMessageBox.StandardButton.Cancel:
            return
        self.progress_dialog = QProgressDialog("Scanning for BOMs...", "Cancel", 0, 100, self.parent_window)
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.setWindowTitle("Removing BOMs")
        self.progress_dialog.setValue(0); self.progress_dialog.setAutoClose(False)

        self.bom_worker = BOMRemovalWorker(path)
        self.bom_worker.signals.progress.connect(self._on_bom_progress_update)
        self.bom_worker.signals.finished.connect(self._on_bom_finished)
        self.progress_dialog.canceled.connect(self.bom_worker.cancel)
        self.threadpool.start(self.bom_worker)

    def _on_bom_progress_update(self, filename: str):
        if self.progress_dialog: self.progress_dialog.setLabelText(f"Checking: {filename}")

    def _on_bom_finished(self, processed_count: int, fixed_count: int, errors: List[str]):
        if self.progress_dialog: self.progress_dialog.close()
        summary_message = f"BOM removal complete.\n\n- Files scanned: {processed_count}\n- Files fixed: {fixed_count}"
        if errors:
            summary_message += f"\n\nEncountered {len(errors)} error(s):\n" + "\n".join(errors[:3])
            if len(errors) > 3: summary_message += "\n... (see log for details)"
        QMessageBox.information(self.parent_window, "BOM Removal Complete", summary_message)
        if self.parent_window.explorer_panel: self.parent_window.explorer_panel.refresh()

    def create_file(self, path: str) -> Tuple[bool, Optional[str]]:
        try:
            if os.path.exists(path): return False, f"A {'folder' if os.path.isdir(path) else 'file'} named '{os.path.basename(path)}' already exists."
            with open(path, 'w', encoding='utf-8'): pass
            log.info(f"Created file: {path}"); self.item_created.emit("file", path); return True, None
        except OSError as e: log.error(f"Failed to create file at {path}: {e}", exc_info=True); return False, f"Failed to create file: {e}"

    def create_folder(self, path: str) -> Tuple[bool, Optional[str]]:
        try:
            if os.path.exists(path): return False, f"A {'folder' if os.path.isdir(path) else 'file'} named '{os.path.basename(path)}' already exists."
            os.makedirs(path); log.info(f"Created folder: {path}"); self.item_created.emit("folder", path); return True, None
        except OSError as e: log.error(f"Failed to create folder at {path}: {e}", exc_info=True); return False, f"Failed to create folder: {e}"

    def rename_item(self, old_path: str, new_name: str) -> Tuple[bool, str]:
        new_name = new_name.strip()
        if not new_name: return False, "Name cannot be empty."
        if re.search(r'[<>:"/\\|?*]', new_name): return False, 'Name contains illegal characters (\\ / : * ? " < > |).'
        new_path = os.path.join(os.path.dirname(old_path), new_name)

        if old_path.lower() == new_path.lower() and old_path != new_path:
            temp_path = old_path + '.Koromali_rename_temp'
            try:
                os.rename(old_path, temp_path); os.rename(temp_path, new_path)
                item_type = 'folder' if os.path.isdir(new_path) else 'file'
                self.item_renamed.emit(item_type, old_path, new_path); return True, new_path
            except OSError as e:
                log.error(f"Failed to case-rename '{old_path}': {e}", exc_info=True)
                if os.path.exists(temp_path): os.rename(temp_path, old_path)
                return False, f"Failed to rename: {e}"

        if os.path.exists(new_path): return False, f"'{new_name}' already exists."

        try:
            item_type = 'folder' if os.path.isdir(old_path) else 'file'; os.rename(old_path, new_path)
            log.info(f"Renamed '{old_path}' to '{new_path}'"); self.item_renamed.emit(item_type, old_path, new_path); return True, new_path
        except OSError as e: log.error(f"Failed to rename '{old_path}': {e}", exc_info=True); return False, f"Failed to rename: {e}"

    def delete_item(self, path):
        item_type = 'file' if os.path.isfile(path) else 'folder'
        try:
            if os.path.isfile(path): os.remove(path)
            elif os.path.isdir(path): shutil.rmtree(path)
            log.info(f"Deleted item: {path}"); self.item_deleted.emit(item_type, path); return True, None
        except (OSError, shutil.Error) as e: log.error(f"Failed to delete '{path}': {e}", exc_info=True); return False, f"Failed to delete: {e}"

    def copy_path_to_clipboard(self, path):
        try:
            QGuiApplication.clipboard().setText(os.path.normpath(path)); log.info(f"Copied path: {path}")
            if hasattr(self.parent_window, "statusBar"): self.parent_window.statusBar().showMessage("Path copied", 2000)
        except Exception as e: log.error(f"Could not copy path: {e}")

    def reveal_in_explorer(self, path):
        path = os.path.normpath(path)
        try:
            if sys.platform == 'win32': subprocess.run(['explorer', '/select,', path] if not os.path.isdir(path) else ['explorer', path])
            elif sys.platform == 'darwin': subprocess.run(['open', '-R', path])
            else: subprocess.run(['xdg-open', os.path.dirname(path)])
        except Exception as e: log.error(f"Could not open file browser: {e}"); QMessageBox.warning(self.parent_window, "Error", f"Could not open browser: {e}")

    def open_with_default_app(self, path):
        try: QDesktopServices.openUrl(QUrl.fromLocalFile(path))
        except Exception as e: log.error(f"Failed to open '{path}': {e}"); QMessageBox.warning(self.parent_window, "Error", f"Could not open file: {e}")

    def duplicate_item(self, path):
        dir, (base, ext) = os.path.dirname(path), os.path.splitext(os.path.basename(path))
        c, new_path = 1, os.path.join(dir, f"{base}_copy{ext}")
        while os.path.exists(new_path): c += 1; new_path = os.path.join(dir, f"{base}_copy_{c}{ext}")
        try:
            item_type = "folder" if os.path.isdir(path) else "file"
            if item_type == "file": shutil.copy2(path, new_path)
            else: shutil.copytree(path, new_path)
            log.info(f"Duplicated '{path}' to '{new_path}'"); self.item_created.emit(item_type, new_path); return True, None
        except (OSError, shutil.Error) as e: log.error(f"Failed to duplicate '{path}': {e}", exc_info=True); return False, f"Failed to duplicate: {e}"

    def cut_item(self, path): 
        self._internal_clipboard = {"operation": "cut", "path": path}
        if hasattr(self.parent_window, "statusBar"): self.parent_window.statusBar().showMessage(f"Cut: {os.path.basename(path)}", 3000)

    def copy_item(self, path): 
        self._internal_clipboard = {"operation": "copy", "path": path}
        if hasattr(self.parent_window, "statusBar"): self.parent_window.statusBar().showMessage(f"Copied: {os.path.basename(path)}", 3000)
        
    def paste_item(self, dest_dir):
        op, src = self._internal_clipboard.get("operation"), self._internal_clipboard.get("path")
        if not op or not src or not os.path.exists(src) or not os.path.isdir(dest_dir): return False, "Nothing to paste or invalid destination."
        dest = os.path.join(dest_dir, os.path.basename(src))
        if os.path.exists(dest): return False, f"'{os.path.basename(dest)}' already exists."
        try:
            itype = 'folder' if os.path.isdir(src) else 'file'
            if op == "cut":
                shutil.move(src, dest); log.info(f"Moved '{src}' to '{dest}'")
                self.item_renamed.emit(itype, src, dest); self._internal_clipboard = {"operation": None, "path": None}
            elif op == "copy":
                if os.path.isdir(src): shutil.copytree(src, dest)
                else: shutil.copy2(src, dest)
                log.info(f"Copied '{src}' to '{dest}'"); self.item_created.emit(itype, dest)
            return True, None
        except (OSError, shutil.Error) as e: log.error(f"Paste failed: {e}", exc_info=True); return False, f"Paste failed: {e}"

    def move_item(self, src_path, dest_dir):
        if not (os.path.exists(src_path) and os.path.isdir(dest_dir)): return False, "Invalid source or destination."
        dest = os.path.join(dest_dir, os.path.basename(src_path))
        if os.path.normpath(src_path) == os.path.normpath(dest): return True, dest
        if os.path.exists(dest): return False, f"'{os.path.basename(src_path)}' already exists."
        if os.path.isdir(src_path) and os.path.normpath(dest_dir).startswith(os.path.normpath(src_path)): return False, "Cannot move a folder into itself."
        try:
            itype = 'folder' if os.path.isdir(src_path) else 'file'; shutil.move(src_path, dest)
            log.info(f"Moved '{src_path}' to '{dest}'"); self.item_renamed.emit(itype, src_path, dest); return True, dest
        except (OSError, shutil.Error) as e: log.error(f"Move failed: {e}", exc_info=True); return False, f"Move failed: {e}"

    def copy_item_to_dest(self, src_path: str, dest_dir: str) -> Tuple[bool, Optional[str]]:
        if not (os.path.exists(src_path) and os.path.isdir(dest_dir)): return False, "Invalid source or destination."
        dest = os.path.join(dest_dir, os.path.basename(src_path))
        if os.path.exists(dest): return False, f"'{os.path.basename(src_path)}' already exists."
        try:
            itype = 'folder' if os.path.isdir(src_path) else 'file'
            if itype == 'folder': shutil.copytree(src_path, dest)
            else: shutil.copy2(src_path, dest)
            log.info(f"Copied '{src_path}' to '{dest}'"); self.item_created.emit(itype, dest); return True, dest
        except (OSError, shutil.Error) as e: log.error(f"Copy failed: {e}", exc_info=True); return False, f"Copy failed: {e}"

    def get_clipboard_status(self): return self._internal_clipboard.get("operation")
    def _add_to_recent_files(self, filepath):
        if not filepath: return
        recents = self.settings_manager.get("recent_files", []);
        if filepath in recents: recents.remove(filepath)
        recents.insert(0, filepath); max_files = self.settings_manager.get("max_recent_files", 10)
        self.settings_manager.set("recent_files", recents[:max_files]); self.recent_files_changed.emit()