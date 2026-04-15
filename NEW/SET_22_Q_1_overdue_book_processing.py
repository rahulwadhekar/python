borrowed_days = {
    "S101": 10,
    "S102": 18,
    "S103": 25,
    "S104": 14
}

fines = []

for sid, days in borrowed_days.items():
    if days > 14:
        fine = (days - 14) * 10
        fines.append((sid, fine))

print("Fines:", fines)