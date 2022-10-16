#!/usr/bin/python3
import boto3
import json

client = boto3.client('sns')
response = client.publish(
    TargetArn='SNS_Topic_ARN',
    Message=json.dumps({'default': json.dumps('This is test From SNS')}),
    MessageStructure='json'
)
