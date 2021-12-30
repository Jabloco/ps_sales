from api_client import BotApiClient


bot_api = BotApiClient()


def greet_user(update, context):
    user_id = update['message']['chat']['id']
    data_from_api = bot_api.start(user_id)
    update.message.reply_text(data_from_api['message'])
