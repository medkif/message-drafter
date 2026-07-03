import subprocess, os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
from anthropic import Anthropic
import ollama

# Try to load .env file if it exists (local dev)
# Otherwise, will be gotten from GitHub Secrets
env_path = Path(__file__).resolve().parent.parent / "secrets.env"
if env_path.exists():
    load_dotenv(env_path)

SYSTEM_PROMPT = "You are a message drafter. Your job is to help people connect with their friends by drafting friendly messages."

def openai_chat_completion(recent_messages:list[str]) -> str:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') # OpenAI API Key
    if not OPENAI_API_KEY: raise RuntimeError("Missing OPENAI_API_KEY. Make sure env vars are set.")
    # Module-level authentication to OpenAI
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except:
        raise Exception("Error when connecting to OpenAI Client.")
    
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
        draft = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )
    except:
        raise Exception("Something went wrong with OpenAI API.")
    
    return draft.choices[0].message.content.strip()

def anthropic_chat_completion(recent_messages: list[str]) -> str:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    if not ANTHROPIC_API_KEY: raise RuntimeError("Missing OPENAI_API_KEY. Make sure env vars are set.")
    # Module-level authentication to Anthropic
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
    except:
        raise Exception("Error when connecting to Anthropic Client.")
    
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
            model="claude-sonnet-5",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
    except Exception as e:
        raise Exception(f"Something went wrong with Anthropic API: {e}")

    return "".join(block.text for block in draft.content if block.type == "text").strip()

def ollama_local(prompt:str) -> str:
    result = subprocess.run(
        ["ollama", "run", "llama3"],  # input arguments to process
        input=prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode().strip()


def ollama_api(prompt:str,model='llama3') -> str:
    result = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
        )
    
    completion=result["message"]["content"].strip()
    return completion