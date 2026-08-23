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
