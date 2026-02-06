import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

# fetching based upon the condition 
mycursor.execute("SELECT * FROM Customers WHERE id = 104")

myresult = mycursor.fetchall()

print(myresult)


