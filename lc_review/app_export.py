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
import textwrap
from pathlib import Path

from . import ac_times, code_shape
from .problem_source import PROBLEMS, REPO, elements_of, meta_of, statement_of, title_of

SCHEMA_VERSION = 4
OUT_PATH = REPO / "app" / "content.json"

# "1005_univalued-binary-tree" -> 1005. Folder names always start with the id.
_NUMBER_RE = re.compile(r"^(\d+)_")
# "solution_10.py" must sort after "solution_2.py", which string order gets wrong.
_SOLUTION_RE = re.compile(r"^solution_(\d+)\.py$")

# pseudocode.md parsing: turn a hand-written "article" (headings, prose,
# one fenced pseudocode block, a complexity section) into typed blocks the
# app can render with the right typography for each kind. See
# `_pseudocode_blocks` for the block shapes.
_HEADING_RE = re.compile(r"^(#{2,})\s*(.*)$")
_TITLE_RE = re.compile(r"^#\s+.*$")
_FENCE_RE = re.compile(r"^\s*```")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_LATEX_RE = re.compile(r"\$([^$]+)\$")
_BULLET_RE = re.compile(r"^(\s*)-\s+")


def _clean_text_line(line: str) -> str:
    """Strip markdown emphasis/code/math markers from one prose line.

    Order matters: bullets first (so a bolded bullet like "- **X**" still
    gets its dash swapped before the bold markers are stripped), then bold,
    then inline code, then LaTeX delimiters.
    """
    line = _BULLET_RE.sub(lambda m: m.group(1) + "• ", line)
    line = _BOLD_RE.sub(lambda m: m.group(1), line)
    line = _INLINE_CODE_RE.sub(lambda m: m.group(1), line)
    line = _LATEX_RE.sub(lambda m: m.group(1), line)
    return line


def _pseudocode_blocks(text: str) -> list[dict]:
    """Parse a pseudocode.md body (title line already stripped) into blocks.

    - `##`+ headings become {"kind": "heading"} with the hashes removed.
    - A lone `# ` line is a second copy of the document title some articles
      carry in the body; it repeats the problem name, so it is dropped.
    - Fenced ``` blocks become {"kind": "code"}, dedented but with their
      internal (relative) indentation intact — some articles nest the fence
      inside a bullet, which indents the fence markers but not the meaning
      of the pseudocode's own indentation.
    - Everything else is prose: consecutive non-blank lines join into one
      {"kind": "text"} block, cleaned of markdown markers; a blank line
      starts a new block.
    """
    lines = text.splitlines()
    blocks: list[dict] = []
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            cleaned = "\n".join(paragraph).strip()
            if cleaned:
                blocks.append({"kind": "text", "text": cleaned})
            paragraph.clear()

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        if _FENCE_RE.match(line):
            flush()
            i += 1
            code_lines: list[str] = []
            while i < n and not _FENCE_RE.match(lines[i]):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip the closing fence
            code = textwrap.dedent("\n".join(code_lines)).strip("\n")
            if code:
                blocks.append({"kind": "code", "text": code})
            continue

        heading_match = _HEADING_RE.match(line)
        if heading_match:
            flush()
            _, rest = heading_match.groups()
            blocks.append({"kind": "heading", "text": rest.strip()})
            i += 1
            continue

        if _TITLE_RE.match(line):
            flush()
            i += 1
            continue

        if not line.strip():
            flush()
            i += 1
            continue

        paragraph.append(_clean_text_line(line))
        i += 1

    flush()
    return blocks


def _pseudocode_of(folder: Path) -> list[dict]:
    return _pseudocode_blocks(_body_after_heading(folder / "pseudocode.md"))


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


#: How many solutions a card will show at most.
#:
#: The folder holds every accepted submission, and passing then tweaking and
#: resubmitting inside one session is normal -- one problem here has sixteen,
#: twelve of which survive shape deduplication because `not head` and
#: `head is None` are different trees. A dozen cards is a scroll nobody
#: reviews, and the oldest of them are a debugging session from a year ago.
MAX_SOLUTIONS = 5


def _accepted_versions(folder: Path) -> int:
    """How many accepted versions the repository holds for this problem."""
    return sum(1 for path in folder.iterdir() if _SOLUTION_RE.match(path.name))


