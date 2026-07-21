"""Parse AI Suite responses into actionable change dictionaries.

This module converts large-language-model responses into a list of change
instructions that the AI Suite plugin can execute. It intentionally favours
robustness over strict formatting so that a variety of fenced code block
notations can be interpreted consistently.

Supported formats:
  * Golden Rules sections: ``### File: `/path` `` followed by a full-file fence,
    ``---DELETED---``, or ``---MOVED-TO: /new/path---``
  * Operation-labelled fences: `` ```patch ``, `` ```create path ``, `` ```delete path ``, etc.
  * Unified diffs whose paths are inferred from ``---`` / ``+++`` headers
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

# Accept ``` or ~~~ fences (golden rules allow either).
_CODE_BLOCK_RE = re.compile(
    r"(?P<fence>```|~~~)(?P<label>[^\n]*)\n(?P<body>.*?)(?P=fence)",
    re.DOTALL,
)

_FILE_HEADER_RE = re.compile(
    r"^###\s*File:\s*`?(?P<path>/?[^`\n]+?)`?\s*$",
    re.MULTILINE | re.IGNORECASE,
)

_DELETED_RE = re.compile(r"^\s*---DELETED---\s*$", re.MULTILINE)
_MOVED_RE = re.compile(
    r"^\s*---MOVED-TO:\s*`?(?P<path>/?[^`\n-]+?)`?\s*---\s*$",
    re.MULTILINE | re.IGNORECASE,
)

ChangeDict = Dict[str, object]


def parse_llm_response(response_text: str, project_root: str) -> List[ChangeDict]:
    """Return structured change dictionaries parsed from *response_text*.

    Recognises both the Golden Rules ``### File:`` layout (what browser-LLM
    exports ask for) and operation-labelled fences (``patch``, ``create``, …).
    """

    if not response_text or not response_text.strip():
        return []

    # Normalise exotic fence openers some models emit.
    text = response_text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("````", "```")

    changes: List[ChangeDict] = []
    changes.extend(_parse_golden_rule_sections(text, project_root))
    changes.extend(_parse_labelled_fences(text, project_root))

    # Stable de-dupe: later identical (type, path) wins so labelled ops can
    # refine a prior full-file write when both appear.
    deduped: Dict[Tuple[str, str], ChangeDict] = {}
    ordered: List[ChangeDict] = []
    for change in changes:
        key = _change_key(change)
        if key in deduped:
            # Replace in place to keep first-seen position.
            idx = ordered.index(deduped[key])
            ordered[idx] = change
            deduped[key] = change
        else:
            deduped[key] = change
            ordered.append(change)

    return ordered


def _change_key(change: ChangeDict) -> Tuple[str, str]:
    ctype = str(change.get("type", ""))
    if ctype == "MOVE":
        return ctype, f"{change.get('src_path')}=>{change.get('dst_path')}"
    return ctype, str(change.get("file_path", ""))


def _parse_golden_rule_sections(text: str, project_root: str) -> List[ChangeDict]:
    """Parse ``### File:`` sections from the Golden Rules format."""

    headers = list(_FILE_HEADER_RE.finditer(text))
    if not headers:
        return []

    changes: List[ChangeDict] = []
    for i, match in enumerate(headers):
        raw_path = match.group("path").strip()
        start = match.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[start:end].strip()

        try:
            rel_path = _normalise_project_path(project_root, raw_path)
        except ValueError as exc:
            log.warning("AI Patcher: Skipping ### File section with bad path '%s': %s", raw_path, exc)
            continue

        if _DELETED_RE.search(body):
            changes.append({"type": "DELETE", "file_path": rel_path})
            continue

        moved = _MOVED_RE.search(body)
        if moved:
            try:
                dst = _normalise_project_path(project_root, moved.group("path").strip())
            except ValueError as exc:
                log.warning("AI Patcher: Skipping MOVE with bad destination: %s", exc)
                continue
            changes.append({
                "type": "MOVE",
                "src_path": rel_path,
                "dst_path": dst,
            })
            continue

        fence = _CODE_BLOCK_RE.search(body)
        if not fence:
            # Body might be a bare unified diff without fences.
            if _looks_like_unified_diff(body):
                changes.append({
                    "type": "APPLY_PATCH",
                    "file_path": rel_path,
                    "content": body.strip(),
                })
            else:
                log.warning(
                    "AI Patcher: ### File section for '%s' has no code block; skipping.",
                    rel_path,
                )
            continue

        content = fence.group("body")
        # Preserve intentional trailing newline for full-file writes.
        if content.endswith("\n"):
            file_body = content
        else:
            file_body = content

        if _looks_like_unified_diff(file_body):
            changes.append({
                "type": "APPLY_PATCH",
                "file_path": rel_path,
                "content": file_body.strip(),
            })
        else:
            changes.append({
                "type": "CREATE_OR_REPLACE",
                "file_path": rel_path,
                "content": file_body if file_body.endswith("\n") or not file_body else file_body + "\n",
            })

    return changes


