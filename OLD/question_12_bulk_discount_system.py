prices = [800, 1500, 6000, 2500, 7000]

discounted_prices = []
total_savings = 0

for price in prices:
    if price > 5000:
        discount = price * 0.20
    elif price > 1000:
        discount = price * 0.10
    else:
        discount = 0

    new_price = price - discount
    discounted_prices.append(new_price)
    total_savings += discount

print("Original Prices:", prices)
print("Discounted Prices:", discounted_prices)
print("Total Savings:", total_savings)