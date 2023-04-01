from telebot.types import CallbackQuery
from telebot import TeleBot
import os
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
# joined callback query
def joined(query:CallbackQuery,bot:TeleBot):
    print(query)
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    bot.send_message(query.message.from_user.id ,text="You have successfully joined")