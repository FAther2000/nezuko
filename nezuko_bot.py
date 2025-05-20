import speech_recognition as sr
from gtts import gTTS
import os
import time

def listen_to_user():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Nezuko is listening... 🎤")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Couldn't understand. Please try again.")
        return None
    except sr.RequestError:
        print("Speech Recognition API unavailable.")
        return None

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "nezuko_reply.mp3"
    tts.save(filename)
    os.system(f"mpg123 {filename}")

while True:
    user_input = listen_to_user()
    if user_input:
        response = f"Nezuko heard you say: {user_input}"
        speak(response)
    time.sleep(1)

