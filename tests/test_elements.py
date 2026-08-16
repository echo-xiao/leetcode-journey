from lc_review.elements import (
    CARDS,
    FIELDS,
    chapter_to_cards,
    link_state_to_cards,
    render_elements,
    suggest_chapter_links,
)
from lc_review.lingshen import ProblemEntry


def test_there_are_eighteen_cards_with_unique_names():
    assert len(CARDS) == 18
    assert len({card.name for card in CARDS}) == 18


def test_every_card_cites_at_least_one_source():
    for card in CARDS:
        assert card.sources, f"{card.name} has no source"
        for url in card.sources:
            assert url.startswith("https://labuladong.online/algo/")


def test_the_six_fields_cover_echos_example_plus_her_top_weaknesses():
    assert FIELDS == (
        "问题的定义",
        "主体 / 状态",
        "不变量",
        "停止条件 / 边界",
        "操作顺序",
        "典型坑",
    )


def test_chapter_links_are_suggested_by_keyword_match():
    entries = [
        ProblemEntry("1", "滑动窗口与双指针", 1, "a", "a", None, "一、定长滑动窗口", "§1.1", 0),
        ProblemEntry("11", "链表、树与回溯", 2, "b", "b", None, "二、二叉树", "§2.1", 1),
    ]
    links = suggest_chapter_links(entries)
    assert ("1", "一、定长滑动窗口") in links["滑动窗口"]
    assert ("11", "二、二叉树") in links["二叉树"]


def test_render_marks_bodies_as_unwritten_rather_than_inventing_them():
    entries = [ProblemEntry("11", "链表、树与回溯", 2, "b", "b", None, "二、二叉树", "§2.1", 0)]
    output = render_elements(CARDS, suggest_chapter_links(entries))
    assert "待填写" in output
    assert all(field in output for field in FIELDS)


def test_render_uses_a_supplied_body_but_still_marks_missing_fields_unwritten():
    # A card can have a real body for one field and nothing for another;
    # the rendered sheet must show the real text for the first and fall
    # back to the explicit 待填写 marker for the second, never a blank.
    card = CARDS[0]
    bodies = {(card.name, FIELDS[0]): "真实内容，来自原文。"}
    output = render_elements(CARDS, {}, bodies)
    assert "真实内容，来自原文。" in output
    assert "待填写" in output


def test_chapter_to_cards_breaks_ties_by_cards_order():
    # "一、单调栈" matches both 单调栈 and 栈与队列's keywords; 单调栈 is the
    # more specific technique and comes first in CARDS, so it should win
    # rather than the mapping silently picking an arbitrary card.
    entries = [ProblemEntry("3", "单调栈", 1, "a", "a", None, "一、单调栈", None, 0)]
    owner = chapter_to_cards(entries)
    assert owner[("3", "一、单调栈")] == "单调栈"


def test_link_state_to_cards_fills_in_matched_records_and_leaves_others_null():
    entries = [ProblemEntry("1", "滑动窗口与双指针", 1, "a", "a", None, "一、定长滑动窗口", "§1.1", 0)]
    state = {
        "matched": {"题单": "1. 滑动窗口与双指针", "章": "一、定长滑动窗口", "要素卡": None},
        "unmatched": {"题单": "1. 滑动窗口与双指针", "章": "没有这个章", "要素卡": None},
        "no_chapter": {"题单": "1. 滑动窗口与双指针", "章": None, "要素卡": None},
    }
    linked, unlinked = link_state_to_cards(state, entries)
    assert linked == 1
    assert unlinked == 2
    assert state["matched"]["要素卡"] == "滑动窗口"
    assert state["unmatched"]["要素卡"] is None
    assert state["no_chapter"]["要素卡"] is None
