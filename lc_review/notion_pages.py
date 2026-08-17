"""Render a Notion page back into the text shape the retrospective parsers expect.

``lc_review.fupan`` was written against Notion's *export* format: colour
emphasis arrives as ``<span color="orange">…</span>`` and pipes are
backslash-escaped. The REST API instead returns rich-text runs with an
``annotations`` object, so a naive plain-text render would drop every
highlight — and the highlights are the whole point, they are echo's own
record of what she got wrong.

This module rebuilds the span markup from annotations so the existing
parsers keep working unchanged.
"""

from __future__ import annotations

from .notion_api import _request

EASY_PAGE = "23e23475-3881-8070-bd8d-d452b95de664"      # Leetcode 刷题复盘 - easy
MEDIUM_PAGE = "36a23475-3881-80f3-85ad-cced95b68fd0"    # LeetCode 刷题复盘 - medium


def _render_rich_text(runs: list[dict]) -> str:
    parts: list[str] = []
    for run in runs:
        text = run.get("plain_text", "")
        if not text:
            continue
        ann = run.get("annotations", {})
        colour = ann.get("color", "default")
        if colour and colour != "default":
            # Match the export spelling the parsers key off.
            text = f'<span color="{colour.replace("_background", "")}">{text}</span>'
        if ann.get("bold"):
            text = f"**{text}**"
        if ann.get("code"):
            text = f"`{text}`"
        parts.append(text)
    return "".join(parts)


def _block_children(block_id: str) -> list[dict]:
    blocks: list[dict] = []
    cursor = None
    while True:
        query = f"?page_size=100" + (f"&start_cursor={cursor}" if cursor else "")
        data = _request("GET", f"/blocks/{block_id}/children{query}")
        blocks.extend(data.get("results", []))
        if not data.get("has_more"):
            return blocks
        cursor = data["next_cursor"]


def render_page(page_id: str) -> str:
    """Flatten a page (and nested children) into one text blob."""
    lines: list[str] = []

    def walk(block_id: str) -> None:
        for block in _block_children(block_id):
            kind = block.get("type")
            payload = block.get(kind, {}) or {}
            runs = payload.get("rich_text") or []
            text = _render_rich_text(runs)
            if kind == "code":
                language = payload.get("language", "")
                lines.append(f"```{language}\n{text}\n```")
            elif text:
                lines.append(text)
            if block.get("has_children"):
                walk(block["id"])

    walk(page_id)
    return "\n".join(lines)


def fetch_easy() -> str:
    return render_page(EASY_PAGE)


def fetch_medium() -> str:
    return render_page(MEDIUM_PAGE)
