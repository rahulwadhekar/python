cart = [
    {'item': 'Apple', 'qty': 5, 'price': 20},
    {'item': 'Milk', 'qty': 2, 'price': 50}
]

subtotal = 0

for c in cart:
    subtotal += c['qty'] * c['price']

if subtotal > 1000:
    discount = subtotal * 0.10
elif subtotal > 500:
    discount = subtotal * 0.05
else:
    discount = 0

total = subtotal - discount

bill = (cart, total)

print("Bill:", bill)