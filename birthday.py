import streamlit as st
import datetime
import time

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday, Neema!",
    page_icon="🎉",
    layout="centered"
)

# Apply custom CSS for background color, font, and animation
st.markdown(
    """
    <style>
    body {
        background-color: #FFFAF0;
        color: #8B0000;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    .envelope {
        position: relative;
        width: 150px;
        height: 100px;
        background: #E74C3C;
        margin: auto;
        border-radius: 10px 10px 0 0;
    }
    .flap {
        position: absolute;
        top: 0;
        left: 0;
        width: 150px;
        height: 100px;
        background: #C0392B;
        border-radius: 10px 10px 0 0;
        transform-origin: top;
        animation: openFlap 2s forwards;
    }
    @keyframes openFlap {
        0% { transform: rotateX(0deg); }
        100% { transform: rotateX(180deg); }
    }
    .message {
        position: relative;
        width: 120px;
        height: 80px;
        background: white;
        margin: auto;
        top: -60px;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #E74C3C;
        opacity: 0;
        animation: showMessage 3s forwards;
    }
    @keyframes showMessage {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .hearts {
        position: absolute;
        width: 100%;
        height: 100px;
        overflow: hidden;
    }
    .heart {
        position: absolute;
        width: 20px;
        height: 20px;
        background: red;
        transform: rotate(-45deg);
        animation: floatHearts 5s infinite ease-in-out;
    }
    .heart:before,
    .heart:after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        background: red;
        border-radius: 50%;
    }
    .heart:before { top: -10px; left: 0; }
    .heart:after { left: 10px; top: 0; }
    @keyframes floatHearts {
        0% { transform: translateY(0) rotate(-45deg); opacity: 1; }
        100% { transform: translateY(-100px) rotate(-45deg); opacity: 0; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main heading with emoji
st.markdown("<h1 style='text-align: center;'>🎂 Happy Birthday, Neema! 🎂</h1>", unsafe_allow_html=True)

# Animated envelope with a message inside
st.markdown(
    """
    <div class='envelope'>
        <div class='flap'></div>
    </div>
    <div class='message'>
        🎉 Happy Birthday, Neema! 🎉<br>
        Wishing you joy, love, and endless happiness! 💖
    </div>
    """,
    unsafe_allow_html=True
)

# Display current date
current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
st.markdown(f"<div style='text-align: center;'>Today's Date: {current_date}</div>", unsafe_allow_html=True)

# Confetti animation
st.balloons()

# Floating hearts effect
st.markdown(
    """
    <div class='hearts'>
        <div class='heart' style='left: 10%; animation-delay: 0s;'></div>
        <div class='heart' style='left: 30%; animation-delay: 1s;'></div>
        <div class='heart' style='left: 50%; animation-delay: 2s;'></div>
        <div class='heart' style='left: 70%; animation-delay: 3s;'></div>
        <div class='heart' style='left: 90%; animation-delay: 4s;'></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Special wish section
st.success("🎉 Happy Birthday, Neema! You are truly special and loved. Wishing you all the best! 🎈")
