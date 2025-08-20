# Koromali/ui/explorer/icon_provider.py
import os
from PyQt6.QtWidgets import QFileIconProvider
from PyQt6.QtCore import QFileInfo
import qtawesome as qta
from app_core.koromali_api import KoromaliPluginAPI


class CustomFileIconProvider(QFileIconProvider):
    BINARY_EXTENSIONS = {'.exe', '.dll', '.so', '.o', '.a', '.lib', '.dylib', '.app', '.msi'}
    ICON_MAP = {
        ".git": "mdi.git", "__pycache__": "mdi.folder-cog-outline", "venv": "mdi.folder-cog-outline",
        ".venv": "mdi.folder-cog-outline", "dist": "mdi.folder-zip-outline", "build": "mdi.folder-zip-outline",
        "node_modules": "mdi.folder-npm-outline", "logs": "mdi.folder-text-outline",
        "tests": "mdi.folder-search-outline", "test": "mdi.folder-search-outline",
        ".vscode": "mdi.folder-vscode", ".idea": "mdi.folder-cog-outline",
        "Dockerfile": "mdi.docker", ".dockerignore": "mdi.docker", "docker-compose.yml": "mdi.docker",
        "OverlayApp": "mdi.git", ".gitattributes": "mdi.git", "pyproject.toml": "mdi.language-python",
        "poetry.lock": "mdi.language-python", "requirements.txt": "mdi.format-list-numbered",
        "package.json": "mdi.npm", "package-lock.json": "mdi.npm", "pnpm-lock.yaml": "mdi.npm", "yarn.lock": "mdi.npm",
        ".env": "mdi.key-variant", ".env.example": "mdi.key-outline",
        "README.md": "mdi.book-open-variant",
        ".py": "mdi.language-python", ".pyc": "mdi.language-python", ".pyw": "mdi.language-python",
        ".js": "mdi.language-javascript", ".mjs": "mdi.language-javascript", ".ts": "mdi.language-typescript",
        ".tsx": "mdi.language-typescript", ".java": "mdi.language-java", ".jar": "mdi.language-java",
        ".cs": "mdi.language-csharp", ".csproj": "mdi.language-csharp", ".cpp": "mdi.language-cpp",
        ".hpp": "mdi.language-cpp", ".c": "mdi.language-c", ".h": "mdi.language-c",
        ".rs": "mdi.language-rust", ".go": "mdi.language-go", ".rb": "mdi.language-ruby",
        ".php": "mdi.language-php", ".swift": "mdi.language-swift", ".kt": "mdi.language-kotlin",
        ".sh": "mdi.bash", ".bat": "mdi.powershell", ".ps1": "mdi.powershell",
        ".html": "mdi.language-html5", ".htm": "mdi.language-html5", ".css": "mdi.language-css3",
        ".scss": "mdi.language-css3", ".json": "mdi.code-json", ".xml": "mdi.xml",
        ".yaml": "mdi.yaml", ".yml": "mdi.yaml", ".toml": "mdi.cog-outline", ".ini": "mdi.cog-outline",
        ".cfg": "mdi.cog-outline", ".conf": "mdi.cog-outline", ".sql": "mdi.database", ".db": "mdi.database",
        ".sqlite3": "mdi.database", ".zip": "mdi.folder-zip-outline", ".rar": "mdi.folder-zip-outline",
        ".7z": "mdi.folder-zip-outline", ".tar": "mdi.folder-zip-outline", ".gz": "mdi.folder-zip-outline",
        ".bz2": "mdi.folder-zip-outline", ".png": "mdi.file-image", ".jpg": "mdi.file-image",
        ".jpeg": "mdi.file-image", ".gif": "mdi.file-image", ".bmp": "mdi.file-image",
        ".ico": "mdi.file-image", ".svg": "mdi.svg",
    }

    def __init__(self, koromali_api: KoromaliPluginAPI):
        super().__init__()
        self.api = koromali_api

    def icon(self, fileInfoOrType):
        if not isinstance(fileInfoOrType, QFileInfo):
            if isinstance(fileInfoOrType, QFileIconProvider.IconType):
                return super().icon(fileInfoOrType)
            return qta.icon('fa5s.file')

        file_info = fileInfoOrType
        main_window = self.api.get_main_window()
        if not main_window: return qta.icon('fa5s.file')

        theme_manager = main_window.theme_manager
        theme_data = theme_manager.current_theme_data or {}
        colors = theme_data.get('colors', {})
        icon_colors = colors.get('icon.colors', {})

        default_folder_color = icon_colors.get('default_folder', '#79b8f2')
        default_file_color = icon_colors.get('default_file', '#C0C5CE')

        # --- Live Share visual indicator ---
        shared_paths = main_window.get_shared_paths()
        is_hosted = False
        if shared_paths:
            try:
                norm_path = os.path.normpath(file_info.absoluteFilePath())
                if any(norm_path == p or norm_path.startswith(p + os.sep) for p in shared_paths):
                    is_hosted = True
            except Exception:
                pass

        base_icon_name = None
        color = None

        if file_info.isDir():
            folder_name = file_info.fileName()
            base_icon_name = self.ICON_MAP.get(folder_name, 'mdi.folder-outline')
            color = icon_colors.get(folder_name, default_folder_color)
        else:
            file_name = file_info.fileName()
            extension = f".{file_info.suffix().lower()}"
            if file_name in self.ICON_MAP:
                base_icon_name = self.ICON_MAP[file_name]
                color = icon_colors.get(file_name, default_file_color)
            elif extension in self.BINARY_EXTENSIONS:
                base_icon_name = 'mdi.cog'
                color = default_file_color
            elif extension in self.ICON_MAP:
                base_icon_name = self.ICON_MAP[extension]
                color = icon_colors.get(extension, default_file_color)

        if is_hosted:
            # If we don't have a mapped icon, provide a generic default for stacking
            if not base_icon_name:
                base_icon_name = 'mdi.file-outline' if not file_info.isDir() else 'mdi.folder-outline'
                color = default_file_color if not file_info.isDir() else default_folder_color
            
            return qta.icon(
                base_icon_name, 'fa5s.users',
                options=[
                    {'color': color},
                    {
                        'scale_factor': 0.6, 'offset': (0.15, 0.15),
                        'color': 'rgba(131, 192, 146, 0.9)'
                    }
                ]
            )

        if base_icon_name:
            return qta.icon(base_icon_name, color=color)

        return super().icon(file_info)