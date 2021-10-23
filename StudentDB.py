import sqlite3
connection = sqlite3.connect("student_detials.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
#cursor.execute('''DROP TABLE Student_Info;''')
connection.execute("create table Student_Info (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL , Roll_No TEXT NOT NULL, Age TEXT NOT NULL,  Mobile_No TEXT UNIQUE NOT NULL, Email TEXT UNIQUE NOT NULL)")
print("Table created successfully")
connection.close()   
