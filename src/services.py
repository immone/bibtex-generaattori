"""Module for database actions"""
from init import Reference 


class Services:
    """Class for database actions"""
    def __init__(self, db) -> None:
        self.db = db

    def save_to_db(self, author: str, title: str, year: str):
        """Save form data to database."""
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
  
    def remove_from_db(self, ref_id: int):
        """Remove reference from database"""
        reference = Reference.query.filter_by(id=ref_id).one()
        self.db.session.delete(reference) # pylint: disable=no-member
        self.db.session.commit() # pylint: disable=no-member
