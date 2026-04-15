expenses = {}

while True:
    category = input("Enter category (or DONE to finish): ")

    if category.upper() == "DONE":
        break

    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

print("\nExpense Breakdown:")
for category, total in expenses.items():
    print(f"{category}: ₹{total}")