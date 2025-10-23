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
}

BANNED_IDENTIFIERS = {
    "".join(("stell", "iro")),
    "".join(("gik", "e5")),
}


def should_scan(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return False
    if not path.is_file():
        return False
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    # Allow scanning files without an extension if they look like text.
    return path.suffix == ""


def test_repository_does_not_contain_personal_github_identifiers() -> None:
    repo_root = Path(__file__).resolve().parents[1]

    offending_files: list[str] = []

    for file_path in repo_root.rglob("*"):
        if not should_scan(file_path):
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
