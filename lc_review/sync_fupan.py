"""Push the Notion retrospective pages into the per-problem review rows.

Both retrospective pages are written as running logs — easy as
``20、valid parentheses：body`` lines, medium as ``N、LC 1456 title：body``
under ``Day`` headings. ``lc_review.fupan`` already knows how to read them;
this module decides where each entry lands in 「LC 旧题回顾」.

A problem can appear more than once across the two pages (echo revisited 34
of them). Those bodies are joined rather than overwritten, so a later pass
never silently drops an earlier note.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .fupan import Retrospective, parse_easy_page, parse_medium_page
from .notion_api import (
    REVIEW_DB,
    create_page,
    prop_number,
    prop_select,
    prop_rich,
    prop_text,
    prop_title,
    prop_url,
    query_all,
    read_number,
    read_text,
    update_page,
)

SPAN_RE = re.compile(r'</?span[^>]*>')
SPAN_PAIR_RE = re.compile(r'<span color=\\?"[a-z_]+\\?">(.*?)</span>', re.DOTALL)
BOLD_RE = re.compile(r'\*\*(.+?)\*\*', re.DOTALL)
ESCAPE_RE = re.compile(r'\\([|\[\]<>*_`])')


def _clean(text: str) -> str:
    text = BOLD_RE.sub(r"\1", text)
    text = ESCAPE_RE.sub(r"\1", text)
    return re.sub(r"[ \t]+", " ", text)


def to_plain(body: str) -> str:
    """Markup-free text, for callers that cannot carry formatting."""
    return _clean(SPAN_RE.sub("", body)).strip()


def to_segments(body: str) -> list[tuple[str, bool]]:
    """Split into (text, highlighted) runs so the orange marking survives.

    Notion's rich-text properties do carry annotations, so the highlights can
    be rebuilt on the far side instead of being flattened away.
    """
    segments: list[tuple[str, bool]] = []
    cursor = 0
    for match in SPAN_PAIR_RE.finditer(body):
        before = body[cursor:match.start()]
        if before:
            segments.append((_clean(SPAN_RE.sub("", before)), False))
        inner = _clean(SPAN_RE.sub("", match.group(1)))
        if inner:
            segments.append((inner, True))
        cursor = match.end()
    tail = body[cursor:]
    if tail:
        segments.append((_clean(SPAN_RE.sub("", tail)), False))
    return segments


@dataclass(frozen=True)
class Plan:
    """What a sync would do, before it does it."""

    update: dict[int, str]                              # problem id -> combined body
    create: dict[int, str]
    segments: dict[int, list[tuple[str, bool]]]         # same content, highlight runs
    skipped_no_id: int


def collect(easy_text: str, medium_text: str) -> dict[int, list[Retrospective]]:
    """All retrospectives keyed by problem id, easy first then medium."""
    by_id: dict[int, list[Retrospective]] = {}
    for entry in parse_easy_page(easy_text) + parse_medium_page(medium_text):
        by_id.setdefault(entry.problem_id, []).append(entry)
    return by_id


def combine(entries: list[Retrospective]) -> str:
    """One cell of text for a problem, keeping every pass echo wrote.

    No Day/topic prefix: the row already carries 二级 and 三级 columns saying
    the same thing, so repeating it in the cell is noise. review.md keeps the
    heading, because a standalone file has no columns to lean on.
    """
    parts = [to_plain(entry.body) for entry in entries]
    return "\n\n".join(part for part in parts if part)


def combine_segments(entries: list[Retrospective]) -> list[tuple[str, bool]]:
    """Same content as ``combine`` but as highlighted/plain runs."""
    segments: list[tuple[str, bool]] = []
    for index, entry in enumerate(entries):
        if index:
            segments.append(("\n\n", False))
        segments.extend(to_segments(entry.body))
    return [(t, h) for t, h in segments if t]


def build_plan(by_id: dict[int, list[Retrospective]], rows: list[dict]) -> Plan:
    existing = {}
    for row in rows:
        number = read_number(row, "题号")
        if number is not None:
            existing[int(number)] = row
    update: dict[int, str] = {}
    create: dict[int, str] = {}
    segments: dict[int, list[tuple[str, bool]]] = {}
    for problem_id, entries in by_id.items():
        body = combine(entries)
        if not body:
            continue
        segments[problem_id] = combine_segments(entries)
        (update if problem_id in existing else create)[problem_id] = body
    return Plan(update=update, create=create, segments=segments, skipped_no_id=0)


def apply_plan(plan: Plan, rows: list[dict], titles: dict[int, str], dry_run: bool = True) -> None:
    by_number = {}
    for row in rows:
        number = read_number(row, "题号")
        if number is not None:
            by_number[int(number)] = row

    print(f"更新已有行 {len(plan.update)} 条，新建行 {len(plan.create)} 条"
          f"{'（试运行，不写入）' if dry_run else ''}")
    if dry_run:
        return

    written = 0
    for problem_id, body in sorted(plan.update.items()):
        row = by_number[problem_id]
        if read_text(row, "复盘").strip() == body.strip():
            continue                     # already synced; skip the write
        update_page(row["id"], {"复盘": prop_rich(plan.segments[problem_id])})
        written += 1
        if written % 25 == 0:
            print(f"  已更新 {written}/{len(plan.update)}", flush=True)
    print(f"  更新完成 {written} 条")

    for problem_id, body in sorted(plan.create.items()):
        create_page(
            REVIEW_DB,
            {
                "题名字": prop_title(titles.get(problem_id, f"LC {problem_id}")),
                "题号": prop_number(problem_id),
                "复盘": prop_rich(plan.segments[problem_id]),
                "归属来源": prop_select("外-我判定"),
                "链接": prop_url(None),
            },
        )
    print(f"  新建完成 {len(plan.create)} 条")


def sync(easy_text: str, medium_text: str, titles: dict[int, str], dry_run: bool = True) -> Plan:
    by_id = collect(easy_text, medium_text)
    rows = query_all(REVIEW_DB)
    plan = build_plan(by_id, rows)
    apply_plan(plan, rows, titles, dry_run=dry_run)
    return plan
