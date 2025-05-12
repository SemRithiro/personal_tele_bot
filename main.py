from src.controllers.teleBot import TeleBot
from src.controllers.sqliteDB import SqliteDB

from src.configurations.app import TELEGRAM_TOKEN

if __name__ == '__main__':
    sqliteDb = SqliteDB()
    
    application = TeleBot(telegram_token_=TELEGRAM_TOKEN)
    application.set_datasource(datasource_= sqliteDb)
    
    application.run()
    