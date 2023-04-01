from telebot import TeleBot
from telebot.types import Message
import os
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
def send_contact(message:Message,bot:TeleBot):
    bot.send_message(message.from_user.id,text=f"Please contact to admin @jhonnyCrypto")