# Koromali/app_core/plugin_manager.py
import os
import sys
import json
import importlib
import importlib.util
import inspect
import zipfile
import tempfile
import shutil
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, Tuple, List
from utils.logger import log, get_app_data_path
from utils.helpers import get_base_path
from app_core.koromali_api import KoromaliPluginAPI  # Import API for type hinting

try:
    from packaging.version import Version, InvalidVersion
except ImportError:
    log.warning(
        "The 'packaging' library is not installed. Version comparison will be basic. Run 'pip install packaging'.")


    # Define dummy classes if 'packaging' is not available
    class _DummyVersion:
        def __init__(self, v): self.v = v

        def __eq__(self, o): return self.v == o.v

        def __lt__(self, o): return self.v < o.v

        def __le__(self, o): return self.v <= o.v

        def __gt__(self, o): return self.v > o.v

        def __ge__(self, o): return self.v >= o.v


    Version = _DummyVersion
    InvalidVersion = ValueError


@dataclass
class Plugin:
    """A dataclass to hold all information about a plugin."""
    manifest: Dict[str, Any]
    path: str
    source_type: str  # 'built-in', 'core-tool', 'user'
    is_core: bool = False
    is_loaded: bool = False
    enabled: bool = True
    module: Optional[Any] = None
    instance: Optional[Any] = None
    status_reason: str = "Not loaded"

    @property
    def id(self) -> str: return self.manifest.get('id', 'unknown')

    @property
    def name(self) -> str: return self.manifest.get('name', self.id)

    @property
    def version(self) -> str: return self.manifest.get('version', '0.0.0')


