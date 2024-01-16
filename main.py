import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🌃 Gdynia 🌃", callback_data='join_group'),
         InlineKeyboardButton("🌇 Gdańsk 🌇", callback_data='join_group')],
        [InlineKeyboardButton("🌆 Białystok 🌆", callback_data='join_group'),
         InlineKeyboardButton("🌁 Kraków 🌁", callback_data='join_group')],
        [InlineKeyboardButton("📧 E-mail 📧", callback_data='join_group')],
    [InlineKeyboardButton("📞 Zadzwoń 📞", callback_data='call_us')],
    [InlineKeyboardButton("🤖 Dołącz do grupy 🤖", callback_data='join_group')]
]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Wybierz odpowiednią pozycję do kontaktu z nami:', reply_markup=reply_markup)
    # chat_link = 'https://t.me/joinchat/+6qm4HJDD2ZkxNDU0'  # replace with the link to your group
    # chat_id = chat_link.split('/')[-1]  # extract the chat_id from the link


def show_message(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'call_us':
        query.message.reply_text('Skontaktuj się z nami +48123456789')
        
    if query.data == 'join_group':
        query.message.reply_text('https://t.me/joinchat/+6qm4HJDD2ZkxNDU0')


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