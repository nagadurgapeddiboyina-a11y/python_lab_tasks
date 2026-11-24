from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: Square of numbers
square = list(map(lambda x: x * x, numbers))
print("Squares:", square)

# Filter: Even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# Reduce: Sum of numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)