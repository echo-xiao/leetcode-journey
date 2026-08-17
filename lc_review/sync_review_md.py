"""Write each problem's retrospective into its folder as review.md.

The retrospectives live in two Notion pages as running logs. This puts a copy
next to the code they are about, so a problem folder holds the whole picture:
statement, approach, framework slots, and what actually went wrong.

Highlights are kept. Notion's ``<span color="orange">`` does not render on
GitHub, so the marked text becomes bold — the emphasis survives in a form the
target actually displays.
"""

from __future__ import annotations

import re
from pathlib import Path

from .fupan import Retrospective, parse_easy_page, parse_medium_page
from .notion_pages import fetch_easy, fetch_medium

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"

SPAN_OPEN_RE = re.compile(r'<span color=\\?"[a-z_]+\\?">')
SPAN_CLOSE_RE = re.compile(r"</span>")
ESCAPE_RE = re.compile(r"\\([|\[\]<>*_`])")


def to_markdown(body: str) -> str:
    """Notion export markup -> GitHub markdown, keeping the highlights visible.

    Bold is how the orange marking survives: GitHub strips the colour span
    outright, which would erase echo's own record of what tripped her up.
    """
    text = SPAN_OPEN_RE.sub("**", body)
    text = SPAN_CLOSE_RE.sub("**", text)
    text = ESCAPE_RE.sub(r"\1", text)
    text = re.sub(r"\*\*\s*\*\*", "", text)          # empty bold from adjacent spans
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    # A span opened in the source and never closed leaves an odd marker, which
    # renders as a literal ** and swallows the rest of the paragraph. Drop the
    # stray one rather than guessing where the emphasis was meant to end.
    if text.count("**") % 2:
        text = text[::-1].replace("**", "", 1)[::-1]
    return text


def folder_index() -> dict[int, Path]:
    """Problem id -> folder.

    The retrospectives number problems the way leetcode.cn does; the folders
    are named after leetcode.com ids, and for many problems the two differ
    (509 斐波那契数 is folder 1013_fibonacci-number). 「LC 旧题回顾」carries both
    — 题号 is the .cn id, 代码 links the repo folder — so it is the bridge.
    Folder-prefix matching is kept as a fallback for anything the table has
    not catalogued.
    """
    index: dict[int, Path] = {}
    if not PROBLEMS.exists():
        return index

    for path in PROBLEMS.iterdir():
        if path.is_dir():
            head = path.name.split("_", 1)[0]
            if head.isdigit():
                index.setdefault(int(head), path)

    try:
        from .notion_api import REVIEW_DB, query_all, read_number, read_url
    except Exception:
        return index
    try:
        rows = query_all(REVIEW_DB)
    except Exception as error:                       # offline or unshared: keep the fallback
        print(f"  (未能读取 Notion 映射，仅用文件夹前缀匹配: {error})")
        return index

    for row in rows:
        number = read_number(row, "题号")
        code_url = read_url(row, "代码")
        if number is None or not code_url:
            continue
        folder = PROBLEMS / code_url.rstrip("/").rsplit("/", 1)[-1]
        if folder.is_dir():
            index[int(number)] = folder          # .cn id wins over prefix guess
    return index


def title_of(folder: Path) -> str:
    problem = folder / "problem.md"
    if problem.exists():
        first = problem.read_text(encoding="utf-8").splitlines()[0]
        return first.lstrip("# ").replace(" · 题目", "").strip()
    return folder.name


def render(title: str, entries: list[Retrospective]) -> str:
    """One review.md. Multiple passes over a problem are kept in order.

    No Day/topic heading: it says nothing about the problem itself, and the
    file is read while looking at this one problem's code. Several passes are
    separated by a rule instead.
    """
    bodies = [to_markdown(entry.body) for entry in entries]
    bodies = [b for b in bodies if b]
    if not bodies:
        return ""
    return f"# {title} · 复盘\n\n" + "\n\n---\n\n".join(bodies) + "\n"


def sync(dry_run: bool = True) -> tuple[int, int]:
    """Write review.md for every problem that has a retrospective.

    Returns (written, orphaned) — orphaned means a retrospective whose problem
    has no folder here, which is reported rather than dropped.
    """
    by_id: dict[int, list[Retrospective]] = {}
    for entry in parse_easy_page(fetch_easy()) + parse_medium_page(fetch_medium()):
        by_id.setdefault(entry.problem_id, []).append(entry)

    folders = folder_index()
    written = 0
    orphans: list[int] = []
    empty: list[int] = []
    for problem_id, entries in sorted(by_id.items()):
        folder = folders.get(problem_id)
        if folder is None:
            orphans.append(problem_id)
            continue
        content = render(title_of(folder), entries)
        if not content:
            empty.append(problem_id)     # heading with no body in the source
            continue
        if not dry_run:
            (folder / "review.md").write_text(content, encoding="utf-8")
        written += 1

    print(f"写入 review.md {written} 个{'（试运行）' if dry_run else ''}；"
          f"{len(orphans)} 条复盘在仓库里没有对应文件夹；"
          f"{len(empty)} 条原文只有标题没有正文，跳过不建空文件")
    if orphans:
        print("  无对应文件夹的题号:", ", ".join(str(i) for i in orphans[:20]),
              "..." if len(orphans) > 20 else "")
    return written, len(orphans)
