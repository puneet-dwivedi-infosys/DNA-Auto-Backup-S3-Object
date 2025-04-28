# default region 
DEFAULT_REGION = "ap-south-1"

# this bucket using for the keeping my dependent data like my cloud formation template 
EXTERNAL_S3_DATA_BUCKET = "project-partials-1745563858254"

# name of my cloud formation template
CLOUD_FORMATION_TEMPLATE_NAME = "s3-object-backup-cft.yml"

# lambda function handler
LAMBDA_FUNCTION_HANDLER_FILE_NAME = "lambda-handler.zip"

# Main Bucket Name
MAIN_S3_BUCKET = "main-bucket-1745580594020"

# Backup Bucket Name
BACKUP_S3_BUCKET = "backup-bucket-1745580594020"

# Auto Backup S3 Obect Cloud formation stack name
AUTO_BACKUP_S3_OBJECT_CLOUD_FORMATION_STACK_NAME = "auto-backup-s3-object-stack"

# Auto Backup S3 Obect Cloud formation template url
AUTO_BACKUP_S3_OBJECT_CLOUD_FORMATION_STACK_TEMPLATE_URL = f"https://{EXTERNAL_S3_DATA_BUCKET}.s3.{DEFAULT_REGION}.amazonaws.com/{CLOUD_FORMATION_TEMPLATE_NAME}"