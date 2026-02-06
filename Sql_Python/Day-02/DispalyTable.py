import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

# fetching only name and address
# mycursor.execute('SELECT * FROM Customers')
mycursor.execute('SELECT name,address FROM Customers')


myresult = mycursor.fetchall() # fetchall is used to fetch all the rows and last executed statement

for x in myresult:
    print(x)
    
    
