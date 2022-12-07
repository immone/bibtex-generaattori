"""Module for database actions"""
from init import Reference 

class Services:
    """Class for database actions"""
    def __init__(self, db) -> None:
        self.db = db


    def save_to_db(self, author, title, year):
        """Save form data to database."""
        print('Save to db', author, title, year)
        new = Reference(
            author=author,
            title=title,
            booktitle=None,
            year=year,
            type_id=1
        )
        self.db.session.add(new)  # pylint: disable=no-member
        self.db.session.commit()  # pylint: disable=no-member


    def get_db_contents(self):
        """Get references from database"""
        return Reference.query.all()

    def create_bibtex_file(self) -> None:
        """Create bibtex file for upload."""
        references = Reference.query.all()
        text = ''
        for reference in references:
            text += reference.to_bibtex() + '\n\n'

        with open('references.bib', 'w') as file:
            file.write(text)

    