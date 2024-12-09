# Task 2.1 - Basic Vehicle Class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")

# Inheritance
class Car(Vehicle):
    pass

class MotorCycle(Vehicle):
    pass

# Create objects of Car and MotorCycle
car = Car()
motorcycle = MotorCycle()

car.start()
car.stop()

motorcycle.start()
motorcycle.stop()
