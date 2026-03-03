from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.book_service import list_Books, create_book
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