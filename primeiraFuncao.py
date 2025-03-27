import json
from log import *
import boto3

def lambda_handler(event, context):
    return handle_s3(event, context)

def lambda_handler_bkp(event, context):
    # TODO implement
    log(event)

    return {
        'statusCode': 200,
        'body': {
            "status":"success",
            "data":"Hello from Lambda",
        },
        'event': event,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

def handle_s3(event, context):
    s3_client = boto3.client('s3', region_name='us-east-1')

    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    object_key = record['s3']['object']['key']

    response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
    content_length = response['ContentLength']
    mega_bytes = 1024 * 1024

    if content_length > mega_bytes:
        log("Objeto muito grande")

        return {
            'statusCode': 413,
            'body': json.dumps({
                "status":"error",
                "message": "File is too large"
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    else:
        log("Objeto de tamanho OK")

        return {
            'statusCode': 200,
            'body': json.dumps({
                "status":"success",
                "message": "File is ok"
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }