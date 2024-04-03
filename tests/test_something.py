import requests

from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from jsonschema import validate

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    response_posts = response.json()
    print(response_posts)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(response_posts) == 2, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    validate(response_posts)

## [{'id': 1, 'body': 'some comment', 'postId': 1}, {'id': 2, 'body': 'some comment', 'postId': 1}]