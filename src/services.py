"""Module for database actions"""
from init import Reference


class Service:
    """Class for database actions"""
    def __init__(self, database) -> None:
        self.database = database

    def save_reference(self, author: str, title: str, year: str):
        """Save form data for inCollection type to database."""
        new = Reference(
            author=author,
            title=title,
            year=year,
            type_id=1
        )
        self.database.session.add(new)  # pylint: disable=no-member
        self.database.session.commit()  # pylint: disable=no-member

    def save_reference_book(
        self, author: str, title: str, year: str, booktitle: str,
        pagenumber: str
    ): # pylint: disable=too-many-arguments
        """Save form data book type to database."""
        new = Reference(
            author=author,
            title=title,
            booktitle=booktitle,
            year=year,
            pagenumber=pagenumber,
            type_id=2
        )
        self.database.session.add(new)  # pylint: disable=no-member
        self.database.session.commit()  # pylint: disable=no-member

    def get_all_references(self):
        """Get references from database"""
        return Reference.query.all()

    def create_bibtex_file(self) -> None:
        """Create bibtex file for upload."""
        references = Reference.query.all()
        text = ''
        for reference in references:
            text += reference.to_bibtex() + '\n\n'

        with open('references.bib','w', encoding='utf-8') as file:
            file.write(text)

    def delete_reference(self, ref_id: int):
        """Remove reference from database"""
        reference = Reference.query.filter_by(id=ref_id).one()
        self.database.session.delete(reference) # pylint: disable=no-member
        self.database.session.commit() # pylint: disable=no-member
