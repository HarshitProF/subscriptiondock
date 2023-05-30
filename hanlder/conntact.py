from telebot import TeleBot
from telebot.types import Message
import os
admins=["@jhonnyCrypto","@LogannCrypto","@ZachCryptoAD","@AlexRoseAdmin","@CHIEF099","@zachcryptoad","@loganncrypto"]

chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
def send_contact(message:Message,bot:TeleBot):
    if chat_id=="-1001978412172":

        bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[6]}")
    if chat_id=="-1001912770234":

        bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[5]}")
    
    if chat_id=="-1001691747162":
        bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[2]}")
    elif chat_id=="-1001696317955":
        bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[3]}")
    elif chat_id=="-1001633570949":
        bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[4]}")
    elif chat_id=="-1001566254717":
        bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[1]}")
    else:
        pass
        #bot.send_message(message.from_user.id,text=f"Please contact to admin {admins[0]}")
