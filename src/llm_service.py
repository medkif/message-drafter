import os
from dotenv import load_dotenv
from pathlib import Path
from anthropic import Anthropic

# Try to load .env file if it exists (local dev)
# Otherwise, will be gotten from GitHub Secrets
env_path = Path(__file__).resolve().parent.parent / "secrets.env"
if env_path.exists():
    load_dotenv(env_path)

SYSTEM_PROMPT = "You are a message drafter. Your job is to help people connect with their friends by drafting friendly messages."

def anthropic_chat_completion(recent_messages: list[str]) -> str:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    if not ANTHROPIC_API_KEY: raise RuntimeError("Missing ANTHROPIC_API_KEY. Make sure env vars are set.")
    # Module-level authentication to Anthropic
    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""
    Write a short greeting in swedish that is going to be sent on Messenger.
    - Start the message with Tja (swedish slang).
    - Be easy going, concrete and articulated. 
    - Finish with a simple question.
    - Do not seek to hangout or setup a call.
    - Only write 1 to 3 sentences.
    - avoid writing any of the previous messages: {recent_messages}
    - Do not include quotes.
    """

    try:
        draft = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
    except Exception as e:
        raise Exception(f"Something went wrong with Anthropic API: {e}")

    return "".join(block.text for block in draft.content if block.type == "text").strip()

