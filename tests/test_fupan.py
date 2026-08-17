from lc_review.fupan import (
    Retrospective,
    attach,
    parse_easy_page,
    parse_medium_page,
    to_anki_html,
)


def test_easy_page_finds_every_entry(fupan_easy_sample):
    entries = parse_easy_page(fupan_easy_sample)
    assert [e.problem_id for e in entries] == [1385, 1826, 2108]


def test_easy_page_skips_the_job_notes_preamble(fupan_easy_sample):
    entries = parse_easy_page(fupan_easy_sample)
    assert all("coffee chat" not in e.body for e in entries)


def test_easy_page_captures_the_body(fupan_easy_sample):
    entries = parse_easy_page(fupan_easy_sample)
    assert "暴力解法" in entries[0].body
    assert entries[0].source == "notion-easy"


def test_medium_page_finds_entries_and_ids(fupan_medium_sample):
    entries = parse_medium_page(fupan_medium_sample)
    assert [e.problem_id for e in entries] == [1456, 2379, 904]


def test_medium_page_carries_day_topic_and_date(fupan_medium_sample):
    entries = parse_medium_page(fupan_medium_sample)
    assert entries[0].day == "Day 1"
    assert entries[0].topic == "W1 滑动窗口 | 定长滑动窗口 （同向）"
    assert entries[0].date == "2026-05-24"
    assert entries[2].day == "Day 2"


def test_attach_matches_by_problem_id():
    state = {"max-consecutive-ones-iii": {"id": 1004, "我的复盘": None}}
    retro = Retrospective(1004, "窗口不合法时移动left", "notion-medium", "Day 3", "滑窗", "2026-05-26")
    state, orphans = attach(state, [retro])
    assert state["max-consecutive-ones-iii"]["我的复盘"]["正文"] == "窗口不合法时移动left"
    assert state["max-consecutive-ones-iii"]["我的复盘"]["来源"] == "notion-medium"
    assert orphans == []


def test_attach_reports_retrospectives_with_no_local_code():
    state = {"max-consecutive-ones-iii": {"id": 1004, "我的复盘": None}}
    orphan = Retrospective(9999, "some note", "notion-easy", None, None, None)
    _, orphans = attach(state, [orphan])
    assert [o.problem_id for o in orphans] == [9999]


def test_attach_keeps_the_longer_body_when_a_problem_appears_twice():
    state = {"slug": {"id": 1, "我的复盘": None}}
    short = Retrospective(1, "short", "notion-easy", None, None, None, ())
    long = Retrospective(1, "a much longer retrospective body", "notion-medium", None, None, None, ())
    state, _ = attach(state, [short, long])
    assert state["slug"]["我的复盘"]["正文"] == "a much longer retrospective body"


def test_highlights_survive_parsing():
    text = '1385、find the distance：<span color="orange">目标设定错了</span>要用二分查找。'
    entry = parse_easy_page(text)[0]
    assert entry.highlights == ("目标设定错了",)
    assert "目标设定错了" in entry.body


def test_highlights_handle_backslash_escaped_quotes():
    text = '1385、find the distance：<span color=\\"orange\\">目标设定错了</span>要用二分。'
    assert parse_easy_page(text)[0].highlights == ("目标设定错了",)


def test_to_anki_html_turns_colour_spans_into_a_background():
    html = to_anki_html('前面<span color="orange">这里错了</span>后面')
    assert "background" in html
    assert "这里错了" in html
    assert "color=" not in html


def test_to_anki_html_leaves_unhighlighted_text_alone():
    assert to_anki_html("没有高亮") == "没有高亮"


def test_attach_stores_highlights_alongside_the_body():
    state = {"slug": {"id": 1, "我的复盘": None}}
    retro = Retrospective(1, "body", "notion-easy", None, None, None, ("加入和修复的顺序反了",))
    state, _ = attach(state, [retro])
    assert state["slug"]["我的复盘"]["高亮"] == ["加入和修复的顺序反了"]


def test_easy_page_splits_br_joined_entries_on_one_physical_line():
    text = "1385、find the distance value：first body.<br>1826、faulty sensor：second body."
    entries = parse_easy_page(text)
    assert [e.problem_id for e in entries] == [1385, 1826]
    assert entries[0].body == "first body."
    assert entries[1].body == "second body."


def test_easy_page_handles_span_wrapped_entry_number():
    text = '<span color="orange">1385、find the distance value：</span>这个题目只能用暴力解法吗？'
    entry = parse_easy_page(text)[0]
    assert entry.problem_id == 1385
    assert entry.body.startswith("这个题目")
    assert entry.highlights == ()


def test_medium_page_splits_br_joined_entries_on_one_physical_line():
    text = "1、LC 15 三数之和：固定一个值，然后双指针。<br>2、LC 16 最接近的三数之和：另一道题。"
    entries = parse_medium_page(text)
    assert [e.problem_id for e in entries] == [15, 16]
    assert entries[0].body == "固定一个值，然后双指针。"
    assert entries[1].body == "另一道题。"


def test_medium_page_handles_span_wrapped_entry_number():
    text = '<span color="orange">2、LC 904 水果成篮：</span>难点在于while条件怎么写。'
    entry = parse_medium_page(text)[0]
    assert entry.problem_id == 904
    assert entry.body.startswith("难点在于")
    assert entry.highlights == ()


def test_easy_page_captures_highlight_when_span_closes_inside_the_body():
    text = (
        '<span color="orange">589、N-ary tree preorder traversal：'
        "多叉树的遍历，跟二叉树的遍历，两个逻辑整体的区别在于</span>，"
        "多叉树的遍历是一种..."
    )
    entry = parse_easy_page(text)[0]
    assert entry.problem_id == 589
    assert entry.highlights == ("多叉树的遍历，跟二叉树的遍历，两个逻辑整体的区别在于",)
    assert "589" not in entry.highlights[0]
    assert "preorder" not in entry.highlights[0]
    assert entry.body.count("<span") == entry.body.count("</span>")
    html = to_anki_html(entry.body)
    assert "background" in html
    assert "color=" not in html
    assert "多叉树的遍历，跟二叉树的遍历，两个逻辑整体的区别在于" in html


def test_attach_unions_highlights_across_duplicate_entries():
    state = {"slug": {"id": 1, "我的复盘": None}}
    short = Retrospective(1, "short", "notion-easy", None, None, None, ("highlight from short",))
    long = Retrospective(
        1, "a much longer retrospective body", "notion-medium", None, None, None, ("highlight from long",)
    )
    state, _ = attach(state, [short, long])
    assert state["slug"]["我的复盘"]["正文"] == "a much longer retrospective body"
    assert state["slug"]["我的复盘"]["高亮"] == ["highlight from short", "highlight from long"]


def test_attach_deduplicates_identical_highlights_across_duplicates():
    state = {"slug": {"id": 1, "我的复盘": None}}
    first = Retrospective(1, "short", "notion-easy", None, None, None, ("same highlight",))
    second = Retrospective(
        1, "a much longer body here", "notion-medium", None, None, None, ("same highlight", "different one")
    )
    state, _ = attach(state, [first, second])
    assert state["slug"]["我的复盘"]["高亮"] == ["same highlight", "different one"]


def test_medium_day_heading_tolerates_backslash_escaped_pipe():
    text = "- -- Day 1 \\| W1 滑动窗口 \\| 定长滑动窗口 （同向）(2026-05-24) ---\n1、LC 1456 定长子串中元音的最大数目：body."
    entries = parse_medium_page(text)
    assert entries[0].day == "Day 1"
    assert entries[0].date == "2026-05-24"
