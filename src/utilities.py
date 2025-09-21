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

def openai_api(prompt:str, api_key:str) -> str:
    client = OpenAI(api_key)
    try:
        draft = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a message drafter. Your job is to help me connect with my friend."},
                {"role": "user", "content": prompt}
            ]
        )
    except:
        raise Exception("Something went wrong with OpenAI API.")
    return draft

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

def send_to_telegram(message, BOT_TOKEN, CHAT_ID):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)