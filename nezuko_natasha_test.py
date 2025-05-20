import os
import requests

AZURE_KEY = "G8Tkkf8JSfWVeiXfsdz8IBKNYfEZottZYBtPhiGBrhDil7HE9YKPJQQJ99BEACYeBjFXJ3w3AAAYACOGSkFH"
AZURE_REGION = "eastus"

def synthesize_speech(text, filename="nezuko_natasha.wav"):
    endpoint = f"https://{AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    }

    ssml = f"""
    <speak version='1.0' xml:lang='en-AU'>
        <voice name='en-AU-NatashaNeural'>{text}</voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=ssml.encode('utf-8'))

    if response.status_code == 200:
        with open(filename, "wb") as audio_file:
            audio_file.write(response.content)
        print(f"✅ Speech saved as {filename}")
        os.system(f"aplay {filename}")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

# Test message
nezuko_line = "G'day! What drink would you like me to make for you, mate?"
synthesize_speech(nezuko_line)

