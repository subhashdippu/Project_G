import psutil
import pyttsx3
import os
engine = pyttsx3.init()


def speak(audio):
    global query
    audio = str(audio)
    engine.say(audio)
    engine.runAndWait()


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


battery = psutil. sensors_battery()
plugged = battery.power_plugged
percent = str(battery. percent)
percent1 = battery. percent
plugged = "Plugged In" if plugged else "UnPlugged In"
print(percent+'% | '+plugged)
while True:
    battery = psutil. sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery. percent)
    percent1 = battery. percent
    # plugged = "Plugged In" if plugged else "UnPlugged In"
    # if plugged:
    #     print('In')
    # else:
    #     print("out")
    if percent1 == 85 and plugged:
        speak("Battery is 85 percent charged.")
        notify("Battery is 85 percent charged.", "Heres an alert")

    elif percent1 > 85:
        speak("Battery is charged more then 85 percent Please off the charger switch")
    # print(percent+'% | '+plugged)
