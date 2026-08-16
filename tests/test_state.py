import json

from lc_review.classify import ORIGIN_CROSS, ORIGIN_OUTSIDE, Assignment
from lc_review.problems import SolvedProblem
from lc_review.state import build_state, load_state, render_judgment_report, save_state

SCHEDULING_FIELDS = {"熟练度", "上次复习", "下次复习", "复习次数", "状态"}


def an_assignment(**overrides):
    defaults = dict(
        slug="min-cost",
        problem_id=746,
        id_source="灵神",
        title="使用最小花费爬楼梯",
        list_no="7",
        list_name="动态规划",
        chapter="一、入门 DP",
        section="§1.1 爬楼梯",
        rating=1300,
        origin="灵神",
        also_in=[],
    )
    defaults.update(overrides)
    return Assignment(**defaults)


def test_state_is_keyed_by_slug_and_carries_the_taxonomy():
    state = build_state([an_assignment()], [SolvedProblem(747, "min-cost", "747_min-cost")], {})
    record = state["min-cost"]
    assert record["id"] == 746
    assert record["题单"] == "7. 动态规划"
    assert record["章"] == "一、入门 DP"
    assert record["节"] == "§1.1 爬楼梯"
    assert record["归属来源"] == "灵神"
    assert record["代码"] == "Problems/747_min-cost"


def test_state_never_contains_scheduling_fields():
    state = build_state([an_assignment()], [SolvedProblem(747, "min-cost", "747_min-cost")], {})
    assert SCHEDULING_FIELDS.isdisjoint(state["min-cost"])


def test_state_carries_ai_sections_and_empty_card_list():
    state = build_state(
        [an_assignment()],
        [SolvedProblem(747, "min-cost", "747_min-cost")],
        {"min-cost": {"pseudocode": "loop", "complexity": "$O(n)$"}},
    )
    assert state["min-cost"]["AI题解"] == {"伪代码": "loop", "复杂度": "$O(n)$"}
    assert state["min-cost"]["已生成卡片"] == []
    assert state["min-cost"]["我的复盘"] is None


def test_save_and_load_round_trip(tmp_path):
    state = build_state([an_assignment()], [SolvedProblem(747, "min-cost", "747_min-cost")], {})
    path = tmp_path / "review_state.json"
    save_state(state, path)
    assert load_state(path) == state
    assert "使用最小花费爬楼梯" in path.read_text(encoding="utf-8")


def test_judgment_report_lists_only_cross_outside_and_unplaceable():
    state = build_state(
        [
            an_assignment(),
            an_assignment(slug="container", problem_id=11, origin=ORIGIN_CROSS,
                          also_in=[("1", "一", "§1.1")]),
            an_assignment(slug="design-thing", problem_id=1, origin=ORIGIN_OUTSIDE),
        ],
        [
            SolvedProblem(747, "min-cost", "747_min-cost"),
            SolvedProblem(11, "container", "11_container"),
            SolvedProblem(1, "design-thing", "1_design-thing"),
        ],
        {},
    )
    report = render_judgment_report(state, [SolvedProblem(9, "odd-one", "9_odd-one")])
    assert "container" in report
    assert "design-thing" in report
    assert "odd-one" in report
    assert "min-cost" not in report


def test_state_carries_id_source_for_both_lingshen_and_api_derived_ids():
    """题号来源 must reflect where the displayed number actually came from.

    A problem placed straight from 灵神's lists has a trustworthy displayed
    number from the list itself. A problem 灵神 never listed had to have its
    number resolved via the LeetCode API instead, and the two must stay
    distinguishable in the persisted record, not just in the Assignment.
    """
    state = build_state(
        [
            an_assignment(slug="min-cost", problem_id=746, id_source="灵神"),
            an_assignment(
                slug="design-thing",
                problem_id=1,
                id_source="leetcode-api",
                origin=ORIGIN_OUTSIDE,
            ),
        ],
        [
            SolvedProblem(747, "min-cost", "747_min-cost"),
            SolvedProblem(1, "design-thing", "1_design-thing"),
        ],
        {},
    )
    assert state["min-cost"]["题号来源"] == "灵神"
    assert state["design-thing"]["题号来源"] == "leetcode-api"
