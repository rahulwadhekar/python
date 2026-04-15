feedback_list = [
    {'rating': 4, 'comment': 'Good food'},
    {'rating': 2, 'comment': 'Slow service'},
    {'rating': 5, 'comment': 'Excellent experience'},
    {'rating': 1, 'comment': 'Very bad taste'},
    {'rating': 3, 'comment': 'Average ambiance'}
]

total_rating = 0
count = 0
complaints = []

for feedback in feedback_list:
    total_rating += feedback['rating']
    count += 1

    if feedback['rating'] <= 2:
        complaints.append(feedback['comment'])

average_rating = total_rating / count

print("Average Rating:", average_rating)
print("Complaints:", complaints)