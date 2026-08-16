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
# tag is optional and consumed as part of the header (captured, so it can be
# re-applied to the body below) so it never leaks into the body; the header
# also swallows an immediate closing tag so a number-wrapping span does not
# turn into a garbage highlight containing the entry number and title (see
# extract_highlights docstring). Sometimes that same opening span instead
# closes partway through the body -- e.g. problem 589, where
# ``<span color="orange">589、title：``real highlight``</span>rest`` -- and the
# header's own optional close does not fire because it only matches
# immediately after the colon; see _rebalance_dangling_span for how that
# dangling ``</span>`` is repaired.
_SPAN_OPEN = r'(<span color=\\?"[a-z_]+\\?">)?'
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


def _rebalance_dangling_span(span_open: str | None, body: str) -> str:
    """Re-pair a highlight span whose opening tag sat before the entry number.

    When echo's orange span opens before the number and closes partway
    through the body (problem 589 is the canonical example -- see
    ``_SPAN_OPEN`` above), the entry-header regex consumes the opening tag as
    header noise, leaving a ``</span>`` in the body with no matching opener.
    That drops the highlighted text (``extract_highlights`` needs a matched
    pair) and leaves malformed HTML for ``to_anki_html`` to choke on.
    Re-prepending the original opening tag to the body restores the pair
    without pulling the number/title back into the highlight, since those
    were already stripped by the header match.
    """
    if not span_open:
        return body
    close_pos = body.find("</span>")
    if close_pos == -1:
        return body
    open_match = HIGHLIGHT_OPEN_RE.search(body)
    if open_match is not None and open_match.start() < close_pos:
        # The body already has its own well-formed span; nothing dangling.
        return body
    return span_open + body


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
        body = line[match.end() : end].strip()
        body = _rebalance_dangling_span(match.group(1), body)
        pairs.append((match.group(2), body))
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

    A problem id can appear more than once across the two Notion pages (42 do
    in practice). Only the longest body is kept as ``正文``, but every
    duplicate's highlights are unioned into ``高亮`` -- in first-seen order,
    exact duplicates collapsed -- because a shorter, losing body can still
    carry a highlight the winning body never mentions.
    """
    slug_by_id = {record["id"]: slug for slug, record in state.items()}
    orphans: list[Retrospective] = []
    highlights_by_slug: dict[str, list[str]] = {}
    for slug, record in state.items():
        existing = record.get("我的复盘")
        if existing is not None:
            highlights_by_slug[slug] = list(existing.get("高亮", []))

    for retro in retrospectives:
        slug = slug_by_id.get(retro.problem_id)
        if slug is None:
            orphans.append(retro)
            continue
        seen = highlights_by_slug.setdefault(slug, [])
        for highlight in retro.highlights:
            if highlight not in seen:
                seen.append(highlight)
        existing = state[slug].get("我的复盘")
        if existing is not None and len(existing["正文"]) >= len(retro.body):
            continue
        state[slug]["我的复盘"] = {
            "来源": retro.source,
            "正文": retro.body,
            "高亮": [],  # filled in below once every duplicate has been seen
            "Day": retro.day,
            "模式": retro.topic,
            "日期": retro.date,
        }

    for slug, highlights in highlights_by_slug.items():
        record = state[slug].get("我的复盘")
        if record is not None:
            record["高亮"] = highlights
    return state, orphans
