menu = ("Burger", "Pizza", "Pasta")
order = ["Burger", "Fries", "Pizza"]

valid = []
invalid = []

for item in order:
    if item in menu:
        valid.append(item)
    else:
        invalid.append(item)

print("Valid Orders:", valid)
print("Invalid Orders:", invalid)