from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

class TeleBot:
    application = None
    
    def __init__(self, telegram_token_: str):
        self.application = ApplicationBuilder().token(token=telegram_token_).build()
        self.application.add_handler(CommandHandler(command='start', callback=self._start))
        self.application.add_handler(CommandHandler(command='about', callback=self._about))
        self.application.add_handler(MessageHandler(filters=filters.TEXT & ~filters.COMMAND, callback=self._handle_message))
 
    async def _start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            ['Option 1', 'Option 2']
        ]
        
        await self._reply_text_keyboard_markup(update_=update, text_='Welcome! How can I help you today?', keyboard_=keyboard )
        
    async def _about(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        about_text = (
            "🤖 <b>About This Bot</b>\n"
            "This bot was developed using <b>Python</b> and the <i>python-telegram-bot</i> library.\n\n"
            "👨‍💻 <b>Developer:</b> Sem Rithiro\n"
            "📧 <b>Email:</b> rithiro@gmail.com\n"
            "🌐 <b>Portfolio:</b> <a href='https://semrithiro.github.io/curriculumn_vitae'>semrithiro.github.io</a>"
        )
        await self._reply_text(update_=update, text_=about_text )
        
    async def _reply_text (self, update_: Update, text_: str):
        reply_markup = ReplyKeyboardRemove()
        return await update_.message.reply_text(text=text_, parse_mode='HTML', reply_markup=reply_markup)
    
    async def _reply_text_keyboard_markup(self, update_: Update, text_: str, keyboard_: list):
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard_, resize_keyboard=True)
        return await update_.message.reply_text(text=text_, parse_mode='HTML', reply_markup=reply_markup)
    
    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        option = update.message.text
        await self._reply_text(update_=update, text_=f'You sent {option}',)
        
    def run(self):
        self.application.run_polling()