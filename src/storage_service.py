import os
from dotenv import load_dotenv
from pathlib import Path
from google.cloud import firestore
from datetime import datetime, timezone

env_path = Path(__file__).resolve().parent.parent / "secrets.env"
if env_path.exists():
    load_dotenv(env_path)
PROJECT_ID = os.getenv('PROJECT_ID') # GCP Project ID
DB_NAME    = os.getenv('DB_NAME') # Firestore db id
if not PROJECT_ID: raise RuntimeError("Missing PROJECT_ID. Make sure env vars are set.")
if not DB_NAME: raise RuntimeError("Missing DB_NAME. Make sure env vars are set.")

# Module-level authentication to Firestore
db = firestore.Client(project=PROJECT_ID,database=DB_NAME)

def save_draft(collection_name:str, text: str):
    """Save a draft message into Firestore"""
    doc_ref = db.collection(collection_name).document()
    doc_ref.set({
        "text": text,
        "timestamp": datetime.now(timezone.utc)
    })

def fetch_recent_drafts(collection_name:str,n: int = 5) -> list[str]:
    """Fetch the most recent n drafts"""
    docs = db.collection(collection_name) \
             .order_by("timestamp", direction=firestore.Query.DESCENDING) \
             .limit(n) \
             .stream()
    return [doc.to_dict()["text"] for doc in docs]
