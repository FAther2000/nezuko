from gtts import gTTS
import os

text = "Hello! I am Nezuko, your cute bartender. How can I help you today?"

tts = gTTS(text=text, lang='en')
tts.save("gtts_greeting.mp3")
os.system("mpg123 gtts_greeting.mp3")

