import time
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
speak("Time alert Calling Started")
while True:
    now = time.strftime("%H:%M:%S")
    if now[3:8] == "00:00":
        if int(now[0:2]) < 12:
            speak("Time" + now[0:3] + 'AM')
            print("Time" + now[0:3] + 'AM')
        else:
            t = int(now[0:2])%12
            speak("Time" + str(t) + 'PM')
            print("Time" + str(t) + 'PM')
        
        time.sleep(1)
        continue
    else:
        pass
    