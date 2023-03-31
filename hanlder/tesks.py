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
                    try:
                        user.user().set_status(telegram_id=k['telegram_id'],user_status="Banned")
                    except Exception as e:
                        print(e)
                    text=f"Name :- {k['fname']} {k['lname']} \n\n Username :-@{k['username']} \n\n His plan has expired"
                    bot.send_message(int(admin),text=text)
                elif (difference.days <= 4) and (difference.days>=1) :
                    bot.send_message(k['telegram_id'],text="your subscription is expiring soon")
            else :
                pass