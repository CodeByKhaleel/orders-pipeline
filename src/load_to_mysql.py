import csv

records = []

with open('../data/processed/valid_orders.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        records.append((
            int(row['order_id']),
            row['customer_id'],
            row['order_date'][:10],
            row['product'],
            row['category'],
            int(row['quantity']),
            float(row['unit_price'])
        ))
print("Total records:", len(records))
print(records[0])
sql = """
INSERT INTO orders
(order_id, customer_id, order_date, product, category, quantity, unit_price)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="pipeline_user",
    password=DB_PASS,
    database="retail_orders"
)

cursor = connection.cursor()

cursor.executemany(sql, records)
connection.commit()

print("Records inserted:", cursor.rowcount)

cursor.close()
connection.close()