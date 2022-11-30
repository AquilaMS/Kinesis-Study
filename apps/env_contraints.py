import os 
import boto3


access_key = os.environ.get('AWS_ACCESS_KEY')
secret_key = os.environ.get('AWS_ACCESS_SECRET_KEY')
stream_name = os.environ.get('AWS_STREAM_NAME')

fake_user_api_url = 'https://randomuser.me/api/'

#loads kinesis client with keys
client = boto3.client(
    'kinesis', 
    aws_access_key_id = access_key, 
    aws_secret_access_key = secret_key, 
    region_name = 'us-east-1')