from abc import ABC, abstractmethod
class Device(ABC):
    def __init__(self, name,model,price):
        self.name = name
        self.model = model
        self.price = price
    @abstractmethod
    def getPrice(self):
        return self.price

class Phone(Device):
    def __init__(self, name, model, price):
        super().__init__(name, model, price)
    def getPrice(self):
        return self.price

newPhone = Phone("Samsung","Galaxy S21",799.99)
print(f"Device Name: {newPhone.name}")
print(f"Device Model: {newPhone.model}")
print(f"Device Price: {newPhone.getPrice()}")
    