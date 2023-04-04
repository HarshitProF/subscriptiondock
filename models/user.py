import mysql.connector
import os
class user:
    def __init__(self):
        print(f"{os.getenv('HOST',default=None)}  {os.getenv('USER',default=None)}  {os.getenv('PWD')}  {os.getenv('DB',default=None)}")
        self.conn=mysql.connector.connect(host=os.getenv('HOST',default=None),user=os.getenv('USER',default=None),password=os.getenv('PWD',default=None),database=os.getenv('DB',default=None))
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
    