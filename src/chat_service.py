import requests, os
from dotenv import load_dotenv
from pathlib import Path

# Try to load .env file if it exists (local dev)
# Otherwise, will be gotten from GitHub Secrets
env_path = Path(__file__).resolve().parent.parent / "secrets.env"
if env_path.exists():
    load_dotenv(env_path)

def send_to_telegram(message: str):
    """
    Send a message to a Telegram chat.

    Args:
        message (str): The text message to send.
        bot_token (str): Telegram bot token.
        chat_id (str): The chat ID (user, group, or channel).

    Returns:
        requests.Response: The response object from Telegram API.
    """
    bot_token = os.getenv('BOT_TOKEN')
    chat_id   = os.getenv('CHAT_ID')
    if not bot_token or not chat_id:
        raise RuntimeError("Missing BOT_TOKEN or CHAT_ID. Make sure env vars are set.")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Raise error for HTTP failures
        return response
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to send Telegram message: {e}") from e