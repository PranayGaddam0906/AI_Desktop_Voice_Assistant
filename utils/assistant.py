import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime
from utils.commands import execute_command

class Assistant:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self):
        hour = datetime.now().hour
        if hour < 12:
            self.speak("Good Morning!")
        elif hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I am your desktop assistant. How can I help you today?")

    def listen_commands(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    voice = self.listener.listen(source)
                    command = self.listener.recognize_google(voice)
                    command = command.lower()
                    print(f"Command: {command}")
                    execute_command(command, self.speak)
            except Exception as e:
                print("Error:", e)
