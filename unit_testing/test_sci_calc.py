from sci_calc import *
import pytest


def test_find_sqrt():
    assert find_sqrt(100) == 10

@pytest.mark.skip("WIP") # decorator that skips following test
def test_find_ceil():
    assert find_ceil(3.14) == 4