def _parse_labelled_fences(text: str, project_root: str) -> List[ChangeDict]:
    """Parse operation-labelled fences (patch/create/delete/move/json)."""

    changes: List[ChangeDict] = []
    for match in _CODE_BLOCK_RE.finditer(text):
        label = match.group("label").strip()
        body = match.group("body")
        op, _meta = _normalise_label(label)
        # Skip language-only fences (```python); those belong to ### File: sections.
        if not op or op not in {
            "patch", "diff", "apply_patch",
            "create", "write", "file", "replace", "update",
            "delete", "remove", "rm",
            "move", "rename",
            "json",
        }:
            # Bare unified-diff fence with empty/lang label still useful.
            if _looks_like_unified_diff(body):
                try:
                    src, dst = _parse_paths_from_patch(body)
                    header_path = dst or src
                    if not header_path:
                        continue
                    rel_path = _normalise_project_path(project_root, header_path)
                    changes.append({
                        "type": "APPLY_PATCH",
                        "file_path": rel_path,
                        "content": body.strip(),
                    })
                except Exception as exc:
                    log.warning("AI Patcher: Failed to parse bare diff block: %s", exc)
            continue

        try:
            block_changes = list(_parse_block(label, body, project_root))
        except Exception as exc:  # pragma: no cover - defensive logging
            log.warning("AI Patcher: Failed to parse block '%s': %s", label or "<empty>", exc)
            continue
        changes.extend(block_changes)

    return changes


def _looks_like_unified_diff(body: str) -> bool:
    """Heuristic: true when *body* appears to be a unified / git diff."""

    if not body or not body.strip():
        return False
    lines = body.lstrip().splitlines()
    if not lines:
        return False
    head = lines[0].lstrip()
    if head.startswith("diff --git") or head.startswith("--- ") or head.startswith("+++ "):
        return True
    # Hunk marker somewhere near the top is also a strong signal.
    for line in lines[:20]:
        if line.startswith("@@ "):
            return True
    return False


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
            "content": body.strip(),
        }
        return

    if op in {"create", "write", "file", "replace", "update"}:
        header_path = meta.get("path")
        if not header_path:
            raise ValueError("CREATE block missing filepath")
        rel_path = _normalise_project_path(project_root, header_path)
        content = body
        if content and not content.endswith("\n"):
            content = content + "\n"
        yield {
            "type": "CREATE_OR_REPLACE",
            "file_path": rel_path,
            "content": content,
        }
        return

    if op in {"delete", "remove", "rm"}:
        header_path = meta.get("path")
        if not header_path:
            raise ValueError("DELETE block missing filepath")
        rel_path = _normalise_project_path(project_root, header_path)
        yield {
            "type": "DELETE",
            "file_path": rel_path,
        }
        return

    if op in {"move", "rename"}:
        src = meta.get("src")
        dst = meta.get("dst")
        if not (src and dst):
            src, dst = _parse_move_from_body(body)
        if not (src and dst):
            raise ValueError("MOVE block missing source or destination path")
        src_rel = _normalise_project_path(project_root, src)
        dst_rel = _normalise_project_path(project_root, dst)
        yield {
            "type": "MOVE",
            "src_path": src_rel,
            "dst_path": dst_rel,
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
            src = _strip_patch_prefix(stripped[len("rename from "):])
        elif stripped.startswith("rename to "):
            dst = _strip_patch_prefix(stripped[len("rename to "):])
        elif stripped.startswith("--- "):
            src = _strip_patch_prefix(stripped[4:])
        elif stripped.startswith("+++ "):
            dst = _strip_patch_prefix(stripped[4:])
        if src and dst:
            break
    return src, dst


def _strip_patch_prefix(path: str) -> str:
    path = path.strip().strip('"')
    # Drop optional tab-separated timestamps from `diff -u` output.
    if "\t" in path:
        path = path.split("\t", 1)[0]
    if path.startswith("a/") or path.startswith("b/"):
        path = path[2:]
    # /dev/null means create/delete; keep empty-ish so caller can pick the other side.
    if path in {"/dev/null", "dev/null"}:
        return ""
    return path.lstrip("/")


def _paths_share_root(root: str, candidate: str) -> bool:
    """Return True when *candidate* is inside *root* (Windows-safe)."""

    root = os.path.normcase(os.path.abspath(root))
    candidate = os.path.normcase(os.path.abspath(candidate))
    try:
        common = os.path.normcase(os.path.commonpath([root, candidate]))
    except ValueError:
        return False
    return common == root


def _normalise_project_path(project_root: str, candidate: str) -> str:
    """Validate *candidate* and return a safe relative path."""

    if not candidate:
        raise ValueError("Empty path")

    candidate = candidate.strip().strip('`"')
    if candidate.startswith("a/") or candidate.startswith("b/"):
        candidate = candidate[2:]
    candidate = candidate.lstrip("/")

    abs_root = os.path.abspath(project_root)
    abs_candidate = os.path.abspath(os.path.join(abs_root, candidate))
    if not _paths_share_root(abs_root, abs_candidate):
        raise ValueError("Path escapes project root")
    rel_path = os.path.relpath(abs_candidate, abs_root)
    return rel_path.replace("\\", "/")


def apply_changes_to_project(project_root: str, changes: List[ChangeDict]) -> Tuple[bool, str]:
    """Apply parsed *changes* to *project_root* atomically (temp file + replace)."""

    if not project_root or not os.path.isdir(project_root):
        return False, "Invalid project root."
    if not changes:
        return True, "No changes to apply."

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

            parent = os.path.dirname(safe_path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            tmp_path = f"{safe_path}.tmp.{os.getpid()}"
            try:
                with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(new_content)
                os.replace(tmp_path, safe_path)
            except Exception:
                if os.path.exists(tmp_path):
                    try:
                        os.remove(tmp_path)
                    except OSError:
                        pass
                raise
            log.info("Wrote changes to: %s", safe_path)
    except Exception as exc:
        return False, f"A critical error occurred during file writing: {exc}"

    return True, f"Successfully applied {len(snapshot)} change(s)."


def _safe_join(root: str, rel_path: str) -> str:
    """Join *root* with *rel_path* while preventing directory traversal."""

    root = os.path.abspath(root)
    joined = os.path.normpath(os.path.join(root, rel_path))
    if not _paths_share_root(root, joined):
        raise ValueError("Path escapes project root")
    return joined
