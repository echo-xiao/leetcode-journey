from lc_review import refresh_changed


def test_candidate_slugs_are_deduplicated_keeping_order():
    # The recent list is per submission, so one problem solved three times
    # today appears three times. Checking it three times would triple the
    # requests for no new information.
    submissions = [
        {"titleSlug": "3sum", "timestamp": "3"},
        {"titleSlug": "two-sum", "timestamp": "2"},
        {"titleSlug": "3sum", "timestamp": "1"},
    ]
    assert refresh_changed.candidate_slugs(submissions) == ["3sum", "two-sum"]


def test_candidate_slugs_ignores_entries_without_a_slug():
    assert refresh_changed.candidate_slugs([{"timestamp": "1"}]) == []


def test_needs_refresh_is_false_when_the_problem_is_not_in_the_library(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh_changed, "PROBLEMS", tmp_path)
    # sync-new downloads it; refreshing something absent is not this module's
    # job.
    assert not refresh_changed.needs_refresh("brand-new", ["def f(): pass"])


def test_needs_refresh_is_false_when_every_remote_shape_is_already_local(tmp_path, monkeypatch):
    folder = tmp_path / "1_two-sum"
    folder.mkdir()
    (folder / "solution_1.py").write_text("def f(x):\n    return sum(x)\n", encoding="utf-8")
    monkeypatch.setattr(refresh_changed, "PROBLEMS", tmp_path)

    renamed = "def g(nums):\n    return sum(nums)\n"
    assert not refresh_changed.needs_refresh("two-sum", [renamed])


def test_needs_refresh_is_true_when_a_new_shape_turns_up(tmp_path, monkeypatch):
    folder = tmp_path / "1_two-sum"
    folder.mkdir()
    (folder / "solution_1.py").write_text("def f(x):\n    return sum(x)\n", encoding="utf-8")
    monkeypatch.setattr(refresh_changed, "PROBLEMS", tmp_path)

    rewritten = "def f(x):\n    t = 0\n    for i in x:\n        t += i\n    return t\n"
    assert refresh_changed.needs_refresh("two-sum", [rewritten])


def test_needs_refresh_is_true_when_the_folder_has_no_code_at_all(tmp_path, monkeypatch):
    # A folder whose download failed halfway. Nothing local to compare
    # against, so anything remote is new.
    folder = tmp_path / "1_two-sum"
    folder.mkdir()
    monkeypatch.setattr(refresh_changed, "PROBLEMS", tmp_path)

    assert refresh_changed.needs_refresh("two-sum", ["def f(): pass"])


def test_a_slug_matches_only_the_whole_suffix(tmp_path, monkeypatch):
    # "3sum" must not match "18_4sum". Matching on the part after the number
    # is what keeps one problem's refresh from landing on another's folder.
    (tmp_path / "18_4sum").mkdir()
    monkeypatch.setattr(refresh_changed, "PROBLEMS", tmp_path)

    assert not refresh_changed.needs_refresh("3sum", ["def f(): pass"])
