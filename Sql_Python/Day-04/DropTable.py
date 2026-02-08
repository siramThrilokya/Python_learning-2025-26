import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

# sql = 'DROP TABLE Customers'

# drop only when exists 
sql = "DROP TABLE IF EXISTS Customers"

mycursor.execute(sql)