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
