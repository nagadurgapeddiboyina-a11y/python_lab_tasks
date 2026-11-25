squares = {}

for i in range(1, 11):
    squares[i] = i * i

print("Squares:", squares)

even = {}

for i in range(1, 11):
    if i % 2 == 0:
        even[i] = i

print("Even numbers:", even)