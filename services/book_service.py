from sqlalchemy.orm import Session
from models.book import Book


def list_Books(db: Session):
    """
    Return a list of all books in the database.

    Args:
        db: Database session.

    Returns:
        List of Book objects.
    """
    return db.query(Book).all()
