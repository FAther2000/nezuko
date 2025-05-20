import random
import os
import requests
from azure_config import AZURE_KEY, AZURE_REGION

libby_lines = [
    "Hello, darling. What can I prepare for you today?",
    "Care for a lovely drink? Just say the word.",
    "Tell me your order, love. I’m all ears.",
    "Fancy a tipple? What shall it be?",
    "Your personal bartender at your service. What’ll you have?",
    "Feeling adventurous or shall we keep it classic?",
    "Right then, let’s mix up something delightful, shall we?",
    "Go on, tell me your drink of choice.",
    "I’m ready when you are. What can I get you?",
    "It’s a lovely day for a lovely drink, don’t you think?",
    "Your drink is served, love. Cheers!",
    "If you fancy another, you know who to ask.",
    "Quick as a flash, your drink’s ready.",
    "One sip and you'll be chuffed, I promise.",
    "Not to brag, but I'm rather good at this bartending business."
]

def synthesize_speech(text, voice_name="en-GB-LibbyNeural", filename="nezuko_libby.wav"):
    endpoint = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    }

    ssml = f"""
    <speak version='1.0' xml:lang='en-GB'>
        <voice name='{voice_name}'>{text}</voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=ssml.encode('utf-8'))

    if response.status_code == 200:
        with open(filename, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"✅ Libby said: {text}")
        os.system(f"aplay {filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# Run Libby with random line
selected_line = random.choice(libby_lines)
synthesize_speech(selected_line)

