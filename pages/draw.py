import streamlit as st
from utils.tts import play_button

TUTORIALS = {
    "🐱 Katze": {
        "intro": "Heute lernen wir, eine Katze zu zeichnen! Schritt für Schritt!",
        "steps": [
            {
                "title": "Ein großer Kreis",
                "desc":  "Zeichne einen großen Kreis – das ist der Kopf der Katze!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="100" cy="100" r="70" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                </svg>""",
            },
            {
                "title": "Ohren hinzufügen",
                "desc":  "Jetzt zeichnen wir zwei spitze Dreiecke oben auf den Kopf – das sind die Ohren!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="100" cy="110" r="70" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="55,60 75,15 95,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="105,60 125,15 145,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                </svg>""",
            },
            {
                "title": "Augen malen",
                "desc":  "Zeichne zwei kleine Kreise für die Augen. Mal sie innen schwarz aus!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="100" cy="110" r="70" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="55,60 75,15 95,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="105,60 125,15 145,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <circle cx="82"  cy="100" r="10" fill="#1E3A5F"/>
                  <circle cx="118" cy="100" r="10" fill="#1E3A5F"/>
                  <circle cx="86"  cy="96"  r="3"  fill="white"/>
                  <circle cx="122" cy="96"  r="3"  fill="white"/>
                </svg>""",
            },
            {
                "title": "Nase & Mund",
                "desc":  "Zeichne ein kleines Dreieck als Nase und darunter ein W für den Mund!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="100" cy="110" r="70" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="55,60 75,15 95,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="105,60 125,15 145,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <circle cx="82"  cy="100" r="10" fill="#1E3A5F"/>
                  <circle cx="118" cy="100" r="10" fill="#1E3A5F"/>
                  <circle cx="86"  cy="96"  r="3"  fill="white"/>
                  <circle cx="122" cy="96"  r="3"  fill="white"/>
                  <polygon points="96,116 104,116 100,122" fill="#F87171"/>
                  <path d="M88,128 Q100,140 112,128" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                </svg>""",
            },
            {
                "title": "Schnurrhaare 🎉",
                "desc":  "Fast fertig! Zeichne links und rechts von der Nase je drei Linien – das sind die Schnurrhaare!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="100" cy="110" r="70" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="55,60 75,15 95,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="105,60 125,15 145,60" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <circle cx="82"  cy="100" r="10" fill="#1E3A5F"/>
                  <circle cx="118" cy="100" r="10" fill="#1E3A5F"/>
                  <circle cx="86"  cy="96"  r="3"  fill="white"/>
                  <circle cx="122" cy="96"  r="3"  fill="white"/>
                  <polygon points="96,116 104,116 100,122" fill="#F87171"/>
                  <path d="M88,128 Q100,140 112,128" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <line x1="40" y1="113" x2="90" y2="118" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="40" y1="119" x2="90" y2="121" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="40" y1="125" x2="90" y2="124" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="110" y1="118" x2="160" y2="113" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="110" y1="121" x2="160" y2="119" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="110" y1="124" x2="160" y2="125" stroke="#1E3A5F" stroke-width="2"/>
                </svg>""",
            },
        ],
    },

    "🏠 Haus": {
        "intro": "Heute zeichnen wir ein schönes Haus! Los geht's!",
        "steps": [
            {
                "title": "Ein Rechteck",
                "desc":  "Zeichne ein großes Rechteck – das ist der Körper des Hauses!",
                "svg": """<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg">
                  <rect x="30" y="100" width="140" height="100" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                </svg>""",
            },
            {
                "title": "Das Dach",
                "desc":  "Zeichne ein Dreieck oben drauf – das ist das Dach!",
                "svg": """<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg">
                  <rect x="30" y="100" width="140" height="100" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="15,105 100,30 185,105" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                </svg>""",
            },
            {
                "title": "Tür & Fenster",
                "desc":  "Zeichne eine Tür in der Mitte und zwei Fenster links und rechts!",
                "svg": """<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg">
                  <rect x="30" y="100" width="140" height="100" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="15,105 100,30 185,105" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <rect x="84" y="150" width="32" height="50" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <rect x="44" y="120" width="30" height="25" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <rect x="126" y="120" width="30" height="25" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <line x1="59"  y1="120" x2="59"  y2="145" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="44"  y1="132" x2="74"  y2="132" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="141" y1="120" x2="141" y2="145" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="126" y1="132" x2="156" y2="132" stroke="#1E3A5F" stroke-width="2"/>
                </svg>""",
            },
            {
                "title": "Schornstein 🎉",
                "desc":  "Zeichne einen Schornstein oben auf das Dach – fertig ist dein Haus!",
                "svg": """<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg">
                  <rect x="30" y="100" width="140" height="100" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <polygon points="15,105 100,30 185,105" stroke="#1E3A5F" stroke-width="4" fill="none"/>
                  <rect x="84" y="150" width="32" height="50" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <rect x="44" y="120" width="30" height="25" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <rect x="126" y="120" width="30" height="25" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <line x1="59"  y1="120" x2="59"  y2="145" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="44"  y1="132" x2="74"  y2="132" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="141" y1="120" x2="141" y2="145" stroke="#1E3A5F" stroke-width="2"/>
                  <line x1="126" y1="132" x2="156" y2="132" stroke="#1E3A5F" stroke-width="2"/>
                  <rect x="120" y="50" width="20" height="40" stroke="#1E3A5F" stroke-width="3" fill="none"/>
                  <path d="M118,46 Q125,30 132,46" stroke="#6B7280" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
                </svg>""",
            },
        ],
    },

    "⭐ Stern": {
        "intro": "Heute zeichnen wir einen funkelnden Stern!",
        "steps": [
            {
                "title": "Zwei Dreiecke",
                "desc":  "Zeichne ein Dreieck – spitze nach oben. Dann noch eins – spitze nach unten.",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <polygon points="100,20 120,80 80,80" stroke="#FBBF24" stroke-width="4" fill="none"/>
                  <polygon points="80,60 120,60 100,120" stroke="#FBBF24" stroke-width="4" fill="none"/>
                </svg>""",
            },
            {
                "title": "Den Stern ausschneiden",
                "desc":  "Verbinde die Spitzen der beiden Dreiecke – du siehst jetzt einen Stern!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <polygon points="100,20 118,68 150,68 125,90 135,130 100,108 65,130 75,90 50,68 82,68"
                           stroke="#FBBF24" stroke-width="4" fill="none"/>
                </svg>""",
            },
            {
                "title": "Ausmalen 🌟",
                "desc":  "Jetzt mal deinen Stern schön gelb aus – er soll leuchten wie am Himmel!",
                "svg": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                  <polygon points="100,20 118,68 150,68 125,90 135,130 100,108 65,130 75,90 50,68 82,68"
                           stroke="#D97706" stroke-width="4" fill="#FBBF24"/>
                  <circle cx="90" cy="80" r="6" fill="white" opacity="0.5"/>
                </svg>""",
            },
        ],
    },
}

