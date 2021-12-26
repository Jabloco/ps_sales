def greet_user(update, context):
    update.message.reply_text('Hello')
    print(update)
    print(context)