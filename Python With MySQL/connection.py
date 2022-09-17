import mysql.connector

print("Name : Suraj Shriram Sahani")
print("Roll Number : 237")
print("Division : SEB\n")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")

print(myconn)

cur = myconn.cursor()

print(cur)