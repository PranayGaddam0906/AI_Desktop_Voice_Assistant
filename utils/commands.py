import webbrowser
import os

def execute_command(command, speak):
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
    elif "time" in command:
        from datetime import datetime
        time = datetime.now().strftime("%H:%M:%S")
        speak(f"Current time is {time}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")
