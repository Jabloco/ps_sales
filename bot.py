from telegram.ext import Updater, CommandHandler

from bot_settings import TOKEN
from bot_handler import greet_user

def main():
    ps_bot = Updater(TOKEN)

    dp = ps_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    ps_bot.start_polling()
    ps_bot.idle()

main()