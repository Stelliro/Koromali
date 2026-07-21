"""Project specific Python site customisations."""
from __future__ import annotations

import sys
import warnings

try:
    from utils.qt_compat import ensure_qt_binding
except Exception as exc:  # pragma: no cover - extremely early import errors
    warnings.warn(f"Koromali: failed to import Qt compatibility helpers: {exc}")
else:
    try:
        ensure_qt_binding()
    except Exception as exc:  # pragma: no cover - binding missing at runtime
        warnings.warn(
            "Koromali: No supported Qt binding is available. "
            "Install PyQt6 or PySide6 to run the desktop client.",
            RuntimeWarning,
        )
        if "pytest" not in sys.modules:
            warnings.warn(str(exc))
