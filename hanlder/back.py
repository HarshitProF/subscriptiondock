from telebot import TeleBot
from telebot.types import CallbackQuery,KeyboardButton,ReplyKeyboardMarkup
def welcome_key():
    keys=["Plans","Status","Contact Support"]
    buttons=[KeyboardButton(k) for k in keys]
    markup=ReplyKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    return markup
def back(query:CallbackQuery,bot:TeleBot):
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    bot.send_message(query.from_user.id,text="Welcome to Main Menu",reply_markup=welcome_key())