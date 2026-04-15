durations = [25, 45, 70, 30, 55, 20, 80]
classification = {}

for i in range(len(durations)):
    if durations[i] < 30:
        classification[i] = 'Fast'
    elif 30 <= durations[i] <= 60:
        classification[i] = 'Normal'
    else:
        classification[i] = 'Extended'

print(classification)