import pytest


@pytest.mark.sanity
def test_sample_tc__4():
    marks = [1, 2, 4]
    assert len(marks) == 0
