from telebot import TeleBot
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,Message
from models import user
admin='1869901487'
def status(message:Message,bot:TeleBot):
    try:
        result=user.user().get_user_by_telegram_id(message.from_user.id)
    except Exception as e:
        print(e)
    else:
        if result['end_date']:
            bot.send_message(message.from_user.id,text=f"Your subscription will expire on {result['end_date']}")
        else:
            bot.send_message(message.from_user.id,text="Your plan has expired or You do not have any plan")