def show():
    if st.button("⬅️ Zurück", key="draw_back"):
        for k in list(st.session_state.keys()):
            if k.startswith("draw_"):
                del st.session_state[k]
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <style>
    .draw-title  { font-size:2rem; font-weight:900; color:#1E3A5F; text-align:center; }
    .draw-sub    { font-size:1.1rem; color:#4B6FA5; text-align:center; margin-bottom:1.5rem; }
    .step-box    { background:white; border-radius:20px; padding:1.2rem;
                   box-shadow:0 4px 14px rgba(0,0,0,0.07); margin-bottom:1rem; }
    .step-title  { font-size:1.3rem; font-weight:900; color:#1E3A5F; }
    .step-desc   { font-size:1.05rem; color:#374151; margin-top:0.4rem; }
    .progress-label { font-size:1rem; color:#6B7280; text-align:center; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="draw-title">✏️ Zeichen-Schule</div>', unsafe_allow_html=True)
    st.markdown('<div class="draw-sub">Wähle etwas aus und ich zeige dir, wie man es zeichnet!</div>', unsafe_allow_html=True)

    tutorial_names = list(TUTORIALS.keys())
    cols = st.columns(len(tutorial_names))
    for i, name in enumerate(tutorial_names):
        with cols[i]:
            if st.button(name, key=f"tut_{i}"):
                st.session_state.draw_tutorial = name
                st.session_state.draw_step     = 0
                st.rerun()

    tut_name = st.session_state.get("draw_tutorial")
    if not tut_name:
        return

    tut   = TUTORIALS[tut_name]
    step  = st.session_state.get("draw_step", 0)
    steps = tut["steps"]

    if step == 0 and not st.session_state.get(f"draw_intro_{tut_name}"):
        from utils.tts import play_text
        play_text(tut["intro"])
        st.session_state[f"draw_intro_{tut_name}"] = True

    st.markdown(f'<div class="progress-label">Schritt {step+1} von {len(steps)}</div>', unsafe_allow_html=True)
    st.progress((step + 1) / len(steps))

    current = steps[step]
    st.markdown(f"""
    <div class="step-box">
        <div class="step-title">Schritt {step+1}: {current['title']}</div>
        <div class="step-desc">{current['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; background:white; border-radius:20px;
                padding:1rem; box-shadow:0 4px 14px rgba(0,0,0,0.07); margin-bottom:1rem;">
        <div style="max-width:280px; margin:auto;">{current['svg']}</div>
    </div>
    """, unsafe_allow_html=True)

    play_button(current['desc'], label=f"🔊 Schritt {step+1} vorlesen")

    left, _, right = st.columns([1, 0.2, 1])
    with left:
        if step > 0:
            if st.button("⬅️ Vorheriger Schritt", key="prev_step"):
                st.session_state.draw_step -= 1
                st.rerun()
    with right:
        if step < len(steps) - 1:
            if st.button("Nächster Schritt ➡️", key="next_step"):
                st.session_state.draw_step += 1
                st.rerun()
        else:
            st.markdown('<div style="text-align:right;font-size:1.5rem">🎉 Fertig!</div>', unsafe_allow_html=True)
            if st.button("🔄 Nochmal von vorne", key="restart_draw"):
                st.session_state.draw_step = 0
                st.rerun()
