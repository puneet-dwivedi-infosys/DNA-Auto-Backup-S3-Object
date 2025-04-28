import boto3
from utils.constants import DEFAULT_REGION


class CloudFormationClient:
    def __init__(self, access_key, secret_key, region = DEFAULT_REGION) :
        self.__session = boto3.session.Session(
                            aws_access_key_id = access_key,
                            aws_secret_access_key = secret_key,
                            region_name = region
                            )
        self.cf_client = self.__session.client("cloudformation")

    def get_cf_client(self):
        return self.cf_client


class CloudFormationStack:

    def __init__(self, stack_name, template_url, parameters, cf_client):
        self.stack_name = stack_name
        self.template_url = template_url
        self.parameters = parameters
        self.cf_client = cf_client

    def __create_stack(self):
        """Create a CloudFormation Stack"""

        response = self.cf_client.create_stack(
            StackName=self.stack_name,
            TemplateURL=self.template_url,
            Parameters=self.parameters,
            Capabilities=['CAPABILITY_NAMED_IAM'],
            OnFailure='DELETE'
        )
        return response

    def __update_stack(self):
        """Update an existing CloudFormation Stack"""

        response = self.cf_client.update_stack(
            StackName=self.stack_name,
            TemplateURL=self.template_url,
            Parameters=self.parameters,
            Capabilities=['CAPABILITY_NAMED_IAM'],
        )
        return response

    def deploy(self):
        """Deploys the stack by first checking if it exists and either creates or updates"""
        try:
            print(f"Initiating Creation of stack - {self.stack_name}")
            self.__create_stack()
            print("Stack Created Successfully.")

        except Exception as e:
            if "AlreadyExistsException" in str(e):
                print(f"Stack already exists - {self.stack_name}")
                try :
                    # update the stack
                    print(f"Updating the stack - {self.stack_name}")
                    self.__update_stack()
                    print("Stack updated Successfully.")
                except Exception as update_err :
                    if 'No updates are to be performed' in str(update_err) :
                        print("No updates are to be performed") 
                    else :
                        print(f"Error in updating stack {update_err}")
            else :
                print(f"Error in creating stack - {self.stack_name}, {e}")