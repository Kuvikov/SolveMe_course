POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "body": {"type": "string"},
        "postId": {"type": "number"},
    },
    "required": ["body"]
}

#{'id': 1, 'body': 'some comment', 'postId': 1}