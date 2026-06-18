import io
import base64
import streamlit as st

def text_to_audio_b64(text: str, lang: str = "de") -> str:
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        return base64.b64encode(buf.read()).decode()
    except Exception as e:
        st.warning(f"Sprachausgabe nicht verfügbar: {e}")
        return ""

def play_text(text: str, lang: str = "de"):
    b64 = text_to_audio_b64(text, lang)
    if b64:
        audio_html = f"""
        <audio autoplay style="display:none">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

def play_button(text: str, label: str = "🔊 Vorlesen", lang: str = "de"):
    if st.button(label, key=f"tts_{hash(text) % 99999}"):
        play_text(text, lang)
