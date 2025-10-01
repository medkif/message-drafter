import requests, os
from dotenv import load_dotenv
from pathlib import Path

# Try to load .env file if it exists (local dev)
# Otherwise, will be gotten from GitHub Secrets
env_path = Path(__file__).resolve().parent.parent / "secrets.env"
if env_path.exists():
    load_dotenv(env_path)

BOT_TOKEN      = os.getenv('BOT_TOKEN') # Telegram bot token
CHAT_ID        = os.getenv('CHAT_ID') # Telegram chat ID

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("Missing BOT_TOKEN or CHAT_ID. Make sure env vars are set.")

def send_to_telegram(message: str, bot_token: str = BOT_TOKEN, chat_id: str = CHAT_ID):
    """
    Send a message to a Telegram chat.

    Args:
        message (str): The text message to send.
        bot_token (str): Telegram bot token.
        chat_id (str): The chat ID (user, group, or channel).

    Returns:
        requests.Response: The response object from Telegram API.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Raise error for HTTP failures
        return response
    except requests.RequestException as e:
        print(f"Error sending message: {e}")
        return None