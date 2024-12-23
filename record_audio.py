import sounddevice as sd
import numpy
import wave

# Parameters for recording
samplerate = 44100  # Sample rate (44.1 kHz is standard)
duration = 15       # Duration of the recording in seconds
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

# Save left and right channels to separate WAV files
def save_mono_wav(filename, data, sample_rate):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # Bytes per sample
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())

def save_stereo_wav(filename, data, samplerate):
    with wave.open(filename, 'w') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)  # 2 bytes (16 bits)
            wf.setframerate(samplerate)
            wf.writeframes(data.tobytes())

def record_audio_and_save_left_and_right(filename, samplerate, duration, channels):
    print("Recording...")
    audio_data = sd.rec(int(samplerate * duration), samplerate, channels, dtype='int16')
    sd.wait()
    print("Recording finished.")

    # Split channels
    left_channel = audio_data[:, 0]
    right_channel = audio_data[:, 1]
    stereo_channel = audio_data

    save_mono_wav("left_channel.wav", left_channel, samplerate)
    save_mono_wav("right_channel.wav", right_channel, samplerate)
    save_stereo_wav("stereo_channel.wav", stereo_channel, samplerate)

# Call the function
record_audio_and_save_left_and_right(filename, samplerate, duration, channels)