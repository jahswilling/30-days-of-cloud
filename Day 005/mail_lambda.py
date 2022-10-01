import json
import boto3
from botocore.exceptions import ClientError
import datetime
import os
import urllib.parse 

def send_sns(message, subject):
    client = boto3.client("sns")
    topic_arn = os.environ["Sns_topic"]
    response = client.publish(
        TopicArn=topic_arn, Message=message, Subject=subject)
    return response
    
def save_to_db(data):
    
    client_dynamo=boto3.resource('dynamodb')
    
    table_name = os.environ["Table_name"]
    table=client_dynamo.Table(table_name)
    
    response=table.put_item(Item=data)
    
    return response

def lambda_handler(event, context):
    
    form_data = urllib.parse.parse_qs(event['body'])

    create_at = datetime.datetime.now()
    
    data = {
                'First-Name': form_data['firstname'][0],
                'Last-Name': form_data['lastname'][0],
                'email': form_data['email'][0],
                'country': form_data['country'][0],
                'subject': form_data['subject'][0],
                'create_at': create_at.strftime("%m/%d/%Y, %H:%M:%S")
            }
    
    try:
        save_to_db(data)
    except ClientError as e:
        print(e.response['Error']['Message'])
    
    try:
        send_sns(json.dumps(data),"testing")
    except ClientError as e:
        print(e.response['Error']['Message'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email successfully sent!')
    }