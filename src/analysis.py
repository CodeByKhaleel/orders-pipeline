import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="pipeline_user",
    password=DB_PASS,
    database="retail_orders"
)
cursor = connection.cursor()

