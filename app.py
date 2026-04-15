import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

    .main {
        background: linear-gradient(135deg, #fff5f7 0%, #fde2e4 100%);
    }
    
    .birthday-msg {
        font-family: 'Dancing Script', cursive;
        color: #d63384;
        text-align: center;
        font-size: 3.5rem;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .sub-msg {
        font-family: 'Poppins', sans-serif;
        color: #555;
        text-align: center;
        font-size: 1.3rem;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Collage Styling */
    .img-container {
        border-radius: 20px;
        transition: transform 0.3s ease-in-out;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    .img-container:hover {
        transform: scale(1.05) rotate(2deg);
    }
    </style>
    """, unsafe_allow_html=True)


if 'celebrate' not in st.session_state:
    st.session_state.celebrate = False


st.write("<h1 style='text-align: center; color: #ff4b2b;'>💖 A Special Celebration 💖</h1>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,1,1])
with col2:
    if not st.session_state.celebrate:
        if st.button("Celebrate 🎂", use_container_width=True):
            st.session_state.celebrate = True
            st.balloons()

if st.session_state.celebrate:
    
    
    music_url = "https://www.bensound.com/bensound-music/bensound-memories.mp3"
    st.markdown(f"""
        <audio autoplay loop>
            <source src="{music_url}" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

    # 2. Lottie Confetti Animation
    components.html("""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <div style="display: flex; justify-content: center;">
            <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_u4yrau.json" background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></lottie-player>
        </div>
    """, height=300)

    # 3. Birthday Message
    st.markdown("""
        <div class="birthday-msg">Happy Birthday! 🎉</div>
        <div class="sub-msg">
            You are doing amazing in your life, and I am truly proud of you.<br>
            Keep going, keep shining, and never stop believing in yourself.<br>
            One day, you will achieve everything you dream of.<br>
            All the best for your journey ahead — just keep cheering and smiling! 😊
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # 4. PHOTO COLLAGE (8 Local Images)
    st.write("<h2 style='text-align: center; font-family: Dancing Script;'>I selected the top-tier pictures of yours. With each one you looked better, so I chose the best ones. ✨</h2>", unsafe_allow_html=True)
    
    # List of your local filenames
    photo_files = ["pic1.jpeg", "pic2.jpeg", "pic3.jpeg", "pic4.jpeg", 
                   "pic5.jpeg", "pic6.jpeg", "pic7.jpeg", "pic8.jpeg"]

    # Grid layout for collage (2 rows of 4)
    row1 = st.columns(4)
    row2 = st.columns(4)
    
    for i, col in enumerate(row1 + row2):
        file_path = photo_files[i]
        if os.path.exists(file_path):
            with col:
                # Open image to ensure it displays nicely
                img = Image.open(file_path)
                st.image(img, use_container_width=True, caption=f"gorgeous {i+1}")
                st.markdown('<div class="img-container"></div>', unsafe_allow_html=True)
        else:
            col.warning(f"File {file_path} not found!")

    # 5. Interactive Candle Section
    st.markdown("---")
    st.write("<h3 style='text-align: center;'>🕯️ Make a Wish 🕯️</h3>", unsafe_allow_html=True)
    
    candle_html = """
    <div style="text-align: center;">
        <div id="candle" style="font-size: 80px; cursor: pointer;">🎂🕯️</div>
        <p style="font-family: Poppins;">Click the cake to blow the candles!</p>
    </div>
    <script>
    const candle = document.getElementById('candle');
    candle.onclick = function() {
        candle.innerHTML = '🎂💨';
        candle.style.transition = '2s';
        alert('Make a big wish! ✨');
    };
    </script>
    """
    components.html(candle_html, height=200)

else:
    st.markdown("<p style='text-align: center;'>Ready for the surprise?</p>", unsafe_allow_html=True)
