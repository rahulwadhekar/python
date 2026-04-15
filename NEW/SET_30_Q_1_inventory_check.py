expected = (50, 30, 20, 100)
actual = (45, 30, 18, 90)

loss = {}

for i in range(len(expected)):
    if actual[i] < expected[i]:
        loss[i] = expected[i] - actual[i]

print("Loss Report:", loss)