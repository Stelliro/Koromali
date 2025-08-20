# Koromali/updater.py
import sys
import os
import time
import requests
import zipfile
import shutil

# Default app name, can be overridden by a command-line argument.
APP_NAME = "Koromali"

# A set of files and folders that the updater will NEVER overwrite to preserve user settings.
# This will be dynamically updated if a new APP_NAME is provided via args.
PROTECTED_ITEMS = {
    f"{APP_NAME}_editor_settings.json",
    "logs",
    "assets/themes/custom_themes.json"
}


def log(message: str):
    """Simple logger for the updater script that prints to stdout."""
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def _copy_protected_items(install_dir: str, source_dir: str):
    """Copies user-specific files from the old install directory to the new one."""
    log("Copying protected user files to new version...")
    for item in PROTECTED_ITEMS:
        src_path = os.path.join(install_dir, item.replace('/', os.sep))
        dest_path = os.path.join(source_dir, item.replace('/', os.sep))

        if os.path.exists(src_path):
            try:
                # Ensure the destination directory exists before copying.
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                else:
                    shutil.copy2(src_path, dest_path)
                log(f"  - Preserved '{item}'")
            except Exception as e:
                log(f"  - WARNING: Could not preserve '{item}': {e}")
    log("Finished preserving protected files.")


def atomic_update(install_dir: str, source_dir: str):
    """
    Performs a robust, atomic update by renaming directories. This minimizes
    the risk of a corrupted installation if the process is interrupted.
    """
    backup_dir = f"{install_dir}_backup_{int(time.time())}"
    log(f"Creating backup of current installation at: {backup_dir}")

    try:
        # 1. Preserve user settings by copying them into the new version's folder.
        _copy_protected_items(install_dir, source_dir)

        # 2. Atomically move the current installation to a backup location.
        os.rename(install_dir, backup_dir)
        log(f"Moved current version to backup directory.")

        # 3. Atomically move the new, updated version into the correct location.
        os.rename(source_dir, install_dir)
        log(f"New version moved into place.")

        # 4. If everything was successful, clean up the backup.
        log("Update appears successful. Removing backup directory...")
        shutil.rmtree(backup_dir, ignore_errors=True)
        log("Update successfully installed.")

    except Exception as e:
        log(f"FATAL ERROR during update process: {e}")
        log("Attempting to restore from backup...")
        # If anything failed, try to restore the original directory.
        if os.path.exists(backup_dir):
            if os.path.exists(install_dir):
                shutil.rmtree(install_dir, ignore_errors=True)
            try:
                os.rename(backup_dir, install_dir)
                log("Successfully restored previous version from backup.")
            except Exception as restore_e:
                log(f"CRITICAL: FAILED TO RESTORE BACKUP. {restore_e}")
                log("The application is likely in a broken state.")
        else:
            log("CRITICAL: No backup directory found to restore from.")
        raise e  # Re-raise the exception to signal failure.


def main():
    global APP_NAME, PROTECTED_ITEMS

    if len(sys.argv) < 3:
        log("Error: Missing arguments. "
            "Usage: python updater.py <download_url> <install_dir> [pid] [app_name]")
        sys.exit(1)

    download_url = sys.argv[1]
    install_dir = sys.argv[2]
    pid_to_wait = None

    if len(sys.argv) > 3:
        try:
            pid_to_wait = int(sys.argv[3])
        except (ValueError, IndexError):
            log("Invalid PID provided. Falling back to a simple sleep timer.")
            time.sleep(2)
    else:
        log("No PID provided. Waiting for 2 seconds to allow the main app to close...")
        time.sleep(2)

    if len(sys.argv) > 4:
        APP_NAME = sys.argv[4]
        # Re-populate protected items with the correct app name
        PROTECTED_ITEMS = {
            f"{APP_NAME}_editor_settings.json", "logs", "assets/themes/custom_themes.json"
        }

    log(f"{APP_NAME} Updater started.")
    
    # Use the parent of the install dir for temporary files to avoid permission issues.
    temp_root = os.path.dirname(install_dir)
    temp_extract_dir = os.path.join(temp_root, f"{APP_NAME}_update_temp")
    zip_path = os.path.join(temp_extract_dir, "update.zip")

    log(f"Update requested for directory: {install_dir}")
    log(f"Downloading from: {download_url}")

    # If psutil is available, use it for a more reliable PID-based wait.
    if pid_to_wait:
        try:
            import psutil
            log(f"Waiting for main application (PID: {pid_to_wait}) to exit...")
            p = psutil.Process(pid_to_wait)
            p.wait(timeout=10)
            log("Main application has exited.")
        except ImportError:
            log("psutil not found. Falling back to a simple sleep timer.")
            time.sleep(2)
        except (psutil.NoSuchProcess, psutil.TimeoutExpired) as e:
            log(f"Could not wait for PID {pid_to_wait}: {e}. Proceeding with update.")
        except Exception as e:
            log(f"An unexpected error occurred while waiting for PID: {e}")
            time.sleep(2)

    try:
        # Prepare a clean temporary extraction directory.
        if os.path.exists(temp_extract_dir):
            shutil.rmtree(temp_extract_dir)
        os.makedirs(temp_extract_dir, exist_ok=True)

        log("Downloading new version...")
        response = requests.get(download_url, stream=True, timeout=30)
        response.raise_for_status()

        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        log("Download complete.")

        log("Unzipping update...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_extract_dir)
        log("Unzip complete.")

        # Determine the correct source directory within the unzipped content.
        extracted_content = os.listdir(temp_extract_dir)
        source_dir = temp_extract_dir
        potential_dirs = [d for d in extracted_content if os.path.isdir(os.path.join(temp_extract_dir, d))]
        if len(potential_dirs) == 1:
            log(f"Update appears to be in a root folder: {potential_dirs[0]}")
            source_dir = os.path.join(temp_extract_dir, potential_dirs[0])

        atomic_update(install_dir, source_dir)

    except Exception as e:
        log(f"An error occurred during the update process: {e}")
        # In a real-world scenario, you might want to show a message box here.
        return
    finally:
        log("Cleaning up temporary files...")
        shutil.rmtree(temp_extract_dir, ignore_errors=True)

    log("Update process finished. The application can now be relaunched.")


if __name__ == "__main__":
    main()