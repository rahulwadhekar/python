passengers = {
    "Alice": 2,
    "Bob": 1,
    "Charlie": 3,
    "David": 1,
    "Eva": 2,
    "Frank": 3
}

for zone in [1, 2, 3]:
    print(f"\nNow boarding Zone {zone}:")

    for name, z in passengers.items():
        if z == zone:
            print(f"Passenger {name}, please board.")