import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s,%s)"
# adding the single row 
# val = (1, "Prashant", "shamshabad")
# adding mutliple rows at a time 

val = [
('Peter', 'Lowstreet 4'),
('Amy', 'Apple st 652'),
('Hannah', 'Mountain 21'),
('Michael', 'Valley 345'),
('Sandy', 'Ocean blvd 2'),
('Betty', 'Green Grass 1'),
('Richard', 'Sky st 331'),
('Susan', 'One way 98'),
('Vicky', 'Yellow Garden 2'),
('Ben', 'Park Lane 38'),
('William', 'Central st 954'),
('Chuck', 'Main Road 989'),
('Viola', 'Sideway 1633'),
('Arjun', 'Lake View 12'),
('Neha', 'Rose Street 45'),
('Rahul', 'Hill Road 8'),
('Kavya', 'Sunset Avenue 101'),
('Aman', 'Palm Grove 27')
]

# val = [
    
# ]

mycursor.executemany(sql,val)

mydb.commit() #commit is used to make updated without this commit i can't perform insertion hopefully i can explain myself

# print(mycursor.rowcount, "record inserted")
print(mycursor.rowcount, "records inserted", mycursor.lastrowid)


