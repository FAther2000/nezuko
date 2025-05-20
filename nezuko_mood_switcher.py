import random
import os
import requests
from azure_config import AZURE_KEY, AZURE_REGION

libby_lines = [
    "Hello there, what drink can I prepare for you today?",
    "Ready for a delightful sip? Let me know your order.",
    "Good choice! Let’s get that drink ready.",
    "I'm here to make your perfect drink. What'll it be?",
    "Let’s craft something delicious together.",
    "The bar is open! What can I get you?",
    "Tell me your order, I'll handle the magic.",
    "Cheers! One drink coming right up.",
    "Ready to serve your next favourite drink.",
    "Just say the word, and your drink is on the way."
]

natasha_lines = [
    "Hey there, what drink are we whipping up today?",
    "Alrighty, tell me your order and I’ll get right on it.",
    "Feeling like a cheeky drink? I’m ready when you are.",
    "Oi, thirsty? Let's fix that, shall we?",
    "What'll it be, mate? The bar’s all yours.",
    "Crikey, you’ve come to the right place for a good time.",
    "Alright, time to mix up something tasty!",
    "Hit me with your drink order, let’s do this.",
    "One drink coming right up, Aussie style!",
    "Don’t be shy, tell me what you’re after."
]

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
        print(f"✅ Nezuko said: {text} ({voice_name})")
        os.system(f"aplay {filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# === Mood Switcher ===
mood = input("Select mood (libby/natasha): ").strip().lower()

if mood == "libby":
    selected_line = random.choice(libby_lines)
    synthesize_speech(selected_line, "en-GB-LibbyNeural")
elif mood == "natasha":
    selected_line = random.choice(natasha_lines)
    synthesize_speech(selected_line, "en-AU-NatashaNeural")
else:
    print("❌ Invalid mood selection. Please choose 'libby' or 'natasha'.")

