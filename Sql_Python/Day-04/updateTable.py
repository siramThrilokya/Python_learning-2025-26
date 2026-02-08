import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

# sql= "UPDATE Customers SET address = 'shamshabad' WHERE address= 'valley 345'"

# prevent from sql injection 

sql= "UPDATE Customers SET address = %s WHERE address= %s"
val = ("shamshabad","valley 345")

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

