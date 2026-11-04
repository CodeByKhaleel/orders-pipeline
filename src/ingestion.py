import csv
from datetime import datetime
valid_rows = []
rejected_rows = []
seen_order_ids = set()
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
                errors = [
                    message
                    for condition, message in [
                        (quantity <= 0, "Invalid quantity"),
                        (unit_price <= 0, "Invalid unit price"),
                        (not customer_id.strip(), "Missing customer ID"),
                        (not product.strip(), "Missing product"),
                        (not category.strip(), "Missing category")
                    ]
                    if condition
                ]
                if errors:
                    rejected_rows.append({"row": row, "reason": errors})

                elif order_id in seen_order_ids:
                    rejected_rows.append({"row": row, "reason": ["Duplicate order ID"]})

                else:
                    seen_order_ids.add(order_id)
                    valid_rows.append({"order_id":order_id,"customer_id":customer_id,"order_date":order_date,"product":product,"category":category,"quantity":quantity,"unit_price":unit_price})
                
            except ValueError as e:
                rejected_rows.append({
                    "row":row,
                    "reason": [str(e)]
                })
        else:
            rejected_rows.append({
                "row": row,
                "reason": ["Invalid number of columns"]
            })
    print("VALID ROWS",len(valid_rows))
    print("REJECTED ROWS",len(rejected_rows))
    print(rejected_rows)