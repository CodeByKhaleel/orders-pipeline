import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="pipeline_user",
    password=DB_PASS,
    database="retail_orders"
)

if connection.is_connected():
    print("Successfully connected to MySQL!")
cursor = connection.cursor()
connection.close()