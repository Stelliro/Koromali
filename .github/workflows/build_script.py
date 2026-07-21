# .github/workflows/build_script.py
import os
import shutil
import argparse
import subprocess
import sys
from pathlib import Path

# --- Configuration ---
APP_NAME = "Koromali"
ORG_NAME = os.environ.get("KOROMALI_ORG_NAME", "Koromali")
MAIN_EXE = f"{APP_NAME}.exe"
TRAY_EXE = f"{APP_NAME}Tray.exe"
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DIST_DIR = ROOT_DIR / "dist"
ASSETS_DIR = ROOT_DIR / "assets"
TEMPLATE_NSI_PATH = ASSETS_DIR / "template.nsi"


def log(message):
    print(f"--- {message}")


def nsis_path(path) -> str:
    """Return an absolute path safe for NSIS string literals (forward slashes)."""
    return str(Path(path).resolve()).replace("\\", "/")


def ensure_installer_bitmaps():
    """Create simple BMP side/header images if missing (NSIS MUI expects them)."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        log("Pillow not available; will skip custom installer bitmaps if missing.")
        return

    header = ASSETS_DIR / "header.bmp"
    welcome = ASSETS_DIR / "welcome.bmp"

    def _make(path: Path, size: tuple[int, int], accent=(108, 158, 248)):
        img = Image.new("RGB", size, (30, 31, 36))
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, size[0], 8], fill=accent)
        d.rectangle([0, 0, 8, size[1]], fill=accent)
        img.save(path, format="BMP")
        log(f"Created installer bitmap: {path}")

    if not header.exists():
        # Classic MUI header size
        _make(header, (150, 57))
    if not welcome.exists():
        # Classic MUI welcome/finish side bitmap
        _make(welcome, (164, 314))


def prepare_source_directory():
    """Copies all necessary built files into a clean source directory for the installer."""
    log("Preparing files for installer...")
    source_dir = DIST_DIR / "installer_source"
    if source_dir.exists():
        shutil.rmtree(source_dir)
    source_dir.mkdir()

    # Copy main app files from PyInstaller's onedir output (preferred).
    main_app_dist = DIST_DIR / APP_NAME
    onefile_exe = DIST_DIR / MAIN_EXE
    if main_app_dist.is_dir():
        shutil.copytree(main_app_dist, source_dir, dirs_exist_ok=True)
        log(f"Copied main application from '{main_app_dist}'")
    elif onefile_exe.is_file():
        # Fallback for one-file PyInstaller builds.
        shutil.copy2(onefile_exe, source_dir / MAIN_EXE)
        log(f"Copied one-file main executable from '{onefile_exe}'")
    else:
        raise FileNotFoundError(
            f"Main app dist not found. Expected onedir '{main_app_dist}' "
            f"or onefile '{onefile_exe}'. Dist contents: {list(DIST_DIR.glob('*'))}"
        )

    # Copy tray app (onedir or onefile)
    tray_app_dist = DIST_DIR / f"{APP_NAME}Tray"
    tray_exe_path = tray_app_dist / TRAY_EXE
    tray_onefile = DIST_DIR / TRAY_EXE
    if tray_exe_path.is_file():
        shutil.copy2(tray_exe_path, source_dir / TRAY_EXE)
        log(f"Copied tray application from '{tray_app_dist}'")
    elif tray_onefile.is_file():
        shutil.copy2(tray_onefile, source_dir / TRAY_EXE)
        log(f"Copied tray one-file executable from '{tray_onefile}'")
    else:
        log(f"Tray executable not found; installer will omit {TRAY_EXE}")

    return source_dir


def build_nsis_defines(version, source_dir) -> list[str]:
    """Return makensis /D flags. Paths use forward slashes for NSIS."""
    ensure_installer_bitmaps()
    icon_path = ASSETS_DIR / "koromali.ico"
    if not icon_path.is_file():
        raise FileNotFoundError(f"Installer icon missing: {icon_path}")

    # Values only — compile_installer prefixes each with /D
    return [
        f"APP_NAME={APP_NAME}",
        f"APP_VERSION={version}",
        f"APP_AUTHOR={ORG_NAME}",
        f"MAIN_EXE={MAIN_EXE}",
        f"OUT_FILE={nsis_path(DIST_DIR / f'{APP_NAME}_{version}_Setup.exe')}",
        f"ASSETS_DIR={nsis_path(ASSETS_DIR)}",
        f"INSTALLER_ICON={nsis_path(icon_path)}",
        f"LICENSE_FILE={nsis_path(ROOT_DIR / 'LICENSE')}",
        f"BUILD_SOURCE_DIR={nsis_path(source_dir)}",
    ]


def generate_nsi_script(version, source_dir):
    """Dynamically creates the NSIS script from the template."""
    log("Generating NSIS script...")
    with open(TEMPLATE_NSI_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    # --- Section and Function Definitions ---
    sections = []
    functions = []
    descriptions = ['!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN']
    
    # Core Application Section
    src = nsis_path(source_dir)
    sections.append(
        'Section "Core Application" SEC_CORE\n'
        '  SectionIn RO\n'
        '  SetOutPath "$INSTDIR"\n'
        f'  File /r "{src}/*.*"\n'
        '  WriteUninstaller "$INSTDIR\\uninstall.exe"\n'
        '  CreateShortCut "$DESKTOP\\${APP_NAME}.lnk" "$INSTDIR\\${MAIN_EXE}"\n'
        '  CreateDirectory "$SMPROGRAMS\\${APP_NAME}"\n'
        '  CreateShortCut "$SMPROGRAMS\\${APP_NAME}\\${APP_NAME}.lnk" "$INSTDIR\\${MAIN_EXE}"\n'
        '  CreateShortCut "$SMPROGRAMS\\${APP_NAME}\\Uninstall ${APP_NAME}.lnk" "$INSTDIR\\uninstall.exe"\n'
        'SectionEnd'
    )
    descriptions.append('!insertmacro MUI_DESCRIPTION_TEXT ${SEC_CORE} "Installs the main application files and shortcuts."')

    # Optional File Associations
    assoc_exts = {
        ".py": "Python File", ".txt": "Text Document", ".md": "Markdown File",
        ".json": "JSON File", ".js": "JavaScript File", ".html": "HTML Document",
        ".css": "CSS Stylesheet", ".xml": "XML Document", ".yml": "YAML Document",
        ".c": "C Source File", ".cpp": "C++ Source File", ".h": "C/C++ Header File",
        ".cs": "C# Source File", ".rs": "Rust Source File"
    }
    
    # Generate registry keys for each association
    assoc_commands = ['Function RegisterFileAssociations']
    un_assoc_commands = ['Function un.UnregisterFileAssociations']
    for ext, desc in assoc_exts.items():
        prog_id = f'{APP_NAME}{ext}'
        assoc_commands.extend([
            f'  WriteRegStr HKCR "{ext}" "" "{prog_id}"',
            f'  WriteRegStr HKCR "{prog_id}" "" "{desc}"',
            f'  WriteRegStr HKCR "{prog_id}\\DefaultIcon" "" "$INSTDIR\\${MAIN_EXE},0"',
            f'  WriteRegStr HKCR "{prog_id}\\shell\\open\\command" "" \'"$INSTDIR\\${MAIN_EXE}" "%1"\'',
        ])
        un_assoc_commands.extend([
            f'  DeleteRegKey HKCR "{prog_id}"',
            f'  ReadRegStr $0 HKCR "{ext}" ""',
            f'  StrCmp $0 "{prog_id}" 0 +2',
            f'  DeleteRegKey HKCR "{ext}"',
        ])
    assoc_commands.append('FunctionEnd')
    un_assoc_commands.append('FunctionEnd')
    
    sections.append(
        'Section "File Associations" SEC_ASSOC\n'
        '  Call RegisterFileAssociations\n'
        'SectionEnd'
    )
    descriptions.append('!insertmacro MUI_DESCRIPTION_TEXT ${SEC_ASSOC} "Associate common code files with Koromali."')
    
    # System Tray Application
    sections.append(
        'Section "System Tray Application" SEC_TRAY\n'
        f'  CreateShortCut "$STARTUP\\${APP_NAME} Tray.lnk" "$INSTDIR\\{TRAY_EXE}"\n'
        'SectionEnd'
    )
    descriptions.append('!insertmacro MUI_DESCRIPTION_TEXT ${SEC_TRAY} "Launch Koromali in the background on system startup."')

    descriptions.append('!insertmacro MUI_FUNCTION_DESCRIPTION_END')
    functions.extend(assoc_commands)
    functions.extend(un_assoc_commands)
    
    # Uninstall Section (includes unregistering associations and app data)
    sections.append(
        'Section "Uninstall"\n'
        '  Call un.UnregisterFileAssociations\n'
        '  RMDir /r "$INSTDIR"\n'
        '  Delete "$DESKTOP\\${APP_NAME}.lnk"\n'
        '  RMDir /r "$SMPROGRAMS\\${APP_NAME}"\n'
        '  Delete "$STARTUP\\${APP_NAME} Tray.lnk"\n'
        '  RMDir /r "$LOCALAPPDATA\\${APP_AUTHOR}\\${APP_NAME}"\n' # Remove user settings and logs
        '  DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${PRODUCT_NAME}"\n'
        'SectionEnd'
    )

    # --- Combine and write script ---
    # Defines are passed on the makensis command line (/D), not injected here.
    generated_content = "\n".join(descriptions + sections)
    generated_functions = "\n".join(functions)

    final_script = template.replace('!GENERATED_CONTENT_GOES_HERE!', generated_content)
    final_script = final_script.replace('!GENERATED_FUNCTIONS_GOES_HERE!', generated_functions)

    generated_nsi_path = DIST_DIR / "installer.nsi"
    generated_nsi_path.write_text(final_script, encoding='utf-8')
    log(f"NSIS script generated at '{generated_nsi_path}'")
    return generated_nsi_path


def compile_installer(nsi_script_path, define_flags: list[str]):
    """Runs makensis.exe to compile the installer with /D defines."""
    log("Compiling installer with NSIS...")
    cmd = ["makensis"]
    for flag in define_flags:
        cmd.append(f"/D{flag}")
    cmd.append(str(nsi_script_path))
    log(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
        )
        log("Installer compiled successfully.")
        if result.stdout:
            log(f"NSIS STDOUT:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        log(f"NSIS compilation failed. STDOUT:\n{e.stdout}\n\nSTDERR:\n{e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        log("NSIS executable 'makensis' not found in PATH.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="CI build script for Koromali.")
    parser.add_argument("--version", required=True, help="The application version (e.g., 1.0.0).")
    args = parser.parse_args()

    source_dir = prepare_source_directory()
    define_flags = build_nsis_defines(args.version, source_dir)
    nsi_path = generate_nsi_script(args.version, source_dir)
    compile_installer(nsi_path, define_flags)
    log("Build process complete.")


if __name__ == "__main__":
    main()