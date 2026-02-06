import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (Id, name, address) VALUES (%s,%s,%s)"
val = (1, "Prashant", "shamshabad")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted")