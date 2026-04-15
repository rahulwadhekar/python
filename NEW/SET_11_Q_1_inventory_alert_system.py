inventory = [
    {'product': 'Laptop', 'stock': 12, 'reorder_level': 15},
    {'product': 'Mouse', 'stock': 50, 'reorder_level': 20},
    {'product': 'Keyboard', 'stock': 10, 'reorder_level': 15}
]

restock = []

for item in inventory:
    if item['stock'] < item['reorder_level']:
        restock.append(item['product'])

print("Restock Alert:", restock)