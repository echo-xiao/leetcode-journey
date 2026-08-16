from lc_review.cli import parse_readme_title_heading


def test_parses_number_dot_title_heading():
    text = "# 746. 使用最小花费爬楼梯\n\n**难度**: Easy\n"
    assert parse_readme_title_heading(text) == "使用最小花费爬楼梯"


def test_returns_none_when_no_heading_present():
    assert parse_readme_title_heading("no heading here\n") is None
