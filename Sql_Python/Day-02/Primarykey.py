import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customer2 (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(25), address varchar(255))")
