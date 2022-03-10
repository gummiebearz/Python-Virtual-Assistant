### USER INTERFACE FOR BOT APPLICATION ###
from bot import Bot

class BotApp():
    def __init__(self):
        self.__bot = Bot()
    
    def run(self):
        while True:
            try:
                cmd = self.__bot.take_command()
                print(f"* Command: {cmd if cmd != '' and cmd != None else 'Unknown'}")

                if cmd in ['exit', 'goodbye', 'shutdown', 'shut down']:
                    self.__bot.say('I wish to see you again!')
                    print("BOT SHUTTING DOWN...")
                    break
                elif cmd == '':
                    self.__bot.say(f'Sorry, please say the command again! It starts with "Hey {self.__bot.bot_name.upper()}", followed by your prefered utility. For a list of utilities, please say "Hey {self.__bot.bot_name.upper()}", see utilities"')
                    print("-> Missing required command...")
                else:
                    self.__bot.process_command(cmd)

                print()
            except ValueError:
                self.__bot.say('Sorry, there was an error getting audio input. Shutting down...')
                print("Failed to get audio input. BOT SHUT DOWN!")
                break
    
    def __str__(self):
        return f"Hello. This is the user interface for using {self.__bot.bot_name.upper()}, the best virtual assistant."

if __name__ == '__main__':
    app = BotApp()
    app.run()
    # print(app)