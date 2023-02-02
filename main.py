import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from win10toast import ToastNotifier
import time


toaster = ToastNotifier()

toaster.show_toast("kash notification",
                   "Initializing kash",
                   duration=5)
   


print("Initializing kash")

MASTER = "Akash"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(text):
    engine.say(text)
    engine.runAndWait()



def wishme():
    hour = datetime.datetime.now().hour
    print(hour)


    if hour>=0 and hour <12:
        speak("Good morning" + MASTER)
        print("Good morning" + MASTER)
        speak("hi sir welcome")

    elif hour>=12 and hour<18:
        speak("Good afternoon" + MASTER)
        print("Good afternoon" + MASTER)
        speak("hi sir hope all is well")

    else:
        speak("Good evening" + MASTER)
        print("Good evening" + MASTER)
        speak("hi sir where is your tomji")

    speak("I am kash how may i help you?")

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

    
    
    
        
def time():
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strtime} ")
    print(f"{MASTER} the time is {strtime} ")
    toaster.show_toast( f"Time is {strtime} ",
                   
                   duration=5)


   

speak("Initializing kash....")
wishme()
#time.sleep(10)
time()
#takecommand()


    

while True: 
    code=input("say anything:")
    if 'play song' in  code:
        songs_dir = "E:\\video songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))
    elif "wikipedia" in code:
        speak("Searching wikipedia")
        code = code.replace("wikipedia","")
        result = wikipedia.summary(code,sentences=2)
        speak("according to wikipedia")
        print(result)
        speak(result) 
    elif "open pictures" in code:
        openpicturespath = "C:\\Users\\Akash\\Pictures"
        openpictures = os.listdir(openpicturespath)
        toaster.show_toast("opening pictuers",
        duration=5
    
        )
        speak("opening..")
        print(openpictures)
        os.startfile(os.path.join(openpicturespath,openpictures[0]))
    elif 'open youtube' in code:
            webbrowser.open("youtube.com")
    elif 'open code' in code:
            codePath = "C:\\Users\\Akash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
    elif 'open google' in code:
            
            webbrowser.open("google.com")
    elif 'open photoshop' in code:
            codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
           
            toaster.show_toast("opening photoshop",
            duration=5   
            )
            os.startfile(codePath)
    elif 'open bavithra' in code:
        codePath = "E:\\"
       
        toaster.show_toast("opening bavithra",
            duration=5   
            )
        os.startfile(codePath)
    elif 'open akash' in code:
        codePath = "D:\\"
        os.startfile(codePath)
        toaster.show_toast("opening akash",
            duration=5   
            )
        os.startfile(codePath)

      
    


     