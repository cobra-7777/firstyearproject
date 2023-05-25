import speech_recognition as sr
                                      
r = sr.Recognizer()                         # Initialize recognizer class 
                                                        
audio = sr.AudioFile("harvard.wav")         # Path of the audio object

with audio as source:                       # Read audio object and transcribe
    audio = r.record(source)                  
    sr_result = r.recognize_google(audio)
    
print(sr_result)