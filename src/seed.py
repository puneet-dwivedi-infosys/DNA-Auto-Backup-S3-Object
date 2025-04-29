import os
from dotenv import load_dotenv
from services.s3_manager import S3Manager
from utils.constants import EXTERNAL_S3_DATA_BUCKET, LAMBDA_FUNCTION_HANDLER_FILE_NAME, CLOUD_FORMATION_TEMPLATE_NAME

# loading my environment variables
load_dotenv() 

# variables
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
DEFAULT_REGION = os.getenv("DEFAULT_REGION")


def seed():
    
    s3_mgr = S3Manager(access_key = ACCESS_KEY, secret_key = SECRET_KEY, region = DEFAULT_REGION)

    print("Uploading the cloud formation template and lambda zip to the s3.")

    # Creating the bucket 
    s3_mgr.create_bucket(EXTERNAL_S3_DATA_BUCKET)
    # disble public read of the bucket
    s3_mgr.disable_public_access_block(EXTERNAL_S3_DATA_BUCKET)

    # Checking if bucket created
    # print(s3_mgr.get_buckets())

    # uploading the cloud formation template and lambda fuction handler
    # getting the base directory 
    base_dir = os.getcwd()
    # upload cloud formation template for the task
    template_file_path = os.path.join(base_dir, "src", "partials", CLOUD_FORMATION_TEMPLATE_NAME)
    s3_mgr.upload_file(template_file_path, EXTERNAL_S3_DATA_BUCKET, CLOUD_FORMATION_TEMPLATE_NAME)
    
    # upload lambda handler function
    lambda_function_file_path = os.path.join(base_dir, "src", "partials", LAMBDA_FUNCTION_HANDLER_FILE_NAME)
    s3_mgr.upload_file(lambda_function_file_path, EXTERNAL_S3_DATA_BUCKET, LAMBDA_FUNCTION_HANDLER_FILE_NAME)
    
    
    # allow public read
    s3_mgr.add_public_read_object_policy(EXTERNAL_S3_DATA_BUCKET, CLOUD_FORMATION_TEMPLATE_NAME)
    s3_mgr.add_public_read_object_policy(EXTERNAL_S3_DATA_BUCKET, LAMBDA_FUNCTION_HANDLER_FILE_NAME)

    print("Uploaded Successfully........")
seed()