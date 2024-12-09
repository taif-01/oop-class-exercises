a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

print(a, b)

print(len(a), type(a))
print(len(b), type(b))

a.add(10)
print(a)

a.discard(8)
print(a)

union_set = a.union(b)
print(union_set)

intersection_set = a.intersection(b)
print(intersection_set)

difference_set = a.difference(b)
print(difference_set)

symmetric_difference_set = a.symmetric_difference(b)
print(symmetric_difference_set)

is_subset = a.issubset(b)
print(is_subset)

a.update([2, 3, 4])
print(a)
