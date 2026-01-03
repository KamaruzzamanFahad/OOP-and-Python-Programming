from abc import ABC, abstractmethod
from ride import Ride, RideRequest, RideMatching

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount

    def display_profile(self):
        print(f"Rider Name: {self.name} and Email: {self.email}")
    
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount less then zero")
    def update_location(self, current_location):
        self.current_location = current_location
    
    def request_ride(self, ridesharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ridesharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("Ride requested successfully.")

    def show_current_ride(self):
        print("Current Ride Details:")
        print("Rider:", self.name)
        print("From:", self.current_ride.start_location)
        print("To:", self.current_ride.end_location)
        print("Vehicle Type:", self.current_ride.vehicle.vehicle_type)
        print("Estimated Fare:", self.current_ride.estimated_fare)
        print("Driver:", self.current_ride.driver.name if self.current_ride.driver else "No driver assigned")

    
    

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email,nid)
        self.current_location = current_location
        self.wallet = 0
    
    def display_profile(self):
        print(f"Driver Name: {self.name} and Email: {self.email}")

    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)
    
    def rech_destination(self, ride):
        ride.end_ride()