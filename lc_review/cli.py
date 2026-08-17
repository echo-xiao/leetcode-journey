"""Command line entry points.

Run order matters. The full sequence is:

    build-state -> attach-fupan -> build-elements -> build-table -> export-anki

- ``build-state`` must run first: it is the only command that (re)computes
  every record's taxonomy placement from the twelve 灵神 lists and the
  ``Problems/`` scan. It carries forward ``我的复盘``, ``要素卡``,
  ``要素卡来源``, and ``已生成卡片`` from whatever state file already exists,
  so re-running it is safe -- see ``lc_review.state.build_state``.
- ``attach-fupan`` must run after ``build-state``: it hangs echo's own
  retrospectives (and their orange highlights) onto the records ``build-state``
  just (re)created.
- ``build-elements`` must run before ``build-table``: it is the only command
  that fills in each record's ``要素卡``. Running ``build-table`` first
  renders every 要素卡 cell as ``—``, because ``build-table`` only reads what
  is already in ``review_state.json`` and never assigns 要素卡 itself.
- ``export-anki`` should run last, once every field above is in its final
  state, so the three decks reflect everything.

``daily`` runs all five steps in this exact order automatically; it is the
command to reach for day to day rather than remembering this sequence by hand.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
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
from lc_review.element_essentials import ESSENTIALS
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
FRONTEND_ID_CACHE_PATH = REPO / "data" / "frontend_ids.json"

# The four lines Anki needs at the top of a TSV to import deck and tags as
# real fields instead of ordinary columns, and to render <br> / highlight
# spans as HTML instead of literal text. Column numbers are 1-indexed and
# must match the tuple order every exporter in lc_review.anki writes
# (deck, front, back, tags) -- see lc_review.anki's module docstring.
TSV_IMPORT_HEADER = "#separator:tab\n#html:true\n#deck column:1\n#tags column:4\n"


def _write_tsv(path: Path, rows: str) -> None:
    path.write_text(TSV_IMPORT_HEADER + rows, encoding="utf-8")


def _summary_records() -> list[dict]:
    """Read summary.json exactly once per command invocation.

    ``_tags_by_slug`` and ``_title_lookup`` both need it; passing the parsed
    records into both avoids parsing the same 135KB file twice per run.
    """
    if not SUMMARY_PATH.exists():
        return []
    return json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))


def _tags_by_slug(records: list[dict]) -> dict[str, list[str]]:
    """Read LeetCode's own tags out of already-parsed summary.json records.

    Only the ``tags`` field is used. ``category_main`` and ``category_sub`` in
    the same file come from a first-match-wins keyword mapping that misfiles
    most problems, and are never read.
    """
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


def _title_lookup(solved: list[SolvedProblem], records: list[dict]) -> Callable[[str], str | None]:
    """Build a slug -> Chinese title lookup from local sources only.

    Prefers already-parsed summary.json records' ``title_cn`` (only
    ``title_cn`` and ``title_en`` are read from them). Falls back to the
    leading heading of the problem's own ``README_CN.md`` for slugs
    summary.json does not cover.
    """
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


def _cached_id_resolver(
    cache_path: Path, resolver: Callable[[str], int] = resolve_frontend_id
) -> Callable[[str], int]:
    """Wrap ``resolver`` with an on-disk cache keyed by slug.

    ``classify.assign`` calls this once per taxonomy-uncovered solved
    problem; without a cache that is one live LeetCode API call per problem
    on every single run (71 of the 372 problems, as of this fix), even
    though a slug's frontend id never changes once resolved.
    """
    cache: dict[str, int] = {}
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))

    def resolve(slug: str) -> int:
        if slug in cache:
            return cache[slug]
        frontend_id = resolver(slug)
        cache[slug] = frontend_id
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(
            json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8"
        )
        return frontend_id

    return resolve


def build_state_command(refresh: bool) -> None:
    previous = load_state(STATE_PATH) if STATE_PATH.exists() else {}
    entries = fetch_all(CACHE_DIR, refresh=refresh)
    solved, malformed = scan(REPO / "Problems")
    if malformed:
        raise SystemExit(f"malformed problem directories, repair them first: {malformed}")
    summary_records = _summary_records()
    assignments, unplaceable = assign(
        entries,
        solved,
        _tags_by_slug(summary_records),
        _cached_id_resolver(FRONTEND_ID_CACHE_PATH),
        _title_lookup(solved, summary_records),
    )
    ai_sections = {
        problem.slug: read_ai_sections(REPO / "Problems" / problem.directory / "README_CN.md")
        for problem in solved
    }
    state = build_state(assignments, solved, ai_sections, previous=previous)
    save_state(state, STATE_PATH)
    report_path = REPO / "docs" / "lingshen" / "judgment-review.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_judgment_report(assignments, unplaceable), encoding="utf-8")
    print(f"wrote {len(state)} records to {STATE_PATH}")
    print(f"wrote judgment review list to {report_path}")


def attach_fupan_command() -> None:
    state = load_state(STATE_PATH)
    easy = NOTION_DIR / "easy.txt"
    medium = NOTION_DIR / "medium.txt"
    if not easy.exists() and not medium.exists():
        raise SystemExit(
            f"no Notion retrospective dump found in {NOTION_DIR} "
            "(expected easy.txt and/or medium.txt); refusing to attach "
            "nothing and silently claim it worked -- restore one of them "
            "before running attach-fupan"
        )
    retrospectives = []
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
    path.write_text(render_elements(CARDS, suggest_chapter_links(entries), state), encoding="utf-8")
    print(f"wrote {path}")


def export_anki_command() -> None:
    state = load_state(STATE_PATH)
    entries = fetch_all(CACHE_DIR)
    entry_order: dict[str, dict[tuple[str, str, str], int]] = {}
    for entry in entries:
        placement = (entry.list_no, entry.chapter or "", entry.section or "")
        entry_order.setdefault(entry.slug, {})[placement] = entry.order
    rank = weakness_rank(highlight_density(state))

    generated: dict[str, list[str]] = defaultdict(list)
    for slug, record in state.items():
        if record.get("我的复盘"):
            generated[slug].append("复习")
        ai = record.get("AI题解") or {}
        if ai.get("伪代码") or ai.get("复杂度"):
            generated[slug].append("伪代码")
    for slug, record in state.items():
        record["已生成卡片"] = generated.get(slug, [])
    save_state(state, STATE_PATH)

    out = REPO / "docs" / "anki"
    out.mkdir(parents=True, exist_ok=True)
    _write_tsv(out / "elements.tsv", export_elements(CARDS, ESSENTIALS, BODIES, rank))
    _write_tsv(out / "retrospectives.tsv", export_retrospectives(state, rank, entry_order))
    _write_tsv(out / "pseudocode.tsv", export_pseudocode(state, rank, entry_order))
    print(f"wrote three decks to {out}")


def render_daily_brief(state: dict[str, dict], new_slugs: list[str], today: str) -> str:
    """Summarise what changed, and what still needs echo's hand."""
    missing_retro = [r for r in state.values() if not r["我的复盘"]]
    no_cards = [r for r in state.values() if not r["已生成卡片"]]
    lines = [
        f"# {today} 刷题简报",
        "",
        f"新增 {len(new_slugs)} 题",
        f"待生成卡片 {len(no_cards)} 题",
        "",
        f"## 缺复盘（{len(missing_retro)} 题）",
        "",
    ]
    lines += [f"- {r['id']}. {r['题名']}" for r in sorted(missing_retro, key=lambda r: r["id"])]
    lines.append("")
    return "\n".join(lines)


