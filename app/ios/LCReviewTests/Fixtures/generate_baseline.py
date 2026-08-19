"""Generate the FSRS baseline the Swift port is checked against.

The Swift implementation is a port, and a port is only as trustworthy as the
fixture that pins it. Regenerate with:

    python3 app/ios/LCReviewTests/Fixtures/generate_baseline.py

Notes on the installed py-fsrs (6.x):
  - It implements FSRS-6, not FSRS-5: 21 parameters instead of 19, with the
    forgetting-curve decay as a learned parameter (parameters[20]) instead of
    a fixed -0.5/19-81 constant. The Swift port must read decay/factor from
    the parameters, not hardcode them.
  - `Scheduler()` defaults to minute-level learning_steps/relearning_steps
    and to `enable_fuzzing=True`. Both are disabled below: this app has no
    minute-level learning phase (that is handled elsewhere, same-sitting),
    and fuzzing would make the baseline non-deterministic.
"""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fsrs import Card, Rating, Scheduler

# Same three buttons the app exposes. Easy is never produced.
GRADES = {1: Rating.Again, 2: Rating.Hard, 3: Rating.Good}

# Deliberately includes a long gap (365 days) so the port is pinned on the
# overdue path, where a wrong sign silently collapses intervals instead of
# stretching them.
#
# The last four cases exist to pin the elapsed-time contract py-fsrs enforces
# before either forgetting-curve formula runs: gaps under one day route to
# `_short_term_stability` instead of the long-term formula, and gaps of one
# day or more get floored to a whole day first. Whole-day gaps ≥ 1 (the first
# eight cases) can't catch a port that skips either rule.
SEQUENCES = [
    [(3, 0)],
    [(1, 0)],
    [(2, 0)],
    [(3, 0), (3, 1)],
    [(3, 0), (1, 1)],
    [(3, 0), (3, 1), (3, 6), (3, 15)],
    [(3, 0), (3, 1), (2, 3), (1, 2), (3, 5)],
    [(3, 0), (3, 1), (3, 6), (3, 365)],
    [(3, 0), (3, 0.5)],            # 12-hour gap: short-term path
    [(3, 0), (3, 0)],              # same instant: short-term path, elapsed 0
    [(3, 0), (3, 1.5)],            # 1.5-day gap: long-term path, floored to 1
    [(3, 0), (3, 0.5), (1, 0.3)],  # a lapse (Again) following a sub-day gap
]

scheduler = Scheduler(learning_steps=(), relearning_steps=(), enable_fuzzing=False)
start = datetime(2026, 1, 1, tzinfo=timezone.utc)
out = {"parameters": list(scheduler.parameters),
       "desiredRetention": scheduler.desired_retention,
       "cases": []}

for sequence in SEQUENCES:
    card = Card()
    now = start
    steps = []
    for grade, gap in sequence:
        now = now + timedelta(days=gap)
        card, _ = scheduler.review_card(card, GRADES[grade], now)
        steps.append({
            "grade": grade,
            "elapsedDays": gap,
            "stability": card.stability,
            "difficulty": card.difficulty,
            "intervalDays": (card.due - now).total_seconds() / 86400.0,
        })
    out["cases"].append({"sequence": [g for g, _ in sequence], "steps": steps})

# Resolved relative to this script, not the caller's working directory, so
# running it from any directory (including its own) updates the fixture in
# place instead of writing a nested app/ios/... tree next to it.
path = Path(__file__).resolve().parent / "fsrs-baseline.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"wrote {path}: {len(out['cases'])} cases")
