import os
from dotenv import load_dotenv
from pathlib import Path
from utilities import translate_to_swe,send_to_telegram

if __name__ == "__main__":

    # Try to load .env file if it exists (local dev)
    # Otherwise, will be gotten from GitHub Secrets
    env_path = Path(__file__).resolve().parent.parent / "secrets.env"
    if env_path.exists():
        load_dotenv(env_path)
    BOT_TOKEN = os.getenv('BOT_TOKEN') # Telegram bot token
    CHAT_ID   = os.getenv('CHAT_ID') # Telegram chat ID
    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Missing BOT_TOKEN or CHAT_ID. Make sure env vars are set.")

    # Prompt
    prompt = """
    Write a short greeting that is going to be sent on Messenger.
    - Start the message with Tja (swedish slang).
    - Be easy going, concrete and articulated. 
    - Finish with a simple question.
    - Do not seek to hangout or setup a call.
    - Only write 1 to 3 sentences.
    - Only write the message, no other text.
    - Do not include quotes.
    """

    draft = 'Hello, this is a draft prompt.'
    draft = translate_to_swe(draft)

    # Send message
    send_to_telegram(draft, BOT_TOKEN, CHAT_ID)