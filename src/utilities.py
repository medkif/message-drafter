import subprocess, requests, urllib.parse, ollama
from openai import OpenAI
from translate import Translator


def ollama_local(prompt:str) -> str:
    result = subprocess.run(
        ["ollama", "run", "llama3"],  # input arguments to process
        input=prompt.encode("utf-8"),
        capture_output=True
    )
    return result.stdout.decode().strip()
import ollama

def ollama_api(prompt:str,model='llama3') -> str:
    result = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
        )
    
    completion=result["message"]["content"].strip()
    return completion

def openai_chat_completion(api_key:str) -> str:
    client = OpenAI(api_key=api_key)
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

    try:
        draft = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a message drafter. Your job is to help people connect with their friends by drafting friendly messages."},
                {"role": "user", "content": prompt}
            ]
        )
    except:
        raise Exception("Something went wrong with OpenAI API.")
    return draft.choices[0].message.content.strip()

def pollinations_api(prompt:str) -> str:
    # Generate
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching text: {e}")
        if response is not None: print("Response text:", response.text)
    if response is not None: draft = response.text
    return prompt

def mlvoca_api(prompt:str) -> str:
    try:
        url = "https://mlvoca.com/api/generate"
        payload = {
            "model": "tinyllama",   # or "tinyllama"
            "prompt": prompt,
            "stream": False
        }
        resp = requests.post(url, json=payload, timeout=60)
        draft=resp.json().get("response")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching text: {e}")
    return draft

def translate_to_swe(input_text:str) -> str:
    # Translate:
    translation = Translator(to_lang="sv").translate(input_text)

    # For testing:
    print("Original text:\n"+input_text)
    print(translation)
    return translation

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