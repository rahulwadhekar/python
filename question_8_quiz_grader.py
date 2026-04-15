correct_answers = {
    'Q1': 'A',
    'Q2': 'C',
    'Q3': 'B',
    'Q4': 'D'
}

student_answers = {
    'Q1': 'A',
    'Q2': 'B',
    'Q3': 'B',
    'Q4': 'A'
}

score = 0

for question in correct_answers:
    if question in student_answers:
        if student_answers[question] == correct_answers[question]:
            score += 2
        else:
            score -= 1

print("Final Score:", score)