class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
        self.fare = 500
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self, seats_to_book):
        if seats_to_book <= self.available_seats():
            self.booked_seats += seats_to_book
            return True
        else:
            return False

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
    def __init__(self, username, password ):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        return self.username == username and self.password == password

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin("admin", "1234")
    
    def add_bus(self,number, route, seats):
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print(f"Bus {number} added successfully.")
    
    def book_ticket(self, bus_number, name, phone):
        if len(bus_number) == 0:
            print("\nInvalid bus number.\n")
            return
        if not self.buses:
            print("\nNo buses available.\n")
            return
        bus = None
        for b in self.buses:
            if b.number == bus_number:
                bus = b
                break

        if bus:
            if bus.available_seats() <= 0:
                print("\nNo available seats.\n")
                return
            if bus.book_seat(1):
                passenger = Passenger(name, phone, bus)
                self.passengers.append(passenger)
                print(f"\n Ticket booked successfully for {name} on bus {bus_number}. Fare: {bus.fare} \n")
            else:
                print("\n No available seats. \n")
        else:
            print("\nBus not found.\n")

    def show_buses(self):
        if not self.buses:
            print("No buses available.")
            return
        print("\n-----------All BUsses------------")
        for bus in self.buses:
            print(f"Bus Number: {bus.number}, Route: {bus.route}, Available Seats: {bus.available_seats()} Fare: {bus.fare}")


def main():
    greenline_bus_system = BusSystem()
    while True:
        print("Welcome to GreenLine Bus Management System")
        # 1. Admin Login 2. Book Ticket 3. View Buses 4. Exit
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if greenline_bus_system.admin.login(username, password):
                # 1. Add Bus 2. View All Buses 3. Logout
                print("\nAdmin logged in successfully.")
                while True:
                    print("1. Add Bus")
                    print("2. View All Buses")
                    print("3. Logout")
                    admin_choice = input("Enter your choice: ")
                    if admin_choice == '1':
                        bus_number = input("Enter bus number: ")
                        route = input("Enter bus route: ")
                        seats_input = input("Enter Total Seats: ").strip()
                        if not seats_input:
                            print("\nSeats cannot be empty!\n")
                            continue
                        try:
                            seats_int = int(seats_input)
                        except ValueError:
                            print("\nSeats must be a valid integer!\n")
                            continue
                        if len(bus_number) == 0 or len(route) == 0 or seats_int <= 0:
                            print("\nInvalid bus details.\n")
                        else:   
                            greenline_bus_system.add_bus(bus_number, route, seats_int)
                    elif admin_choice == '2':
                        greenline_bus_system.show_buses()
                    elif admin_choice == '3':
                        print("Admin logged out.")
                        break
                    else:
                        print("\nInvalid choice.\n")

            else:
                print("\nInvalid admin credentials.\n")

        
        elif choice == '2':
            bus_number = input("Enter bus number to book ticket: ")
            name = input("Enter passenger name: ")
            phone = input("Enter passenger phone: ")
            if len(bus_number) == 0 or len(name) == 0 or len(phone) == 0:
                print("\nInvalid booking details.\n")
            else:
                greenline_bus_system.book_ticket(bus_number, name, phone)

        elif choice == '3':
            greenline_bus_system.show_buses()
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice.\n")
main()