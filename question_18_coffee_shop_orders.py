orders = [('Latte', 'Medium'), ('Espresso', 'Large'), ('Mocha', 'Small')]

total = 0

for drink, size in orders:
    price = 100

    if size == 'Large':
        price += 50
    elif size == 'Small':
        price -= 20

    total += price
    print(drink, size, "₹", price)

print("Total ₹", total)