import base64

import streamlit as st
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(
    page_title="For My Forever Valentine ❤️",
    page_icon="💖",
    layout="centered"
)

# --- BACKGROUND MUSIC ---
components.html(
    """
    <div id=\"player\"></div>
    <script src=\"https://www.youtube.com/iframe_api\"></script>
    <script>
        let player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                height: '0',
                width: '0',
                videoId: 'O-91jWrOxYk',
                playerVars: {
                    autoplay: 1,
                    controls: 0,
                    start: 40,
                    loop: 1,
                    playlist: 'O-91jWrOxYk',
                    mute: 1,
                    rel: 0,
                    playsinline: 1
                },
                events: {
                    onReady: (event) => {
                        event.target.mute();  // Required for autoplay policies
                        event.target.playVideo();
                        setTimeout(() => {
                            event.target.unMute();
                            event.target.setVolume(70);
                        }, 600);
                    },
                    onStateChange: (event) => {
                        if (event.data === YT.PlayerState.ENDED) {
                            event.target.seekTo(40);
                            event.target.playVideo();
                        }
                    }
                }
            });
        }
    </script>
    """,
    height=0,
)

# --- CUSTOM CSS (Sticker Background Restored) ---
st.markdown("""
<style>

/* Background Sticker Pattern */
.stApp {
    background-color: #FFF5F7;
    background-image: url("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXo2ajRua2R6aWt4bjlkY3QwMDhoaTNncnNwYzYyNjYybDVlMXNsZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/GSLbyMH6Afqn1lc4cb/giphy.gif");
    background-repeat: repeat;
    background-size: 280px;
    background-position: center;
    background-attachment: fixed;
}

/* White Overlay for Readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.78);
    pointer-events: none;
    z-index: 1;
}

/* Keep content above overlay */
.stApp > * {
    position: relative;
    z-index: 2;
}

/* Big Question Text */
.big-font {
    font-size: 30px !important;
    font-weight: bold;
    color: #d63384;
}

/* Button Styling */
div.stButton > button {
    background-color: #ffb3c1;
    color: #590d22;
    border-radius: 20px;
    border: 2px solid #ff4d6d;
    padding: 10px 24px;
    font-weight: bold;
    font-size: 20px;
}

div.stButton > button:hover {
    background-color: #ff4d6d;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# --- STATE ---
if "step" not in st.session_state:
    st.session_state.step = 1

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1


def scroll_top():
    components.html(
        "<script>window.parent.scrollTo(0, 0);</script>",
        height=0,
    )


def right_button(label, key=None, **button_kwargs):
    spacer, button_col = st.columns([1, 0.25])
    with button_col:
        return st.button(label, key=key, **button_kwargs)


def left_button(label, key=None, **button_kwargs):
    button_col, _ = st.columns([0.25, 1])
    with button_col:
        return st.button(label, key=key, **button_kwargs)


# --- PAGES ---

# PAGE 1: INTRO (Bollywood Romance)
if st.session_state.step == 1:
    scroll_top()
    st.markdown("<h1 style='text-align:center; '>Hey Husband ❤️</h1>", unsafe_allow_html=True)
    st.space("xlarge")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGg2bm16MWd0OGE0aXlyeW5zZDhtbTVkdHpyZHpkeDhwaGlycTM1bSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0OgdJVNjbcIifqSb7U/giphy.gif",
            width=400
        )

    st.markdown(
    "<h3 style='text-align:center; color:#590d22;'>"
    "I made something small for you… just a tiny journey through us 💕"
    "</h3>",
    unsafe_allow_html=True
    )
    st.space("small")

    st.markdown(
        "<p style='text-align:center;'>"
        "No pressure. Just click through slowly… and smile while you do 😌"
        "</p>",
        unsafe_allow_html=True
    )


    st.space("xlarge")
    # st.space("xlarge")
    if right_button("Click me!", key="page1_click"):
        next_step()
        st.rerun()


elif st.session_state.step == 2:
    scroll_top()
    st.markdown("<h1 style='text-align:center; '>The Love Quiz 💘</h1>", unsafe_allow_html=True)

    st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "Before I ask you the real question… I want to see something 😏<br>"
    "How well do you remember our little moments?"
    "</p>",
    unsafe_allow_html=True
    )

    # Embed Tenor GIF
    components.iframe(
        "https://tenor.com/embed/18378927",
        height=400,
        scrolling=False
    )
    
    st.markdown(
        "<p style='text-align:center;'>"
        "Don’t worry… even wrong answers are adorable."
        "</p>",
        unsafe_allow_html=True
    )


    # Initialize quiz_submitted state
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    st.markdown("<p class='big-font'>Q1: What did we first cook together?</p>", unsafe_allow_html=True)
    q1_choice = st.radio(
        "Pick the right answer:",
        ["Tea", "Maggi", "Sandwich", "Pasta"],
        index=None,
        key="q1"
    )

    st.markdown("<p class='big-font'>Q2: What movie we watched together on our second date?</p>", unsafe_allow_html=True)
    q2_choice = st.radio(
        "Pick the right answer:",
        ["The Holiday", "Jab we Met", "Sita Ramam", "Band Baja Barat"],
        index=None,
        key="q2"
    )

    st.markdown("<p class='big-font'>Q3: Where did we take this photo?</p>", unsafe_allow_html=True)
    st.image(
        "pic1.jpg",
        caption="A beautiful memory"
    )
    q3_choice = st.radio(
        "Pick the right answer:",
        ["Goa", "Mahe", "Praslin", "Chikkamagaluru"],
        index=None,
        key="q3"
    )

    st.markdown("<p class='big-font'>Q4: Who said I love you first?</p>", unsafe_allow_html=True)
    q4_choice = st.radio(
        "Pick the right answer:",
        ["Nitz! 😘", "Aru! 😌", "We said it together! 🥰", "Neither of us remember 😂"],
        index=None,
        key="q4"
    )

    # Define correct answers (UPDATE THESE WITH YOUR ACTUAL ANSWERS)
    correct_answers = {
        "q1": "Pasta",
        "q2": "Jab we Met",
        "q3": "Mahe",
        "q4": "Nitz! 😘"
    }

    if right_button("Submit", key="submit_answers"):
        st.session_state.quiz_submitted = True

    if st.session_state.quiz_submitted:
        # Check all answers
        all_correct = (
            q1_choice == correct_answers["q1"] and
            q2_choice == correct_answers["q2"] and
            q3_choice == correct_answers["q3"] and
            q4_choice == correct_answers["q4"]
        )

        if all_correct:
            st.success("Perfect score! You remember everything! 🎉")
            # GIF for all correct
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(
                    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
                    caption="Let's move ahead! 💕"
                )
            if right_button("Next", key="quiz_next"):
                next_step()
        else:
            st.error("Oops! Some answers need another try! 😅")
            # GIF for wrong answers - Kajol crying
            components.iframe(
                "https://tenor.com/embed/27244248",
                height=400,
                scrolling=False
            )
            if right_button("Try Again", key="quiz_retry"):
                st.session_state.quiz_submitted = False
                st.rerun()


# PAGE 3: WHY I LOVE YOU (POI Emotion)
elif st.session_state.step == 3:
    scroll_top()
    st.markdown("<h1 style='text-align:center; '>Why I Love You ❤️ </h1>", unsafe_allow_html=True)

    # st.markdown("Some feelings are quiet… but permanent 🖤")
    st.markdown(
        "<p style='text-align:center; font-size:18px;'>"
        "Okay… quiz aside, this part is the easiest.<br>"
        "Because loving you has never taken any effort."
        "</p>",
        unsafe_allow_html=True
    )



    st.markdown("""
    <div style="text-align: center;">
        <iframe src="https://tenor.com/embed/6133114" width="400" height="400" style="border:0;" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    reasons = [
        "❤️  You let me be 'me'",
        "❤️  You remember the tiniest details about me",
        "❤️  You are my safe space",
        "❤️  You always know how to make me laugh",
        "❤️  Your witty comebacks!",
        "❤️  You are sexy!! ",
    ]

    st.markdown("<br>", unsafe_allow_html=True)

    for r in reasons:
        st.markdown(f"<h3 style='text-align:left;'>{r}</h3>", unsafe_allow_html=True)

    st.space("large")

    if right_button("Next", key="page3_next"):
        next_step()


# PAGE 4: BIG QUESTION (Root Mischief)
elif st.session_state.step == 4:
    scroll_top()
    st.markdown("<h1 style='text-align:center;'>Last One!</h1>", unsafe_allow_html=True)

    st.space("small")
    st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "So after all the memories… after all the reasons…<br>"
    "I just have one last thing to ask."
    "</p>",
    unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "And yes… this is the most important question of them all 😌"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align:center;'>Will you be my Valentine? 🌹</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style="display:flex; justify-content:center;">
        <div style="width:400px; height:300px; overflow:hidden; border-radius:20px;">
            <iframe src="https://tenor.com/embed/21340252" width="400" height="400" style="border:0; margin-top:-100px;" allowfullscreen></iframe>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col, col_yes, col_no = st.columns([0.5,2,1])

    with col_yes:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        if st.button("YES!", key="yes_streamlit_button"):
            next_step()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_no:
        components.html(
            """
            <div style="display:flex; flex-direction:column; align-items:center; gap:16px;">
                <div style="display:flex; justify-content:center; align-items:center; height:150px;">
                    <button id=\"noBtn\"
                        style=\"padding:10px 24px; font-size:16px; background-color:#ffb3c1; color:#590d22; border:2px solid #ff4d6d; border-radius:20px; cursor:pointer;\">
                        No
                    </button>
                </div>
                <div id=\"noGifContainer\" style=\"display:none; width:100%; max-width:400px;\"></div>
            </div>
            <script>
                const noBtn = document.getElementById('noBtn');
                noBtn.addEventListener('mouseover', () => {
                    const x = Math.random() * (window.innerWidth - 150);
                    const y = Math.random() * (window.innerHeight - 100);
                    noBtn.style.position = 'fixed';
                    noBtn.style.left = x + 'px';
                    noBtn.style.top = y + 'px';
                });
                noBtn.addEventListener('click', () => {
                    const container = document.getElementById('noGifContainer');
                    if (!container) return;
                    if (!container.dataset.loaded) {
                        container.style.display = 'block';
                        container.innerHTML = `
                            <div class="tenor-gif-embed" data-postid="8417007939964092403" data-share-method="host" data-aspect-ratio="1.76596" data-width="100%">
                                <a href="https://tenor.com/view/no-try-again-no-nope-try-again-denied-gif-8417007939964092403">No Try Again Nope GIF</a>
                                from <a href="https://tenor.com/search/no+try+again-gifs">No Try Again GIFs</a>
                            </div>`;
                        const script = document.createElement('script');
                        script.type = 'text/javascript';
                        script.src = 'https://tenor.com/embed.js';
                        script.async = true;
                        container.appendChild(script);
                        container.dataset.loaded = 'true';
                    } else {
                        container.style.display = 'block';
                    }
                });
            </script>
            """,
            height=360,
        )


# PAGE 5: CELEBRATION (Bollywood Ending)
elif st.session_state.step == 5:
    scroll_top()
    st.balloons()

    st.markdown("<h1 style='text-align:center;'>YAY! 🥰</h1>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center; font-size:18px;'>"
        "Love you, my Valentine ❤️<br>"
        "Just like every day… I choose you."
        "</p>",
        unsafe_allow_html=True
    )

    # st.markdown("Bollywood ending. Husband approved. ❤️")
    st.space("small")
    col1, col2, col3 = st.columns([1, 2, 1])
    # col2.image(
    #     "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGg5N2Q0NzE3czB2dmNvbHNsZHF1Z2Z3Nnd2MjRobHk3bjgwdXFyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qFmdpUKAFZ6rMobzzu/giphy.gif",
    #     width=400
    # )

    with open("gif1.gif", "rb") as gif_file:
        gif_bytes = gif_file.read()
    gif_base64 = base64.b64encode(gif_bytes).decode("utf-8")
    col2.markdown(
        f"""
        <div style="display:flex; justify-content:center;">
            <div style="width:400px; height:550px; overflow:hidden; border-radius:20px;">
                <img src="data:image/gif;base64,{gif_base64}" style="width:400px; margin-top:-120px;"/>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.space("small")

    st.markdown(
        "<p style='text-align:center;'>"
        "Now close this tab, come give me a hug… and let’s celebrate properly 😌"
        "</p>",
        unsafe_allow_html=True
    )

    # st.space("small")
    st.markdown("### 🎁 Surprise")

    st.write("Show me this page tonight.")
    st.write("Dinner + dessert is on me 😌")

    if right_button("Start over?", key="start_over"):
        st.session_state.step = 1
        st.rerun()


# --- BACK BUTTON ---
if st.session_state.step > 1 and st.session_state.step < 5:
    if left_button("⬅️ Back", key="back_button"):
        prev_step()
