import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycusor = mydb.cursor()

mycusor.execute("CREATE TABLE Customers (name varchar(25), address varchar(255))")


# if table is existes 

# mycusor.execute("SHOW TABLES")

for x in mycusor:
    print(x)