"""Fetch and parse the twelve EndlessCheng (灵神) classification lists."""

from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

ENTRY_RE = re.compile(
    r"^-\s*\[(\d+)\.\s*(.+?)\]\(https://leetcode\.cn/problems/([a-z0-9\-]+)/?\)\s*(\d+)?"
)

POST_URL = "https://leetcode.cn/discuss/post/{slug}/"
USER_AGENT = "Mozilla/5.0"
NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.DOTALL
)
MIN_CONTENT_LENGTH = 2000

# (list_no, list_name, discuss slug). Read from the "算法题单" footer of the
# dynamic-programming post; re-read that footer before editing.
LISTS: tuple[tuple[str, str, str], ...] = (
    ("1", "滑动窗口与双指针", "0viNMK"),
    ("2", "二分算法", "SqopEo"),
    ("3", "单调栈", "9oZFK9"),
    ("4", "网格图", "YiXPXW"),
    ("5", "位运算", "dHn9Vk"),
    ("6", "图论算法", "01LUak"),
    ("7", "动态规划", "tXLS3i"),
    ("8", "常用数据结构", "mOr1u6"),
    ("9", "数学算法", "IYT3ss"),
    ("10", "贪心与思维", "g6KTKL"),
    ("11", "链表、树与回溯", "K0n2gO"),
    ("12", "字符串", "SJFwQI"),
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


def _walk_for_content(node: object) -> Iterator[str]:
    """Yield every long ``content`` string anywhere in a decoded JSON tree."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "content" and isinstance(value, str) and len(value) > MIN_CONTENT_LENGTH:
                yield value
            else:
                yield from _walk_for_content(value)
    elif isinstance(node, list):
        for value in node:
            yield from _walk_for_content(value)


def _walk_for_qa_question_content(node: object) -> Iterator[str]:
    """Yield ``content`` strings found under a ``qaQuestion`` key.

    This is the known-correct shape of the post payload
    (``...state.data.qaQuestion.content``), so a match here is preferred
    over any other long ``content`` string that might appear elsewhere in
    the tree.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "qaQuestion" and isinstance(value, dict):
                content = value.get("content")
                if isinstance(content, str):
                    yield content
                    continue
            yield from _walk_for_qa_question_content(value)
    elif isinstance(node, list):
        for value in node:
            yield from _walk_for_qa_question_content(value)


def extract_post_content(html: str) -> str:
    """Return the post's raw markdown from an embedded __NEXT_DATA__ blob.

    The exact JSON path is
    ``props.pageProps.dehydratedState.queries[1].state.data.qaQuestion.content``
    but the query index is not stable across posts, so we search the tree
    instead of hard-coding it. The search is preferential: a ``content``
    string nested under a ``qaQuestion`` key is the known-correct shape and
    is returned first if present; only if that search finds nothing do we
    fall back to the first sufficiently long ``content`` string anywhere in
    the tree.
    """
    match = NEXT_DATA_RE.search(html)
    if match is None:
        raise ValueError("no __NEXT_DATA__ script found in page")
    tree = json.loads(match.group(1))
    content = next(_walk_for_qa_question_content(tree), None)
    if content is None:
        content = next(_walk_for_content(tree), None)
    if content is None:
        raise ValueError("no post content found inside __NEXT_DATA__")
    return content


def _download(slug: str) -> str:
    request = urllib.request.Request(
        POST_URL.format(slug=slug), headers={"User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def fetch_all(cache_dir: Path, refresh: bool = False) -> list[ProblemEntry]:
    """Fetch (or reuse cached copies of) all twelve lists and parse them."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    entries: list[ProblemEntry] = []
    for list_no, list_name, slug in LISTS:
        cached = cache_dir / f"{list_no}.md"
        if refresh or not cached.exists():
            cached.write_text(extract_post_content(_download(slug)), encoding="utf-8")
        entries.extend(parse_list(cached.read_text(encoding="utf-8"), list_no, list_name))
    return entries
