"""Render the grouped progress table."""

from __future__ import annotations

from collections import defaultdict

from lc_review.classify import ORIGIN_CROSS, ORIGIN_OUTSIDE
from lc_review.lingshen import ProblemEntry

MARKERS = {ORIGIN_CROSS: "[跨]", ORIGIN_OUTSIDE: "[外]"}
COLUMNS = "| 题号 | 题名 | 难度分 | 要素卡 | 代码 | 我的复盘 | 已出卡 |"
DIVIDER = "|---|---|---|---|---|---|---|"


def _row(record: dict) -> str:
    marker = MARKERS.get(record["归属来源"], "")
    retro = "有" if record["我的复盘"] else "缺"
    cards = "/".join(record["已生成卡片"]) or "—"
    rating = record["难度分"] if record["难度分"] is not None else "—"
    return (
        f"| {record['id']} | {marker}{record['题名']} | {rating} | "
        f"{record['要素卡'] or '—'} | `{record['代码']}` | {retro} | {cards} |"
    )


def render_table(state: dict[str, dict], entries: list[ProblemEntry]) -> str:
    """Group solved problems under the source taxonomy, verbatim headings.

    Unsolved problems never become rows. Their only trace is the denominator on
    each heading and the trailing list of sections with nothing solved in them,
    which keeps the file readable while still showing where the gaps are.
    """
    totals: dict[tuple[str, str, str], int] = defaultdict(int)
    order: dict[tuple[str, str, str], int] = {}
    chapter_order: dict[tuple[str, str], int] = {}
    names: dict[str, str] = {}
    for entry in entries:
        key = (entry.list_no, entry.chapter or "", entry.section or "")
        totals[key] += 1
        order.setdefault(key, entry.order)
        chapter_key = (entry.list_no, entry.chapter or "")
        if chapter_key not in chapter_order or entry.order < chapter_order[chapter_key]:
            chapter_order[chapter_key] = entry.order
        names[entry.list_no] = entry.list_name

    solved_by_key: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for record in state.values():
        list_no = record["题单"].split(".", 1)[0]
        solved_by_key[(list_no, record["章"] or "", record["节"] or "")].append(record)

    lines = ["# 旧题回顾大表", ""]
    empty_sections: list[tuple[str, str, str, int]] = []

    for list_no in sorted(names, key=int):
        keys = [key for key in totals if key[0] == list_no]
        list_done = sum(len(solved_by_key[key]) for key in keys)
        list_total = sum(totals[key] for key in keys)
        lines += [f"## {list_no}. {names[list_no]}", f"已做 {list_done} / 题单 {list_total}", ""]

        chapters = sorted(
            {key[1] for key in keys}, key=lambda c: chapter_order[(list_no, c)]
        )
        for chapter in chapters:
            chapter_keys = [key for key in keys if key[1] == chapter]
            chapter_done = sum(len(solved_by_key[key]) for key in chapter_keys)
            chapter_total = sum(totals[key] for key in chapter_keys)
            if chapter:
                lines += [f"### {chapter}", f"已做 {chapter_done} / 题单 {chapter_total}", ""]

            for key in sorted(chapter_keys, key=lambda k: order[k]):
                records = solved_by_key[key]
                if not records:
                    empty_sections.append((list_no, chapter, key[2], totals[key]))
                    continue
                if key[2]:
                    lines += [
                        f"#### {key[2]}",
                        f"已做 {len(records)} / 题单 {totals[key]}",
                        "",
                    ]
                lines += [COLUMNS, DIVIDER]
                for record in sorted(records, key=lambda r: r["id"]):
                    lines.append(_row(record))
                    for placement in record["亦属"]:
                        lines.append(f"| | 亦属：{' / '.join(placement)} | | | | | |")
                lines.append("")

    lines += ["## 空白节", "", "灵神题单里一道没做的节：", ""]
    for list_no, chapter, section, total in empty_sections:
        label = f"{chapter} / {section}" if section else chapter
        lines.append(f"- {list_no}. {names[list_no]} / {label} （{total} 题）")
    lines.append("")
    return "\n".join(lines)
