import speech_recognition as sr
import edge_tts
import openai
import asyncio

# OpenAI API Key 
openai.api_key = "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"

# Default Nezuko Voice
nezuko_voice = "en-AU-NatashaNeural"
nezuko_rate = "-20%"

# Nezuko speaks function
async def nezuko_speak(text):
    communicate = edge_tts.Communicate(text, nezuko_voice, rate=nezuko_rate)
    await communicate.save("nezuko_response.mp3")
    print(f"🎤 Nezuko said: {text}")
    os.system("mpg123 nezuko_response.mp3")

# Listen to user input
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command
    except sr.UnknownValueError:
        print("❌ Sorry, I didn't catch that.")
        return None

# Get ChatGPT response
def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Nezuko, a sassy but cute bartender. Be playful and charming."},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response.choices[0].message.content.strip()
    return reply

# Main loop
async def main():
    await nezuko_speak("Hello darling! Welcome to Nezuko's bar. How can I make your day better?")
    while True:
        command = listen_command()
        if command:
            if "exit" in command.lower() or "bye" in command.lower():
                await nezuko_speak("Alright, see you next time sweetie!")
                break
            response = get_gpt_response(command)
            await nezuko_speak(response)

# Run program
if __name__ == "__main__":
    import os
    asyncio.run(main())
