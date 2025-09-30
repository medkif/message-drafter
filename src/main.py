import os
from dotenv import load_dotenv
from pathlib import Path
from utilities import openai_chat_completion,translate_to_swe,send_to_telegram

if __name__ == "__main__":

    # Try to load .env file if it exists (local dev)
    # Otherwise, will be gotten from GitHub Secrets
    env_path = Path(__file__).resolve().parent.parent / "secrets.env"
    if env_path.exists():
        load_dotenv(env_path)
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') # OpenAI API Key
    BOT_TOKEN      = os.getenv('BOT_TOKEN') # Telegram bot token
    CHAT_ID        = os.getenv('CHAT_ID') # Telegram chat ID

    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Missing BOT_TOKEN or CHAT_ID. Make sure env vars are set.")

    draft = openai_chat_completion(api_key=OPENAI_API_KEY)

    draft = translate_to_swe(draft)

    # Send message
    send_to_telegram(draft, BOT_TOKEN, CHAT_ID)