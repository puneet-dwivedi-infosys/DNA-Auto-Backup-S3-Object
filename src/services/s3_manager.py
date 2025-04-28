import boto3
import json

class S3Manager():

    def __init__(self, access_key, secret_key, region='ap-south-1'):
        """
        Initializes the S3Manager with AWS credentials and creates an S3 client.

        :param access_key: AWS Access Key ID
        :param secret_key: AWS Secret Access Key
        :param region: AWS region name (default is 'ap-south-1')
        """
        self.__session = boto3.session.Session(
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_key,
                            region_name = region
                            )
        self.s3 = self.__session.client("s3")

    def get_buckets(self):
        """Returns a list of all S3 bucket names."""
        try:
            response = self.s3.list_buckets()
            buckets = [bucket['Name'] for bucket in response['Buckets']]
            return buckets
        except Exception as e:
            print(f"Error fetching buckets: {e}")
            return []
        
    def create_bucket(self, bucket_name):
        try:
            location = {'LocationConstraint': self.s3.meta.region_name}
            response = self.s3.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = location)
            return True
        except Exception as e:
             print(f"Error creating bucket: {e}")
             return False

    def upload_file(self, file_path, bucket_name, object_key, ExtraArgs={}):
        """
        Uploads a file from local storage to the specified S3 bucket.

        :param file_path: Path to the local file
        :param bucket_name: Target S3 bucket
        :param object_key: Optional S3 object key (defaults to file name)
        """
        try:
            self.s3.upload_file(file_path, bucket_name, object_key, ExtraArgs = ExtraArgs)
            return True
        except Exception as e :
            print(f"Error uploading object {e}")
            return False

    def add_public_read_object_policy(self, bucket_name, object_key):
        
        # Define the bucket policy
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid" : "AllowPublicRead",
                    "Effect" : "Allow",
                    "Action" : "s3:GetObject",
                    "Resource" : f"arn:aws:s3:::{bucket_name}/{object_key}",
                    "Principal" : "*"
                }
            ]
        }
        
        # Convert the policy to JSON string format
        policy_string = json.dumps(bucket_policy)
        
        try:
            # Attach the policy to the bucket
            self.s3.put_bucket_policy(Bucket=bucket_name, Policy=policy_string)
            return True
        except Exception as e:
            print(f"Error adding bucket policy: {e}")
    
    def disable_public_access_block(self, bucket_name):
        try:
            self.s3.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': False,  # Allow public ACLs
                    'IgnorePublicAcls': False,  # Allow public ACLs
                    'BlockPublicPolicy': False,  # Allow public policies
                    'RestrictPublicBuckets': False  # Allow unrestricted public access
                }
            )
        except Exception as e:
            print("Error in putting bucket public access block", e)