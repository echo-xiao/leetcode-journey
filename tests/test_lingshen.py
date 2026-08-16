from lc_review.lingshen import ProblemEntry, parse_list


def test_parses_every_problem_entry(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    assert len(entries) == 5


def test_captures_id_title_slug_and_rating(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    entry = entries[1]
    assert entry.problem_id == 746
    assert entry.title == "使用最小花费爬楼梯"
    assert entry.slug == "min-cost-climbing-stairs"
    assert entry.rating == 1300


def test_rating_is_none_when_absent(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    assert entries[0].problem_id == 70
    assert entries[0].rating is None


def test_tracks_chapter_and_section(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    assert entries[0].chapter == "一、入门 DP"
    assert entries[0].section == "§1.1 爬楼梯"
    assert entries[3].section == "§1.2 打家劫舍"
    assert entries[4].chapter == "二、网格图 DP"


def test_carries_list_identity(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    assert entries[0].list_no == "7"
    assert entries[0].list_name == "动态规划"


def test_order_preserves_source_sequence(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    assert [e.order for e in entries] == [0, 1, 2, 3, 4]


def test_ignores_the_footer_link_index(lingshen_sample):
    entries = parse_list(lingshen_sample, "7", "动态规划")
    assert all("circle" not in e.slug for e in entries)


def test_entry_fields_are_positional_in_declared_order():
    a = ProblemEntry("7", "动态规划", 70, "爬楼梯", "climbing-stairs", None, "一", "§1.1", 0)
    assert a.list_no == "7"
    assert a.list_name == "动态规划"
    assert a.problem_id == 70
    assert a.title == "爬楼梯"
    assert a.slug == "climbing-stairs"
    assert a.rating is None
    assert a.chapter == "一"
    assert a.section == "§1.1"
    assert a.order == 0
