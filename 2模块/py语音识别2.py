# -*- coding: utf-8 -*-
import speech_recognition as sr
AUDIO_FILE = r"C:\Users\69598\Downloads\Music\paju5-bxw6n.wav"
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

res = r.recognize_sphinx(audio)
res1 = res.split(" ")
# for each in res1:
print(" ".join(res1))