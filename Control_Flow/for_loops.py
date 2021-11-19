

menu = [
    {"food": "pizza", "price" : 13.00},
    {"food": "burger", "price" : 9.50},
    {"food": "chips", "price" : 2.60}
]

# calc total cost for 1 of eah item in the menu

total = 0
for d in menu:
    total += d["price"]
print(f"Total is £{total:.2f}")