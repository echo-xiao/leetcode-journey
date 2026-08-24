"""Refresh the problems whose code changed shape since they were downloaded.

`sync_new` only ever looks at problems missing from the library, so a problem
rewritten with a different approach kept its old code, pseudocode and
elements. This closes that gap without scanning four hundred problems: it
looks only at what LeetCode reports as recently accepted, and within that only
at problems whose accepted code has a shape the repository has never held.

The expensive part -- regenerating pseudocode and elements through Claude --
happens only past that second filter. Fetching the code to compare costs
network requests and nothing else, so a day of resubmitting the same solution
costs nothing.
"""

from __future__ import annotations

from pathlib import Path

from . import code_shape, refresh_problem

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"
USERNAME = "echo666"


def candidate_slugs(submissions: list[dict]) -> list[str]:
    """Distinct slugs from the recent-accepted list, newest first."""
    seen: set[str] = set()
    slugs: list[str] = []
    for submission in submissions:
        slug = submission.get("titleSlug")
        if not slug or slug in seen:
            continue
        seen.add(slug)
        slugs.append(slug)
    return slugs


def _local_folder(slug: str) -> Path | None:
    """`3sum` -> `Problems/15_3sum`, matching the whole part after the number.

    A substring match would let `3sum` land on `18_4sum`, and a refresh
    writing into the wrong folder would be silent and hard to notice.
    """
    suffix = "_" + slug
    for path in PROBLEMS.iterdir():
        if path.is_dir() and path.name.endswith(suffix):
            return path
    return None


def needs_refresh(slug: str, remote_codes: list[str]) -> bool:
    """True when LeetCode holds a shape this problem's folder does not.

    A problem not in the library returns False: downloading it is sync-new's
    job, and doing it here would duplicate that path.
    """
    folder = _local_folder(slug)
    if folder is None:
        return False
    local = [
        path.read_text(encoding="utf-8", errors="replace")
        for path in sorted(folder.glob("solution_*"))
    ]
    if not local:
        return True
    return code_shape.has_new_shape(remote_codes, local)


def run(dry_run: bool = True, limit: int | None = None) -> list[str]:
    """Returns the slugs that were refreshed, or would be on a dry run."""
    from . import leetcode_api as fetcher

    submissions = fetcher.get_recent_ac_submissions(USERNAME)
    slugs = candidate_slugs(submissions)
    if limit:
        slugs = slugs[:limit]
    print(f"最近碰过 {len(slugs)} 道题，逐道比对代码结构")

    changed: list[str] = []
    for slug in slugs:
        if _local_folder(slug) is None:
            continue
        remote = []
        for submission in fetcher.get_all_ac_submissions(slug):
            code = fetcher.get_submission_code(submission["id"])
            if code:
                remote.append(code)
        if not remote:
            print(f"  {slug}: 没取到代码，跳过")
            continue
        if not needs_refresh(slug, remote):
            continue
        changed.append(slug)
        print(f"  {slug}: 出现了新的写法")
        if not dry_run:
            refresh_problem.run(slug, dry_run=False)

    if not changed:
        print("没有题目需要刷新")
    elif dry_run:
        print(f"待刷新 {len(changed)} 道（试运行，不写入）")
    return changed
