import os
import requests
import streamlit as st

HF_API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-3B-Instruct"

def _get_token() -> str:
    try:
        return st.secrets["HF_TOKEN"]
    except Exception:
        return os.environ.get("HF_TOKEN", "")

def generate(
    prompt: str,
    system: str = "Du bist ein freundlicher Lehrerzauberer für Kinder von 5-9 Jahren. Antworte immer auf Deutsch, kurz und einfach verständlich.",
    max_new_tokens: int = 400,
) -> str:
    token = _get_token()
    if not token:
        return "⚠️ Kein Hugging Face API-Token gefunden. Bitte in den Streamlit-Secrets eintragen (HF_TOKEN)."

    headers = {"Authorization": f"Bearer {token}"}
    chat_prompt = f"<|im_start|>system\n{system}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"

    payload = {
        "inputs": chat_prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": 0.8,
            "do_sample": True,
            "return_full_text": False,
        },
    }

    try:
        resp = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list) and data:
            return data[0].get("generated_text", "").strip()
        return str(data)
    except requests.exceptions.Timeout:
        return "⏳ Das Modell braucht gerade etwas länger – bitte nochmal versuchen!"
    except Exception as e:
        return f"⚠️ Fehler: {e}"
