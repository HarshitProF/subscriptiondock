from telebot import TeleBot
import os
apikey=os.getenv('TOKEN',default=None)
chat_id=os.getenv('CHAT_ID',default=None)
admin=os.getenv('ADMIN_ID',default=None)
print(apikey)
bot=TeleBot(apikey)