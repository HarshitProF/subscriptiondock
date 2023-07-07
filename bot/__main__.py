from . import bot
import threading
import os
import apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from hanlder import tesks
from dotenv import load_dotenv
load_dotenv()

#admin='741728025'
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
import datetime
import os
from urllib.parse import urlparse
url=str(os.getenv('CLEARDB_DATABASE_URL'))
if __name__=="__main__":
    print(datetime.datetime.now())
    from register_handlers import register
    register.register().add(bot)
    job_stores={'defualt':SQLAlchemyJobStore(url=url, tablename="jobs")}
    schedule=BackgroundScheduler(job_stores=job_stores,demon=True,timezone="Asia/kolkata")
    schedule.add_job(func=tesks.reminder ,kwargs={'bot':bot},trigger='cron',hour='17',minute='50')
    schedule.start()
    print(schedule.get_jobs())
    bot.infinity_polling(allowed_updates=['message','callback_query','my_chat_member','chat_member'])