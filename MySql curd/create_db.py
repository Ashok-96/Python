import mysql.connector
mydb = mysql.connector.connect(
host="127.0.0.1",
  user="root",
  password="",
  database='python'
  )

input=('1','ashok')

mycursor=mydb.cursor()
query="""INSERT INTO python (id, name) VALUES (%s,%s)"""

mycursor.execute(query, input)

mydb.commit()

print('the num rows affected:'+mycursor.rowcount)
