import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="dcrm"
)   

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm")
print("All Done!")