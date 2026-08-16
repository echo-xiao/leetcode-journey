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
    cards: tuple[ElementCard, ...], links: dict[str, list[tuple[str, str]]]
) -> str:
    """Emit the skeleton. Bodies stay marked 待填写 until read from the source."""
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
            lines += [f"### {field}", "", "待填写", ""]
        lines += ["### 变体", "", "待填写", ""]
    return "\n".join(lines)
