"""Parse AI Suite responses into actionable change dictionaries.

This module converts large-language-model responses into a list of change
instructions that the AI Suite plugin can execute. It intentionally favours
robustness over strict formatting so that a variety of fenced code block
notations can be interpreted consistently.
"""

from __future__ import annotations

import json
import os
import re
from typing import Dict, Iterable, List, Optional, Tuple

from utils.helpers import apply_patch
from utils.logger import log

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

_CODE_BLOCK_RE = re.compile(r"```(?P<label>[^\n]*)\n(?P<body>.*?)```", re.DOTALL)


ChangeDict = Dict[str, object]


def parse_llm_response(response_text: str, project_root: str) -> List[ChangeDict]:
    """Return structured change dictionaries parsed from *response_text*.

    The parser looks for fenced code blocks and interprets their language label
    as the operation to perform (for example ``patch``, ``create`` or
    ``delete``). Each recognised block contributes a change dictionary that is
    later consumed by :func:`apply_changes_to_project`.
    """

    if not response_text or not response_text.strip():
        return []

    changes: List[ChangeDict] = []
    for match in _CODE_BLOCK_RE.finditer(response_text):
        label = match.group("label").strip()
        body = match.group("body")
        try:
            block_changes = list(_parse_block(label, body, project_root))
        except Exception as exc:  # pragma: no cover - defensive logging
            log.warning("AI Patcher: Failed to parse block '%s': %s", label or "<empty>", exc)
            continue
        changes.extend(block_changes)

    return changes


def _parse_block(label: str, body: str, project_root: str) -> Iterable[ChangeDict]:
    """Yield change dictionaries parsed from a single fenced code block."""

    op, meta = _normalise_label(label)
    op = op or ""

    if op in {"patch", "diff", "apply_patch"}:
        header_path = meta.get("path")
        if header_path:
            try:
                rel_path = _normalise_project_path(project_root, header_path)
            except ValueError as exc:
                raise ValueError(f"Invalid patch path '{header_path}': {exc}") from exc
        else:
            src, dst = _parse_paths_from_patch(body)
            header_path = dst or src
            if not header_path:
                raise ValueError("PATCH block missing filepath")
            rel_path = _normalise_project_path(project_root, header_path)

        yield {
            "type": "APPLY_PATCH",
            "file_path": rel_path,
            "content": body.strip()
        }
        return

    if op in {"create", "write", "file", "replace", "update"}:
        header_path = meta.get("path")
        if not header_path:
            raise ValueError("CREATE block missing filepath")
        rel_path = _normalise_project_path(project_root, header_path)
        yield {
            "type": "CREATE_OR_REPLACE",
            "file_path": rel_path,
            "content": body
        }
        return

    if op in {"delete", "remove", "rm"}:
        header_path = meta.get("path")
        if not header_path:
            raise ValueError("DELETE block missing filepath")
        rel_path = _normalise_project_path(project_root, header_path)
        yield {
            "type": "DELETE",
            "file_path": rel_path
        }
        return

    if op in {"move", "rename"}:
        src = meta.get("src")
        dst = meta.get("dst")
        if not (src and dst):
            # Allow JSON encoded body when the label could not provide paths.
            src, dst = _parse_move_from_body(body)
        if not (src and dst):
            raise ValueError("MOVE block missing source or destination path")
        src_rel = _normalise_project_path(project_root, src)
        dst_rel = _normalise_project_path(project_root, dst)
        yield {
            "type": "MOVE",
            "src_path": src_rel,
            "dst_path": dst_rel
        }
        return

    if op == "json":
        payload = json.loads(body)
        if isinstance(payload, dict):
            payload = [payload]
        if not isinstance(payload, list):
            raise ValueError("JSON block must decode to a change or list of changes")
        for change in payload:
            if not isinstance(change, dict):
                continue
            change = dict(change)
            if "file_path" in change:
                change["file_path"] = _normalise_project_path(project_root, str(change["file_path"]))
            if "src_path" in change:
                change["src_path"] = _normalise_project_path(project_root, str(change["src_path"]))
            if "dst_path" in change:
                change["dst_path"] = _normalise_project_path(project_root, str(change["dst_path"]))
            yield change
        return

    log.warning("AI Patcher: Unknown block type '%s'. Skipping.", label)


def _normalise_label(label: str) -> Tuple[str, Dict[str, str]]:
    """Return (operation, metadata) extracted from a fence label."""

    meta: Dict[str, str] = {}
    if not label:
        return "", meta

    cleaned = label.replace(":", " ").replace("->", " ")
    tokens = [token for token in re.split(r"\s+", cleaned.strip()) if token]
    if not tokens:
        return "", meta

    op = tokens[0].lower()

    if op in {"patch", "diff", "apply_patch"} and len(tokens) > 1:
        meta["path"] = " ".join(tokens[1:])
    elif op in {"create", "write", "file", "replace", "update", "delete", "remove", "rm"} and len(tokens) > 1:
        meta["path"] = " ".join(tokens[1:])
    elif op in {"move", "rename"}:
        remaining = tokens[1:]
        if "to" in remaining:
            idx = remaining.index("to")
            src_tokens = remaining[:idx]
            dst_tokens = remaining[idx + 1:]
        elif "=>" in remaining:
            idx = remaining.index("=>")
            src_tokens = remaining[:idx]
            dst_tokens = remaining[idx + 1:]
        else:
            # Default split in half
            src_tokens = remaining[:1]
            dst_tokens = remaining[1:]
        if src_tokens:
            meta["src"] = " ".join(src_tokens)
        if dst_tokens:
            meta["dst"] = " ".join(dst_tokens)
    elif op == "json" and len(tokens) > 1:
        meta["path"] = " ".join(tokens[1:])

    return op, meta


