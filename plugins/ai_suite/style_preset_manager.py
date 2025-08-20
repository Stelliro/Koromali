# /plugins/ai_suite/style_preset_manager.py


def _validate_preset(data: Dict[str, Any]) -> Dict[str, str]:
"""Return a sanitized copy of a preset dict. Only string->string entries are allowed."""
out: Dict[str, str] = {}
for k, v in (data or {}).items():
if isinstance(k, str) and isinstance(v, str):
out[k] = v
return out


class StylePresetManager:
def __init__(self) -> None:
base = get_base_path()
self._dir = os.path.join(base, ".koromali")
self._file = os.path.join(self._dir, "style_presets.json")
self._presets: Dict[str, Dict[str, str]] = {}
self._load()


def list_presets(self) -> List[str]:
names = list(self._presets.keys())
# Keep "Default" first, avoid case-duplicate
names.sort(key=lambda n: (0 if n.lower() == "default" else 1, n.lower()))
return names


def get_preset(self, name: str) -> Dict[str, str]:
return dict(self._presets.get(name, DEFAULT_PRESETS["Default"]))


def set_preset(self, name: str, data: Dict[str, str]) -> None:
clean_name = (name or "Unnamed").strip()
if not clean_name:
clean_name = "Preset"
# Normalize to Title Case except known "Default"
if clean_name.lower() == "default":
clean_name = "Default"
else:
clean_name = clean_name[:1].upper() + clean_name[1:]


clean_data = _validate_preset(data)
if not clean_data:
raise ValueError("Preset must contain at least one string key/value")


self._presets[clean_name] = clean_data
self._save()


def delete_preset(self, name: str) -> bool:
if name.lower() == "default":
return False
removed = self._presets.pop(name, None) is not None
if removed:
self._save()
return removed


# ---- internal I/O ----
def _load(self) -> None:
try:
os.makedirs(self._dir, exist_ok=True)
if os.path.exists(self._file):
with open(self._file, "r", encoding="utf-8") as f:
loaded = json.load(f)
else:
loaded = {}
if not isinstance(loaded, dict):
loaded = {}
except Exception as e:
log.warning(f"Could not load style presets: {e}")
loaded = {}
# Sanitize values to str->str
safe_loaded: Dict[str, Dict[str, str]] = {}
for key, val in loaded.items():
if not isinstance(key, str) or not isinstance(val, dict):
continue
safe_loaded[key] = _validate_preset(val)
self._presets = {**DEFAULT_PRESETS, **safe_loaded}


def _save(self) -> None:
try:
os.makedirs(self._dir, exist_ok=True)
# Save only non-defaults and only if they differ from defaults
to_save: Dict[str, Dict[str, str]] = {}
for k, v in self._presets.items():
if k in DEFAULT_PRESETS and v == DEFAULT_PRESETS[k]:
continue
to_save[k] = v
with open(self._file, "w", encoding="utf-8") as f:
json.dump(to_save, f, indent=2, ensure_ascii=False)
except Exception as e:
log.warning(f"Could not save style presets: {e}")