import streamlit as st
import random
from utils.tts import play_text

ANIMALS = [
    {"name": "Elefant",  "emoji": "🐘", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/480px-African_Bush_Elephant.jpg"},
    {"name": "Löwe",     "emoji": "🦁", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/480px-Lion_waiting_in_Namibia.jpg"},
    {"name": "Pinguin",  "emoji": "🐧", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Spheniscus_demersus_in_Boulders_Beach.jpg/480px-Spheniscus_demersus_in_Boulders_Beach.jpg"},
    {"name": "Giraffe",  "emoji": "🦒", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Giraffe_Mikumi_National_Park.jpg/480px-Giraffe_Mikumi_National_Park.jpg"},
    {"name": "Zebra",    "emoji": "🦓", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Plains_Zebra_Equus_quagga.jpg/480px-Plains_Zebra_Equus_quagga.jpg"},
    {"name": "Gorilla",  "emoji": "🦍", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Silverback_Gorilla.jpg/480px-Silverback_Gorilla.jpg"},
    {"name": "Flamingo", "emoji": "🦩", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Flamingos_Laguna_Colorada.jpg/480px-Flamingos_Laguna_Colorada.jpg"},
    {"name": "Krokodil", "emoji": "🐊", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Crocodylus_niloticus_nel_parco_nazionale_Kruger.jpg/480px-Crocodylus_niloticus_nel_parco_nazionale_Kruger.jpg"},
    {"name": "Nashorn",  "emoji": "🦏", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/White_Rhinoceros.jpg/480px-White_Rhinoceros.jpg"},
    {"name": "Koalabär", "emoji": "🐨", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Koala_climbing_tree.jpg/480px-Koala_climbing_tree.jpg"},
    {"name": "Panda",    "emoji": "🐼", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Grosser_Panda.JPG/480px-Grosser_Panda.JPG"},
    {"name": "Kamel",    "emoji": "🐪", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Camelus_bactrianus_Bactrian_Camel.jpg/480px-Camelus_bactrianus_Bactrian_Camel.jpg"},
]

MAX_LIVES = 5

def _init_quiz():
    all_animals = ANIMALS[:]
    random.shuffle(all_animals)
    correct = all_animals[0]
    wrong   = random.sample(all_animals[1:], 3)
    options = [correct] + wrong
    random.shuffle(options)
    st.session_state.quiz_correct  = correct
    st.session_state.quiz_options  = options
    st.session_state.quiz_answered = False
    st.session_state.quiz_chosen   = None

def show():
    if st.button("⬅️ Zurück", key="quiz_back"):
        for k in list(st.session_state.keys()):
            if k.startswith("quiz_"):
                del st.session_state[k]
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <style>
    .quiz-title    { font-size:2rem; font-weight:900; color:#1E3A5F; text-align:center; }
    .quiz-question { font-size:1.6rem; font-weight:700; color:#1E3A5F; text-align:center;
                     background:white; border-radius:16px; padding:1rem;
                     box-shadow:0 4px 12px rgba(0,0,0,0.07); margin-bottom:1rem; }
    .img-correct { border:6px solid #34D399; border-radius:16px; }
    .img-wrong   { border:6px solid #F87171; border-radius:16px; filter:brightness(0.7); }
    .img-normal  { border:6px solid transparent; border-radius:16px; }
    .feedback-ok  { font-size:2rem; text-align:center; color:#059669; font-weight:900; }
    .feedback-bad { font-size:2rem; text-align:center; color:#DC2626; font-weight:900; }
    .game-over    { font-size:2.5rem; text-align:center; font-weight:900; color:#1E3A5F; }
    </style>
    """, unsafe_allow_html=True)

    if "quiz_lives" not in st.session_state:
        st.session_state.quiz_lives = MAX_LIVES
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    if "quiz_correct" not in st.session_state:
        _init_quiz()

    lives = st.session_state.quiz_lives
    score = st.session_state.quiz_score

    st.markdown('<div class="quiz-title">🎯 Tierquiz</div>', unsafe_allow_html=True)
    hearts = "❤️" * lives + "🖤" * (MAX_LIVES - lives)
    st.markdown(f'<div style="text-align:center;font-size:2rem">{hearts} &nbsp; ⭐ {score}</div>', unsafe_allow_html=True)

    if lives <= 0:
        st.markdown(f'<div class="game-over">😢 Game Over!<br>Du hattest {score} ⭐</div>', unsafe_allow_html=True)
        play_text(f"Schade! Du hast {score} Punkte erreicht. Versuch es nochmal!")
        if st.button("🔄 Nochmal spielen", key="restart"):
            st.session_state.quiz_lives = MAX_LIVES
            st.session_state.quiz_score = 0
            _init_quiz()
            st.rerun()
        return

    correct  = st.session_state.quiz_correct
    options  = st.session_state.quiz_options
    answered = st.session_state.quiz_answered
    chosen   = st.session_state.quiz_chosen

    question_text = f"Welches Bild zeigt den {correct['name']}? {correct['emoji']}"
    st.markdown(f'<div class="quiz-question">{question_text}</div>', unsafe_allow_html=True)

    if not answered and not st.session_state.get("quiz_question_read"):
        play_text(f"Welches Bild zeigt den {correct['name']}?")
        st.session_state.quiz_question_read = True

    cols = st.columns(2)
    for i, animal in enumerate(options):
        with cols[i % 2]:
            if answered:
                if animal["name"] == correct["name"]:
                    css_class = "img-correct"
                elif animal["name"] == chosen:
                    css_class = "img-wrong"
                else:
                    css_class = "img-normal"
                st.markdown(f'<img src="{animal["url"]}" class="{css_class}" style="width:100%;border-radius:16px">', unsafe_allow_html=True)
                st.markdown(f'<p style="text-align:center;font-size:1.1rem;font-weight:700">{animal["emoji"]} {animal["name"]}</p>', unsafe_allow_html=True)
            else:
                # ← HIER die Änderung: HTML img statt st.image()
                st.markdown(f'<img src="{animal["url"]}" style="width:100%;border-radius:16px;margin-bottom:0.5rem">', unsafe_allow_html=True)
                if st.button(f"{animal['emoji']} Das ist es!", key=f"answer_{i}_{animal['name']}"):
                    st.session_state.quiz_answered = True
                    st.session_state.quiz_chosen   = animal["name"]
                    if animal["name"] == correct["name"]:
                        st.session_state.quiz_score += 1
                        st.session_state.quiz_question_read = False
                    else:
                        st.session_state.quiz_lives -= 1
                        st.session_state.quiz_question_read = False
                    st.rerun()

    if answered:
        if chosen == correct["name"]:
            st.markdown('<div class="feedback-ok">🎉 Super! Richtig! ⭐</div>', unsafe_allow_html=True)
            play_text(f"Super! Das war wirklich der {correct['name']}! Du bekommst einen Stern!")
        else:
            st.markdown(f'<div class="feedback-bad">❌ Das war der {correct["name"]}! {correct["emoji"]}</div>', unsafe_allow_html=True)
            play_text(f"Das war leider falsch. Das richtige Tier war der {correct['name']}!")

        if st.button("➡️ Nächste Frage", key="next_q"):
            _init_quiz()
            st.session_state.quiz_question_read = False
            st.rerun()
