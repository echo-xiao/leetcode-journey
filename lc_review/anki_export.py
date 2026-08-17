"""Build Anki decks from the per-problem markdown.

Everything comes out of ``Problems/*/``. Notion is not consulted: the markdown
is already the synced copy, and reading it keeps the export runnable offline
and reproducible from a checkout.

Decks are kept separate on purpose. Anki schedules per card, and the three
kinds of material want different rhythms — the framework slots settle down
after a few passes, while the mistakes worth re-reading are the ones echo
highlighted. Merging them into one card would force a single interval on both.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"
OUT_DIR = REPO / "anki"

# Anki reads these four directives at the top of a TSV to treat deck and tags
# as real fields rather than ordinary columns, and to render the HTML we emit
# instead of printing it literally. Column numbers are 1-indexed and must match
# the tuple order each builder writes: (deck, front, back, tags).
TSV_HEADER = "#separator:tab\n#html:true\n#deck column:1\n#tags column:4\n"

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
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def statement_of(folder: Path, limit: int = 500) -> str:
    """The problem statement, trimmed to the part that prompts recall."""
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
    if len(body) <= limit:
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


def _technique_map() -> dict[str, str]:
    """folder -> technique, from the same tables elements.md was rendered from.

    elements.md itself no longer prints the technique (echo asked for the file
    to carry nothing but the slots), so it has to come from the source tables.
    """
    from .elements_render import load_map

    return load_map()


def meta_of(folder: Path, techniques: dict[str, str]) -> tuple[str, str]:
    """(difficulty, technique)."""
    difficulty = ""
    problem = folder / "problem.md"
    if problem.exists():
        match = re.search(r"\*\*难度\*\*:\s*(\w+)", problem.read_text(encoding="utf-8"))
        if match:
            difficulty = match.group(1)
    return difficulty, techniques.get(folder.name, "")


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


def _row(deck: str, front: str, back: str, tags: str) -> str:
    """One TSV line. Tabs and newlines would break the format, so they go."""
    clean = lambda s: s.replace("\t", " ").replace("\n", "<br>")
    return "\t".join((deck, clean(front), clean(back), tags))


def build_elements_deck() -> list[str]:
    """Front: the problem. Back: how its framework slots get filled."""
    rows = []
    techniques = _technique_map()
    for folder in sorted(PROBLEMS.iterdir()):
        if not folder.is_dir():
            continue
        slots = elements_of(folder)
        if not slots:
            continue
        title = title_of(folder)
        difficulty, technique = meta_of(folder, techniques)
        statement = statement_of(folder)

        front = f"<b>{title}</b>"
        if statement:
            front += f"<br><br>{statement}"
        front += "<br><br><i>这道题的要素怎么填？</i>"

        back = f"<b>{technique}</b><br><br>" if technique else ""
        back += "<br>".join(f"{index}. {slot}" for index, slot in enumerate(slots, 1))

        tags = " ".join(t for t in (technique, difficulty) if t)
        rows.append(_row("LeetCode::要素", front, back, tags))
    return rows


def write(rows: list[str], name: str) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    path.write_text(TSV_HEADER + "\n".join(rows) + "\n", encoding="utf-8")
    return path


def run() -> None:
    rows = build_elements_deck()
    path = write(rows, "elements.tsv")
    print(f"要素卡 {len(rows)} 张 -> {path}")
