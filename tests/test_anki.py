from lc_review.anki import (
    escape_field,
    export_elements,
    export_pseudocode,
    export_retrospectives,
    highlight_density,
    order_key,
    weakness_rank,
)
from lc_review.elements import ElementCard, FIELDS

RECORD = {
    "id": 1004,
    "题名": "最大连续1的个数 III",
    "难度分": 1656,
    "题单": "1. 滑动窗口与双指针",
    "章": "二、不定长滑动窗口",
    "节": "§2.1 求最长",
    "归属来源": "灵神",
    "亦属": [],
    "要素卡": "滑动窗口",
    "代码": "Problems/1046_max-consecutive-ones-iii",
    "我的复盘": {"来源": "notion-medium",
                "正文": '先加入再修复\n<span color="orange">再记录</span>',
                "高亮": ["再记录"], "Day": "Day 2", "模式": "滑窗", "日期": "2026-05-25"},
    "AI题解": {"伪代码": "初始化 left\n返回 maxLen", "复杂度": "$O(n)$"},
    "已生成卡片": [],
}


def test_highlight_density_counts_per_technique():
    state = {
        "a": {"要素卡": "动态规划", "我的复盘": {"高亮": ["没懂最优子结构", "状态定义错了"]}},
        "b": {"要素卡": "滑动窗口", "我的复盘": {"高亮": ["顺序反了"]}},
        "c": {"要素卡": "滑动窗口", "我的复盘": None},
    }
    assert highlight_density(state) == {"动态规划": 2, "滑动窗口": 1}


def test_weakness_rank_puts_the_densest_technique_first():
    rank = weakness_rank({"动态规划": 2, "滑动窗口": 1})
    assert rank["动态规划"] == 0
    assert rank["滑动窗口"] == 1


def test_weakness_rank_is_empty_when_nothing_is_highlighted():
    assert weakness_rank(highlight_density({})) == {}


def test_order_key_puts_weaker_topics_first():
    rank = {"动态规划": 0, "滑动窗口": 1}
    dp = order_key("max-consecutive-ones-iii", {**RECORD, "要素卡": "动态规划"}, rank, {})
    sliding = order_key("max-consecutive-ones-iii", RECORD, rank, {})
    assert dp < sliding


def test_order_key_falls_back_to_source_order_within_a_topic():
    rank = {"滑动窗口": 0}
    entry_order = {
        "max-consecutive-ones-iii": {("1", "二、不定长滑动窗口", "§2.1 求最长"): 7}
    }
    key = order_key("max-consecutive-ones-iii", RECORD, rank, entry_order)
    assert 7 in key


def test_order_key_falls_back_to_smallest_order_when_placement_not_recorded():
    """If the record's own placement is not among the slug's entries, use the
    smallest order recorded for that slug rather than the sentinel."""
    rank = {"滑动窗口": 0}
    entry_order = {
        "max-consecutive-ones-iii": {
            ("1", "二、不定长滑动窗口", "§2.9 elsewhere"): 3,
            ("1", "二、不定长滑动窗口", "§2.1 别处"): 1,
        }
    }
    key = order_key("max-consecutive-ones-iii", RECORD, rank, entry_order)
    assert 1 in key


def test_order_key_falls_back_to_sentinel_when_slug_unknown():
    rank = {"滑动窗口": 0}
    key = order_key("unknown-slug", RECORD, rank, {})
    assert 10**6 in key


