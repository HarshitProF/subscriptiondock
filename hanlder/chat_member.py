from telebot import TeleBot
import os
from datetime import date
from  models import user
from telebot.types import Message,ChatMemberUpdated,ChatJoinRequest
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)


from models import link
def chat_member(message:ChatMemberUpdated,bot:TeleBot):
    print(message.invite_link)
    try:
        required_user=user.user().get_user_by_telegram_id(message.new_chat_member.id)
    except Exception as e:
        dat=str(e).split(" ")
        print(dat)
        if dat[0]=="user":
            try:
                bot.ban_chat_member(chat_id=chat_id,user_id=message.new_chat_member.user.id)
            except Exception as e:
                print(e)
        else:
            print("not user")
            print(e)
    else:

        curdate=date.today()
        if  (not required_user['end_date']) or (required_user['end_date']<curdate) :
            try:
                bot.ban_chat_member(chat_id=chat_id,user_id=message.new_chat_member.user.id)
                print("banned")
            except Exception as e:
                print(e)
            return
        try:
            if message.invite_link :
                link.link_model().insert_link(message.invite_link.invite_link)
        except Exception as e:
            print(e)
            bot.ban_chat_member(chat_id=chat_id,user_id=message.new_chat_member.user.id)
        else:
            if hasattr(message.invite_link,'invite_link'):
                result=bot.revoke_chat_invite_link(chat_id=chat_id,invite_link=message.invite_link.invite_link)
                #print(result)