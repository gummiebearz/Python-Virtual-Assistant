### USER INTERFACE FOR BOT APPLICATION ###
import speech_recognition as sr
from bot import Bot

# extern variable for dev mode
DEBUG = True
class BotApp():
    def __init__(self):
        self.__bot = Bot()

    def __str__(self):
        return f"Hello. This is the user interface for using {self.__bot.bot_name.upper()}, the best virtual assistant."

    # Take user's command
    def take_command(self):
        cmd = self.__bot.get_audio_input()

        if f"hey {self.__bot.bot_name}" in cmd:
            cmd = cmd.replace(f"hey {self.__bot.bot_name}", '').strip()
            return cmd
        return '' 

    # Process user's command
    def process_command(self, cmd):
        # show utilties
        if 'see utilities' in cmd:
            self.__bot.get_utilities()
        # play music
        elif 'play' in cmd and 'music' in cmd:
            self.__bot.play_music()            
        # get weather data
        elif 'weather' in cmd:
            self.__bot.get_weather(cmd)
        # get joke
        elif 'joke' in cmd or 'jokes' in cmd:
            self.__bot.get_joke()
        # get current time
        elif 'what' in cmd and 'time' in cmd:
            self.__bot.get_time()
        # get current date
        elif 'today' in cmd and 'date' in cmd:
            self.__bot.get_date()
        # send email
        elif 'send' in cmd and 'email' in cmd:
            self.__bot.send_email()
        # create new email contact
        elif 'save' in cmd and 'email' in cmd and 'contact' in cmd:
            self.__bot.add_email_contact()
        elif 'tell me what is' in cmd or 'tell me who is' in cmd:
            search_term = cmd.replace('tell me what is', '') if 'tell me what is' in cmd else cmd.replace('tell me who is', '')
            self.__bot.wiki_search(search_term.strip())
        else:
            self.__bot.say(f"Sorry, I couldn't get that. Please try again.")
            
    # Execute the logic
    def run(self):
        while True:
            try:
                cmd = self.take_command()
                print(f"* Command: {cmd if cmd != '' and cmd != None else 'Unknown'}")

                if cmd in ['exit', 'goodbye', 'shutdown', 'shut down']:
                    self.__bot.say('I wish to see you again!')
                    self.__bot.shutdown_tasks()
                    print("BOT SHUTTING DOWN...")

                    break

                elif cmd == '':
                    self.__bot.say(f'Sorry, please say the command again! It starts with "Hey {self.__bot.bot_name}", followed by your prefered utility. For a list of utilities, please say "Hey {self.__bot.bot_name}", see utilities"')
                    print("-> Missing required command...")

                else:
                    self.process_command(cmd)

                print()

            except sr.UnknownValueError as err_msg:
                print(err_msg)
                self.__bot.say("Sorry, there was an error getting the audio input. Shutting down...")

                self.__bot.shutdown_tasks()
                break
    

if __name__ == '__main__':
    app = BotApp()
    app.run()
    # print(app)