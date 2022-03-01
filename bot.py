import speech_recognition as sr
import pyttsx3
from helper import configs
import pywhatkit
from AppKit import *

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
    
    def process_command(self, cmd):
        pass
            
    
    def run(self):
        while True:
            cmd = self.take_command()
            print(f"* Command: {cmd}")

            if 'exit' in cmd or 'goodbye' in cmd:
                self.say('I wish to see you again!')
                print("BOT SHUTTING DOWN...")
                break
            elif cmd == '':
                print("-> Missing required command...")
                self.say('Sorry, please say the command again! It starts with "Hey Alexa", followed by the chosen function')
            else:
                self.process_command(cmd)

            

if __name__ == '__main__':
    bot = Bot()
    bot.run()