# Lambda function
square_formula = lambda a, b: a**2 + b**2 + 2 * a * b

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
result = square_formula(a, b)
print("The result of (a + b)^2 using lambda is:", result)
