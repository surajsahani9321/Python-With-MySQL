import mysql.connector

print("Name : Suraj Shriram Sahani")
print("Roll Number : 237")
print("Division : SEB\n")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")

cur = myconn.cursor()

sql="delete from personaldata where best_friend='Ankit Yadav'"

cur.execute(sql)

sql="delete from  personaldata where best_friend='Amit Sahani'"

cur.execute(sql)

myconn.commit()
print("Deleted Successfully")
