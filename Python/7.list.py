marks = [1, 2, 3, 4, 5]  # Initialize a list
marks.append(6)  # Adds 6 to the end of the list
print(marks)  # Output: [1, 2, 3, 4, 5, 6]

marks.insert(2, 10)  # Inserts 10 at index 2
print(marks)  # Output: [1, 2, 10, 3, 4, 5, 6]

marks.remove(10)  # Removes the first occurrence of 10
print(marks)  # Output: [1, 2, 3, 4, 5, 6]

marks.pop()  # Removes the last element (6)
print(marks)  # Output: [1, 2, 3, 4, 5]

print(marks.index(4))  # Finds index of first occurrence of 4 (Output: 3)

print(marks.count(4))  # Counts occurrences of 4 in the list (Output: 1)

marks.sort()  # Sorts the list in ascending order
print(marks)  # Output: [1, 2, 3, 4, 5] (already sorted)

marks.reverse()  # Reverses the list
print(marks)  # Output: [5, 4, 3, 2, 1]

marks2 = marks.copy()  # Creates a copy of the list

# marks.clear()  # Uncommenting this would remove all elements from `marks`
# print(marks)  # Output: []

print(marks[0])  # Output: 5
print(marks[-1])  # Output: 1
print(marks[2:4])  # Output: [3, 2]

print(len(marks))  # Output: 5

print(2 in marks)  # Output: True

for i in marks[2:4]:  # Iterate over the list
    print(i)

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
