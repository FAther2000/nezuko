import edge_tts
import asyncio

# User custom input
text = input("🗣️ What should Nezuko say? ")

# Japanese-accented voice model
voice = "ja-JP-NanamiNeural"

# Speaking rate adjustment
rate = "-20%"

async def main():
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save("nezuko_test.mp3")
    print("✅ Nezuko said it! File saved as 'nezuko_test.mp3'.")

# Run the async function
asyncio.run(main())

