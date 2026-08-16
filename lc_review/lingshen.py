"""Fetch and parse the twelve EndlessCheng (灵神) classification lists."""

from __future__ import annotations

import re
from dataclasses import dataclass

ENTRY_RE = re.compile(
    r"^-\s*\[(\d+)\.\s*(.+?)\]\(https://leetcode\.cn/problems/([a-z0-9\-]+)/?\)\s*(\d+)?"
)


@dataclass(frozen=True)
class ProblemEntry:
    """One problem as it appears in one of the twelve lists."""

    list_no: str
    list_name: str
    problem_id: int
    title: str
    slug: str
    rating: int | None
    chapter: str | None
    section: str | None
    order: int


def parse_list(text: str, list_no: str, list_name: str) -> list[ProblemEntry]:
    """Turn one list's raw markdown into ordered problem entries.

    Headings carry the taxonomy: ``## `` starts a chapter, ``### `` a section.
    A chapter heading resets the current section so entries that sit directly
    under a chapter get ``section=None`` rather than leaking the previous one.
    """
    chapter: str | None = None
    section: str | None = None
    entries: list[ProblemEntry] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("### "):
            section = line[4:].strip()
            continue
        if line.startswith("## "):
            chapter = line[3:].strip()
            section = None
            continue
        match = ENTRY_RE.match(line)
        if match is None:
            continue
        problem_id, title, slug, rating = match.groups()
        entries.append(
            ProblemEntry(
                list_no=list_no,
                list_name=list_name,
                problem_id=int(problem_id),
                title=title.strip(),
                slug=slug,
                rating=int(rating) if rating else None,
                chapter=chapter,
                section=section,
                order=len(entries),
            )
        )
    return entries
