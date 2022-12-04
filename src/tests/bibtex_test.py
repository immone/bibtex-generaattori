"""App tests."""
import pytest


def func(number):
    """Add 1 to given number."""
    return number + 1

def func_raises():
    """Raise an error as example."""
    raise ValueError

# All program behavior other than exceptions can be tested with assert
# The test below is an example of how failing tests look in pytest output
#def test_wrong_answer():
    #assert func(3) == 5

def test_answer():
    """Test func return value."""
    assert func(3) == 4

# Exceptions can be tested with pytest.raises blocks
def test_exception():
    """Test raising an exception."""
    with pytest.raises(ValueError):
        func_raises()
