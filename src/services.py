"""Module for database actions"""
from init import db, Reference

class Services:
    """Class for database actions"""
    def __init__(self) -> None:
        pass


    def save_to_db(self, author: str, title: str, year: str):
        """Save form data to database."""
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

    def remove_from_db(self, ref_id: int):
        """Remove reference from database"""
        reference = Reference.query.filter_by(id=ref_id).one()
        db.session.delete(reference) # pylint: disable=no-member
        db.session.commit() # pylint: disable=no-member
