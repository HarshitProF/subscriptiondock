import mysql.connector
class payment_model:
    def __init__(self):
        self.conn=mysql.connector.connect(host="us-cdbr-east-06.cleardb.net",user="b26ed14e9970fb",password="e09e3491",database="heroku_062a08291def40a")
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