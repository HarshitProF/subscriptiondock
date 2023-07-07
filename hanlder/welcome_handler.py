from telebot import TeleBot 
from telebot.types import Message,ReplyKeyboardMarkup,KeyboardButton
from models import user
import os
from dotenv import load_dotenv
load_dotenv()
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
#welcome keyboard
def welcome_key():
    keys=["Plans","Status","Contact Support"]
    buttons=[KeyboardButton(k) for k in keys]
    markup=ReplyKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    return markup
def welcome(message:Message,bot:TeleBot):
    bot.send_message(message.from_user.id,text="welcome",reply_markup=welcome_key())
    try:
        user.user().insert_user(telegram_id=message.from_user.id,user_status="no subscription",fname=message.from_user.first_name,lname=message.from_user.last_name,username=message.from_user.username)
    except Exception as e:
        print(e)

