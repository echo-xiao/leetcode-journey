"""Move the accepted-at date forward for problems solved again recently.

`sync_new` records a date only for problems it downloads, so re-solving a
problem already in the library would leave it looking as stale as the day it
was first solved -- and "review what I just practised" is exactly what that
date is for.

One request, no authentication. LeetCode caps the recent-accepted list at
twenty entries whatever limit is asked for, so this keeps recent activity
honest rather than replacing the one-off backfill.
"""

from __future__ import annotations

from pathlib import Path

from . import ac_times

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"
USERNAME = "echo666"


def run(dry_run: bool = True) -> int:
    """Returns how many dates moved forward."""
    from . import leetcode_api as fetcher

    submissions = fetcher.get_recent_ac_submissions(USERNAME)
    if not submissions:
        print("力扣没有返回最近通过记录，跳过")
        return 0

    index = ac_times.load()
    folders = [d.name for d in PROBLEMS.iterdir() if d.is_dir()]
    # Merged into a copy first, so a dry run can report the same number the
    # real run would change without writing anything.
    preview = dict(index)
    changed = ac_times.merge_recent(submissions, preview, folders)

    print(f"最近通过 {len(submissions)} 条，其中 {changed} 道题的日期需要更新"
          f"{'（试运行，不写入）' if dry_run else ''}")
    if dry_run or not changed:
        return changed

    ac_times.save(preview)
    return changed
