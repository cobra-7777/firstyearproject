import sounddevice as sd
import wavio
from datetime import date
import serial

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def record_audio(duration, fs, channels, filename):
    # Record audio
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()

    # Save audio to WAV file
    wavio.write(filename, recording, fs, sampwidth=2)

# Set the recording parameters
duration = 5  # Duration in seconds
fs = 44100  # Sample rate
channels = 1  # Number of audio channels
filename = 'Undervisning: ' + str(date.today()) + '.wav'  # Output filename


while True:
    try:
        if ser.inWaiting():
            received_message = ser.readline() # the message send from esp32 needs to have a \n newline in the end
            print(received_message.decode().strip())
            test = int(received_message.decode().strip())
            
            if test == 1:
                print("Recording..")
                record_audio(60, 44100.0, 1, filename)
                print("Recording saved as", filename)

            if test == 3:
                print("Listening..")




    except KeyboardInterrupt:
        ser.close()