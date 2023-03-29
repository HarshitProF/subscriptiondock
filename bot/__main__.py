from . import bot
import threading
from telebot import util
#from telebot.util.update_types import message,callback_query,my_chat_member,chat_member,chat_join_request
#import apscheduler
admin='741728025'
from hanlder import welcome_handler,plan_handler,buy_handler,joined_handler,back,conntact,approve_or_reject,admin_handler,tesks,status,chat_member

if __name__=="__main__":
    from register_handlers import register
    register.register(bot)
    #schedule=BackgroundScheduler(job_stores=job_stores,demon=True,timezone="Asia/Kolkata")
    #schedule.add_job(func=tesks.reminder ,kwargs={'bot':bot},trigger='cron',hour='21',minute='36')
    #print(schedule.get_jobs())
    bot.infinity_polling(allowed_updates=['message','callback_query','my_chat_member','chat_member'])