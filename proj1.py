from subprocess import call  # Here this is use for taking screenshort
import subprocess
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import random
from time import ctime
import time
import os
import threading
import requests
from bs4 import BeautifulSoup
global query

engine = pyttsx3.init()


class Person:
    name = "Subhash Prasad"

    def setName(self, name1):
        self.name1 = name1


class assis:
    # name = "Genius"
    def setName(self, name):
        self.name = name


def speak(audio):
    global query
    audio = str(audio)
    engine.say(audio)
    engine.runAndWait()


def exists(terms):
    global query  # UnboundLocalError
    for term in terms:
        if term in query:
            return True


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


def takeCommand():
    global query  # UnboundLocalError
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        # Listening only for 4 sec
        audio = r.listen(source, phrase_time_limit=4)
        # audio = r.listen(source)

    try:
        print("Recognizing...")
        print("\n")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except sr.UnknownValueError:  # error: recognizer does not understand
        speak('I did not get that')
        takeCommand().lower()

    except sr.RequestError:
        # error: recognizer is not connected
        speak('Sorry, the service is down')
        print("Say that again please...")
    except UnboundLocalError:
        takeCommand().lower()
    return query


name = Person()
name.name1 = "Subhash"
asis = assis()
asis.name = "Genius"

if __name__ == "__main__":
    def clear(): return os.system('cls')
    clear()
    wishMe()
    while True:

        query = takeCommand().lower()
        if exists(['goodbye', 'exit', 'quit']):
            speak("bye")
            exit()

        if exists(["weather"]):
            from bs4 import BeautifulSoup
            import requests
            import webbrowser

            headers = {  # Show the user agent
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
            }

            url = "https://weather.com/en-IN/weather/today/l/28.62,77.22?par=apple_widget"
            webbrowser.get().open(url)
            # speak("Here is what I found for" + search_term + "on google")
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                # class of the text written over thereCurrentConditions--tempValue--3a50n
                result1 = soup.find(
                    class_="CurrentConditions--tempValue--MHmYY").get_text()
                result2 = soup.find(
                    class_="CurrentConditions--phraseValue--mZC_p").get_text()
                speak(
                    f"Current temperature is {result1} and weather is {result2}")
                # speak(result1)
                print(
                    f"Current temperature is {result1} and weather is {result2}")
                a = int(result1[:-1])
                if a > 35:
                    print(
                        "Please bring umbrella sir, because the temperature is too high")
                    speak(
                        "Please bring umbrella sir, because the temperature is too high")
                if a < 15:
                    speak(
                        "Please bring enough cloths sir, because the temperature is low")
                    print(
                        "Please bring enough cloths sir, because the temperature is low")
                if a < 5:
                    speak(
                        "Sir, Please make sure you bring enough cloths, because the temperature is too low")
                    print(
                        "Sir, Please make sure you bring enough cloths, because the temperature is too low")
            except:
                pass
            continue

        if exists(['capture', 'screenshot']):
            from datetime import datetime
            a = datetime.today().strftime("%Y-%m-%d" + " at " + "%I:%M:%S.%f %p")
            call(["screencapture", f"screenshot {a}.jpg"])
            continue

        if exists(['hey genius', 'hi genius', 'hello genius']):
            greetings = ["hey, how can I help you", "hey, what's up?",
                         "I'm listening", "how can I help you?", "hello"]
            greet = greetings[random.randint(0, len(greetings)-1)]
            speak(greet)
            continue

        if exists(['open vs code', 'open visual studio code']):
            os.system("open /Applications/Visual\ Studio\ Code.app")
            continue

        if exists(['who are you']):
            speak(f"I am {asis.name} you assistant, Sir")
            continue

        if exists(["what's your name", 'what is your name']):
            speak(f"My name is {asis.name}, Sir")
            continue

        if exists(["play movie"]):
            try:
                if ('movie_path.txt'):
                    with open('movie_path.txt', 'r') as f:
                        b = f.read()
                    import os
                    import fnmatch
                    speak("Which movie you want to play, Sir")
                    a = takeCommand()
                    # b = "/Users/subhashprasad/Movies/"  # without this program not going to run
                    for f in os.listdir(b):
                        if os.path.isfile(b + f):
                            if fnmatch.fnmatch(f, f"{a}*"):
                                os.system(f'open {b}/{f}')
                                break

                            elif fnmatch.fnmatch(f, f"{a.capitalize()}*"):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'{a.upper()}*'):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'*{a}*'):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'*{a.capitalize()}*'):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'*{a.upper()}*'):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'*{a}'):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'*{a.capitalize()}'):
                                os.system(f'open {b}/{f}')
                                break
                            elif fnmatch.fnmatch(f, f'*{a.upper()}'):
                                os.system(f'open {b}/{f}')
            except Exception as e:
                if e:
                    try:
                        import tkinter
                        from tkinter import filedialog
                        import os
                        root = tkinter.Tk()
                        root.withdraw()  # use to hide tkinter window

                        def search_for_file_path():
                            currdir = os.getcwd()
                            tempdir = filedialog.askdirectory(
                                initialdir=currdir, title='Please select a directory')
                            if len(tempdir) > 0:
                                print("You chose: %s" % tempdir)
                            return tempdir
                        file_path_variable = search_for_file_path()
                        with open('movie_path.txt', 'w') as f:
                            b = f.write(file_path_variable)
                        with open('movie_path.txt', 'a') as f:
                            f.write("/")
                        with open('movie_path.txt', 'r') as f:
                            b = f.read()
                        # print ("\nfile_path_variable = ", file_path_variable)
                        import os
                        import fnmatch
                        speak("Which movie you want to play, Sir")
                        a = takeCommand()
                        for f in os.listdir(b):
                            if os.path.isfile(b + f):
                                if fnmatch.fnmatch(f, f"{a}*"):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f"{a.capitalize()}*"):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'{a.upper()}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.capitalize()}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.upper()}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a}'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.capitalize()}'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.upper()}'):
                                    os.system(f'open {b}/{f}')

                    except Exception as e:
                        speak(
                            "Here the music is not available, Sir please select another path sir")
                        import tkinter
                        from tkinter import filedialog
                        import os
                        root = tkinter.Tk()
                        root.withdraw()  # use to hide tkinter window

                        def search_for_file_path():
                            currdir = os.getcwd()
                            tempdir = filedialog.askdirectory(
                                initialdir=currdir, title='Please select a directory')
                            if len(tempdir) > 0:
                                print("You chose: %s" % tempdir)
                            return tempdir
                        file_path_variable = search_for_file_path()
                        with open('movie_path.txt', 'w') as f:
                            b = f.write(file_path_variable)
                        with open('movie_path.txt', 'a') as f:
                            f.write("/")
                        with open('movie_path.txt', 'r') as f:
                            b = f.read()
                        # print ("\nfile_path_variable = ", file_path_variable)
                        import os
                        import fnmatch
                        speak("Which movie you want to play, Sir")
                        a = takeCommand()
                        for f in os.listdir(b):
                            if os.path.isfile(b + f):
                                if fnmatch.fnmatch(f, f"{a}*"):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f"{a.capitalize()}*"):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'{a.upper()}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.capitalize()}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.upper()}*'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a}'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.capitalize()}'):
                                    os.system(f'open {b}/{f}')
                                    break

                                elif fnmatch.fnmatch(f, f'*{a.upper()}'):
                                    os.system(f'open {b}/{f}')

            continue

        if exists(["play some music", "play music"]):
            try:
                if ('music_path.txt'):
                    with open('music_path.txt', 'r') as f:
                        b = f.read()
                    from playsound import playsound
                    import os
                    import random
                    a = random.choice(os.listdir(f"{b}"))
                    os.system(f"open {b}/{a}")

            except Exception as e:
                if e:
                    try:
                        import tkinter
                        from tkinter import filedialog
                        import os
                        root = tkinter.Tk()
                        root.withdraw()  # use to hide tkinter window

                        def search_for_file_path():
                            currdir = os.getcwd()
                            tempdir = filedialog.askdirectory(
                                initialdir=currdir, title='Please select a directory')
                            if len(tempdir) > 0:
                                print("You chose: %s" % tempdir)
                            return tempdir
                        file_path_variable = search_for_file_path()
                        with open('music_path.txt', 'w') as f:
                            b = f.write(file_path_variable)
                        with open('music_path.txt', 'r') as f:
                            b = f.read()
                        # print ("\nfile_path_variable = ", file_path_variable)
                        from playsound import playsound
                        import os
                        import random
                        a = random.choice(os.listdir(f"{b}"))
                        os.system(f"open {b}/{a}")
                        # playsound(f"/Users/subhashprasad/Music/{a}")

                    except Exception as e:
                        speak(
                            "Here the music is not available, Sir please select movie_path path sir")
                        import tkinter
                        from tkinter import filedialog
                        import os
                        root = tkinter.Tk()
                        root.withdraw()  # use to hide tkinter window

                        def search_for_file_path():
                            currdir = os.getcwd()
                            tempdir = filedialog.askdirectory(
                                initialdir=currdir, title='Please select a directory')
                            if len(tempdir) > 0:
                                print("You chose: %s" % tempdir)
                            return tempdir
                        file_path_variable = search_for_file_path()
                        with open('music_path.txt', 'w') as f:
                            b = f.write(file_path_variable)
                        with open('music_path.txt', 'r') as f:
                            b = f.read()
                        # print ("\nfile_path_variable = ", file_path_variable)
                        from playsound import playsound
                        import os
                        import random
                        try:
                            a = random.choice(os.listdir(f"{b}"))
                            os.system(f"open {b}/{a}")
                        except Exception as e:  # with this program will not exit
                            pass
                        # playsound(f"/Users/subhashprasad/Music/{a}")
            continue

        if exists(['where am i', 'my current location', 'show my current loction']):
            import geocoder
            import socket
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)   # problemmmm8**********
            # print("Your Computer Name is:"+hostname)
            # print("Your Computer IP Address is:"+IPAddr)
            ip = geocoder.ip(IPAddr)
            ip = geocoder.ip("me")
            print(ip.city)
            from geopy.geocoders import Nominatim
            geolocator = Nominatim(user_agent="MyApp")
            location = geolocator.geocode(ip.city)
            print("The latitude of the location is: ", location.latitude)
            print("The longitude of the location is: ", location.longitude)
            import webbrowser
            url = f"https://www.google.com/maps/search/{location}/location/"
            webbrowser.get().open(url)
            speak("You must be somewhere near here, as per Google maps")
            continue

        if exists(["play song from youtube", 'song from youtube']):
            import pywhatkit
            song = 'song'
            pywhatkit.playonyt(song)
            continue

        if 'who i am' in query:
            # speak(f"You are {name.name} that's you told me")
            greetings = [f"You are {name.name}, Sir", f"You are {name.name}, but you asked me to call you {name.name1}",
                         f"You're {name.name} But since we're friends,I get to call you {name.name1}"]
            greet = greetings[random.randint(0, len(greetings)-1)]
            speak(greet)
            continue

        if 'restart the pc' in query:
            subprocess.call(
                ['osascript', '-e', 'tell application "System Events" to restart'])

        if 'shutdown the pc' in query:
            subprocess.call(
                ['osascript', '-e', 'tell application "System Events" to shutdown'])

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url = "https://www.youtube.com"
            webbrowser.get().open(url)

        elif 'click pic' in query:
            # import pygame
            # import pygame.camera // we are not going to use this because after click pic camra is going open for infinite time
            from datetime import datetime
            a = datetime.today().strftime("%Y-%m-%d" + " at " + "%I:%M:%S.%f %p")

            import cv2

            camera = cv2.VideoCapture(0)
            camera = cv2.VideoCapture(0)

            camera.isOpened()
            i = 1
            return_value, image = camera.read()
            cv2.imwrite(f"Image {a}.jpg", image)
            del (camera)

        elif 'open google' in query:
            url = "https://www.google.co.in"
            webbrowser.get().open(url)

        elif 'the time' in query:
            import datetime
            strTime = datetime.datetime.now().strftime("%I:%M.%p")
            speak(f"Sir, the time is {strTime}")

        elif 'open whatsapp' in query:
            os.system("open /Applications/WhatsApp.app")

        elif 'open safari' in query:
            os.system("open /Applications/Safari.app")

        elif 'open music' in query:
            os.system("open /System/Applications/Music.app")

        elif 'open chrome' in query:
            os.system("open /Applications/Google\ Chrome.app")

        elif 'open scheduler' in query:
            import Time_Scheduler

        elif 'open timer' in query:
            os.system('open dist/Time_Stoper')

        elif 'open timer' in query:
            os.system('open dist/battery')

        elif 'open book reader' in query:
            import pdf_reader

        elif 'open system preferences' in query:
            os.system("open -a System\ Preferences")

        elif 'open app store' in query:
            os.system("open -a App\ Store")

        else:
            headers = {  # Show the user agent
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
            }
            search_term = query.split("for")[-1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            # speak("Here is what I found for" + search_term + "on google")
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                # class of the text written over there
                result1 = soup.find(class_="Z0LcW").get_text()
                speak(result1)
                print(result1)
            except:
                pass
            try:
                result2 = soup.find(class_="Z0LcW CfV8xf").get_text()
                speak(result2)
                print(result2)
            except:
                pass
time.sleep(1)
