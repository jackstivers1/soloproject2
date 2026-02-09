import json
import os

def handler(event, context):
    path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(path, "r") as f:
        data = json.load(f)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(data)
    }
