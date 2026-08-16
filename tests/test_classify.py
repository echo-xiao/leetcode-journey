from lc_review.classify import (
    ORIGIN_CROSS,
    ORIGIN_LINGSHEN,
    ORIGIN_OUTSIDE,
    assign,
)
from lc_review.lingshen import ProblemEntry
from lc_review.problems import SolvedProblem


def entry(list_no, chapter, section, pid, slug, order=0, title=None):
    return ProblemEntry(list_no, f"list{list_no}", pid, title or slug, slug, None, chapter, section, order)


def never_called(slug):
    raise AssertionError(f"should not have needed to resolve {slug}")


def no_title_lookup(slug):
    raise AssertionError(f"should not have needed to look up a title for {slug}")


def fake_resolver(slug):
    return {"house-robber": 198, "design-thing": 1622}[slug]


def fake_title_lookup(slug):
    return {"house-robber": "打家劫舍"}.get(slug)


def test_single_list_problem_keeps_lingshen_origin():
    entries = [entry("7", "一", "§1.1", 746, "min-cost")]
    solved = [SolvedProblem(747, "min-cost", "747_min-cost")]
    assignments, unplaceable = assign(entries, solved, {}, never_called, no_title_lookup)
    assert unplaceable == []
    assert assignments[0].origin == ORIGIN_LINGSHEN
    assert assignments[0].section == "§1.1"
    assert assignments[0].also_in == []


def test_problem_id_comes_from_the_taxonomy_not_the_directory_prefix():
    # The directory says 1046; the taxonomy says 1004. 1004 must win, because
    # 1046 is a different problem entirely (Last Stone Weight).
    entries = [entry("1", "二", "§2.1", 1004, "max-consecutive-ones-iii")]
    solved = [SolvedProblem(1046, "max-consecutive-ones-iii", "1046_max-consecutive-ones-iii")]
    assignments, _ = assign(entries, solved, {}, never_called, no_title_lookup)
    assert assignments[0].problem_id == 1004
    assert assignments[0].id_source == "灵神"


def test_uncovered_problem_asks_leetcode_for_its_number():
    entries = [entry("7", "一", "§1.1", 746, "min-cost")]
    solved = [
        SolvedProblem(747, "min-cost", "747_min-cost"),
        SolvedProblem(9999, "house-robber", "9999_house-robber"),
    ]
    tags = {"min-cost": ["Dynamic Programming"], "house-robber": ["Dynamic Programming"]}
    assignments, _ = assign(entries, solved, tags, fake_resolver, fake_title_lookup)
    robber = next(a for a in assignments if a.slug == "house-robber")
    assert robber.problem_id == 198
    assert robber.id_source == "leetcode-api"


def test_cross_list_problem_picks_the_smallest_section():
    entries = [
        entry("1", "一", "§1.1", 11, "container"),
        entry("1", "一", "§1.1", 15, "three-sum"),
        entry("1", "一", "§1.1", 16, "closest"),
        entry("10", "二", "§2.1", 11, "container"),
    ]
    solved = [SolvedProblem(11, "container", "11_container")]
    assignments, _ = assign(entries, solved, {}, never_called, no_title_lookup)
    assert assignments[0].origin == ORIGIN_CROSS
    assert assignments[0].list_no == "10"
    assert assignments[0].also_in == [("1", "一", "§1.1")]


def test_cross_list_tie_breaks_deterministically():
    entries = [
        entry("1", "一", "§1.1", 11, "container"),
        entry("10", "二", "§2.1", 11, "container"),
    ]
    solved = [SolvedProblem(11, "container", "11_container")]
    first, _ = assign(entries, solved, {}, never_called, no_title_lookup)
    second, _ = assign(list(reversed(entries)), solved, {}, never_called, no_title_lookup)
    assert first[0].section == second[0].section


def test_uncovered_problem_lands_in_the_most_tag_similar_section():
    entries = [
        entry("7", "一", "§1.1", 746, "min-cost"),
        entry("11", "二", "§2.1", 104, "max-depth"),
    ]
    solved = [
        SolvedProblem(747, "min-cost", "747_min-cost"),
        SolvedProblem(104, "max-depth", "104_max-depth"),
        SolvedProblem(198, "house-robber", "198_house-robber"),
    ]
    tags = {
        "min-cost": ["Array", "Dynamic Programming"],
        "max-depth": ["Tree", "Depth-First Search"],
        "house-robber": ["Array", "Dynamic Programming"],
    }
    assignments, unplaceable = assign(entries, solved, tags, fake_resolver, fake_title_lookup)
    house = next(a for a in assignments if a.slug == "house-robber")
    assert house.origin == ORIGIN_OUTSIDE
    assert house.section == "§1.1"
    assert unplaceable == []


def test_uncovered_problem_with_no_tag_overlap_is_unplaceable():
    entries = [entry("7", "一", "§1.1", 746, "min-cost")]
    solved = [
        SolvedProblem(747, "min-cost", "747_min-cost"),
        SolvedProblem(1, "design-thing", "1_design-thing"),
    ]
    tags = {"min-cost": ["Dynamic Programming"], "design-thing": ["Design"]}
    assignments, unplaceable = assign(entries, solved, tags, fake_resolver, fake_title_lookup)
    assert [p.slug for p in unplaceable] == ["design-thing"]
    assert all(a.slug != "design-thing" for a in assignments)


def test_only_solved_problems_are_assigned():
    entries = [entry("7", "一", "§1.1", 70, "climbing"), entry("7", "一", "§1.1", 746, "min-cost")]
    solved = [SolvedProblem(747, "min-cost", "747_min-cost")]
    assignments, _ = assign(entries, solved, {}, never_called, no_title_lookup)
    assert [a.slug for a in assignments] == ["min-cost"]


def test_taxonomy_covered_problem_keeps_the_taxonomy_title():
    entries = [entry("7", "一", "§1.1", 746, "min-cost", title="使用最小花费爬楼梯")]
    solved = [SolvedProblem(747, "min-cost", "747_min-cost")]
    assignments, _ = assign(entries, solved, {}, never_called, no_title_lookup)
    assert assignments[0].title == "使用最小花费爬楼梯"


def test_uncovered_problem_gets_the_looked_up_title():
    entries = [entry("7", "一", "§1.1", 746, "min-cost")]
    solved = [
        SolvedProblem(747, "min-cost", "747_min-cost"),
        SolvedProblem(9999, "house-robber", "9999_house-robber"),
    ]
    tags = {"min-cost": ["Dynamic Programming"], "house-robber": ["Dynamic Programming"]}
    assignments, _ = assign(entries, solved, tags, fake_resolver, fake_title_lookup)
    robber = next(a for a in assignments if a.slug == "house-robber")
    assert robber.title == "打家劫舍"


def test_uncovered_problem_with_no_lookup_result_falls_back_to_the_slug():
    entries = [entry("7", "一", "§1.1", 746, "min-cost")]
    solved = [
        SolvedProblem(747, "min-cost", "747_min-cost"),
        SolvedProblem(1622, "design-thing", "1622_design-thing"),
    ]
    tags = {"min-cost": ["Dynamic Programming"], "design-thing": ["Dynamic Programming"]}
    assignments, _ = assign(entries, solved, tags, fake_resolver, fake_title_lookup)
    design = next(a for a in assignments if a.slug == "design-thing")
    assert design.title == "design-thing"
