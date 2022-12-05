"""Module for database actions"""
from init import db, Reference

class Services:
    """Class for database actions"""
    def __init__(self) -> None:
        pass


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
        db.session.add(new)  # pylint: disable=no-member
        db.session.commit()  # pylint: disable=no-member


    def get_db_contents(self):
        """Get references from database"""
        return Reference.query.all()
