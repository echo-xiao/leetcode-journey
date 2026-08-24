"""Re-download one problem's accepted code and regenerate what depends on it.

`sync_new` only ever looks at problems missing from the library, so solving an
existing problem again — a better version, a different technique — left the
repository holding the old code, the old pseudocode, and elements answered
against both. The app then reviewed a version its owner had already moved on
from.

This refreshes one problem end to end: code, pseudocode, elements, and the
accepted-at dates. It is deliberately per-problem rather than a sweep; a sweep
would re-run Claude over four hundred problems to catch the handful that
changed.
"""

from __future__ import annotations

import sys
from pathlib import Path

from . import ac_times

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"

_LANG_EXT = {
    "python": "py", "python3": "py", "java": "java",
    "cpp": "cpp", "javascript": "js",
}


def folder_for(slug: str) -> Path | None:
    suffix = "_" + slug
    for path in PROBLEMS.iterdir():
        if path.is_dir() and path.name.endswith(suffix):
            return path
    return None


def local_solution_count(folder: Path) -> int:
    return len(list(folder.glob("solution_*")))


def run(slug: str, dry_run: bool = True) -> bool:
    """Returns True when something was refreshed."""
    folder = folder_for(slug)
    if folder is None:
        print(f"仓库里没有 {slug}，先跑 sync-new")
        return False

    from . import leetcode_api as fetcher

    submissions = fetcher.get_all_ac_submissions(slug)
    if not submissions:
        print(f"{slug}: 力扣没有返回 AC 提交")
        return False

    local = local_solution_count(folder)
    print(f"{folder.name}: 力扣 {len(submissions)} 版，本地 {local} 版"
          f"{'（试运行，不写入）' if dry_run else ''}")
    if dry_run:
        return len(submissions) != local

    codes: dict[str, str] = {}
    fetched: list[tuple[str, str]] = []
    for submission in submissions:
        code = fetcher.get_submission_code(submission["id"])
        if not code:
            continue
        ext = _LANG_EXT.get(submission["lang"], "txt")
        fetched.append((ext, code))
        codes[f"{submission['id']}_{submission['lang']}"] = code
    if not codes:
        print(f"{slug}: 一份代码都没取到，保留原样")
        return False

    # Old files are removed only once new ones are in hand, so a failed fetch
    # cannot leave the problem with no solutions at all.
    for old in folder.glob("solution_*"):
        old.unlink()
    for index, (ext, code) in enumerate(fetched, 1):
        (folder / f"solution_{index}.{ext}").write_text(code, encoding="utf-8")

    title = _title_of(folder)
    analysis = fetcher.ai_analyze_all_versions(title, codes)
    (folder / "pseudocode.md").write_text(
        f"# {title} · 解题思路与伪代码\n\n{analysis}\n", encoding="utf-8"
    )

    solved_at = ac_times.latest_ac_timestamp(submissions)
    first_at = ac_times.earliest_ac_timestamp(submissions)
    if solved_at is not None:
        ac_times.record(folder.name, solved_at)
    if first_at is not None:
        ac_times.record_first(folder.name, first_at)

    _rebuild_elements(folder.name)
    print(f"{folder.name}: 已刷新 {len(fetched)} 版代码、伪代码、要素")
    return True


def _title_of(folder: Path) -> str:
    path = folder / "problem.md"
    if path.exists():
        first = path.read_text(encoding="utf-8").splitlines()[0]
        return first.lstrip("# ").replace(" · 题目", "").strip()
    return folder.name


def _rebuild_elements(folder_name: str) -> None:
    """Re-answer this problem's framework slots against the new pseudocode."""
    from . import elements_build, elements_render

    argv = sys.argv
    sys.argv = ["build", f"--only={folder_name}"]
    try:
        elements_build.main()
    finally:
        sys.argv = argv
    elements_render.main()
