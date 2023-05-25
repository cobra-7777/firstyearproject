import speech_recognition as sr
                                      
r = sr.Recognizer()                                
                                                        
audio = sr.AudioFile("harvard.wav")                 

try:
    with audio as source:                           
        audio = r.record(source)                  
        sr_result = r.recognize_google(audio)
    print(sr_result)
except:
    print("The speech to text conversion failed...")