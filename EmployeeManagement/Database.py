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
    def Insert(self,details):
        print(tuple(details.values()))
        sql="INSERT INTO `Employee` ('Name', 'Age','DOJ', 'Gender', 'Email', 'Contact', 'Address' )values(?,?,?,?,?,?,?)"
        self.cur.execute(sql,tuple(details.values()))
        self.con.commit()

    def closeConnection(self):
        self.con.close()

