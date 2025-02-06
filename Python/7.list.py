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


marks.reverse()
#marks = [1, 2, 3, 4, 5] 

print(marks[0])  # Output: 5
print(marks[-1])  # Output: 1
print(marks[2:4])  # Output: [3, 2]

print(len(marks))  # Output: 5

print(2 in marks)  # Output: True

for i in marks[2:4]:  # Iterate over the list
    print(i)

# Nested for loop to print combinations of i and j
for i in range(3):  # Outer loop from 0 to 2
    for j in range(2):  # Inner loop from 0 to 1
        print(f"i={i}, j={j}")  # Prints the values of i and j for each combination

# Loop through the 'marks' list by index and print each index and corresponding value
marks = [80, 90, 85, 70]
for i in range(len(marks)):  # Loop over the length of the marks list
    print(f"i={i}, [{i}]={marks[i]}")  # Prints the index and value at that index

# Iterate through the 'students' list and break when "Fahim" is encountered
students = ["Alvi", "Shefa", "Fahim", "Okita"]
for i in range(len(students)):  # Loop over the students list by index
    if students[i] == "Fahim":  # If the student is "Fahim"
        break  # Exit the loop immediately when "Fahim" is found
    print(f"The students are {students[i]}")  # Print the student's name before "Fahim"

# Iterate through the 'students' list and skip "Fahim" using continue
students = ["Alvi", "Shefa", "Fahim", "Okita"]
for i in range(len(students)):  # Loop over the students list by index
    if students[i] == "Fahim":  # If the student is "Fahim"
        continue  # Skip this iteration and move to the next student
    print(f"The students are {students[i]}")  # Print the student's name excluding "Fahim"

# Create a new list 'new_student' by excluding "Fahim"
new_student = []  # Initialize an empty list to store students without "Fahim"
for i in range(len(students)):  # Loop over the students list by index
    if students[i] == "Fahim":  # If the student is "Fahim"
        continue  # Skip "Fahim" and do not add them to the new list
    new_student.append(students[i])  # Add other students to the new list

# Print the 'new_student' list with index and value
for i in range(len(new_student)):  # Loop through the new_student list
    print(f"i={i}, [{i}]={new_student[i]}")  # Print the index and student name from the new list
