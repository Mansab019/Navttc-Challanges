# Task 8 - Find Area of Triangle (Heron's Formula)

a = 5
b = 6
c = 7

# Uncomment to take input from user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# Calculate semi-perimeter
s = (a + b + c) / 2

# Calculate area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
