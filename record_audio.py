import sounddevice as sd
from scipy.io.wavfile import write

# Settings
duration = 5  # seconds
fs = 44100  # Sample rate (CD quality)

print("Recording started... 🎤")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Wait until recording is finished
write('test.wav', fs, recording)
print("Recording finished. Saved as test.wav ✅")

