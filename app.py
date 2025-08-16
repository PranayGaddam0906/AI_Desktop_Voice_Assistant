import streamlit as st
import pyttsx3
import speech_recognition as sr

st.title("AI Desktop Voice Assistant Demo")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

st.write("Type a command below or simulate a voice command:")

command = st.text_input("Command:")

if st.button("Speak"):
    if command:
        speak(command)
        st.success(f"Spoken: {command}")
    else:
        st.warning("Please enter a command.")
