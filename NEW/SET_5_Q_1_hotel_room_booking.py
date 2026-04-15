rooms = {101: "Available", 102: "Booked", 103: "Available"}

while True:
    print("\n1.Book Room  2.Checkout  3.View  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        r = int(input("Enter room: "))
        if rooms.get(r) == "Available":
            rooms[r] = "Booked"
            print("Room booked")
        else:
            print("Already booked")

    elif choice == "2":
        r = int(input("Enter room: "))
        if rooms.get(r) == "Booked":
            rooms[r] = "Available"
            print("Checked out")
        else:
            print("Room already free")

    elif choice == "3":
        print(rooms)

    elif choice == "4":
        break