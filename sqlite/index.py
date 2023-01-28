import sqlite3

class Database:
    def __init__(self,db):
        self.db=db
        self.cur=''
    def connecteDatabase(self):
        self.con=sqlite3.connect(self.db)
        self.cur=self.con.cursor()
        if self.con:
            print("connected successfully")
    def CreateTable(self,table):
        sql="CREATE TABLE `"+table+"`(name text, phone text, email text)"
        res=self.cur.execute(sql)
        if sql:
            print("Table created successfully")
    def Insert(self,table,name, phone, email):
        sql="INSERT INTO `"+table+"`(name, phone, email )values(?,?,?) "
        result=self.cur.execute(sql,(name, phone, email))
        self.con.commit()
    def closeConnection(self):
        self.con.close()