def daily_command(date: str) -> None:
    previous = load_state(STATE_PATH) if STATE_PATH.exists() else {}
    build_state_command(refresh=False)
    attach_fupan_command()
    build_elements_command()
    build_table_command()
    export_anki_command()
    new_slugs = sorted(set(load_state(STATE_PATH)) - set(previous))
    path = REPO / "docs" / "daily" / f"{date}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_daily_brief(load_state(STATE_PATH), new_slugs, date), encoding="utf-8")
    print(f"wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="lc_review")
    subparsers = parser.add_subparsers(dest="command", required=True)
    build = subparsers.add_parser("build-state", help="rebuild review_state.json")
    build.add_argument("--refresh", action="store_true", help="re-download the taxonomy lists")
    subparsers.add_parser("attach-fupan", help="attach Notion retrospectives to the state file")
    subparsers.add_parser("build-table", help="regenerate the progress table")
    subparsers.add_parser("build-elements", help="regenerate the eighteen technique cards sheet")
    subparsers.add_parser("export-anki", help="export the three Anki decks as TSV")
    daily = subparsers.add_parser("daily", help="refresh everything and write today's brief")
    daily.add_argument("--date", required=True, help="YYYY-MM-DD")
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
    if args.command == "daily":
        daily_command(args.date)


if __name__ == "__main__":
    main()
