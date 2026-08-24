import sys

from lc_review import cli


def test_export_app_subcommand_calls_run(monkeypatch):
    called = []
    monkeypatch.setattr("lc_review.app_export.run", lambda dry_run=False: called.append(dry_run))
    monkeypatch.setattr(sys, "argv", ["lc_review", "export-app"])
    cli.main()
    # The standalone subcommand always writes: it only touches files inside
    # the repo, so there is nothing to opt into.
    assert called == [False]


def test_sync_all_runs_export_app_last(monkeypatch):
    order = []
    # Every step is stubbed, including the two that talk to LeetCode. A unit
    # test that reaches the network is slow, flaky, and stops being a test of
    # the pipeline's order.
    monkeypatch.setattr(cli, "refresh_ac_times_command", lambda *a: order.append("dates"))
    monkeypatch.setattr(cli, "refresh_changed_command", lambda *a: order.append("changed"))
    monkeypatch.setattr(cli, "sync_new_command", lambda *a: order.append("new"))
    monkeypatch.setattr(cli, "build_answers_command", lambda *a: order.append("answers"))
    monkeypatch.setattr(cli, "sync_review_md_command", lambda *a: order.append("review"))
    monkeypatch.setattr(cli, "sync_fupan_command", lambda *a: order.append("fupan"))
    monkeypatch.setattr(cli, "export_app_command", lambda apply: order.append(("app", apply)))

    cli.sync_all_command(apply=True)

    # The refresh of changed problems must land after the new ones arrive
    # and before the elements are answered against their pseudocode.
    assert order == [
        "dates", "new", "changed", "answers", "review", "fupan", ("app", True)
    ]


def test_sync_all_dry_run_does_not_write_app_content(monkeypatch, tmp_path):
    """apply=False must reach step 5 too, or a dry sync-all silently writes
    the 2.3 MB app payload for real."""
    monkeypatch.setattr(cli, "refresh_ac_times_command", lambda *a: None)
    monkeypatch.setattr(cli, "refresh_changed_command", lambda *a: None)
    monkeypatch.setattr(cli, "sync_new_command", lambda *a: None)
    monkeypatch.setattr(cli, "build_answers_command", lambda *a: None)
    monkeypatch.setattr(cli, "sync_review_md_command", lambda *a: None)
    monkeypatch.setattr(cli, "sync_fupan_command", lambda *a: None)

    out_path = tmp_path / "content.json"
    monkeypatch.setattr("lc_review.app_export.OUT_PATH", out_path)

    cli.sync_all_command(apply=False)

    assert not out_path.exists()
