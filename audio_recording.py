import sounddevice as sd
from scipy.io.wavfile import write
 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 10
 
# Start recorder with the given values of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
 
# Record audio for the given number of seconds
print("Recording...")
sd.wait()
 
# This will convert the NumPy array to an audio file with the given sampling frequency
print("Finished recording.")
write("resources/recording0.wav", freq, recording)