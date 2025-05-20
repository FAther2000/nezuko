import speech_recognition as sr
import openai
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play

# Nezuko Intro
def speak(text):
    print(f"Nezuko: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    play(sound)

# Voice to Text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nezuko is listening... 🎤")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Nezuko didn't understand that.")
        return None

# ChatGPT Response
def ask_chatgpt(prompt):
    openai.api_key = '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'  # 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

# Main Loop
if __name__ == "__main__":
    speak("Hello! I'm Nezuko, your cute bartender! What drink would you like?")
    while True:
        user_input = listen()
        if user_input:
            if "exit" in user_input.lower():
                speak("Bye bye! Nezuko signing off!")
                break
            reply = ask_chatgpt(f"You are an AI bartender named Nezuko. Answer this: {user_input}")
            speak(reply)
