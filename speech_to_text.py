import speech_recognition as sr
                                      
r = sr.Recognizer()

def transcribe_audio(file_path):
    retries = 0
    success = False
    while retries <= 5 and success == False:
        try:
            audio = sr.AudioFile(file_path)
            with audio as source:                           
                audio = r.record(source)                  
                sr_result = r.recognize_google(audio)
                print("Audio transcribed!")
            success = True
        except:
            if retries >= 5:
                print("Critical error, audio transcription has failed multiple times. Stopping program...")
                break
            else:
                retries = retries + 1
                print("The speech to text conversion failed... Retrying for the " + str(retries) + " time...")
    
    return(sr_result)


