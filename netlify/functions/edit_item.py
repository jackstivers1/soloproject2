import json, os

def handler(event, context):
    path = os.path.join(os.path.dirname(__file__), "data.json")
    update = json.loads(event["body"])

    with open(path, "r") as f:
        items = json.load(f)

    for item in items:
        if item["id"] == update.get("id"):
            for key in ["name", "date", "genre", "author"]:
                if update.get(key):
                    item[key] = update[key]

    with open(path, "w") as f:
        json.dump(items, f, indent=2)

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"success": True})
    }
