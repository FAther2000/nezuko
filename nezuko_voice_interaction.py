import speech_recognition as sr
import openai
import requests
import os
import random
from chatgpt_config import OPENAI_API_KEY
from azure_config import AZURE_KEY, AZURE_REGION

openai.api_key = OPENAI_API_KEY

libby_voice = "en-GB-LibbyNeural"
natasha_voice = "en-AU-NatashaNeural"

# Mood selection
mood = input("Select mood (libby/natasha): ").strip().lower()
voice_name = libby_voice if mood == "libby" else natasha_voice

def listen_to_user():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("📝 Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"❌ Recognition error: {e}")
        return None

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're Nezuko, an AI bartender with a cheeky but friendly personality."},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response.choices[0].message['content'].strip()
    print(f"🤖 Nezuko says: {reply}")
    return reply

def synthesize_speech(text, voice_name, filename="nezuko_voice.wav"):
    endpoint = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    }

    ssml = f"""
    <speak version='1.0' xml:lang='en-US'>
        <voice name='{voice_name}'>{text}</voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=ssml.encode('utf-8'))

    if response.status_code == 200:
        with open(filename, "wb") as audio_file:
            audio_file.write(response.content)
        os.system(f"aplay {filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# === Main Loop ===
while True:
    user_input = listen_to_user()
    if user_input:
        gpt_reply = chat_with_gpt(user_input)
        synthesize_speech(gpt_reply, voice_name)

