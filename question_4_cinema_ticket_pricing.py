ages = [8, 15, 65, 30, 10, 70]
base_price = 200

final_prices = []
total_bill = 0

for age in ages:
    if age < 12:
        price = base_price * 0.5
    elif age > 60:
        price = base_price * 0.7
    else:
        price = base_price

    final_prices.append(price)
    total_bill += price

print("Individual ticket prices:", final_prices)
print("Total group bill:", total_bill)