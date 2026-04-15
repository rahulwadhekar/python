attendance = [
    ("E101", 18),
    ("E102", 30),
    ("E103", 25),
    ("E104", 15)
]

warning = []
bonus = []

for emp, days in attendance:
    if days < 20:
        warning.append(emp)
    elif days == 30:
        bonus.append(emp)

print("Warning List:", warning)
print("Bonus List:", bonus)