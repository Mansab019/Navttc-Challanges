# Task 23 - String Data Type
# Reference: https://www.programiz.com/python-programming/string

name = "Mansab Ali"

# Basic operations
print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("Ali", "Ahmed"))

# Slicing
print(name[0:6])
print(name[::-1])   # Reverse

# Split and Join
words = name.split(" ")
print(words)
print(" | ".join(words))

# String formatting
age = 21
city = "Lahore"
print(f"My name is {name}, I am {age} years old from {city}.")

# Check methods
print("Mansab".startswith("Man"))
print("Mansab".endswith("ab"))
print("123".isdigit())
print("hello".isalpha())

# Strip
messy = "   hello world   "
print(messy.strip())
