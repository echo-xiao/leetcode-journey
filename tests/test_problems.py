from pathlib import Path

import pytest

from lc_review.problems import SolvedProblem, read_ai_sections, resolve_frontend_id, scan


def _make_problem(root: Path, dirname: str, readme: str = "") -> None:
    directory = root / dirname
    directory.mkdir(parents=True)
    (directory / "README_CN.md").write_text(readme, encoding="utf-8")


def test_scan_reads_internal_id_and_slug(tmp_path):
    _make_problem(tmp_path, "747_min-cost-climbing-stairs")
    solved, malformed = scan(tmp_path)
    assert solved == [
        SolvedProblem(747, "min-cost-climbing-stairs", "747_min-cost-climbing-stairs")
    ]
    assert malformed == []


def test_scan_reports_malformed_directories_without_guessing(tmp_path):
    _make_problem(tmp_path, "None_lowest-common-ancestor-of-a-binary-search-tree")
    _make_problem(tmp_path, "1_two-sum")
    solved, malformed = scan(tmp_path)
    assert [p.internal_id for p in solved] == [1]
    assert malformed == ["None_lowest-common-ancestor-of-a-binary-search-tree"]


def test_scan_is_sorted_by_internal_id(tmp_path):
    _make_problem(tmp_path, "746_a")
    _make_problem(tmp_path, "70_b")
    solved, _ = scan(tmp_path)
    assert [p.internal_id for p in solved] == [70, 746]


@pytest.mark.network
def test_resolve_frontend_id_returns_the_displayed_number():
    # 1046 is this problem's internal id; 1004 is what LeetCode displays.
    assert resolve_frontend_id("max-consecutive-ones-iii") == 1004


@pytest.mark.network
def test_resolve_frontend_id_distinguishes_the_colliding_pair():
    # Problem 1046 is Last Stone Weight, whose internal id is 1127. Getting
    # these two backwards attaches the wrong retrospective to both.
    assert resolve_frontend_id("last-stone-weight") == 1046


def test_read_ai_sections_extracts_pseudocode_and_complexity(tmp_path):
    readme = """# 746. 使用最小花费爬楼梯

## 题目描述

blah

---
## 解题思路与复盘

1. 一句话直击本质：滑动窗口。

2. 综合思路：
   - 双指针

3. 全量伪代码：
   ```plaintext
   初始化 left 为 0
   返回 maxLen
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$
   - 空间复杂度：$O(1)$
"""
    path = tmp_path / "README_CN.md"
    path.write_text(readme, encoding="utf-8")
    sections = read_ai_sections(path)
    assert "初始化 left 为 0" in sections["pseudocode"]
    assert "$O(n)$" in sections["complexity"]
    assert "一句话直击本质" not in sections["pseudocode"]


def test_read_ai_sections_returns_empty_strings_when_absent(tmp_path):
    path = tmp_path / "README_CN.md"
    path.write_text("# 1. two sum\n\nno retrospective here\n", encoding="utf-8")
    assert read_ai_sections(path) == {"pseudocode": "", "complexity": ""}
