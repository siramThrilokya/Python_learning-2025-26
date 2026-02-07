import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name LIKE 's%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)