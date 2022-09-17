import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonwithmysql")

# printing the connection object
print(myconn)

cur = myconn.cursor()

print(cur)

# try:
#     dbs = cur.execute("show databases")
# except:
#     myconn.rollback()
# for x in cur:
#     print(x)
# myconn.close()

sql = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"

# The row values are provided in the form of tuple
# val = ("Suraj Sahani", 2, 50000, 201, "Kopar Khairane")
# val = [("Suraj Sahani", 102, 25000.00, 201, "IT"),("Anjali Gupta",103,25000.00,202,"IT"),("Shraddha Yadav",104,90000.00,203,"IT")]
# val = ("Sonu",105,28000,202,"Guyana")
try:
    # # inserting the values into the table
    # cur.execute(sql, val)
    # # cur.executemany(sql,val)
    # # commit the transaction
    # myconn.commit()
    # print(cur.rowcount, "record inserted! id:", cur.lastrowid)

    # cur.execute("select * from Employee")
    # cur.execute("select name, id, salary from Employee")
    # cur.execute("select name, id, salary from Employee where name like 'J%'")
    # cur.execute("select name, id, salary from Employee where id in (101,102,103)")
    # cur.execute("select name, id, salary from Employee order by name")
    # cur.execute("select name, id, salary from Employee order by name desc")
    # cur.execute("update Employee set name = 'alex' where id = 110")
    cur.execute("delete from Employee where id = 110")
    # fetching the rows from the cursor object
    # result = cur.fetchall()
    # # printing the result
    #
    #
    #
    # for x in result:
    #     print(x);

    # result = cur.fetchone()
    #
    # # printing the result
    # print(result)

    # print("Name    id    Salary");
    # for row in result:
    #     print("%s    %d    %d" % (row[0], row[1], row[2]))

    myconn.commit()
except:
    myconn.rollback()

print(cur.rowcount, "record inserted!")
myconn.close()