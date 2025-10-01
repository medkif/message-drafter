import os
from dotenv import load_dotenv
from pathlib import Path
from storage_service import fetch_recent_drafts, save_draft
from llm_service import openai_chat_completion, translate_to_swe
from chat_service import send_to_telegram

if __name__ == "__main__":

    # Try to load .env file if it exists (local dev)
    # Otherwise, will be gotten from GitHub Secrets
    env_path = Path(__file__).resolve().parent.parent / "secrets.env"
    if env_path.exists():
        load_dotenv(env_path)
    # PROJECT_ID     = os.getenv('PROJECT_ID') # GCP Project ID
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') # OpenAI API Key
    BOT_TOKEN      = os.getenv('BOT_TOKEN') # Telegram bot token
    CHAT_ID        = os.getenv('CHAT_ID') # Telegram chat ID

    if not BOT_TOKEN or not CHAT_ID:
        raise RuntimeError("Missing BOT_TOKEN or CHAT_ID. Make sure env vars are set.")    

    latest_messages = fetch_recent_drafts(collection_name="drafts")
    print(f'recent drafts:\n{latest_messages}')

    draft = openai_chat_completion(api_key=OPENAI_API_KEY, recent_messages=latest_messages)

    # Send message
    send_to_telegram(draft, BOT_TOKEN, CHAT_ID)

    save_draft(collection_name="drafts",text=draft)