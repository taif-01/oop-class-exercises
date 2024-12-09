class Department:
    def display_name(self):
        print("Department: Generic Department")

class Teacher(Department):
    def display_name(self):
        print("Department: Teaching Staff")

class Author(Department):
    def display_name(self):
        print("Department: Writing Team")

# Demonstrating runtime polymorphism
def show_department(department):
    department.display_name()

teacher = Teacher()
author = Author()

show_department(teacher)  # Output: Department: Teaching Staff
show_department(author)   # Output: Department: Writing Team
