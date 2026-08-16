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
