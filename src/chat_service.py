import requests

def send_to_telegram(message: str, bot_token: str, chat_id: str):
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