"""Export three Anki decks as tab-separated notes.

Anki orders new cards by import order, so the row order written here is the
order echo will study in. Weakest techniques come first, then source order
within a technique.
"""

from __future__ import annotations

from lc_review.elements import FIELDS, ElementCard
from lc_review.fupan import to_anki_html


def highlight_density(state: dict[str, dict]) -> dict[str, int]:
    """Count how many orange highlights each technique accumulated.

    echo marks what she got wrong in orange while writing a retrospective, so a
    technique with many highlights is a technique she keeps tripping on. This is
    recomputed from the retrospectives on every run — there is no separate
    weakness list to maintain and no frequency baked into this file.
    """
    density: dict[str, int] = {}
    for record in state.values():
        retro = record.get("我的复盘")
        topic = record.get("要素卡")
        if not retro or not topic:
            continue
        density[topic] = density.get(topic, 0) + len(retro.get("高亮", []))
    return density


def weakness_rank(density: dict[str, int]) -> dict[str, int]:
    """Turn highlight counts into a sort rank, densest technique first."""
    ordered = sorted(density.items(), key=lambda pair: (-pair[1], pair[0]))
    return {name: index for index, (name, _count) in enumerate(ordered)}


def escape_field(text: str) -> str:
    """Flatten a field so one note stays on one line."""
    return text.replace("\r\n", "\n").replace("\n", "<br>").replace("\t", " ")


def order_key(
    record: dict,
    rank: dict[str, int],
    entry_order: dict[tuple[str, str, str], int],
) -> tuple[int, str, int, int]:
    """Sort by weakness rank, then technique, then the source's own ordering."""
    topic = record["要素卡"] or ""
    list_no = record["题单"].split(".", 1)[0]
    key = (list_no, record["章"] or "", record["节"] or "")
    return (
        rank.get(topic, len(rank)),
        topic,
        entry_order.get(key, 10**6),
        record["id"],
    )


def _tags(record: dict) -> str:
    list_no = record["题单"].split(".", 1)[0]
    rating = record["难度分"]
    band = f"{rating // 100 * 100}" if isinstance(rating, int) else "未评分"
    return " ".join(
        [
            f"灵神::{record['题单']}::{record['章'] or '无章'}".replace(" ", "_"),
            f"要素::{record['要素卡'] or '未挂靠'}",
            f"难度::{band}",
            f"来源::{record['归属来源']}",
            f"题单编号::{list_no}",
        ]
    )


def _sorted_records(state: dict[str, dict], rank, entry_order) -> list[dict]:
    return sorted(state.values(), key=lambda record: order_key(record, rank, entry_order))


def export_elements(
    cards: tuple[ElementCard, ...], bodies: dict[tuple[str, str], str]
) -> str:
    """One note per (technique, field). Bodies come from the elements sheet."""
    rows = []
    for card in cards:
        for field in FIELDS:
            body = bodies.get((card.name, field), "待填写")
            rows.append(
                "\t".join(
                    [
                        f"LeetCode::要素::{card.name}",
                        escape_field(f"{card.name} —— {field}是什么？"),
                        escape_field(body + "\n\n来源：" + "、".join(card.sources)),
                        f"要素::{card.name}",
                    ]
                )
            )
    return "\n".join(rows)


def export_retrospectives(state: dict[str, dict], rank, entry_order) -> str:
    """One note per problem that echo actually wrote a retrospective for."""
    rows = []
    for record in _sorted_records(state, rank, entry_order):
        retro = record["我的复盘"]
        if not retro:
            continue
        rows.append(
            "\t".join(
                [
                    f"LeetCode::我的复习::{record['题单']}",
                    escape_field(f"{record['id']}. {record['题名']}"),
                    escape_field(to_anki_html(retro["正文"])),
                    _tags(record),
                ]
            )
        )
    return "\n".join(rows)


def export_pseudocode(state: dict[str, dict], rank, entry_order) -> str:
    """Two notes per problem: pseudocode, and complexity on its own card."""
    rows = []
    for record in _sorted_records(state, rank, entry_order):
        ai = record["AI题解"]
        front = f"{record['id']}. {record['题名']}"
        if ai["伪代码"]:
            rows.append(
                "\t".join(
                    [
                        "LeetCode::伪代码",
                        escape_field(front + " —— 伪代码？"),
                        escape_field(ai["伪代码"] + "\n\n（GPT 生成，非本人复盘）"),
                        _tags(record),
                    ]
                )
            )
        if ai["复杂度"]:
            rows.append(
                "\t".join(
                    [
                        "LeetCode::伪代码",
                        escape_field(front + " —— 时间/空间复杂度？"),
                        escape_field(ai["复杂度"] + "\n\n（GPT 生成，非本人复盘）"),
                        _tags(record),
                    ]
                )
            )
    return "\n".join(rows)
