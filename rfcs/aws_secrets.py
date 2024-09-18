import boto3
import json
from botocore.exceptions import ClientError

def get_aws_secret(secret_name, region_name="us-west-2"):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            return json.loads(get_secret_value_response['SecretString'])

# Usage
aws_secrets = get_aws_secret("your_secret_name")
