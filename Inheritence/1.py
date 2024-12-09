# Base Class: Person
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")


# Derived Class: Student
class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduation_year}")


# Derived Class: CurrentStudent (inherits from Student)
class CurrentStudent(Student):
    def __init__(self, first_name, last_name, graduation_year, current_semester):
        super().__init__(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        super().display()
        print(f"Current Semester: {self.current_semester}")


# Derived Class: Alumni (inherits from Student)
class Alumni(Student):
    def __init__(self, first_name, last_name, graduation_year, passing_year):
        super().__init__(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        super().display()
        print(f"Passing Year: {self.passing_year}")


# Derived Class: Teacher
class Teacher(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")


# Derived Class: Admin
class Admin(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")


# Derived Class: Employee
class Employee(Person):
    def __init__(self, first_name, last_name, emp_id):
        super().__init__(first_name, last_name)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")


# Example Usage
person = Person("John", "Doe")
student = Student("Alice", "Smith", 2025)
current_student = CurrentStudent("Bob", "Brown", 2025, "Semester 3")
alumni = Alumni("Charlie", "Davis", 2020, 2022)
teacher = Teacher("Dr. Emily", "White", 2010)
admin = Admin("Mr. James", "Clark", 2015)
employee = Employee("Sophia", "Green", "EMP123")

print("\n--- Examples ---")
person.display()
student.display()
current_student.display()
alumni.display()
teacher.display()
admin.display()
employee.display()
