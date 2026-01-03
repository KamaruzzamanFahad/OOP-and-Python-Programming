from datetime import datetime
from vehicle import Car, Bike

class RideSharing():
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    def add_rider(self, rider):
        self.riders.append(rider)
    def add_driver(self, driver):
        self.drivers.append(driver)

    def __str__(self):
        return f"RideSharing Company: {self.company_name}, Riders: {len(self.riders)}, Drivers: {len(self.drivers)}"

class Ride:
    def __init__(self, start_location, end_location, vehicle) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle
    
    def set_driver(self, driver):
        self.driver = driver
    def start_ride(self):
        self.start_time = datetime.now()
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    
    def calculate_fare(self,  vehicle):
        distance = 10
        fare_par_km ={
            'car': 40,
            'bike': 50,
            'cng': 60
        }
        return distance * fare_par_km.get(vehicle)
    
    def __repr__(self):
        return f"Ride from {self.start_location} to {self.end_location} driven by {self.driver.name if self.driver else 'No driver assigned'}"
        
class RideRequest:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_request, vehicle_type):
            if len(self.available_drivers) > 0:
                print("Looking for drivers...")
                driver = self.available_drivers[0]
                
                if vehicle_type == 'car':
                    vehicle = Car('car', 'XYZ-1234', 40)
                elif vehicle_type == 'bike':
                    vehicle = Bike('bike', 'ABC-5678', 50)

                ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
                driver.accept_ride(ride)
                return ride
            