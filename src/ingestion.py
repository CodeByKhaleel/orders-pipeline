import csv

with open('../data/raw/orders.csv') as read_data:
    table = csv.reader(read_data)
    next(table)
    for row in table:
        order_id = row[0]
        quantity = row[5]
        unit_price = row[6]
        print(f"Raw order_id: {row[0]}")
        print(f"Raw quantity: {row[5]}")
        print(f"Raw unit_price: {row[6]}")
        order_id = int(order_id)
        quantity = int(quantity)
        unit_price = float(unit_price)
        print(f"order_id:{order_id},quantity:{quantity},unit_price:{unit_price}")