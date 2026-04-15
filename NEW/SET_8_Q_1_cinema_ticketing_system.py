seats = [["O" for _ in range(5)] for _ in range(5)]

while True:
    print("\nSeating:")
    for row in seats:
        print(" ".join(row))

    r = int(input("Enter row (0-4): "))
    c = int(input("Enter col (0-4): "))

    if seats[r][c] == "O":
        seats[r][c] = "X"
        print("Seat booked")
    else:
        print("Seat already taken")

    cont = input("Continue? (y/n): ")
    if cont.lower() != "y":
        break