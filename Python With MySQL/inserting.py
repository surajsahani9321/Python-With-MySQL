import mysql.connector

print("Name : Suraj Shriram Sahani")
print("Roll Number : 237")
print("Division : SEB\n")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")

cur = myconn.cursor()


sql="insert into personaldata(id,name,current_status,best_friend,passion,dream) VALUES(%s, %s, %s, %s, %s,%s)"

val=("3","Amit Sahani", "Computer Enginerring Student", "Ankit Yadav", "Java And Python Programming", "Become A Perfect Java And Python Programmer")

cur.execute(sql,val)


sql2 = "insert into personaldata(id,name,current_status,best_friend,passion,dream) VALUES(%s, %s, %s, %s, %s,%s)"

val2 = ("4","Ankit Yadav", "Computer Enginerring Student", "Amit Sahani", "Python Programming", "Become A Perfect Python Programmer And Web Developer")

cur.execute(sql2,val2)


myconn.commit()
print(cur.rowcount, "record inserted!")
