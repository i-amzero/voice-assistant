import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import wolframalpha
import subprocess
import os
import requests
import ctypes
import urllib.parse

listener = sr.Recognizer()
engine = pyttsx3.init()

brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
web = webbrowser.get('brave')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        talk("Hello, Good Morning, sir")
        print("Hello, Good Morning")
    elif 12 <= hour < 18:
        talk("Hello, Good Afternoon, sir")
        print("Hello, Good Afternoon")
    else:
        talk("Hello, Good Evening, sir")
        print("Hello, Good Evening")


def search_web(query):
    base_url = "https://www.google.com/search?q="
    search_url = base_url + urllib.parse.quote_plus(query)
    webbrowser.open_new_tab(search_url)


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
    return ""


wishMe()


def run_banner():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        statement = command.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=5)
        talk("According to Wikipedia")
        print(results)
        talk(results)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'go for date' in command:
        talk('sorry, I have a girlfriend, I am in a relationship with Google Assistant')
    elif 'are you single' in command:
        talk('I am in a relationship')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'lock window' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'open google' in command:
        web.open_new_tab("https://www.google.com")
        talk("Google Chrome is open now")
    elif "open stack overflow" in command:
        web.open_new_tab("https://stackoverflow.com/login")
        talk("Here is Stack Overflow")
    elif "audio" in command:
        talk("Troubleshooting the audio of your system")
        os.startfile("C:\\Users\\DELL\\Desktop\\project\\Jarvis project\\Audio_Troubleshooting.bat")
    elif "network" in command:
        talk("Troubleshooting the network of your system")
        os.startfile("C:\\Users\\DELL\\Desktop\\project\\Jarvis project\\Network_Troubleshooting.bat")
    elif "bluetooth" in command:
        talk("Troubleshooting the bluetooth of your system")
        os.startfile("C:\\Users\\DELL\\Desktop\\project\\Jarvis project\\Bluetooth_troubleshooting.bat")
    elif "keyboard" in command:
        talk("Troubleshooting the keyboard of your system")
        os.startfile("C:\\Users\\DELL\\Desktop\\project\\Jarvis project\\Keyboard_Troubleshooting.bat")
    elif "music" in command:
        talk("Opening the Music folder")
        os.startfile("C:\\Users\\DELL\\Desktop\\project\\Jarvis project\\Open_Music .bat")
    elif 'write' in command:
        talk('wait! opening Microsoft Word')
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk')
    elif "hello" in command:
        talk('hello, how are you')
    elif 'fine' in command or "good" in command:
        talk("It's good to know that you're fine")
    elif 'news' in command:
        web.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from the Times of India, Happy reading')
    elif 'search' in command:
        query = command.replace("search", "").strip()
        search_web(query)
    elif "weather" in command:
        api_key = "ebbcc5f9fbf949ad263048adda328143"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        talk("What's the city name?")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk("Temperature in Kelvin unit is " +
                 str(current_temperature) +
                 "\n humidity in percentage is " +
                 str(current_humidity) +
                 "\n description  " +
                 str(weather_description))
            print(" Temperature in Kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidity) +
                  "\n description = " +
                  str(weather_description))
        else:
            talk("City Not Found")
    elif 'question' in command:
        talk('What question do you want to ask now?')
        question = take_command()
        app_id = "W2H76L-RK3KJ3UJE7"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)
    elif 'open gmail' in command:
        webbrowser.open_new_tab("https://mail.google.com")
        talk("Google Mail is open now")
    elif "log off" in command or "sign out" in command:
        talk("Ok, your PC will log off in 10 seconds, make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])
    elif "quite" or "sleep" in command:
        return 10
    else:
        talk("Sorry, I didn't hear you, please say again.")


while True:
    num = run_banner()

