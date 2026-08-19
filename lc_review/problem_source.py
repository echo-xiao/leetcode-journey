"""Read one problem's parts out of ``Problems/<folder>/``.

Both exporters read through here, so the Anki deck and the app payload can
never drift apart on what "the statement" or "the slots" mean.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"

TAG_RE = re.compile(r"<[^>]+>")
# Block-level tags carry the statement's line structure. Collapsing them into
# spaces along with the inline tags turns a worked example into one long
# run-on, which is exactly what makes a card unreadable.
BLOCK_END_RE = re.compile(r"</(p|pre|div|li|ul|ol|h[1-6]|blockquote)>|<br\s*/?>", re.I)
# Only the constraints block is dropped. The worked examples stay: several
# statements are one clause long because the real definition sits behind a
# link on the site ("判断它是否是平衡二叉树"), and without the examples the card
# gives you nothing to recall from.
TRIM_RE = re.compile(r"(提示[：:]|进阶[：:]|Constraints[：:])")


def _plain(text: str) -> str:
    """HTML -> text, keeping paragraph and line breaks.

    Inline tags vanish outright rather than becoming spaces: "<strong>输入：
    </strong>nums" should read "输入：nums", not "输入： nums".
    """
    text = BLOCK_END_RE.sub("\n", text)
    text = TAG_RE.sub("", text)
    text = html.unescape(text)
    text = text.replace(" ", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def statement_of(folder: Path, limit: int | None = 500) -> str:
    """The problem statement, trimmed to the part that prompts recall.

    ``limit`` caps the length for Anki, whose cards cannot scroll. The app can
    scroll, so it passes ``None`` and gets the whole statement; capping there
    would cut the worked examples off 130 of the 402 problems.
    """
    path = folder / "problem.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if "## 题目描述" not in text:
        return ""
    body = _plain(text.split("## 题目描述", 1)[1])
    cut = TRIM_RE.search(body)
    if cut and cut.start() > 30:
        body = body[: cut.start()].strip()
    if limit is None or len(body) <= limit:
        return body
    # Cut on a line boundary; slicing mid-sentence looks like a bug.
    kept: list[str] = []
    used = 0
    for line in body.splitlines():
        if used + len(line) > limit:
            break
        kept.append(line)
        used += len(line) + 1
    return "\n".join(kept).strip() or body[:limit]


def title_of(folder: Path) -> str:
    path = folder / "problem.md"
    if not path.exists():
        return folder.name
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return first.lstrip("# ").replace(" · 题目", "").strip()


def elements_of(folder: Path) -> list[str]:
    """The answered slots, as ``槽位：答案`` lines."""
    path = folder / "elements.md"
    if not path.exists():
        return []
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        # Slot labels can contain spaces and latin text ("base case"), so the
        # label is whatever precedes the first full-width colon.
        if re.match(r"^\d+\.\s+[^：]{1,20}：", line):
            lines.append(re.sub(r"^\d+\.\s*", "", line))
    return lines


def meta_of(folder: Path, techniques: dict[str, str]) -> tuple[str, str]:
    """(difficulty, technique)."""
    difficulty = ""
    problem = folder / "problem.md"
    if problem.exists():
        match = re.search(r"\*\*难度\*\*:\s*(\w+)", problem.read_text(encoding="utf-8"))
        if match:
            difficulty = match.group(1)
    return difficulty, techniques.get(folder.name, "")


def technique_map() -> dict[str, str]:
    """folder -> technique, from the same tables elements.md was rendered from.

    ``load_map`` merges the hand-labelled ``yaosu_map.tsv`` (303 rows) with the
    model-inferred ``inferred_tags.tsv`` (99 rows). Reading only the latter
    would leave 303 problems with no technique at all.
    """
    from .elements_render import load_map

    return load_map()
