import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime
import pyautogui
from selenium import webdriver
import random

import string
import tkinter as tk
from tkinter import filedialog, Text
import subprocess


PATH = "D:\Webdrivers\87\chromedriver.exe"

port = 587  # For starttls
emailAdresses = open("D:\GameAdminEmailDatabase\emails.txt", "r")
smtp_server = "smtp.gmail.com"

insults = [
    "esti prost de dai in gropi",
    "maaaaaaii",
    "ta ta tauuuurr",
    "mi te anuntasei coaie",
    "ardelean besit",
    "eram cu trepadus si baby fane",
    "mi-l sugi ?"
]

def speak(text):
    tts = gTTS(text=text, lang="ro")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    print("I am listening...")
    playsound.playsound("Soft Beep Sound Effect.mp3")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:

            print("processing sound...")
            said = r.recognize_google(audio, language="ro-RO")
            print(said)
            speak("Ai spus: " + said)

            #region Voice Commands
            if "timp" in said or "ceasul" in said:
                t = time.localtime()
                current_time = time.strftime("%H:%M", t)
                speak("Ora e " + current_time)
            if "data" in said:
                d = datetime.datetime.now().date()
                speak("Azi e :" + str(d))
            if "gluma" in said:
                speak("Cra cra crou loveste din nou")
            if "deschide" in said:
                if "Tim" in said:
                    speak("Deschid Tim")
                    os.startfile(r"C:\Users\Victor\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk")
                if "discord" in said:
                    speak("Deschid discord")
                    os.startfile(r"C:\Users\Victor\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Hammer & Chisel, Inc\Discord.lnk")
                if "vis" in said:
                    speak("Deschid Visual studio code")
                    os.startfile(r"C:\Users\Victor\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
                if "Google" in said:
                    speak("Deschid google chrome")
                    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            if "caută" in said or "cauta" in said:
                searchContent = ""
                if "caută" in said:
                    searchContent = said.__str__().replace("caută","")
                elif "cauta" in said:
                    searchContent = said.__str__().replace("cauta", "")
                driver = webdriver.Chrome(PATH)
                driver.get("https://www.google.com/")
                time.sleep(0.5)
                driver.switch_to.frame(0)
                driver.find_element_by_xpath("/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div").click()
                searchBar = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
                searchBar.send_keys(searchContent)
                time.sleep(1)
                pyautogui.press("enter")
            if "insluta" in said:
                speak(random.choice(insults))




            #endregion

            #region AskToContinue
            answer = input("Do you want to continue y/n :")
            answer.lower()
            if (answer == "y"):
                print("Speak now")
                get_audio()
            elif (answer == "n"):
                print("Thanks for using this voice assistant")
                return
            #endregion
        except Exception as e:
            print("Exception: " + str(e))
            # region AskToContinue
            answer = input("Do you want to continue y/n :")
            answer.lower()
            if (answer == "y"):
                print("Speak now")
                get_audio()
            elif (answer == "n"):
                print("Thanks for using this voice assistant")
                return
            # endregion

        return said

get_audio()

