"""Command line entry points."""

from __future__ import annotations

import argparse
import json
import re
from collections.abc import Callable
from pathlib import Path

from lc_review.anki import (
    export_elements,
    export_pseudocode,
    export_retrospectives,
    highlight_density,
    weakness_rank,
)
from lc_review.classify import assign
from lc_review.element_bodies import BODIES
from lc_review.elements import CARDS, link_state_to_cards, render_elements, suggest_chapter_links
from lc_review.fupan import attach, parse_easy_page, parse_medium_page
from lc_review.lingshen import fetch_all
from lc_review.problems import SolvedProblem, read_ai_sections, resolve_frontend_id, scan
from lc_review.state import build_state, load_state, render_judgment_report, save_state
from lc_review.table import render_table

REPO = Path(__file__).resolve().parent.parent
STATE_PATH = REPO / "review_state.json"
CACHE_DIR = REPO / "data" / "lingshen"
SUMMARY_PATH = REPO / "summary.json"
NOTION_DIR = REPO / "data" / "notion"


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


README_TITLE_HEADING_RE = re.compile(r"^#\s*\d+\.\s*(.+?)\s*$", re.MULTILINE)


def parse_readme_title_heading(text: str) -> str | None:
    """Parse the leading ``# <number>. <title>`` heading of a README_CN.md.

    Returns just the title, with the number and separator stripped. Returns
    ``None`` when no such heading is present.
    """
    match = README_TITLE_HEADING_RE.search(text)
    if match is None:
        return None
    return match.group(1)


def _title_lookup(solved: list[SolvedProblem]) -> Callable[[str], str | None]:
    """Build a slug -> Chinese title lookup from local sources only.

    Prefers ``summary.json``'s ``title_cn`` (only ``title_cn`` and
    ``title_en`` are read from it). Falls back to the leading heading of the
    problem's own ``README_CN.md`` for slugs summary.json does not cover.
    """
    titles_by_slug: dict[str, str] = {}
    if SUMMARY_PATH.exists():
        records = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
        titles_by_slug = {record["title_en"]: record["title_cn"] for record in records}
    readme_by_slug = {problem.slug: problem.directory for problem in solved}

    def lookup(slug: str) -> str | None:
        title = titles_by_slug.get(slug)
        if title:
            return title
        directory = readme_by_slug.get(slug)
        if directory is None:
            return None
        readme = REPO / "Problems" / directory / "README_CN.md"
        if not readme.exists():
            return None
        return parse_readme_title_heading(readme.read_text(encoding="utf-8"))

    return lookup


def build_state_command(refresh: bool) -> None:
    entries = fetch_all(CACHE_DIR, refresh=refresh)
    solved, malformed = scan(REPO / "Problems")
    if malformed:
        raise SystemExit(f"malformed problem directories, repair them first: {malformed}")
    assignments, unplaceable = assign(
        entries, solved, _tags_by_slug(), resolve_frontend_id, _title_lookup(solved)
    )
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


def attach_fupan_command() -> None:
    state = load_state(STATE_PATH)
    retrospectives = []
    easy = NOTION_DIR / "easy.txt"
    medium = NOTION_DIR / "medium.txt"
    if easy.exists():
        retrospectives += parse_easy_page(easy.read_text(encoding="utf-8"))
    if medium.exists():
        retrospectives += parse_medium_page(medium.read_text(encoding="utf-8"))
    state, orphans = attach(state, retrospectives)
    save_state(state, STATE_PATH)
    with_retro = sum(1 for record in state.values() if record["我的复盘"] is not None)
    orphan_path = REPO / "docs" / "lingshen" / "retrospectives-without-code.md"
    orphan_path.parent.mkdir(parents=True, exist_ok=True)
    orphan_path.write_text(
        "# Retrospectives with no local solution\n\n"
        + "\n".join(f"- {o.problem_id} ({o.source})" for o in sorted(orphans, key=lambda o: o.problem_id))
        + "\n",
        encoding="utf-8",
    )
    print(f"attached {with_retro} retrospectives; {len(orphans)} have no local code")


def build_table_command() -> None:
    state = load_state(STATE_PATH)
    entries = fetch_all(CACHE_DIR)
    path = REPO / "docs" / "lingshen" / "大表.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_table(state, entries), encoding="utf-8")
    print(f"wrote {path}")


def build_elements_command() -> None:
    entries = fetch_all(CACHE_DIR)
    state = load_state(STATE_PATH)
    linked, unlinked = link_state_to_cards(state, entries)
    save_state(state, STATE_PATH)
    print(f"linked {linked} state records to a card; {unlinked} matched no card")
    path = REPO / "docs" / "lingshen" / "要素表.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_elements(CARDS, suggest_chapter_links(entries), BODIES), encoding="utf-8")
    print(f"wrote {path}")


def export_anki_command() -> None:
    state = load_state(STATE_PATH)
    entries = fetch_all(CACHE_DIR)
    entry_order = {}
    for entry in entries:
        entry_order.setdefault((entry.list_no, entry.chapter or "", entry.section or ""), entry.order)
    rank = weakness_rank(highlight_density(state))
    out = REPO / "docs" / "anki"
    out.mkdir(parents=True, exist_ok=True)
    (out / "elements.tsv").write_text(export_elements(CARDS, {}), encoding="utf-8")
    (out / "retrospectives.tsv").write_text(
        export_retrospectives(state, rank, entry_order), encoding="utf-8"
    )
    (out / "pseudocode.tsv").write_text(
        export_pseudocode(state, rank, entry_order), encoding="utf-8"
    )
    print(f"wrote three decks to {out}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="lc_review")
    subparsers = parser.add_subparsers(dest="command", required=True)
    build = subparsers.add_parser("build-state", help="rebuild review_state.json")
    build.add_argument("--refresh", action="store_true", help="re-download the taxonomy lists")
    subparsers.add_parser("attach-fupan", help="attach Notion retrospectives to the state file")
    subparsers.add_parser("build-table", help="regenerate the progress table")
    subparsers.add_parser("build-elements", help="regenerate the eighteen technique cards sheet")
    subparsers.add_parser("export-anki", help="export the three Anki decks as TSV")
    args = parser.parse_args()
    if args.command == "build-state":
        build_state_command(args.refresh)
    if args.command == "attach-fupan":
        attach_fupan_command()
    if args.command == "build-table":
        build_table_command()
    if args.command == "build-elements":
        build_elements_command()
    if args.command == "export-anki":
        export_anki_command()


if __name__ == "__main__":
    main()
