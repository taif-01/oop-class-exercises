import numpy as np

# Given Score Array
score = np.array([85, 90, 78, 92, 88])

# (a) Convert the data type into float
score_float = score.astype(float)
print("Score as float:", score_float)

# (b) Create a copy of "score" named "a_score" and add 5 points on it
a_score = score.copy()
a_score += 5
print("Original Score:", score)
print("Updated a_score:", a_score)

# (c) Find shape, ndim, size, itemsize, dtype, and sorted array
print("Shape:", score.shape)
print("ndim:", score.ndim)
print("Size:", score.size)
print("Itemsize:", score.itemsize)
print("Dtype:", score.dtype)
print("Sorted Score:", np.sort(score))

# (d) Find the index of scores greater than 80
indexes = np.where(score > 80)
print("Indexes of scores greater than 80:", indexes[0])

# (e) Find min, max, std, var, sum, mean
print("Min:", np.min(score))
print("Max:", np.max(score))
print("Std Dev:", np.std(score))
print("Variance:", np.var(score))
print("Sum:", np.sum(score))
print("Mean:", np.mean(score))

# (f) Print score[::2], score[-3:-1], score[1:4]
print("score[::2]:", score[::2])
print("score[-3:-1]:", score[-3:-1])
print("score[1:4]:", score[1:4])
