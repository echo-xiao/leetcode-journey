"""When each problem was last accepted on LeetCode.

Kept as one index file rather than a field inside each problem folder: it is
written by two different paths (a one-off backfill over the whole library, and
`sync_new` as it downloads each new problem), and a single file keeps both of
them to one write and one diff.

It is a generated artefact — delete it and a backfill rebuilds it — but it is
committed, because `app/content.json` is built from the working tree and the
app has no other way to learn these dates. The repository stays the one source
of truth.
"""

from __future__ import annotations

import json
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "Problems" / "_ac_times.json"
#: When each problem was solved for the *first* time. Kept apart from PATH
#: because the two answer different questions and are written by different
#: rules: the last pass moves forward as you practise, the first never
#: moves at all.
FIRST_PATH = Path(__file__).resolve().parent.parent / "Problems" / "_first_ac.json"


def latest_ac_timestamp(submissions: list[dict]) -> int | None:
    """The most recent accepted submission's unix time, or None.

    The most recent rather than the first: the question this answers is "when
    did I last practise this", which is what an ordering by recency needs. A
    problem solved in 2017 and revisited yesterday is a recent problem.

    LeetCode happens to return newest first, but that is not promised
    anywhere, so the maximum is taken rather than the head. Entries whose
    timestamp will not parse are skipped instead of failing the whole
    problem — one malformed row should not cost the other submissions.
    """
    stamps: list[int] = []
    for submission in submissions:
        try:
            stamps.append(int(submission.get("timestamp")))
        except (TypeError, ValueError):
            continue
    return max(stamps) if stamps else None


def folder_for_slug(slug: str, folder_names: list[str]) -> str | None:
    """`3sum` -> `15_3sum`. None for a problem not downloaded yet.

    Matching on the part after the number rather than on a substring: `3sum`
    is a substring of `15_3sum` but also of `18_4sum`-adjacent names, and a
    wrong match would move another problem's date.
    """
    suffix = "_" + slug
    for name in folder_names:
        if name.endswith(suffix):
            return name
    return None


def merge_recent(
    submissions: list[dict], index: dict[str, int], folder_names: list[str]
) -> int:
    """Fold LeetCode's recent-accepted list into the index. Returns how many
    dates moved.

    Only ever moves a date forward. The recent list is capped at twenty
    entries and can report an older pass than the one already recorded; taking
    it would make a problem look staler than it is and push it back up the
    queue.

    A problem that is not in the library yet is skipped rather than recorded
    against a folder that does not exist. `sync_new` downloads it and records
    its date in the same pass.
    """
    changed = 0
    for submission in submissions:
        slug = submission.get("titleSlug")
        if not slug:
            continue
        folder = folder_for_slug(slug, folder_names)
        if folder is None:
            continue
        try:
            stamp = int(submission.get("timestamp"))
        except (TypeError, ValueError):
            continue
        if stamp > index.get(folder, 0):
            index[folder] = stamp
            changed += 1
    return changed


def earliest_ac_timestamp(submissions: list[dict]) -> int | None:
    """The first accepted submission's unix time, or None.

    The counterpart to `latest_ac_timestamp`: this is the day a problem stopped
    being unsolved, which is what separates新刷 from 复习 in a daily count.
    """
    stamps: list[int] = []
    for submission in submissions:
        try:
            stamps.append(int(submission.get("timestamp")))
        except (TypeError, ValueError):
            continue
    return min(stamps) if stamps else None


def record_first(problem_id: str, timestamp: int, path: Path | None = None) -> None:
    """Set one problem's first-solved date, keeping the earlier of the two.

    The opposite rule to `record`. A first pass is a fact about the past, so a
    later run seeing a newer submission must not overwrite it; but an earlier
    one turning up (a deeper page of history) should win.
    """
    path = path or FIRST_PATH
    index = load(path)
    existing = index.get(problem_id)
    index[problem_id] = min(int(timestamp), existing) if existing else int(timestamp)
    save(index, path)


def load(path: Path | None = None) -> dict[str, int]:
    """The index, or an empty one if it does not exist yet.

    A file that exists but does not parse raises rather than reading as empty:
    treating it as empty would make the next `record` overwrite every date in
    it with a single entry.
    """
    path = path or PATH
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path} is not valid JSON: {error}") from error


def save(index: dict[str, int], path: Path | None = None) -> None:
    """Sorted, so a run that adds one problem produces a one-line diff."""
    path = path or PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    path.write_text(text, encoding="utf-8")


def record(problem_id: str, timestamp: int, path: Path | None = None) -> None:
    """Set one problem's date, overwriting any earlier value.

    Overwriting rather than keeping the older date: a re-solved problem is
    recent again, and that is the whole point of the field.
    """
    index = load(path)
    index[problem_id] = int(timestamp)
    save(index, path)
