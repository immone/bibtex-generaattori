"""App tests."""
import pytest
from init import Reference, Type, app # pylint: disable=unused-import


class TestReference:
    """Tests for reference class."""
    def test_all_data_valid_to_bibtex(self):
        """Test that bibtex generation works with all fields."""
        reference = Reference(
            id=1,
            author='Mikko Mallikas',
            title='Ohjelmointi',
            booktitle='Tietokoneiden salat',
            year=2022,
            type_id=1
        )
        with app.app_context():
            assert (reference.to_bibtex() ==
                    '@InCollection{1Mallikas2022,author={Mikko Mallikas},'
                    'title={Ohjelmointi},booktitle={Tietokoneiden salat},'
                    'year={2022}}')

    def test_all_nullable_values_as_null_to_bibtex(self):
        """Test that None values are output as empty string."""
        reference = Reference(type_id=1)
        with app.app_context():
            assert (reference.to_bibtex() == '@InCollection{,author={},'
                    'title={},booktitle={},year={}}')

    def test_book_type_to_bibtex(self):
        """Test that boot type is converted correctly."""
        reference = Reference(type_id=2)
        with app.app_context():
            assert (reference.to_bibtex() == '@Book{,author={},'
                    'title={},booktitle={},year={}}')

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
