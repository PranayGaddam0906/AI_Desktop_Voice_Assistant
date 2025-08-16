import streamlit as st
import pyttsx3
from datetime import datetime
import webbrowser

# ------------------------------
# Page Setup
# ------------------------------
st.set_page_config(
    page_title="AI Desktop Voice Assistant",
    page_icon="🤖",
    layout="centered"
)
st.title("🤖 AI Desktop Voice Assistant Demo")

# Instructions
st.markdown("""
**How to use this demo:**
- Type a command in the input box and click "Speak Command"
- Or click the buttons below for quick actions
- Buttons simulate desktop assistant features
""")

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ------------------------------
# Custom Command Input
# ------------------------------
command = st.text_input("Type a command here:")

if st.button("Speak Command"):
    if command:
        speak(command)
        st.success(f"Spoken: {command}")
    else:
        st.warning("Please enter a command first!")

# ------------------------------
# Quick Action Buttons
# ------------------------------
st.markdown("---")
st.write("Quick Demo Actions:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Open Google"):
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        
with col2:
    if st.button("Open YouTube"):
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

with col3:
    if st.button("Open Wikipedia"):
        speak("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("Show Time"):
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
        st.info(f"Current time: {now}")

with col5:
    if st.button("Say Hello"):
        speak("Hello! I am your AI assistant.")
        st.success("Hello! I am your AI assistant.")

with col6:
    if st.button("Give Tip"):
        tip = "Stay focused and keep learning AI every day!"
        speak(tip)
        st.info(tip)

# ------------------------------
# Supported Commands Panel
# ------------------------------
st.markdown("---")
st.subheader("Supported Commands in Demo")
st.write("""
- Speak any text using the input box
- Open Google, YouTube, Wikipedia
- Show current time
- Say Hello
- Get a motivational tip
""")
