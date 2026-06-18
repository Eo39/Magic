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
    background-color: #F0F9FF;
}
.stApp { background-color: #F0F9FF; }
#MainMenu, header, footer { visibility: hidden; }

div.stButton > button {
    font-family: 'Nunito', sans-serif;
    font-size: 1.5rem;
    font-weight: 900;
    border-radius: 24px;
    padding: 1rem 2rem;
    border: none;
    cursor: pointer;
    transition: transform 0.15s, box-shadow 0.15s;
    width: 100%;
}
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
.title-text {
    font-size: 3rem;
    font-weight: 900;
    color: #1E3A5F;
    text-align: center;
    line-height: 1.1;
}
.subtitle-text {
    font-size: 1.3rem;
    color: #4B6FA5;
    text-align: center;
    margin-bottom: 2rem;
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
.menu-card {
    background: white;
    border-radius: 24px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}
.menu-card .icon { font-size: 3.5rem; }
.menu-card .label {
    font-size: 1.4rem;
    font-weight: 900;
    color: #1E3A5F;
    margin-top: 0.5rem;
}
.menu-card .desc {
    font-size: 0.95rem;
    color: #6B7280;
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
    st.markdown('<div class="title-text">WissenWunderland</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Was möchtest du heute entdecken?</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="menu-card">
            <div class="icon">📖</div>
            <div class="label">Geschichten</div>
            <div class="desc">Reise mit dem Zauberer durch die Welt!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Geschichten 📖", key="btn_story"):
            go("story")

    with col2:
        st.markdown("""
        <div class="menu-card">
            <div class="icon">🎯</div>
            <div class="label">Quiz</div>
            <div class="desc">Erkenne die Tiere und sammle Punkte!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Quiz 🎯", key="btn_quiz"):
            go("quiz")

    with col3:
        st.markdown("""
        <div class="menu-card">
            <div class="icon">✏️</div>
            <div class="label">Zeichnen</div>
            <div class="desc">Lerne Schritt für Schritt zu zeichnen!</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Zeichnen ✏️", key="btn_draw"):
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
