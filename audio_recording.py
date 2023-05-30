import sounddevice as sd
import wavio

def record_audio(duration, fs, channels, filename):
    # Record audio
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()

    # Save audio to WAV file
    wavio.write(filename, recording, fs, sampwidth=2)

# Set the recording parameters
duration = 10  # Duration in seconds
fs = 44100  # Sample rate
channels = 1  # Number of audio channels
filename = 'recording.wav'  # Output filename

# Record and save audio
print("Recording..")
record_audio(duration, fs, channels, filename)
print("Recording saved as", filename)