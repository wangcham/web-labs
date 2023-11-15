import sqlite3

table = """
CREATE TABLE if not exists info(
    username VARCHAR(255),
    password VARCHAR(255),
    nickname VARCHAR(255),
    admin INT
)
"""

class Database:
    def execute(self,query,args=None):
        self.conn = None
        self.cursor = None

        try:
            self.conn = sqlite3.connect('sql.db')
            self.cursor = self.conn.cursor()

            if args:
                self.cursor.execute(query,args)
            else:
                self.cursor.execute(query)

            results = self.cursor.fetchall()
            self.conn.commit()

            return results
        
        except Exception as e:
            print("数据库操作失败,异常是"+str(e))
            if self.conn:
                self.conn.rollback()

        finally:
            if self.conn:
                self.conn.close()

    def create(self):
        self.execute(table)
        print("成功创建数据库")

    def addAdmin(self):
        sql = "select * from info where admin = ?"
        result = self.execute(sql,(1,))
        if result:
            print("管理员账户已经存在")
            return
        sql = "INSERT into info (username,password,nickname,admin) VALUES (?,?,?,?)"
        self.execute(sql,('admin','00000000','超级管理员',1))
        print("成功创建管理员账户")
