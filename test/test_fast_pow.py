from src.fast_pow import fastPow
import pytest


def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1

def test_negative_power():
    with pytest.raises(ValueError):
        fastPow(2, -3)