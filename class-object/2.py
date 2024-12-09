# Base Class: Shape
class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"Shape: {self.name}")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")


# Example Usage
rectangle = Rectangle(5, 3)
rectangle.display_info()
