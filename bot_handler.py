from api_client import BotApiClient
# from telegram import replymarkup

from bot_keyboard import keyboard

bot_api = BotApiClient()


def greet_user(update, context):
    user_id = update['message']['chat']['id']
    data_from_api = bot_api.start(user_id)
    context.user_data['greet'] = data_from_api["message"]
    update.message.reply_text(
        f'{context.user_data["greet"]}',
        reply_markup=keyboard
        )
