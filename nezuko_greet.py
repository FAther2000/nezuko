from gtts import gTTS
import os

# Text to say
text = "Hi, I am Nezuko, your AI bartender."

# Convert text to speech
tts = gTTS(text=text, lang='en', tld='com', slow=False)
tts.save("nezuko_greeting.mp3")

# Play the audio
os.system("mpg123 nezuko_greeting.mp3")
