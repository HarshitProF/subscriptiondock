import mysql.connector
import os
class link_model:
    def __init__(self):
        self.conn=mysql.connector.connect(host=os.getenv('HOST',default=None),user=os.getenv('USER',default=None),password=os.getenv('PWD',default=None),database=os.getenv('DB',default=None))
        self.cursor=self.conn.cursor()
    def insert_link(self,invite_link):
        query="insert into invite_link (link) values (%s);"
        values=(invite_link,)
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