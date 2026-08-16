"""Parse echo's own retrospectives out of two Notion pages.

These are the only real retrospectives. The ``解题思路与复盘`` block inside each
README_CN.md is GPT-4o output describing accepted code, and is handled
separately as reference material.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# A colour span sometimes wraps the entry number itself, e.g.
# ``<span color="orange">2、LC 904 水果成篮：</span>难点在于...``. The opening
# tag is optional and consumed as part of the header so it never leaks into
# the body; the header also swallows an immediate closing tag so a
# number-wrapping span does not turn into a garbage highlight containing the
# entry number and title (see extract_highlights docstring).
_SPAN_OPEN = r'(?:<span color=\\?"[a-z_]+\\?">)?'
_SPAN_CLOSE = r"(?:</span>)?"

EASY_ENTRY_RE = re.compile(
    _SPAN_OPEN + r"(?<!\d)(\d{1,4})、\s*[A-Za-z][^：\n]{3,80}：\s*" + _SPAN_CLOSE
)
MEDIUM_ENTRY_RE = re.compile(
    _SPAN_OPEN + r"\d+、\s*LC\s*(\d+)\s*[^：\n]*：\s*" + _SPAN_CLOSE
)
# Notion's export backslash-escapes the "|" separator on some pages; both
# spellings must match or every Day heading -- and every entry's day/topic/
# date -- silently comes back None.
MEDIUM_DAY_RE = re.compile(r"--\s*(Day\s*\d+)\s*\\?\|\s*(.+?)\s*\((\d{4}-\d{2}-\d{2})\)\s*---")
BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)


def _normalize_line_breaks(text: str) -> str:
    """Turn literal ``<br>``/``<br/>``/``<br />`` into real newlines.

    Notion frequently packs several numbered entries onto one physical line
    separated by literal ``<br>`` text rather than real newlines. Without
    this, only the first entry on such a line is ever seen.
    """
    return BR_RE.sub("\n", text)


def _entries_in_line(pattern: re.Pattern[str], line: str) -> list[tuple[str, str]]:
    """Split one line into (captured_id, body) pairs for every entry match.

    A line can hold more than one entry after ``<br>`` normalisation (or, in
    principle, if Notion already separated them without a line break). Each
    entry's body runs from the end of its header to the start of the next
    entry's header, or to the end of the line.
    """
    matches = list(pattern.finditer(line))
    pairs = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(line)
        pairs.append((match.group(1), line[match.end() : end].strip()))
    return pairs

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
    for line in _normalize_line_breaks(text).splitlines():
        for problem_id, body in _entries_in_line(EASY_ENTRY_RE, line):
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
    for raw_line in _normalize_line_breaks(text).splitlines():
        line = raw_line.strip()
        heading = MEDIUM_DAY_RE.search(line)
        if heading is not None:
            day, topic, date = heading.group(1), heading.group(2), heading.group(3)
            continue
        for problem_id, body in _entries_in_line(MEDIUM_ENTRY_RE, line):
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
