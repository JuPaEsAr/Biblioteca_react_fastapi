from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.book_service import list_Books, create_book, get_book_by_id, update_book
from schemas import BookRead, BookCreate, BookUpdate

# Create a router for book-related endpoints
router = APIRouter(
    prefix="/api/books",
    tags=["Books"]
)

@router.get("/", response_model=List[BookRead])
def get_books_endpoint(db: Session = Depends(get_db)):
    """
    Endpoint that retrieves a list of all books from the database. 
    It uses the `list_Books` function from the `book_service` to fetch the data and returns it as a list of `BookRead` models.
    """
    books = list_Books(db)
    return books

@router.post("/", response_model=BookRead, status_code=201)
def create_book_endpoint(book_data: BookCreate, db: Session = Depends(get_db)):
    """
    Endpoint that creates a new book in the database. 
    It accepts a `BookCreate` model as input, which contains the data for the new book. 
    The endpoint uses the `create_book` function from the `book_service` to save the new book and returns the created book as a `BookRead` model.
    """
    new_book = create_book(db, book_data)
    return new_book

@router.get("/{book_id}", response_model=BookRead)
def get_book_by_id_endpoint(book_id: int = Path(...,gt=0,description="ID of the book to fetch"), db: Session = Depends(get_db)):
    """
    Endpoint that retrieves a book by its ID. 
    It uses the `get_book_by_id` function from the `book_service` to fetch the book. 
    If the book is found, it returns it as a `BookRead` model; otherwise, it raises a 404 HTTP exception.
    """
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookRead, status_code=200)
def update_book_endpoint(book_id: int = Path(...,gt=0,description="ID of the book to update"), book_data: BookUpdate = None, db: Session = Depends(get_db)):
    """
    Endpoint that updates an existing book in the database. 
    It accepts a `BookUpdate` model as input, which contains the updated data for the book. 
    The endpoint uses the `update_book` function from the `book_service` to perform the update. 
    If the book is found and updated successfully, it returns the updated book as a `BookRead` model; otherwise, it raises a 404 HTTP exception.
    """
    updated_book = update_book(db, book_id, book_data)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book