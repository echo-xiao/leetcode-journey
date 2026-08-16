"""Command line entry points."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from lc_review.classify import assign
from lc_review.lingshen import fetch_all
from lc_review.problems import read_ai_sections, resolve_frontend_id, scan
from lc_review.state import build_state, render_judgment_report, save_state

REPO = Path(__file__).resolve().parent.parent
STATE_PATH = REPO / "review_state.json"
CACHE_DIR = REPO / "data" / "lingshen"
SUMMARY_PATH = REPO / "summary.json"


def _tags_by_slug() -> dict[str, list[str]]:
    """Read LeetCode's own tags out of summary.json.

    Only the ``tags`` field is used. ``category_main`` and ``category_sub`` in
    the same file come from a first-match-wins keyword mapping that misfiles
    most problems, and are never read.
    """
    if not SUMMARY_PATH.exists():
        return {}
    records = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    return {record["title_en"]: record.get("tags", []) for record in records}


def build_state_command(refresh: bool) -> None:
    entries = fetch_all(CACHE_DIR, refresh=refresh)
    solved, malformed = scan(REPO / "Problems")
    if malformed:
        raise SystemExit(f"malformed problem directories, repair them first: {malformed}")
    assignments, unplaceable = assign(entries, solved, _tags_by_slug(), resolve_frontend_id)
    ai_sections = {
        problem.slug: read_ai_sections(REPO / "Problems" / problem.directory / "README_CN.md")
        for problem in solved
    }
    state = build_state(assignments, solved, ai_sections)
    save_state(state, STATE_PATH)
    report_path = REPO / "docs" / "lingshen" / "judgment-review.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_judgment_report(state, unplaceable), encoding="utf-8")
    print(f"wrote {len(state)} records to {STATE_PATH}")
    print(f"wrote judgment review list to {report_path}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="lc_review")
    subparsers = parser.add_subparsers(dest="command", required=True)
    build = subparsers.add_parser("build-state", help="rebuild review_state.json")
    build.add_argument("--refresh", action="store_true", help="re-download the taxonomy lists")
    args = parser.parse_args()
    if args.command == "build-state":
        build_state_command(args.refresh)


if __name__ == "__main__":
    main()
