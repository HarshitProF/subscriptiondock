from bot import bot
from hanlder import tesks
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
job_stores={'defualt':SQLAlchemyJobStore(url="mysql://root:H@r$hit1@localhost:3306/subscription", tablename="jobs")}
schedule=BackgroundScheduler(job_stores=job_stores,demon=True,timezone="Asia/Kolkata")
schedule.add_job(func=tesks.reminder ,kwargs={'bot':bot},trigger='cron',hour='21',minute='36')
print(schedule.get_jobs())