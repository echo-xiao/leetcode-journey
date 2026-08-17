"""Export three Anki decks as tab-separated notes.

Anki orders new cards by import order, so the row order written here is the
order echo will study in. Weakest techniques come first, then source order
within a technique.
"""

from __future__ import annotations

from lc_review.elements import FIELDS, ElementCard
from lc_review.fupan import HIGHLIGHT_STYLE, extract_highlights, to_anki_html


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
    slug: str,
    record: dict,
    rank: dict[str, int],
    entry_order: dict[str, dict[tuple[str, str, str], int]],
) -> tuple[int, str, int, int]:
    """Sort by weakness rank, then technique, then the source's own ordering.

    ``entry_order`` maps a problem's slug to every taxonomy placement it was
    seen at (a problem can be cross-listed in more than one entry). The order
    used is the entry matching this record's *assigned* placement (its own
    ``题单``/``章``/``节``); if that exact placement is not among the entries
    for this slug, fall back to the smallest order recorded for the slug, and
    only then to a large sentinel. ``record["id"]`` (the LeetCode number)
    stays as the final tiebreak only, so it never drives ordering within a
    section on its own.
    """
    topic = record["要素卡"] or ""
    list_no = record["题单"].split(".", 1)[0]
    placement = (list_no, record["章"] or "", record["节"] or "")
    placements = entry_order.get(slug, {})
    if placement in placements:
        order = placements[placement]
    elif placements:
        order = min(placements.values())
    else:
        order = 10**6
    return (
        rank.get(topic, len(rank)),
        topic,
        order,
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
    return [
        record
        for _slug, record in sorted(
            state.items(), key=lambda item: order_key(item[0], item[1], rank, entry_order)
        )
    ]


# 典型坑 is excluded from the guidance text: it is pitfalls, not guidance for
# answering an essential question, and (see FIX 7 / elements._pitfall_count)
# is derived from live state at render time, not from this frozen file.
GUIDANCE_FIELDS: tuple[str, ...] = tuple(field for field in FIELDS if field != "典型坑")
_PLACEHOLDER_BODIES = ("原文未涉及", "待填写")


def _guidance_text(card_name: str, bodies: dict[tuple[str, str], str]) -> str:
    """Collect this technique's non-placeholder field bodies as one passage.

    ``element_essentials.ESSENTIALS`` questions are technique-specific and
    were not authored with a one-to-one mapping onto ``element_bodies.BODIES``'
    six generic fields, so a card's back shows all of that technique's real
    guidance rather than guessing which single field answers which question.
    """
    parts = [
        bodies[(card_name, field)]
        for field in GUIDANCE_FIELDS
        if bodies.get((card_name, field)) not in (None, *_PLACEHOLDER_BODIES)
    ]
    return "\n\n".join(parts) if parts else "待补充"


def export_elements(
    cards: tuple[ElementCard, ...],
    essentials: dict[str, tuple[str, ...]],
    bodies: dict[tuple[str, str], str],
    rank: dict[str, int] | None = None,
) -> str:
    """One note per (technique, essential question), weakest technique first.

    Driven by ``element_essentials.ESSENTIALS`` -- each technique's own
    questions -- not the six generic ``FIELDS``, which was the framing echo
    rejected. A technique with an empty ``ESSENTIALS`` entry (an honest gap:
    its source article states no unifying checklist) emits no notes at all,
    rather than placeholder cards nobody asked for.
    """
    rank = rank or {}
    ordered_cards = sorted(cards, key=lambda card: (rank.get(card.name, len(rank)), card.name))
    rows = []
    for card in ordered_cards:
        questions = essentials.get(card.name, ())
        if not questions:
            continue
        guidance = _guidance_text(card.name, bodies)
        for question in questions:
            rows.append(
                "\t".join(
                    [
                        f"LeetCode::要素::{card.name}",
                        escape_field(f"{card.name} —— {question}"),
                        escape_field(guidance + "\n\n来源：" + "、".join(card.sources)),
                        f"要素::{card.name}",
                    ]
                )
            )
    return "\n".join(rows)


def _append_missing_highlights(body_html: str, retro: dict) -> str:
    """Append any highlight not already visible in ``正文`` to the card back.

    ``fupan.attach`` unions highlights across duplicate Notion entries but
    keeps only the longest body, so a highlight that came from a losing
    duplicate can end up recorded in ``高亮`` without ever appearing in
    ``正文``. Dropping it silently on the Anki card would make that highlight
    -- echo's own weakness signal -- invisible everywhere.

    A highlight only counts as "already visible" if it is actually rendered
    as a highlighted span in ``正文`` (via ``fupan.extract_highlights``), not
    merely a plain-text substring match -- a short highlight like "回溯" can
    otherwise appear to already be present just because a longer unrelated
    word like "回溯算法" happens to contain it.
    """
    highlighted_in_body = set(extract_highlights(retro["正文"]))
    missing = [h for h in retro.get("高亮", []) if h not in highlighted_in_body]
    if not missing:
        return body_html
    extra_spans = "\n".join(f"{HIGHLIGHT_STYLE}{h}</span>" for h in missing)
    return body_html + "\n\n补充高亮：\n" + extra_spans


def export_retrospectives(state: dict[str, dict], rank, entry_order) -> str:
    """One note per problem that echo actually wrote a retrospective for."""
    rows = []
    for record in _sorted_records(state, rank, entry_order):
        retro = record["我的复盘"]
        if not retro:
            continue
        back = _append_missing_highlights(to_anki_html(retro["正文"]), retro)
        rows.append(
            "\t".join(
                [
                    f"LeetCode::我的复习::{record['题单']}",
                    escape_field(f"{record['id']}. {record['题名']}"),
                    escape_field(back),
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
