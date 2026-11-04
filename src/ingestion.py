import csv
from datetime import datetime
valid_rows = []
rejected_rows = []
with open('../data/raw/orders.csv') as read_data:
    table = csv.reader(read_data)
    next(table)
    for row in table:
        if len(row) == 7:
            order_id = row[0]
            customer_id = row[1]
            order_date = row[2]
            product = row[3]
            category = row[4]
            quantity = row[5]
            unit_price = row[6]
            date_format = '%Y-%m-%d'
            try:
                order_id = int(order_id)
                quantity = int(quantity)
                unit_price = float(unit_price)
                order_date = datetime.strptime(order_date,date_format)
                if quantity > 0 and unit_price > 0 and all(field.strip()for field in [customer_id,product,category]):
                    valid_rows.append({"order_id":order_id,"customer_id":customer_id,"order_date":order_date,"product":product,"category":category,"quantity":quantity,"unit_price":unit_price})
                else:
                    rejected_rows.append({"order_id":order_id,"customer_id":customer_id,"order_date":order_date,"product":product,"category":category,"quantity":quantity,"unit_price":unit_price})
                
            except ValueError as e:
                rejected_rows.append(row)
        else:
            rejected_rows.append(row)
    print("VALID ROWS",len(valid_rows))
    print("REJECTED ROWS",len(rejected_rows))