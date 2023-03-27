import os
import logging

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from gitlab.payload.issue_event import IssueEventPayload

app = FastAPI()

SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

slack_client = WebClient(token=SLACK_BOT_TOKEN)

@app.post("/gitlab-webhook")
async def handler(request: Request, response: Response):
  data = await request.json()
  webhook_payload = IssueEventPayload.parse_obj(data)
  message = webhook_payload.json()
  response = await send_to_slack(message)
  if response.status_code == 200:
    return JSONResponse(content={"success": True})
  else:
    return JSONResponse(content={"success": False})

async def send_to_slack(message: str):
  try:
    response = slack_client.chat_postMessage(
      channel=SLACK_CHANNEL,
      text=message
    )
    return response

  except SlackApiError as e:
    logging.error(e)
    raise e

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("app:app", host="0.0.0.0",
              reload=True, port=int(os.environ.get("PORT", 8080)))
