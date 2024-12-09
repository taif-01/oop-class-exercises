# Given dictionary:
employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "parmanent": True,
    "Salary": 30000,
    100: (1, 2, 3),
    4.5: {5, 6, True, 7, 1}
}

#1 Print length, type, and the dictionary
print(len(employee))
print(type(employee))
print(employee)

#2: Access the key "type" -> "developer"
print(employee["type"]["developer"])

# 3: Change the value of "parmanent" to False
employee["parmanent"] = False
print(employee["parmanent"])

#4: Add a new key "gender" with value "male"
employee["gender"] = "male"
print(employee)

# 5: Remove the "age" key
employee.pop("age", None)
print(employee)

#6: Use keys(), values(), and items()
print(employee.keys())
print(employee.values())
print(employee.items())

#7: Iterate the dictionary using a loop
for key, value in employee.items():
    print(f"{key}: {value}")
