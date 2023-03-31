from telebot import TeleBot
from telebot.types import Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from models import plans
admin='1869901487'

# inline buttons for plans
def plans_buttons():
    try:
        results=plans.plans().get_plans()
    except Exception as e:
        print(e)
        raise Exception (e)
    else:
        buttons=[InlineKeyboardButton(text=f"{k['plan']}--{k['price']} USDT--{k['validity']} Days",callback_data=f"plans-{k['plan']}-{k['price']}-{k['validity']}") for k in results]
        markup=InlineKeyboardMarkup(row_width=1)
        markup.add(*buttons)
        return markup
def send_plans(message:Message,bot:TeleBot):
    bot.send_message(message.from_user.id,text="Select Your Plan",reply_markup=plans_buttons())
# plan callback query handler
def plan_handle(query:CallbackQuery,bot:TeleBot):
    bot.delete_message(chat_id=query.from_user.id ,message_id=query.message.id)
    data=query.data.split("-")
    text=f"plan validity is {data[3]} Days\n\n price is {data[2]} USDT"
    bot.send_message(query.from_user.id,text=text,reply_markup=plans_buy_back(plan=data[1],price=data[2],validity=data[3]))

# buttons with plan callback query
def plans_buy_back(plan,price,validity):
    buttons=[InlineKeyboardButton(text="Go To Next Step",callback_data=f"buy-{plan}-{price}-{validity}"),InlineKeyboardButton(text="Back To Main Menu ",callback_data="back")]
    markup=InlineKeyboardMarkup(row_width=2)
    markup.add(*buttons)
    return markup
