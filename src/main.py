import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError

load_dotenv(dotenv_path='../.env')

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_SECRET = os.getenv("SLACK_SIGNING_SECRET")

# Initializes your app with your bot token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SECRET
)


# BOT EVENTS FROM THE SLACK
@app.event("app_mention")
def mention_handler(body, say):
    say(text="Leave me alone")


# CUSTOM REQUEST USING CHANNEL ID
def send_to_channel(channel_id: str, text: str, blocks: str = None, attachments: str = None) -> None:
    try:
        # Powered by SlackBolt
        result = app.client.chat_postMessage(
            channel=channel_id,
            blocks=blocks,
            text=text,
            attachments=attachments
        )
        logging.info(result)

    except SlackApiError as e:
        logging.error(f"Error posting message: {e}")


# Start your app
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
