from models import user
from datetime import date,timedelta
admin='1869901487'
chat_id='-1001988279635'
def reminder(bot):
    try:
        users=user.user().get_all_user()
        print(users)
    except Exception as e:
        print(e)
    else:
        curdate=date.today()
        for k in users:
            if k['end_date']:
                difference=k['end_date']-curdate
                if k['end_date']==curdate :
                    bot.ban_chat_member(chat_id=chat_id,user_id=k['telegram_id'])
                    bot.send_message(k['telegram_id'],text="Your plan has expired")
                elif (difference.days <= 4) and (difference.days>0) :
                    bot.send_message(k['telegram_id'],text="your subscription is expiring soon")
            else :
                pass