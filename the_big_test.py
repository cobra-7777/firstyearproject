import speech_to_text as stt
import gpt_api as gpt
from time import sleep

stt_result = stt.transcribe_audio("resources/harvard.wav")
print(stt_result)

sleep(5)

gpt_result = gpt.gpt_request(stt_result)
print(gpt_result)

sleep(5)

print("You should now have a transcribed version of the .wav file, and a version where ChatGPT attempted to extract the most important information of the transcription.")