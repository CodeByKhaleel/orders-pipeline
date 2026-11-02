from datetime import datetime
import csv

valid_rows = []
rejected_rows = []
with open('data/orders.csv') as read_data:
    table_data = csv.reader(read_data)
    next(table_data)
    for row in table_data:
        order_id = int(row[0])
        customer_id = row[1]
        date_format = "%Y-%m-%d"
        try:
            order_date = datetime.strptime(row[2],date_format)
        except ValueError:
            reason = "Wrong date format"
            rejected_at = datetime.now()
            rejected_rows.append({"data":row,"reason":reason,"rejected_at":rejected_at,"source":"orders.csv"})
            continue
        product = row[3]
        category = row[4]
        quantity = int(row[5])
        unit_price = float(row[6])
        
        if quantity < 0:
            reason = "Invalid quantity"
            rejected_at = datetime.now()
            rejected_rows.append({"data":row,"reason":reason,"rejected_at":rejected_at,"source":"orders.csv"})
            continue
        if unit_price < 0:
            reason = "Invalid unit_price"
            rejected_at = datetime.now()
            rejected_rows.append({"data":row,"reason":reason,"rejected_at":rejected_at,"source":"orders.csv"})
            continue
        total_amount = quantity * unit_price
        valid_rows.append({"order_id":order_id,"customer_id":customer_id,"order_date":order_date,"product":product,"category":category,"quantity":quantity,"unit_price":unit_price,"total_amount":total_amount})
    print(valid_rows)
