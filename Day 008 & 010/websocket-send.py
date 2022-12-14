import json
import boto3
import os

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    message = json.loads(event['body'])['message']
    paginator = dynamodb.get_paginator('scan')
    connectionIds = []

    apigatewaymanagementapi = boto3.client(
        'apigatewaymanagementapi', 
        endpoint_url = "https://" + event["requestContext"]["domainName"] + "/" + event["requestContext"]["stage"]
    )

    for page in paginator.paginate(TableName=os.environ['WEBSOCKET_TABLE']):
        connectionIds.extend(page['Items'])
        
    print(message)

    for connectionId in connectionIds:
        apigatewaymanagementapi.post_to_connection(
            Data=message,
            ConnectionId=connectionId['connection_id']['S']
        )

    return {}