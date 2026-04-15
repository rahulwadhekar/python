expected_counts = (50, 30, 20, 100, 60)
physical_counts = (45, 30, 18, 90, 60)

loss_report = {}

for i in range(len(expected_counts)):
    if physical_counts[i] < expected_counts[i]:
        loss_report[i] = expected_counts[i] - physical_counts[i]

print("Loss Report:", loss_report)