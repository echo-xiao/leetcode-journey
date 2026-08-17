import json

import pytest

from lc_review import cli
from lc_review.cli import TSV_IMPORT_HEADER, parse_readme_title_heading
from lc_review.lingshen import ProblemEntry
from lc_review.problems import SolvedProblem


def test_parses_number_dot_title_heading():
    text = "# 746. 使用最小花费爬楼梯\n\n**难度**: Easy\n"
    assert parse_readme_title_heading(text) == "使用最小花费爬楼梯"


def test_returns_none_when_no_heading_present():
    assert parse_readme_title_heading("no heading here\n") is None


def test_tsv_import_header_has_the_four_lines_with_correct_column_numbers():
    lines = TSV_IMPORT_HEADER.splitlines()
    assert lines == ["#separator:tab", "#html:true", "#deck column:1", "#tags column:4"]


ENTRIES = [
    ProblemEntry("7", "动态规划", 746, "使用最小花费爬楼梯", "min-cost", None, "一、入门 DP", "§1.1", 0)
]
SOLVED = [SolvedProblem(747, "min-cost", "747_min-cost")]


def _patch_build_state_dependencies(monkeypatch, tmp_path):
    monkeypatch.setattr(cli, "REPO", tmp_path)
    monkeypatch.setattr(cli, "STATE_PATH", tmp_path / "review_state.json")
    monkeypatch.setattr(cli, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(cli, "FRONTEND_ID_CACHE_PATH", tmp_path / "data" / "frontend_ids.json")
    monkeypatch.setattr(cli, "fetch_all", lambda *a, **k: ENTRIES)
    monkeypatch.setattr(cli, "scan", lambda *a, **k: (SOLVED, []))
    monkeypatch.setattr(cli, "read_ai_sections", lambda *a, **k: {"pseudocode": "", "complexity": ""})
    monkeypatch.setattr(cli, "_summary_records", lambda: [])


def test_build_state_command_preserves_retrospectives_and_cards_across_rebuild(tmp_path, monkeypatch):
    """FIX 1 regression: build-state must never reset 我的复盘/要素卡/已生成卡片
    to empty on a routine rebuild -- both review_state.json and data/ are
    gitignored, so resetting them is unrecoverable."""
    _patch_build_state_dependencies(monkeypatch, tmp_path)

    cli.build_state_command(refresh=False)
    state = cli.load_state(cli.STATE_PATH)
    state["min-cost"]["我的复盘"] = {"来源": "notion-easy", "正文": "hand written retro", "高亮": []}
    state["min-cost"]["要素卡"] = "动态规划"
    state["min-cost"]["要素卡来源"] = "关键词匹配"
    state["min-cost"]["已生成卡片"] = ["伪代码"]
    cli.save_state(state, cli.STATE_PATH)

    cli.build_state_command(refresh=False)
    rebuilt = cli.load_state(cli.STATE_PATH)
    assert rebuilt["min-cost"]["我的复盘"]["正文"] == "hand written retro"
    assert rebuilt["min-cost"]["要素卡"] == "动态规划"
    assert rebuilt["min-cost"]["要素卡来源"] == "关键词匹配"
    assert rebuilt["min-cost"]["已生成卡片"] == ["伪代码"]


def test_attach_fupan_command_refuses_to_run_when_no_notion_dump_exists(tmp_path, monkeypatch):
    """FIX 1 regression: attach-fupan must not silently no-op (and print
    success) when neither Notion export is present on disk."""
    monkeypatch.setattr(cli, "REPO", tmp_path)
    monkeypatch.setattr(cli, "STATE_PATH", tmp_path / "review_state.json")
    monkeypatch.setattr(cli, "NOTION_DIR", tmp_path / "data" / "notion")
    cli.save_state({}, cli.STATE_PATH)
    with pytest.raises(SystemExit):
        cli.attach_fupan_command()


def test_attach_fupan_command_runs_when_only_one_dump_exists(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "REPO", tmp_path)
    monkeypatch.setattr(cli, "STATE_PATH", tmp_path / "review_state.json")
    notion_dir = tmp_path / "data" / "notion"
    notion_dir.mkdir(parents=True)
    (notion_dir / "easy.txt").write_text("", encoding="utf-8")
    monkeypatch.setattr(cli, "NOTION_DIR", notion_dir)
    cli.save_state({}, cli.STATE_PATH)
    cli.attach_fupan_command()  # must not raise


def test_cached_id_resolver_only_calls_the_underlying_resolver_once_per_slug(tmp_path):
    cache_path = tmp_path / "frontend_ids.json"
    calls = []

    def fake_resolve(slug):
        calls.append(slug)
        return 42

    resolve = cli._cached_id_resolver(cache_path, fake_resolve)
    assert resolve("a") == 42
    assert resolve("a") == 42
    assert calls == ["a"]
    assert json.loads(cache_path.read_text(encoding="utf-8"))["a"] == 42


def test_cached_id_resolver_reads_a_pre_existing_cache_without_calling_resolver(tmp_path):
    cache_path = tmp_path / "frontend_ids.json"
    cache_path.write_text(json.dumps({"a": 7}), encoding="utf-8")

    def never(slug):
        raise AssertionError("should not call the resolver for an already-cached slug")

    resolve = cli._cached_id_resolver(cache_path, never)
    assert resolve("a") == 7


def test_daily_command_runs_build_elements_before_build_table(tmp_path, monkeypatch):
    """FIX 8 regression: build-elements must run before build-table so 要素卡
    is filled in before the table reads it."""
    order = []
    monkeypatch.setattr(cli, "build_state_command", lambda refresh: order.append("state"))
    monkeypatch.setattr(cli, "attach_fupan_command", lambda: order.append("fupan"))
    monkeypatch.setattr(cli, "build_elements_command", lambda: order.append("elements"))
    monkeypatch.setattr(cli, "build_table_command", lambda: order.append("table"))
    monkeypatch.setattr(cli, "export_anki_command", lambda: order.append("anki"))
    monkeypatch.setattr(cli, "REPO", tmp_path)
    monkeypatch.setattr(cli, "STATE_PATH", tmp_path / "review_state.json")
    cli.save_state({}, cli.STATE_PATH)

    cli.daily_command("2026-08-18")

    assert order == ["state", "fupan", "elements", "table", "anki"]


BASE_RECORD = {
    "id": 1,
    "题号来源": "灵神",
    "题名": "示例题",
    "难度分": 1500,
    "题单": "1. 滑动窗口与双指针",
    "章": "一、定长滑动窗口",
    "节": "§1.1",
    "归属来源": "灵神",
    "亦属": [],
    "要素卡": "滑动窗口",
    "要素卡来源": "关键词匹配",
    "代码": "Problems/1_example",
}


def test_export_anki_command_records_which_decks_each_slug_got_a_note_in(tmp_path, monkeypatch):
    """FIX 10 regression: export-anki must persist 已生成卡片 so the daily
    brief and 大表's 已出卡 column stop reading it as permanently empty."""
    monkeypatch.setattr(cli, "REPO", tmp_path)
    monkeypatch.setattr(cli, "STATE_PATH", tmp_path / "review_state.json")
    monkeypatch.setattr(cli, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(cli, "fetch_all", lambda *a, **k: [])

    state = {
        "has-retro": {
            **BASE_RECORD,
            "我的复盘": {"来源": "notion-easy", "正文": "y", "高亮": []},
            "AI题解": {"伪代码": "", "复杂度": ""},
            "已生成卡片": [],
        },
        "has-pseudocode": {
            **BASE_RECORD,
            "id": 2,
            "我的复盘": None,
            "AI题解": {"伪代码": "code", "复杂度": ""},
            "已生成卡片": [],
        },
        "has-neither": {
            **BASE_RECORD,
            "id": 3,
            "我的复盘": None,
            "AI题解": {"伪代码": "", "复杂度": ""},
            "已生成卡片": ["stale"],
        },
    }
    cli.save_state(state, cli.STATE_PATH)

    cli.export_anki_command()

    rebuilt = cli.load_state(cli.STATE_PATH)
    assert rebuilt["has-retro"]["已生成卡片"] == ["复习"]
    assert rebuilt["has-pseudocode"]["已生成卡片"] == ["伪代码"]
    assert rebuilt["has-neither"]["已生成卡片"] == []


def test_export_anki_command_writes_import_headers_to_every_tsv(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "REPO", tmp_path)
    monkeypatch.setattr(cli, "STATE_PATH", tmp_path / "review_state.json")
    monkeypatch.setattr(cli, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(cli, "fetch_all", lambda *a, **k: [])
    cli.save_state({}, cli.STATE_PATH)

    cli.export_anki_command()

    for name in ("elements.tsv", "retrospectives.tsv", "pseudocode.tsv"):
        text = (tmp_path / "docs" / "anki" / name).read_text(encoding="utf-8")
        assert text.startswith(TSV_IMPORT_HEADER)
