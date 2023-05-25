import speech_recognition as sr
                                      
r = sr.Recognizer()

def transcribe_audio(file_path):
    try:
        audio = sr.AudioFile(file_path)
        with audio as source:                           
            audio = r.record(source)                  
            sr_result = r.recognize_google(audio)
            print("Audio transcribed!")
    except:
        print("The speech to text conversion failed...")
    
    return(sr_result)