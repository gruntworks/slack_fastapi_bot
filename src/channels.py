import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

channels = {
    'test': os.getenv("SLACK_TEST_CHANNEL"),
}

def get_channel(channel_id: str) -> str or None:

    return channels[channel_id] or None
