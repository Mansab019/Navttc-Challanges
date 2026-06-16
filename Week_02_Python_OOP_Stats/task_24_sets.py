# Task 24 - Set Data Type
# Reference: https://www.programiz.com/python-programming/set

# Create a set (no duplicates)
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)   # apple appears only once

# Add and Remove
fruits.add("mango")
fruits.discard("banana")
print(fruits)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Membership
print(3 in a)
print(7 not in b)
