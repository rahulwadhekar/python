weights = [5, 10, 8]

total = sum(weights)

extra = max(0, total - 15)
fee = extra * 500

receipt = {
    "Weights": weights,
    "Total": total,
    "Fee": fee
}

print("Receipt:", receipt)