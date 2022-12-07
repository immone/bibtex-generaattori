"""Tests for reference list functionality."""
from os import remove, path
from init import app, db, Reference
from services import Service

class TestReferenceList:
    """Tests for reference list functionality."""
    def setup_method(self):
        """Pytest setup method"""
        self.services = Service(db) # pylint: disable=attribute-defined-outside-init

    def test_db_write_and_read(self):
        """Test adding a reference to the database and reading references."""
        with app.app_context():
            self.services.save_to_db("Very Real", "Test Data", "2022")
            assert self.services.get_db_contents() == [
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
            assert len(self.services.get_db_contents()) == 1
            self.services.remove_from_db(1)
            references = self.services.get_db_contents()
            assert references == []

    def test_create_file(self):
        """Test bibtex-file is created and is correct"""
        with app.app_context():
            self.services.save_to_db("Very Real", "Test Data", "2022")
            self.services.create_bibtex_file()
            assert path.isfile('references.bib')

            with open('references.bib', 'r', encoding='utf-8') as file:
                bibtex_file = file.read().strip()
                should_be = (
                    '@InCollection{1Real2022,author={Very Real},'
                    'title={Test Data},'
                    'booktitle={},year={2022}}'
                ).strip()

                assert bibtex_file == should_be


def teardown_module():
    """Pytest test suite teardown."""
    remove('src/instance/test.db')
