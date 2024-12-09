from abc import ABC, abstractmethod

# Abstract Base Class Vehicle
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass

    def description(self):
        return f"This vehicle is a {self.brand}."

# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        return f"The {self.model} car's engine has started."

# Test Cases
car = Car("Toyota", "Corolla")
print(car.description())
print(car.start_engine())

# Attempting to create an object of Vehicle will raise an error
# vehicle = Vehicle("Generic")  # Uncommenting this line will raise a TypeError
