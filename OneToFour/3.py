def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input and test
n = int(input("Enter a number to find its factorial: "))
result = factorial(n)
print(f"The factorial of {n} is:", result)
