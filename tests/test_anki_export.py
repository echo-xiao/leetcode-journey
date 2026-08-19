from lc_review import anki_export

TECHNIQUES = {
    "9999_fixture-long": "数组双指针",
    "9998_fixture-minimal": "数学技巧",
}


def test_elements_row_for_fixture_long(fixture_problems):
    """Pins the exact TSV row _elements_row builds for the long fixture.

    An exact-match test on a synthetic fixture is deliberate: it is the guard
    against someone tuning _plain/TRIM_RE in problem_source.py for the app's
    benefit and silently changing all 402 real Anki cards. The fixture never
    changes, so this stays stable as the real library grows.
    """
    row = anki_export._elements_row(fixture_problems / "9999_fixture-long", TECHNIQUES)
    assert row == (
        "LeetCode::要素\t"
        "<b>9999. 夹具长题</b><br><br>"
        "给你一个整数数组 nums，请你找出所有满足条件的三元组。<br><br>"
        "示例 1：<br><br>输入：nums = [1, 2, 3]<br>输出：[[1, 2, 3]]<br><br>"
        "<i>这道题的要素怎么填？</i>\t"
        "<b>数组双指针</b><br><br>"
        "1. 指针类型：左右指针相向而行<br>"
        "2. slow 含义：本题不涉及<br>"
        "3. 停止条件：left < right 不成立时结束\t"
        "数组双指针 Medium"
    )


def test_elements_row_for_fixture_minimal(fixture_problems):
    row = anki_export._elements_row(fixture_problems / "9998_fixture-minimal", TECHNIQUES)
    assert row == (
        "LeetCode::要素\t"
        "<b>9998. 夹具短题</b><br><br>"
        "给你一个整数 n，返回 n 的平方。<br><br>"
        "示例 1：<br><br>输入：n = 3<br>输出：9<br><br>"
        "<i>这道题的要素怎么填？</i>\t"
        "<b>数学技巧</b><br><br>"
        "1. 函数定义：square(n) 返回 n 的平方\t"
        "数学技巧 Easy"
    )


def test_elements_row_is_none_without_answered_slots(tmp_path):
    folder = tmp_path / "1_demo"
    folder.mkdir()
    (folder / "problem.md").write_text(
        "# 1. Demo · 题目\n\n**难度**: Easy\n\n## 题目描述\n\nx\n", encoding="utf-8"
    )
    assert anki_export._elements_row(folder, {}) is None
