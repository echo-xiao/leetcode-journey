"""Command line entry points.

One pipeline, in one direction:

    LeetCode ──sync-new──▶ Problems/ ──build-answers──▶ elements.md
    Notion 复盘页 ──sync-review-md──▶ review.md
                 └──sync-fupan──▶ 「LC 旧题回顾」复盘列

``sync-all`` runs all four in the order they depend on each other and is the
command to reach for day to day. The order is not cosmetic: a problem has to
exist locally before its retrospective can be filed next to it, and its review
row has to exist before the 复盘 column can be written.

Every command defaults to a dry run. Three of the four write outside the
working tree — into Notion, which has no undo — so writing is opt-in via
``--apply``.
"""

from __future__ import annotations

import argparse


def sync_review_md_command(apply: bool) -> None:
    """Notion retrospectives -> Problems/*/review.md."""
    from .sync_review_md import sync

    sync(dry_run=not apply)


def sync_fupan_command(apply: bool) -> None:
    """Notion retrospectives -> the 复盘 column of 「LC 旧题回顾」."""
    from .notion_pages import fetch_easy, fetch_medium
    from .sync_fupan import sync

    sync(fetch_easy(), fetch_medium(), titles={}, dry_run=not apply)


def sync_new_command(apply: bool, limit: int | None) -> None:
    """Newly solved LeetCode problems -> Problems/ + a row in 「LC 旧题回顾」."""
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


def sync_all_command(apply: bool) -> None:
    """The day-to-day command: LeetCode -> Problems/ -> Notion, in that order."""
    steps = (
        ("拉取新 AC 题并在 Notion 建行", lambda: sync_new_command(apply, None)),
        ("生成新题的要素答案", lambda: build_answers_command(apply, None)),
        ("复盘写入 Problems/*/review.md", lambda: sync_review_md_command(apply)),
        ("复盘写入 Notion 复盘列", lambda: sync_fupan_command(apply)),
    )
    for index, (label, step) in enumerate(steps, 1):
        print(f"\n[{index}/{len(steps)}] {label}")
        step()
    if not apply:
        print("\n以上为试运行。确认无误后加 --apply 实际写入。")


def main() -> None:
    parser = argparse.ArgumentParser(prog="lc_review")
    subparsers = parser.add_subparsers(dest="command", required=True)

    all_cmd = subparsers.add_parser("sync-all", help="日常一条龙：新题、要素、review.md、Notion")
    all_cmd.add_argument("--apply", action="store_true", help="实际写入")

    new = subparsers.add_parser("sync-new", help="下载新 AC 题并在 Notion 建行")
    new.add_argument("--apply", action="store_true", help="实际下载并写入")
    new.add_argument("--limit", type=int, default=None, help="最多处理几道")

    answers = subparsers.add_parser("build-answers", help="逐题生成要素答案")
    answers.add_argument("--apply", action="store_true", help="同时渲染 elements.md")
    answers.add_argument("--limit", type=int, default=None, help="最多处理几道")

    review_md = subparsers.add_parser("sync-review-md", help="复盘写入 Problems/*/review.md")
    review_md.add_argument("--apply", action="store_true", help="实际写文件")

    fupan = subparsers.add_parser("sync-fupan", help="复盘写入 Notion 复盘列")
    fupan.add_argument("--apply", action="store_true", help="实际写入 Notion")

    # Writes only into anki/ inside the repo, so there is nothing to opt into.
    subparsers.add_parser("export-anki", help="导出 Anki 卡片 TSV")

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


if __name__ == "__main__":
    main()
