from abc import ABC, abstractmethod
from re import L

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
    
    def request_ride(self, ridesharing, destination):
        pass

    def current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email,nid)
        self.current_location = current_location
        self.wallet = 0
    
    def display_profile(self):
        print(f"Driver Name: {self.name} and Email: {self.email}")
    
    def accept_ride(slef, ride):
        pass