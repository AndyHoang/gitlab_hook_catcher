import json
import os
from gitlab.payload.issue_event import IssueEventPayload

def test_parse_gitlab_webhook_payload():
    # Load the JSON payload from a file
    json_file_path = os.path.join(os.path.dirname(__file__),"testcase", "test_issue_event.json")
    with open(json_file_path, "r") as f:
        json_payload = f.read()

    # Parse the JSON payload into a GitLabWebhookPayload object
    webhook_payload = IssueEventPayload.parse_raw(json_payload)

    # Test that the parsed object is correct based on the input JSON
    assert webhook_payload.object_kind == "issue"
    # assert webhook_payload.ref == "ref/heads/feature/new-feature"
    assert webhook_payload.user.id == 1
    assert webhook_payload.user.name == "Administrator"
    assert webhook_payload.user.username == "root"
    print(webhook_payload.json())
    # etc.
