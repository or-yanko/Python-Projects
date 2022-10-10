import gtts
from playsound import playsound
import speech_recognition as sr
import sys

x = input('press 1 to convert text to speech\npress 2 to convert speech to text\t')
if x == '1':
    landict = gtts.lang.tts_langs()

    print('available languages:')
    for i in landict:
        print(f"for {landict[i]}\tenter\t{i}")

    lang = input('enter languages:\t\t')
    txt = input('enter sentence to convert:\t')
    tts = gtts.gTTS(txt, lang=lang)
    tts.save("speech.mp3")
    if input('play is? y/n\t').lower() == 'y':
        playsound("speech.mp3")
    exit()

filename = input(
    'enter filename(make sure it on your current working directory)')
if filename == '':
    filename = 'speech.mp3'

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
