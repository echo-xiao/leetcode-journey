from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def lingshen_sample() -> str:
    return (FIXTURES / "lingshen_sample.md").read_text(encoding="utf-8")


@pytest.fixture
def fupan_easy_sample() -> str:
    return (FIXTURES / "fupan_easy_sample.txt").read_text(encoding="utf-8")


@pytest.fixture
def fupan_medium_sample() -> str:
    return (FIXTURES / "fupan_medium_sample.txt").read_text(encoding="utf-8")


@pytest.fixture
def fixture_problems() -> Path:
    """Two synthetic problems covering the export edge cases.

    Synthetic rather than copied from Problems/, because the real library
    grows every week and would make these tests fail on unrelated days.
    """
    return FIXTURES / "problems"
