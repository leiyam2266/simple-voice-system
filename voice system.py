import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import tempfile
import datetime
import time

t = time.time()
dt = datetime.datetime.fromtimestamp(t)
dt_1 = datetime.datetime.fromtimestamp(t).strftime('%d')
dt_4 = datetime.datetime.fromtimestamp(t).strftime('%m')
Speech = ''
r = sr.Recognizer()


def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)


if dt_4 == "01":
    dt_4 = "January"
if dt_4 == "02":
    dt_4 = "February"
if dt_4 == "03":
    dt_4 = "March"
if dt_4 == "04":
    dt_4 = "April"
if dt_4 == "05":
    dt_4 = "may"
if dt_4 == "06":
    dt_4 = "June"
if dt_4 == "07":
    dt_4 = "July"
if dt_4 == "08":
    dt_4 = "August"
if dt_4 == "09":
    dt_4 = "September"
if dt_4 == "10":
    dt_4 = "October"
if dt_4 == "11":
    dt_4 = "November"
if dt_4 == "12":
    dt_4 = "December"

while True:

    with sr.Microphone() as source:
        speak("how can I help you....",'en')
        print("how can I help you....")
        time.sleep(3)
        audio = r.listen(source)
    Speech = r.recognize_google(audio, language='en-US')

    if Speech == "what day is it":
        speak("today is" + dt_4 + " of " + dt_1, 'en')
        time.sleep(3)
    else:
        speak("say it again", 'en')