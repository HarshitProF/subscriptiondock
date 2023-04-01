import os
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
from hanlder import welcome_handler,plan_handler,buy_handler,joined_handler,back,conntact,approve_or_reject,admin_handler,tesks,status,chat_member
class register:
    def __init__(self):
        pass
    def add(self,bot):
        bot.register_message_handler(welcome_handler.welcome,commands=['start'],pass_bot=True)
        bot.register_message_handler(conntact.send_contact,func=lambda message : message.text=="Contact Support",pass_bot=True)
        bot.register_message_handler(admin_handler.all_users,commands=['all_users'],func=lambda message : message.from_user.id==int(admin),pass_bot=True)
        bot.register_message_handler(admin_handler.add_plan,commands=['add_plan'],func=lambda message : message.from_user.id==int(admin),pass_bot=True)
        bot.register_message_handler(admin_handler.get_plans,commands=['all_plans'],func=lambda message : message.from_user.id==int(admin),pass_bot=True)
        bot.register_message_handler(plan_handler.send_plans,func=lambda message : message.text=="Plans",pass_bot=True)
        bot.register_message_handler(status.status,func=lambda message : message.text=="Status",pass_bot=True)
        bot.register_callback_query_handler(plan_handler.plan_handle,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="plans",pass_bot=True)
        bot.register_callback_query_handler(buy_handler.buy,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="buy",pass_bot=True)
        bot.register_callback_query_handler(approve_or_reject.approve,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="approve",pass_bot=True)
        bot.register_callback_query_handler(admin_handler.viewuser,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="viewuser",pass_bot=True)
        bot.register_callback_query_handler(admin_handler.ban_user,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="Ban",pass_bot=True)
        bot.register_callback_query_handler(admin_handler.Unban_user,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="Unban",pass_bot=True)
        bot.register_callback_query_handler(admin_handler.viewplan,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="viewplan",pass_bot=True)
        bot.register_callback_query_handler(back.back,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="back",pass_bot=True)
        bot.register_callback_query_handler(admin_handler.delete_plans,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="deleteplan",pass_bot=True)
        bot.register_chat_member_handler(callback=chat_member.chat_member,pass_bot=True)
        bot.register_callback_query_handler(joined_handler.joined,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="joined",pass_bot=True)
        bot.register_callback_query_handler(approve_or_reject.reject,func=lambda CallbackQuery:CallbackQuery.data.split("-")[0]=="reject",pass_bot=True)