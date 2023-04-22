from telebot import TeleBot
import os
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from models import user,plans
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
def all_users(message:Message,bot:TeleBot):
    try:
        results=user.user().get_all_user()
    except Exception as e:
        print(e)
    else:
        if results:
            bot.send_message(admin,text="These are your members",reply_markup=user_markup(results))
def user_markup(results):
    buttons=[InlineKeyboardButton(text=f"{k['telegram_id']}-{k['user_status']}-{k['start_date']}-{k['end_date']}",callback_data=f"viewuser-{k['telegram_id']}-{k['user_status']}-{k['start_date']}-{k['end_date']}") for k in results]
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(*buttons)
    return markup
# user view by admin callback query is "viwuser"
def viewuser(query:CallbackQuery,bot:TeleBot):
    data=query.data.split("-")
    print(data)
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    text=f"Telegram_id :- {data[1]} \n\nuser_status :- {data[2]}\n\n buy_date :- {data[3]}/{data[4]}/{data[5]}\n\n end_date :- {data[6]}/{data[7]}/{data[8]}"
    bot.send_message(admin ,text=text,reply_markup=ban_markup(data[1]))
# mark for user ban 
def ban_markup(telegram_id):
    buttons=[InlineKeyboardButton(text= "Ban User",callback_data=f"Ban-{telegram_id}"),InlineKeyboardButton(text= "UnBan",callback_data=f"Unban-{telegram_id}")]
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(*buttons)
    return markup
# ban query handler query is "ban"
def ban_user(query:CallbackQuery,bot:TeleBot):
    data=query.data.split("-")
    try:
        result=bot.ban_chat_member(chat_id=chat_id ,user_id=data[1])
    except Exception as e:
        print(e)
    else:
        if result==True:
            bot.send_message(admin, text="User banned Successfully")
            try:
                user.user().set_status(telegram_id=data[1],user_status="Banned")
            except Exception as e:
                print(e)
                pass
        else:
            bot.send_message(admin , text="Something went wrong")
# Unban query handler query is "Unban"
def Unban_user(query:CallbackQuery,bot:TeleBot):
    print("query recieved")
    data=query.data.split("-")
    try:
        result=bot.unban_chat_member(chat_id=chat_id ,user_id=data[1])
    except Exception as e:
        print(e)
    else:
        if result==True:
            bot.send_message(query.from_user.id , text="User Unbanned Successfully")
            try:
                user.user().set_status(telegram_id=data[1],user_status="UnBanned")
            except Exception as e:
                print(e)
                pass
        else:
            bot.send_message(query.from_user.id , text="Something went wrong")
def add_plan(message:Message,bot:TeleBot):
    text=f"Now send the plan Name , price and validity like this \n\n planName-price-validity"
    plan_message=bot.send_message(message.from_user.id,text=text)
    bot.register_next_step_handler(plan_message,callback=plans_adder,bot=bot)
def plans_adder(message:Message ,bot):
    text=message.text.split("-")
    try:
        if (text[1]) and (text[2]) :
            pass
    except Exception as e:
        print(e)
        bot.send_message(message.from_user.id,text="Invalid formate")
    else:
        try:
            plans.plans().add_plan(plan=text[0],price=text[1],validity=text[2])
        except Exception as e:
            print(e)
        else:
            bot.send_message(message.from_user.id,text="plan added successfully")
# get all plans
def get_plans(message:Message,bot:TeleBot):
    print(message)
    try:
        results=plans.plans().get_plans()
    except Exception as e:
        print(e)
    else:
        if results:
            bot.send_message(message.from_user.id,text="These are the following plans",reply_markup=plans_buttons(results))
def plans_buttons(results):
    buttons=[InlineKeyboardButton(text=f"{k['plan']}-{k['price']} USDT-{k['validity']} Days",callback_data=f"viewplan-{k['plan']}-{k['price']}-{k['validity']}") for k in results]
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(*buttons)
    return markup
# query is "viewplan"
def viewplan(query:CallbackQuery,bot:TeleBot):
    data=query.data.split("-")
    text=f"plan :- {data[1]}\n\n Price :- {data[2]}\n\n Validity :- {data[3]}"
    bot.send_message(query.from_user.id,text=text,reply_markup=plan_delete_button(plan=data[1]))
def plan_delete_button(plan):
    buttons=[InlineKeyboardButton(text="Delete",callback_data=f"deleteplan-{plan}")]
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(*buttons)
    return markup
# delete query handler 
def delete_plans(query:CallbackQuery,bot:TeleBot):
    data=query.data.split("-")
    print(data[1])
    try:
        plans.plans().delete_plan(plan=data[1])
    except Exception as e:
        bot.send_message(query.from_user.id,text="Something went wrong")
        print(e)
    else:
        bot.send_message(query.from_user.id,text="Plan deleted successfully")
# get user
def get_user_by_id(message:Message,bot:TeleBot):
    user_tele_id=bot.send_message(admin,text="send the telegram_id ")
    bot.register_next_step_handler(user_tele_id,callback=get_user_id,bot=bot)
def get_user_id(message:Message,bot):
    data=message.text
    try:
        required_user=user.user().get_user_by_telegram_id(data)
    except Exception as e:
        bot.send_message(admin,text="user not found")
    else:
        bot.send_message(message.from_user.id,text="this is the following user",reply_markup=user_markup([required_user]))
# send data of all users:
import pandas as pd
import io
def send_cvs(message:Message,bot:TeleBot):
    try:
        result=user.user().get_details()
    except Exception as e:
        print(e)
    data=pd.DataFrame(result)
    towrite=io.BytesIO()
    df.to_excel(towrite)
    bot.send_document(admin,document=towrite)
        