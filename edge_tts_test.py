import edge_tts
import asyncio

# Greeting text for Nezuko in English with Japanese accent
text = "Hello! I am Nezuko, your bartender. How can I help you today?"

# Japanese-accented voice model
voice = "ja-JP-NanamiNeural"

async def main():
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("nezuko_greeting.mp3")
    print("✅ Nezuko's greeting has been generated as 'nezuko_greeting.mp3'.")

# Run the async function
asyncio.run(main())

