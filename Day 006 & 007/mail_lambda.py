import json
import boto3
import os
import uuid
from botocore.exceptions import ClientError

client = boto3.client('dynamodb')

def save_to_db(data):
    
    client_dynamo=boto3.resource('dynamodb')
    
    table_name = 'products'
    table=client_dynamo.Table(table_name)
    
    response=table.put_item(Item=data)
    
    return response

def lambda_handler(event, context):
    
    # data={'id':str(uuid.uuid4()),'title':'Classical Watch','price':50000,'image':'https://flutter-test-products.s3.amazonaws.com/watch.jpg'}

    # try:
    #     save_to_db(data)
    # except ClientError as e:
    #     print(e.response['Error']['Message'])
    
    
    table_name = 'products'
    data = client.scan(
    TableName=table_name
    )
    
    response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }
    
    return response
