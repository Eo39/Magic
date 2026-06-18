import os
import requests
import streamlit as st

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def _get_token() -> str:
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return os.environ.get("GROQ_API_KEY", "")

def generate(
    prompt: str,
    system: str = "Du bist ein freundlicher Lehrerzauberer für Kinder von 5-9 Jahren. Antworte immer auf Deutsch, kurz und einfach verständlich.",
    max_new_tokens: int = 400,
) -> str:
    token = _get_token()
    if not token:
        return "⚠️ Kein API-Token gefunden. Bitte GROQ_API_KEY in den Streamlit-Secrets eintragen."

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": prompt},
        ],
        "max_tokens": max_new_tokens,
        "temperature": 0.8,
    }

    try:
        resp = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except requests.exceptions.Timeout:
        return "⏳ Das Modell braucht gerade etwas länger – bitte nochmal versuchen!"
    except Exception as e:
        return f"⚠️ Fehler: {e}"
