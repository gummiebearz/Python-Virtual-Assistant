import speech_recognition as sr
import pyttsx3

import pywhatkit
from AppKit import *

from helper import configs

import requests
import geocoder

import pyjokes

### BOT CLASS MODULE ###
class Bot:
    def __init__(self):
        ### GET BOT NAME
        self.bot_name = configs["BOT_NAME"]

        ### INITIALIZE THE BOT
        self.__ear = sr.Recognizer()
        self.__engine = pyttsx3.init()
        voice = self.__engine.getProperty('voice')
        self.__engine.setProperty('voice', voice.replace("Alex", "samantha"))
        self.__utilities = ""

        ### READ ALL AVAILABLE UTILITIES FROM utilities.txt
        try:
            with open("utilities.txt", "r") as file:
                utilities = file.read().replace("\n", ", ")
                self.__utilities = utilities
        except:
            print("*** ERROR: Could not open utilities.txt")
    
    # Text-to-speech
    def say(self, text):
        self.__engine.say(text)
        self.__engine.runAndWait()
    
    # Take command from user
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
    
    # Get a list of available utilities
    def get_utilities(self):
        self.say(f"Available utilities are {self.__utilities}")
    
    # Play music based on user's preferences
    def play_music(self):
            print("__STREAMING MUSIC__")
            self.say("MUSIC UTILITY")
            # This print line is needed to know the delay after the bot says before the user can say the command
            print("> Please say the name of the song you want to play <")

            with sr.Microphone() as stream:
                src = self.__ear.listen(stream)
                song = self.__ear.recognize_google(src)
                song = song.upper()

            self.say(f"Playing {song} on Youtube")
            print(f"> Current song: {song}")
            pywhatkit.playonyt(song, use_api=True)
    
    # Get data for current weather in specific location
    def get_weather(self, cmd):
        print("__GET WEATHER__")
        self.say('WEATHER UTILITY')
        # If location is specified, return data for that location
        if 'in' in cmd:
            loc = cmd.split(' ')[-1]
            url = f"https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={configs['WEATHER_API_KEY']}&units=metric"
        # Otherwise, get the location based on location of machine running
        else:
            loc = geocoder.ip('me') 
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={loc.latlng[0]}&lon={loc.latlng[1]}&appid={configs['WEATHER_API_KEY']}&units=metric"

        response = requests.get(url)
        response = response.json()

        self.say(f'Currently, in {response["name"]}, it is {response["main"]["temp"]:.1f} degrees Celcius, with {response["weather"][0]["description"]}.')
    
    # Get jokes
    def get_joke(self):
        self.say(pyjokes.get_joke())

    # Process user's command
    def process_command(self, cmd):
        if 'see utilities' in cmd:
            self.get_utilities()
        elif 'play' in cmd and 'music' in cmd:
            self.play_music()            
        elif 'weather' in cmd:
            self.get_weather(cmd)
        elif 'joke' in cmd or 'jokes' in cmd:
            self.get_joke()
        else:
            self.say('Sorry, please say the command again! It starts with "Hey Alexa", followed by your prefered utility. For a list of utilities, please say "Hey Alexa see utilities"')
    
    # Execute the logic
    def run(self):
        while True:
            cmd = self.take_command()
            print(f"* Command: {cmd if cmd != '' and cmd != None else 'Unknown'}")

            if 'exit' in cmd or 'goodbye' in cmd or 'shut down' in cmd:
                self.say('I wish to see you again!')
                print("BOT SHUTTING DOWN...")
                break
            elif cmd == '':
                self.say('Sorry, please say the command again! It starts with "Hey Alexa", followed by your prefered utility. For a list of utilities, please say "Hey Alexa see utilities"')
                print("-> Missing required command...")
            else:
                self.process_command(cmd)

            print()

            

if __name__ == '__main__':
    bot = Bot()
    bot.run()