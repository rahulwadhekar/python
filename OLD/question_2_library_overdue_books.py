borrowed_days = {
    "S101": 10,
    "S102": 18,
    "S103": 25,
    "S104": 14,
    "S105": 20
}

fines = []

for student_id, days in borrowed_days.items():
    if days > 14:
        extra_days = days - 14
        fine = extra_days * 10
        fines.append((student_id, fine))

print("Students with fines:", fines)