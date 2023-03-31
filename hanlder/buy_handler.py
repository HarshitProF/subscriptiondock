from telebot import TeleBot
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from models import user,payment

#admin='741728025'
admin='1869901487'
def buy(query:CallbackQuery,bot:TeleBot):
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    data=query.data.split("-")
    text="Submit your Transaction ID/ Hash"
    message_buy=bot.send_message(query.from_user.id,text=text)
    bot.register_next_step_handler(message_buy,callback=get_hash,plan=data[1],price=data[2],validity=data[3],bot=bot)
def get_hash(message:Message,bot,price,plan,validity):
    if len(message.text)<32:
        again1=bot.send_message(message.from_user.id ,text="Invalid Transaction hash/id, Send again")
        bot.register_next_step_handler(again1,callback=get_hash,plan=plan,price=price,validity=validity,bot=bot)
    try:
        result=user.user().get_user_by_telegram_id(telegram_id=message.from_user.id)
    except Exception as e:
        print(e)
    else:
        #print(result)
        try:
            payment.payment_model().insert_payment(transaction_hash=message.text,owner=result['user_id'])
        except Exception as e:
            bot.send_message(message.from_user.id , text="Transaction hash/id already used")
            print(e)
        else:
            text=F"the user {message.from_user.id} and\n\n username :- @{result['username']} \n\nName :- {result['fanme']} {result['lname']} wanted to buy the following plan \n price is {price } \n plan is {plan} \n validity is {validity}\n\n Hash is :- {message.text}"
            #send this to admin for approve or reject
            if validity=="LifeTime":
                validity=800
                bot.send_message(admin,text,reply_markup=approve_or_reject(plan,price,validity,user=message.from_user.id))
            else:
                bot.send_message(admin,text,reply_markup=approve_or_reject(plan,price,validity,user=message.from_user.id))
            bot.send_message(message.from_user.id , text="We have forwarded your request to admin")
def approve_or_reject(plan,price,validity,user):
    buttons=[InlineKeyboardButton(text="Approve",callback_data=F"approve-{user}-{plan}-{price}-{validity}"),InlineKeyboardButton(text="Reject",callback_data=f"reject-{user}")]
    markup=InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    return markup
