import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")
print(myconn)
cur=myconn.cursor()
print(cur)
try:
    print("hi")
    # cur.execute("create table emp1(name varchar(50),salary varchar(50),department varchar(50))")
    # cur.execute("insert into emp1(name,salary,department) values('Suraj Sahani','100','manager')")
    # cur.execute("insert into emp1(name,salary,department) values('Suraj Sahani','100','manager')")
    # cur.execute("insert into emp1(name,salary,department) values('Suraj Sahani','100','manager')")
    # cur.execute("insert into emp1(name,salary,department) values('Suraj Sahani','100','manager')")
    # cur.execute("insert into emp1(name,salary,department) values('Suraj Sahani','100','manager')")
    # cur.execute("insert into emp1(name,salary,department) values('Suraj Sahani','100','manager')")
    # cur.execute("update  emp1 set name='Anjali' where name='Suraj Sahani'")
    # cur.execute("delete from emp1 where name='Anjali'")
    cur.execute("select * from emp1")
    m=cur.fetchall()
    for x in m:
        print(x)

    # myconn.commit()
    print("table created")
except:
    myconn.rollback()

myconn.close()


