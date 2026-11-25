# Create a nested dictionary
students = {
    1: {"name": "Krishna", "marks": 85},
    2: {"name": "Durga", "marks": 90},
    3: {"name": "Ravi", "marks": 78}
}

# Print student names and marks
for i in students:
    print("Name:", students[i]["name"])
    print("Marks:", students[i]["marks"])
