properties = [
    (1, 500000, "Pune", 2),
    (2, 700000, "Mumbai", 3),
    (3, 400000, "Pune", 1)
]

budget = int(input("Enter budget: "))
city = input("Enter city: ")

result = set()

for pid, price, c, bed in properties:
    if price <= budget and c == city:
        result.add(pid)

print("Matching Properties:", result)