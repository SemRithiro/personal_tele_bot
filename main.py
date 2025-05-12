from src.configurations.teleBot import TeleBot
from src.configurations.app import TELEGRAM_TOKEN

if __name__ == '__main__':
    application = TeleBot(telegram_token_=TELEGRAM_TOKEN)
    application.run()
    