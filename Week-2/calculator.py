class Calculator:
    brand = "PyCalc"
    def add(self, a,b):
        return a + b
    def subtract(self, a,b):
        return a - b
    def multiply(self, a,b):
        return a * b
    def divide(self, a,b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

print(Calculator.brand)
print("Addition:", Calculator().add(10, 5))
print("Subtraction:", Calculator().subtract(10, 5))
print("Multiplication:", Calculator().multiply(10, 5))
print("Division:", Calculator().divide(10, 5))