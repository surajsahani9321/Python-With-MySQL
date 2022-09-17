import mysql.connector

print("Name : Suraj Shriram Sahani")
print("Roll Number : 237")
print("Division : SEB\n")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")

cur = myconn.cursor()

cur.execute("select * from personaldata")
result = cur.fetchall()

for x in result:
     print(x)