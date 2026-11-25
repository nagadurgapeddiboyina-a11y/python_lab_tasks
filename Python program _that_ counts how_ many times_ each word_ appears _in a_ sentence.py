# Create a dictionary
student = {
    "name": "Krishna",
    "age": 20,
    "course": "B.Tech"
}

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display items
print("Items:", student.items())

# Get a value
print("Name:", student.get("name"))

# Update dictionary
student.update({"age": 21})

# Remove an item
student.pop("course")

# Display updated dictionary
print("Updated Dictionary:", student)
