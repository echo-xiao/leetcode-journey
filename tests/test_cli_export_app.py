import sys

from lc_review import cli


def test_export_app_subcommand_calls_run(monkeypatch):
    called = []
    monkeypatch.setattr("lc_review.app_export.run", lambda: called.append(True))
    monkeypatch.setattr(sys, "argv", ["lc_review", "export-app"])
    cli.main()
    assert called == [True]


def test_sync_all_runs_export_app_last(monkeypatch):
    order = []
    monkeypatch.setattr(cli, "sync_new_command", lambda *a: order.append("new"))
    monkeypatch.setattr(cli, "build_answers_command", lambda *a: order.append("answers"))
    monkeypatch.setattr(cli, "sync_review_md_command", lambda *a: order.append("review"))
    monkeypatch.setattr(cli, "sync_fupan_command", lambda *a: order.append("fupan"))
    monkeypatch.setattr(cli, "export_app_command", lambda: order.append("app"))

    cli.sync_all_command(apply=True)

    assert order == ["new", "answers", "review", "fupan", "app"]
