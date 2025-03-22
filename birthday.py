import streamlit as st

# Set page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# Main heading
st.title("🎉 Happy Birthday! 🎈")

# Birthday message
st.write(
    """
    **Wishing you a fantastic day filled with joy, laughter, and love!** 🎂🎁🎊
    May this year bring you all the success and happiness you deserve.
    """
)

# Display a birthday image
st.image(
    "https://images.unsplash.com/photo-1515543237356-5f0d2740b117", 
    caption="Enjoy your special day!", use_column_width=True
)

# Play a birthday song
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format='audio/mp3')

# Confetti animation
st.balloons()

# Personalized birthday wishes
name = st.text_input("Enter your name to send wishes:")
if name:
    st.success(f"🎉 {name} sends you warm birthday wishes! 🎈")
