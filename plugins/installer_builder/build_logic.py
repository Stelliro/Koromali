# /plugins/installer_builder/build_logic.py
import os
import sys
import shutil
import tempfile
import struct
import subprocess
from pathlib import Path
from typing import Callable, Dict, Any, List


class BuildLogic:
    """Generates a dynamic NSIS script from a config dict and runs the build."""

    COLOR_MAP = {"HEADER": "#E5C07B", "OKBLUE": "#61AFEF", "OKGREEN": "#98C379", "FAIL": "#E06C75",
                   "DEFAULT": "#ABB2BF"}

    def __init__(self, log_callback: Callable[[str, str], None]):
        self.log = log_callback
        self.temp_dir = Path(tempfile.gettempdir()) / f"Koromali_builder_{os.getpid()}"
        self.build_source_dir = self.temp_dir / "source"
        self.generated_nsi_path = self.temp_dir / "generated_script.nsi"
        self._cleanup()

    def _cleanup(self):
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)
        self.temp_dir.mkdir(exist_ok=True, parents=True)
        self.build_source_dir.mkdir(exist_ok=True)

    def log_step(self, message: str):
        self.log(f"\n===== {message} =====", self.COLOR_MAP["HEADER"])

    def run_full_build(self, config: Dict[str, Any]) -> tuple[bool, str]:
        """Executes the entire build process based on the user's UI settings."""
        try:
            self._validate_config(config)
            self._run_pyinstaller_builds_if_needed(config)
            self._prepare_source_for_installer(config)
            self._generate_installer_assets(config)
            nsi_script = self._generate_nsi_script_content(config)
            self.generated_nsi_path.write_text(nsi_script, encoding='utf-8')
            self.log("Successfully generated dynamic NSIS script.", self.COLOR_MAP["OKGREEN"])

            self._run_command([config['build']['nsis_path'], str(self.generated_nsi_path)])

            output_file = Path(config['build']['output_dir']) / f"{config['metadata']['app_name']}_{config['metadata']['version']}_Setup.exe"
            return True, f"Build successful! Installer created at:\n{output_file}"
        except Exception as e:
            return False, f"Build failed: {e}"
        finally:
            self._cleanup()
            
    def _run_pyinstaller_builds_if_needed(self, config: Dict):
        """Runs PyInstaller for the main app and optionally for the tray app."""
        self.log_step("Checking Application Binaries")
        pyinstaller_path = shutil.which("pyinstaller")
        if not pyinstaller_path:
            raise FileNotFoundError("Could not find 'pyinstaller' in your system's PATH.")

        project_root = config['build']['project_root_dir']
        
        # Build Main Application
        self.log("Building main application...", self.COLOR_MAP["DEFAULT"])
        self._run_command([pyinstaller_path, "main.spec", "--noconfirm"], cwd=project_root)

        # Build Tray Application if requested
        if config['build']['install_tray_app']:
            self.log("Building tray application...", self.COLOR_MAP["DEFAULT"])
            self._run_command([pyinstaller_path, "tray_app.spec", "--noconfirm"], cwd=project_root)

    def _prepare_source_for_installer(self, config: Dict):
        """Copies all necessary built files into a clean source directory for the installer."""
        self.log_step("Preparing Files for Installer")
        project_root = Path(config['build']['project_root_dir'])
        app_name = config['metadata']['app_name']
        
        # Copy main app files
        main_app_dist = project_root / "dist" / app_name
        shutil.copytree(main_app_dist, self.build_source_dir, dirs_exist_ok=True)
        self.log(f"Copied main app from '{main_app_dist}'", self.COLOR_MAP["DEFAULT"])

        # Copy tray app if requested
        if config['build']['install_tray_app']:
            tray_app_dist = project_root / "dist" / f"{app_name}Tray"
            tray_exe_path = tray_app_dist / f"{app_name}Tray.exe"
            if tray_exe_path.exists():
                shutil.copy2(tray_exe_path, self.build_source_dir)
                self.log(f"Copied tray app from '{tray_app_dist}'", self.COLOR_MAP["DEFAULT"])
            else:
                self.log("Tray app executable not found after build, skipping.", self.COLOR_MAP["WARNING"])
        
        # Copy extra themes if requested
        if config['build']['install_extra_themes']:
            themes_src = project_root / "assets" / "themes"
            themes_dest = self.build_source_dir / "assets" / "themes"
            themes_dest.mkdir(parents=True, exist_ok=True)
            if (themes_src / "custom_themes.json").exists():
                shutil.copy2(themes_src / "custom_themes.json", themes_dest)
                self.log("Copied extra themes.", self.COLOR_MAP["DEFAULT"])
            else:
                self.log("custom_themes.json not found, skipping.", self.COLOR_MAP["WARNING"])

    def _validate_config(self, config: Dict):
        """Raises descriptive FileNotFoundError exceptions if paths are invalid."""
        self.log_step("Validating Configuration")
        if not Path(config['build']['nsis_path']).is_file():
            raise FileNotFoundError("Error: NSIS executable (makensis.exe) not found.")
        self.log("Configuration is valid.", self.COLOR_MAP["OKGREEN"])

    def _generate_installer_assets(self, config: Dict):
        """Creates placeholder icons and bitmaps if they are not provided by the user."""
        self.log_step("Preparing Installer Assets")
        if not config['build'].get('installer_icon_path'):
            self._create_ico(32, "#268bd2", self.temp_dir / "installer_icon.ico")

        self._create_bmp(496, 58, "#F0F0F0", self.temp_dir / "header.bmp")
        self._create_bmp(164, 314, "#FFFFFF", self.temp_dir / "welcome.bmp")

    def _run_command(self, command: list, cwd=None):
        """Runs a command-line process and pipes its output to the UI logger."""
        cmd_str = ' '.join(f'"{c}"' if ' ' in str(c) else str(c) for c in command)
        self.log(f"Executing: {cmd_str}", self.COLOR_MAP["OKBLUE"])

        startupinfo = None
        if sys.platform == "win32":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, encoding='utf-8', errors='ignore', startupinfo=startupinfo,
                                   cwd=cwd)
        for line in iter(process.stdout.readline, ''):
            if line:
                self.log(line.strip(), self.COLOR_MAP["DEFAULT"])
        process.wait()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, cmd_str, "Command failed.")

    def _generate_nsi_script_content(self, config: Dict) -> str:
        """Dynamically builds the entire NSIS script as a single string."""
        with open(config['build']['nsi_template_path'], 'r', encoding='utf-8') as f:
            template = f.read()
        
        m, b = config['metadata'], config['build']

        defines_list = [f'!define {k.upper()} "{v}"' for k, v in m.items()]
        installer_path = Path(b["output_dir"]) / f"{m['app_name']}_{m['version']}_Setup.exe"
        icon_path = b.get('installer_icon_path') or self.temp_dir / 'installer_icon.ico'

        defines_list.extend([
            f'!define OUT_FILE "{installer_path.resolve()}"',
            f'!define ASSETS_DIR "{self.temp_dir.resolve()}"',
            f'!define INSTALLER_ICON "{Path(icon_path).resolve()}"'
        ])
        if lic_path := b.get('license_path'):
            defines_list.append(f'!define LICENSE_FILE "{Path(lic_path).resolve()}"')

        # Generate Sections and Descriptions
        descriptions = ['!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN']
        sections = []

        # Core section
        sections.append('Section "Core Application" SEC_CORE\n  SectionIn RO\n' + '\n'.join(self._generate_install_commands(config)) + '\nSectionEnd')
        descriptions.append('!insertmacro MUI_DESCRIPTION_TEXT ${SEC_CORE} "Installs the main application files."')

        if b['install_extra_themes']:
             sections.append('Section "Extra Themes" SEC_THEMES\n  SetOutPath "$INSTDIR\\assets\\themes"\n  File "${BUILD_SOURCE_DIR}\\assets\\themes\\*.*"\nSectionEnd')
             descriptions.append('!insertmacro MUI_DESCRIPTION_TEXT ${SEC_THEMES} "Installs additional UI themes."')
        
        if b['install_tray_app']:
            sections.append('Section "System Tray Application" SEC_TRAY\n' + '\n'.join(self._generate_tray_install_commands(config)) + '\nSectionEnd')
            descriptions.append('!insertmacro MUI_DESCRIPTION_TEXT ${SEC_TRAY} "Adds a background application for quick launching from the system tray."')
            
        descriptions.append('!insertmacro MUI_FUNCTION_DESCRIPTION_END')

        # Insert generated content into template
        generated_content = "\n".join(defines_list + descriptions + sections)
        return template.replace('!GENERATED_CONTENT_GOES_HERE!', generated_content)

    def _generate_install_commands(self, config: Dict) -> list[str]:
        """Generates a list of NSIS commands for the main installation section."""
        b, m = config['build'], config['metadata']
        commands = [
            '  SetOutPath "$INSTDIR"',
            '  WriteUninstaller "$INSTDIR\\uninstall.exe"',
            f'  File /r "{self.build_source_dir.resolve()}\\*.*"'
        ]

        if b.get('desktop_shortcut'):
            commands.append(f'  CreateShortCut "$DESKTOP\\{m["app_name"]}.lnk" "$INSTDIR\\{m["main_exe"]}"')
        if b.get('start_menu_shortcut'):
            sm_folder = f'"$SMPROGRAMS\\{m["app_name"]}"'
            commands.extend([
                f'  CreateDirectory {sm_folder}',
                f'  CreateShortCut {sm_folder}\\{m["app_name"]}.lnk" "$INSTDIR\\{m["main_exe"]}"',
                f'  CreateShortCut {sm_folder}\\Uninstall.lnk" "$INSTDIR\\uninstall.exe"'
            ])
        
        return commands + self._generate_uninstall_commands(config)

    def _generate_tray_install_commands(self, config: Dict) -> List[str]:
        m = config['metadata']
        return [
            f'  CreateShortCut "$STARTUP\\{m["app_name"]} Tray.lnk" "$INSTDIR\\{m["app_name"]}Tray.exe"',
            f'  Delete "$STARTMENU\\Programs\\Startup\\{m["app_name"]}.lnk"' # Old cleanup
        ]

    def _generate_uninstall_commands(self, config: Dict) -> list[str]:
        m, b = config['metadata'], config['build']
        un_prefix = "  un."
        commands = [
            f'{un_prefix}RMDir /r "$INSTDIR"',
        ]

        if b.get('desktop_shortcut'):
            commands.append(f'{un_prefix}Delete "$DESKTOP\\{m["app_name"]}.lnk"')
        if b.get('start_menu_shortcut'):
            sm_folder = f'"$SMPROGRAMS\\{m["app_name"]}"'
            commands.extend([
                f'{un_prefix}Delete {sm_folder}\\Uninstall.lnk"',
                f'{un_prefix}Delete {sm_folder}\\{m["app_name"]}.lnk"',
                f'{un_prefix}RMDir {sm_folder}'
            ])
        
        if b.get('install_tray_app'):
            commands.append(f'{un_prefix}Delete "$STARTUP\\{m["app_name"]} Tray.lnk"')
            
        return commands

    def _create_ico(self, size, color, path):
        color_hex = color.lstrip('#')
        bgra = tuple(int(color_hex[i:i + 2], 16) for i in (4, 2, 0)) + (255,)
        dib = struct.pack('<lllHHLLllLL', 40, size, size * 2, 1, 32, 0, 0, 0, 0, 0, 0)
        dib += bytearray(struct.pack('<BBBB', *bgra) * (size * size))
        dib += bytearray([0x00] * (size * size // 8))
        with open(path, 'wb') as f:
            f.write(struct.pack('<HHH', 0, 1, 1) + struct.pack('<BBBBHHLL', size, size, 0, 0, 1, 32, len(dib), 22) + dib)
        self.log(f"Generated asset: {path.name}", self.COLOR_MAP["OKGREEN"])

    def _create_bmp(self, w, h, color, path):
        color_hex = color.lstrip('#')
        bgr = tuple(int(color_hex[i:i + 2], 16) for i in (4, 2, 0))
        pad = (4 - (w * 3) % 4) % 4
        file_header_size, info_header_size = 14, 40
        file_size = file_header_size + info_header_size + (w * 3 + pad) * h
        with open(path, 'wb') as f:
            f.write(b'BM' + struct.pack('<LHHLL', file_size, 0, 0, 54, info_header_size))
            f.write(struct.pack('<llHHLLllLL', w, h, 1, 24, 0, 0, 0, 0, 0, 0))
            for _ in range(h):
                f.write((struct.pack('BBB', *bgr) * w) + (b'\x00' * pad))
        self.log(f"Generated asset: {path.name}", self.COLOR_MAP["OKGREEN"])