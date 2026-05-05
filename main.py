koseats = 50
bookings = {}
booking_id = 1

while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")
           
        if choice == "1":
         print("Available seats:", seats)
        elif choice == "2":
           if seats > 0:
            name = input("Enter name: ")
            age = input("Enter age: ")

            bookings[booking_id] = {"name": name, "age": age}

            print("Booking successful!")
            print("Your booking ID is:", booking_id)

            booking_id += 1
            seats -= 1
           else:
             print("No seats available!")
        elif choice == "3":
        bid = int(input("Enter booking ID: "))
         if bid in bookings:
            print("Booking Details:", bookings[bid])
         else:
            print("Booking not found!")
        elif choice == "4":
        bid = int(input("Enter booking ID to cancel: "))
         if bid in bookings:
            del bookings[bid]
            seats += 1
            print("Booking cancelled successfully!")
         else:
            print("Invalid booking ID!") 
        elif choice == "5":
        print("Thank you for using the system!")
        break
         else:
           print("Invalid choice!")
