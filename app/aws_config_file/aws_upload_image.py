from fastapi import File, UploadFile, HTTPException
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os

from dotenv import load_dotenv



load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_IMAGE_FOLDER = os.getenv("S3_IMAGE_FOLDER")

# Create S3 client
s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


async def upload_image(file: UploadFile = File(...)):
    try:
        file_extension = os.path.splitext(file.filename)[1].lower()
        if file_extension.lower() not in [".jpg", ".jpeg", ".png", ".gif"]:
            raise HTTPException(status_code=400, detail="Unsupported file type.")

        s3_key = f"{S3_IMAGE_FOLDER}{file.filename}"  

        s3_client.upload_fileobj(
            file.file,
            S3_BUCKET_NAME,
            s3_key,
            ExtraArgs={"ContentType": file.content_type}  # Make public if needed
        )

        file_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"
        return {"message": "Image uploaded successfully", "url": file_url}

    except (BotoCoreError, ClientError) as e:
        raise HTTPException(status_code=500, detail=str(e))



