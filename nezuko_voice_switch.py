import os
import requests

AZURE_KEY = "G8Tkkf8JSfWVeiXfsdz8IBKNYfEZottZYBtPhiGBrhDil7HE9YKPJQQJ99BEACYeBjFXJ3w3AAAYACOGSkFH"
AZURE_REGION = "eastus"

VOICE_MAP = {
    "aussie": "en-AU-NatashaNeural",
    "british": "en-GB-LibbyNeural",
    "american": "en-US-JennyNeural"
}

def nezuko_speak(text, voice="aussie", filename="nezuko_voice.wav"):
    if voice not in VOICE_MAP:
        print(f"❗ Unknown voice '{voice}'. Available: {list(VOICE_MAP.keys())}")
        return

    selected_voice = VOICE_MAP[voice]

    endpoint = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    }

    ssml = f"""
    <speak version='1.0' xml:lang='{selected_voice.split('-')[0]}'>
        <voice name='{selected_voice}'>{text}</voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=ssml.encode('utf-8'))

    if response.status_code == 200:
        with open(filename, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"✅ Nezuko ({voice}) says: '{text}'")
        os.system(f"aplay {filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# Test lines:
nezuko_speak("Alrighty, what drink are we mixing up today, mate?", voice="aussie")
nezuko_speak("Hello love, what drink shall I prepare for you today?", voice="british")
nezuko_speak("Hey there! What can I get you to drink?", voice="american")
