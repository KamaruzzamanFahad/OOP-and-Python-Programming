class Device:
    def __init__(self, name,mode,price):
        self.name = name
        self.mode = mode
        self.__price = price
    def getPrice(self):
        return self.__price

phone = Device("samsung","galaxy",999.99)
print(f"Device Name: {phone.name}")
print(f"Device Mode: {phone.mode}")
# print(f"Device Price: {phone.__price}")  # Accessing the private attribute using name mangling
print(f"Device Price: {phone.getPrice()}")  # Accessing the private attribute using a public method