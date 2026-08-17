import json

import pytest

from lc_review.lingshen import (
    LISTS,
    ProblemEntry,
    extract_post_content,
    fetch_all,
    parse_list,
)


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


def test_lists_has_twelve_entries_with_unique_slugs():
    assert len(LISTS) == 12
    assert len({slug for _, _, slug in LISTS}) == 12


def test_extract_post_content_pulls_markdown_from_next_data():
    payload = {
        "props": {
            "pageProps": {
                "dehydratedState": {
                    "queries": [
                        {"state": {"data": {"unrelated": "x"}}},
                        {
                            "state": {
                                "data": {
                                    "qaQuestion": {"content": "## 一、入门\n" + "x" * 2100}
                                }
                            }
                        },
                    ]
                }
            }
        }
    }
    html = (
        "<html><body>"
        f'<script id="__NEXT_DATA__" type="application/json">{json.dumps(payload)}</script>'
        "</body></html>"
    )
    content = extract_post_content(html)
    assert content.startswith("## 一、入门")


def test_extract_post_content_raises_when_script_missing():
    with pytest.raises(ValueError, match="__NEXT_DATA__"):
        extract_post_content("<html><body>nothing here</body></html>")


def test_extract_post_content_raises_when_no_long_content_string_found():
    payload = {
        "props": {
            "pageProps": {
                "dehydratedState": {
                    "queries": [
                        {"state": {"data": {"content": "too short"}}},
                    ]
                }
            }
        }
    }
    html = (
        "<html><body>"
        f'<script id="__NEXT_DATA__" type="application/json">{json.dumps(payload)}</script>'
        "</body></html>"
    )
    with pytest.raises(ValueError, match="no post content found"):
        extract_post_content(html)


def test_extract_post_content_prefers_qa_question_over_earlier_long_content():
    """An unrelated long ``content`` string that appears earlier in dict
    iteration order must not shadow the known-correct qaQuestion.content."""
    payload = {
        "props": {
            "pageProps": {
                "dehydratedState": {
                    "queries": [
                        {
                            "state": {
                                "data": {
                                    "unrelatedLongContent": {
                                        "content": "DECOY " + "y" * 2100
                                    },
                                    "qaQuestion": {
                                        "content": "## 一、真正的题单\n" + "x" * 2100
                                    },
                                }
                            }
                        },
                    ]
                }
            }
        }
    }
    html = (
        "<html><body>"
        f'<script id="__NEXT_DATA__" type="application/json">{json.dumps(payload)}</script>'
        "</body></html>"
    )
    content = extract_post_content(html)
    assert content.startswith("## 一、真正的题单")
    assert "DECOY" not in content


def test_fetch_all_uses_cache_and_does_not_redownload(tmp_path, monkeypatch):
    download_calls = []

    def fake_download(slug):
        download_calls.append(slug)
        return f"<html>{slug}</html>"

    monkeypatch.setattr("lc_review.lingshen._download", fake_download)
    monkeypatch.setattr(
        "lc_review.lingshen.extract_post_content", lambda html: "## chapter\n"
    )

    for list_no, _, _ in LISTS:
        (tmp_path / f"{list_no}.md").write_text("## cached chapter\n", encoding="utf-8")

    entries = fetch_all(tmp_path)

    assert download_calls == []
    assert entries == []


def test_fetch_all_refresh_true_forces_redownload(tmp_path, monkeypatch):
    download_calls = []

    def fake_download(slug):
        download_calls.append(slug)
        return f"<html>{slug}</html>"

    monkeypatch.setattr("lc_review.lingshen._download", fake_download)
    monkeypatch.setattr(
        "lc_review.lingshen.extract_post_content", lambda html: "## chapter\n"
    )

    for list_no, _, _ in LISTS:
        (tmp_path / f"{list_no}.md").write_text("## cached chapter\n", encoding="utf-8")

    fetch_all(tmp_path, refresh=True)

    assert download_calls == [slug for _, _, slug in LISTS]
    for list_no, _, _ in LISTS:
        assert (tmp_path / f"{list_no}.md").read_text(encoding="utf-8") == "## chapter\n"
