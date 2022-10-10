from logging import exception
import speech_recognition as sr
import sys

try:
    duration = int(sys.argv[1])
except:
    print('python live-speech-to-text.py to 5 sec\nnext time enter in this format:python live-speech-to-text.py <time-to-run>')
    duration = 5
r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)
