import streamlit as st
import datetime

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday, Neema!",
    page_icon="🎉",
    layout="centered"
)

# Apply custom CSS for background color and font
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
    </style>
    """,
    unsafe_allow_html=True
)

# Main heading with emoji
st.markdown("<h1 style='text-align: center;'>🎂 Happy Birthday, Neema! 🎂</h1>", unsafe_allow_html=True)

# Birthday message
st.markdown(
    """
    <div style='text-align: center;'>
        <p><strong>Wishing you a day filled with happiness and a year filled with joy, Neema!</strong></p>
        <p>May your special day be as amazing as you are. 🎈🎁</p>
    </div>
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
