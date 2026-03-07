from sqlalchemy.orm import Session
from models.book import Book
from schemas import BookCreate, BookRead, BookUpdate

def list_Books(db: Session):
    """
    Return a list of all books in the database.

    Args:
        db: Database session.

    Returns:
        List of Book objects.
    """
    return db.query(Book).all()

def create_book(db: Session, book_data:BookCreate):
    """
    Create a new book in the database.

    Args:
        db: Database session.
        book_data: Data for the new book (should be a BookCreate schema).

    Returns:
        The created Book object.
    """
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        rating=book_data.rating
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_book_by_id(db: Session, book_id: int):
    """
    Retrieve a book by its ID.

    Args:
        db: Database session.
        book_id: ID of the book to retrieve.

    Returns:
        The Book object if found, otherwise None.
    """
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_data: BookUpdate):
    """
    Update an existing book in the database.

    Args:
        db: Database session.
        book_id: ID of the book to update.
        book_data: Updated data for the book (should be a BookUpdate schema).

    Returns:
        The updated Book object if found and updated, otherwise None.
    """
    book = get_book_by_id(db, book_id)
    if not book:
        return None
    
    if book_data.title is not None:
        book.title = book_data.title
    
    if book_data.author is not None:
        book.author = book_data.author

    if book_data.rating is not None:
        book.rating = book_data.rating

    db.commit()
    db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    """
    Delete a book from the database.

    Args:
        db: Database session.
        book_id: ID of the book to delete.

    Returns:
        True if the book was deleted, False otherwise.
    """
    book = get_book_by_id(db, book_id)
    if not book:
        return False

    db.delete(book)
    db.commit()
    return True