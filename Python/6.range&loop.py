num = range(5)  # Creates a range object from 0 to 4
print("Range object:", num)  # Output: range(0, 5)

# While loop: prints numbers from 0 to 4
i = 0
while i < 5:
    print(i)  # Output: 0, 1, 2, 3, 4
    i += 1

# For loop: prints numbers from 0 to 4
print("\nFor loop from 0 to 4:")
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# For loop: prints even numbers from 0 to 8
print("\nFor loop with step of 2:")
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8

# Reverse range: prints numbers from 5 to 1
print("\nFor loop with reverse range:")
for i in range(5, 0, -1):
    print(i)  # Output: 5, 4, 3, 2, 1

# Using range with starting point and step
print("\nFor loop with starting point 2 and step of 3:")
for i in range(2, 11, 3):
    print(i)  # Output: 2, 5, 8

# Looping through a list with range and len()
my_list = ["apple", "banana", "cherry"]
print("\nLooping through list with range and len:")
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")

# Nested loop: checking numbers from 0 to 2 and 0 to 1
print("\nNested loops:")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Using if-else with range
print("\nIf-else with range:")
for i in range(5):
    if i == 3:
        print(f"Found 3 at index {i}")
    else:
        print(f"Not 3: {i}")
        
# Checking if number is within a range
print("\nChecking if number is in range:")
number = 4
if number in range(5):  # Check if 4 is in the range 0 to 4
    print(f"{number} is in the range 0 to 4.")
else:
    print(f"{number} is not in the range 0 to 4.")

# Using else block with a for loop
print("\nFor loop with else block:")
for i in range(3):
    print(i)
else:
    print("Loop completed successfully.")
