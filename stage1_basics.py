# The Inventory List
ivnventory = [
    {"name":"Laptop", "price": 45000, "in_stock": True}, 
    {"name":"Mouse", "price": 1200, "in_stock": True},
    {"name":"Keyboard", "price":2500, "in_stock": False}
]

# Adding a new item
ivnventory.append({"name":"HDMI Cable", "price":500, "in_stock":True})

print("---Updating Prices---")

#The Loop to update prices
for item in ivnventory:
    if item["price"] > 10000:
        # Apply 10% discount
        item["price"] = item["price"] *0.9

    elif item["price"] < 2000:
        # Increase Rs 500 due to logistics cost
        item["price"] = item["price"] + 500

    else:
        # 'pass' just tells python to do nothing and move to the next line
        pass

    print(f"product: {item['name']} | New Price: {item['price']}")
