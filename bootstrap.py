"""Bootstrapper that prepares Koromali before launching the main entry point."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

from utils.qt_compat import ensure_qt_binding


def main() -> None:
    """Ensure a Qt binding is available, then execute ``main.py``."""
    ensure_qt_binding()

    script_path = Path(__file__).with_name("main.py").resolve()
    # Mimic ``python main.py`` so downstream argument parsing behaves the same.
    sys.argv = [str(script_path), *sys.argv[1:]]
    runpy.run_path(str(script_path), run_name="__main__")

if __name__ == "__main__":
    main()
