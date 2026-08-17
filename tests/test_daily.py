from lc_review.cli import render_daily_brief

STATE = {
    "a": {"id": 1, "题名": "两数之和", "我的复盘": {"正文": "x"}, "已生成卡片": ["伪代码"]},
    "b": {"id": 2, "题名": "两数相加", "我的复盘": None, "已生成卡片": []},
}


def test_brief_reports_the_date_and_new_problem_count():
    brief = render_daily_brief(STATE, ["b"], "2026-08-17")
    assert "2026-08-17" in brief
    assert "新增 1 题" in brief


def test_brief_lists_problems_still_missing_a_retrospective():
    brief = render_daily_brief(STATE, [], "2026-08-17")
    assert "两数相加" in brief
    assert "两数之和" not in brief.split("缺复盘")[1]


def test_brief_counts_cards_not_yet_generated():
    brief = render_daily_brief(STATE, [], "2026-08-17")
    assert "待生成卡片 1 题" in brief
