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


def render_elements(
    cards: tuple[ElementCard, ...],
    links: dict[str, list[tuple[str, str]]],
    bodies: dict[tuple[str, str], str] | None = None,
) -> str:
    """Emit the sheet. A field with no entry in ``bodies`` stays marked 待填写
    rather than being invented; a field whose source genuinely does not cover
    it should have its body set to the literal string 原文未涉及, not be left
    out of ``bodies``.
    """
    bodies = bodies or {}
    lines = ["# 要素表", "", "每张卡对应 labuladong 的一篇框架文。正文从原文抽取，不自撰。", ""]
    for index, card in enumerate(cards, start=1):
        lines += [f"## {index}. {card.name}", ""]
        lines.append("来源：" + "、".join(f"<{url}>" for url in card.sources))
        covered = links.get(card.name, [])
        lines.append(
            "覆盖章（我方判断，待 echo 复核）："
            + ("；".join(f"{no} / {chapter}" for no, chapter in covered) if covered else "无")
        )
        lines.append("")
        for field in FIELDS:
            body = bodies.get((card.name, field), "待填写")
            lines += [f"### {field}", "", body, ""]
        lines += ["### 变体", "", "待填写", ""]
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


def link_state_to_cards(state: dict[str, dict], entries: list[ProblemEntry]) -> tuple[int, int]:
    """Fill in each state record's 要素卡 from its (题单, 章), in place.

    A record whose chapter matches no card's keywords keeps 要素卡 as None.
    Returns (linked_count, unlinked_count).
    """
    owner = chapter_to_cards(entries)
    linked = 0
    unlinked = 0
    for record in state.values():
        list_no = record["题单"].split(".", 1)[0].strip()
        chapter = record["章"]
        card_name = owner.get((list_no, chapter)) if chapter else None
        record["要素卡"] = card_name
        if card_name:
            linked += 1
        else:
            unlinked += 1
    return linked, unlinked
