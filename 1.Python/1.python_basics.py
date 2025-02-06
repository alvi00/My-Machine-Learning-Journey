# There are actually 5 types of variables in Python:
# 1. int
# 2. float
# 3. string
# 4. boolean
# 5. none

# print("Hello World")

# To get input from the user, we use the input() function
# name = input("Enter your name: ")
# print(name)

old_age = input("Enter your age: ")  # Get the age from the user as a string
new_Age = int(old_age) + 2  # Convert the input to an integer and add 2
print(new_Age)  # Print the new age after adding 2

first_number = input("Enter your first number")  # Get the first number from the user as a string
second_number = input("Enter your second number")  # Get the second number from the user as a string
result = int(first_number) + int(second_number)  # Convert both inputs to integers and sum them
print("The sum is ", result)  # Print the result of the sum
