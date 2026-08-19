"""Build the JSON payload the iOS app downloads.

The app fetches this file from GitHub Raw at launch, so it has to be committed
even though it is generated — Raw only serves what is in the repository. That
is a deliberate exception to the convention that generated artefacts (anki/)
stay out of git.

There is no timestamp in the payload on purpose. A field that changes daily
would rewrite the file on every sync and bloat the history for nothing;
freshness is the ETag's job, not the file's.
"""

from __future__ import annotations

import re
from pathlib import Path

from .problem_source import elements_of, meta_of, statement_of, title_of

SCHEMA_VERSION = 1

# "1005_univalued-binary-tree" -> 1005. Folder names always start with the id.
_NUMBER_RE = re.compile(r"^(\d+)_")
# "solution_10.py" must sort after "solution_2.py", which string order gets wrong.
_SOLUTION_RE = re.compile(r"^solution_(\d+)\.py$")


def _body_after_heading(path: Path) -> str:
    """A markdown file without its "# 15. 三数之和 · 复盘" title line.

    The app draws its own headings, and the file's own title is redundant on a
    card that already shows the problem name at the top.
    """
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip()


def _solutions(folder: Path) -> list[dict]:
    found = []
    for path in folder.iterdir():
        match = _SOLUTION_RE.match(path.name)
        if match:
            found.append((int(match.group(1)), path))
    return [
        {"name": path.name, "code": path.read_text(encoding="utf-8")}
        for _, path in sorted(found)
    ]


def problem_entry(folder: Path, techniques: dict[str, str]) -> dict:
    """One problem, with every layer of the chain the app reveals."""
    difficulty, technique = meta_of(folder, techniques)
    number_match = _NUMBER_RE.match(folder.name)
    return {
        "id": folder.name,
        "number": int(number_match.group(1)) if number_match else 0,
        "title": title_of(folder),
        "difficulty": difficulty,
        "technique": technique,
        # None, not 500: the app scrolls, and capping would cut the worked
        # examples off 130 of the 402 problems.
        "statement": statement_of(folder, limit=None),
        "elements": elements_of(folder),
        "pseudocode": _body_after_heading(folder / "pseudocode.md"),
        # Empty for the 66 problems with no review.md. The ==marked== spans are
        # passed through untouched; the app renders them as highlights, and they
        # are the part of a retrospective worth seeing.
        "retrospective": _body_after_heading(folder / "review.md"),
        "solutions": _solutions(folder),
    }


def build_payload(problems_dir: Path, techniques: dict[str, str]) -> dict:
    """The whole file. Problems are sorted by folder name so diffs stay small."""
    folders = sorted(d for d in problems_dir.iterdir() if d.is_dir())
    return {
        "version": SCHEMA_VERSION,
        "problems": [problem_entry(folder, techniques) for folder in folders],
    }
