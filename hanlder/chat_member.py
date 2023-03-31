from telebot import TeleBot
from telebot.types import Message,ChatMemberUpdated,ChatJoinRequest
chat_id='-1001988279635'
admin='1869901487'
from models import link
def chat_member(message:ChatMemberUpdated,bot:TeleBot):
    print(message.invite_link)
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