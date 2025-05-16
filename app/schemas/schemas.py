from pydantic import BaseModel, HttpUrl
from typing import Optional, List



class ImageUploadResponse(BaseModel):
    message: str
    url: HttpUrl

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
        from_attributes = True

class ShowUserWithoutBood(BaseModel):
    id : int
    email : str
    name : str
    
    class Config:
        from_attributes = True




class ShowUser(BaseModel):
    id : int
    email : str
    name : str
    bookdata : List[ShowBookRead] = []

    class Config:
        from_attributes = True


class BookRead(BaseModel):
    id: int
    title: str
    author: str
    price: Optional[int] = None
    creator: ShowUserWithoutBood

    class Config:
        from_attributes = True




class Login(BaseModel):
    email : str
    password : str