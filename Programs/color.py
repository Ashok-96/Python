from pyfiglet import figlet_format as pfg
import mysql.connector
from termcolor import colored
import sqlite3 
result= pfg("Ashokkumar")
colored_ascii=colored(result, color="green",)
print(colored_ascii)
#pyfiglet
mydb=mysql.connector.connect(host="localhost", user="root", password="",database='users')
mycursor=mydb.cursor()
print(mydb)
connection=sqlite3.connect('demo.db')
cursor=connection.cursor()
print(cursor)
sql="SELECT * FROM `users`"
mycursor.execute(sql)
res=mycursor.fetchone()
for user in res:
    print(user)