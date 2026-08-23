import json

import pytest

from lc_review import ac_times


def test_latest_ac_timestamp_takes_the_most_recent_pass():
    # LeetCode returns newest first, but the order is not promised anywhere,
    # so the pick must not depend on it.
    subs = [
        {"id": "3", "timestamp": "1787184000"},
        {"id": "1", "timestamp": "1700000000"},
        {"id": "2", "timestamp": "1750000000"},
    ]
    assert ac_times.latest_ac_timestamp(subs) == 1_787_184_000


def test_latest_ac_timestamp_is_none_without_submissions():
    assert ac_times.latest_ac_timestamp([]) is None


def test_latest_ac_timestamp_ignores_unparseable_entries():
    subs = [{"id": "1", "timestamp": "not-a-number"}, {"id": "2", "timestamp": 1_700_000_000}]
    assert ac_times.latest_ac_timestamp(subs) == 1_700_000_000


def test_missing_index_reads_as_empty(tmp_path):
    assert ac_times.load(tmp_path / "nope.json") == {}


def test_record_then_load_round_trips(tmp_path):
    path = tmp_path / "_ac_times.json"
    ac_times.record("1_two-sum", 1_700_000_000, path=path)
    ac_times.record("15_3sum", 1_787_184_000, path=path)

    assert ac_times.load(path) == {"1_two-sum": 1_700_000_000, "15_3sum": 1_787_184_000}


def test_record_overwrites_an_earlier_value_for_the_same_problem(tmp_path):
    path = tmp_path / "_ac_times.json"
    ac_times.record("1_two-sum", 1_700_000_000, path=path)
    ac_times.record("1_two-sum", 1_787_184_000, path=path)

    assert ac_times.load(path) == {"1_two-sum": 1_787_184_000}


def test_the_file_is_sorted_so_diffs_stay_small(tmp_path):
    path = tmp_path / "_ac_times.json"
    ac_times.record("15_3sum", 1, path=path)
    ac_times.record("1_two-sum", 2, path=path)

    assert list(json.loads(path.read_text(encoding="utf-8"))) == ["15_3sum", "1_two-sum"]


def test_a_corrupt_index_is_an_error_rather_than_silent_data_loss(tmp_path):
    path = tmp_path / "_ac_times.json"
    path.write_text("{ not json", encoding="utf-8")

    with pytest.raises(ValueError):
        ac_times.load(path)


def test_folder_for_slug_matches_on_the_slug_after_the_number():
    folders = ["1_two-sum", "15_3sum", "42_trapping-rain-water"]
    assert ac_times.folder_for_slug("3sum", folders) == "15_3sum"
    assert ac_times.folder_for_slug("trapping-rain-water", folders) == "42_trapping-rain-water"


def test_folder_for_slug_is_none_for_a_problem_not_downloaded_yet():
    assert ac_times.folder_for_slug("brand-new", ["1_two-sum"]) is None


def test_merge_recent_updates_a_problem_that_was_solved_again():
    index = {"15_3sum": 1_700_000_000}
    changed = ac_times.merge_recent(
        [{"titleSlug": "3sum", "timestamp": "1787184000"}], index, ["15_3sum"]
    )
    assert changed == 1
    assert index["15_3sum"] == 1_787_184_000


def test_merge_recent_never_moves_a_date_backwards():
    # The recent list is capped at 20 entries and can report an older pass
    # than the one already recorded. Taking it would make a problem look
    # staler than it is.
    index = {"15_3sum": 1_787_184_000}
    changed = ac_times.merge_recent(
        [{"titleSlug": "3sum", "timestamp": "1700000000"}], index, ["15_3sum"]
    )
    assert changed == 0
    assert index["15_3sum"] == 1_787_184_000


def test_merge_recent_records_a_problem_that_had_no_date():
    index = {}
    changed = ac_times.merge_recent(
        [{"titleSlug": "3sum", "timestamp": "1787184000"}], index, ["15_3sum"]
    )
    assert changed == 1
    assert index == {"15_3sum": 1_787_184_000}


def test_merge_recent_skips_problems_not_in_the_library():
    # A problem solved on LeetCode but not yet downloaded has no folder to
    # attach a date to. sync-new will pick it up and record it then.
    index = {}
    changed = ac_times.merge_recent(
        [{"titleSlug": "brand-new", "timestamp": "1787184000"}], index, ["1_two-sum"]
    )
    assert changed == 0
    assert index == {}
