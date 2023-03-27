from fastapi.testclient import TestClient
import json
import os

# Import FastAPI app to test
from app import app as _app

def test_call_api():
    # Load data from file
    json_file_path = os.path.join(os.path.dirname(__file__),"data.json")
    with open(json_file_path, "r") as file:
        data = json.load(file)
    # Create a TestClient instance
        client = TestClient(_app)

        # Make the request and get the response
        response = client.post(
            "/gitlab-webhook",
            headers={
                "Content-Type": "application/json",
                "X-Gitlab-Event": "Push Hook",
            },
            json=data,
        )
        __import__('pdb').set_trace()
        assert response.status_code == 200
