from telebot import TeleBot
from telebot.types import Message
def send_contact(message:Message,bot:TeleBot):
    bot.send_message(message.from_user.id,text=f"Please contact to admin @jhonnyCrypto")