import sounddevice as sd
import wavio
from time import sleep
from datetime import date


def start_recording():

    def record_audio(fs, channels, filename):
        # Start recording
        recording = sd.rec(int(fs), samplerate=fs, channels=channels)
        sd.wait()

        # Save audio to WAV file
        wavio.write(filename, recording, fs, sampwidth=2)

    # Set the recording parameters
    fs = 44100  # Sample rate
    channels = 1  # Number of audio channels
    filename = "Recorded Lecture " + date.today()  # Output filename

    is_recording = False

    while True:
        button_state = read_button_state()  # Function to read button state here

        if button_state == 'pressed' and not is_recording:
            # Start recording
            print("Recording started..")
            record_audio(fs, channels, filename)
            is_recording = True
            print("Recording saved as ", filename)

        elif button_state == 'pressed' and is_recording:
            # Stop recording
            print("Recording stopped.")
            is_recording = False
            break

        sleep(0.1)