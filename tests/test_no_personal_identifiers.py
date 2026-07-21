"""Regression checks for accidental personal account references."""

from __future__ import annotations

from pathlib import Path


TEXT_EXTENSIONS = {
    ".cfg",
    ".conf",
    ".css",
    ".csv",
    ".desktop",
    ".html",
    ".ini",
    ".json",
    ".js",
    ".lock",
    ".md",
    ".patch",
    ".py",
    ".rst",
    ".sh",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    "ai_exports",
    "node_modules",
    "venv",
    ".grok",
    ".koromali",
    "logs",
    "session_data",
}

# Local-only / gitignored machine state that may contain absolute user paths.
SKIP_FILES = {
    "Koromali_editor_settings.json",
    "credentials.json",
}

BANNED_IDENTIFIERS = {
    "".join(("stell", "iro")),
    "".join(("gik", "e5")),
}


def _tracked_files(repo_root: Path) -> set[Path]:
    """Return paths tracked by git when available; empty set on failure."""
    import subprocess

    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "ls-files", "-z"],
            capture_output=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return set()
    tracked: set[Path] = set()
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        tracked.add((repo_root / raw.decode("utf-8", errors="ignore")).resolve())
    return tracked


def should_scan(path: Path, tracked: set[Path] | None = None) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return False
    if path.name in SKIP_FILES:
        return False
    if not path.is_file():
        return False
    if tracked is not None and tracked and path.resolve() not in tracked:
        # Prefer scanning only version-controlled files when git is available.
        return False
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    return path.suffix == ""


def test_repository_does_not_contain_personal_github_identifiers() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    tracked = _tracked_files(repo_root)

    offending_files: list[str] = []

    for file_path in repo_root.rglob("*"):
        if not should_scan(file_path, tracked):
            continue

        try:
            contents = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        lower_contents = contents.lower()
        if any(identifier in lower_contents for identifier in BANNED_IDENTIFIERS):
            offending_files.append(str(file_path.relative_to(repo_root)))

    assert not offending_files, (
        "Found banned personal GitHub identifiers in files: "
        + ", ".join(sorted(offending_files))
    )
