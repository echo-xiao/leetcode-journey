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

import json
import re
from pathlib import Path

from .problem_source import PROBLEMS, REPO, elements_of, meta_of, statement_of, title_of

SCHEMA_VERSION = 1
OUT_PATH = REPO / "app" / "content.json"

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
    """The whole file. Numeric order is both readable and deterministic, and
    determinism is what keeps the diffs small."""

    def _sort_key(folder: Path) -> tuple[int, str]:
        match = _NUMBER_RE.match(folder.name)
        return (int(match.group(1)) if match else 0, folder.name)

    folders = sorted((d for d in problems_dir.iterdir() if d.is_dir()), key=_sort_key)
    return {
        "version": SCHEMA_VERSION,
        "problems": [problem_entry(folder, techniques) for folder in folders],
    }


def _serialise(payload: dict) -> str:
    # ensure_ascii=False keeps the Chinese readable and roughly halves the size
    # of a file the app downloads on every cold launch.
    return json.dumps(payload, ensure_ascii=False, indent=1, sort_keys=True) + "\n"


def write_if_changed(path: Path, payload: dict) -> bool:
    """Write the payload only when it differs. Returns whether it wrote.

    Rewriting an identical two-megabyte file on every sync-all would grow the
    git history for nothing, so an unchanged library must leave the file — and
    its mtime — alone.
    """
    text = _serialise(payload)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def run() -> None:
    from .problem_source import technique_map

    payload = build_payload(PROBLEMS, technique_map())
    count = len(payload["problems"])
    if write_if_changed(OUT_PATH, payload):
        size = OUT_PATH.stat().st_size / 1024 / 1024
        print(f"内容 {count} 道题 -> {OUT_PATH}（{size:.1f} MB）")
        print("记得 git add app/content.json 并 push，否则手机上拿到的还是旧的。")
    else:
        print(f"内容 {count} 道题，与磁盘上一致，未改动 {OUT_PATH}")
