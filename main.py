from src.controllers.telegram_bot import Telegram_Bot

from src.configurations.app import TELEGRAM_BOT_TOKEN

if __name__ == '__main__':
    application = Telegram_Bot(telegram_token=TELEGRAM_BOT_TOKEN)
    application.run()
    