temps = [12, 18, 32, 35, 36, 37, 25]

cold, hot, moderate = [], [], []
streak = 0
warning = False

for t in temps:
    if t < 15:
        cold.append(t)
        streak = 0
    elif t > 30:
        hot.append(t)
        streak += 1
        if streak > 3:
            warning = True
    else:
        moderate.append(t)
        streak = 0

print("Cold:", cold)
print("Moderate:", moderate)
print("Hot:", hot)

if warning:
    print("Warning: >3 consecutive hot days")