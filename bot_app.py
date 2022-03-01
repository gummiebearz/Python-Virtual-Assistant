### USER INTERFACE FOR BOT APPLICATION ###
from bot import Bot

class BotApp():
    def __init__(self):
        self.__bot = Bot()
    
    def run(self):
        self.__bot.run()

if __name__ == '__main__':
    app = BotApp()
    app.run