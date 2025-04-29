import os

from utils.constants import AUTO_BACKUP_S3_OBJECT_CLOUD_FORMATION_STACK_NAME, AUTO_BACKUP_S3_OBJECT_CLOUD_FORMATION_STACK_TEMPLATE_URL
from services.cloud_formation_stack import CloudFormationClient, CloudFormationStack

def main():
    
    ''' Loading the env variables '''
    ACCESS_KEY = os.getenv("ACCESS_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEFAULT_REGION = os.getenv("DEFAULT_REGION")

    '''Creating the CloudFormation client with aws credentials '''
    cf_client = CloudFormationClient(ACCESS_KEY, SECRET_KEY, DEFAULT_REGION).get_cf_client()
    

    ''' Deploying Cloud Formation stack '''
    template_parameters = [
        {
            'ParameterKey': 'MainS3BucketName',
            'ParameterValue': 'main-bucket-1745822612793',
        },
        {
            'ParameterKey': 'BackupS3BucketName',
            'ParameterValue': 'backup-bucket-1745822612793',
        }
    ]

    cf_stack = CloudFormationStack(
        stack_name = AUTO_BACKUP_S3_OBJECT_CLOUD_FORMATION_STACK_NAME,
        template_url = AUTO_BACKUP_S3_OBJECT_CLOUD_FORMATION_STACK_TEMPLATE_URL,
        parameters = template_parameters,
        cf_client = cf_client
    )

    cf_stack.deploy()