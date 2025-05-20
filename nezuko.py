import speech_recognition as sr
import openai
from gtts import gTTS
import os
import sys


original_stderr = sys.stderr

print("🍸 Nezuko Bartender is ready!")

# OpenAI API Key 
openai.api_key = "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"

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Nezuko is listening... Speak now!")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"👤 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Nezuko couldn't understand you.")
        return ""
    except sr.RequestError:
        print("Speech Recognition service error.")
        return ""

def chat_with_nezuko(prompt):
    try:
        # Updated to use current OpenAI API format
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content.strip()
        print(f"Nezuko: {reply}")
        return reply
    except Exception as e:
        print(f"ChatGPT Error: {e}")
        return "I'm having a bit of a brain freeze, please try again."

def speak(text):
    try:
        # Save as MP3
        tts = gTTS(text=text, lang='en')
        tts.save("nezuko_voice.mp3")
        
        # Try multiple audio playback methods
        success = False
        
        try:
            import playsound
            print("Trying playsound...")
            playsound.playsound("nezuko_voice.mp3")
            print("✓ playsound successful")
            success = True
        except (ImportError, Exception) as e:
            print(f"× playsound failed: {e}, trying Sox...")
            
            sox_result = os.system("play -q nezuko_voice.mp3 2>/dev/null")
            if sox_result == 0:
                print("✓ Sox play successful")
                success = True
            else:
                print("× Sox failed, trying mpg123...")
                
            
                mpg_result = os.system("mpg123 -q -o alsa:nezuko nezuko_voice.mp3 2>/dev/null")
                if mpg_result == 0:
                    print("✓ mpg123 playback with nezuko device successful")
                    success = True
                else:
                    print("× mpg123 with nezuko device failed, trying default...")
                    
                    
                    mpg_result = os.system("mpg123 -q nezuko_voice.mp3 2>/dev/null")
                    if mpg_result == 0:
                        print("✓ mpg123 playback successful")
                        success = True
                    else:
                        print("× All audio playback methods failed")
                        print("Try installing: sudo apt-get install sox libsox-fmt-mp3")
                        
        # Clean up
        os.remove("nezuko_voice.mp3")
        if os.path.exists("nezuko_voice.wav"):
            os.remove("nezuko_voice.wav")
            
        return success
    except Exception as e:
        print(f"Audio Error: {e}")
        return False

# Main Loop
while True:
    user_input = recognize_speech()
    if user_input:
        response = chat_with_nezuko(user_input)
        success = speak(response)
        if not success:
            print("Failed to play audio. Check your audio configuration.")
