import random
import os
import requests
from azure_config import AZURE_KEY, AZURE_REGION

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
    "Don’t be shy, tell me what you’re after.",
    "Cheers, mate! Your drink’s ready to enjoy.",
    "Fancy another round? Just holler.",
    "Quick and easy, just like we like it.",
    "This one’s going to be a ripper, promise!",
    "You're gonna love this drink, I can tell."
]

def synthesize_speech(text, voice_name="en-AU-NatashaNeural", filename="nezuko_natasha.wav"):
    endpoint = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    }

    ssml = f"""
    <speak version='1.0' xml:lang='en-AU'>
        <voice name='{voice_name}'>{text}</voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=ssml.encode('utf-8'))

    if response.status_code == 200:
        with open(filename, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"✅ Natasha said: {text}")
        os.system(f"aplay {filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# Run Natasha with random line
selected_line = random.choice(natasha_lines)
synthesize_speech(selected_line)

