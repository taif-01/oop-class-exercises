# Base Class: Vehicle
class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicle_info(self):
        print(f"Color: {self.color}")


# Derived Class: Taxi
class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    # Getters
    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def get_variant(self):
        return self.__variant

    # Setters
    def set_model(self, model):
        self.__model = model

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_variant(self, variant):
        self.__variant = variant

    # Overriding vehicle_info
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Model: {self.__model}, Capacity: {self.__capacity}, Variant: {self.__variant}")


# Example Usage
t1 = Taxi("Yellow", "Toyota Prius", 4, "Hybrid")
t2 = Taxi("White", "Honda City", 4, "Sedan")

t1.vehicle_info()
t2.vehicle_info()

# Modifying details using setters
t1.set_model("Toyota Corolla")
t1.set_variant("Petrol")
print("\nAfter modifications:")
t1.vehicle_info()
