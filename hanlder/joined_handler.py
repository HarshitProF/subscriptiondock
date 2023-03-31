from telebot.types import CallbackQuery
from telebot import TeleBot
admin='1869901487'
# joined callback query
def joined(query:CallbackQuery,bot:TeleBot):
    print(query)
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    bot.send_message(query.message.from_user.id ,text="You have successfully joined")