def test_within_section_order_follows_taxonomy_not_leetcode_id():
    """Several problems share one section; taxonomy order disagrees with id order.

    The exporter must follow the taxonomy's own per-problem ``order`` (the
    author already sorted easy-to-hard), not fall back to the LeetCode id.
    """
    common = {
        "题单": "1. 滑动窗口与双指针",
        "章": "二、不定长滑动窗口",
        "节": "§2.1 求最长",
        "归属来源": "灵神",
        "亦属": [],
        "要素卡": "滑动窗口",
        "难度分": 1600,
        "AI题解": {"伪代码": "", "复杂度": ""},
        "已生成卡片": [],
    }
    placement = ("1", "二、不定长滑动窗口", "§2.1 求最长")
    state = {
        "slug-high-id-early-in-taxonomy": {
            **common,
            "id": 3090,
            "题名": "A",
            "我的复盘": {"来源": "x", "正文": "a", "高亮": []},
        },
        "slug-low-id-late-in-taxonomy": {
            **common,
            "id": 3,
            "题名": "B",
            "我的复盘": {"来源": "x", "正文": "b", "高亮": []},
        },
    }
    entry_order = {
        "slug-high-id-early-in-taxonomy": {placement: 0},
        "slug-low-id-late-in-taxonomy": {placement: 1},
    }
    rank = {"滑动窗口": 0}
    rows = export_retrospectives(state, rank, entry_order).splitlines()
    ids_in_order = [row.split("\t")[1] for row in rows]
    assert ids_in_order[0].startswith("3090")
    assert ids_in_order[1].startswith("3.")


def test_escape_field_flattens_newlines_and_tabs():
    assert escape_field("a\nb\tc") == "a<br>b c"


def test_retrospective_deck_skips_problems_without_one():
    rows = export_retrospectives({"a": {**RECORD, "我的复盘": None}}, {}, {}).splitlines()
    assert rows == []


def test_retrospective_row_has_deck_front_back_and_tags():
    rows = export_retrospectives({"a": RECORD}, {"滑动窗口": 0}, {}).splitlines()
    deck, front, back, tags = rows[0].split("\t")
    assert deck == "LeetCode::我的复习::1. 滑动窗口与双指针"
    assert "1004" in front
    assert "先加入再修复<br>" in back
    assert "要素::滑动窗口" in tags


def test_retrospective_back_keeps_the_highlight_as_a_background_span():
    rows = export_retrospectives({"a": RECORD}, {"滑动窗口": 0}, {}).splitlines()
    back = rows[0].split("\t")[2]
    assert "background" in back
    assert "再记录" in back
    assert 'color="orange"' not in back


def test_pseudocode_deck_labels_the_content_as_machine_generated():
    rows = export_pseudocode({"a": RECORD}, {"滑动窗口": 0}, {}).splitlines()
    assert any("GPT 生成" in row for row in rows)


def test_pseudocode_deck_emits_a_separate_complexity_note():
    rows = export_pseudocode({"a": RECORD}, {"滑动窗口": 0}, {}).splitlines()
    assert len(rows) == 2
    assert any("$O(n)$" in row for row in rows)


ELEMENT_CARD = ElementCard(
    "滑动窗口", ("https://labuladong.online/algo/essential-technique/sliding-window-framework/",), ("滑动窗口",)
)


def test_export_elements_emits_one_note_per_technique_and_field():
    rows = export_elements((ELEMENT_CARD,), {}).splitlines()
    assert len(rows) == len(FIELDS)


def test_export_elements_deck_name_is_element_technique():
    rows = export_elements((ELEMENT_CARD,), {}).splitlines()
    decks = {row.split("\t")[0] for row in rows}
    assert decks == {"LeetCode::要素::滑动窗口"}


def test_export_elements_field_body_appears_on_the_back():
    bodies = {("滑动窗口", FIELDS[0]): "窗口的定义在此"}
    rows = export_elements((ELEMENT_CARD,), bodies).splitlines()
    backs = [row.split("\t")[2] for row in rows]
    assert any("窗口的定义在此" in back for back in backs)


def test_export_elements_cites_the_source_url():
    rows = export_elements((ELEMENT_CARD,), {}).splitlines()
    back = rows[0].split("\t")[2]
    assert "https://labuladong.online/algo/essential-technique/sliding-window-framework/" in back


def test_export_elements_missing_body_renders_an_explicit_placeholder():
    rows = export_elements((ELEMENT_CARD,), {}).splitlines()
    backs = [row.split("\t")[2] for row in rows]
    assert all("待填写" in back for back in backs)
