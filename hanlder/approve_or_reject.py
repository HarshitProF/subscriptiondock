from datetime import date,timedelta
from models import user,history_model
import json
from telebot import TeleBot
#admin='741728025'
admin='1869901487'
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
def approve(query:CallbackQuery,bot:TeleBot):
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    data=query.data.split('-')
    print(data)
    try:
        bot.unban_chat_member(chat_id='-1001988279635',user_id=data[1],only_if_banned=True)
    except  Exception as e:
        print(e)
    try:
        link=bot.create_chat_invite_link(chat_id='-1001988279635',member_limit=1)
    except Exception as e:
        print(e)
    else:
        curdate=date.today()
        validity=int(data[4])
        try:
            result_user=user.user().get_user_by_telegram_id(telegram_id=data[1])
        except Exception as e:
            raise Exception (e)
        else:
            bot.send_message(int(admin),text=f"User_id :- {result_user['telegram_id']}\n\n Name :-{result_user['fname']} {result_user['lname']}\n\n Username :- @{result_user['username']}\n\n {validity} Days membership activated")
            #bot.send_message(data[1],text=f"Congratulations admin approved the request",reply_markup=join_button(join_link=link.invite_link))
            if result_user['end_date']:
                if curdate<=result_user['end_date'] :
                    difference=result_user['end_date']-curdate
                    print(difference.days)
                    validity+=difference.days
                    print(validity)
            end_date=curdate + timedelta(days=validity)
            try:
                user.user().set_buy(start_date=curdate,end_date=end_date,user_status="active",telegram_id=data[1])  
            except Exception as e:
                print(e)
            else:
                try:
                    history_model.history().add_data(owner=result_user['user_id'],plan=data[2],price=data[3],validity=data[4],buy_date=curdate)
                except Exception as e:
                    print(e)
                if result_user['user_status']=="active":
                    bot.send_message(result_user['telegram_id'],text=f"Your validity extended {validity-difference.days} days .Now expiry date is {end_date}")
                else:
                    bot.send_message(data[1],text=f"Congratulations admin approved the request",reply_markup=join_button(join_link=link.invite_link))
                    
# join button
def join_button(join_link):
    buttons=[InlineKeyboardButton(text="Join",url=join_link,callback_data="joined")]
    markup=InlineKeyboardMarkup()
    markup.add(*buttons)
    return markup
#reject callback handler
def reject(query:CallbackQuery,bot:TeleBot):
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    data=query.data.split("-")
    bot.send_message(data[1],text="Please submit valid transaction hash , your request was rejected by admin")