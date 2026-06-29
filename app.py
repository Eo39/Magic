import streamlit as st

st.set_page_config(
    page_title="WissenWunderland",
    page_icon="🧙‍♂️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 40%, #0f3460 100%);
    min-height: 100vh;
}

.stApp::before {
    content: '⭐✨🌟💫⭐✨🌟💫⭐✨🌟💫⭐✨🌟💫⭐✨🌟💫';
    position: fixed;
    top: 0; left: 0;
    width: 100%;
    font-size: 1.5rem;
    opacity: 0.15;
    word-break: break-all;
    line-height: 2.5rem;
    pointer-events: none;
    z-index: 0;
}

#MainMenu, header, footer { visibility: hidden; }

div.stButton > button {
    font-family: 'Nunito', sans-serif;
    font-size: 1.4rem;
    font-weight: 900;
    border-radius: 20px;
    padding: 1rem 1.5rem;
    border: 2px solid rgba(255,255,255,0.6);
    cursor: pointer;
    transition: transform 0.15s, box-shadow 0.15s;
    width: 100%;
    background: rgba(255,255,255,0.35);
    color: white;
    backdrop-filter: blur(10px);
}
div.stButton > button:hover {
    transform: scale(1.06);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    background: rgba(255,255,255,0.5);
}

.wizard-emoji {
    font-size: 6rem;
    text-align: center;
    display: block;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%,100% { transform: translateY(0px); }
    50%      { transform: translateY(-15px); }
}

.title-text {
    font-size: 3rem;
    font-weight: 900;
    color: #FFD700;
    text-align: center;
    text-shadow: 0 0 30px rgba(255,215,0,0.5);
    margin-bottom: 0.3rem;
}
.subtitle-text {
    font-size: 1.2rem;
    color: rgba(255,255,255,0.8);
    text-align: center;
    margin-bottom: 2rem;
}

.menu-card {
    background: rgba(255,255,255,0.22);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.45);
    border-radius: 24px;
    padding: 1.5rem 1rem;
    text-align: center;
    margin-bottom: 0.5rem;
    transition: transform 0.2s;
}
.menu-card .icon { font-size: 3rem; display: block; }
.menu-card .label {
    font-size: 1.2rem;
    font-weight: 900;
    color: white;
    margin-top: 0.4rem;
}
.menu-card .desc {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.7);
    margin-top: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page):
    st.session_state.page = page
    st.rerun()

page = st.session_state.page

if page == "home":
    st.markdown('<span class="wizard-emoji">🧙‍♂️</span>', unsafe_allow_html=True)
    st.markdown('<div class="title-text">✨ WissenWunderland ✨</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Was möchtest du heute entdecken?</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="menu-card">
            <span class="icon">📖</span>
            <div class="label">Geschichten</div>
            <div class="desc">Reise mit dem Zauberer durch die Welt!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Geschichten", key="btn_story", use_container_width=True):
            go("story")

    with col2:
        st.markdown("""
        <div class="menu-card">
            <span class="icon">🎯</span>
            <div class="label">Quiz</div>
            <div class="desc">Erkenne die Tiere und sammle Punkte!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎯 Quiz", key="btn_quiz", use_container_width=True):
            go("quiz")

    with col3:
        st.markdown("""
        <div class="menu-card">
            <span class="icon">✏️</span>
            <div class="label">Zeichnen</div>
            <div class="desc">Lerne Schritt für Schritt zu zeichnen!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✏️ Zeichnen", key="btn_draw", use_container_width=True):
            go("draw")

elif page == "story":
    from modules import story
    story.show()

elif page == "quiz":
    from modules import quiz
    quiz.show()

elif page == "draw":
    from modules import draw
    draw.show()
