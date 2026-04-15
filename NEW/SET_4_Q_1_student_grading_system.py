students = [
    {'student_id': 101, 'marks': 85},
    {'student_id': 102, 'marks': 65},
    {'student_id': 103, 'marks': 50},
    {'student_id': 104, 'marks': 90}
]

grades = {}

for s in students:
    sid = s['student_id']
    marks = s['marks']

    if marks > 80:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    else:
        grade = 'C'

    if grade not in grades:
        grades[grade] = []
    grades[grade].append(sid)

print("Grade Distribution:", grades)