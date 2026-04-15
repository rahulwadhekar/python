data = {}

while True:
    name = input("Enter name (or EXIT): ")
    if name == "EXIT":
        break

    exercise = input("Enter exercise: ")

    if name in data:
        data[name].add(exercise)
    else:
        data[name] = {exercise}

for user, ex in data.items():
    print(user, ":", len(ex), "exercises")