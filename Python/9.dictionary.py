# Define a dictionary to store subjects and their corresponding marks
marks = {"english": 80, "math": 90, "science": 85}

# Print the entire dictionary
print(marks)  # Output: {'english': 80, 'math': 90, 'science': 85}

# Access the value associated with the key "math"
print(marks["math"])  # Output: 90

# Get the value of "science" using the get() method
print(marks.get("science"))  # Output: 85

# Attempt to get a non-existent key, returns None
print(marks.get("history"))  # Output: None

# Attempt to get a non-existent key with a default value
print(marks.get("history", "Not found"))  # Output: Not found

# Get all keys in the dictionary
print(marks.keys())  # Output: dict_keys(['english', 'math', 'science'])

# Get all values in the dictionary
print(marks.values())  # Output: dict_values([80, 90, 85])

# Get all key-value pairs in the dictionary
print(marks.items())  # Output: dict_items([('english', 80), ('math', 90), ('science', 85)])

# Check if a key exists in the dictionary
print("math" in marks)  # Output: True
print("history" in marks)  # Output: False

# Get the number of key-value pairs in the dictionary
print(len(marks))  # Output: 3

# Add a new key-value pair to the dictionary
marks["history"] = 75
print(marks)  # Output: {'english': 80, 'math': 90, 'science': 85, 'history': 75}

# Remove a key-value pair using pop()
marks.pop("math")
print(marks)  # Output: {'english': 80, 'science': 85, 'history': 75}

# Clear all key-value pairs in the dictionary
# marks.clear()
# print(marks)  # Output: {}

# Iterate over the dictionary and print key-value pairs
for key in marks:
    print(key, marks[key])

# Iterate over the dictionary using items()
for key, value in marks.items():
    print(key, value)

# Iterate over the dictionary using keys()
for key in marks.keys():
    print(key)

# Iterate over the dictionary using values()
for value in marks.values():
    print(value)

# Define a nested dictionary to store student information
student = {
    "name": "Alice",
    "class": 12,
    "subjects": {
        "math": 90,
        "science": 85
    }
}

# Print the nested dictionary
print(student)  # Output: {'name': 'Alice', 'class': 12, 'subjects': {'math': 90, 'science': 85}}

# Access nested dictionary values
print(student["subjects"]["math"])  # Output: 90
print(student["subjects"]["science"])  # Output: 85

# Add a new subject and mark to the nested dictionary
student["subjects"]["history"] = 75
print(student)  # Output: {'name': 'Alice', 'class': 12, 'subjects': {'math': 90, 'science': 85, 'history': 75}}

# Remove a key-value pair from the nested dictionary
student["subjects"].pop("math")
print(student)  # Output: {'name': 'Alice', 'class': 12, 'subjects': {'science': 85, 'history': 75}}

# Clear the nested dictionary inside "subjects"
student["subjects"].clear()
print(student)  # Output: {'name': 'Alice', 'class': 12, 'subjects': {}}

# Iterate over the nested dictionary
for key in student:
    if key == "subjects":
        # If the key is "subjects", iterate over its nested dictionary
        for subject in student[key]:
            print(subject, student[key][subject])
    else:
        print(key, student[key])

# Iterate over the nested dictionary using items()
for key, value in student.items():
    if key == "subjects":
        for subject, marks in value.items():
            print(subject, marks)
    else:
        print(key, value)

# Iterate over the nested dictionary using keys()
for key in student.keys():
    if key == "subjects":
        for subject in student[key]:
            print(subject, student[key][subject])
    else:
        print(key, student[key])

# Iterate over the nested dictionary using values()
for value in student.values():
    if isinstance(value, dict):
        for subject, marks in value.items():
            print(subject, marks)
    else:
        print(value)
