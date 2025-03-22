import streamlit as st
import datetime
import time

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday, Neema!",
    page_icon="🎉",
    layout="centered"
)

# Custom CSS for envelope animation and hidden message
st.markdown(
    """
    <style>
    body {
        background-color: #FFFAF0;
        color: #8B0000;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    .envelope-container {
        position: relative;
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }
    .envelope {
        width: 200px;
        height: 150px;
        background: #E74C3C;
        position: relative;
        border-radius: 10px;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .flap {
        position: absolute;
        top: 0;
        left: 0;
        width: 200px;
        height: 100px;
        background: #C0392B;
        border-radius: 10px 10px 0 0;
        transition: transform 1s ease-in-out;
    }
    .message {
        display: none;
        font-size: 18px;
        font-weight: bold;
        color: #E74C3C;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main heading
st.markdown("<h1>🎂 Happy Birthday, Neema! 🎂</h1>", unsafe_allow_html=True)

# Envelope section
st.markdown(
    """
    <div class='envelope-container' onclick='openEnvelope()'>
        <div class='envelope'>
            <div class='flap' id='flap'></div>
            <p style='color: white; font-weight: bold;'>Tap to Open</p>
        </div>
    </div>
    <div class='message' id='message'>🎉 Happy Birthday, Neema! 🎉<br> Wishing you joy, love, and endless happiness! 💖</div>
    <script>
    function openEnvelope() {
        document.getElementById('flap').style.transform = 'rotateX(180deg)';
        setTimeout(() => {
            document.getElementById('message').style.display = 'block';
        }, 1000);
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Display current date
current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
st.markdown(f"<div style='text-align: center;'>Today's Date: {current_date}</div>", unsafe_allow_html=True)

# Confetti animation
st.balloons()

# Special wish section
st.success("🎉 Happy Birthday, Neema! You are truly special and loved. Wishing you all the best! 🎈")
