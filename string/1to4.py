# Initial strings
a = "hello"
b = "b2b2b2    "
c = " 3g3g    "

# Question 1: Declare a new variable d and concatenate a, b, and c
d = a + b + c
print(d)

#2: Find the length of d and print d[:-1]
print(len(d))
print(d[:-1])

#3: Check if "a2" is present in d
print("a2" in d)

#4: Perform  many string operations:
print(d.upper())
print(d.lower())
print(d.title())
print(d.strip()) 
print(d.isdigit())
print(d.find("3g"))
print(d.capitalize())
print(d.isalnum())   # Check if d is alphanumeric
print(d.count("b2"))
print(d.split())   
print(d.swapcase()) 
print(d.lstrip()) 
print(d.replace("hello", "python"))
