#1
a = [1, 3, 5, 7, 4]
# Access elements
element_neg2 = a[-2]
element_2 = a[2]

length = len(a)
list_type = type(a)

print("a[-2]:", element_neg2)
print("a[2]:", element_2)
print("Length of the list:", length)
print("Type of the list:", list_type)


#2
a[-3] = 50
sliced = a[2:4]

print("Updated list:", a)
print("Sliced list (a[2:4]):", sliced)


#3
a.append(100)
a.insert(2, 200)

print("List after adding 100 and 200:", a)

#4
a.pop()
del a[1]
print("List after removals:", a)

#5
new_list = [2, 4, 6]
a.extend(new_list)
print("List after joining:", a)

#6
# Copy list
b = a.copy()
print("Copied list b:", b)

#7
# Sort b
b.sort()
print("Sorted list b:", b)

#8
for element in a:
    print(element)
    if element == 5:
        break

#9
largest = max(a)
print("The largest number in the list:", largest)

