available_seats = set(range(1, 21))

while True:
    print("Available seats:", available_seats)

    seat = int(input("Enter seat number to book (0 to exit): "))

    if seat == 0:
        print("Booking system terminated.")
        break

    if seat in available_seats:
        available_seats.remove(seat)
        print("Seat Booked")
    else:
        print("Seat Unavailable")

    if not available_seats:
        print("All seats are booked.")
        break