# /plugins/ai_suite/persona_manager.py
import os
import importlib.util
from typing import List, Dict, Any

try:
    from utils.logger import log
except Exception:  # pragma: no cover
    class _L:
        def info(self, *a, **k): print("[INFO]", *a)
        def warning(self, *a, **k): print("[WARN]", *a)
        def error(self, *a, **k): print("[ERROR]", *a)
    log = _L()

try:
    from utils.helpers import get_base_path
except Exception:  # pragma: no cover
    def get_base_path() -> str:
        # A simple fallback for when running outside the main app
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


class PersonaManager:
    """Discovers and loads AI personas from the assets directory."""
    def __init__(self):
        self.personas_dir = os.path.join(get_base_path(), "assets", "ai_personas")
        self.personas: List[Dict[str, Any]] = self._load_personas()

    def _load_personas(self) -> List[Dict[str, Any]]:
        """Scans the personas directory and loads valid persona modules."""
        loaded_personas = []
        if not os.path.isdir(self.personas_dir):
            log.warning(f"Personas directory not found: {self.personas_dir}")
            return []

        for filename in os.listdir(self.personas_dir):
            if not filename.endswith(".py") or filename.startswith("__"):
                continue
            
            file_path = os.path.join(self.personas_dir, filename)
            module_name = f"assets.ai_personas.{os.path.splitext(filename)[0]}"
            
            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    if hasattr(module, "get_persona_info") and callable(module.get_persona_info):
                        persona_info = module.get_persona_info()
                        
                        # Be more lenient: require id and name, but use defaults for others.
                        if "id" in persona_info and "name" in persona_info:
                            persona_info.setdefault("expertise", "N/A")
                            persona_info.setdefault("system_prompt", "You are a helpful assistant.")
                            loaded_personas.append(persona_info)
                        else:
                            log.warning(f"Persona file '{filename}' is missing required 'id' or 'name' keys.")
                    else:
                        log.warning(f"Persona file '{filename}' does not have a get_persona_info() function.")
            except Exception as e:
                log.error(f"Failed to load persona from '{filename}': {e}", exc_info=True)

        loaded_personas.sort(key=lambda p: p.get("name", ""))
        return loaded_personas

    def get_personas(self) -> List[Dict[str, Any]]:
        """Returns the list of loaded personas."""
        return self.personas

    def get_persona_by_id(self, persona_id: str) -> Dict[str, Any] | None:
        """Finds a persona by its ID."""
        for persona in self.personas:
            if persona.get("id") == persona_id:
                return persona
        return None