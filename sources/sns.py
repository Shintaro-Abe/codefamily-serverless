import json
import os
import boto3

snscli = boto3.client('sns')

def handler(event, context):
    Body = json.loads(event['body'])
    Sub = Body["sub"]
    Mes = Body["mes"]
    
    response = snscli.publish(
        TopicArn = os.environ["topic"],
        Subject = Sub,
        Message = Mes)
    print(response)
    
    text = "Subject: " + Sub + " Message: " + Mes
    return {
        'statusCode': 200,
        'body': text
    }