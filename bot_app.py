### USER INTERFACE FOR BOT APPLICATION ###
from bot import Bot

class BotApp():
    def __init__(self):
        self.__bot = Bot()
    
    def run(self):
        while True:
            cmd = self.__bot.take_command()
            print(f"* Command: {cmd}")

            if 'exit' in cmd or 'goodbye' in cmd:
                self.__bot.say('I wish to see you again!')
                print("BOT SHUTTING DOWN...")
                break
            elif cmd == '':
                self.__bot.say('Sorry, please say the command again! It starts with "Hey Alexa", followed by the chosen function')
                print("-> Missing required command...")
            else:
                self.__bot.process_command(cmd)
    
    def __str__(self):
        return "This is a simplified bot application created by Gumball!"

if __name__ == '__main__':
    app = BotApp()
    app.run()