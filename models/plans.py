import mysql.connector
class plans:
    def __init__(self):
        self.conn=mysql.connector.connect(host="us-cdbr-east-06.cleardb.net",user="b26ed14e9970fb",password="e09e3491",database="heroku_062a08291def40a")
        self.cursor=self.conn.cursor()
    def add_plan(self,plan,price ,validity):
        query="insert into plans (plan,price,validity) values (%s,%s,%s);"
        values=(plan,price,validity)
        try:
            result=self.cursor.execute(query,values)

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
    def get_plans(self):
        query="select * from plans"
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise Exception(e)
        else:
            datas=[]
            results=self.cursor.fetchall()
            if results:
                for result in results:
                    data={"plan":result[0],"price":result[1],"validity":result[2]}
                    datas.append(data)
                return datas
            if not results:
                raise Exception("No data found")
            try:
                self.conn.close()
            except :
                pass
    def get_plan(self,plan):
        query=f"select * from plans where plan=%s"
        values=(plan,)
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
                return {"plan":result[0],"price":result[1],"validity":result[2]}
            if not result:
                raise Exception("plan not found")
    def delete_plan(self,plan):
        query="delete from plans Where plan=%s "
        values=(plan,)
        try:
            self.cursor.execute(query,values)
        except Exception as e:
            print(e)
            raise Exception (e)
        else:
            try:
                self.conn.commit()
            except Exception as e:
                raise Exception(e)
            else:
                try:
                    self.conn.close()
                except:
                    pass