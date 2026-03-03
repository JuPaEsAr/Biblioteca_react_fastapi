from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BookBase(BaseModel):
    """
    Esquema base con campos comunes a creación y actualización.
    Incluye validaciones de datos.
    """

    title: str = Field(..., min_length=1, description="Book title")
    author: str = Field(..., min_length=1, description="Book author")
    rating: int = Field(
        ..., ge=1, le=5,
        description="Book rating from 1 to 5"
    )

    # Validación adicional opcional
    @field_validator("title", "author")
    def no_vacios(cls, value):
        if not value.strip():
            raise ValueError("This field cannot be empty")
        return value


class BookCreate(BookBase):
    """
    Sketch to create a new book.
    Inherits all fields and validations from BookBase.
    """
    pass


class BookUpdate(BaseModel):
    """
    Sketch to update an existing book.
    All fields are optional, but if provided, must pass the same validations as BookBase.
    """

    title: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1)
    rating: Optional[int] = Field(None, ge=1, le=5)

    @field_validator("title", "author")
    def no_vacios_opcional(cls, value):
        if value is not None and not value.strip():
            raise ValueError("This field cannot be empty")
        return value


class BookRead(BaseModel):
    """
    Sketch to read a book from the database.
    Includes the ID and allows returning ORM objects directly.
    """

    id: int
    title: str
    author: str
    rating: int

    # Allow returning ORM objects directly
    model_config = {
        "from_attributes": True
    }
