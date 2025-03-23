import json
from log import *

def lambda_handler(event, context):
    # TODO implement
    log("Log INFO event: ", event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'event': json.dumps(event)
    }
