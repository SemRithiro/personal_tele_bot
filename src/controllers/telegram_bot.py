from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters

from src.utils.helper import get_option, generate_html_message, chunk_keyboard_markup_button

from src.configurations.app import OPTIONS, ABOUT_ME_TEXT, CHOOSE_OPTION

class Telegram_Bot:
    application = None

    def __init__(self, telegram_token: str):
        """Initialize the Telegram Bot instance"""
        self.application = ApplicationBuilder().token(token=telegram_token).build()
        
        # self.application.add_handler(MessageHandler(filters=filters.PHOTO, callback=self._handle_photo))
        # self.application.add_handler(MessageHandler(filters=filters.VIDEO, callback=self._handle_video))
        # self.application.add_handler(MessageHandler(filters=filters.Document.ALL, callback=self._handle_file))
        # self.application.add_handler(MessageHandler(filters=filters.LOCATION, callback=self._handle_location))
        # self.application.add_handler(MessageHandler(filters=filters.CONTACT, callback=self._handle_contact))
        
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler(command='ability', callback=self._handle_converation)],
            states={
                CHOOSE_OPTION: [MessageHandler(filters=filters.TEXT & ~filters.COMMAND, callback=self._handle_converation)]
            },
            fallbacks=[MessageHandler(filters=filters.ALL, callback=self._handle_invalid_option)]
        )
        
        self.application.add_handler(conv_handler);
        self.application.add_handler(CommandHandler(command='start', callback=self._handle_welcome_message))
        self.application.add_handler(CommandHandler(command='about', callback=self._handle_about_me))
        self.application.add_handler(CommandHandler(command='cancel', callback=self._handle_cancel_operation))

    async def _handle_extract_user_choice(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        breadcrumbs = context.user_data.get('BREADCRUMBS')
        if breadcrumbs == None:
            breadcrumbs = ['Main']
        else:
            pass
        return breadcrumbs

    async def _handle_converation(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user

        if update.message:
            if update.message.text:
                user_choice = update.message.text
                
                if user_choice.startswith('/'):
                    context.user_data['BREADCRUMBS'] = ['Main']
                
                breadcrumbs = await self._handle_extract_user_choice(update=update, context=context)
                options_list, select_option = get_option(options=OPTIONS, breadcrumbs=breadcrumbs)

                if user_choice in options_list:
                    if not user_choice in breadcrumbs:
                        breadcrumbs.append(user_choice)
                    elif breadcrumbs.index(user_choice) <= len(breadcrumbs):
                        breadcrumbs = breadcrumbs[:breadcrumbs.index(user_choice)]
                context.user_data['BREADCRUMBS'] = breadcrumbs
                options_list, select_option = get_option(options=OPTIONS, breadcrumbs=breadcrumbs)
                await self._reply_message(update=update, text=generate_html_message(select_option), options=options_list)
                if len(options_list) > 0:
                    return CHOOSE_OPTION
                else:
                    return ConversationHandler.END

    async def _reply_message(self, update: Update, text: str, options: list = []):
        keyboard = ReplyKeyboardRemove()
        if len(options) > 0:
            keyboard = ReplyKeyboardMarkup(keyboard=chunk_keyboard_markup_button(options), resize_keyboard=True)
        await update.message.reply_html(text=text, reply_markup=keyboard)

    async def _handle_photo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        photo = update.message.photo[-1] # Get highest quality
        if photo != None:
            file = await photo.get_file()
            file_path = f"downloads/{user.id}_{photo.file_id}.jpg"
            await file.download_to_drive(file_path)
        await update.message.reply_html(text='Thanks you!')
    async def _handle_video(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        video = update.message.video
        if video != None:
            file = await video.get_file()
            file_path = f"downloads/{user.id}_{video.file_unique_id}_{video.file_name}"
            await file.download_to_drive(file_path)
        await update.message.reply_html(text='Thanks you!')
    async def _handle_file(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        document = update.message.document
        if document != None:
            file = await document.get_file()
            file_path = f"downloads/{user.id}_{document.file_unique_id}_{document.file_name}"
            await file.download_to_drive(file_path)
        await update.message.reply_html(text='Thanks you!')
    # TODO: Live location not yet working.
    async def _handle_location(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        location = update.message.location
        if location != None:
            latitude = location.latitude
            longitude = location.longitude

            print(f"[LIVE LOCATION] User: {user.id}, Lat: {latitude}, Long: {longitude}. Period: {location.live_period}")
        
        await update.message.reply_html(text='Thanks you!')  
    async def _handle_contact(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        contact = update.message.contact
        if contact != None:
            print(contact.to_json())
        await update.message.reply_html(text='Thanks you!')

    async def _handle_invalid_option(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_html(text='❌ Ivalid option. Please choose again.')
        return CHOOSE_OPTION

    async def _handle_welcome_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await update.message.reply_html(text=f'Welcome {user.last_name}. How can I help you today!')
        return ConversationHandler.END

    async def _handle_about_me(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_html(text=ABOUT_ME_TEXT)
        return ConversationHandler.END
        
    async def _handle_cancel_operation(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_html(text='No active command to cancel. I wasn\'t doing anything anyway. Zzzzz...')
        return ConversationHandler.END
    
    def run(self):
        """Start polling the Telegram Bot"""
        print('Telegram Bot is running')
        self.application.run_polling()