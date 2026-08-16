from lc_review.elements import CARDS, FIELDS, render_elements, suggest_chapter_links
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
