from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.book_service import list_Books
from schemas import BookRead

# Create a router for book-related endpoints
router = APIRouter(
    prefix="/api/books",
    tags=["Libros"]
)

@router.get("/", response_model=List[BookRead])
def obtener_libros(db: Session = Depends(get_db)):
    """
    Endpoint that retrieves a list of all books from the database. 
    It uses the `list_Books` function from the `book_service` to fetch the data and returns it as a list of `BookRead` models.
    """
    books = list_Books(db)
    return books
