"""Render the grouped progress table."""

from __future__ import annotations

from collections import defaultdict

from lc_review.classify import ORIGIN_CROSS, ORIGIN_LINGSHEN, ORIGIN_OUTSIDE
from lc_review.lingshen import ProblemEntry

MARKERS = {ORIGIN_CROSS: "[跨]", ORIGIN_OUTSIDE: "[外]"}
COLUMNS = "| 题号 | 题名 | 难度分 | 要素卡 | 代码 | 我的复盘 | 已出卡 |"
DIVIDER = "|---|---|---|---|---|---|---|"

# Only these origins actually come from this section of the taxonomy. A
# ORIGIN_OUTSIDE ([外]) record was placed here by our own tag-similarity
# judgment, not by 灵神, and must not inflate the "已做" numerator -- see
# FIX 4 in the review that produced this module.
IN_TAXONOMY_ORIGINS = {ORIGIN_LINGSHEN, ORIGIN_CROSS}


def _row(record: dict) -> str:
    marker = MARKERS.get(record["归属来源"], "")
    retro = "有" if record["我的复盘"] else "缺"
    cards = "/".join(record["已生成卡片"]) or "—"
    rating = record["难度分"] if record["难度分"] is not None else "—"
    return (
        f"| {record['id']} | {marker}{record['题名']} | {rating} | "
        f"{record['要素卡'] or '—'} | `{record['代码']}` | {retro} | {cards} |"
    )


def _pointer_row(record: dict) -> str:
    """A grey pointer row shown in a SECONDARY section, referencing the primary.

    Per spec §3.3: a cross-listed problem's other sections show a pointer
    back to where it actually lives, rather than duplicating (or, as the
    prior bug did, never showing) the problem there.
    """
    primary = " / ".join(part for part in (record["题单"], record["章"], record["节"]) if part)
    return f"| {record['id']} | 亦属：{record['题名']}（主：{primary}） | | | | | |"


def _heading(done: int, total: int, outside: int) -> str:
    line = f"已做 {done} / 题单 {total}"
    if outside:
        line += f"（另有 {outside} 题为 [外] 归入）"
    return line


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
    in_taxonomy_by_key: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for record in state.values():
        list_no = record["题单"].split(".", 1)[0]
        key = (list_no, record["章"] or "", record["节"] or "")
        solved_by_key[key].append(record)
        if record["归属来源"] in IN_TAXONOMY_ORIGINS:
            in_taxonomy_by_key[key].append(record)

    # A secondary placement (亦属) gets a pointer row in the OTHER section it
    # points at, not duplicated under the primary row where the prior bug put
    # it. Also used below so a section with only pointer rows (no primary
    # record of its own) is not falsely reported as empty.
    pointers_by_key: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for record in state.values():
        for placement in record["亦属"]:
            pointers_by_key[tuple(placement)].append(record)

    lines = ["# 旧题回顾大表", ""]
    empty_sections: list[tuple[str, str, str, int]] = []

    for list_no in sorted(names, key=int):
        keys = [key for key in totals if key[0] == list_no]
        list_done = sum(len(in_taxonomy_by_key[key]) for key in keys)
        list_outside = sum(len(solved_by_key[key]) - len(in_taxonomy_by_key[key]) for key in keys)
        list_total = sum(totals[key] for key in keys)
        lines += [
            f"## {list_no}. {names[list_no]}",
            _heading(list_done, list_total, list_outside),
            "",
        ]

        chapters = sorted(
            {key[1] for key in keys}, key=lambda c: chapter_order[(list_no, c)]
        )
        for chapter in chapters:
            chapter_keys = [key for key in keys if key[1] == chapter]
            chapter_done = sum(len(in_taxonomy_by_key[key]) for key in chapter_keys)
            chapter_outside = sum(
                len(solved_by_key[key]) - len(in_taxonomy_by_key[key]) for key in chapter_keys
            )
            chapter_total = sum(totals[key] for key in chapter_keys)
            if chapter:
                lines += [
                    f"### {chapter}",
                    _heading(chapter_done, chapter_total, chapter_outside),
                    "",
                ]

            for key in sorted(chapter_keys, key=lambda k: order[k]):
                records = solved_by_key[key]
                pointers = pointers_by_key.get(key, [])
                if not records and not pointers:
                    empty_sections.append((list_no, chapter, key[2], totals[key]))
                    continue
                section_done = len(in_taxonomy_by_key[key])
                section_outside = len(records) - section_done
                if key[2]:
                    lines += [
                        f"#### {key[2]}",
                        _heading(section_done, totals[key], section_outside),
                        "",
                    ]
                lines += [COLUMNS, DIVIDER]
                for record in sorted(records, key=lambda r: r["id"]):
                    lines.append(_row(record))
                for pointer in sorted(pointers, key=lambda r: r["id"]):
                    lines.append(_pointer_row(pointer))
                lines.append("")

    lines += ["## 空白节", "", "灵神题单里一道没做的节：", ""]
    for list_no, chapter, section, total in empty_sections:
        label = f"{chapter} / {section}" if section else chapter
        lines.append(f"- {list_no}. {names[list_no]} / {label} （{total} 题）")
    lines.append("")
    return "\n".join(lines)
