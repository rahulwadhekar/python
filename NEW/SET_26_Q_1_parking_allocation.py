parking = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]

i = 0
assigned = False

while i < len(parking):
    if parking[i] == 0:
        parking[i] = 1
        print("Spot assigned at:", i)
        assigned = True
        break
    i += 1

if not assigned:
    print("Parking Full")