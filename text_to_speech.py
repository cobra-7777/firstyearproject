from gtts import gTTS
import os

def tts_process_and_play(input_text):
    tts = gTTS(text=input_text, lang='en', slow=False)
    tts.save("resources/tts_result.mp3")
    os.system("start resources/tts_result.mp3")