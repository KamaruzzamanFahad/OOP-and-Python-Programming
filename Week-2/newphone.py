class Phone:
    brand = "samsung"

    def __init__(self, model, year, color, price):
        self.model= model
        self.year = year
        self.color = color
        self.price = price

myphone = Phone('galaxy', 2020, 'black', 999.99)
josimphone = Phone('note', 2021, 'white', 1099.99)
akterphone = Phone('a-series', 2019, 'blue', 499.99)
print(f"Phone Brand: {myphone.brand} Model: {myphone.model} Year: {myphone.year} Color: {myphone.color} Price: ${myphone.price}")
print(f"Phone Brand: {josimphone.brand} Model: {josimphone.model} Year: {josimphone.year} Color: {josimphone.color} Price: ${josimphone.price}")
print(f"Phone Brand: {akterphone.brand} Model: {akterphone.model} Year: {akterphone.year} Color: {akterphone.color} Price: ${akterphone.price}")