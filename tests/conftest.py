from pathlib import Path

import pytest


@pytest.fixture
def samplefile() -> Path:
    return Path(__file__).parent.parent / "samples" / "oref.results.json"
