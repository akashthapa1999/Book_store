from fastapi import APIRouter, Depends
from ..schemas.schemas import UserCreate, ShowUser
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

from ..crud.userdatacrud import (
    get_all_user,
    Create_user_data,
    # get_user_by_id,
    # Update_user_data,
    # Delete_user_data,
)


router = APIRouter(prefix="/User", tags=["UserData"])


@router.post("/")
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return Create_user_data(request, db)


@router.get("/", response_model=List[ShowUser])
def show_user(db: Session = Depends(get_db)):
    return get_all_user(db)


# @router.get("/{id}", response_model=ShowUser)
# def show_user_id(id: int, db: Session = Depends(get_db)):
#     return get_user_by_id(id, db)


# @router.put("/user/{id}", response_model=ShowUser)
# def update_user(id: int, request: UserCreate, db: Session = Depends(get_db)):
#     return Update_user_data(id, request, db)


# @router.delete("/{id}")
# def delete_user(id: int, db: Session = Depends(get_db)):
#     return Delete_user_data(id, db)
