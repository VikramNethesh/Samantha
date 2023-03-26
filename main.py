import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import tkinter as tk
from PIL import ImageTk,Image


def primary():
    query = TakeCommand()
    print(query)
    if 'wikipedia' in query:
        speak("Searching Wikipedia......")
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak("According to wikipedia")
        speak(results)

    elif "open" in query:
        x = query.split()
        speak(f"Opening {x[1]}\n")
        webbrowser.open(f"{x[1]}\n.com")


    elif "play music" in query:
        Music()

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")
        Music()

    elif "bye" in query:
        speak("Bye,bye sir")
        run = 2


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour<12:
        speak("Good morning sir")
    elif hour<16:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold= 0.5
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n ")
    except Exception as e:
        print("Say that again please")
        return "none"
    return query.lower()

def Music():
    dir = os.getcwd()
    dir += r"\songs"
    print(dir)
    music_dir = dir
    songs = os.listdir(music_dir)
    y = len(songs)
    song = random.randrange(y - 1)
    os.startfile(os.path.join(music_dir, songs[song]))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

root = tk.Tk()
root.geometry("500x500")
root.title("Samantha")
root.iconbitmap("icon.ico")
bg = ImageTk.PhotoImage(Image.open("Background.jpg"))
bgLabel = tk.Label(image = bg)
bgLabel.place(x=0,y=0)

button = tk.Button(root, text = "Mic", bg = "Light green",command = primary)
button.place(x=225,y=400,height=50,width=50,command = wishme())
root.mainloop()























