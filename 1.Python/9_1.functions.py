from math import *
print(sqrt(25))  # Output: 5.0

#we will learn now about user defined functions

# A function is a block of code that performs a specific task.

def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!


# A function can accept parameters or arguments.

def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alvi")  # Output: Hello, Alvi!


# A function can return a value using the return statement.

def add(a, b):
    return a + b

# Call the function and store the returned value in a variable
result = add(3, 5)
print(result)  # Output: 8

# A function can return multiple values using tuples.

def add_sub(a, b):
    return a + b, a - b

# Call the function and store the returned values in a tuple

result = add_sub(3, 5)
print(result)  # Output: (8, -2)

# Unpack the returned tuple
addition, subtraction = add_sub(3, 5)
print(addition)  # Output: 8
print(subtraction)  # Output: -2

# A function can have default parameters.

def greet(name="World"):
    print(f"Hello, {name}!")

# Call the function without an argument
greet()  # Output: Hello, World!

# Call the function with an argument
greet("Alvi")  # Output: Hello, Alvi!

# A function can accept a variable number of arguments using *args.

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# Call the function with multiple arguments
print(add(1, 2, 3))  # Output: 6

# Call the function with a list

numbers = [1, 2, 3]

print(add(*numbers))  # Output: 6

# A function can accept a variable number of keyword arguments using **kwargs.

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with multiple keyword arguments

greet(name="Alice", age=25)  # Output: name: Alice, age: 25

# Call the function with a dictionary

info = {"name": "Alice", "age": 25}

greet(**info)  # Output: name: Alice, age: 25

# A function can accept both positional and keyword arguments.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Call the function with positional arguments
greet("Alice", 25)  # Output: Hello, Alice! You are 25 years old.

# Call the function with keyword arguments
greet(name="Alice", age=25)  # Output: Hello, Alice! You are 25 years old.

# Call the function with a mix of positional and keyword arguments
greet("Alice", age=25)  # Output: Hello, Alice! You are 25 years old.