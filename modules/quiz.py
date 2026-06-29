import streamlit as st
import random
from helpers.tts import play_text

ANIMALS = [
    {"name": "Elefant",  "emoji": "🐘", "url": "https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=400"},
    {"name": "Löwe",     "emoji": "🦁", "url": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=400"},
    {"name": "Pinguin",  "emoji": "🐧", "url": "https://images.unsplash.com/photo-1551986782-d0169b3f8fa7?w=400"},
    {"name": "Giraffe",  "emoji": "🦒", "url": "https://images.unsplash.com/photo-1547721064-da6cfb341d50?w=400"},
    {"name": "Zebra",    "emoji": "🦓", "url": "https://images.unsplash.com/photo-1529728329775-c90d27125b7b?w=400"},
    {"name": "Gorilla",  "emoji": "🦍", "url": "https://images.unsplash.com/photo-1520808663317-647b476a81b9?w=400"},
    {"name": "Flamingo", "emoji": "🦩", "url": "https://images.unsplash.com/photo-1497206365907-f5e630693df0?w=400"},
    {"name": "Krokodil", "emoji": "🐊", "url": "https://images.unsplash.com/photo-1610058494255-9a773f4b1ac3?w=400"},
    {"name": "Nashorn",  "emoji": "🦏", "url": "https://images.unsplash.com/photo-1598439210625-5067c578f3f6?w=400"},
    {"name": "Koalabär", "emoji": "🐨", "url": "https://images.unsplash.com/photo-1459262838948-3e2de6c1ec80?w=400"},
    {"name": "Panda",    "emoji": "🐼", "url": "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7?w=400"},
    {"name": "Kamel",    "emoji": "🐪", "url": "https://images.unsplash.com/photo-1518467166778-b88f373ffec7?w=400"},
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
    .feedback-ok  { font-size:2rem; text-align:center; color:#059669; font-weight:900; margin-top:1rem; }
    .feedback-bad { font-size:2rem; text-align:center; color:#DC2626; font-weight:900; margin-top:1rem; }
    .game-over    { font-size:2.5rem; text-align:center; font-weight:900; color:#1E3A5F; }

    .img-btn {
        background: none;
        border: 6px solid transparent;
        border-radius: 20px;
        padding: 4px;
        cursor: pointer;
        width: 100%;
        transition: transform 0.15s, border-color 0.15s;
        display: block;
    }
    .img-btn:hover {
        transform: scale(1.04);
        border-color: #2563EB;
    }
    .img-btn img {
        width: 100%;
        border-radius: 14px;
        display: block;
        height: 180px;
        object-fit: cover;
    }
    .img-correct { border:6px solid #34D399 !important; border-radius:20px; padding:4px; display:block; }
    .img-correct img { width:100%; border-radius:14px; height:180px; object-fit:cover; display:block; }
    .img-wrong   { border:6px solid #F87171 !important; border-radius:20px; padding:4px; display:block; opacity:0.6; }
    .img-wrong img   { width:100%; border-radius:14px; height:180px; object-fit:cover; display:block; }
    .img-neutral { border:6px solid transparent; border-radius:20px; padding:4px; display:block; }
    .img-neutral img { width:100%; border-radius:14px; height:180px; object-fit:cover; display:block; }
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

    # Inject JS to handle image clicks → sets a hidden query param
    if not answered:
        click_js = """
        <script>
        function chooseAnimal(name) {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: name}, '*');
        }
        </script>
        """
        st.markdown(click_js, unsafe_allow_html=True)

    cols = st.columns(2)
    for i, animal in enumerate(options):
        with cols[i % 2]:
            if answered:
                if animal["name"] == correct["name"]:
                    css = "img-correct"
                elif animal["name"] == chosen:
                    css = "img-wrong"
                else:
                    css = "img-neutral"
                st.markdown(f'''
                    <div class="{css}">
                        <img src="{animal["url"]}">
                    </div>
                    <p style="text-align:center;font-size:1.2rem;font-weight:900;margin-top:6px">
                        {animal["emoji"]} {animal["name"]}
                    </p>
                ''', unsafe_allow_html=True)
            else:
                # Großer klickbarer Button mit Bild
                if st.button(
                    f"{animal['emoji']} {animal['name']}",
                    key=f"answer_{i}_{animal['name']}",
                    use_container_width=True,
                ):
                    st.session_state.quiz_answered = True
                    st.session_state.quiz_chosen   = animal["name"]
                    if animal["name"] == correct["name"]:
                        st.session_state.quiz_score += 1
                    else:
                        st.session_state.quiz_lives -= 1
                    st.session_state.quiz_question_read = False
                    st.rerun()

                st.markdown(f'''
                    <img src="{animal["url"]}"
                         style="width:100%; height:180px; object-fit:cover;
                                border-radius:16px; margin-top:-0.5rem; margin-bottom:0.8rem;
                                cursor:pointer; display:block;"
                    >
                ''', unsafe_allow_html=True)

    if answered:
        if chosen == correct["name"]:
            st.markdown('<div class="feedback-ok">🎉 Super! Richtig! ⭐</div>', unsafe_allow_html=True)
            play_text(f"Super! Das war wirklich der {correct['name']}! Du bekommst einen Stern!")
        else:
            st.markdown(f'<div class="feedback-bad">❌ Das war der {correct["name"]}! {correct["emoji"]}</div>', unsafe_allow_html=True)
            play_text(f"Das war leider falsch. Das richtige Tier war der {correct['name']}!")

        if st.button("➡️ Nächste Frage", key="next_q", use_container_width=True):
            _init_quiz()
            st.session_state.quiz_question_read = False
            st.rerun()
