"""Parse echo's own retrospectives out of two Notion pages.

These are the only real retrospectives. The ``解题思路与复盘`` block inside each
README_CN.md is GPT-4o output describing accepted code, and is handled
separately as reference material.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

EASY_ENTRY_RE = re.compile(r"(?<!\d)(\d{1,4})、\s*([A-Za-z][^：\n]{3,80})：(.*)")
MEDIUM_ENTRY_RE = re.compile(r"^\d+、\s*LC\s*(\d+)\s*[^：\n]*：(.*)")
MEDIUM_DAY_RE = re.compile(r"--\s*(Day\s*\d+)\s*\|\s*(.+?)\s*\((\d{4}-\d{2}-\d{2})\)\s*---")

# Notion emits <span color="orange">…</span>; the MCP transport sometimes
# backslash-escapes the quotes, so both spellings must match.
HIGHLIGHT_RE = re.compile(r'<span color=\\?"[a-z_]+\\?">(.*?)</span>', re.DOTALL)
HIGHLIGHT_OPEN_RE = re.compile(r'<span color=\\?"[a-z_]+\\?">')
HIGHLIGHT_STYLE = '<span style="background:#ffe0b2">'


@dataclass(frozen=True)
class Retrospective:
    """One problem's retrospective as echo wrote it, highlights included."""

    problem_id: int
    body: str
    source: str
    day: str | None
    topic: str | None
    date: str | None
    highlights: tuple[str, ...] = ()


def extract_highlights(body: str) -> tuple[str, ...]:
    """Return the text echo marked in orange — her own record of what she got wrong."""
    return tuple(match.strip() for match in HIGHLIGHT_RE.findall(body) if match.strip())


def to_anki_html(body: str) -> str:
    """Rewrite Notion colour spans as background-shaded spans Anki can render.

    Anki does not understand Notion's ``color`` attribute, so a straight copy
    would render as unstyled text and the highlight would silently vanish.
    """
    return HIGHLIGHT_OPEN_RE.sub(HIGHLIGHT_STYLE, body)


def parse_easy_page(text: str) -> list[Retrospective]:
    """Parse ``1385、english title：body`` entries.

    The page opens with unrelated coffee-chat and job-hunting notes. They are
    skipped because they do not match the entry shape, not by a content filter.
    """
    found: list[Retrospective] = []
    for line in text.splitlines():
        match = EASY_ENTRY_RE.search(line)
        if match is None:
            continue
        problem_id, _title, body = match.groups()
        body = body.strip()
        found.append(
            Retrospective(
                int(problem_id), body, "notion-easy", None, None, None,
                extract_highlights(body),
            )
        )
    return found


def parse_medium_page(text: str) -> list[Retrospective]:
    """Parse ``N、LC 1456 title：body`` entries under ``Day`` headings."""
    day: str | None = None
    topic: str | None = None
    date: str | None = None
    found: list[Retrospective] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        heading = MEDIUM_DAY_RE.search(line)
        if heading is not None:
            day, topic, date = heading.group(1), heading.group(2), heading.group(3)
            continue
        match = MEDIUM_ENTRY_RE.match(line)
        if match is None:
            continue
        problem_id, body = match.groups()
        body = body.strip()
        found.append(
            Retrospective(
                int(problem_id), body, "notion-medium", day, topic, date,
                extract_highlights(body),
            )
        )
    return found


def attach(
    state: dict[str, dict], retrospectives: list[Retrospective]
) -> tuple[dict[str, dict], list[Retrospective]]:
    """Hang retrospectives onto state records by problem id.

    A retrospective with no matching local record is returned as an orphan
    rather than dropped: echo wrote roughly 170 of those for problems whose
    code never got synced down, and losing them would lose real work.
    """
    slug_by_id = {record["id"]: slug for slug, record in state.items()}
    orphans: list[Retrospective] = []
    for retro in retrospectives:
        slug = slug_by_id.get(retro.problem_id)
        if slug is None:
            orphans.append(retro)
            continue
        existing = state[slug].get("我的复盘")
        if existing is not None and len(existing["正文"]) >= len(retro.body):
            continue
        state[slug]["我的复盘"] = {
            "来源": retro.source,
            "正文": retro.body,
            "高亮": list(retro.highlights),
            "Day": retro.day,
            "模式": retro.topic,
            "日期": retro.date,
        }
    return state, orphans
