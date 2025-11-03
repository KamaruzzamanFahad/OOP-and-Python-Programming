from itertools import product


class Shoping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
    def remove_from_cart(self, item):
        self.cart = [product for product in self.cart if product['item'] != item]
    def view_cart(self):
        return self.cart
    def total_price(self):
        total = sum(product['price'] * product['quantity'] for product in self.cart)
        return total
    def checkout(self, payment):
        total = self.total_price()
        if payment >= total:
            change = payment - total
            self.cart = []  # Empty the cart after checkout
            return f"Payment successful! Change: ${change:.2f}"
        else:
            return "Insufficient payment. Please add more funds."
shop = Shoping("My Shop")
shop.add_to_cart("Apple", 1.5, 4)
shop.add_to_cart("Banana", 0.75, 6)
print("Cart Contents:", shop.view_cart())
print("Total Price: $", shop.total_price())
print(shop.checkout(20))
print("Cart Contents after checkout:", shop.view_cart())