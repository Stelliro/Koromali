"""Tests for project launch-script resolution in Script Runner."""

from __future__ import annotations

import os
from types import SimpleNamespace

from plugins.script_runner.plugin_main import LAUNCH_SCRIPTS_SETTING, ScriptRunnerPlugin


class _FakeSettings:
    def __init__(self, data=None):
        self.data = dict(data or {})

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value, *_args, **_kwargs):
        self.data[key] = value


class _FakeProject:
    def __init__(self, path):
        self.path = path

    def get_active_project_path(self):
        return self.path


def _bind_helpers(tmp_path, settings_data=None):
    """Attach ScriptRunnerPlugin helpers onto a plain object for unit testing."""
    settings = _FakeSettings(settings_data)
    project = _FakeProject(str(tmp_path))
    managers = {"settings": settings, "project": project}
    host = SimpleNamespace(
        api=SimpleNamespace(get_manager=lambda name: managers.get(name))
    )
    # Bind unbound methods from the plugin class.
    host._active_project_root = ScriptRunnerPlugin._active_project_root.__get__(host)
    host._get_launch_script_map = ScriptRunnerPlugin._get_launch_script_map.__get__(host)
    host._set_launch_script = ScriptRunnerPlugin._set_launch_script.__get__(host)
    host._resolve_launch_script_path = ScriptRunnerPlugin._resolve_launch_script_path.__get__(
        host
    )
    return host, settings


def test_set_and_resolve_launch_script(tmp_path):
    script = tmp_path / "app" / "main.py"
    script.parent.mkdir()
    script.write_text("print('hi')\n", encoding="utf-8")

    plugin, settings = _bind_helpers(tmp_path)
    plugin._set_launch_script(str(tmp_path), "app/main.py")

    stored = settings.get(LAUNCH_SCRIPTS_SETTING)
    assert os.path.normpath(str(tmp_path)) in stored
    assert stored[os.path.normpath(str(tmp_path))] == "app/main.py"

    resolved = plugin._resolve_launch_script_path()
    assert resolved is not None
    assert os.path.normpath(resolved) == os.path.normpath(str(script))


def test_resolve_rejects_missing_and_escape(tmp_path):
    plugin, _settings = _bind_helpers(tmp_path)
    plugin._set_launch_script(str(tmp_path), "missing.py")
    assert plugin._resolve_launch_script_path() is None

    plugin._set_launch_script(str(tmp_path), "../outside.py")
    assert plugin._resolve_launch_script_path() is None
