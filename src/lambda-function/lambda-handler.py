import json
import boto3

# variables
BACKUP_S3_BUCKET = "backup-bucket-1745822612793"

# backup object funtion 
def backup_object(source_bucket, object_key, backup_bucket):
    # initializing s3 client
    s3 = boto3.client("s3")
    try:
        copy_source = { 'Bucket' : source_bucket, 'Key' : object_key }
        response = s3.copy_object(CopySource = copy_source, 
                                  Bucket = backup_bucket, 
                                  Key = object_key)
    except Exception as e:
        print("Error Occured ", e)
        return False
    return True


def handler(event, context):
    
    # taking the bucket 
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    backup_bucket = BACKUP_S3_BUCKET

    print(source_bucket, object_key, backup_bucket)

    # performing backup task
    backup_object(source_bucket, object_key, backup_bucket)

    return {
        'statusCode': 200,
        'body': json.dumps('Object BackUp Successful')
    }