"""Unit tests for AI Suite response parsing and pure-Python patch apply."""

from __future__ import annotations

import os
import textwrap

import pytest

from plugins.ai_suite.response_parser import (
    apply_changes_to_project,
    parse_llm_response,
)
from utils.helpers import apply_patch


def test_apply_patch_basic_replacement():
    original = "line1\nline2\nline3\n"
    patch = textwrap.dedent(
        """\
        --- a/f.py
        +++ b/f.py
        @@ -1,3 +1,3 @@
         line1
        -line2
        +LINE2
         line3
        """
    )
    result = apply_patch(original, patch)
    assert result == "line1\nLINE2\nline3\n"


def test_apply_patch_tolerates_trailing_whitespace_mismatch():
    original = "alpha\nbeta  \ngamma\n"
    patch = textwrap.dedent(
        """\
        --- a/f.py
        +++ b/f.py
        @@ -1,3 +1,3 @@
         alpha
        -beta
        +BETA
         gamma
        """
    )
    result = apply_patch(original, patch)
    assert "BETA" in result
    assert "alpha" in result


def test_parse_golden_rules_full_file(tmp_path):
    response = textwrap.dedent(
        """\
        ### File: `/hello.py`
        ```python
        print("hi")
        ```
        """
    )
    changes = parse_llm_response(response, str(tmp_path))
    assert len(changes) == 1
    assert changes[0]["type"] == "CREATE_OR_REPLACE"
    assert changes[0]["file_path"] == "hello.py"
    assert "print(\"hi\")" in str(changes[0]["content"])


def test_parse_golden_rules_delete_and_move(tmp_path):
    response = textwrap.dedent(
        """\
        ### File: `/old.py`
        ---DELETED---

        ### File: `/a.py`
        ---MOVED-TO: /b/a.py---
        """
    )
    changes = parse_llm_response(response, str(tmp_path))
    types = {c["type"] for c in changes}
    assert types == {"DELETE", "MOVE"}
    delete = next(c for c in changes if c["type"] == "DELETE")
    move = next(c for c in changes if c["type"] == "MOVE")
    assert delete["file_path"] == "old.py"
    assert move["src_path"] == "a.py"
    assert move["dst_path"] == "b/a.py"


def test_parse_labelled_patch_fence(tmp_path):
    response = textwrap.dedent(
        """\
        ```patch
        --- a/src/app.py
        +++ b/src/app.py
        @@ -1,2 +1,2 @@
         x = 1
        -y = 2
        +y = 3
        ```
        """
    )
    changes = parse_llm_response(response, str(tmp_path))
    assert len(changes) == 1
    assert changes[0]["type"] == "APPLY_PATCH"
    assert changes[0]["file_path"] == "src/app.py"


def test_path_traversal_rejected(tmp_path):
    response = textwrap.dedent(
        """\
        ### File: `/../../evil.py`
        ```python
        bad
        ```
        """
    )
    changes = parse_llm_response(response, str(tmp_path))
    assert changes == []


def test_apply_changes_write_delete_move(tmp_path):
    project = tmp_path / "proj"
    project.mkdir()
    (project / "keep.py").write_text("keep\n", encoding="utf-8")
    (project / "gone.py").write_text("gone\n", encoding="utf-8")
    (project / "src").mkdir()
    (project / "src" / "old.py").write_text("moved\n", encoding="utf-8")

    response = textwrap.dedent(
        """\
        ### File: `/new.py`
        ```python
        print("new")
        ```

        ### File: `/gone.py`
        ---DELETED---

        ### File: `/src/old.py`
        ---MOVED-TO: /src/new_name.py---
        """
    )
    changes = parse_llm_response(response, str(project))
    ok, msg = apply_changes_to_project(str(project), changes)
    assert ok, msg
    assert (project / "new.py").read_text(encoding="utf-8").startswith("print")
    assert not (project / "gone.py").exists()
    assert not (project / "src" / "old.py").exists()
    assert (project / "src" / "new_name.py").read_text(encoding="utf-8") == "moved\n"
    assert (project / "keep.py").read_text(encoding="utf-8") == "keep\n"


def test_apply_changes_patch(tmp_path):
    project = tmp_path / "proj"
    project.mkdir()
    target = project / "f.py"
    target.write_text("a\nb\nc\n", encoding="utf-8")

    response = textwrap.dedent(
        """\
        ```patch
        --- a/f.py
        +++ b/f.py
        @@ -1,3 +1,3 @@
         a
        -b
        +B
         c
        ```
        """
    )
    changes = parse_llm_response(response, str(project))
    ok, msg = apply_changes_to_project(str(project), changes)
    assert ok, msg
    assert target.read_text(encoding="utf-8") == "a\nB\nc\n"


def test_get_rules_markdown_exists():
    from app_core.golden_rules import get_rules_markdown

    text = get_rules_markdown()
    assert "Golden Rules" in text
    assert "### File:" in text
    assert "---DELETED---" in text
