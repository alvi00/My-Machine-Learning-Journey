name = "Tony Stack"

# Converts the string to uppercase
print(name.upper())  # Output: TONY STACK

# Finds the index of the first occurrence of "Stack"
print(name.find("Stack"))  # Output: 5

# Replaces "Stack" with "Stark"
print(name.replace("Stack", "Stark"))  # Output: Tony Stark

# Splits the string into a list based on spaces
print(name.split(" "))  # Output: ['Tony', 'Stack']

# Checks if the string contains only alphabetic characters
print(name.isalpha())  # Output: False (since it contains a space)

# Checks if the string contains only digits
print(name.isdigit())  # Output: False

# Checks if the string contains only alphanumeric characters
print(name.isalnum())  # Output: False (due to the space)

# Checks if the string contains only whitespace characters
print(name.isspace())  # Output: False

# Checks if the string starts with "Tony"
print(name.startswith("Tony"))  # Output: True

# Checks if the string ends with "Stack"
print(name.endswith("Stack"))  # Output: True

# Counts occurrences of "t" in the string
print(name.count("t"))  # Output: 1

# Finds the index of the first occurrence of "S"
print(name.index("S"))  # Output: 5

# Capitalizes the first letter of the string
print(name.capitalize())  # Output: Tony stack

# Converts the first letter of each word to uppercase
print(name.title())  # Output: Tony Stack

# Swaps uppercase and lowercase letters
print(name.swapcase())  # Output: tONY sTACK

# Centers the string within a width of 20 characters
print(name.center(20))  # Output:   Tony Stack    

# Left-justifies the string within a width of 20 characters
print(name.ljust(20))  # Output: Tony Stack        

# Right-justifies the string within a width of 20 characters
print(name.rjust(20))  # Output:         Tony Stack

# Removes leading and trailing whitespace
print(name.strip())  # Output: Tony Stack

# Removes leading whitespace
print(name.lstrip())  # Output: Tony Stack

# Removes trailing whitespace
print(name.rstrip())  # Output: Tony Stack

# Fills the string with zeros up to a width of 20 characters
print(name.zfill(20))  # Output: 000000Tony Stack

# Formats the string (this method will do nothing in this case)
print(name.format())  # Output: Tony Stack

# Replaces placeholders in the string with "Tony" (will not work as expected here)
print(name.format_map("Tony"))  # Output: Tony Stack

# Encodes the string to bytes using the default encoding
print(name.encode())  # Output: b'Tony Stack'

# Converts the string to lowercase
print(name.casefold())  # Output: tony stack

# Expands tabs to spaces (not much effect here)
print(name.expandtabs(20))  # Output: Tony Stack

# Checks if "S" is in the string
print("S" in name)  # Output: True
