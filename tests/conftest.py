from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def lingshen_sample() -> str:
    return (FIXTURES / "lingshen_sample.md").read_text(encoding="utf-8")
