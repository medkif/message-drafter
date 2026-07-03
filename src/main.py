import logging
from storage_service import fetch_recent_drafts, save_draft
from llm_service import anthropic_chat_completion
from chat_service import send_to_telegram

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    latest_messages = fetch_recent_drafts(collection_name="drafts")
    logging.info(f"recent drafts: {latest_messages}")

    draft = anthropic_chat_completion(recent_messages=latest_messages)
    send_to_telegram(draft)
    logging.info("draft sent successfully")

    save_draft(collection_name="drafts", text=draft)
    logging.info("draft saved to Firestore")