"""Pull newly solved problems down and register them everywhere.

Three things have to agree: LeetCode (what you actually solved), the Problems
folder (code plus the four markdown files), and 「LC 旧题回顾」(the row you
review from). This module walks that gap.

The LeetCode session expires every few weeks. When it does, the API keeps
answering — with zero solved problems — so a silent run would look like a
successful no-op forever. ``require_session`` turns that into a loud failure.
"""

from __future__ import annotations

import os
from pathlib import Path

from . import ac_times

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"


def require_session() -> tuple[str, int]:
    """Fail loudly when the LeetCode cookie has expired.

    Returns (username, solved_count). An expired session answers 200 with an
    empty username and zero solved, which is indistinguishable from "nothing
    new" unless it is checked for explicitly.
    """
    from . import leetcode_api as fetcher

    data = fetcher.session.get(f"{fetcher.BASE_URL_EN}/api/problems/all/", timeout=25).json()
    user = data.get("user_name") or ""
    solved = data.get("num_solved") or 0
    if not user or not solved:
        raise SystemExit(
            "LeetCode session 已失效：接口返回空用户名 / 0 道通过题。\n"
            "在 Chrome 里重新登录 leetcode.com，把 LEETCODE_SESSION 更新到 .env 再跑。"
        )
    return user, solved


def local_slugs() -> set[str]:
    """Slugs already downloaded, read off the folder names."""
    if not PROBLEMS.exists():
        return set()
    return {
        path.name.split("_", 1)[1]
        for path in PROBLEMS.iterdir()
        if path.is_dir() and "_" in path.name
    }


def missing_questions() -> list[dict]:
    """Solved on LeetCode but absent from Problems/."""
    from . import leetcode_api as fetcher

    have = local_slugs()
    return [q for q in fetcher.get_all_ac_questions(fetcher.session) if q["titleSlug"] not in have]


def register_in_notion(entries: list[dict], dry_run: bool = True) -> int:
    """Create a 「LC 旧题回顾」row for each newly downloaded problem.

    Rows are keyed on 题号. Anything already present is left alone rather than
    duplicated — the table is the thing echo reviews from, and a double row
    would quietly split a problem's history in two.
    """
    from .notion_api import (
        REVIEW_DB,
        create_page,
        prop_number,
        prop_select,
        prop_title,
        prop_url,
        query_all,
        read_number,
    )

    existing = {
        int(read_number(row, "题号"))
        for row in query_all(REVIEW_DB)
        if read_number(row, "题号") is not None
    }
    todo = [e for e in entries if int(e["question_id"]) not in existing]
    print(f"Notion 建行 {len(todo)} 条{'（试运行）' if dry_run else ''}")
    if dry_run:
        return len(todo)

    for entry in todo:
        create_page(
            REVIEW_DB,
            {
                "题名字": prop_title(entry["title"]),
                "题号": prop_number(int(entry["question_id"])),
                "链接": prop_url(f"https://leetcode.cn/problems/{entry['slug']}/"),
                "代码": prop_url(
                    "https://github.com/echo-xiao/leetcode-journey/tree/main/Problems/"
                    f"{entry['folder']}"
                ),
                "归属来源": prop_select("外-我判定"),
            },
        )
    return len(todo)


def run(dry_run: bool = True, limit: int | None = None) -> list[dict]:
    """Download what is missing, write the markdown, then register the rows."""
    user, solved = require_session()
    print(f"👤 {user} | 力扣已通过 {solved} 道 | 本地 {len(local_slugs())} 道")

    from . import leetcode_api as fetcher

    pending = missing_questions()
    if limit:
        pending = pending[:limit]
    print(f"待下载 {len(pending)} 道{'（试运行，不下载）' if dry_run else ''}")
    if dry_run or not pending:
        return []

    downloaded: list[dict] = []
    for question in pending:
        slug = question["titleSlug"]
        try:
            q_id, difficulty, tags, prob_cn = fetcher.get_problem_details(slug)
            if q_id is None:
                print(f"  跳过 {slug}: 拿不到元数据")
                continue
            title = (prob_cn.get("translatedTitle") if prob_cn else slug) or slug
            folder = PROBLEMS / f"{q_id}_{slug}"
            folder.mkdir(parents=True, exist_ok=True)

            subs = fetcher.get_all_ac_submissions(slug)
            # Free here: this response was fetched for the code anyway, and
            # it carries the timestamps. Recorded before the code is even
            # written out, so a problem whose code fetch fails still leaves
            # no half-written date behind -- the folder is skipped below and
            # the next run retries the whole problem.
            solved_at = ac_times.latest_ac_timestamp(subs)
            first_at = ac_times.earliest_ac_timestamp(subs)
            codes: dict[str, str] = {}
            for index, sub in enumerate(subs):
                code = fetcher.get_submission_code(sub["id"])
                if not code:
                    continue
                ext = {"python": "py", "python3": "py", "java": "java",
                       "cpp": "cpp", "javascript": "js"}.get(sub["lang"], "txt")
                (folder / f"solution_{index + 1}.{ext}").write_text(code, encoding="utf-8")
                codes[f"{sub['id']}_{sub['lang']}"] = code
            if not codes:
                print(f"  跳过 {slug}: 没有取到代码")
                continue

            analysis = fetcher.ai_analyze_all_versions(title, codes)
            main_cat, sub_cat = fetcher.classify_question(tags, title)
            description = (prob_cn.get("translatedContent") if prob_cn else None) or "暂无描述"
            fetcher.write_problem_files(
                str(folder), q_id, title, difficulty, tags, main_cat, sub_cat, description, analysis
            )
            if solved_at is not None:
                ac_times.record(folder.name, solved_at)
            if first_at is not None:
                ac_times.record_first(folder.name, first_at)
            downloaded.append(
                {"question_id": q_id, "slug": slug, "title": title, "folder": folder.name}
            )
            print(f"  ✓ {q_id} {title}")
        except Exception as error:
            print(f"  ✗ {slug}: {error}")

    print(f"下载完成 {len(downloaded)} 道")
    register_in_notion(downloaded, dry_run=False)
    return downloaded
