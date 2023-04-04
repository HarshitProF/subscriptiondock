from . import bot
import threading
import os
import apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from hanlder import tesks

#admin='741728025'
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
import datetime

if __name__=="__main__":
    print(datetime.datetime.now())
    from register_handlers import register
    register.register().add(bot)
    job_stores={'defualt':SQLAlchemyJobStore(url="mysql://root:H@r$hit1@localhost:3306/subscription", tablename="jobs")}
    schedule=BackgroundScheduler(job_stores=job_stores,demon=True,timezone="Eastern time")
    schedule.add_job(func=tesks.reminder ,kwargs={'bot':bot},trigger='cron',hour='12',minute='00')
    schedule.start()
    print(schedule.get_jobs())
    bot.infinity_polling(allowed_updates=['message','callback_query','my_chat_member','chat_member'])