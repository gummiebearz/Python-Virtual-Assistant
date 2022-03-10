### USER INTERFACE FOR BOT APPLICATION ###
from bot import Bot

class BotApp():
    def __init__(self):
        self.__bot = Bot()

    # Take user's command
    def take_command(self):
        try:
            cmd = self.__bot.get_audio_input()

            if f"hey {self.__bot.bot_name}" in cmd:
                cmd = cmd.replace(f"hey {self.__bot.bot_name}", '').strip()
                return cmd
            return '' 
        except:
            raise ValueError()

    # Process user's command
    def process_command(self, cmd):
        if 'see utilities' in cmd:
            self.__bot.get_utilities()
        elif 'play' in cmd and 'music' in cmd:
            self.__bot.play_music()            
        elif 'weather' in cmd:
            self.__bot.get_weather(cmd)
        elif 'joke' in cmd or 'jokes' in cmd:
            self.__bot.get_joke()
        elif 'time' in cmd:
            self.__bot.get_time()
        elif 'today' in cmd and 'date' in cmd:
            self.__bot.get_date()
        elif 'send' in cmd and 'email' in cmd:
            self.__bot.send_email()
        elif 'add' in cmd and 'email' in cmd:
            self.__bot.add_email_contact()
        else:
            self.__bot.say(f'Sorry, please say the command again! It starts with "Hey {self.bot_name}", followed by your prefered utility. For a list of utilities, please say "Hey {self.bot_name} see utilities"')
            
    def run(self):
        while True:
            try:
                cmd = self.take_command()
                print(f"* Command: {cmd if cmd != '' and cmd != None else 'Unknown'}")

                if cmd in ['exit', 'goodbye', 'shutdown', 'shut down']:
                    self.__bot.say('I wish to see you again!')
                    print("BOT SHUTTING DOWN...")
                    break

                elif cmd == '':
                    self.__bot.say(f'Sorry, please say the command again! It starts with "Hey {self.__bot.bot_name.upper()}", followed by your prefered utility. For a list of utilities, please say "Hey {self.__bot.bot_name.upper()}", see utilities"')
                    print("-> Missing required command...")

                else:
                    self.process_command(cmd)

                print()

            except ValueError:
                self.__bot.say('Sorry, there was an error getting audio input. Shutting down...')
                print("Failed to get audio input. BOT SHUT DOWN!")
                break
    
    def __str__(self):
        return f"Hello. This is the user interface for using {self.__bot.bot_name.upper()}, the best virtual assistant."

if __name__ == '__main__':
    app = BotApp()
    # app.run()
    print(app)