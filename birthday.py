import streamlit as st
import datetime
import time

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday, Neema!",
    page_icon="🎉",
    layout="centered"
)

# Custom CSS for elegant animation
st.markdown(
    """
    <style>
    body {
        background-color: #fff5e6;
        color: #d6336c;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .card {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        width: 300px;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 5px 5px 20px rgba(0,0,0,0.2);
        margin: auto;
        animation: fadeIn 2s ease-in-out;
    }
    .card h2 {
        font-size: 24px;
        color: white;
    }
    .heart {
        font-size: 50px;
        color: red;
        animation: heartbeat 1.5s infinite;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.8); }
        to { opacity: 1; transform: scale(1); }
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main heading
st.markdown("<h1>🎂 Happy Birthday, Neema! 🎂</h1>", unsafe_allow_html=True)

# Birthday Card Section
st.markdown(
    """
    <div class='card'>
        <h2>Happy Birthday, Neema! 🎉</h2>
        <p>May your day be filled with love, laughter, and endless happiness! 💖</p>
        <div class='heart'>❤️</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Display current date
current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
st.markdown(f"<div style='text-align: center; margin-top: 20px;'>Today's Date: {current_date}</div>", unsafe_allow_html=True)

# Confetti animation
st.balloons()

# Special wish section
st.success("🎉 Happy Birthday, Neema! You are truly special and loved. Wishing you all the best! 🎈")

