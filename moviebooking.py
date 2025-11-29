print("Welcome to Movie Ticket Booking!")

movie = input("Enter movie name: ")
tickets = int(input("How many tickets?: "))
price = 100  

total = tickets * price

print("\nTicket Summary")
print("Movie:", movie)
print("Tickets:", tickets)
print("Total Amount: Rs", total)
print("Booking Successful!")
