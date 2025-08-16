import streamlit as st
import pyttsx3
from datetime import datetime
import webbrowser

st.set_page_config(page_title="AI Desktop Voice Assistant", page_icon="🤖", layout="centered")
st.title("🤖 AI Desktop Voice Assistant Demo")
st.write("Simulate voice commands and see text-to-speech output.")

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Text input for custom commands
command = st.text_input("Type a command here:")

if st.button("Speak Command"):
    if command:
        speak(command)
        st.success(f"Spoken: {command}")
    else:
        st.warning("Please enter a command first!")

# Buttons for common demo actions
st.markdown("---")
st.write("Quick demo actions:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Open Google"):
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

with col2:
    if st.button("Show Time"):
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
        st.info(f"Current time: {now}")

with col3:
    if st.button("Say Hello"):
        speak("Hello! I am your AI assistant.")
        st.success("Hello! I am your AI assistant.")

st.markdown("---")
st.write("This demo simulates voice commands in the browser using text input and buttons.")
