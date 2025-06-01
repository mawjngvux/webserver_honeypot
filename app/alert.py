from flask import requests
from config.secrets import DISCORD_WEBHOOK_URL

def send_discord_alert(message: str):
    data = {
        "content": message
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        raise Exception(f"Failed to send Discord alert: {response.text}")