import mysql.connector

print("Name : Suraj Shriram Sahani")
print("Roll Number : 237")
print("Division : SEB\n")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")

cur = myconn.cursor()

sql="update personaldata set best_friend='Shraddha Programmer' where best_friend='Shraddha Yadav'"

cur.execute(sql)

sql="update personaldata set best_friend='Suraj Programmer' where best_friend='Suraj Sahani'"

cur.execute(sql)

myconn.commit()
print("Updated Successfully")
