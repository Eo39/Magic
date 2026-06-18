import streamlit as st
from utils.llm import generate
from utils.tts import play_text, play_button

TOPICS = [
    {"emoji": "🏛️", "label": "Ägypten & Pyramiden",  "prompt": "Erzähle eine kurze, spannende Geschichte für Kinder über das alte Ägypten und die Pyramiden. Erkläre dabei einfach, warum die Pyramiden gebaut wurden."},
    {"emoji": "🦕", "label": "Dinosaurier",           "prompt": "Erzähle eine kurze Geschichte für Kinder über Dinosaurier. Was haben sie gegessen? Warum gibt es sie nicht mehr?"},
    {"emoji": "🌋", "label": "Vulkane",               "prompt": "Erkläre Kindern in einer kurzen Geschichte, wie ein Vulkan funktioniert. Nutze einfache Worte und ein Abenteuer als Rahmen."},
    {"emoji": "🚀", "label": "Weltall & Planeten",    "prompt": "Erzähle eine kurze Geschichte für Kinder über das Weltall. Was sind Planeten? Wie weit ist die Sonne entfernt?"},
    {"emoji": "🐋", "label": "Tiere im Ozean",        "prompt": "Erzähle eine kurze Geschichte für Kinder über Tiere im Ozean. Was lebt in der Tiefsee? Warum ist das Meer so wichtig?"},
    {"emoji": "🏰", "label": "Ritter & Burgen",       "prompt": "Erzähle eine kurze Geschichte für Kinder über Ritter und Burgen im Mittelalter. Was haben Ritter gemacht? Wie sah ihr Leben aus?"},
    {"emoji": "🌿", "label": "Regenwald",             "prompt": "Erzähle eine kurze Geschichte für Kinder über den Regenwald. Welche Tiere leben dort? Warum ist er so wichtig für uns?"},
    {"emoji": "❄️", "label": "Arktis & Eisbären",     "prompt": "Erzähle eine kurze Geschichte für Kinder über die Arktis und die Tiere, die dort leben. Wie überleben sie die Kälte?"},
]

WIZARD_LINES = [
    "Hm, lass mich nachdenken... 🌟",
    "Ah, eine wunderbare Wahl! ✨",
    "Mein Zauberbuch verrät mir... 📚",
    "Höre gut zu, kleiner Entdecker! 🔮",
]

def show():
    if st.button("⬅️ Zurück", key="story_back"):
        st.session_state.page = "home"
        for k in ["story_text", "story_topic_idx"]:
            st.session_state.pop(k, None)
        st.rerun()

    st.markdown("""
    <style>
    .wizard-big { font-size:5rem; text-align:center; display:block;
                  animation: float 3s ease-in-out infinite; }
    @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
    .story-title { font-size:2rem; font-weight:900; color:#1E3A5F; text-align:center; }
    .story-sub   { font-size:1.1rem; color:#4B6FA5; text-align:center; margin-bottom:1.5rem; }
    .story-box   { background:white; border-radius:20px; padding:1.5rem;
                   font-size:1.15rem; line-height:1.8; color:#1f2937;
                   box-shadow:0 4px 16px rgba(0,0,0,0.08); margin-top:1rem; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<span class="wizard-big">🧙‍♂️</span>', unsafe_allow_html=True)
    st.markdown('<div class="story-title">Zauberer Wissaldo</div>', unsafe_allow_html=True)
    st.markdown('<div class="story-sub">Wähle ein Thema und ich erzähle dir eine Geschichte!</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    chosen_idx = None
    for i, topic in enumerate(TOPICS):
        with cols[i % 4]:
            if st.button(f"{topic['emoji']}\n{topic['label']}", key=f"topic_{i}"):
                chosen_idx = i
                st.session_state.story_topic_idx = i
                st.session_state.pop("story_text", None)

    if chosen_idx is None:
        chosen_idx = st.session_state.get("story_topic_idx", None)

    if chosen_idx is not None:
        topic = TOPICS[chosen_idx]

        if "story_text" not in st.session_state:
            import random
            wizard_line = random.choice(WIZARD_LINES)
            with st.spinner(f"🧙‍♂️ {wizard_line}"):
                story = generate(topic["prompt"])
            st.session_state.story_text = story
        else:
            story = st.session_state.story_text

        st.markdown(f'<div class="story-box">📖 <strong>{topic["emoji"]} {topic["label"]}</strong><br><br>{story}</div>', unsafe_allow_html=True)
        play_button(story, label="🔊 Geschichte vorlesen")

        if st.button("🔄 Neue Geschichte zu diesem Thema", key="new_story"):
            st.session_state.pop("story_text", None)
            st.rerun()
