# Task 22 - Tuple Data Type
# Reference: https://www.programiz.com/python-programming/tuple

coords = (10, 20, 30)

# Access
print(coords[0])
print(coords[-1])

# Slicing
print(coords[0:2])

# Tuple unpacking
x, y, z = coords
print(f"x={x}, y={y}, z={z}")

# Immutable - this would raise error:
# coords[0] = 99

# Count and Index
nums = (1, 2, 3, 2, 4, 2)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))
for pair in nested:
    print(pair)
