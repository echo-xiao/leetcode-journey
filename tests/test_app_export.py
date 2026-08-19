from lc_review import app_export

TECHNIQUES = {
    "9999_fixture-long": "数组双指针",
    "9998_fixture-minimal": "数学技巧",
}


def test_entry_carries_every_layer_of_the_chain(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9999_fixture-long", TECHNIQUES
    )
    assert entry["id"] == "9999_fixture-long"
    assert entry["number"] == 9999
    assert entry["title"] == "9999. 夹具长题"
    assert entry["difficulty"] == "Medium"
    assert entry["technique"] == "数组双指针"
    assert "填充内容四" in entry["statement"]
    assert entry["elements"][0] == "指针类型：左右指针相向而行"
    assert "排序后固定一数" in entry["pseudocode"]
    assert "去重那一步漏了" in entry["retrospective"]
    assert [s["name"] for s in entry["solutions"]] == [
        "solution_1.py",
        "solution_2.py",
    ]
    assert "def three_sum(nums):" in entry["solutions"][0]["code"]


def test_entry_keeps_the_highlight_markers_verbatim(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9999_fixture-long", TECHNIQUES
    )
    assert "==**去重那一步漏了，导致结果里有重复三元组。**==" in entry["retrospective"]


def test_entry_drops_the_retrospective_heading(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9999_fixture-long", TECHNIQUES
    )
    assert not entry["retrospective"].startswith("#")


def test_missing_retrospective_becomes_an_empty_string(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9998_fixture-minimal", TECHNIQUES
    )
    assert entry["retrospective"] == ""
    assert entry["solutions"] == []


def test_statement_is_not_capped(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9999_fixture-long", TECHNIQUES
    )
    assert len(entry["statement"]) > 500


def test_solutions_sort_numerically_not_lexically(tmp_path):
    folder = tmp_path / "1_demo"
    folder.mkdir()
    (folder / "problem.md").write_text(
        "# 1. Demo · 题目\n\n**难度**: Easy\n\n## 题目描述\n\nx\n", encoding="utf-8"
    )
    (folder / "elements.md").write_text("# 1. Demo · 要素\n", encoding="utf-8")
    for index in (1, 2, 10):
        (folder / f"solution_{index}.py").write_text(f"# {index}\n", encoding="utf-8")
    entry = app_export.problem_entry(folder, {})
    assert [s["name"] for s in entry["solutions"]] == [
        "solution_1.py",
        "solution_2.py",
        "solution_10.py",
    ]


def test_payload_is_versioned_and_sorted_and_has_no_timestamp(fixture_problems):
    payload = app_export.build_payload(fixture_problems, TECHNIQUES)
    assert payload["version"] == app_export.SCHEMA_VERSION
    assert [p["id"] for p in payload["problems"]] == [
        "9998_fixture-minimal",
        "9999_fixture-long",
    ]
    # A timestamp would change every day and defeat the write-if-changed check.
    assert "generatedAt" not in payload
