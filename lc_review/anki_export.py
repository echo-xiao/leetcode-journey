"""Build Anki decks from the per-problem markdown.

Everything comes out of ``Problems/*/``. Notion is not consulted: the markdown
is already the synced copy, and reading it keeps the export runnable offline
and reproducible from a checkout.

Decks are kept separate on purpose. Anki schedules per card, and the three
kinds of material want different rhythms — the framework slots settle down
after a few passes, while the mistakes worth re-reading are the ones echo
highlighted. Merging them into one card would force a single interval on both.

The readers live in ``problem_source`` so the app exporter reads the same way.
"""

from __future__ import annotations

from pathlib import Path

from .problem_source import (
    PROBLEMS,
    REPO,
    elements_of,
    meta_of,
    statement_of,
    technique_map as _technique_map,
    title_of,
)

OUT_DIR = REPO / "anki"

# Anki reads these four directives at the top of a TSV to treat deck and tags
# as real fields rather than ordinary columns, and to render the HTML we emit
# instead of printing it literally. Column numbers are 1-indexed and must match
# the tuple order each builder writes: (deck, front, back, tags).
TSV_HEADER = "#separator:tab\n#html:true\n#deck column:1\n#tags column:4\n"


def _row(deck: str, front: str, back: str, tags: str) -> str:
    """One TSV line. Tabs and newlines would break the format, so they go."""
    clean = lambda s: s.replace("\t", " ").replace("\n", "<br>")
    return "\t".join((deck, clean(front), clean(back), tags))


def _elements_row(folder: Path, techniques: dict[str, str]) -> str | None:
    """One folder's TSV row, or None when it has no answered slots yet."""
    slots = elements_of(folder)
    if not slots:
        return None
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
    return _row("LeetCode::要素", front, back, tags)


def build_elements_deck() -> list[str]:
    """Front: the problem. Back: how its framework slots get filled."""
    techniques = _technique_map()
    rows = []
    for folder in sorted(PROBLEMS.iterdir()):
        if not folder.is_dir():
            continue
        row = _elements_row(folder, techniques)
        if row is not None:
            rows.append(row)
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
