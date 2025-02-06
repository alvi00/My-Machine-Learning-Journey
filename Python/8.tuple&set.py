marks=(10,20,30)
print(marks)  # Output: (10, 20, 30)
print(marks[0])  # Output: 10
print(marks[-1])  # Output: 30
print(marks.count(20))  # Output: 1
print(marks.index(20))  # Output: 1
# marks[0] = 5  # This will raise an error
# marks.append(40)  # This will raise an error
# because this is immutable

# Set
# Set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements from a set.
# Sets do not allow duplicate elements.
# Sets are defined using curly braces {}.
# You can create an empty set using set().
# You can create a set from a list using set(list_name).
# You can add elements to a set using the add() method.
# You can remove elements from a set using the remove() method.
# You can check if an element is present in a set using the in keyword.
# You can iterate over a set using a for loop.
# You can perform set operations like union, intersection, difference, and symmetric difference.
# You can use set comprehension to create a set.
# Here's an example of using sets in Python:
# Create a set of unique elements
fruits = {"apple", "banana", "cherry","cherry"}
print(fruits)  # Output: {'banana', 'apple', 'cherry'}

# Create an empty set
empty_set = set()
print(empty_set)  # Output: set()

# Create a set from a list
numbers = [1, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Add an element to the set
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Remove an element from the set
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# Check if an element is present in the set
print(2 in unique_numbers)  # Output: True

# Iterate over the set
for number in range(len(unique_numbers)):
    print(number)


#Iterating over a set with 2 step

for number in range(0,len(unique_numbers),2):
    print(number)


# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of two sets
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of two sets

print(set1 & set2)  # Output: {4, 5}

# Difference between two sets

print(set1 - set2)  # Output: {1, 2, 3}

# Symmetric difference between two sets

print(set1 ^ set2)  # Output: {1, 2, 3, 6, 7, 8}

# Set comprehension

squared_numbers = {x**2 for x in range(10)}
print(squared_numbers)  # Output: {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}



