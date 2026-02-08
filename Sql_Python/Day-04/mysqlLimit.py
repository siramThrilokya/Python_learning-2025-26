import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

# mycursor.execute('SELECT * FROM Customers LIMIT 5')

# start from another position 

mycursor.execute('SELECT * FROM Customers LIMIT 5 OFFSET 2')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)