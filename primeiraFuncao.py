import json
from log import *

def lambda_handler(event, context):
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
