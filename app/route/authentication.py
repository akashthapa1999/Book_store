from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..models.models import User
from ..auth.services.hashing import Hashing_class
from ..auth.services.JwtToken import create_access_token

from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"])



@router.post("/login")
def login(request:OAuth2PasswordRequestForm =Depends(), db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not Hashing_class.verify_password(request.password, user.password):
        raise HTTPException(status_code=404, detail="Incorrect Password")
    
    access_token = create_access_token(
        data={"sub": user.email, "id":user.id})
    return {"access_token":access_token, "token_type":"bearer"}






@router.post("/logout")
def logout():
    pass