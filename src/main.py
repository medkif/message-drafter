from storage_service import fetch_recent_drafts, save_draft
from llm_service import openai_chat_completion, anthropic_chat_completion
from chat_service import send_to_telegram

if __name__ == "__main__":

    latest_messages = fetch_recent_drafts(collection_name="drafts")
    print(f'recent drafts:\n    {latest_messages}')

    # draft = openai_chat_completion(recent_messages=latest_messages)
    draft = anthropic_chat_completion(recent_messages=latest_messages)
    # Send message
    send_to_telegram(draft)

    save_draft(collection_name="drafts",text=draft)