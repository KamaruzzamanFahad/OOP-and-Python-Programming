from menu import Menu

class Resturant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def view_employees(self):
        print("Employee List:")
        for em in self.employees:
            print(em.name, em.email, em.phone, em.address, em.age, em.designation, em.salary)
