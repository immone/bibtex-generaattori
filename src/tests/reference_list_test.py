"""Tests for reference list functionality."""
from os import remove
from init import Reference, app
from services import Services

class TestReferenceList:
    """Tests for reference list functionality."""
    def setup_method(self):
        """Pytest setup method"""
        self.svcs = Services() # pylint: disable=attribute-defined-outside-init

    def test_db_write_and_read(self):
        """Test adding a reference to the database and reading references."""
        with app.app_context():
            self.svcs.save_to_db("Very Real", "Test Data", "2022")
            assert self.svcs.get_db_contents() == [
                Reference(
                    id=1,
                    author='Very Real',
                    title='Test Data',
                    year=2022,
                    type_id=1
                )
            ]

    def test_db_remove_entry(self):
        """Test removing a reference from the database."""
        with app.app_context():
            assert len(self.svcs.get_db_contents()) == 1
            self.svcs.remove_from_db(1)
            references = self.svcs.get_db_contents()
            assert references == []

def teardown_module():
    """Pytest test suite teardown."""
    remove('src/instance/test.db')
