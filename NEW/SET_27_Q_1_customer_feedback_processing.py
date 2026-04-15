feedback = [
    {'rating': 4, 'comment': 'Good'},
    {'rating': 2, 'comment': 'Bad service'},
    {'rating': 1, 'comment': 'Very poor'}
]

total = 0
count = 0
complaints = []

for f in feedback:
    total += f['rating']
    count += 1

    if f['rating'] <= 2:
        complaints.append(f['comment'])

avg = total / count

print("Average Rating:", avg)
print("Complaints:", complaints)