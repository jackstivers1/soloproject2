import json, os

def handler(event, context):
    path = os.path.join(os.path.dirname(__file__), "data.json")
    body = json.loads(event["body"])
    delete_id = body["id"]

    with open(path, "r") as f:
        items = json.load(f)

    items = [item for item in items if item["id"] != delete_id]

    with open(path, "w") as f:
        json.dump(items, f, indent=2)

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"success": True})
    }
