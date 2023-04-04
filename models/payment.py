import mysql.connector
import os
from urllib.parse import urlparse
resu=urlparse(os.getenv('CLEARDB_DATABASE_URL'))
class payment_model:
    def __init__(self):
        self.conn=mysql.connector.connect(host=resu.hostname,user=resu.username,password=resu.password,database=os.getenv('DB',default=None))
        self.cursor=self.conn.cursor()
    def insert_payment(self,transaction_hash,owner):
        query="insert into payment (transactions_hash,owner) values (%s,%s);"
        values=(transaction_hash,owner)
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