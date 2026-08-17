"""The eighteen technique cards, keyed to labuladong's framework articles."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from lc_review.lingshen import ProblemEntry

BASE = "https://labuladong.online/algo/"

# Six fields: the three echo named (definition, subject, stopping condition)
# plus three themes that recur in what she highlights in her own retrospectives
# (imprecise invariants, boundary/initialisation, operation ordering).
FIELDS: tuple[str, ...] = (
    "问题的定义",
    "主体 / 状态",
    "不变量",
    "停止条件 / 边界",
    "操作顺序",
    "典型坑",
)


@dataclass(frozen=True)
class ElementCard:
    """One technique, its source articles, and the words that identify it."""

    name: str
    sources: tuple[str, ...]
    keywords: tuple[str, ...]


# Every URL below was read from labuladong's own table of contents
# (https://raw.githubusercontent.com/labuladong/fucking-algorithm/master/README.md)
# and confirmed to return HTTP 200, not guessed from URL-slug conventions.
CARDS: tuple[ElementCard, ...] = (
    ElementCard("链表双指针", (BASE + "essential-technique/linked-list-skills-summary/",), ("链表",)),
    ElementCard("数组双指针", (BASE + "essential-technique/array-two-pointers-summary/",), ("双指针",)),
    ElementCard("滑动窗口", (BASE + "essential-technique/sliding-window-framework/",), ("滑动窗口",)),
    ElementCard("二分搜索", (BASE + "essential-technique/binary-search-framework/",), ("二分",)),
    ElementCard("单调栈", (BASE + "data-structure/monotonic-stack/",), ("单调栈", "单调队列")),
    ElementCard("前缀和与差分", (BASE + "data-structure/prefix-sum/", BASE + "data-structure/diff-array/"), ("前缀和", "差分")),
    ElementCard("栈与队列", (BASE + "problem-set/stack/", BASE + "problem-set/queue/"), ("栈", "队列")),
    ElementCard("堆（优先级队列）", (BASE + "problem-set/binary-heap/",), ("堆",)),
    ElementCard("二叉树", (BASE + "essential-technique/binary-tree-summary/",), ("二叉树", "树")),
    ElementCard("递归思维", (BASE + "essential-technique/understand-recursion/",), ("递归",)),
    ElementCard(
        "回溯",
        (BASE + "essential-technique/backtrack-framework/", BASE + "essential-technique/permutation-combination-subset-all-in-one/"),
        ("回溯", "排列", "组合", "子集"),
    ),
    ElementCard("BFS", (BASE + "essential-technique/bfs-framework/",), ("BFS", "网格图")),
    ElementCard(
        "图论",
        (
            BASE + "data-structure-basic/graph-traverse-basic/",
            BASE + "data-structure/topological-sort/",
            BASE + "data-structure-basic/graph-shortest-path/",
        ),
        ("图", "拓扑", "最短路"),
    ),
    ElementCard("并查集", (BASE + "data-structure/union-find/",), ("并查集",)),
    ElementCard("动态规划", (BASE + "essential-technique/dynamic-programming-framework/",), ("DP", "动态规划", "背包")),
    ElementCard("贪心", (BASE + "essential-technique/greedy/",), ("贪心",)),
    ElementCard("分治", (BASE + "essential-technique/divide-and-conquer/",), ("分治",)),
    ElementCard("数学技巧", (BASE + "essential-technique/math-techniques-summary/",), ("数学", "位运算")),
)


def suggest_chapter_links(entries: list[ProblemEntry]) -> dict[str, list[tuple[str, str]]]:
    """Propose which taxonomy chapters each card covers, by keyword match.

    This is a suggestion for echo to review, not a claim by either author.
    A chapter matching no keyword is simply left unlinked.
    """
    chapters = sorted({(entry.list_no, entry.chapter) for entry in entries if entry.chapter})
    links: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for card in CARDS:
        for list_no, chapter in chapters:
            if any(keyword in chapter for keyword in card.keywords):
                links[card.name].append((list_no, chapter))
    return dict(links)


def _pitfall_count(state: dict[str, dict], card_name: str) -> int:
    """Count problems linked to this card with an actual highlighted pitfall.

    Derived from ``review_state.json`` at render time -- never from a frozen
    copy of echo's highlight text -- so a new retrospective is reflected the
    next time this renders, with no separate frequency to keep in sync. See
    ``lc_review.element_bodies``'s module docstring: 不在代码里写死任何踩坑频次.
    """
    return sum(
        1
        for record in state.values()
        if record.get("要素卡") == card_name
        and record.get("我的复盘")
        and record["我的复盘"].get("高亮")
    )


def _pitfall_cell(state: dict[str, dict], card_name: str) -> str:
    count = _pitfall_count(state, card_name)
    return f"{count} 条" if count else "—"


def _source_links(urls: tuple[str, ...]) -> str:
    if len(urls) == 1:
        return f"[原文]({urls[0]})"
    return "、".join(f"[原文{i}]({url})" for i, url in enumerate(urls, start=1))


NO_CHECKLIST = "原文无明确清单"


def _essentials_cell(items: tuple[str, ...]) -> str:
    """Render one technique's 要素 as a numbered, ``<br>``-joined cell.

    An empty tuple means the source article genuinely states no unifying
    checklist (see ``lc_review.element_essentials`` for which cards these
    are and why); that must render as an explicit marker, never a blank
    cell that could be mistaken for a forgotten entry.
    """
    if not items:
        return NO_CHECKLIST
    numbered = [f"{i}. {item}" for i, item in enumerate(items, start=1)]
    return "<br>".join(numbered).replace("|", "\\|")


def render_elements(
    cards: tuple[ElementCard, ...],
    links: dict[str, list[tuple[str, str]]],
    state: dict[str, dict] | None = None,
) -> str:
    """Emit the sheet as a single markdown table, one row per technique.

    Each technique gets its own 要素 -- the small set of questions you must
    answer to write that kind of code -- from
    ``lc_review.element_essentials.ESSENTIALS``, not the six generic fields
    in ``FIELDS`` (those still back the Anki elements deck's guidance text
    via ``element_bodies.BODIES`` and ``lc_review.anki.export_elements``, but
    no longer drive this sheet). The 典型坑 column shows a count computed
    live from ``state`` (``review_state.json``'s ``我的复盘.高亮``), never
    from a frozen copy; the full pitfall text stays in the Anki deck.
    """
    from lc_review.element_essentials import ESSENTIALS

    state = state or {}
    header = ["题型", "要素", "典型坑", "来源"]
    lines = [
        "# 要素表",
        "",
        "每行对应一种题型；「要素」是写这类代码前必须回答的问题，逐条列出，"
        "来自原文自己的框架或从原文的坚持中提炼（见 lc_review/element_essentials.py "
        "里每条的出处说明）。典型坑列显示 echo 复盘中标出的问题数（实时从 "
        "review_state.json 统计，不是写死的），完整坑点见 Anki 要素卡。",
        "",
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * len(header)) + " |",
    ]
    for card in cards:
        row = [
            card.name,
            _essentials_cell(ESSENTIALS.get(card.name, ())),
            _pitfall_cell(state, card.name),
            _source_links(card.sources),
        ]
        lines.append("| " + " | ".join(row) + " |")
    lines += ["", "## 章节对应（我方判断，待 echo 复核）", ""]
    any_links = False
    for card in cards:
        covered = links.get(card.name, [])
        if covered:
            any_links = True
            lines.append(f"- {card.name}：" + "；".join(f"{no} / {chapter}" for no, chapter in covered))
    if not any_links:
        lines.append("（无匹配）")
    return "\n".join(lines)


def chapter_to_cards(entries: list[ProblemEntry]) -> dict[tuple[str, str], str]:
    """Invert ``suggest_chapter_links``: (题单编号, 章) -> the one card that owns it.

    Several cards' keyword lists can both match the same chapter (e.g. both
    单调栈 and 栈与队列 match a chapter named "一、单调栈"). Ties are broken by
    ``CARDS`` order, which lists the more specific technique first, so the
    result is a single card name rather than a list — this keeps the mapping
    compatible with review_state.json's 要素卡 field, which anki.py already
    treats as a plain string.
    """
    links = suggest_chapter_links(entries)
    owner: dict[tuple[str, str], str] = {}
    for card in CARDS:
        for chapter_key in links.get(card.name, []):
            owner.setdefault(chapter_key, card.name)
    return owner


CARD_LINK_SOURCE = "关键词匹配"


def link_state_to_cards(state: dict[str, dict], entries: list[ProblemEntry]) -> tuple[int, int]:
    """Fill in each state record's 要素卡 from its (题单, 章), in place.

    A record whose chapter matches no card's keywords keeps 要素卡 as None.
    Also records ``要素卡来源`` -- like ``归属来源`` and ``题号来源``, this is
    our judgment rather than a fact from the taxonomy, and it deserves the
    same provenance marker they already get. Null exactly when 要素卡 is
    null. Returns (linked_count, unlinked_count).
    """
    owner = chapter_to_cards(entries)
    linked = 0
    unlinked = 0
    for record in state.values():
        list_no = record["题单"].split(".", 1)[0].strip()
        chapter = record["章"]
        card_name = owner.get((list_no, chapter)) if chapter else None
        record["要素卡"] = card_name
        record["要素卡来源"] = CARD_LINK_SOURCE if card_name else None
        if card_name:
            linked += 1
        else:
            unlinked += 1
    return linked, unlinked
