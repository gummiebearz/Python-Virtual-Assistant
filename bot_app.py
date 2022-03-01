### USER INTERFACE FOR BOT APPLICATION ###
from bot import Bot

class BotApp():
    def __init__(self):
        self.__bot = Bot()
    
    def run(self):
        self.__bot.run()
    
    def __str__(self):
        return f"Hello. This is the user interface for using {self.__bot.bot_name.upper()}, the best virtual assistant."

if __name__ == '__main__':
    app = BotApp()
    app.run()
    # print(app)