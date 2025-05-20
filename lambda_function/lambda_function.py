import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.info("File uploaded event received.")
    print("Event data ----->", event)

    try:
        key = event['Records'][0]['s3']['object']['key']
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        destination_bucket = os.environ['BOOKSTORE_FINAL_BUCKET']

        logger.info(f"Moving '{key}' from '{source_bucket}' to '{destination_bucket}'")

        # Step 1: Copy the object
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)
        logger.info(" File copied successfully.")

        # # Step 2: Delete the original
        # s3.delete_object(Bucket=source_bucket, Key=key)
        # logger.info(" Original file deleted from source bucket.")

    except Exception as e:
        logger.error(" Error during file transfer:")
        logger.error(str(e))





