from abc import ABC
from tkinter import NO
from typing import Self
from order import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()
    
    def view_menu(self, resturant):
        resturant.menu.show_menu_item()
    
    def add_to_cart(self, resturant, item_name, quantity):
        item = resturant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f"Item quantity exceeded {item.quantity} available")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print(f"item {item.name} added to cart")
        else:
            print("item not found")
    
    def view_cart(self, resturant):
        print("*****Cart*****")
        print("Name\tPrice\tQuantity")

        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
            print(f"Total Price: {self.cart.total_price}")

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        
    def add_employee(self, resturant, employee):
        resturant.add_employee(employee)
        print(f"Employee {employee.name} added successfully.")

    def view_employees(self, resturant):
        resturant.view_employees()

    def add_menu_item(self, resturant, item):
        resturant.menu.add_menu_item(item)

    def remove_menu_item(self, resturant, item):
        resturant.menu.remove_item(item)


