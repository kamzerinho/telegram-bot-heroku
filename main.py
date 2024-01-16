import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🌃 Gdynia 🌃", url='https://t.me/+6qm4HJDD2ZkxNDU0'),
         InlineKeyboardButton("🌇 Gdańsk 🌇", url='https://t.me/+6qm4HJDD2ZkxNDU0')],
        [InlineKeyboardButton("🌆 Białystok 🌆", url='https://t.me/+6qm4HJDD2ZkxNDU0'),
         InlineKeyboardButton("🌁 Kraków 🌁", url='https://t.me/+6qm4HJDD2ZkxNDU0')],
        [InlineKeyboardButton("📞 Zadzwoń 📞", callback_data='call_us')],
        [InlineKeyboardButton("📧 E-mail 📧", url='mailto:info@example.com')],
        [InlineKeyboardButton("🤖 Dołącz do grupy 🤖", url='https://t.me/+6qm4HJDD2ZkxNDU0')]
        
    ]
    
    # reply_markup = InlineKeyboardMarkup(keyboard)
    # update.message.reply_text('Wybierz odpowiednią pozycję do kontaktu z nami:', reply_markup=reply_markup)
    # chat_link = 'https://t.me/+6qm4HJDD2ZkxNDU0'  # replace with the link to your group
    # chat_id = chat_link.split('/')[-1]  # extract the chat_id from the link


def show_message(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'call_us':
        query.message.reply_text('Skontaktuj się z nami +48123456789')


def main():
    # Set up the bot
    bot_token = '6055065508:AAERu4d2RYwwTzOI27DufK5lsotLwyQJZXE'
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Define the start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Define the callback query handler
    callback_query_handler = CallbackQueryHandler(show_message)
    dispatcher.add_handler(callback_query_handler)



    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()