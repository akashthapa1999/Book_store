from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse


from ..schemas.schemas import BookRead, BookCreate
from ..models.models import Book
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from ..auth.services.outh2 import get_current_user
from ..schemas.schemas import UserCreate

from ..crud.bookdatacrud import Create_book

router = APIRouter(prefix="/books", tags=["BookData"])


@router.post("/", response_model=BookRead)
def createBook(
    request: BookCreate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_user),
):
    return Create_book(request, db , current_user)


@router.get("/", response_model=List[BookRead])
def read_books(
    db: Session = Depends(get_db), current_user: UserCreate = Depends(get_current_user)
):
    return db.query(Book).all()


@router.get("/{id}", response_model=BookRead)
def book_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_user),
):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/book/{id}")
def update_book(
    id: int,
    request: BookCreate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_user),
):
    # breakpoint()
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = request.title
    book.author = request.author
    book.price = request.price
    db.commit()
    db.refresh(book)
    return book


@router.delete("/books/{id}")
def delete_book(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_user),
):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return JSONResponse(
        content={"message": "Book deleted successfully"}, status_code=200
    )
