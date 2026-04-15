flights = {
    "F101": [1000, 2000, 2500],
    "F102": [1500, 1000],
    "F103": [3000, 2500]
}

cleared = []
grounded = []

for f, weights in flights.items():
    total = sum(weights)

    if total > 5000:
        grounded.append(f)
    else:
        cleared.append(f)

print("Cleared Flights:", cleared)
print("Grounded Flights:", grounded)