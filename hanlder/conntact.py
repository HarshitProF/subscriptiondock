from telebot import TeleBot
from telebot.types import Message
admin='1869901487'
def send_contact(message:Message,bot:TeleBot):
    bot.send_message(message.from_user.id,text=f"Please contact to admin @jhonnyCrypto")