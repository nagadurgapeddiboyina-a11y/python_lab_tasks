n = int(input("How many numbers? "))
largest = None

for i in range(n):
    num = int(input("Enter a number: "))

    if largest is None or num > largest:
        largest = num

print("Largest number:", largest)
