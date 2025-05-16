from sqlalchemy.orm import Session
from ..models.models import Book
from fastapi import HTTPException
from ..aws_config_file.aws_upload_image import upload_image
from ..schemas.schemas import ImageUploadResponse
from pydantic import ValidationError


async def Create_book(request, image, db:Session,  current_user ):
    try:
        raw_response = await upload_image(image)
        image_response = ImageUploadResponse(**raw_response)  
        image_url = str(image_response.url)
    except ValidationError as ve:
        raise HTTPException(status_code=500, detail=f"Invalid upload response: {ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image upload failed: {str(e)}")
    
    db_book = Book(
    title=request.title,
    author=request.author,
    price=request.price,
    image = image_url,
    creator_id=current_user.user_id,

    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book