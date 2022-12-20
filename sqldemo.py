#ZERO version

import mysql.connector

mydb=mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="users"
)

c=mydb.cursor()
sql="SELECT * FROM `users`"
c.execute(sql)
print(c.fetchall()[0])

