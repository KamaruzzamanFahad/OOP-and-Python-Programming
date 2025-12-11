from user import User, Customer, Employee, Admin
from resturant import Resturant
from menu import Menu
from fooditem import FoodItem
from orders import Order


mamar_resturant = Resturant("mamar resturant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add item to Cart")
        print("3. View Cart")
        print("4. Paybill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(mamar_resturant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            customer.add_to_cart(mamar_resturant, item_name, quantity)
        elif choice == 3:
            customer.view_cart(mamar_resturant)
        elif choice == 4:
            customer.Paybill()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome Admin {admin.name}")
        print("1. Add Item")
        print("2. Add Employees")
        print("3. view Employees")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))

            food_item = FoodItem(name=item_name, price=item_price, quantity=item_quantity)
            admin.add_menu_item(mamar_resturant, food_item)

        elif choice == 2:
            name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            phone = input("Enter employee phone: ")
            address = input("Enter employee address: ")
            age = int(input("Enter employee age: "))
            designation = input("Enter employee designation: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name=name, email=email, phone=phone, address=address, age=age, designation=designation, salary=salary)
            admin.add_employee(mamar_resturant, employee)
        
        elif choice == 3:
            admin.view_employees(mamar_resturant)
        elif choice == 4:
            admin.view_menu(mamar_resturant)
        elif choice == 5:
            item_name = input("Enter item name to delete: ")
            admin.remove_menu_item(mamar_resturant, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")