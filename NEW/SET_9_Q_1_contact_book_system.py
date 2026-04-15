contacts = {}

while True:
    print("\n1.Add 2.Search 3.Delete 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        if name in contacts:
            print("Already exists")
        else:
            contacts[name] = input("Phone: ")

    elif ch == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == "3":
        name = input("Delete name: ")
        contacts.pop(name, None)

    elif ch == "4":
        break