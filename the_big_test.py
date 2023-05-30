import speech_to_text as stt
import gpt_api as gpt
import text_to_docfile as ttd
from time import sleep

stt_result = stt.transcribe_audio("resources/plane crash tedtalk.wav")
print(stt_result)

sleep(5)

gpt_result = gpt.gpt_request(stt_result)
print(gpt_result)

sleep(5)

ttd.text_to_doc("A Document Title", gpt_result)

sleep(5)

print("You should now have a DOCS file with the most important points of the .wav file")