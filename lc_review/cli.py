"""Command line entry points.

One pipeline, in one direction:

    LeetCode ──sync-new──▶ Problems/ ──build-answers──▶ elements.md
    Notion retro pages ──sync-review-md──▶ review.md
                       └──sync-fupan──▶ review tracker's retrospective column
    Problems/ ──export-app──▶ app/content.json ──▶ the iOS app

``sync-all`` runs all five in the order they depend on each other and is the
command to reach for day to day. The order is not cosmetic: a problem has to
exist locally before its retrospective can be filed next to it, its review
row has to exist before the retrospective column can be written, and the app payload has to
be packed last or it ships the previous run's markdown.

Every command defaults to a dry run. Three of the five write outside the
working tree — into Notion, which has no undo — so writing is opt-in via
``--apply``. The two exporters only write inside the repository.
"""

from __future__ import annotations

import argparse


def sync_review_md_command(apply: bool) -> None:
    """Notion retrospectives -> Problems/*/review.md."""
    from .sync_review_md import sync

    sync(dry_run=not apply)


def sync_fupan_command(apply: bool) -> None:
    """Notion retrospectives -> the retrospective column of the review tracker."""
    from .notion_pages import fetch_easy, fetch_medium
    from .sync_fupan import sync

    sync(fetch_easy(), fetch_medium(), titles={}, dry_run=not apply)


def sync_new_command(apply: bool, limit: int | None) -> None:
    """Newly solved LeetCode problems -> Problems/ + a row in the review tracker."""
    from .sync_new import run

    run(dry_run=not apply, limit=limit)


def build_answers_command(apply: bool, limit: int | None) -> None:
    """Answer each problem's framework slots, then render elements.md.

    One Claude call per problem, so it only fills in what is missing.
    """
    import sys

    from . import elements_build, elements_render

    argv = sys.argv
    sys.argv = ["build"] + ([f"--limit={limit}"] if limit else [])
    try:
        elements_build.main()
    finally:
        sys.argv = argv
    if apply:
        elements_render.main()


def export_anki_command() -> None:
    """Problems/*/ -> anki/*.tsv, ready to import."""
    from .anki_export import run

    run()


def export_app_command(apply: bool = True) -> None:
    """Problems/*/ -> app/content.json, which the iOS app downloads.

    ``apply`` defaults to True because the standalone ``export-app``
    subcommand always writes — it only writes inside the repo, so there is
    nothing to opt into. ``sync-all`` is the caller that passes ``apply``
    through so a dry run of the whole pipeline stays dry for this step too.
    """
    from .app_export import run

    run(dry_run=not apply)


def refresh_changed_command(apply: bool, limit: int | None) -> None:
    """Refresh the recently-touched problems whose code changed shape.

    Sits between sync-new and build-answers in the pipeline: after the new
    problems have arrived (they need no refresh) and before the elements are
    answered (a refresh rewrites the pseudocode they are answered against).
    """
    from .refresh_changed import run

    run(dry_run=not apply, limit=limit)


def refresh_problem_command(slug: str, apply: bool) -> None:
    """Re-download one problem's code and regenerate pseudocode and elements.

    For a problem solved again after it was already in the library: sync-new
    never revisits those, so the repository keeps the old version.
    """
    from .refresh_problem import run

    run(slug, dry_run=not apply)


def refresh_ac_times_command(apply: bool) -> None:
    """Move the accepted-at date forward for problems solved again recently.

    One request, so it rides along in ``sync-all`` before the content is
    packed. Without it, re-solving a problem already in the library leaves it
    looking as stale as the day it was first solved.
    """
    from .refresh_ac_times import run

    run(dry_run=not apply)


def backfill_ac_times_command(apply: bool, limit: int | None) -> None:
    """A one-off: ask LeetCode for the accepted-at date of older problems.

    Not part of ``sync-all``. Every problem downloaded from now on gets its
    date for free, so this is only for the library that predates the field,
    and running it on a schedule would be several hundred pointless
    requests a day.
    """
    from .backfill_ac_times import run

    run(dry_run=not apply, limit=limit)


