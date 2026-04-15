records = [
    ("Coffee", 100, 10),
    ("Tea", 50, 20),
    ("Cake", 200, 5)
]

total = 0
best_item = ""
max_qty = 0
max_revenue = 0
high_item = ""

for name, price, qty in records:
    if qty <= 0:
        continue

    revenue = price * qty
    total += revenue

    if qty > max_qty:
        max_qty = qty
        best_item = name

    if revenue > max_revenue:
        max_revenue = revenue
        high_item = name

print("Total Revenue:", total)
print("Best Selling:", best_item)
print("Highest Revenue:", high_item)