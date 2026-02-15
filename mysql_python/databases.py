import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="bismillah"
)
cursor1=conn.cursor()
# cursor1.execute("SHOW DATABASES")
# for x in cursor1:
#     print(x)
#
# cursor1.execute("CREATE DATABASE school1")
#
# cursor1.execute("SHOW DATABASES")
# for x in cursor1:
#     print(x)
q='''
CREATE TABLE students(
roll INT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
marks INT,
dob DATE NOT NULL,
division INT 5 NOT NULL
)
'''
cursor1.execute(q)