def _solutions(folder: Path) -> list[dict]:
    """The newest few accepted versions, one per approach.

    Two filters. Versions sharing a code shape collapse to one, so the same
    solution submitted twice is not shown twice. What survives is then capped
    at `MAX_SOLUTIONS`, newest first -- file numbering follows LeetCode's
    order, so the lowest numbers are the most recent thinking.

    The folder keeps everything either way. It is the record; this is the
    reading list.
    """
    found = []
    for path in folder.iterdir():
        match = _SOLUTION_RE.match(path.name)
        if match:
            found.append((int(match.group(1)), path))

    kept: list[dict] = []
    seen: set[str] = set()
    for _, path in sorted(found):
        code = path.read_text(encoding="utf-8")
        shape = code_shape.shape_of(code)
        if shape in seen:
            continue
        seen.add(shape)
        kept.append({"name": path.name, "code": code})
        if len(kept) == MAX_SOLUTIONS:
            break
    return kept


def problem_entry(
    folder: Path,
    techniques: dict[str, str],
    ac_times: dict[str, int] | None = None,
    first_ac: dict[str, int] | None = None,
) -> dict:
    """One problem, with every layer of the chain the app reveals."""
    difficulty, technique = meta_of(folder, techniques)
    ac_times = ac_times or {}
    first_ac = first_ac or {}
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
        "pseudocode": _pseudocode_of(folder),
        # Empty for the 66 problems with no review.md. The ==marked== spans are
        # passed through untouched; the app renders them as highlights, and they
        # are the part of a retrospective worth seeing.
        "retrospective": _body_after_heading(folder / "review.md"),
        "solutions": _solutions(folder),
        # Everything the folder holds, so the card can say how much it is
        # not showing. A fact rather than a difference, so the app is not
        # trusting arithmetic done here.
        "acceptedVersions": _accepted_versions(folder),
        # When this problem was last accepted on LeetCode, or null if the
        # index does not know yet. Null rather than 0, because 0 is a real
        # date (1970) and would sort as the oldest problem in the library
        # instead of as unknown.
        "solvedAt": ac_times.get(folder.name),
        # The day this problem stopped being unsolved. Distinct from
        # solvedAt, which moves every time it is practised again: one says
        # "new", the other says "recent", and a daily count needs both.
        "firstSolvedAt": first_ac.get(folder.name),
    }


def build_payload(problems_dir: Path, techniques: dict[str, str]) -> dict:
    """The whole file. Numeric order is both readable and deterministic, and
    determinism is what keeps the diffs small."""

    def _sort_key(folder: Path) -> tuple[int, str]:
        match = _NUMBER_RE.match(folder.name)
        return (int(match.group(1)) if match else 0, folder.name)

    folders = sorted((d for d in problems_dir.iterdir() if d.is_dir()), key=_sort_key)
    solved = ac_times.load()
    first = ac_times.load(ac_times.FIRST_PATH)
    return {
        "version": SCHEMA_VERSION,
        "problems": [
            problem_entry(folder, techniques, solved, first) for folder in folders
        ],
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


def run(dry_run: bool = False) -> None:
    from .problem_source import technique_map

    payload = build_payload(PROBLEMS, technique_map())
    count = len(payload["problems"])

    if dry_run:
        # Still build the payload and compare it against disk, just don't
        # write — a dry run through sync-all must not touch content.json.
        text = _serialise(payload)
        on_disk = OUT_PATH.exists()
        changed = not (on_disk and OUT_PATH.read_text(encoding="utf-8") == text)
        if not on_disk:
            verb = "会新建"
        elif changed:
            verb = "会更新"
        else:
            verb = "不会改动"
        print(f"[试运行] 内容 {count} 道题，{verb} {OUT_PATH}")
        return

    if write_if_changed(OUT_PATH, payload):
        size = OUT_PATH.stat().st_size / 1024 / 1024
        print(f"内容 {count} 道题 -> {OUT_PATH}（{size:.1f} MB）")
    else:
        print(f"内容 {count} 道题，与磁盘上一致，未改动 {OUT_PATH}")
    # Printed either way: an unpushed file is just as stale as a never-written
    # one, and "nothing changed" is exactly the run where this is easiest to
    # forget.
    print("记得 git add app/content.json 并 push，否则手机上拿到的还是旧的。")
