import sounddevice as sd
import wave

# Parameters for recording
samplerate = 44100  # Sample rate (44.1 kHz is standard)
duration = 5       # Duration of the recording in seconds
channels = 2        # Number of channels (stereo)

# File to save the recording
filename = "recorded_audio.wav"

# Function to record audio
def record_audio(filename, samplerate, duration, channels):
    print(f"Recording for {duration} seconds...")
    try:
        # Record audio
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording finished. Saving file...")

        # Save as a WAV file
        with wave.open(filename, 'w') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)  # 2 bytes (16 bits)
            wf.setframerate(samplerate)
            wf.writeframes(audio.tobytes())

        print(f"Audio saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
record_audio(filename, samplerate, duration, channels)