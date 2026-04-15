books = {}

while True:
    print("\n1. Add/Update Book")
    print("2. Issue Book")
    print("3. View Books")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        qty = int(input("Enter quantity: "))
        books[name] = books.get(name, 0) + qty

    elif choice == "2":
        name = input("Enter book to issue: ")
        if name in books and books[name] > 0:
            books[name] -= 1
            print("Book issued")
        else:
            print("Book not available")

    elif choice == "3":
        for b, q in books.items():
            print(b, ":", q)

    elif choice == "4":
        break