temps = [10, -2, 36, 40, 15, 5, 38]

total = 0
freezing = 0
heatwave = 0

for t in temps:
    total += t
    if t < 0:
        freezing += 1
    elif t > 35:
        heatwave += 1

average = total / len(temps)

report = {
    "Average": average,
    "Freezing Days": freezing,
    "Heatwave Days": heatwave
}

print("Weather Report:", report)