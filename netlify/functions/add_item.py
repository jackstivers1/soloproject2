import json
import os

def handler(event, context):
    path = os.path.join(os.path.dirname(__file__), "data.json")
    new_item = json.loads(event["body"])

    with open(path, "r") as f:
        items = json.load(f)

    items.append(new_item)

    with open(path, "w") as f:
        json.dump(items, f, indent=2)

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"success": True})
    }