def sync_all_command(apply: bool) -> None:
    """The day-to-day command: LeetCode -> Problems/ -> Notion, in that order."""
    steps = (
        ("Refresh accepted times of recently re-solved problems", lambda: refresh_ac_times_command(apply)),
        ("Pull new AC problems and create Notion rows", lambda: sync_new_command(apply, None)),
        ("Refresh old problems whose solution changed", lambda: refresh_changed_command(apply, None)),
        ("Generate element answers for new problems", lambda: build_answers_command(apply, None)),
        ("Write retrospectives into Problems/*/review.md", lambda: sync_review_md_command(apply)),
        ("Write retrospectives into the Notion column", lambda: sync_fupan_command(apply)),
        ("Package app content app/content.json", lambda: export_app_command(apply)),
    )
    for index, (label, step) in enumerate(steps, 1):
        print(f"\n[{index}/{len(steps)}] {label}")
        step()
    if not apply:
        print("\nThis was a dry run. Add --apply to actually write.")


def main() -> None:
    parser = argparse.ArgumentParser(prog="lc_review")
    subparsers = parser.add_subparsers(dest="command", required=True)

    all_cmd = subparsers.add_parser("sync-all", help="daily pipeline: new problems, elements, review.md, Notion")
    all_cmd.add_argument("--apply", action="store_true", help="actually write")

    new = subparsers.add_parser("sync-new", help="download new AC problems and create Notion rows")
    new.add_argument("--apply", action="store_true", help="actually download and write")
    new.add_argument("--limit", type=int, default=None, help="process at most N problems")

    answers = subparsers.add_parser("build-answers", help="generate element answers per problem")
    answers.add_argument("--apply", action="store_true", help="also render elements.md")
    answers.add_argument("--limit", type=int, default=None, help="process at most N problems")

    review_md = subparsers.add_parser("sync-review-md", help="write retrospectives into Problems/*/review.md")
    review_md.add_argument("--apply", action="store_true", help="actually write files")

    fupan = subparsers.add_parser("sync-fupan", help="write retrospectives into the Notion column")
    fupan.add_argument("--apply", action="store_true", help="actually write to Notion")

    # Writes only into anki/ inside the repo, so there is nothing to opt into.
    subparsers.add_parser("export-anki", help="export Anki flashcard TSV")

    # Writes only into app/ inside the repo, so there is nothing to opt into.
    subparsers.add_parser("export-app", help="export app content content.json")

    changed = subparsers.add_parser(
        "refresh-changed", help="refresh old problems whose solution recently changed"
    )
    changed.add_argument("--apply", action="store_true", help="actually write")
    changed.add_argument("--limit", type=int, help="only check the most recent N")

    problem = subparsers.add_parser(
        "refresh-problem", help="re-download one problem's code and regenerate pseudocode and elements"
    )
    problem.add_argument("slug", help="problem slug, e.g. trapping-rain-water")
    problem.add_argument("--apply", action="store_true", help="actually write")

    refresh = subparsers.add_parser(
        "refresh-ac-times", help="refresh accepted times of recently re-solved problems"
    )
    refresh.add_argument("--apply", action="store_true", help="actually write")

    backfill = subparsers.add_parser(
        "backfill-ac-times", help="one-off: backfill accepted times for older problems"
    )
    backfill.add_argument("--apply", action="store_true", help="actually request and write")
    backfill.add_argument("--limit", type=int, help="only process the first N, as a trial")

    args = parser.parse_args()
    if args.command == "sync-all":
        sync_all_command(args.apply)
    elif args.command == "sync-new":
        sync_new_command(args.apply, args.limit)
    elif args.command == "build-answers":
        build_answers_command(args.apply, args.limit)
    elif args.command == "sync-review-md":
        sync_review_md_command(args.apply)
    elif args.command == "sync-fupan":
        sync_fupan_command(args.apply)
    elif args.command == "export-anki":
        export_anki_command()
    elif args.command == "export-app":
        export_app_command()
    elif args.command == "refresh-changed":
        refresh_changed_command(args.apply, args.limit)
    elif args.command == "refresh-problem":
        refresh_problem_command(args.slug, args.apply)
    elif args.command == "refresh-ac-times":
        refresh_ac_times_command(args.apply)
    elif args.command == "backfill-ac-times":
        backfill_ac_times_command(args.apply, args.limit)


if __name__ == "__main__":
    main()
