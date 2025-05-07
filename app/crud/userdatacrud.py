from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.models import User
from ..auth.services.hashing import Hashing_class
from fastapi.responses import JSONResponse


def get_all_user(db:Session):
    data = db.query(User).all()
    if not data:
        raise HTTPException(status_code=404, detail="User not found") 
    return data



def Create_user_data(request, db:Session):
    new_user = User(
        name=request.name,
        email=request.email,
        password= Hashing_class.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(id, db:Session):
    user = db.query(User).filter(User.id == id ).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

def Update_user_data(id, request, db:Session):
    user_id = db.query(User).filter(User.id==id).first()
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_id.email = request.email
    user_id.name = request.name
    user_id.password = request.password
    db.commit()
    db.refresh(user_id)
    return user_id


def Delete_user_data(id, db:Session):
    user_id = db.query(User).filter(User.id==id).first()
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user_id)
    db.commit()

    return JSONResponse(content={"message": "User deleted successfully"}, status_code=200)