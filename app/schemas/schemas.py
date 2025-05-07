from pydantic import BaseModel
from typing import Optional, List




class UserCreate(BaseModel):
    email : str
    name : str
    password : str


class BookCreate(BaseModel):
    title: str
    author: str
    price: Optional[int] = None


class ShowBookRead(BaseModel):
    id: int
    title: str
    author: str
    price: Optional[int] = None
    
    class Config:
        orm_mode = True

class ShowUserWithoutBood(BaseModel):
    id : int
    email : str
    name : str
    
    class Config:
        orm_moda = True




class ShowUser(BaseModel):
    id : int
    email : str
    name : str
    bookdata : List[ShowBookRead] = []

    class Config:
        orm_mode = True


class BookRead(BaseModel):
    id: int
    title: str
    author: str
    price: Optional[int] = None
    creator: ShowUserWithoutBood

    class Config:
        orm_mode = True




class Login(BaseModel):
    email : str
    password : str