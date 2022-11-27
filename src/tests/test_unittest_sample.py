import pytest

def func(x):
    return x + 1

def func_raises():
    raise ValueError

# All program behavior other than exceptions can be tested with assert
# The test below is an example of how failing tests look in pytest output
def test_wrong_answer():
    assert func(3) == 5

def test_answer():
    assert func(3) == 4

# Exceptions can be tested with pytest.raises blocks
def test_exception():
    with pytest.raises(ValueError):
        func_raises()
