# Base Class: Product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Name: {self.name}, Price: {self.price}")


# Derived Class: ElectronicProduct
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty} years")


# Example Usage
product = Product("Generic Item", 50)
product.display_detail()

electronic = ElectronicProduct("Smartphone", 699, 2)
electronic.display_detail()
