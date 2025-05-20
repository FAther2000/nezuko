import edge_tts
import asyncio

# 🎤 Voice Options Menu
print("🎤 Choose Nezuko's voice:")
print("1. Natasha (Aussie playful vibe)")
print("2. Aria (Soft & sweet American)")
print("3. Libby (Charming British)")
print("4. Jenny (Natural friendly American)")

choice = input("Enter 1, 2, 3, or 4: ")

# 🎙️ Assign voice based on choice
if choice == "1":
    voice = "en-AU-NatashaNeural"
elif choice == "2":
    voice = "en-US-AriaNeural"
elif choice == "3":
    voice = "en-GB-LibbyNeural"
elif choice == "4":
    voice = "en-US-JennyNeural"
else:
    print("Invalid choice! Defaulting to Aria.")
    voice = "en-US-AriaNeural"

# 🗣️ Get User's custom text
text = input("🗣️ What should Nezuko say? ")

# 🐢 Slow down a bit for cuteness
rate = "-20%"

# 🔊 Main TTS function
async def main():
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save("nezuko_test.mp3")
    print(f"✅ Nezuko ({voice}) said it! File saved as 'nezuko_test.mp3'.")

# 🚀 Run async
asyncio.run(main())

