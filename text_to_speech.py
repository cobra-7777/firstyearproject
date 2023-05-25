from gtts import gTTS
import os

def tts_process_and_play(input_text):
    retries = 0
    success = False
    while retries <= 5 and success == False:
        try:
            tts = gTTS(text=input_text, lang='en', slow=False)
            tts.save("resources/tts_result.mp3")
            os.system("start resources/tts_result.mp3")
            success = True
        except:
            if retries >= 5:
                print("Critical error, text to speech module has failed multiple times. Stopping program...")
                break
            else:
                retries = retries + 1
                print("The text to speech module has failed... Retrying for the " + str(retries) + " time...")