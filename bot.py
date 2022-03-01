import speech_recognition as sr
import pyttsx3

import pywhatkit
from AppKit import *

from helper import configs
from helper import emails

import requests
import geocoder

import pyjokes
import datetime

import smtplib
from email.message import EmailMessage

### BOT CLASS MODULE ###
class Bot:
    def __init__(self):
        ### GET BOT NAME
        self.__bot_name = configs["BOT_NAME"]

        ### INITIALIZE THE BOT
        self.__ear = sr.Recognizer()
        self.__engine = pyttsx3.init()
        voice = self.__engine.getProperty('voice')
        self.__engine.setProperty('voice', voice.replace("Alex", "samantha"))
        self.__utilities = ""
        self.__emails = {}

        ### READ ALL AVAILABLE UTILITIES FROM utilities.txt
        try:
            with open("utilities.txt", "r") as file:
                utilities = file.read().replace("\n", ", ")
                self.__utilities = utilities
        except:
            print("*** ERROR: Could not open utilities.txt")
        
        ### STORE ALL EMAILS AS DICT
        for name, address in emails.items():
            self.__emails[name] = address
    
    # Brief description of bot
    def __str__(self):
        return f"Hello. This is {self.bot_name.upper()}, your virtual assistant."
    
    # Getter method for emails
    @property
    def emails(self):
        return self.__emails
    
    # Getter method for utilities
    @property
    def utilities(self):
        return self.__utilities
    
    # Getter method for bot name
    @property
    def bot_name(self):
        return self.__bot_name

    # Text-to-speech
    def say(self, text):
        self.__engine.say(text)
        self.__engine.runAndWait()
    
    # Get input
    def get_audio_input(self):
        try:
            with sr.Microphone() as stream:
                print('...On listening...')
                src = self.__ear.listen(stream)
                cmd = self.__ear.recognize_google(src)

                return cmd.lower() if cmd != '' and cmd != None else ''

        except:
            raise ValueError()
    
    # Take command from user
    def take_command(self):
        try:
            cmd = self.get_audio_input()

            if f"hey {self.bot_name}" in cmd:
                cmd = cmd.replace(f"hey {self.bot_name}", '').strip()
                return cmd
            return '' 
        except:
            raise ValueError()
    
    # Get a list of available utilities
    def get_utilities(self):
        print("__GET UTILITIES__")
        self.say(f"Available utilities are {self.utilities}")
    
    # Play music based on user's preferences
    def play_music(self):
            print("__STREAMING MUSIC__")
            print("> Please say the name of the song you want to play <")

            song = self.get_audio_input()
            song = song.upper()

            self.say(f"Playing {song} on Youtube")
            print(f"> Current song: {song}")
            pywhatkit.playonyt(song, use_api=True)
    
    # Get data for current weather in specific location
    def get_weather(self, cmd):
        print("__GET WEATHER__")
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
        print("__GET JOKES__")
        self.say(pyjokes.get_joke())
    
    # Get current time
    def get_time(self):
        print("__GET CURRENT TIME__")
        time = datetime.datetime.now().strftime("%I:%M %p")
        self.say(f"Right now, it is {time}")
    
    # Get today's date
    def get_date(self):
        print("__GET CURRENT DATE__")
        date = datetime.datetime.now().strftime("%B %d, %Y")
        self.say(f"Today's date is {date}")
    
    # Send email
    def send_email(self):
        print("__SEND EMAIL__")

        try:
            print("...Getting email information...")
            self.say("Who is the recipient?")
            recipient = self.get_audio_input()
            self.say("What is the email subject?")
            subject = self.get_audio_input()
            self.say("What is the message?")
            message = self.get_audio_input()

            # Initialize an SMTP client
            server = smtplib.SMTP(configs["EMAIL_DOMAIN"], configs["EMAIL_PORT"])
            server.starttls()
            # Make sure to toggle ON 'Less Secure App Access' before login
            server.login(configs["EMAIL_USER"], configs["EMAIL_PWD"])

            # Initialize email object
            email = EmailMessage()
            email["From"] = configs["EMAIL_USER"]
            email["To"] = self.emails[recipient] 
            email["Subject"] = subject
            email.set_content(message)
        
            # Send email
            server.send_message(email)
            print(f"Sending email to {self.emails[recipient]}...")
            self.say("Email sent!")

        except:
            raise ValueError()

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
        elif 'time' in cmd:
            self.get_time()
        elif 'today' in cmd and 'date' in cmd:
            self.get_date()
        elif 'email' in cmd:
            self.send_email()
        else:
            self.say(f'Sorry, please say the command again! It starts with "Hey {self.bot_name}", followed by your prefered utility. For a list of utilities, please say "Hey {self.bot_name} see utilities"')
    
    # Execute the logic
    def run(self):
        while True:
            try:
                cmd = self.take_command()
                print(f"* Command: {cmd if cmd != '' and cmd != None else 'Unknown'}")

                if cmd in ['exit', 'goodbye', 'shutdown', 'shut down']:
                    self.say('I wish to see you again!')
                    print("BOT SHUTTING DOWN...")
                    break
                elif cmd == '':
                    self.say(f'Sorry, please say the command again! It starts with "Hey {self.bot_name}", followed by your prefered utility. For a list of utilities, please say "Hey {self.bot_name} see utilities"')
                    print("-> Missing required command...")
                else:
                    self.process_command(cmd)

                print()
            except ValueError:
                self.say('Sorry, there was an error getting audio input. Shutting down...')
                print("Failed to get audio input. BOT SHUT DOWN!")
                break

            

if __name__ == '__main__':
    bot = Bot()
    # bot.run()
    print(bot.emails)
    print(bot)