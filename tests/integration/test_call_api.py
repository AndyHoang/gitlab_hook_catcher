import requests
import json
import os

url = "https://0265-2001-ee0-500f-2010-c8b4-7b15-e4e8-ef21.ap.ngrok.io/gitlab-webhook"
headers = {
    "Content-Type": "application/json",
    "X-Gitlab-Event": "Push Hook"
}


def test_call_api():
    json_file_path = os.path.join(os.path.dirname(__file__),"data.json")
    with open(json_file_path, "r") as file:
        data = json.load(file)
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200

