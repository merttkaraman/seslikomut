import webbrowser
from datetime import datetime
import time
from tkinter import StringVar

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os

from django.templatetags.i18n import language
from win32ctypes.pywin32.pywintypes import datetime

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
           voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
           speak("Sizi anlayamadım.")
        except sr.RequestError:
            speak("Sistem Hatası.")
        return voice

def response(voice):
    if "nasılsın" in voice:
        speak("iyi senden")
    if "saat kaç" in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if "arama yap" in voice:
        search = record("ne aramak istiyorsun?")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak(search + " için bulduklarım")
    if "tamamdır" in voice:
        speak("Görüşürüz.")
        exit()

def speak(string):
    tts = gTTS(string, lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Nasıl yardımcı olabilirim?")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
