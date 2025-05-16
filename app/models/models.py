from sqlalchemy import Column, Integer, String,ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String, index=True, nullable=False)

    bookdata = relationship("Book", back_populates="creator")


    
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    price = Column(Integer, nullable=True)
    image = Column(String)  

    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    creator = relationship("User", back_populates="bookdata")
    images = relationship("Image", back_populates="book")



class Image(Base):
    __tablename__ = "images"  # Plural for consistency
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    book = relationship("Book", back_populates="images")
    
    


 
 
