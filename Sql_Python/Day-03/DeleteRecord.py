import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM Customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted !")


# prevent sql injection 

sql = "DELETE FROM Customers WHERE address = %s"
add = ('Mountain 21',)

mycursor.execute(sql,add)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted !")