import pyaudio
import wave

# Parameters
device_index = 0  # You already checked your mic index is 0
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "mic_test.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open Stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    input_device_index=device_index,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record Audio
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop & Close Stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save to WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Saved recording to {WAVE_OUTPUT_FILENAME}")

