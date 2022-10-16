#!/usr/bin/python3
import json, boto3

def lambda_handler(event, context):
    G_ID = 'Security_Group_ID'
    Event_name = 'AuthorizeSecurityGroupIngress'
    RULE_ID = event['detail']['responseElements']['securityGroupRuleSet']['items'][0]['securityGroupRuleId']

    if( event['detail']['eventName'] == Event_name and event['detail']['requestParameters']['groupId'] == G_ID ):
       client = boto3.client('ec2')
       response = client.revoke_security_group_ingress(
            GroupId = G_ID,
            SecurityGroupRuleIds=[
              RULE_ID,
            ]
         )
       client = boto3.client('sns')
       response = client.publish(
           TargetArn='Topic_Arn_Address',
           Message=json.dumps({'default': json.dumps('Security Group Rule Has Been Revoked')}),
           MessageStructure='json'
           )
           

