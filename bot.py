import speech_recognition as sr
import pyttsx3

import pywhatkit
from AppKit import *

from helper import configs

import requests
import geocoder
class Bot:
    def __init__(self):
        self.__ear = sr.Recognizer()
        self.__engine = pyttsx3.init()
        voice = self.__engine.getProperty('voice')
        self.__engine.setProperty('voice', voice.replace("Alex", "samantha"))
    
    def say(self, text):
        self.__engine.say(text)
        self.__engine.runAndWait()
    
    def take_command(self):
        try:
            with sr.Microphone() as stream:
                print('...On listening...')
                src = self.__ear.listen(stream)
                cmd = self.__ear.recognize_google(src)
                cmd = cmd.lower()

                if 'hey alexa' in cmd:
                    cmd = cmd.replace('hey alexa', '').strip()
                    return cmd
                return '' 
        except:
            return ''
    
    def play_music(self):
            print('__PLAYING MUSIC__')
            self.say('Okay...What music do you want to play?')

            with sr.Microphone() as stream:
                src = self.__ear.listen(stream)
                song = self.__ear.recognize_google(src)

            self.say(f"Playing {song} on Youtube")
            print(f"Current song: {song}")
            pywhatkit.playonyt(song, use_api=True)
    
    def get_weather(self, cmd):
        print("__GET WEATHER__")
        if 'in' in cmd:
            loc = cmd.split(' ')[-1]
            url = f"https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={configs['WEATHER_API_KEY']}&units=metric"
        else:
            loc = geocoder.ip('me') 
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={loc.latlng[0]}&lon={loc.latlng[1]}&appid={configs['WEATHER_API_KEY']}&units=metric"

        response = requests.get(url)
        response = response.json()

        self.say(f'Currently, in {response["name"]}, it is {response["main"]["temp"]:.1f} degrees Celcius, with {response["weather"][0]["description"]}.')

    def process_command(self, cmd):
        if 'play' in cmd and 'music' in cmd:
            self.play_music()            
        elif 'weather' in cmd:
            self.get_weather(cmd)
    
    def run(self):
        while True:
            cmd = self.take_command()
            print(f"* Command: {cmd}")

            if 'exit' in cmd or 'goodbye' in cmd:
                self.say('I wish to see you again!')
                print("BOT SHUTTING DOWN...")
                break
            elif cmd == '':
                self.say('Sorry, please say the command again! It starts with "Hey Alexa", followed by the chosen function')
                print("-> Missing required command...")
            else:
                self.process_command(cmd)

            

if __name__ == '__main__':
    bot = Bot()
    bot.run()