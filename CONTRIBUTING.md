# Contributing to Koromali

Thanks for helping improve Koromali.

## Ground rules

- Keep changes focused and reviewable.
- Match existing code style in the area you touch.
- Do not commit secrets, settings, `venv/`, logs, or `ai_exports/`.
- Commercial use remains restricted under the PolyForm Noncommercial license.

## Setup

```bash
python -m venv venv
# activate venv
pip install -r requirements.txt
export PYTHONPATH=.   # Windows: set PYTHONPATH=.
python main.py
```

## Tests

```bash
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
pytest tests/ -q
```

UI smoke (optional):

```bash
pytest tests/test_ui_smoke.py -v -s
```

## Pull requests

1. Describe **what** changed and **why**.
2. Note how you verified (unit tests, smoke, manual steps).
3. Avoid drive-by refactors unrelated to the fix.
