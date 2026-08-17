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
