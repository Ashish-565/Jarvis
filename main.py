from speech_recognition import Microphone, Recognizer
from pywinauto.application import Application
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import webbrowser
import pyautogui
import os
import sys


listener = Recognizer()
engine = pyttsx3.init()
sleep = 0
'''voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)'''  # for different voices


def talk(text):
    """this method takes text and repeats from speaker"""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """this method takes microphone input from user and returns string output"""
    try:
        with Microphone() as source:
            print('listening....')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except:
        talk('please say it again')
        return take_command()
    return command


def run_jarvis():
    global sleep
    command = take_command()
    if 'how are you' in command:
        talk('Iam fine, glad you to ask me that')
    elif 'who are you' in command:
        talk('Iam jarvis. Created by Aashish, to support like a friend')
    elif 'who made you' in command:
        talk('I have been created by Aashish, and he is my boss')
    elif 'hey jarvis' in command:
        jarvis_condition()
    elif 'jarvis' in command:
        talk("Yes sir, Iam in your service")
    elif 'time' in command:
        clock = datetime.datetime.now().strftime('%H:%M %p')
        talk('current time is ' + clock)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open youtube' in command:
        talk('opening youtube')
        webbrowser.open('https://www.youtube.com/')
        time.sleep(10)
        youtube()
    elif 'increase your volume' in command:
        talk('increasing volume')
        pyautogui.hotkey('volumeup')
    elif 'open whatsapp' in command:
        talk('opening whatsapp')
        webbrowser.open('https://web.whatsapp.com/')
        time.sleep(10)
    elif 'open chrome' in command or 'open google' in command:
        talk('opening chrome browser')
        webbrowser.open('https://www.google.com/')
        time.sleep(30)
        talk('please say what you want search in chrome')
        chrome_search = take_command()
        if 'new tab' in chrome_search:
            pyautogui.press('ctrl', 't')
        elif 'side window' in chrome_search:
            pyautogui.press('ctrl', 'shift', 'tab')
        elif 'new chrome window' in chrome_search:
            pyautogui.press('ctrl', 'n')
        else:
            pyautogui.write(chrome_search)
            time.sleep(3)
            pyautogui.press('enter')
    elif 'open notepad' in command:
        talk('opening notepad')
        os.system('C:\WINDOWS\system32\\notepad')
        notepad()
    elif 'wikipedia' in command:
        wik = command.replace('wikipedia', '')
        info = wikipedia.summary(wik, sentences=1)
        talk(info)
    elif 'left side' in command:
        pyautogui.hotkey('win', 'left')
    elif 'right side' in command:
        pyautogui.hotkey('win', 'right')
    elif 'click' in command:
        pyautogui.click()
    elif 'minimise' in command:
        talk('minimising window')
        pyautogui.hotkey('win', 'd')
    elif 'close' in command:
        talk('closing window')
        pyautogui.hotkey('alt', 'f4')
    elif 'wait' in command or 'stop' in command:
        stop()
        sleep = 0
    elif 'exit' in command:
        talk('Thanks for giving me your time')
        sys.exit()
    else:
        talk('I could not understand what you are saying, please say the command again.')


def youtube():
    talk('what you want to play')
    youtube_play = take_command()
    song = youtube_play.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(song)
    time.sleep(5)
    talk('shall I wait')
    command = take_command()
    if 'yes' in command or 'wait' in command:
        stop()
    elif 'pause' in command or 'play' in command:
        pyautogui.press('space')
    elif 'volume up' in command:
        talk('increasing volume')
        pyautogui.press('volumeup')
    elif 'volume down' in command:
        talk('decreasing volume')
        pyautogui.press('volumedown')
    elif 'mute' in command():
        talk('muting volume')
        pyautogui.press('volumemute')
    elif 'unmute' in command:
        pyautogui.press('volumemute')
    elif 'full screen' in command:
        pyautogui.press('f')
    else:
        command = take_command()

def notepad():
    talk('please say what you want to write')
    command = take_command()
    pyautogui.write(command)
    if 'up' in command:
        pyautogui.press('up')
    elif 'down' in command:
        pyautogui.press('down')
    elif 'left' in command:
        pyautogui.press('left')
    elif 'right' in command:
        pyautogui.press('right')
    elif 'enter' in command:
        pyautogui.press('enter')
    else:
        talk('would you like to write more')
        s = take_command()
        if 'yes' in s:
            notepad()


def stop():
    global sleep
    talk('for how many minutes you want to stop jarvis from listening')
    try:
        stopping = int(take_command())
        talk('jarvis going to stop for')
        talk(stopping)
        talk('minutes')
        sleep = 1
        time.sleep(stopping * 60)
    except:
        stop()
    talk('Iam awake sir')


def jarvis_condition():
    global sleep
    if sleep == 1:
        talk('jarvis is on sleep, do you want to wake it up')
        wake = take_command()
        if 'yes' in wake:
            talk('Hello Aashish, Iam jarvis at your service')
            sleep = 0
    else:
        talk('Hello Aashish, Iam jarvis at your service')


def wish_me():
    talk("Hello Aashish")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        talk("Good Morning")
    elif 12 <= hour < 16:
        talk("Good Afternoon")
    else:
        talk("Good Evening")
    talk("Iam Jarvis welcoming you")
    talk("How can i help you")


wish_me()
while True:
    run_jarvis()

'''elif 'open calculator' in command:
        talk('opening calculator')
        Application.start('calculator.exe')
    elif 'open camera' in command:
        talk('opening camera')
        Application.start('camera.exe')
    elif 'write' in command:
        talk('opening notepad to write')
        app = Application.start('notepad.exe')
        notepad()
        talk('would you like to save it')
        save = take_command()
        if 'yes' in save:
            app.UntitledNotepad.menu_select('File->save->save')
            talk('please give a name to file')
            time.sleep(5)
            pyautogui.press('ctrl', 's')
            talk('file has been saved')
        talk('would you like to close notepad')
        close = take_command()
        if 'yes' in close:
            talk('notepad is closing')
            app.UntitledNotepad.menu_select("File->Exit")
            pyautogui.press('alt', 'f4')'''