"""Fill in the accepted-at date for problems downloaded before it was recorded.

A one-off. `sync_new` records the date for every problem from now on, taking
it out of a response it already fetches; this exists only because the 402
problems downloaded before that code existed have no date at all.

It is slow on purpose: LeetCode's list endpoint returns only ids and slugs, so
the timestamp has to be asked for one problem at a time, and the calls are
paced. Roughly five minutes for the whole library. Progress is written to disk
as it goes, so an interrupted run keeps what it got and the next run skips it.
"""

from __future__ import annotations

import re
import time
from pathlib import Path

from . import ac_times

REPO = Path(__file__).resolve().parent.parent
PROBLEMS = REPO / "Problems"

_SLUG_RE = re.compile(r"^\d+_(.+)$")


def slug_of(folder_name: str) -> str | None:
    """`15_3sum` -> `3sum`. None for anything that is not a problem folder."""
    match = _SLUG_RE.match(folder_name)
    return match.group(1) if match else None


def pending_folders(index: dict[str, int]) -> list[str]:
    """Problem folders with no date yet, oldest problem number first.

    Sorted so an interrupted run resumes somewhere predictable rather than
    wherever the filesystem happened to list.
    """
    names = [
        d.name
        for d in PROBLEMS.iterdir()
        if d.is_dir() and slug_of(d.name) and d.name not in index
    ]
    return sorted(names, key=lambda name: int(name.split("_", 1)[0]))


def run(dry_run: bool = True, limit: int | None = None, pause: float = 0.7) -> int:
    """Ask LeetCode for each missing date. Returns how many were recorded."""
    index = ac_times.load()
    pending = pending_folders(index)
    if limit:
        pending = pending[:limit]

    print(f"已有日期 {len(index)} 道 | 待补 {len(pending)} 道"
          f"{'（试运行，不请求也不写入）' if dry_run else ''}")
    if dry_run or not pending:
        return 0

    from . import leetcode_api as fetcher

    recorded = 0
    for position, folder_name in enumerate(pending, 1):
        slug = slug_of(folder_name)
        try:
            submissions = fetcher.get_all_ac_submissions(slug)
            solved_at = ac_times.latest_ac_timestamp(submissions)
            if solved_at is None:
                print(f"  跳过 {folder_name}: 没有取到通过记录")
                continue
            # Written every iteration rather than once at the end: five
            # minutes is long enough that an interruption is a real
            # possibility, and losing the whole run to it would be avoidable.
            ac_times.record(folder_name, solved_at)
            recorded += 1
            if position % 25 == 0 or position == len(pending):
                print(f"  已补 {position} / {len(pending)}")
        except Exception as error:
            print(f"  ✗ {folder_name}: {error}")
        time.sleep(pause)

    print(f"补齐 {recorded} 道，索引现有 {len(ac_times.load())} 道")
    return recorded
