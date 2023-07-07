import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
from urllib.parse import urlparse
resu=urlparse(os.getenv('CLEARDB_DATABASE_URL'))
#print(resu)

class user:
    def __init__(self):
        #print(f"{os.getenv('HOST',default=None)}  {os.getenv('USER',default=None)}  {os.getenv('PAS_W')}  {os.getenv('DB',default=None)}")
        self.conn=mysql.connector.connect(host=resu.hostname,user=resu.username,password=resu.password,database=os.getenv('DB',default=None))
        self.cursor=self.conn.cursor()
    def insert_user(self,telegram_id,user_status,fname,lname,username):
        query="insert into user (telegram_id ,user_status,fname,lname,username) values (%s,%s,%s,%s,%s);"
        values=(telegram_id,user_status,fname,lname,username)
        try:
            result=self.cursor.execute(query, values)

        except Exception as e :
            print(e)
            raise Exception("something went wrong")
        else:
            try:
                self.conn.commit()
            except Exception as e:
                raise Exception(e)
        finally:
            try :
                self.conn.close()
            except:
                pass
    def get_user(self,user_id):
        query=f"select * from user where user_id=%s"
        values=(user_id,)
        try:
            self.cursor.execute(query,values)
        except  Exception as e:
            raise Exception(e)
        else:
            result=self.cursor.fetchone()
            try:
                self.conn.close()
            except:
                pass
            if result:
                return {"user_id":result[0],"telegram_id":result[1],"user_status":result[2],"start_date":result[3],"end_date":result[4],"fname":result[5],"lname":result[6],"username":result[7]}
            if not result:
                raise Exception("user not found")
    def get_user_by_telegram_id2(self,telegram_id):
        values=(telegram_id,)
        query="select * from user where telegram_id=%s "
        try:
            self.cursor.execute(query,values)
        except  Exception as e:
            raise Exception(e)
        else:
            result=self.cursor.fetchone()
            try:
                self.conn.close()
            except:
                pass
            if result:
                return {"user_id":result[0],"telegram_id":result[1],"user_status":result[2],"start_date":result[3],"end_date":result[4],"fname":result[5],"lname":result[6],"username":result[7]}
            if not result:
                return result
    def get_user_by_telegram_id(self,telegram_id):
        values=(telegram_id,)
        query="select * from user where telegram_id=%s "
        try:
            self.cursor.execute(query,values)
        except  Exception as e:
            raise Exception(e)
        else:
            result=self.cursor.fetchone()
            try:
                self.conn.close()
            except:
                pass
            if result:
                return {"user_id":result[0],"telegram_id":result[1],"user_status":result[2],"start_date":result[3],"end_date":result[4],"fname":result[5],"lname":result[6],"username":result[7]}
            if not result:
                raise Exception("user not found")
    def set_status(self,telegram_id,user_status):
        values=(user_status,telegram_id)
        query="UPDATE user SET user_status =%s WHERE telegram_id=%s ;"
        try:
            self.cursor.execute(query,values)
        except Exception as e:
            print (e)
            raise Exception("something is wrong")
        else:
            try: 
                self.conn.commit()
            except Exception as e:
                raise Exception(e)
            try :
                self.conn.close()
            except:
                pass
    def set_buy(self,start_date,telegram_id,end_date,user_status):
        values=(start_date,end_date,user_status,telegram_id)
        query="UPDATE user SET start_date =%s ,end_date=%s ,user_status=%s WHERE telegram_id=%s ;"
        try:
            self.cursor.execute(query,values)
        except Exception as e:
            print (e)
            raise Exception(e)
        else:
            try: 
                self.conn.commit()
            except Exception as e:
                raise Exception(e)
            try :
                self.conn.close()
            except:
                pass
    def get_all_user(self):
        query="select * from user"
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise Exception(e)
        else:
            datas=[]
            results=self.cursor.fetchall()
            if results:
                for result in results:
                    data={"user_id":result[0],"telegram_id":result[1],"user_status":result[2],"start_date":result[3],"end_date":result[4],"fname":result[5],"lname":result[6],"username":result[7]}
                    datas.append(data)
                return datas
            if not results:
                raise Exception("No data found")
            try:
                self.conn.close()
            except :
                pass
    def get_details(self):
        query="select   user_id,telegram_id ,user_status,start_date,end_date,fname,lname,username, user_history.plan,user_history.price,payment.transactions_hash from user Inner join user_history on user.user_id=user_history.owner inner join payment on user_history.owner=payment.owner "
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise Exception(e)
        else:
            results=self.cursor.fetchall()
            try:
                self.conn.close()
            except Exception as e:
                print(e)
            return results
        
class user_method:
    def __init__(self):
        self.user=user()
    def buy(self,user_id,price):
        try:
            required_user=self.user.get_user(user_id)
        except Exception as e:
            raise Exception(e)
        else:
            if (required_user['balance']>=price):
                balance=required_user['balance']-price
                try:
                    user().set_balance(user_id=user_id,balance=balance)
                except Exception as e:
                    raise Exception(e)
            else:
                raise Exception("insufficient balance")
    def addfunds(self,user_id,amount):
        try:
            required_user=self.user.get_user(user_id)
        except Exception as e:
            raise Exception(e)
        else:
            balance=required_user['balance']+int(amount)
            try:
                user().set_balance(user_id=user_id,balance=balance)
            except Exception as e:
                raise Exception(e)
    def addfunds_by_telegram_id(self,telegram_id,amount):
        try:
            required_user=self.user.get_user_by_telegram_id(int(telegram_id))
        except Exception as e:
            print("user not found")
            raise Exception(e)
        else:
            balance=int(required_user['balance'])+int(float(amount))
            try:
                user().set_balance(user_id=required_user['user_id'],balance=balance)
            except Exception as e:
                raise Exception(e)
    