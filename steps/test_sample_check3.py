import time
import pytest


@pytest.mark.sanity
def test_sample_tc__5():
    print("hello test 3")
    marks = [1, 2, 4]
    assert len(marks) != 0
