def calculate_square(a, b):
    return a**2 + b**2 + 2 * a * b

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
result = calculate_square(a, b)
print("The result of (a + b)^2 is:", result)