class PluginManager:
    ESSENTIAL_PLUGIN_IDS = {
        'python_tools',
    }

    def __init__(self, main_window):
        self.api: KoromaliPluginAPI = main_window.koromali_api
        base_app_path = get_base_path()
        app_data_path = get_app_data_path()
        self.built_in_plugins_dir = os.path.join(base_app_path, "plugins")
        self.core_tools_directory = os.path.join(base_app_path, "core_debug_tools")
        self.user_plugins_directory = os.path.join(app_data_path, "plugins")
        self.plugin_states_file = os.path.join(app_data_path, "plugin_states.json")
        self._ensure_paths_and_packages()
        self.plugins: Dict[str, Plugin] = {}
        log.info("PluginManager initialized with a shared API.")

    def _ensure_paths_and_packages(self):
        """Ensures all plugin directories are treated as Python packages."""
        base_path = get_base_path()
        paths_to_check = [
            base_path, # Ensure project root is in path
            self.user_plugins_directory,
            self.built_in_plugins_dir,
            self.core_tools_directory
        ]
        for path in paths_to_check:
            if path and path not in sys.path:
                sys.path.insert(0, path)
                log.info(f"Added to sys.path: {path}")

        # Ensure user plugins directory exists and is a package
        if not os.path.isdir(self.user_plugins_directory):
            log.info(f"Creating user plugins directory: {self.user_plugins_directory}")
            os.makedirs(self.user_plugins_directory)
        init_path = os.path.join(self.user_plugins_directory, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, 'w', encoding='utf-8') as f:
                f.write("# This file makes the user plugins directory a package.\n")

    def discover_and_load_plugins(self, ignore_list: Optional[List[str]] = None):
        log.info("Starting full plugin discovery and loading process...")
        ignore_list = ignore_list or []
        for plugin in self.get_loaded_plugins():
            self.unload_plugin(plugin.id)

        self.plugins.clear()
        self._discover_plugins()
        self._load_plugin_states()
        load_order = self._resolve_dependencies()
        for plugin_id in load_order:
            plugin = self.plugins.get(plugin_id)
            if plugin_id in ignore_list:
                log.info(f"Skipping plugin '{plugin.name if plugin else plugin_id}' as it's in the ignore list.")
                if plugin: plugin.status_reason = "Ignored (pre-loaded)"
                continue
            if plugin and plugin.enabled:
                self.load_plugin(plugin_id)
            elif plugin:
                log.info(f"Plugin '{plugin.name}' is disabled and will not be loaded.")
        log.info("Plugin discovery and loading complete.")

    def _discover_plugins(self):
        plugin_sources = {
            "built-in": self.built_in_plugins_dir,
            "core-tool": self.core_tools_directory,
            "user": self.user_plugins_directory,
        }
        for source_type, plugin_dir in plugin_sources.items():
            if not os.path.isdir(plugin_dir): continue
            for item_name in os.listdir(plugin_dir):
                if item_name.startswith(('__', '.')): continue
                plugin_path = os.path.join(plugin_dir, item_name)
                if os.path.isdir(plugin_path):
                    self._process_potential_plugin(plugin_path, source_type)

    def _process_potential_plugin(self, plugin_path: str, source_type: str):
        manifest_path = os.path.join(plugin_path, "plugin.json")
        if not os.path.exists(manifest_path): return
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            if not self._validate_manifest(manifest, manifest_path): return
            plugin_id = manifest['id']
            if plugin_id in self.plugins: return

            plugin = Plugin(manifest=manifest, path=plugin_path, source_type=source_type)
            plugin.is_core = plugin.id in self.ESSENTIAL_PLUGIN_IDS

            self.plugins[plugin_id] = plugin
        except (json.JSONDecodeError, IOError) as e:
            log.error(f"Failed to read or parse manifest at '{manifest_path}': {e}")

    def _validate_manifest(self, manifest: Dict, path: str) -> bool:
        for field in ['id', 'name', 'version']:
            if field not in manifest or not manifest[field]:
                log.error(f"Manifest at {path} is missing or has empty field: '{field}'. Skipping.")
                return False
        return True

    def _resolve_dependencies(self) -> List[str]:
        log.info("Resolving plugin dependencies...")
        all_plugin_ids = set(self.plugins.keys())
        dependencies = {}
        for pid, p in self.plugins.items():
            deps_field = p.manifest.get('dependencies', {})
            internal_deps = {dep_id: ver for dep_id, ver in deps_field.items() if dep_id in all_plugin_ids}
            dependencies[pid] = set(internal_deps.keys())

        load_order, resolved = [], set()
        while len(load_order) < len(self.plugins):
            ready_to_load = {pid for pid, deps in dependencies.items() if pid not in resolved and not deps - resolved}
            if not ready_to_load:
                unresolved = {pid: deps - resolved for pid, deps in dependencies.items() if pid not in resolved}
                log.error(f"Could not resolve plugin dependencies. Circular or missing. Unresolved: {unresolved}")
                for pid in unresolved:
                    if pid in self.plugins:
                        self.plugins[pid].enabled = False
                        self.plugins[pid].status_reason = f"Unresolved dependencies: {unresolved[pid]}"
                resolved.update(unresolved.keys()) # Mark as resolved to break loop
                continue

            for plugin_id in sorted(list(ready_to_load)):
                # This loop continues from previous logic
                plugin = self.plugins.get(plugin_id)
                if plugin:
                    load_order.append(plugin_id)
                resolved.add(plugin_id)
                
        # Append any plugins that were part of the cycle but weren't added yet
        remaining = all_plugin_ids - set(load_order)
        load_order.extend(list(remaining))
        
        log.info(f"Plugin load order determined: {load_order}")
        return load_order


    def _check_version(self, installed_version: str, required_version_spec: str) -> bool:
        try:
            installed, spec = Version(installed_version), required_version_spec.strip()
            if spec.startswith('>='): return installed >= Version(spec[2:])
            if spec.startswith('<='): return installed <= Version(spec[2:])
            if spec.startswith('=='): return installed == Version(spec[2:])
            if spec.startswith('>'): return installed > Version(spec[1:])
            if spec.startswith('<'): return installed < Version(spec[1:])
            return installed == Version(spec)
        except (InvalidVersion, ValueError) as e:
            log.warning(
                f"Could not parse version. installed='{installed_version}', required='{required_version_spec}'. Error: {e}")
            return False

    def load_plugin(self, plugin_id: str) -> bool:
        plugin = self.plugins.get(plugin_id)
        if not plugin or plugin.is_loaded: return False

        entry_point = plugin.manifest.get("entry_point", "plugin_main.py")
        entry_point_path = os.path.join(plugin.path, entry_point)

        if not os.path.exists(entry_point_path):
            plugin.status_reason = f"Entry point '{entry_point}' not found."
            log.error(f"{plugin.status_reason} for plugin '{plugin.name}'.")
            return False

        # Construct a proper Python module path
        entry_module_name = os.path.splitext(entry_point)[0]
        plugin_dir_name = os.path.basename(os.path.dirname(plugin.path)) # 'plugins', 'core_debug_tools' etc.
        
        # Ensure correct package name based on location
        if plugin.source_type == 'user':
            # User plugins are directly in the user plugins path
             module_name = f"{plugin_id}.{entry_module_name}"
        else:
             module_name = f"{plugin_dir_name}.{plugin_id}.{entry_module_name}"

        try:
            if module_name in sys.modules:
                 log.warning(f"Reloading already imported module: {module_name}")
                 del sys.modules[module_name]

            spec = importlib.util.spec_from_file_location(module_name, entry_point_path)
            if not spec or not spec.loader: raise ImportError(f"Could not create module spec for {module_name}")
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            if hasattr(module, 'initialize'):
                plugin.instance = module.initialize(self.api)
                plugin.module = module
                plugin.is_loaded = True
                plugin.status_reason = "Loaded successfully"
                log.info(f"Successfully initialized plugin: '{plugin.name}' (Version: {plugin.version})")
                return True
            else:
                plugin.status_reason = "No 'initialize' function found."
                log.error(f"Plugin '{plugin.name}' has no 'initialize' function. Skipping.")
                if module_name in sys.modules: del sys.modules[module_name]
                return False
        except Exception as e:
            plugin.status_reason = f"Load error: {e}"
            log.error(f"An unexpected error occurred loading plugin '{plugin.name}': {e}", exc_info=True)
            if module_name in sys.modules: del sys.modules[module_name]
            return False

    def unload_plugin(self, plugin_id: str) -> bool:
        plugin = self.plugins.get(plugin_id)
        if not plugin or not plugin.is_loaded: return True
        log.info(f"Unloading plugin: '{plugin.name}'")
        try:
            if hasattr(plugin.instance, 'shutdown'): plugin.instance.shutdown()

            plugin.is_loaded = False
            plugin.instance = None
            module_name = plugin.module.__name__ if plugin.module else None
            plugin.module = None

            if module_name and module_name in sys.modules:
                del sys.modules[module_name]

            import gc
            gc.collect()

            plugin.status_reason = "Unloaded";
            log.info(f"Successfully unloaded plugin '{plugin.name}'.")
            return True
        except Exception as e:
            plugin.status_reason = f"Unload error: {e}";
            log.error(f"Error during shutdown of plugin '{plugin.name}': {e}", exc_info=True)
            return False

    def reload_plugin(self, plugin_id: str) -> bool:
        log.info(f"Reloading plugin '{plugin_id}'...")
        if self.unload_plugin(plugin_id):
            return self.load_plugin(plugin_id)
        log.error(f"Failed to unload plugin '{plugin_id}' during reload process.")
        return False

    def enable_plugin(self, plugin_id: str):
        plugin = self.plugins.get(plugin_id)
        if not plugin:
            log.error(f"Cannot enable non-existent plugin '{plugin_id}'")
            return
        plugin.enabled = True
        self._save_plugin_states()
        log.info(f"Plugin '{plugin.name}' enabled. Re-evaluating and loading plugins.")
        self.discover_and_load_plugins()

    def disable_plugin(self, plugin_id: str):
        plugin = self.plugins.get(plugin_id)
        if not plugin:
            log.error(f"Cannot disable non-existent plugin '{plugin_id}'")
            return

        plugin.enabled = False
        self._save_plugin_states()
        log.info(f"Plugin '{plugin.name}' disabled. Re-evaluating all plugins.")
        self.discover_and_load_plugins()

    def enable_all(self):
        log.info("Enabling all plugins.")
        for plugin in self.plugins.values():
            plugin.enabled = True
        self._save_plugin_states()
        log.info("All plugins enabled. Re-evaluating and loading all plugins.")
        self.discover_and_load_plugins()

    def disable_all_non_core(self):
        log.info("Disabling all non-essential plugins.")
        plugins_to_disable_ids = [p.id for p in self.plugins.values() if not p.is_core]

        if not plugins_to_disable_ids:
            log.info("No non-essential plugins to disable.")
            return

        for plugin_id in plugins_to_disable_ids:
            plugin = self.plugins.get(plugin_id)
            if plugin:
                plugin.enabled = False

        self._save_plugin_states()
        log.info(f"Marked {len(plugins_to_disable_ids)} non-essential plugins as disabled. Re-evaluating all plugins.")
        self.discover_and_load_plugins()

    def _load_plugin_states(self):
        if not os.path.exists(self.plugin_states_file): return
        try:
            with open(self.plugin_states_file, 'r', encoding='utf-8') as f:
                states = json.load(f)
            for pid, state in states.items():
                if pid in self.plugins and isinstance(state, dict): self.plugins[pid].enabled = state.get('enabled',
                                                                                                          True)
        except (IOError, json.JSONDecodeError) as e:
            log.warning(f"Could not load plugin states from {self.plugin_states_file}: {e}")

    def _save_plugin_states(self):
        states = {pid: {'enabled': p.enabled} for pid, p in self.plugins.items()}
        try:
            with open(self.plugin_states_file, 'w', encoding='utf-8') as f:
                json.dump(states, f, indent=4)
        except IOError as e:
            log.error(f"Could not save plugin states to {self.plugin_states_file}: {e}")

    def get_all_plugins(self) -> List[Plugin]:
        return list(self.plugins.values())

    def get_installed_plugins(self) -> list:
        installed_plugins_data = []
        for p in self.get_all_plugins():
            plugin_data = p.manifest.copy()
            plugin_data['path'] = p.path
            plugin_data['source_type'] = p.source_type
            installed_plugins_data.append(plugin_data)
        return installed_plugins_data

    def get_loaded_plugins(self) -> List[Plugin]:
        return [p for p in self.plugins.values() if p.is_loaded]

    def get_plugin_instance_by_id(self, plugin_id: str) -> Optional[Any]:
        plugin = self.plugins.get(plugin_id)
        if plugin and plugin.is_loaded:
            return plugin.instance
        return None

    def install_plugin_from_zip(self, zip_filepath: str) -> Tuple[bool, str]:
        if not zipfile.is_zipfile(zip_filepath): return False, "Not a valid zip archive."
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                with zipfile.ZipFile(zip_filepath, 'r') as z:
                    z.extractall(temp_dir)
                items = os.listdir(temp_dir);
                is_nested = len(items) == 1 and os.path.isdir(os.path.join(temp_dir, items[0]))
                src_dir = os.path.join(temp_dir, items[0]) if is_nested else temp_dir
                manifest_path = os.path.join(src_dir, 'plugin.json')
                if not os.path.exists(manifest_path): return False, "Archive is missing 'plugin.json'."
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    manifest = json.load(f)
                if not self._validate_manifest(manifest, manifest_path): return False, "Plugin manifest is invalid."
                plugin_id = manifest['id'];
                target_path = os.path.join(self.user_plugins_directory, plugin_id)
                if os.path.exists(target_path): return False, f"A plugin with ID '{plugin_id}' already exists."
                shutil.move(src_dir, target_path);
                plugin_name = manifest.get('name', plugin_id)
                log.info(f"Plugin '{plugin_name}' installed. Reloading plugins...")
                self.discover_and_load_plugins()
                return True, f"Plugin '{plugin_name}' installed and loaded."
        except Exception as e:
            log.error(f"Failed to install plugin from {zip_filepath}: {e}", exc_info=True)
            return False, f"An unexpected error occurred: {e}"

    def uninstall_plugin(self, plugin_id: str) -> Tuple[bool, str]:
        plugin = self.plugins.get(plugin_id)
        if not plugin: return False, f"Plugin '{plugin_id}' is not installed."
        if plugin.source_type != 'user':
            return False, "This is a built-in or core tool and cannot be uninstalled."

        self.unload_plugin(plugin_id)
        target_path = os.path.join(self.user_plugins_directory, plugin_id)
        if not os.path.isdir(target_path): return False, f"Plugin directory for '{plugin_id}' not found."
        try:
            shutil.rmtree(target_path)
            if plugin_id in self.plugins: del self.plugins[plugin_id]
            self._save_plugin_states()
            log.info(f"Successfully uninstalled plugin '{plugin_id}'.")
            return True, f"Plugin '{plugin_id}' was uninstalled."
        except OSError as e:
            log.error(f"Failed to uninstall plugin '{plugin_id}': {e}", exc_info=True)
            return False, f"Error removing plugin directory: {e}"