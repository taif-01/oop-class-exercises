arr = [10, 5, 15, 20]

try:
    # Taking input for divisor
    divisor = int(input("Enter divisor: "))

    # Performing division
    for i in range(len(arr)):
        result = arr[i] / divisor
        print(f"arr[{i}] / {divisor} = {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")
except IndexError:
    print("Error: Index out of range.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division performed successfully!")
finally:
    print("Execution completed.")
