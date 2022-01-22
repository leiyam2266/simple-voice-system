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

datetime_4_counter_1 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
datetime_4_counter_2 = ["January","February","March","April","may","June","July","August","September","October","November","December"]
Speech = ''
r = sr.Recognizer()

for d_counter_1 in range(0 ,11):
    if dt_4 == datetime_4_counter_1[d_counter_1]:
        dt_4 = datetime_4_counter_2[d_counter_1]
        break
    else:
        d_counter_1 += 1

def speak(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(1)

while True:

    with sr.Microphone() as source:
        speak("how can I help you....",'en')
        print("how can I help you....")
        time.sleep(3)
        audio = r.listen(source)
    Speech = r.recognize_google(audio, language='en-US')

    if Speech == "what day is it":
        speak("today is" + dt_4 + " of " + dt_1, 'en')
        print("today is " + dt_4 + " of " + dt_1)
        time.sleep(3)
    else:
        speak("say it again ,please", 'en')
        print("say it again ,please")
        time.sleep(3)