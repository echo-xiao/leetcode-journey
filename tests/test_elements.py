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


def test_the_deck_is_driven_by_essentials_not_the_six_generic_fields():
    """FIELDS predates ESSENTIALS and is the framing echo rejected twice (see
    element_essentials.py's module docstring). It survives only as the label
    set element_bodies.BODIES is keyed on for the Anki elements deck's
    guidance text (lc_review.anki.export_elements) -- it must not drive the
    sheet or the deck's card count/order any more; ESSENTIALS does.
    """
    from lc_review.element_essentials import ESSENTIALS

    assert FIELDS == (
        "问题的定义",
        "主体 / 状态",
        "不变量",
        "停止条件 / 边界",
        "操作顺序",
        "典型坑",
    )
    # 滑动窗口's real questions are its own framework wording, not FIELDS'
    # generic six labels.
    assert ESSENTIALS["滑动窗口"] != FIELDS
    assert all(question.endswith("？") for question in ESSENTIALS["滑动窗口"])


def test_chapter_links_are_suggested_by_keyword_match():
    entries = [
        ProblemEntry("1", "滑动窗口与双指针", 1, "a", "a", None, "一、定长滑动窗口", "§1.1", 0),
        ProblemEntry("11", "链表、树与回溯", 2, "b", "b", None, "二、二叉树", "§2.1", 1),
    ]
    links = suggest_chapter_links(entries)
    assert ("1", "一、定长滑动窗口") in links["滑动窗口"]
    assert ("11", "二、二叉树") in links["二叉树"]


def test_render_emits_exactly_one_table_with_eighteen_data_rows():
    output = render_elements(CARDS, {})
    table_lines = [line for line in output.splitlines() if line.startswith("| ")]
    # line 0 is the header row, line 1 is the --- separator row, the rest
    # are data rows, one per card.
    assert len(table_lines) == 2 + len(CARDS)
    header_cells = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    assert header_cells[0] == "题型"
    assert header_cells[1] == "要素"
    assert header_cells[-2] == "典型坑"
    assert header_cells[-1] == "来源"
    separator_cells = table_lines[1].strip("|").split("|")
    assert all(set(cell.strip()) == {"-"} for cell in separator_cells)


def test_render_has_no_per_card_sections_below_the_table():
    # The old six-field layout expanded each card into its own section; the
    # new sheet is one table plus the chapter-linkage notes, nothing else.
    output = render_elements(CARDS, {})
    for field in ("问题的定义", "主体 / 状态", "不变量", "停止条件 / 边界", "操作顺序"):
        assert field not in output, f"{field} leaked into the sheet"


def test_essentials_cell_lists_this_technique_own_questions():
    # 滑动窗口's essentials come from its own checklist. The first question is
    # now "定长还是变长" (echo added it; the window kind decides the whole shape),
    # so assert on the numbering and on a question unique to this technique
    # rather than on wording that is expected to keep evolving.
    output = render_elements(CARDS, {})
    sliding_window_row = next(line for line in output.splitlines() if line.startswith("| 滑动窗口"))
    assert "1. " in sliding_window_row
    assert "窗口" in sliding_window_row
    assert "<br>" in sliding_window_row


def test_a_card_with_no_checklist_renders_an_explicit_marker():
    # No card is empty any more (echo had the three index-page cards filled
    # in), so the marker is exercised with an explicit empty mapping instead of
    # relying on a card that used to be blank.
    from lc_review.elements import _essentials_cell

    assert "原文无明确清单" in _essentials_cell(())


def test_no_cell_contains_a_raw_newline():
    output = render_elements(CARDS, {})
    table_lines = [line for line in output.splitlines() if line.startswith("| ")]
    assert len(table_lines) == 2 + len(CARDS)


def test_pitfall_column_shows_a_count_derived_from_state_not_a_frozen_body():
    state = {
        "a": {"要素卡": CARDS[0].name, "我的复盘": {"高亮": ["坑一"]}},
        "b": {"要素卡": CARDS[0].name, "我的复盘": {"高亮": ["坑二"]}},
        "c": {"要素卡": CARDS[0].name, "我的复盘": {"高亮": ["坑三"]}},
        "d": {"要素卡": "别的技巧", "我的复盘": {"高亮": ["不该被计入"]}},
    }
    output = render_elements(CARDS, {}, state)
    assert "坑一" not in output
    assert "3 条" in output


def test_pitfall_column_shows_a_dash_when_there_are_no_pitfalls():
    output = render_elements(CARDS, {}, {})
    table_lines = [line for line in output.splitlines() if line.startswith("| ")]
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        assert cells[-2] == "—"


def test_pitfall_count_ignores_records_with_no_actual_highlights():
    state = {"a": {"要素卡": CARDS[0].name, "我的复盘": {"高亮": []}}}
    output = render_elements(CARDS, {}, state)
    row = next(line for line in output.splitlines() if line.startswith(f"| {CARDS[0].name}"))
    assert "—" in row


def test_pitfall_count_reflects_a_freshly_added_retrospective_highlight():
    """The count must never desynchronise from state: adding a highlight
    changes the count on the very next render, with nothing to keep in sync
    by hand."""
    state = {"a": {"要素卡": CARDS[0].name, "我的复盘": {"高亮": ["新增的坑"]}}}
    output = render_elements(CARDS, {}, state)
    row = next(line for line in output.splitlines() if line.startswith(f"| {CARDS[0].name}"))
    assert "1 条" in row


def test_render_keeps_exactly_one_chapter_linkage_section_below_the_table():
    entries = [ProblemEntry("11", "链表、树与回溯", 2, "b", "b", None, "二、二叉树", "§2.1", 0)]
    output = render_elements(CARDS, suggest_chapter_links(entries))
    assert output.count("我方判断") == 1
    assert "二叉树" in output.split("我方判断")[1]


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


def test_link_state_to_cards_records_provenance_of_the_judgment():
    entries = [ProblemEntry("1", "滑动窗口与双指针", 1, "a", "a", None, "一、定长滑动窗口", "§1.1", 0)]
    state = {
        "matched": {"题单": "1. 滑动窗口与双指针", "章": "一、定长滑动窗口", "要素卡": None},
        "unmatched": {"题单": "1. 滑动窗口与双指针", "章": "没有这个章", "要素卡": None},
    }
    link_state_to_cards(state, entries)
    assert state["matched"]["要素卡来源"] == "关键词匹配"
    assert state["unmatched"]["要素卡来源"] is None
