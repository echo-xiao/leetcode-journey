import json

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
    pseudocode_text = "\n".join(block["text"] for block in entry["pseudocode"])
    assert "排序后固定一数" in pseudocode_text
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
        "9997_fixture-no-fence",
        "9998_fixture-minimal",
        "9999_fixture-long",
    ]
    # A timestamp would change every day and defeat the write-if-changed check.
    assert "generatedAt" not in payload


def test_problems_sort_numerically_not_lexically(tmp_path):
    for name in ("1_a", "2_b", "15_c", "100_d", "1005_e"):
        folder = tmp_path / name
        folder.mkdir()
        (folder / "problem.md").write_text(
            "# 1. Demo · 题目\n\n**难度**: Easy\n\n## 题目描述\n\nx\n", encoding="utf-8"
        )
        (folder / "elements.md").write_text("# 1. Demo · 要素\n", encoding="utf-8")
    payload = app_export.build_payload(tmp_path, {})
    assert [p["number"] for p in payload["problems"]] == [1, 2, 15, 100, 1005]


def test_write_if_changed_creates_the_file(tmp_path):
    path = tmp_path / "app" / "content.json"
    written = app_export.write_if_changed(path, {"version": 1, "problems": []})
    assert written is True
    assert json.loads(path.read_text(encoding="utf-8")) == {
        "version": 1,
        "problems": [],
    }


def test_write_if_changed_is_a_noop_when_identical(tmp_path):
    path = tmp_path / "content.json"
    payload = {"version": 1, "problems": [{"id": "1_two-sum"}]}
    app_export.write_if_changed(path, payload)
    before = path.stat().st_mtime_ns

    written = app_export.write_if_changed(path, payload)

    assert written is False
    assert path.stat().st_mtime_ns == before


def test_write_if_changed_rewrites_when_content_differs(tmp_path):
    path = tmp_path / "content.json"
    app_export.write_if_changed(path, {"version": 1, "problems": []})
    written = app_export.write_if_changed(
        path, {"version": 1, "problems": [{"id": "1_two-sum"}]}
    )
    assert written is True
    assert "1_two-sum" in path.read_text(encoding="utf-8")


def test_written_json_keeps_chinese_readable(tmp_path):
    path = tmp_path / "content.json"
    app_export.write_if_changed(path, {"version": 1, "problems": [{"t": "二叉树"}]})
    assert "二叉树" in path.read_text(encoding="utf-8")


def test_pseudocode_is_now_an_array_of_typed_blocks(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9999_fixture-long", TECHNIQUES
    )
    assert isinstance(entry["pseudocode"], list)
    kinds = {block["kind"] for block in entry["pseudocode"]}
    assert kinds <= {"heading", "text", "code"}


def test_fence_becomes_one_code_block_with_indentation_intact():
    text = (
        "## 全量伪代码\n"
        "\n"
        "```\n"
        "1. 排序\n"
        "2. 遍历 i\n"
        "    3. 双指针夹逼\n"
        "```\n"
    )
    blocks = app_export._pseudocode_blocks(text)
    code_blocks = [b for b in blocks if b["kind"] == "code"]
    assert len(code_blocks) == 1
    assert code_blocks[0]["text"] == "1. 排序\n2. 遍历 i\n    3. 双指针夹逼"


def test_heading_hashes_are_stripped():
    text = "## 1. 核心本质\n\n一句话本质。\n"
    blocks = app_export._pseudocode_blocks(text)
    assert blocks[0] == {"kind": "heading", "text": "1. 核心本质"}


def test_top_level_document_title_is_dropped():
    text = "# 三数之和算法分析\n\n## 1. 核心本质\n\n一句话本质。\n"
    blocks = app_export._pseudocode_blocks(text)
    assert all(block["kind"] != "text" or "三数之和算法分析" not in block["text"] for block in blocks)
    assert not any(
        block["kind"] == "heading" and block["text"] == "三数之和算法分析" for block in blocks
    )
    # The lone document title produced no block of its own at all.
    assert blocks == [{"kind": "heading", "text": "1. 核心本质"}, {"kind": "text", "text": "一句话本质。"}]


def test_markdown_markers_are_stripped_from_text_blocks():
    text = "**核心本质**：用 `n % 2` 判断奇偶，复杂度 $O(1)$。\n- 第一条要点\n"
    blocks = app_export._pseudocode_blocks(text)
    assert len(blocks) == 1
    block = blocks[0]
    assert block["kind"] == "text"
    assert "**" not in block["text"]
    assert "`" not in block["text"]
    assert "$" not in block["text"]
    assert "核心本质：用 n % 2 判断奇偶，复杂度 O(1)。" in block["text"]
    assert "• 第一条要点" in block["text"]


def test_pseudocode_with_no_fence_still_produces_sensible_blocks(fixture_problems):
    entry = app_export.problem_entry(
        fixture_problems / "9997_fixture-no-fence", TECHNIQUES
    )
    blocks = entry["pseudocode"]
    assert blocks, "a fence-less pseudocode.md should still yield blocks"
    assert not any(block["kind"] == "code" for block in blocks)
    kinds = [block["kind"] for block in blocks]
    assert "heading" in kinds
    assert "text" in kinds
    # Markdown markers must still be cleaned even without a fence present.
    joined = "\n".join(block["text"] for block in blocks)
    assert "**" not in joined
    assert "`" not in joined
    assert "$" not in joined
