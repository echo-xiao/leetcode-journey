from lc_review.lingshen import ProblemEntry
from lc_review.table import render_table


def entry(list_no, list_name, chapter, section, pid, slug, order):
    return ProblemEntry(list_no, list_name, pid, slug, slug, None, chapter, section, order)


ENTRIES = [
    entry("7", "动态规划", "一、入门 DP", "§1.1 爬楼梯", 70, "climbing-stairs", 0),
    entry("7", "动态规划", "一、入门 DP", "§1.1 爬楼梯", 746, "min-cost", 1),
    entry("7", "动态规划", "二、网格图 DP", "§2.1 基础", 64, "min-path-sum", 2),
]

STATE = {
    "min-cost": {
        "id": 746,
        "题名": "使用最小花费爬楼梯",
        "难度分": 1300,
        "题单": "7. 动态规划",
        "章": "一、入门 DP",
        "节": "§1.1 爬楼梯",
        "归属来源": "灵神",
        "亦属": [],
        "要素卡": "动态规划",
        "代码": "Problems/747_min-cost",
        "我的复盘": {"来源": "notion-easy", "正文": "x"},
        "AI题解": {"伪代码": "", "复杂度": ""},
        "已生成卡片": ["要素"],
    }
}


def test_headings_are_verbatim_from_the_source():
    output = render_table(STATE, ENTRIES)
    assert "## 7. 动态规划" in output
    assert "### 一、入门 DP" in output
    assert "#### §1.1 爬楼梯" in output


def test_section_heading_carries_the_full_denominator():
    output = render_table(STATE, ENTRIES)
    assert "已做 1 / 题单 2" in output


def test_only_solved_problems_become_rows():
    output = render_table(STATE, ENTRIES)
    assert "min-cost" in output
    assert "climbing-stairs" not in output


def test_empty_sections_go_to_a_trailing_list_not_inline():
    output = render_table(STATE, ENTRIES)
    body, _, empty = output.partition("## 空白节")
    assert "§2.1 基础" not in body
    assert "§2.1 基础" in empty


def test_cross_and_outside_placements_are_marked():
    state = {
        "container": {**STATE["min-cost"], "id": 11, "题名": "盛最多水的容器",
                      "归属来源": "跨-我选主节", "亦属": [["1", "一", "§1.1"]]},
    }
    entries = ENTRIES + [entry("7", "动态规划", "一、入门 DP", "§1.1 爬楼梯", 11, "container", 3)]
    output = render_table(state, entries)
    assert "[跨]" in output


def test_missing_retrospective_is_shown_as_missing():
    state = {"min-cost": {**STATE["min-cost"], "我的复盘": None}}
    output = render_table(state, ENTRIES)
    assert "缺" in output


def test_chapters_render_in_source_order_not_alphabetical():
    """A chapter that appears later in the source post must render after an
    earlier one, even when sorting the chapter names as text would reverse
    that order."""
    entries = [
        entry("7", "动态规划", "二、网格图 DP", "§2.1 基础", 64, "min-path-sum", 0),
        entry("7", "动态规划", "一、入门 DP", "§1.1 爬楼梯", 70, "climbing-stairs", 1),
    ]
    state = {
        "min-path-sum": {**STATE["min-cost"], "id": 64, "题名": "最小路径和",
                          "章": "二、网格图 DP", "节": "§2.1 基础"},
        "climbing-stairs": {**STATE["min-cost"], "id": 70, "题名": "爬楼梯",
                             "章": "一、入门 DP", "节": "§1.1 爬楼梯"},
    }
    output = render_table(state, entries)
    assert output.index("### 二、网格图 DP") < output.index("### 一、入门 DP")
