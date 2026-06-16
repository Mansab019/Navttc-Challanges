# Task 21 - List Data Type
# Reference: https://www.programiz.com/python-programming/list

fruits = ["apple", "banana", "cherry", "date"]

# Access
print(fruits[0])        # apple
print(fruits[-1])       # date

# Slice
print(fruits[1:3])      # ['banana', 'cherry']

# Add
fruits.append("mango")
fruits.insert(1, "blueberry")
print(fruits)

# Remove
fruits.remove("banana")
print(fruits)

# Loop
for fruit in fruits:
    print(fruit)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Sort
fruits.sort()
print("Sorted:", fruits)
