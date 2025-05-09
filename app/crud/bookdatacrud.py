from sqlalchemy.orm import Session
from ..models.models import Book


def Create_book(request, db:Session,  current_user ):
    db_book = Book(
    title=request.title,
    author=request.author,
    price=request.price,
    creator_id=current_user.user_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book