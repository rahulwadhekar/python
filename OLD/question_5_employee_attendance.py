attendance = [
    ("E101", 18),
    ("E102", 30),
    ("E103", 25),
    ("E104", 15),
    ("E105", 30)
]

warning_list = []
bonus_list = []

for emp_id, days in attendance:
    if days < 20:
        warning_list.append(emp_id)
    elif days == 30:
        bonus_list.append(emp_id)

print("Warning List:", warning_list)
print("Bonus List:", bonus_list)