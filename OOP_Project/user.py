from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

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

class Resturant:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def view_employees(self):
        print("Employee List:")
        for em in self.employees:
            print(em.name, em.email, em.phone, em.address, em.age, em.designation, em.salary)

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if(item):
            self.items.remove(item)
        else:
            print(f"item not found {item_name}")