def _parse_move_from_body(body: str) -> Tuple[Optional[str], Optional[str]]:
    """Try to extract a MOVE change from JSON or simple text body."""

    stripped = body.strip()
    if not stripped:
        return None, None

    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError:
        # Try to read ``src -> dst`` textual notation.
        parts = [part.strip() for part in re.split(r"->|=>", stripped) if part.strip()]
        if len(parts) == 2:
            return parts[0], parts[1]
        return None, None

    if isinstance(payload, dict):
        src = payload.get("src_path") or payload.get("from")
        dst = payload.get("dst_path") or payload.get("to")
        return src, dst
    if isinstance(payload, list) and payload:
        first = payload[0]
        if isinstance(first, dict):
            src = first.get("src_path") or first.get("from")
            dst = first.get("dst_path") or first.get("to")
            return src, dst
    return None, None


def _parse_paths_from_patch(body: str) -> Tuple[Optional[str], Optional[str]]:
    """Return (src, dst) paths derived from patch headers."""

    src: Optional[str] = None
    dst: Optional[str] = None
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("diff --git"):
            parts = stripped.split()
            if len(parts) >= 4:
                src = _strip_patch_prefix(parts[2])
                dst = _strip_patch_prefix(parts[3])
        elif stripped.startswith("rename from "):
            src = _strip_patch_prefix(stripped[len("rename from ") :])
        elif stripped.startswith("rename to "):
            dst = _strip_patch_prefix(stripped[len("rename to ") :])
        elif stripped.startswith("--- "):
            src = _strip_patch_prefix(stripped[4:])
        elif stripped.startswith("+++ "):
            dst = _strip_patch_prefix(stripped[4:])
        if src and dst:
            break
    return src, dst


def _strip_patch_prefix(path: str) -> str:
    path = path.strip().strip('"')
    if path.startswith("a/") or path.startswith("b/"):
        path = path[2:]
    return path


def _normalise_project_path(project_root: str, candidate: str) -> str:
    """Validate *candidate* and return a safe relative path."""

    if not candidate:
        raise ValueError("Empty path")

    candidate = candidate.strip().strip('"')
    if candidate.startswith("a/") or candidate.startswith("b/"):
        candidate = candidate[2:]

    abs_root = os.path.abspath(project_root)
    abs_candidate = os.path.abspath(os.path.join(abs_root, candidate))
    if os.path.commonpath([abs_root, abs_candidate]) != abs_root:
        raise ValueError("Path escapes project root")
    rel_path = os.path.relpath(abs_candidate, abs_root)
    return rel_path.replace("\\", "/")


def apply_changes_to_project(project_root: str, changes: List[ChangeDict]) -> Tuple[bool, str]:
    """Apply parsed *changes* to *project_root* atomically."""

    log.info("AI Patcher: Stage 1/2 - Preparing snapshot of all file changes...")
    snapshot: Dict[str, Optional[str]] = {}

    def _read_current(path: str) -> str:
        if path in snapshot:
            staged = snapshot[path]
            return "" if staged is None else staged
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as handle:
                return handle.read()
        except FileNotFoundError:
            return ""

    abs_root = os.path.normpath(os.path.abspath(project_root))

    try:
        for change in changes:
            ctype = change.get("type")
            if ctype in {"APPLY_PATCH", "CREATE_OR_REPLACE", "DELETE"}:
                rel = str(change.get("file_path", ""))
                if not rel:
                    raise ValueError("Missing file_path")
                path = _safe_join(abs_root, rel)
            elif ctype == "MOVE":
                src_rel = str(change.get("src_path", ""))
                dst_rel = str(change.get("dst_path", ""))
                if not (src_rel and dst_rel):
                    raise ValueError("MOVE requires src_path and dst_path")
                src_path = _safe_join(abs_root, src_rel)
                dst_path = _safe_join(abs_root, dst_rel)
            else:
                log.warning("AI Patcher: Unknown change type %s; skipping.", ctype)
                continue

            if ctype == "APPLY_PATCH":
                current = _read_current(path)
                try:
                    new_text = apply_patch(current, str(change.get("content", "")))
                except Exception as exc:
                    return False, f"Patch failed for {path}: {exc}"
                snapshot[path] = new_text
            elif ctype == "CREATE_OR_REPLACE":
                snapshot[path] = str(change.get("content", ""))
            elif ctype == "DELETE":
                snapshot[path] = None
            elif ctype == "MOVE":
                current = _read_current(src_path)
                if current == "" and not os.path.exists(src_path) and src_path not in snapshot:
                    log.warning("AI Patcher: MOVE source does not exist: %s", src_path)
                snapshot[dst_path] = current
                snapshot[src_path] = None

        log.info("AI Patcher: Stage 2/2 - Writing files atomically...")
        for path, new_content in snapshot.items():
            safe_path = _safe_join(abs_root, os.path.relpath(path, abs_root))
            if new_content is None:
                if os.path.exists(safe_path):
                    os.remove(safe_path)
                    log.info("Deleted file: %s", safe_path)
                continue

            os.makedirs(os.path.dirname(safe_path), exist_ok=True)
            tmp_path = f"{safe_path}.tmp.{os.getpid()}"
            with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(new_content)
            os.replace(tmp_path, safe_path)
            log.info("Wrote changes to: %s", safe_path)
    except Exception as exc:
        return False, f"A critical error occurred during file writing: {exc}"

    return True, f"Successfully applied {len(snapshot)} change(s)."


def _safe_join(root: str, rel_path: str) -> str:
    """Join *root* with *rel_path* while preventing directory traversal."""

    root = os.path.abspath(root)
    joined = os.path.normpath(os.path.join(root, rel_path))
    if os.path.commonpath([root, joined]) != root:
        raise ValueError("Path escapes project root")
    return joined
