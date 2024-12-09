# Initial tuple
a = (1, 3, 5, 7, 4)

# a) Find the sum of all odd numbers in a
sum_of_odd_numbers = sum(num for num in a if num % 2 != 0)
print("Sum of all odd numbers in a:", sum_of_odd_numbers)

# b) Find the sum of all odd index elements in a
sum_of_odd_index_elements = sum(a[i] for i in range(len(a)) if i % 2 != 0)
print("Sum of all odd index elements in a:", sum_of_odd_index_elements)

# c) Count the number of odd and even numbers separately
odd_count = sum(1 for num in a if num % 2 != 0)
even_count = len(a) - odd_count
print("Odd numbers count:", odd_count)
print("Even numbers count:", even_count)

# d) Extend the tuple with (2, 4, 6)
extended_tuple = a + (2, 4, 6)
print("Extended tuple:", extended_tuple)

# e) Add a new item `(400)` at index 2
a_list = list(a)
a_list.insert(2, 400)
a_with_new_item = tuple(a_list)
print("Tuple after adding 400 at index 2:", a_with_new_item)

# f) Remove the last element
a_list.pop()
a_without_last = tuple(a_list)
print("Tuple after removing the last element:", a_without_last)

# g) Perform slicing [-4:-1]
sliced_tuple = a[-4:-1]
print("Sliced tuple ([-4:-1]):", sliced_tuple)

# h) Print the tuple using a loop and skip (continue) if the element at index 2 is 5
print("Printing tuple with skip logic:")
for idx, value in enumerate(a):
    if idx == 2 and value == 5:
        continue
    print(value)
