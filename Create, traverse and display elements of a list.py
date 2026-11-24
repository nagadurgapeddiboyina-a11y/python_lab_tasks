n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

print("List elements:")

for i in lst:
    print(i)