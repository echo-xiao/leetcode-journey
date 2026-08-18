from lc_review import problem_source


def test_statement_is_capped_for_anki(fixture_problems):
    folder = fixture_problems / "9999_fixture-long"
    capped = problem_source.statement_of(folder)
    assert len(capped) <= 500


def test_statement_is_whole_when_limit_is_none(fixture_problems):
    folder = fixture_problems / "9999_fixture-long"
    whole = problem_source.statement_of(folder, limit=None)
    capped = problem_source.statement_of(folder)
    assert len(whole) > len(capped)
    assert "填充内容四" in whole
    assert "填充内容四" not in capped


def test_statement_drops_the_constraints_block(fixture_problems):
    whole = problem_source.statement_of(
        fixture_problems / "9999_fixture-long", limit=None
    )
    assert "提示" not in whole
    assert "3000" not in whole
    assert "示例 2" in whole


def test_title_strips_the_heading_and_suffix(fixture_problems):
    assert (
        problem_source.title_of(fixture_problems / "9999_fixture-long")
        == "9999. 夹具长题"
    )


def test_elements_drop_their_numbering(fixture_problems):
    slots = problem_source.elements_of(fixture_problems / "9999_fixture-long")
    assert slots == [
        "指针类型：左右指针相向而行",
        "slow 含义：本题不涉及",
        "停止条件：left < right 不成立时结束",
    ]


def test_meta_reads_difficulty_and_looks_up_technique(fixture_problems):
    difficulty, technique = problem_source.meta_of(
        fixture_problems / "9999_fixture-long", {"9999_fixture-long": "数组双指针"}
    )
    assert difficulty == "Medium"
    assert technique == "数组双指针"


def test_meta_returns_empty_technique_when_unmapped(fixture_problems):
    _, technique = problem_source.meta_of(fixture_problems / "9998_fixture-minimal", {})
    assert technique == ""


def test_technique_map_covers_every_problem():
    """The real map, not the fixtures: every folder must resolve to a technique."""
    mapping = problem_source.technique_map()
    folders = [d.name for d in problem_source.PROBLEMS.iterdir() if d.is_dir()]
    missing = [name for name in folders if not mapping.get(name)]
    assert missing == []
