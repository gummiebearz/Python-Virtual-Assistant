import speech_recognition as sr
import pyttsx3
import pywhatkit
from AppKit import * # must include this line explicitly to prevent pywhatkit from throwing error from AppKit
from datetime import datetime
import requests
import geocoder
import pyjokes
from dotenv import dotenv_values

# TAKE ENVIRONMENT VARIABLES FROM .env & STORE INTO DICT
configs = dotenv_values(".env")

ear = sr.Recognizer()
bot = pyttsx3.init()
voice = bot.getProperty('voice')
bot.setProperty('voice', voice.replace("Alex", "samantha"))

def talk(text):
    bot.say(text)
    bot.runAndWait()

def take_command():
    try:
        with sr.Microphone() as stream:
            print('listening...')
            src = ear.listen(stream)
            cmd = ear.recognize_google(src)
            cmd = cmd.lower()

            if 'hey alexa' in cmd:
                cmd = cmd.replace('hey alexa', '').strip()
                return cmd
            return '' 
    except:
        return ''

def process_cmd(cmd):
    print(f"Command: {cmd}")
    if 'play' in cmd:
        music = cmd.replace('play ', '')
        talk(f"Playing {music} on Youtube")
        print(f"Playing music...")
        pywhatkit.playonyt(music, use_api=True)

    elif 'time' in cmd:
        current_time = datetime.now().strftime("%I:%M %p")
        talk(f"Currently, it's {current_time}")

    elif 'weather' in cmd and 'in' not in cmd:
        loc = geocoder.ip('me')
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={loc.latlng[0]}&lon={loc.latlng[1]}&appid={configs['WEATHER_API_KEY']}&units=metric"
        response = requests.get(url)
        response = response.json()
        talk(f'Currently, in {response["name"]}, it is {response["main"]["temp"]} degrees Celcius, with {response["weather"][0]["description"]}.')

    elif 'weather' in cmd and 'in' in cmd:
        loc = cmd.split(' ')[-1]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={configs['WEATHER_API_KEY']}&units=metric"
        response = requests.get(url)
        response = response.json()
        talk(f'Currently, in {response["name"]}, it is {response["main"]["temp"]} degrees Celcius, with {response["weather"][0]["description"]}.')

    elif 'joke' or 'jokes' in cmd:
        talk(pyjokes.get_joke())

    
while True:
    cmd = take_command()

    if 'exit' in cmd or 'goodbye' in cmd:
        talk('I wish to see you again!')
        break
    elif cmd == '':
        talk('Sorry, please say the command again!')
    else:
        process_cmd(cmd)
