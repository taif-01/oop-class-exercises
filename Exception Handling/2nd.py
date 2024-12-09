# Custom Exception
class SalaryNotInRange(Exception):
    pass

# Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        try:
            if self.salary < 10000 or self.salary > 50000:
                raise SalaryNotInRange(f"Salary {self.salary} is not in the valid range (10,000-50,000).")
            print(f"Employee: {self.name}, Salary: {self.salary}")
        except SalaryNotInRange as e:
            print(f"Exception: {e}")

# Example Usage
employee_name = input("Enter employee name: ")
employee_salary = int(input("Enter employee salary: "))
employee = Employee(employee_name, employee_salary)
employee.display_salary()
