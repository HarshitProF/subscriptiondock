import mysql.connector
import os
class history:
    def __init__(self):
        self.conn=mysql.connector.connect(host=os.getenv('HOST',default=None),user=os.getenv('USER',default=None),password=os.getenv('PAS_W',default=None),database=os.getenv('DB',default=None))
        self.cursor=self.conn.cursor()
    def add_data(self,owner,plan,price,validity,buy_date):
        values=(owner,plan,price,validity,buy_date)
        query="insert into user_history (owner,plan,price,validity,buy_date) VALUES (%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(query,values)
        except Exception as e:
            raise Exception(e)
        else:
            try:
                self.conn.commit()
            except Exception as e:
                raise Exception (e)
            try:
                self.conn.close()
            except:
                pass
    def get_data_by_user(self,owner):
        values=(owner,)
        query="select * from user_history where owner=%s"
        try:
            self.cursor.execute(query,values)
        except Exception as e:
            raise Exception(e)
        else:
            datas=[]
            results=self.cursor.fetchall()
            if results:
                for result in results:
                    data={"owner":result[0],"plan":result[1],"price":result[2],"validity":result[3],"buy_date":result[4]}
                    datas.append(data)
                return datas
            if not results:
                raise Exception("No data found")
            try:
                self.conn.close()
            except :
                pass