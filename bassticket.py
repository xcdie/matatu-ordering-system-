class seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def __str__(self):
        status = 'Booked' if self.is_booked else 'Available'
        return f"Seat {self.seat_number}: {status}"
            
class matatu:
    def __init__(self, sacco_name, route, total_seats, fare):
        self.sacco_name = sacco_name
        self.route = route
        self.total_seats = total_seats
        self.fare = fare
        self.seats = [seat(i) for i in range(1, total_seats + 1)]

    def display_seats(self):
        for s in self.seats:
            print(s)

  
    def book_seat(self, seat_number):
        if 1 <= seat_number <= self.total_seats:
            selected_seat = self.seats[seat_number - 1]
            if not selected_seat.is_booked:
                selected_seat.is_booked = True
                print(f"Seat {seat_number} has been booked successfully.")
            else:
                print(f"Seat {seat_number} is already booked.")
        else:
            print(" Invalid seat number.")

class matatu_booking_system:
    def __init__(self):
        self.matatus = [
            matatu("Super Metro", "NAIROBI - THIKA", 14, 100),
            matatu("Zigi", "ODEON - KAHAWA WEST", 12, 80),
            matatu("Safari", "NAIROBI - KISUMU", 16, 150),
            matatu("Mash Poa", "NAIROBI - MOMBASA", 20, 200),
            matatu("2NK", "NAIROBI - NYERI", 18, 120)
        ]

    def show_routes(self):
        print("\nAvailable Matatu Routes:")
        for index, m in enumerate(self.matatus, start=1):
            print(f"{index}. Sacco: {m.sacco_name} | Route: {m.route} | Fare: KES {m.fare}")

    def run(self):
        print(" Welcome to the Matatu Booking System ")

        while True:
            self.show_routes()
            choice = input("\nEnter the number of the matatu you want to book (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Asante sana for using the matatu booking system. Safiri salama!")
                break
            try:
                choice_idx = int(choice)
                if 1 <= choice_idx <= len(self.matatus):
                    selected_matatu = self.matatus[choice_idx - 1]
                    
                    print(f"\n--- Seat Layout for {selected_matatu.sacco_name} ---")
                    selected_matatu.display_seats()
                    
                    seat_choice = int(input(f"\nEnter the seat number to book (1-{selected_matatu.total_seats}): "))
                    selected_matatu.book_seat(seat_choice)
                else:
                    print(" Invalid choice. Please select a valid matatu number.")
            except ValueError:
                print("Invalid input. Please enter a valid number or 'q'.")
