from src.controllers.sqliteDB import SqliteDB

from src.models.Users import Users
from src.models.User import User

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

class TeleBot:
    application = None
    users = None
    
    def __init__(self, telegram_token_: str):
        self.application = ApplicationBuilder().token(token=telegram_token_).build()
        self.application.add_handler(CommandHandler(command='start', callback=self._start))
        self.application.add_handler(CommandHandler(command='about', callback=self._about))
        self.application.add_handler(MessageHandler(filters=filters.TEXT & ~filters.COMMAND, callback=self._handle_message))
        
        self.users = Users()
    
    def set_datasource(self, datasource_: SqliteDB):
        self.datasource = datasource_
        self.users.set_datasource(datasource=datasource_)
 
    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command message handler"""
        keyboard = [
            ['Option 1', 'Option 2']
        ]
        
        await self._extract_user(update=update)

        await self._reply_text_keyboard_markup(update=update, text='Welcome! How can I help you today?', keyboard=keyboard )
        
    async def _about(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """About me command message handler"""
        about_text = (
            "🤖 <b>About This Bot</b>\n"
            "This bot was developed using <b>Python</b> and the <i>python-telegram-bot</i> library.\n\n"
            "👨‍💻 <b>Developer:</b> Sem Rithiro\n"
            "📧 <b>Email:</b> rithiro@gmail.com\n"
            "🌐 <b>Portfolio:</b> <a href='https://semrithiro.github.io/curriculumn_vitae'>semrithiro.github.io</a>"
        )
        await self._reply_text(update=update, text=about_text )
        
    async def _reply_text (self, update: Update, text: str):
        """Reply text with HTML parse mode"""
        reply_markup = ReplyKeyboardRemove()
        return await update.message.reply_text(text=text, parse_mode='HTML', reply_markup=reply_markup)
    
    async def _reply_text_keyboard_markup(self, update: Update, text: str, keyboard: list):
        """Reply text with Keyboard markup"""
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
        return await update.message.reply_text(text=text, parse_mode='HTML', reply_markup=reply_markup)
    
    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Message options handler"""
        option = update.message.text
        await self._reply_text(update=update, text=f'You sent {option}',)
        
    async def _extract_user(self, update: Update):
        """Extract telegram user's information"""
        user = update.message.from_user
        if self.users.is_user_exist(user.id) == None:
            self.users.add(User(user.id, user.first_name, user.last_name, user.username, user.language_code, user.is_bot))
            
    
    def run(self):
        """Initialize the Telegram Bot instance"""
        self.application.run_polling()